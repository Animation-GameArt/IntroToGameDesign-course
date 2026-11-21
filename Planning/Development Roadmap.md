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
| Template project (v0.19.0): Core, 2D, 3D, and eleven kits | Compiles with no errors (checked through the Tower Defense kit, 2026-11-20; Management and Farming kits not yet compiled). Kits and 3D scripts not yet tested in Play mode |
| Exercise tutorials Ex 00–10 (two versions of Ex 05) | Drafted. Ex 01–04 tested |
| Class and Lecture pages, weeks 1–7 | Drafted |
| Canvas HTML copies, rebuilt automatically | Working |
| Ex 00 tutorial | Drafted |
| Script Reference (`Guides/Script Reference.md`) | Written for v0.19.0. Update whenever scripts change |
| Genre map page for students | Drafted (`Guides/Genre Map.md`) |
| Genre kits and kit guides | Platformer, Physics Puzzle, Top-Down Adventure, Turn-Based Battle, Arcade Classic, Top-Down Shooter, Endless Runner, Grid Puzzle, Tower Defense, Management and Farming: scripts and both guides written. Platformer sample built with its menu command (2026-11-20), not yet played through; other samples not built. Other 4 kits not started |
| Scripts for weeks 8–10 (v0.10.0) | Audio, music, camera shake, hit stop, cutscenes, saving, high score and settings. Compiled; not yet tested in Ex 07–10. Dialogue is part of the visual novel kit |
| 3D module and 2.5D tutorials | Tank Controller 3D, Rail Runner 3D, two tutorials. Universal Renderer added. Compiles; not yet tested |
| Class and Lecture pages, weeks 8–16 | Drafted |
| Topic pages | All 16 weeks drafted (54 pages) |
| Assignment pages and rubrics | All 14 drafted, plus Extra Credit. Points assigned (100, plus up to 5 extra credit; table in the schedule) |
| Per-game scripts and guides | After pitch week |

## Next steps: who does what

### Marshall (needs Unity, the lab, or an account)

Every test, with each guide's checks in order, is in the **[Testing Checklist](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Planning/Testing%20Checklist.md)**. Tick items there as they pass.

**First — unblocks everything else (about 15 minutes):**

- [x] **Compile check.** Done 2026-11-20: no errors; two warnings, fixed. Pull the template (v0.13.0), open it, and send Claude every red error in the Console. Any compile error, even in a kit, stops Play mode for the whole project, so nothing else can be tested until the Console is clean.

**Then, in any order:**

- [ ] **Test the exercises** not yet tested: Ex 00, Ex 05 (both versions), Ex 06, Ex 07–10. Report what breaks.
- [ ] **Test the 2.5D tutorials** 1 and 2.
- [x] **Download the Kenney packs** (2026-11-20): Tiny Dungeon, Tiny Town, Physics Assets, Puzzle Pack 2, Space Shooter Remastered, Pixel UI Pack and ten sound packs. Pixel Shmup and Sokoban added the same day. Still to download for later kits: Tower Defense (top-down) and Playing Cards Pack.
- [ ] **Test the first sample builder:** **Collin Game → Kit Samples → Build Platformer Sample**, then play it through Part 10 of the Platformer "Building the Sample" guide. Once it works, Claude writes the same command for the other four kits.
- [ ] **Decisions 3 and 8** below.

**Before the semester:**

- [ ] Spring software request: Unity 6000.3.10f1 and Unity Hub (see Teaching Philosophy, section 7).
- [ ] Confirm what a student's Unity Version Control account gets, and that it works on lab computers.
- [ ] Test the whole student path on a lab computer: download the Release ZIP, unzip, open, import an update.
- [ ] Tag v1.0, publish the Release, and export the update and kit packages.
- [ ] Copy the Canvas HTML into Canvas, and set up the Three Game Ideas and Pitch Discussions.
- [ ] Publish the Obsidian notes to the course website.

### Claude (can start now)

