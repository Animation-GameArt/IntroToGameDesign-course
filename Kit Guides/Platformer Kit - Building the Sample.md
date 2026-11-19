---
title: "Platformer Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.9.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Platformer Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Platformer Kit**, not this page.

Everything goes in `Assets/_Course/Kits/Platformer/Sample/`. The art is in `Assets/_Course/Art/Kenney/kenney_pixel-platformer/Tiles`. Sprite names below, such as `tile_0151`, are files in that folder; names that start with `Characters/` are in its `Characters` subfolder.

Collider sizes are starting points. Adjust each one until it fits the artwork.

## Before you start

1. Pull the template project. It should be version 0.9.0 or later (`Assets/_Course/VERSION.txt`), with no red errors in the Console.
2. In `Assets/_Course/Kits/Platformer`, create a folder `Sample`, and inside it the folders `Data`, `Prefabs`, `Scenes` and `Tiles`.

### Shared Panel Settings

All course UI shares one Panel Settings asset, `CoursePanelSettings` in `Assets/_Course/Core/UI` (version 0.12.0 and later), so every screen scales the same way. A new UI Document gets it by itself. If one doesn't, choose **Collin Game → UI → Use Course Panel Settings in Open Scenes**. If the asset is missing or its text doesn't show, choose **Collin Game → UI → Repair Course Panel Settings**.

## Part 1 — Data

In `Sample/Data`, create:

| Asset | Type | Setting |
|---|---|---|
| `Coins` | Int Variable | Initial Value `0` |
| `Lives` | Int Variable | Initial Value `3` |
| `PlayerHealth` | Int Variable | Initial Value `0` |
| `LevelCompleted` | Void Event Channel | |
| `GameOver` | Void Event Channel | |
| `KeyCollected` | Void Event Channel | |

## Part 2 — The first scene

1. Choose **File → New Scene**, pick the 2D template, and save it in `Sample/Scenes` as `Platformer_Level1`.
2. Select `Main Camera`. Set the Camera's **Background** to a sky color, such as a pale blue.

Build each prefab below in this scene, drag it into `Sample/Prefabs`, then delete it from the scene unless a step says to keep it.

## Part 3 — Prefabs

For every sprite, set **Order in Layer** as listed, so things draw in the right order: background `-10`, tiles `0`, pickups `3`, enemies `5`, player `10`.

### Player

| Step | Setting |
|---|---|
| Sprite | `Characters/tile_0000`, Order in Layer `10` |
| Tag | **Player** |
| Capsule Collider 2D | Size `0.8, 1.1` |
| Platformer Controller 2D | **Input** fills itself in |
| Health | Max Health `3`, Invulnerable Time `1`, Health Variable `PlayerHealth` |
| Health → On Died | **+**, drag in the `Lives` asset, choose **IntVariable → Add (int)**, value `-1` |
| Respawner | defaults |
| Health Popups | defaults |
| Platformer Sprite Animator | Idle `Characters/tile_0000`; Walk: `tile_0000`, `tile_0001`; In Air `tile_0001` |

### Pickups

| Prefab | Sprite | Collider (Is Trigger ticked) | Component settings |
|---|---|---|---|
| `Coin` | `tile_0151`, order `3` | Circle Collider 2D, Radius `0.3` | **Collectible:** Add To `Coins`, Amount `1`. **Sprite Flipbook:** Frames `tile_0151`, `tile_0152`; Frames Per Second `6` |
| `Heart` | `tile_0044`, order `3` | Circle Collider 2D, Radius `0.35` | **Collectible:** Add To empty, Heal `1` |
| `Key` | `tile_0027`, order `3` | Box Collider 2D | **Collectible:** Add To empty, Raise Event `KeyCollected` |
| `Goal Gem` | `tile_0067`, order `3` | Circle Collider 2D, Radius `0.4` | **Trigger Zone:** Only Once ticked, Raise On Enter `LevelCompleted` |

### Obstacles

