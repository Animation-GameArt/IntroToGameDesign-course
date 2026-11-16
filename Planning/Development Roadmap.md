---
title: Development Roadmap
course: GAME 1303 — Intro to Game Design
status: in progress
tags:
  - game1303
  - planning
  - roadmap
  - instructor
---

# Development Roadmap

What is built, what is left, the order to build it in, and the decisions that block the next steps.

## Where things stand

| Piece | State |
|---|---|
| Schedule, teaching philosophy, design-doc templates | Written |
| Template project with Core and 2D scripts (v0.7.0) | Written. Ex 01–02 tested in Unity; Ex 03–06 scripts not yet tested |
| Exercise tutorials Ex 01–06 (two versions of Ex 05) | Drafted. Ex 01–02 tested |
| Class and Lecture pages, weeks 1–7 | Drafted |
| Canvas HTML copies, rebuilt automatically | Working |
| Ex 00 tutorial | Not started |
| Genre map page for students | Drafted (`Guides/Genre Map.md`) |
| Genre kits and kit guides | Not started |
| Scripts for weeks 8–10 (audio, juice, cutscenes, dialogue, saving, settings) | Not started |
| Class and Lecture pages, weeks 8–16 | Drafted |
| Topic pages | Not started. Needs a sample |
| Assignment pages and rubrics | Weeks 8–16 drafted (seven milestone pages, points to be assigned). Weeks 1–7 not started |
| Per-game scripts and guides | After pitch week |

## Order of work

### Phase 1 — Finish the sandbox (weeks 1–7 material)

- [ ] Test Ex 03, 04, 05 (both versions) and 06 in Unity, in order. Fix what breaks.
- [ ] Write the Ex 00 tutorial (install, practice project, Editor tour).
- [ ] Move the reference solutions to `Assets/_Course/Exercises/Solutions/`.
- [ ] Match the Week 5–7 lecture pages to the real script names.

### Phase 2 — What students need before they pitch

- [x] Decide the supported genre list (decision 1).
- [x] **Genre Map** page, drafted in `Guides/Genre Map.md`: for each genre, the core loop, example games, what the kit provides, a sensible scope for eight weeks, and what is out of scope.
- [ ] Assignment pages: Three game ideas, Pitch, One-sheet, Screen layout, Ten-pager draft and final.
- [ ] A pitch format that names the genre from the map and lists the game's mechanics, so each pitch can be checked against its kit.

### Phase 3 — Genre kits

One kit at a time, in priority order. For each kit:

1. Scripts, in `Assets/_Course/Kits/<Genre>/`, with their own assembly. They depend on Core and never change it.
2. A **kit guide** in Markdown that builds the kit's sample game step by step.
3. The instructor follows the guide in Unity. That tests the scripts and the guide, and the result becomes the kit's sample.
4. The kit is exported as its own `.unitypackage`: scripts, sample scene, prefabs and data.

**Build order** (fourteen kits; visual novel and dating sim share one):

1. Small, and they settle the kit format: platformer (scripts and guides written; the sample needs building and testing), top-down adventure, turn-based battle, arcade classic
2. Medium: top-down shooter, endless runner, grid puzzle, tower defense, management and strategy, visual novel with dating sim
3. The 3D template project and 3D script module, then the 3D platformer kit
4. Large: card game, farming and life sim, horror and stealth

Kits aren't used until week 8 of the semester, so the later ones can be finished during weeks 1–7.

**Kenney packs to try first** (to be confirmed as each kit is built):

| Kit | Pack |
|---|---|
| Platformer | Pixel Platformer (in the template) |
| Top-down adventure | Tiny Dungeon, Tiny Town |
| Top-down shooter | Pixel Shmup, or Space Shooter Redux |
| Grid puzzle | Sokoban |
| Tower defense | Tower Defense (top-down) |
| Card game | Playing Cards Pack |
| Menus and HUD | UI Pack |
| Sound effects | Interface Sounds, Impact Sounds |
| 3D kits | Platformer Kit, Prototype Textures |


