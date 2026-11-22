---
title: "Grid Puzzle Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.16.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Grid Puzzle Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Grid Puzzle Kit**, not this page.

Everything goes in `Assets/_Course/Kits/GridPuzzle/Sample/`, with folders `Data`, `Prefabs`, `Scenes` and `Tiles`.

> [!tip] The quick way
> **Collin Game → Kit Samples → Build Grid Puzzle Sample** builds everything on this page in a few seconds and opens the menu scene; press **Play**. It replaces the kit's `Sample` folder. The eight levels, the level list and the Level Select scene are built too. Then work through **Test** to check it. Building by hand, step by step, is still the way to learn the kit, and checks this guide.

## Before you start

1. Pull the template project. It should be version 0.16.0 or later, with no red errors in the Console.
2. **Art.** Kenney's **Sokoban** pack is already in `Assets/_Course/Art/Kenney/kenney_sokoban-pack` (use the `PNG/Default size` images). Its tiles are 64 pixels, so one tile is one unit.
3. Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data

In `Sample/Data`:

| Asset | Type |
|---|---|
| `Moves` | Int Variable |
| `LevelTitle` | String Variable |
| `LevelSolved` | Void Event Channel |
| `Puzzle Levels` | Level List (**Create → Collin Game → Grid Puzzle Kit → Level List**): Save Name `SampleSokoban`; Levels `Puzzle_01` … `Puzzle_08`; Titles as in Part 5 |

## Part 2 — Prefabs

Every piece is a sprite from the Sokoban pack with **Grid Piece**; no collider. Order in Layer: floor `-10`, goals `-5`, pieces `0`, player `5`.

| Prefab | Sprite | Grid Piece | Notes |
|---|---|---|---|
| `Player` | a player sprite | Role **Player**, Move Time `0.1` | |
| `Box` | a brown crate | Role **Pushable** | |
| `Red Box` | a red crate | Role **Pushable**, Kind `red` | |
| `Rock` | a grey block | Role **Solid** | |
| `Gem` | any small item sprite | Role **Item** | |

Goals are sprites with **Grid Goal** (Indicator: its own Sprite Renderer, Filled Color green):

| Prefab | Sprite | Grid Goal |
|---|---|---|
| `Target` | an empty target marker | Filled By **Pushable** |
| `Red Target` | a red target marker | Filled By **Pushable**, Kind `red` |
| `Exit` | a door or flag | Filled By **Player** |

## Part 3 — Puzzle Systems

An empty `Puzzle Systems`, made into a prefab, with these children:

**`Board`** — **Grid Board**: Walls (set in each scene, see Part 4), Max Pushed In A Row `1`, Moves `Moves`, Level List `Puzzle Levels`, Level Title `LevelTitle`, Raise When Solved `LevelSolved`. And **Grid Player Input**.

**`HUD`** — UI Document `PuzzleHUD` (from `Kits/GridPuzzle/UI`), with a **UI Variable Binder**: `level-label` → `LevelTitle` → `{0}`; `moves-label` → `Moves` → `Moves: {0}`.

**`Pause Menu`** — as in the Platformer Kit sample, with its menu button loading `Puzzle_Select`.

**`Settings`** — as in the Platformer Kit sample (`Settings`, Sort Order `4`, UI Screen hidden, UI Settings, `back-button` hides it), with the Pause Menu's `settings-button` showing it.


**`Loader`** — **Puzzle Level Loader**: Level List `Puzzle Levels`, After Last Level `Puzzle_Select`. And a **Scene Changer** with Scene Name `Puzzle_Select`.

**`Solved`** — UI Document `PuzzleSolved`, Sort Order `2`, **UI Screen** (Hidden At Start, Select When Shown `next-button`), a **Void Event Listener** on `LevelSolved` → **UIScreen → Show**, a **UI Variable Binder** (`moves-label` → `Moves` → `Solved in {0} moves`), and **UI Button Events**: `next-button` → `Loader`, **PuzzleLevelLoader → LoadNextLevel**; `select-button` → `Loader`, **SceneChanger → Load**.

Because the Board's Walls differ in each level, set it after placing the prefab in each scene.

