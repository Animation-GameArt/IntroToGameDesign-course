---
title: GAME 1303 — Course Schedule
course: GAME 1303 Game Development
weeks: 16
unity: 6000.3.10f1 (Unity 6.3 LTS)
tags:
  - game1303
  - schedule
  - syllabus
---

# GAME 1303 — Course Schedule

> [!info] How this course works
> - **Weeks 1–10:** a lecture each week, paired with a lab.
> - **Weeks 1–7:** each lab builds one step of a small **sandbox game** in 2D. The sandbox uses the same course scripts you will use in your own game.
> - **Weeks 11–15:** studio weeks, where you build, playtest and debug your own game.
> - **Week 16:** post-mortem presentations.
>
> **No more than one project item is due each week.** Exercises are finished and checked off **in lab**, then backed up with your project. They are not separate homework submissions.
>
> **Project items are due at 11:59 PM the night before class.** That way class time is for feedback and building, not for finishing. The one exception is Week 1's three game ideas, which are due at 11:59 PM on the day of the first class.

---

## Exercises, and your own game

Everyone builds the same **2D sandbox game** in the exercises, whatever kind of game they plan to make. What the exercises teach (events, variables, input, health, checkpoints, UI) is used in every genre.

Your own game fits one of the genres on the **Genre Map**. In week 8 you import that genre's kit and start building.

| Your game is… | You start it from… |
|---|---|
| 2D, or a visual novel | The course project you've used since week 2 |
| 3D | A 3D version of the course project, starting in week 8 |

> [!note] VR and AR
> VR and AR games aren't part of this course. They have their own projects in other courses.

---

## Exercise scenes

Week 1 uses a practice project. From week 2 on, you work in the **course project**, downloaded from GitHub, and each exercise is its own scene in `Assets/Scenes/Exercises/`. When an exercise builds on the previous week, open last week's scene and use **File → Save As…** with the new name, so every week's work is kept.

| # | Scene file | Builds on |
|---|---|---|
| 00 | *(practice project, not kept)* | — |
| 01 | `Ex01_Bootstrap.unity` | — (first scene in the course project) |
| 02 | `Ex02_Events.unity` | Ex01 |
| 03 | `Ex03_Player.unity`, then `Ex03_TopDown.unity` | Ex02 |
| 04 | `Ex04_Level.unity` | Ex03 |
| 05 | `Ex05_Combat.unity` (real-time), or `Ex05_TurnBased.unity` (turn-based) | Ex04; turn-based can start from Ex04 or Ex01 |
| 06 | `Ex06_UI.unity` and `Ex06_MainMenu.unity` | Ex05 — **sandbox complete** |

> [!note] Your own game starts in week 8
> Weeks 1–7 in Unity are for the exercises. During weeks 3–7 your own game is designed on paper: written pitch, one-sheet, screen layout and ten-pager. You start building it in Unity in week 8.

---

## Exercises after week 7

From week 8 the exercises happen inside your own game, so they have no scene files of their own.

| # | Exercise | Week |
|---|---|---|
| 07 | Juice & Audio | 8 |
| 08 | Save & Build: includes your first build, uploaded to a private itch.io page | 9 |
| 09 | Debug & Profile | 10 |
| 10 | Playtest: includes your playtest notes and the changes you choose from them | 13 |

---

## Week-by-week schedule

### Phase 1 — Foundations