- [x] Script Reference: add the 3D module.
- [x] Sample builder for the Platformer Kit.
- [ ] Sample builders for Physics Puzzle, Top-Down Adventure, Turn-Based Battle and Arcade Classic (after the Platformer one is tested; those three also need their Kenney packs).
- [x] Top-down shooter kit: scripts and both guides (v0.14.0).
- [x] Endless runner kit: scripts and both guides (v0.15.0). Uses the Pixel Platformer art already in the project.
- [x] Grid puzzle kit: scripts and both guides (v0.16.0). The eight sample levels were checked with a solver.
- [x] Tower defense kit: scripts and both guides (v0.17.0).
- [x] Management kit: scripts and both guides (v0.18.0). The sample's economy was checked with a simulation.
- [x] Farming kit: scripts and both guides (v0.19.0). The sample's economy was checked with a simulation.
- [ ] Remaining kits, each with scripts, a student guide and a "Building the Sample" guide: visual novel with dating sim (Yarn Spinner 3.3.2, installed from OpenUPM), card game (needs Kenney's Playing Cards Pack).
- [ ] 3D kits: 3D platformer, then horror and stealth, with the 3D module scripts they need (camera helpers, enemies that use a navigation mesh).
- [ ] Match the Week 5–7 lecture pages to the real script names.
- [ ] Move the instructor's tested exercise scenes to `Assets/_Course/Exercises/Solutions/` (once Marshall says they're final).
- [ ] Fix whatever the compile check and tests turn up. This always comes first when reports arrive.

## Order of work

### Phase 1 — Finish the sandbox (weeks 1–7 material)

- [ ] Test Ex 03, 04, 05 (both versions) and 06 in Unity, in order. Fix what breaks.
- [x] Write the Ex 00 tutorial (install, practice project, Editor tour).
- [ ] Move the reference solutions to `Assets/_Course/Exercises/Solutions/`.
- [ ] Match the Week 5–7 lecture pages to the real script names.

### Phase 2 — What students need before they pitch

- [x] Decide the supported genre list (decision 1).
- [x] **Genre Map** page, drafted in `Guides/Genre Map.md`: for each genre, the core loop, example games, what the kit provides, a sensible scope for eight weeks, and what is out of scope.
- [x] Assignment pages: Three game ideas, Pitch, One-sheet, Screen layout, Ten-pager draft and final.
- [x] A pitch format that names the genre from the map and lists the game's mechanics, so each pitch can be checked against its kit.

### Phase 3 — Genre kits

One kit at a time, in priority order. For each kit:

1. Scripts, in `Assets/_Course/Kits/<Genre>/`, with their own assembly. They depend on Core and never change it.
2. A **kit guide** in Markdown that builds the kit's sample game step by step.
3. The instructor follows the guide in Unity. That tests the scripts and the guide, and the result becomes the kit's sample.
4. The kit is exported as its own `.unitypackage`: scripts, sample scene, prefabs and data.

**Build order** (fifteen kits; visual novel and dating sim share one):

1. Small, and they settle the kit format: platformer, top-down adventure, turn-based battle, arcade classic (scripts and both guides written for all four; the samples need building and testing)
2. Medium: physics puzzle (scripts and guides written; sample needs building, and Kenney's Physics Assets pack), top-down shooter (scripts and guides written, v0.14.0; sample needs Kenney's Pixel Shmup), endless runner (scripts and guides written, v0.15.0), grid puzzle (scripts and guides written, v0.16.0), tower defense (scripts and guides written, v0.17.0), management and strategy (scripts and guides written, v0.18.0), visual novel with dating sim
3. The 3D script module, in the same course project (**decided** 2026-11-20: one project, one repository, with the 2D and 3D scripts and kits side by side, sharing the same Core, UI and data). The module's first two scripts, Tank Controller 3D and Rail Runner 3D, are in `_Course/ThreeD`, with two tutorials in `Tutorials/`. Next: a 3D renderer added to the project's URP settings (one-time, in Unity), then the 3D platformer kit
4. Large: card game, farming and life sim (scripts and guides written, v0.19.0), horror and stealth

Kits aren't used until week 8 of the semester, so the later ones can be finished during weeks 1–7.

**Kenney packs to try first** (to be confirmed as each kit is built). Download links for every pack are in the template's `Assets/_Course/Art/Kenney/README.md`:

| Kit | Pack |
|---|---|
| Platformer | Pixel Platformer (in the template) |
| Top-down adventure | Tiny Dungeon, Tiny Town |
| Turn-based battle | Tiny Dungeon |
| Arcade classic | Puzzle Pack 2 (Breakout, Pong), Space Shooter Remastered (Asteroids) |
| Physics puzzle | Physics Assets |
| Top-down shooter | Pixel Shmup, or Space Shooter Remastered |
| Grid puzzle | Sokoban |
| Tower defense | Tower Defense (top-down) |
| Card game | Playing Cards Pack |
| Menus and HUD | Pixel UI Pack |
| Sound effects | Interface Sounds, UI Audio, Impact Sounds, Digital Audio, Sci-Fi Sounds, RPG Audio, Casino Audio, Music Jingles, Voiceover packs (in `Art/Kenney/audio`) |
| 3D kits | Platformer Kit, Prototype Textures |


