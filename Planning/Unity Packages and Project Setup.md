---
title: "Unity Packages and Project Setup"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.23.0
unity: 6000.3.10f1
tags:
  - game1303
  - instructor
  - planning
---

# Unity Packages and Project Setup

**For instructors.** Every Unity package the course project uses, how to install each one (Yarn Spinner is installed differently from the rest), the project settings that aren't packages, and how to rebuild the course project from scratch with the course's own `.unitypackage` files.

The course project already has all of this. You need this page only to set up a **new** project: a fresh start, a new Unity version, or using the course scripts somewhere else.

## Unity

**Unity 6000.3.10f1**, from Unity Hub, with these modules (Unity Hub → Installs → ⚙ → **Add modules**):

| Module | Why |
|---|---|
| Web Build Support | Web builds for itch.io (every milestone) |
| Windows Build Support (Mono) | Windows builds from a Mac (included on Windows) |
| Mac Build Support (Mono) | Mac builds from Windows (included on a Mac) |

New projects start from the **Universal 2D** template (URP).

## Packages

The packages the course adds, or relies on, beyond what the Universal 2D template brings:

| Package | Version | Source | Used by | How to install |
|---|---|---|---|---|
| **Input System** (`com.unity.inputsystem`) | 1.18.0 | Unity Registry (in the template) | Core: the Input Reader and every controller | Already there. Check **Project Settings → Player → Active Input Handling** is **Input System Package (New)** |
| **Cinemachine** (`com.unity.cinemachine`) | 3.1.7 | Unity Registry | Core and every kit's camera; the 2.5D tutorials | Package Manager → Unity Registry → Cinemachine → Install |
| **Splines** (`com.unity.splines`) and **Mathematics** (`com.unity.mathematics`) | 2.8.3 and 1.3.3 | Installed with Cinemachine | The 3D module (Rail Runner 3D) | Nothing to do: Cinemachine brings them |
| **Yarn Spinner** (`dev.yarnspinner.unity`) | 3.3.2 | **OpenUPM** (a scoped registry) | The Visual Novel kit | See **Installing Yarn Spinner** below |
| **AI Navigation** (`com.unity.ai.navigation`) | 2.0.16 | Unity Registry | The Stealth kit (baking NavMeshes) | Package Manager → Unity Registry → AI Navigation → Install |
| **2D Tilemap Extras** (`com.unity.2d.tilemap.extras`) | 6.0.1 | Unity Registry (in the template) | Exercise 04 and the kits' tilemaps | Already there |
| **Timeline** (`com.unity.timeline`) | 1.8.10 | Unity Registry (in the template) | The *Cutscenes with Timeline* topic | Already there |
| **uGUI** (`com.unity.ugui`), which includes TextMeshPro | 2.0.0 | Built in | Core (TextMeshPro, for Floating Text and Variable Label) | Already there |

The rest of `Packages/manifest.json` (2D Animation, Aseprite and PSD importers, Sprite Shape, the IDE packages, Visual Scripting, Test Framework, Multiplayer Center, and the built-in modules) comes with the template. The course doesn't depend on them, but there's no need to remove them.

To install a Unity Registry package by name: **Window → Package Manager → + → Install package by name…**, and type the name in brackets above, such as `com.unity.cinemachine`, with the version.

### Installing Yarn Spinner

Yarn Spinner isn't in the Unity Registry. Its free version comes from **OpenUPM**, an open registry that Unity has to be told about first. It's the route Yarn Spinner's own documentation recommends.

**1. Add the registry.**
1. **Edit → Project Settings → Package Manager.**
2. Under **Scoped Registries**, click **+** and fill in:
   - **Name:** `OpenUPM`
   - **URL:** `https://package.openupm.com`
   - **Scope(s):** `dev.yarnspinner`
3. Click **Save** (or **Apply**).

**2. Install the package.**
1. **Window → Package Manager.**
2. In the list on the left, choose **My Registries**.
3. Select **Yarn Spinner**, choose version **3.3.2**, and click **Install**. The first import takes a few minutes.

Unity shows **"This package has no signature."** Packages from outside Unity's own registry always show this; it's expected and safe.

**If Scoped Registries is hard to find,** edit `Packages/manifest.json` in a text editor instead. Add this beside `"dependencies"`, and add `"dev.yarnspinner.unity": "3.3.2"` inside `"dependencies"`:

```json
"scopedRegistries": [
  {
    "name": "OpenUPM",
    "url": "https://package.openupm.com",
    "scopes": [ "dev.yarnspinner" ]
  }
]
```

Save it, and Unity installs Yarn Spinner when it next has focus. Mind the commas between blocks.

The paid versions (Asset Store, itch.io) add Text Animator and support. The kit doesn't need them.

**Students don't install anything:** the registry and the package are saved in `Packages/manifest.json`, so every copy of the course project already has Yarn Spinner.

## Project settings that aren't packages

These live in `ProjectSettings/` or `Assets/Settings/`, not in packages, so a new project needs them set by hand.

| Setting | Where | Value |
|---|---|---|
| Active Input Handling | Project Settings → Player → Other Settings | **Input System Package (New)** |
| Renderers | `Assets/Settings/UniversalRP` asset → **Renderer List** | Index 0: the **2D Renderer** (the template's; the default). Index 1: a **Universal Renderer** (**Create → Rendering → URP Universal Renderer**), for 3D scenes. 3D scenes pick it on their camera (**Rendering → Renderer**) |
| Tags | Project Settings → Tags and Layers | Add `Enemy` (used by the kits' attacks and projectiles). `Player` is built in |
| Company and Product Name | Project Settings → Player | Your name, the game's title |

## The course's own packages

All the course scripts, in `.unitypackage` files, so they can go into any Unity 6 project without the GitHub repository:

| Package | Contents | Needs |
|---|---|---|
| `CollinGame-Core-<version>` | Core (variables, events, health, UI, input, saving, audio, editor tools), the 2D and 3D modules, the course credits | Input System, Cinemachine (with Splines), TextMeshPro |
| `CollinGame-Kit-<Kit>-<version>` (fifteen) | One kit each: scripts, UI and its sample (once built) | CollinGame-Core, and the Kenney art its sample uses. The Visual Novel kit needs Yarn Spinner; the Stealth kit, AI Navigation |
| `Kenney-<pack>` (twelve, plus audio) | One Kenney art pack each, with the course's import settings | Nothing. CC0: free to use and share |

**Only Core is shared.** Each kit depends only on Core (and the 2D or 3D module inside it), never on another kit, so any one kit can be imported alone.

| Kit | Kenney packs its sample uses |
|---|---|
| Platformer, Endless Runner | Pixel Platformer |
| Physics Puzzle | Physics Assets |
| Top-Down Adventure | Tiny Dungeon, Tiny Town |
| Turn-Based Battle, Visual Novel | Tiny Dungeon |
| Arcade Classic | Puzzle Pack 2, Space Shooter Remastered |
| Top-Down Shooter | Pixel Shmup |
| Grid Puzzle | Sokoban |
| Tower Defense | Tower Defense (top-down) |
| Management | Tiny Town |
| Farming | Tiny Town, Tiny Dungeon |
| Card Game | Playing Cards, Tiny Dungeon |
| 3D Platformer, Stealth | None (Unity's basic shapes) |

### Importing them

Import in this order: **Core first**, then any art packs, then kits. Double-click each package with the project open, and click **Import**. Everything lands in `Assets/_Course`, with the same GUIDs as the course project, so prefabs and samples keep their references.

### Making them

Remake the packages whenever the course project changes, for a release:

- **In Unity:** **Collin Game → Packages → Export Course Packages…**, and choose a folder. Unity exports Core, each kit and each art pack.
- **Without Unity:** from the course repository, `python3 tools/make_unitypackages.py <template project folder> <output folder>`. It builds the same packages straight from the files and their `.meta` files.

Either way, attach them to a **GitHub Release** of the template repository, where the kit guides tell students to download kits.

## Setting up a new project from scratch

1. In Unity Hub, **New project → Universal 2D**, Unity 6000.3.10f1.
2. Install **Cinemachine** and **AI Navigation** from the Unity Registry, and **Yarn Spinner** from OpenUPM (above).
3. Set **Active Input Handling**, add the **Universal Renderer** to the Renderer List, and add the `Enemy` tag (above).
4. Import `CollinGame-Core`, then the Kenney art packs, then the kits you want.
5. Run **Collin Game → Art → Reapply Art Import Settings**, and **Collin Game → UI → Use Course Panel Settings in Open Scenes** in each scene with UI.
6. Open a kit's menu scene and press **Play**.