| Wk | Lecture | Lab exercise (checked off in lab) | Due this week |
|---|---|---|---|
| 1 | **L1 · Games, Genres & the Industry.** What makes a game, core loops, the Genre Map, roles and studios, indie vs. AAA | **Ex00 · Setup:** install Unity Hub and Unity 6000.3.10f1, make a practice project, tour the Editor, enter Play mode | **Three game ideas** (Canvas Discussion) |
| 2 | **L2 · Pitching, Scope & Project Management.** How to pitch, scoping to 13 weeks, task boards, backing up your project (Unity Version Control or SSD) | **Ex01 · Bootstrap:** download the course project from GitHub, add it in Unity Hub, set up your backup, Bootstrapper, SceneLoader | **Project setup check** |
| 3 | **Pitch Day:** live pitches in class, presented from your Canvas Discussion post. Then **L3 · Unity Fundamentals.** GameObjects, components, prefabs, the script lifecycle, ScriptableObjects, Console and breakpoints | **Ex02 · Events:** event channels, SO variables, a collectible and a score counter | **Pitch** (Canvas Discussion post, due 11:59 PM the night before class; presented live in class) |
| 4 | **L4 · Input & Game Feel.** The Input System, control schemes, game feel (coyote time, jump buffering, acceleration). | **Ex03 · Player:** the Input Reader, a platformer controller and a top-down controller | **One-sheet** |
| 5 | **L5 · Level Design & Cameras.** Pacing, teaching through the level, Tilemaps, Cinemachine | **Ex04 · Level:** build a short level, camera follow and bounds, hazards, checkpoints | **Screen layout** (wireframes of your main screens) |
| 6 | **L6 · Game Systems & AI.** Health and damage, pickups, object pooling, spawners, state machines, simple enemy AI, turn-based systems | **Ex05 · Combat.** Choose one. *Real-time:* a patrolling enemy, damage, a spawner, respawning. *Turn-based:* a turn manager, player and enemy turns, attacks and damage, winning and losing | **Ten-pager draft** (peer review) |
| 7 | **L7 · UI & UX.** UI Toolkit screens and HUD, diegetic vs. screen UI, world-space text, menus and pause | **Ex06 · UI:** main menu, pause, HUD, damage popups. **Sandbox complete** | **Ten-pager (final)** |

### Phase 2 — Your Game

| Wk | Lecture | Exercise (in your own game) | Due this week |
|---|---|---|---|
| 8 | **L8 · Juice, Audio & Storytelling.** Feedback, camera shake, sound and music, Timeline cutscenes, dialogue | **Ex07 · Juice & Audio:** feedback for three actions, music, one camera shake | **Production backlog** |
| 9 | **L9 · Saving, Builds & Playtesting.** What to save, settings, building for Windows and Web, publishing privately on itch.io, watching someone play | **Ex08 · Save & Build:** save one thing, a volume setting, your first build uploaded | — |
| 10 | **L10 · Debugging, Profiling & Production.** Reproducing bugs, reading errors, the Profiler, bug triage, cutting scope, milestones | **Ex09 · Debug & Profile:** a bug list, one bug fixed, one Profiler reading | **First Playable** |

### Phase 3 — Studio

Each studio class opens with a stand-up and a short topic. The rest is time to build.

| Wk | Focus | In class | Due this week |
|---|---|---|---|
| 11 | Core loop complete and feeling right | Sprint review: two-minute demos | **Sprint review build** |
| 12 | All features in, even if rough | Alpha check against your must-have list | **Alpha** |
| 13 | Playtesting | **Ex10 · Playtest:** three classmates play while you watch | — |
| 14 | All content in; fixes and polish only | Bug bash | **Beta** |
| 15 | Release | Release check of each public page | **Gold** (public itch.io release) |

### Week 16 — Post-Mortem

| Wk | Activity | Due this week |
|---|---|---|
| 16 | Post-mortem presentations: what went right, what went wrong, what you'd change, planned scope vs. final game | **Post-mortem** |

---

## Milestone definitions

| Milestone | Definition |
|---|---|
| **Three game ideas** | Three one-line game ideas, posted to the Canvas Discussion |
| **Project setup check** | The course project opens on your computer or SSD, and you can show how you back it up (Unity Version Control, or an SSD plus a second copy at home) |
| **Pitch** | A written pitch for one game, with any artwork you have, posted to the Canvas Discussion by **11:59 PM the night before class**. You present it live in class from your post, for feedback and approval |
| **One-sheet** | A one-page summary of your game for an approval meeting. Template: `One-Sheet Template` |
| **Screen layout** | Paper or digital wireframes of your game's main screens: title, HUD, pause, and win/lose. They show what the player sees and where. You'll use them for page 6 of the ten-pager and for the UI lecture in week 7 |
| **Ten-pager** | A ten-page design document covering the whole game. Template: `Ten-Pager Template` |
| **Production backlog** | Every feature from your ten-pager, broken into tasks on your task board, with a week assigned |
| **First Playable** | One complete pass through your core loop: the player can start, play, and win or lose |
| **Sprint review build** | The core loop is complete and feels right. Uploaded before class and shown in a two-minute demo |
| **Alpha** | Every feature exists and works, even if the art, audio and balance are placeholders |
| **Beta** | All content is in. From here on, only bug fixes and polish |
| **Gold** | The finished game, publicly released on itch.io with a store page |
| **Post-mortem** | A presentation reviewing the project honestly |