### Phase 4 — Weeks 8–16

- [x] Scripts for Lectures 8–10: audio, camera shake and hit stop, Timeline cutscenes, saving, settings (v0.10.0). Dialogue moves to the visual novel kit.
- [x] Class and Lecture pages for weeks 8–16.
- [x] Exercise tutorials Ex 07–10 drafted. The class pages assume them (decision 5, still to be confirmed): Juice & Audio, Save & Build, Debug & Profile, Playtest.
- [x] Assignment pages: Production Backlog, First Playable, Sprint Review, Alpha, Beta, Gold, Post-Mortem. The first build moved into Ex 08 and the playtest report into Ex 10.
- [x] Topic pages (decision 6).

### Phase 5 — Release

- [x] Keep kits, art packs and exercise solutions out of the student project ZIP. They stay in the repository for development; a `.gitattributes` file with `export-ignore` lines leaves them out of GitHub's ZIP downloads, and each kit is exported as its own package.
- [x] Shared `CoursePanelSettings` asset (v0.12.0, hand-written; **Collin Game → UI → Repair Course Panel Settings** rebuilds it if Unity rejects it). Exercise 06 and the kit guides use it.

- [x] Assign points to every exercise and assignment (decision 7). Points are on each assignment and class page, and in the schedule's Grading table.
- [ ] Tag v1.0, publish the Release, export the update and kit packages.
- [ ] Test the whole student path on a lab computer.

### Phase 6 — After pitch week (during the semester)

- [ ] Compare each approved pitch with its kit, and list what the kit doesn't cover.
- [ ] Write per-game scripts into `Assets/_Course/Games/<GameName>/`, within the agreed limit (decision 8).
- [ ] Write a short guide for each game.

## Decisions needed

| # | Decision | Recommendation | Blocks |
|---|---|---|---|
| 1 | Which genres are on the map for the first semester | **Decided:** sixteen genres. 2D: arcade classic, platformer, top-down adventure, turn-based battle, endless runner, top-down shooter, grid puzzle, physics puzzle (added later), tower defense, management and strategy, card game, farming and life sim. Narrative: visual novel, dating sim (one kit). 3D: 3D platformer, horror and stealth. No VR or AR. Lectures and exercises stay 2D | — |
| 2 | Art in kit samples | **Decided:** Kenney's CC0 packs, kept under `Assets/_Course/Art/Kenney/` in a folder named as Kenney's download is named (for example `kenney_pixel-platformer`), with the pack's license file. Each pack gets an entry in `CourseArtImporter`, which sets its import settings. Every pack is listed in `Course Credits`, which the game's Credits screen shows. Plain shapes stay in the exercises | — |
| 3 | How each kit's sample is built | **Decided:** a menu command per kit (**Collin Game → Kit Samples**) builds the sample; the instructor plays it, and can follow the "Building the Sample" guide to check it. First one: Platformer (v0.13.1). The rest follow once it's tested | — |
| 4 | Dialogue tool | **Decided:** Yarn Spinner. To be installed from a package registry and not from a Git URL, so lab computers don't need Git | — |
| 5 | Are there graded exercises in weeks 8–10? | **Decided:** yes. Ex 07–10, 2 points each, done inside the student's own game | — |
| 6 | What a Topic page is | **Decided:** one page per lecture topic in `Topics/`, with the lecture's intent, key ideas, an in-class plan, common problems, where the topic comes up, and further resources. Linked from the Lecture page, the Class page and the exercises | — |
| 7 | Point scale | **Decided:** 100 points, plus up to 5 extra credit. Table in the schedule | — |
| 8 | Limit on per-game custom scripts | A fixed number per student, such as two or three small scripts, agreed at pitch approval | Scope of Phase 6 |
| 9 | Does Game & Simulation Group Project start from the same template project? | **Decided:** yes. It uses the same template scripts, with kits imported as needed | — |

## Open risks

- **Untested code is stacked up.** Eleven kits and the 3D module compile but haven't been played, and Ex 05–10 haven't been tested. Each new kit adds to the pile, so test reports take priority over new kits.
- **Each kit costs instructor testing time.** The kit count in decision 1 should match the time available before the semester.
- **The Unity Version Control allowance for students** is still unconfirmed.
- **3D lives in the same course project** as 2D (decided 2026-11-20): one project, one repository, one set of Core, UI and data. 3D scenes use a second URP renderer. **The Unreal section** is deferred until the 2D Unity course is complete.