| Prefab | Sprite | Collider | Component settings |
|---|---|---|---|
| `Lock` | `tile_0028` | Box Collider 2D, solid | **Void Event Listener:** Channel `KeyCollected`; Response: drag in the `Lock` itself, **GameObject → SetActive (bool)**, unticked |
| `Spikes` | `tile_0068` | Box Collider 2D, **Is Trigger**, Size `0.8, 0.4`, Offset `0, -0.3` | **Damage On Touch:** defaults |
| `Spring` | `tile_0107` | Box Collider 2D, **Is Trigger**, Size `0.8, 0.4`, Offset `0, -0.1` | **Bounce Pad 2D:** Bounce Height `6`, Fired Sprite `tile_0108` |
| `One-Way Platform` | `tile_0146` | Box Collider 2D, solid, fitted to the plank, **Used By Effector** ticked | **Platform Effector 2D:** Use One Way ticked |
| `Checkpoint` | `tile_0111`, Color mid-grey | Box Collider 2D, **Is Trigger**, Size `1, 2`, Offset `0, 0.5` | **Checkpoint:** Indicator is the `Checkpoint` itself, Active Color white. **Sprite Flipbook:** Frames `tile_0111`, `tile_0112`; Frames Per Second `4` |

### Moving Platform

1. Create an empty GameObject named `Moving Platform`.
2. Give it three child sprites: `tile_0001` at X `-1`, `tile_0002` at X `0`, `tile_0003` at X `1`.
3. On the parent, add a **Box Collider 2D** with Size `3, 1`.
4. On the parent, add **Waypoint Mover 2D**: Stops has one entry, `4, 0`; Speed `2`; Wait At Stops `0.5`. A Rigidbody 2D is added with it.

### Enemies

| Prefab | Sprite | Collider | Component settings |
|---|---|---|---|
| `Walker` | `Characters/tile_0018`, order `5` | Box Collider 2D, solid, Size `0.75, 0.6`, Offset `0, -0.3` | **Patrol Enemy 2D:** defaults. **Stompable Enemy 2D:** defaults. **Sprite Flipbook:** Frames `Characters/tile_0018`, `tile_0019`; Frames Per Second `4` |
| `Flyer` | `Characters/tile_0024`, order `5` | Circle Collider 2D, **Is Trigger**, Radius `0.35` | **Waypoint Mover 2D:** Stops `4, 0`; Speed `2`; Wait At Stops `0`. **Damage On Touch:** defaults. **Sprite Flipbook:** Frames `Characters/tile_0024`, `tile_0025`, `tile_0026`, `tile_0025`; Frames Per Second `8` |

The Walker uses **Stompable Enemy 2D** in place of Damage On Touch. Don't add both.

### Level Systems

This prefab holds everything a level needs besides the level itself: the HUD, the menus, the rules and the pit. Create an empty GameObject named `Level Systems` at Position `0, 0, 0`, with these children.

**`Scene Changer`** — a **Scene Changer** with Scene Name left empty.

**`To Menu`** — a **Scene Changer** with Scene Name `Platformer_Menu`.

**`Game Rules`**

| Component | Settings |
|---|---|
| Int Variable Condition | Variable `Lives`, Comparison **At Most**, Value `0`, Only Once ticked, Raise Event `GameOver` |
| Variable Resetter | Variables: `Lives`, `Coins`. **Untick** Reset When Scene Starts, so lives and coins carry from level to level |

**`Pit`** — Position `0, -12, 0`. A **Box Collider 2D** with Is Trigger ticked and Size `400, 2`, and a **Kill Zone**.

**`HUD`** — a UI Document with Source Asset `PlatformerHUD` (from `Kits/Platformer/UI`) and Sort Order `0`, plus a **UI Variable Binder**:

| Label Name | Variable | Format |
|---|---|---|
| `health-label` | `PlayerHealth` | `Health: {0}` |
| `lives-label` | `Lives` | `Lives: {0}` |
| `coins-label` | `Coins` | `Coins: {0}` |

**`Pause Menu`** — a UI Document with Source Asset `PauseMenu` (from `Core/UI`) and Sort Order `1`.

| Component | Settings |
|---|---|
| UI Screen | Hidden At Start ticked, Select When Shown `resume-button` |
| Pause Controller | fills itself in |
| UI Button Events | `resume-button` → `Pause Menu`, **PauseController → Resume**. `restart-button` → `Scene Changer`, **SceneChanger → ReloadScene**. `menu-button` → `To Menu`, **SceneChanger → Load** |

**`Level Complete`** — a UI Document with Source Asset `LevelComplete` (from `Kits/Platformer/UI`) and Sort Order `2`.

