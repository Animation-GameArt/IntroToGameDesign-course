---
title: "Visual Novel Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.20.0
unity: 6000.3.10f1
yarn_spinner: 3.3.2
tags:
  - game1303
  - kit
  - instructor
---

# Visual Novel Kit — Building the Sample

**For the instructor.** These steps build the kit's sample story once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Visual Novel Kit**, not this page.

Everything goes in `Assets/_Course/Kits/VisualNovel/Sample/`. The story is already written: `Sample/Story/LanternFestival.yarn`. Add folders `Data`, `Characters`, `UI` and `Scenes`.


> [!tip] The quick way
> **Collin Game → Kit Samples → Build Visual Novel Sample** builds everything on this page in a few seconds and opens the menu scene; press **Play**. It replaces the kit's `Sample` folder. The story script, `Sample/Story/LanternFestival.yarn`, is kept. Then work through **Test** to check it. Building by hand, step by step, is still the way to learn the kit, and checks this guide.

## Before you start

1. Pull the template project. It should be version 0.20.0 or later, with Yarn Spinner 3.3.2 in the Package Manager, and no red errors in the Console.
2. Click `Sample/Story/LanternFestival.yarn`. The Inspector should show its nodes (Start, Stalls, Bridge and three endings) and no errors.
3. Every UI Document uses `CoursePanelSettings`.

## Part 1 — The Yarn Project

1. Right-click `Sample/Story` → **Create → Yarn Spinner → Yarn Project**. Name it `LanternFestival`.
2. Click it. The Inspector lists `LanternFestival.yarn` under its source scripts, with no errors. If it shows errors, note them; they're mistakes in the script for Claude to fix.

## Part 2 — Data

In `Sample/Data`:

| Asset | Type |
|---|---|
| `RenAffection`, `MikaAffection` | Int Variable, Initial Value `0` |
| `RenEnding`, `MikaEnding`, `AloneEnding` | Void Event Channel |

## Part 3 — Characters

In `Sample/Characters` (**Create → Collin Game → Visual Novel Kit → Character**):

| Character | Character Name | Name Color | Portraits | Default Position |
|---|---|---|---|---|
| `Ren` | `Ren` | `FF9F6B` (orange) | `neutral`: Tiny Dungeon `tile_0099` | Left |
| `Mika` | `Mika` | `7FC8FF` (blue) | `neutral`: Tiny Dungeon `tile_0085` | Right |

The pixel characters are tiny; the screen scales them up. With **Filter Mode: Point** (the course art import settings already do this) they stay sharp.

## Part 4 — Story Systems

An empty `Story Systems`, made into a prefab, with these children:

**`Dialogue`**:
1. **Dialogue Runner** (from Yarn Spinner): Yarn Project `LanternFestival`, Start Node `Start`, **Auto Start** ticked.
2. A **UI Document**: Source Asset `VisualNovel` (from `Kits/VisualNovel/UI`).
3. **UI Dialogue Presenter**: Letters Per Second `45`, Show Unavailable Choices ticked, Stop Player While Talking ticked. Drag this component into the Dialogue Runner's **Dialogue Presenters** list, and remove any other presenters there.
4. **Visual Novel Stage**: Runner `Dialogue`; Characters `Ren`, `Mika`; Dim Others ticked; Backgrounds:

   | Name | Sprite | Color |
   |---|---|---|
   | `Square` | — | `2B2547` (dusky purple) |
   | `Stalls` | — | `5A2E2E` (warm red) |
   | `Bridge` | — | `16304A` (night blue) |

   Starting Background `Square`; Events: `RenEnding` → `RenEnding`, `MikaEnding` → `MikaEnding`, `AloneEnding` → `AloneEnding`.
5. **Yarn Variable Link**: Runner `Dialogue`; Links `$ren` → `RenAffection`, `$mika` → `MikaAffection`; Two Way unticked.
6. **UI Relationship Meters**: Ren → `RenAffection`, max `6`; Mika → `MikaAffection`, max `6`; Show Numbers ticked.

**`Reset`** — a **Variable Resetter** with `RenAffection` and `MikaAffection`.

**`Pause Menu`**, **`Settings`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Endings`** — first, duplicate `Core/UI/EndScreen.uxml` three times into `Sample/UI`, and in each copy change the text of `title-label` and `score-label` (in the UI Builder, or in a text editor):

| Copy | `title-label` | `score-label` |
|---|---|---|
| `RenEndScreen` | *Ren's Lantern* | *You and Ren, side by side.* |
| `MikaEndScreen` | *Mika's Lantern* | *The bridge lantern stayed lit.* |
| `AloneEndScreen` | *A Quiet Night* | *Maybe next year.* |

Then three children, each a UI Document using its copy, hidden at start (**UI Screen**), shown by a **Void Event Listener** on its ending (`RenEnding`, `MikaEnding`, `AloneEnding`), with Play Again → **ReloadScene** and Main Menu → the menu scene, as in the Platformer sample's end screen.

## Part 5 — Scenes

**`Story_Game`**: a new 2D scene with a camera (any background; the screen covers it) and `Story Systems`.

**`Story_Menu`**: like the Platformer sample's menu, with Play loading `Story_Game`.

Scene List: `Story_Menu`, `Story_Game`.

## Part 6 — Test

- [ ] The story starts at Play: the Square background, then Ren appears on the left.
- [ ] Lines type out; a click, tap, Space, Enter or E shows the whole line, and another goes to the next line; one press never skips two lines.
- [ ] Narration lines have no name; Ren's name is orange, Mika's blue.
- [ ] When Mika speaks, Ren is darkened, and the other way round.
- [ ] Choices appear as buttons, and work with the mouse, a tap, and the arrow keys and Enter.
- [ ] The relationship meters move when a choice raises or lowers `$ren` or `$mika` (Mika's can go down).
- [ ] In Stalls, *"Ren and I will fix it together."* is greyed out unless you helped Ren find the ticket.
- [ ] At the Bridge, Ren and Mika are greyed out until their meter is 3 or more; *"I'll watch from here."* always works.
- [ ] Each of the three endings shows its own screen; Play Again restarts with both meters at 0.
- [ ] Esc pauses, and lines don't advance while paused.
- [ ] No warnings in the Console about missing characters, backgrounds or events.

Note anything that fails, with the Console message.

## Part 7 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/VisualNovel` and the Tiny Dungeon art folder with **Assets → Export Package**, unticking Core scripts that Unity adds as dependencies. Yarn Spinner isn't in the package; it's already in every copy of the course project.
