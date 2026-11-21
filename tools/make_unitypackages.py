"""Builds the course's .unitypackage files from the template project, without Unity.

    python3 tools/make_unitypackages.py <path to the template project> <output folder>

A .unitypackage is a gzipped tar file with one folder per asset, named by the
asset's GUID, holding `asset` (the file), `asset.meta` and `pathname`. Because
the GUIDs come from the project's own .meta files, everything imported from
these packages keeps its references (a prefab still finds its script, a kit
still finds the Core scripts).

The packages, and what each needs, are listed in PACKAGES and ART below. Keep
them in step with Core/Editor/CoursePackageExporter.cs, which makes the same
packages from inside Unity.
"""
import io
import os
import sys
import tarfile
import time

COURSE = "Assets/_Course"

# name: (folders and files to include, a one-line description)
PACKAGES = {
    "CollinGame-Core": (
        [f"{COURSE}/Core", f"{COURSE}/TwoD", f"{COURSE}/ThreeD", f"{COURSE}/Credits",
         f"{COURSE}/README.md", f"{COURSE}/VERSION.txt", f"{COURSE}/Art/Kenney/README.md"],
        "Core scripts, UI, input, data, editor tools, and the 2D and 3D modules. Every kit needs it",
    ),
}

KITS = {
    # folder: (package name, Kenney packs its sample uses)
    "Platformer": ("Platformer", ["kenney_pixel-platformer"]),
    "PhysicsPuzzle": ("PhysicsPuzzle", ["kenney_physics-assets"]),
    "TopDownAdventure": ("TopDownAdventure", ["kenney_tiny-dungeon", "kenney_tiny-town"]),
    "TurnBasedBattle": ("TurnBasedBattle", ["kenney_tiny-dungeon"]),
    "ArcadeClassic": ("ArcadeClassic", ["kenney_puzzle-pack-2", "kenney_space-shooter-remastered"]),
    "TopDownShooter": ("TopDownShooter", ["kenney_pixel-shmup"]),
    "EndlessRunner": ("EndlessRunner", ["kenney_pixel-platformer"]),
    "GridPuzzle": ("GridPuzzle", ["kenney_sokoban-pack"]),
    "TowerDefense": ("TowerDefense", ["kenney_tower-defense-top-down"]),
    "Management": ("Management", ["kenney_tiny-town"]),
    "Farming": ("Farming", ["kenney_tiny-town", "kenney_tiny-dungeon"]),
    "VisualNovel": ("VisualNovel", ["kenney_tiny-dungeon"]),
    "CardGame": ("CardGame", ["kenney_playing-cards-pack", "kenney_tiny-dungeon"]),
    "Platformer3D": ("Platformer3D", []),
    "Stealth": ("Stealth", []),
}

for folder, (name, art) in KITS.items():
    PACKAGES[f"CollinGame-Kit-{name}"] = ([f"{COURSE}/Kits/{folder}"], f"The {name} kit. Needs CollinGame-Core")

ART_ROOT = f"{COURSE}/Art/Kenney"


def guid_of(meta_path):
    with open(meta_path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("guid:"):
                return line.split(":", 1)[1].strip()
    raise ValueError(f"No guid in {meta_path}")


def collect(project, roots):
    """Every asset under the roots, plus their parent folders, as project-relative paths."""
    found = []

    def add(rel):
        if rel not in found:
            found.append(rel)

    for root in roots:
        full = os.path.join(project, root)
        if not os.path.exists(full):
            print(f"  (skipped, not found: {root})")
            continue

        # Parent folders, so they're created with their own GUIDs.
        parts = root.split("/")
        for i in range(2, len(parts)):
            add("/".join(parts[:i]))

        add(root)

        if os.path.isdir(full):
            for dirpath, dirnames, filenames in os.walk(full):
                dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
                for d in dirnames:
                    add(os.path.relpath(os.path.join(dirpath, d), project).replace(os.sep, "/"))
                for name in sorted(filenames):
                    if name.endswith(".meta") or name.startswith("."):
                        continue
                    add(os.path.relpath(os.path.join(dirpath, name), project).replace(os.sep, "/"))

    return found


def add_bytes(tar, name, data, mtime):
    info = tarfile.TarInfo(name)
    info.size = len(data)
    info.mtime = mtime
    info.mode = 0o644
    tar.addfile(info, io.BytesIO(data))


def write_package(project, out_path, roots):
    assets = collect(project, roots)
    mtime = int(time.time())
    count = 0

    with tarfile.open(out_path, "w:gz", format=tarfile.GNU_FORMAT) as tar:
        for rel in assets:
            full = os.path.join(project, rel)
            meta = full + ".meta"

            if not os.path.exists(meta):
                print(f"  (no .meta, skipped: {rel})")
                continue

            guid = guid_of(meta)
            add_bytes(tar, f"{guid}/pathname", rel.encode("utf-8"), mtime)

            with open(meta, "rb") as f:
                add_bytes(tar, f"{guid}/asset.meta", f.read(), mtime)

            if os.path.isfile(full):
                with open(full, "rb") as f:
                    add_bytes(tar, f"{guid}/asset", f.read(), mtime)

            count += 1

    return count


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    project, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    version = open(os.path.join(project, COURSE, "VERSION.txt")).read().strip()
    rows = []

    for name, (roots, description) in PACKAGES.items():
        path = os.path.join(out, f"{name}-{version}.unitypackage")
        count = write_package(project, path, roots)
        rows.append((name, count, os.path.getsize(path), description))

    # One art package per Kenney pack, and one for the audio.
    art_dir = os.path.join(project, ART_ROOT)
    for pack in sorted(os.listdir(art_dir)):
        if os.path.isdir(os.path.join(art_dir, pack)):
            name = f"Kenney-{pack.replace('kenney_', '')}"
            path = os.path.join(out, f"{name}.unitypackage")
            count = write_package(project, path, [f"{ART_ROOT}/{pack}"])
            rows.append((name, count, os.path.getsize(path), "Kenney art (CC0), with the course's import settings"))

    for name, count, size, _ in rows:
        print(f"{name:42} {count:5} assets {size / 1_000_000:7.1f} MB")


if __name__ == "__main__":
    main()
