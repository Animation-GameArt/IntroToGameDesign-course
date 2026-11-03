---
title: GitHub Repository Setup — GAME 1303
course: GAME 1303
status: to-do
tags:
  - game1303
  - github
  - setup
  - instructor
---

# GitHub Repository Setup — GAME 1303

> [!abstract] Goal
> Set up GitHub so Claude can write and push the course scripts and documents, Marshall can test them in Unity, and students can start their projects from a single template.

---

## Recommended structure

| Item | Purpose |
|---|---|
| **GitHub organization** for the course | Keeps course material out of a personal account. Free; GitHub Education adds extras. |
| **`game1303-template`** | The Unity starter project. Mark it as a **Template repository** (Settings → General). Students start from this. |
| **`game1303-course`** | Schedule, design-doc templates (`.md` and `.docx`), tutorials and exercises. Packages are attached to **Releases**. Source for the website and Canvas. |

> [!tip] GitHub Classroom
> Make `game1303-template` a Classroom assignment. Each student gets their own private copy in one click, and you can see everyone's commits, which is handy for checking off exercises.

---

## Step-by-step

### 1. Create the organization and repositories
- [ ] Create the GitHub organization.
- [ ] Create `game1303-template`. Choose the **Unity** `.gitignore`.
- [ ] Create `game1303-course`.

### 2. Create the Unity project (Marshall, in Unity)
Unity generates `ProjectSettings/` and the URP setup, so these should not be hand-written.
- [ ] Unity Hub → New project → **Unity 6000.5**, **Universal 2D** template.
- [ ] Put the project inside the cloned `game1303-template` folder.
- [ ] Commit and push.

### 3. Connect Claude
- [ ] Send Claude the repository names, e.g. `org-name/game1303-template` and `org-name/game1303-course`.
- [ ] Claude attaches each repository to the session with push access.
- [ ] If access is denied, the error says what to fix. Usually: claude.ai **Settings → Connectors → GitHub**, and give the Claude GitHub app access to those repositories.

### 4. Claude builds; Marshall tests
- Claude commits and pushes:
  - `Packages/manifest.json` (Input System, Cinemachine, UI Toolkit, Timeline, 2D Tilemap Extras, etc.)
  - the folder layout (`Assets/_Course/`, `Assets/Scenes/Exercises/`)
  - the C# scripts and assembly definitions
  - Markdown tutorials and templates in `game1303-course`
- [ ] Marshall pulls, opens the project in Unity, and checks that it compiles and plays.
- [ ] Report any errors back to Claude for fixes.

### 5. Export and release packages (Marshall, in Unity)
`.unitypackage` files must be exported from the Editor.
- [ ] Assets → **Export Package** for each package (`Course_Core`, `Course_2D`, `Course_3D`, `Sandbox_2D`, `Sandbox_3D`, `Kit_<Genre>`, …).
- [ ] Attach the exports to a **GitHub Release** in `game1303-course`, with a version number such as `v1.0.0`.
- [ ] Students download from Releases, so the repository stays light and every version is kept.

### 6. Publish to students
- [ ] Copy tutorials and templates into Canvas assignments.
- [ ] Publish the Obsidian notes to the course website.
- [ ] Share the template link or Classroom assignment link.

---

## Who does what

| Task | Marshall | Claude |
|---|:---:|:---:|
| Create organization and repositories | ✅ | |
| Create Unity project from the Universal 2D template | ✅ | |
| Connect GitHub access | ✅ | |
| Write the package list, folders, scripts, assembly definitions | | ✅ |
| Write tutorials, exercises and templates | | ✅ |
| Compile and play-test in Unity | ✅ | |
| Fix reported errors | | ✅ |
| Export `.unitypackage` files and create Releases | ✅ | |
| Publish to Canvas and the website | ✅ | |

---

## Notes
- Course scripts install under `Assets/_Course/` so they never collide with students' own files.
- To update a package, students re-import the same `.unitypackage`; it overwrites in place.
- Consider **Git LFS** in `game1303-template` if the sandbox art and audio grow large.