| Component | Settings |
|---|---|
| UI Screen | Hidden At Start ticked, Select When Shown `next-button` |
| UI Variable Binder | `coins-label`, `Coins`, `Coins: {0}` |
| Void Event Listener | Channel `LevelCompleted`. Response 1: `Level Complete`, **UIScreen → Show**. Response 2: the `InputReader` asset, **InputReader → DisablePlayerInput** |
| UI Button Events | `next-button` → `Scene Changer`, **SceneChanger → LoadNextScene**. `menu-button` → `To Menu`, **SceneChanger → Load** |

**`Game Over`** — a UI Document with Source Asset `GameOver` (from `Core/UI`) and Sort Order `3`.

| Component | Settings |
|---|---|
| UI Screen | Hidden At Start ticked, Select When Shown `try-again-button` |
| UI Variable Binder | `score-label`, `Coins`, `Coins: {0}` |
| Void Event Listener | Channel `GameOver`. Response 1: `Game Over`, **UIScreen → Show**. Response 2: the `InputReader` asset, **InputReader → DisablePlayerInput** |
| UI Button Events | `try-again-button` → two responses, in this order: `Game Rules`, **VariableResetter → ResetAll**; then `Scene Changer`, **SceneChanger → ReloadScene**. `menu-button` → `To Menu`, **SceneChanger → Load** |

Drag `Level Systems` into `Sample/Prefabs`, and **keep** one in the scene.

## Part 4 — Tiles

1. Open **Window → 2D → Tile Palette** and create a new palette named `Platformer Palette`, saved in `Sample/Tiles`.
2. In the Project window, open the art pack's `Tiles` folder. Select all the sprites directly in it (`tile_0000` to `tile_0179`, not the subfolders) and drag them into the palette. Save the tile assets in `Sample/Tiles`.
3. In the scene, create a Tilemap (**GameObject → 2D Object → Tilemap → Rectangular**) and name it `Ground`. Add a **Tilemap Collider 2D** and a **Composite Collider 2D**, set the Rigidbody 2D's **Body Type** to **Static**, and set the Tilemap Collider's **Composite Operation** to **Merge**.
4. Right-click `Grid` and add a second Tilemap named `Decor`, with no collider. Set its Tilemap Renderer's **Order in Layer** to `-1`.

Tiles worth knowing:

| Use | Tiles |
|---|---|
| Ground surface: left end, middle, right end | `tile_0021`, `tile_0022`, `tile_0023` |
| Dirt under the surface | `tile_0121`, `tile_0122`, `tile_0123` |
| Floating ledge: left, middle, right | `tile_0001`, `tile_0002`, `tile_0003` |
| A single block | `tile_0000` |
| Crate, brick | `tile_0026`, `tile_0006` |
| Plants, signs, clouds (for `Decor`) | `tile_0124`–`tile_0129`, `tile_0084`–`tile_0088`, `tile_0153`–`tile_0156` |

The pack also has sand (`tile_0040`–`tile_0063`) and snow (`tile_0080`–`tile_0103`) versions of the ground.

## Part 5 — Level 1

1. Add the `Player` prefab near the left end of where the level will start.
2. Select `Player` in the Hierarchy and choose **GameObject → Cinemachine → Targeted Cameras → 2D Camera**. Set the Lens **Orthographic Size** to `5`.
3. Add a `Camera Bounds` object with a trigger Box Collider 2D that covers the level, and give the Cinemachine camera a **Cinemachine Confiner 2D** that uses it, as in Exercise 04.
4. Paint and place the level. Each beat introduces one thing:

| Beat | What to build | What it shows |
|---|---|---|
| 1 | Flat ground with three `Coin`s | Collecting |
| 2 | A two-tile gap with a coin above it | Jumping |
| 3 | A flat stretch with a `Walker`, boxed in by a block at each end | Stomping |
| 4 | A `Checkpoint` | Checkpoints |
| 5 | A wide gap with a `Moving Platform` crossing it | Moving platforms |
| 6 | A `Spring` up to a high ledge that holds the `Key`, with two `One-Way Platform`s as steps | Springs, one-way platforms, the key |
| 7 | A `Lock` block in a wall of ground tiles, blocking the way on | Key and lock |
| 8 | A `Heart`, then two `Spikes`, then a gap with a `Flyer` crossing it | Health, hazards, a flying enemy |
| 9 | The `Goal Gem` | Finishing the level |

5. Decorate with the `Decor` Tilemap.
6. Save the scene.