### Phase 4 — Weeks 8–16

- [ ] Scripts for Lectures 8–10: audio, camera shake and feedback, Timeline cutscenes, dialogue, saving, settings, builds.
- [x] Class and Lecture pages for weeks 8–16.
- [ ] Exercise tutorials Ex 07–10. The class pages assume them (decision 5, still to be confirmed): Juice & Audio, Save & Build, Debug & Profile, Playtest.
- [x] Assignment pages: Production Backlog, First Playable, Sprint Review, Alpha, Beta, Gold, Post-Mortem. The first build moved into Ex 08 and the playtest report into Ex 10.
- [ ] Topic pages (decision 6).

### Phase 5 — Release

- [ ] Keep kits, art packs and exercise solutions out of the student project ZIP. They stay in the repository for development; a `.gitattributes` file with `export-ignore` lines leaves them out of GitHub's ZIP downloads, and each kit is exported as its own package.
- [ ] Update Exercise 06 to use the shared `CoursePanelSettings` asset, once it exists.

- [ ] Assign points to every exercise and assignment (decision 7).
- [ ] Tag v1.0, publish the Release, export the update and kit packages.
- [ ] Test the whole student path on a lab computer.

### Phase 6 — After pitch week (during the semester)

- [ ] Compare each approved pitch with its kit, and list what the kit doesn't cover.
- [ ] Write per-game scripts into `Assets/_Course/Games/<GameName>/`, within the agreed limit (decision 8).
- [ ] Write a short guide for each game.

## Decisions needed

| # | Decision | Recommendation | Blocks |
|---|---|---|---|
| 1 | Which genres are on the map for the first semester | **Decided:** fifteen genres. 2D: arcade classic, platformer, top-down adventure, turn-based battle, endless runner, top-down shooter, grid puzzle, tower defense, management and strategy, card game, farming and life sim. Narrative: visual novel, dating sim (one kit). 3D: 3D platformer, horror and stealth. No VR or AR. Lectures and exercises stay 2D | — |
| 2 | Art in kit samples | **Decided:** Kenney's CC0 packs, kept under `Assets/_Course/Art/Kenney/` in a folder named as Kenney's download is named (for example `kenney_pixel-platformer`), with the pack's license file. Each pack gets an entry in `CourseArtImporter`, which sets its import settings. Every pack is listed in `Course Credits`, which the game's Credits screen shows. Plain shapes stay in the exercises | — |
| 3 | How each kit's sample is built | The instructor builds it by following the kit guide, as with the exercises | Instructor time per kit |
| 4 | Dialogue tool | **Decided:** Yarn Spinner. To be installed from a package registry and not from a Git URL, so lab computers don't need Git | — |
| 5 | Are there graded exercises in weeks 8–10? | Yes: three short exercises done inside the student's own game (feedback and audio; saving and a build; a bug list and profiling) | Weeks 8–10 pages, point totals |
| 6 | What a Topic page is | Needs a sample from the current course | Topic pages |
| 7 | Point scale, and the current checklist and grade sheet | Needs the current documents | Assignment pages, rubrics |
| 8 | Limit on per-game custom scripts | A fixed number per student, such as two or three small scripts, agreed at pitch approval | Scope of Phase 6 |
| 9 | Does Game & Simulation Group Project start from the same template project? | **Decided:** yes. It uses the same template scripts, with kits imported as needed | — |

## Open risks

- **Untested code is stacked up.** Ex 03–06 depend on each other. A problem in Ex 03 may change the later ones.
- **Each kit costs instructor testing time.** The kit count in decision 1 should match the time available before the semester.
- **The Unity Version Control allowance for students** is still unconfirmed.
- **The 3D template and the Unreal section** are both deferred until the 2D Unity course is complete.
