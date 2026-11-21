---
title: "Physics Puzzle Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.11.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Physics Puzzle Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Physics Puzzle Kit**, not this page.

Everything goes in `Assets/_Course/Kits/PhysicsPuzzle/Sample/`, with folders `Data`, `Prefabs`, `Scenes` and `Materials`.

## Before you start

1. Pull the template project. It should be version 0.11.0 or later, with no red errors in the Console.
2. **Art.** Kenney's **Physics Assets** pack is already in `Assets/_Course/Art/Kenney/kenney_physics-assets` (70 pixels per unit, so a 70-pixel block is one unit). If sprites look the wrong size, choose **Collin Game → Art → Reapply Art Import Settings**.
3. Every UI Document uses the shared `CoursePanelSettings` (filled in automatically; see the Platformer Kit sample).

## Part 1 — Data

In `Sample/Data`:

| Asset | Type |
|---|---|
| `ShotsLeft`, `TargetsLeft`, `PuzzleScore`, `BestPuzzleScore` | Int Variable |
| `ShotFinished`, `PuzzleWon`, `PuzzleLost` | Void Event Channel |

In `Sample/Materials`, create three **Physics Material 2D** assets:

| Material | Friction | Bounciness |
|---|---|---|
| `Rough` | `0.8` | `0` |
| `Slippery` | `0.05` | `0` |
| `Bouncy` | `0.3` | `0.85` |

## Part 2 — Prefabs

Build each in a new scene `Sample/Scenes/Puzzle_Level1`, drag it into `Sample/Prefabs`, then delete it from the scene unless a step says to keep it.

### Ball

| Component | Settings |
|---|---|
| Sprite | A round sprite from the pack, or **2D Object → Sprites → Circle**, Scale `0.6` |
| Circle Collider 2D | Material `Rough` |
| Rigidbody 2D | Mass `2`, Collision Detection **Continuous** |

### Blocks

Make one, then make the other two as prefab variants.

| Prefab | Sprite | Rigidbody 2D Mass | Breakable 2D Break Speed | Amount |
|---|---|---|---|---|
| `Wood Block` | A wood rectangle from the pack | `1` | `6` | `100` |
| `Glass Block` | A glass rectangle | `0.6` | `3` | `50` |
| `Stone Block` | A stone rectangle | `3` | `11` | `200` |

Each has a **Box Collider 2D** fitted to its sprite, a **Rigidbody 2D**, and a **Breakable 2D** with **Add To** `PuzzleScore`.

### Target

A round character sprite from the pack, with a **Circle Collider 2D**, a **Rigidbody 2D** (Mass `0.8`), a **Breakable 2D** (Break Speed `3`, Add To `PuzzleScore`, Amount `500`), and a **Puzzle Target 2D** (Targets Left `TargetsLeft`).

### Launcher

1. Create an empty GameObject named `Launcher`. Give it a child sprite of a slingshot or post, for looks.
2. Add **Launcher 2D**:
   - **Projectile Prefab:** `Ball`
   - **Max Pull** `2.5`, **Power** `7`
   - **Shots Left:** `ShotsLeft`
   - **Dot Sprite:** the Circle sprite from **Create → 2D → Sprites → Circle** in `Sample/Materials`
   - **Raise On Shot Finished:** `ShotFinished`
   - **Remove Projectile After Shot:** ticked

### Rope Anchor

1. Create a small sprite named `Rope Anchor` high in the air.
2. Add **Rope 2D** with **Link Count** `10` and **Link Sprite** the same Square sprite.
3. Keep it in the scene for Level 3; set **Hanging Body** in each level.

### Level Systems

An empty GameObject at `0, 0, 0` with these children:

**`Rules`** — **Puzzle Rules**: Targets Left `TargetsLeft`, Shots Left `ShotsLeft`, Starting Shots `3`, Shot Finished `ShotFinished`, Raise On Won `PuzzleWon`, Raise On Lost `PuzzleLost`, Score `PuzzleScore`. Also **High Score**: Score `PuzzleScore`, Best `BestPuzzleScore`, Save Name `Puzzle`.