## Part 6 — Level 2

1. With `Platformer_Level1` open, choose **File → Save As…** and save it as `Platformer_Level2`.
2. Repaint it as a shorter, harder level. Use the same prefabs in new combinations, such as a Walker on a Moving Platform, or Spikes under a row of One-Way Platforms.

## Part 7 — Menu scene

1. Create a new 2D scene and save it as `Platformer_Menu`.
2. Create these objects:

**`Main Menu`** — a UI Document with Source Asset `PlatformerMenu` (from `Kits/Platformer/UI`).

| Component | Settings |
|---|---|
| UI Screen | Select When Shown `play-button` |
| Scene Changer | Scene Name `Platformer_Level1` |
| UI Button Events | `play-button` → `Main Menu`, **SceneChanger → Load**. `credits-button` → `Credits`, **UIScreen → Show**. `quit-button` → `Main Menu`, **SceneChanger → QuitGame** |

**`Credits`** — a UI Document with Source Asset `Credits` (from `Core/UI`) and Sort Order `1`.

| Component | Settings |
|---|---|
| UI Screen | Hidden At Start ticked, Select When Shown `back-button` |
| UI Credits | Credit Files: `Course Credits` (from `Assets/_Course/Credits`) |
| UI Button Events | `back-button` → `Credits`, **UIScreen → Hide** |

**`Game Rules`** — a **Variable Resetter** with Variables `Lives` and `Coins`, and Reset When Scene Starts **ticked**. Every visit to the menu starts a new game.

## Part 8 — Win scene

1. Create a new 2D scene and save it as `Platformer_Win`.
2. Create these objects:

**`To Level 1`** — a **Scene Changer** with Scene Name `Platformer_Level1`.

**`To Menu`** — a **Scene Changer** with Scene Name `Platformer_Menu`.

**`Game Rules`** — a **Variable Resetter** with Variables `Lives` and `Coins`, and Reset When Scene Starts **unticked**.

**`Win Screen`** — a UI Document with Source Asset `EndScreen` (from `Core/UI`).

| Component | Settings |
|---|---|
| UI Screen | Select When Shown `play-again-button` |
| UI Variable Binder | `score-label`, `Coins`, `Coins: {0}` |
| UI Button Events | `play-again-button` → two responses, in this order: `Game Rules`, **VariableResetter → ResetAll**; then `To Level 1`, **SceneChanger → Load**. `menu-button` → `To Menu`, **SceneChanger → Load** |

## Part 9 — Scene List

Open **File → Build Profiles → Open Scene List** and add the four scenes, next to each other and in this order:

1. `Platformer_Menu`
2. `Platformer_Level1`
3. `Platformer_Level2`
4. `Platformer_Win`

The Level Complete screen's **Next Level** button loads whichever scene comes next in the list.

## Part 10 — Test

Start from `Platformer_Menu` and check each line.

- [ ] Play, Credits and Back work on the menu.
- [ ] The character walks, jumps and changes sprite when walking and in the air.
- [ ] Coins spin, are collected, and the HUD counts them.
- [ ] Landing on a Walker removes it and bounces the player. Touching its side costs health.
- [ ] The player rides the Moving Platform without sliding off, in both directions.
- [ ] The player can jump up through a One-Way Platform and stand on it.
- [ ] The Spring launches the player and shows its fired sprite for a moment.
- [ ] The Key removes the Lock.
- [ ] Spikes and the Flyer cost health. The Heart gives health back, and floating numbers appear.
- [ ] The Checkpoint turns from grey to white, and the player returns there after dying.
- [ ] Each death costs a life. At 0 lives the Game Over screen appears, and Try Again starts with 3 lives.
- [ ] Falling into the pit costs a life.
- [ ] The Goal Gem shows Level Complete, and Next Level loads Level 2, then the Win scene.
- [ ] Coins and lives carry from Level 1 to Level 2, and reset from the menu.
- [ ] Esc pauses, and Resume, Restart and Main Menu work.

Note anything that fails, with the Console message if there is one.

## Part 11 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

When the kit is released, export it with **Assets → Export Package**. Include `Assets/_Course/Kits/Platformer` and `Assets/_Course/Art/Kenney/kenney_pixel-platformer`. Untick everything else that Unity adds as a dependency: students already have the Core and 2D scripts in their project, at the version their project was made from.
