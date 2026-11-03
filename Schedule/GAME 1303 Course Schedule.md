---
title: GAME 1303 — Course Schedule
course: GAME 1303 Game Development
weeks: 16
unity: 6000.5+
tags:
  - game1303
  - schedule
  - syllabus
---

# GAME 1303 — Course Schedule

> [!info] How this course works
> - **Weeks 1–10:** a lecture each week, paired with a lab.
> - **Weeks 1–7:** each lab builds one step of a small **sandbox game** in your chosen track (2D or 3D). The sandbox uses the same course scripts you will use in your own game.
> - **Weeks 11–15:** studio weeks, where you build, playtest and debug your own game.
> - **Week 16:** post-mortem presentations.
>
> **No more than one project item is due each week.** Exercises are finished and checked off **in lab**, then committed to your repository. They are not separate homework submissions.

---

## Tracks

| Track | Sandbox game | Use it if your game is… |
|---|---|---|
| **2D** | A small "collect and escape" platformer / top-down game | 2D platformer, top-down, shooter, puzzle, tactics, visual novel, card game |
| **3D** | A third-person collect-a-thon | 3D, 2.5D (isometric or side-scrolling with 3D art) |

> [!note] VR and AR
> VR and AR games need instructor approval. These students complete the **3D** track first, then add the XR module.

---

## Exercise scenes

Each exercise is its own scene in `Assets/Scenes/Exercises/`. When an exercise builds on the previous week, open last week's scene and use **File → Save As…** with the new name, so every week's work is kept.

| # | Scene file | Builds on |
|---|---|---|
| 00 | `Ex00_Setup.unity` | — |
| 01 | `Ex01_Bootstrap.unity` | Ex00 |
| 02 | `Ex02_Events.unity` | Ex01 |
| 03 | `Ex03_Player.unity` | Ex02 |
| 04 | `Ex04_Level.unity` | Ex03 |
| 05 | `Ex05_Combat.unity` | Ex04 |
| 06 | `Ex06_UI.unity` | Ex05 — **sandbox complete** |

> [!tip] Starting your own game early
> Once your pitch is approved (week 3), you may repeat each exercise directly in your own game's scenes as well. Your game and the sandbox share one project and one set of course scripts, so they will not conflict.

---

## Week-by-week schedule

### Phase 1 — Foundations

| Wk | Lecture | Lab exercise (checked off in lab) | Due this week |
|---|---|---|---|
| 1 | **L1 · Games, Genres & the Industry.** What makes a game, core loops, the genre map (2D / 3D / 2.5D / VR / AR / narrative), roles and studios, indie vs. AAA | **Ex00 · Setup:** install Unity 6000.5, create your project, import the course packages, choose a track, enter Play mode | **Three game ideas** (one-line pitches) |
| 2 | **L2 · Pitching, Scope & Project Management.** How to pitch, scoping to 13 weeks, Git and GitHub, task boards | **Ex01 · Bootstrap:** Git repository, Bootstrapper, SceneLoader, first commit | **Repository link** |
| 3 | **Pitch Day**, then **L3 · Unity Fundamentals.** GameObjects, components, prefabs, the script lifecycle, ScriptableObjects, Console and breakpoints | **Ex02 · Events:** event channels, SO variables, a collectible and a score counter | **Pitch presentation** |
| 4 | **L4 · Input & Game Feel.** The Input System, control schemes, game feel (coyote time, jump buffering, acceleration). Writing a one-sheet | **Ex03 · Player:** InputReader and the player controller for your track | **One-sheet** |
| 5 | **L5 · Level Design & Cameras.** Pacing, teaching through the level, Tilemaps (2D) or ProBuilder (3D), Cinemachine. Writing a ten-pager | **Ex04 · Level:** build a short level, camera follow and bounds, hazards, checkpoints | — |
| 6 | **L6 · Game Systems & AI.** Health and damage, pickups, object pooling, spawners, state machines, simple enemy AI | **Ex05 · Combat:** a patrolling enemy, damage, a spawner, respawning | **Ten-pager draft** (peer review) |
| 7 | **L7 · UI & UX.** UI Toolkit screens and HUD, diegetic vs. screen UI, world-space text, menus and pause | **Ex06 · UI:** main menu, pause, HUD, damage popups. **Sandbox complete** | **Ten-pager (final)** |

### Phase 2 — Your Game

| Wk | Lecture | Lab (in your own game) | Due this week |
|---|---|---|---|
| 8 | **L8 · Juice, Audio & Storytelling.** Feedback, screen shake, sound design, Timeline cutscenes, dialogue | Audio, camera shake, a cutscene or dialogue in your game | **Production backlog** (task board built from your ten-pager) |
| 9 | **L9 · Saving, Builds & Playtesting.** Save systems, settings, building for Windows/WebGL, publishing to itch.io, running a playtest | Save/load, settings menu, first build | **First build** (private itch.io page) |
| 10 | **L10 · Debugging, Profiling & Production.** Finding and fixing bugs, the Profiler, bug triage, cutting scope, milestones | Profile your game, set up a bug list | **First Playable** |

### Phase 3 — Studio

| Wk | Focus | Due this week |
|---|---|---|
| 11 | Core loop complete; stand-ups and bug triage | **Sprint review** (core loop) |
| 12 | All features in, even if rough | **Alpha** |
| 13 | Cross-team playtesting; turn feedback into tasks | **Playtest report** |
| 14 | All content in; polish and bug fixing | **Beta** |
| 15 | Final fixes, store page, release | **Gold** (public itch.io release) |

### Week 16 — Post-Mortem

| Wk | Activity | Due this week |
|---|---|---|
| 16 | Post-mortem presentations: what went right, what went wrong, what you'd change, planned scope vs. final game | **Post-mortem** |

---

## Milestone definitions

| Milestone | Definition |
|---|---|
| **One-sheet** | A one-page summary of your game for an approval meeting. Template: `One-Sheet Template` |
| **Ten-pager** | A ten-page design document covering the whole game. Template: `Ten-Pager Template` |
| **Production backlog** | Every feature from your ten-pager, broken into tasks on your task board, with a week assigned |
| **First build** | Your game builds and runs outside the Editor and is uploaded to a private itch.io page |
| **First Playable** | One complete pass through your core loop: the player can start, play, and win or lose |
| **Sprint review** | The core loop is complete and feels right, demonstrated in class |
| **Alpha** | Every feature exists and works, even if the art, audio and balance are placeholders |
| **Playtest report** | Notes from at least three outside playtesters, and the tasks you created from their feedback |
| **Beta** | All content is in. From here on, only bug fixes and polish |
| **Gold** | The finished game, publicly released on itch.io with a store page |
| **Post-mortem** | A presentation reviewing the project honestly |