**`Cutter`** — **Cutter 2D**.

**`Scene Changer`** — **Scene Changer**, Scene Name empty. **`To Menu`** — **Scene Changer**, Scene Name `Puzzle_Menu`.

**`HUD`** — UI Document, Source Asset `PuzzleHUD` (from `Kits/PhysicsPuzzle/UI`), with a **UI Variable Binder**: `shots-label` → `ShotsLeft` → `Shots: {0}`; `targets-label` → `TargetsLeft` → `Targets: {0}`; `score-label` → `PuzzleScore` → `Score: {0}`.

**`Pause Menu`** — as in the Platformer Kit sample (`PauseMenu`, UI Screen hidden, Pause Controller, UI Button Events for resume, restart and menu).

**`Level Complete`** — UI Document `LevelComplete` (from `Kits/Platformer/UI`, or a copy), Sort Order `2`, UI Screen hidden, a **UI Variable Binder** (`coins-label` → `PuzzleScore` → `Score: {0}`), a **Void Event Listener** on `PuzzleWon` → **UIScreen → Show**, and buttons `next-button` → **SceneChanger → LoadNextScene**, `menu-button` → To Menu **Load**.

**`Game Over`** — UI Document `GameOver`, Sort Order `3`, UI Screen hidden, a **Void Event Listener** on `PuzzleLost` → **UIScreen → Show**, and buttons `try-again-button` → **SceneChanger → ReloadScene**, `menu-button` → To Menu **Load**.

Keep one `Level Systems` in the scene.

## Part 3 — Levels

Each level teaches one idea.

| Scene | Build | Starting Shots | Teaches |
|---|---|---|---|
| `Puzzle_Level1` | Ground, the Launcher on the left, and on the right a small wood tower with one Target on top | `3` | Launching |
| `Puzzle_Level2` | Two towers: glass in front, stone behind, a Target in each. A `Bouncy` wall at the far right | `3` | Materials and break speeds |
| `Puzzle_Level3` | No Launcher. A Rope Anchor holding a stone block above a wood shelter with a Target inside, and a second rope holding a Ball over a seesaw (plank with a Hinge Joint 2D) | `1` (unused) | Cutting ropes and joints |

Level 3 has no launcher, so it can't be lost by running out of shots; delete the Game Over screen's listener in that level, or keep a Launcher off to the side as a backup.

## Part 4 — Menu and win scenes

Build `Puzzle_Menu` and `Puzzle_Win` as in the Platformer Kit sample, using `PuzzleScore` and `BestPuzzleScore`, and a **Variable Resetter** on `PuzzleScore` in the menu.

## Part 5 — Scene List

`Puzzle_Menu`, `Puzzle_Level1`, `Puzzle_Level2`, `Puzzle_Level3`, `Puzzle_Win`, in that order.

## Part 6 — Test

- [ ] Aiming with the mouse shows dots, and the ball follows them.
- [ ] Aiming with **Enter** and **WASD**, and with a gamepad, works.
- [ ] Each launch uses a shot; at 0 the launcher stops.
- [ ] Glass breaks easily, wood with a good hit, stone rarely.
- [ ] Blocks don't break at the start of the level.
- [ ] Breaking all targets shows Level Complete with points for unused shots.
- [ ] Running out of shots with targets left shows Game Over.
- [ ] In Level 3, swiping cuts the ropes and the stone falls.
- [ ] The rope swings naturally and doesn't stretch apart.
- [ ] The best score is kept after closing and reopening the game.
- [ ] Esc pauses; aiming and cutting stop while paused.

Note anything that fails, with the Console message.

## Part 7 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/PhysicsPuzzle` and the Physics Assets art folder with **Assets → Export Package**, unticking Core and 2D scripts that Unity adds as dependencies.