## Part 4 — The level template (`Puzzle_01`)

1. A new 2D scene. Main Camera: Orthographic, Size `5`, dark background.
2. **GameObject → 2D Object → Tilemap → Rectangular**, named `Floor` (Order in Layer `-10`), then a second Tilemap named `Walls` (Order `-1`).
3. Create Tile assets in `Sample/Tiles` from a floor sprite and a wall sprite (drag the sprites into a Tile Palette).
4. `Puzzle Systems`; set Board → **Walls** to the `Walls` Tilemap.
5. Paint the level below. Place pieces and goals on cell centres (snapping is automatic when the level starts, but neat placement helps).

## Part 5 — Eight levels

Each level is a **Save As** of the last, redesigned. Small rooms, one idea each. In the maps, `#` wall, `.` floor, `P` player, `B` box, `T` target, `*` box already on a target, `R` red box, `r` red target, `O` rock, `G` gem, `E` exit.

**`Puzzle_01` — "First Push"** (one box, straight push)
```
#######
#.....#
#.PB.T#
#.....#
#######
```

**`Puzzle_02` — "Around the Corner"** (push from the other side)
```
#######
#..T..#
#..#..#
#.PB..#
#.....#
#######
```

**`Puzzle_03` — "Two Boxes"**
```
########
#......#
#.B..T.#
#.P##..#
#.B..T.#
#......#
########
```

**`Puzzle_04` — "Corners Are Traps"** (a box in a corner can't be moved; undo teaches itself)
```
#######
#T...##
#.#B..#
#..P..#
##.B.T#
#######
```

**`Puzzle_05` — "Rocks"**
```
########
#..O..T#
#.B.O..#
#.P..B.#
#O...O.#
#T.....#
########
```

**`Puzzle_06` — "Red Box"** (colours must match)
```
########
#r....T#
#..R.B.#
#.P....#
########
```

**`Puzzle_07` — "Collect the Gems"** (Need All Items ticked; reach the Exit; no box targets)
```
########
#G..B.E#
#.##.#.#
#P.B..G#
########
```

**`Puzzle_08` — "Tight Room"**
```
#######
##..T##
#.B.B.#
#T.P.T#
#.B...#
##....#
#######
```

Each layout has been checked with a solver. The fewest moves: 2, 8, 13, 11, 23, 12, 11, 17. Solve each one yourself before moving on.

## Part 6 — Menu and level select

**`Puzzle_Menu`**: like the Platformer sample's menu. Play → a **Puzzle Level Loader** (`Puzzle Levels`) → **LoadFirstUnsolved**. Add a **Levels** button → a Scene Changer to `Puzzle_Select`.

**`Puzzle_Select`**: UI Document `LevelSelect`, with **Puzzle Level Loader** (`Puzzle Levels`), **UI Level Select**, and **UI Button Events**: `back-button` → a Scene Changer to `Puzzle_Menu`.

## Part 7 — Scene List

`Puzzle_Menu`, `Puzzle_Select`, `Puzzle_01` … `Puzzle_08`.

## Part 8 — Test

- [ ] The player moves one cell per press; holding repeats after a short pause.
- [ ] Walls block; boxes push; two boxes in a row don't; rocks never move.
- [ ] Undo takes back one move at a time, including pushes and gem pickups; the move counter goes down.
- [ ] Restart puts everything back; it can't be undone.
- [ ] Targets turn green when filled, and back when emptied.
- [ ] The red target only takes the red box.
- [ ] Level 7 needs every gem and the exit.
- [ ] Solving shows the solved screen with the moves; Next loads the next level; after level 8, the level select.
- [ ] The level select greys out locked levels and colours solved ones; progress survives restarting Unity.
- [ ] With **Unlock All** ticked on the list, every level can be chosen.
- [ ] Esc pauses; no moves while paused.

Note anything that fails, with the Console message.

## Part 9 — Commit

Commit and push the `Sample` folder with its `.meta` files, and the Sokoban art folder.

## Later — Exporting the kit

Export `Assets/_Course/Kits/GridPuzzle` and the Sokoban art folder with **Assets → Export Package**, unticking Core scripts that Unity adds as dependencies.
