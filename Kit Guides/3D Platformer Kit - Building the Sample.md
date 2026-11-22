---
title: "3D Platformer Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - 3d
  - instructor
---

# 3D Platformer Kit — Building the Sample

**For the instructor.** These steps build the kit's sample level once, in the template project. Building it tests every kit script and the course's 3D scripts, and the result is what students import. Students read **3D Platformer Kit**, not this page.

Everything goes in `Assets/_Course/Kits/Platformer3D/Sample/`, with folders `Data`, `Materials`, `Prefabs` and `Scenes`. The level is built from Unity's basic shapes; no art pack is needed.

## Before you start

1. Pull the template project. It should be version 0.22.0 or later, with no red errors in the Console.
2. Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data and materials

In `Sample/Data`: `Coins` and `PlayerHealth` (Int Variables, `0` and `3`), `LevelWon` (Void Event Channel).

In `Sample/Materials`, four materials (**Create → Material**, shader **Universal Render Pipeline/Lit**): `Grass` (Base Map color `6DBE45`), `Stone` (`9A9AA6`), `Coin` (`FFD23F`, Emission ticked, same color), `Danger` (`E04848`). And `Shadow`: shader **Universal Render Pipeline/Particles/Unlit**, Surface Type **Transparent**, Base Map the built-in `Default-Particle` texture (click the circle beside Base Map and search for it), color black at 60% alpha.

## Part 2 — The scene and camera

1. **File → New Scene → Basic (URP)** if offered, otherwise **Basic (Built-in)**; save it as `Sample/Scenes/Islands_Level`.
2. Main Camera → **Rendering → Renderer**: **Universal Renderer**. Main Camera → **Environment → Background Type**: Skybox (or a solid sky blue `8FD3FF`).

## Part 3 — The player

1. An empty `Player` at `0, 1, 0`, tagged **Player**. Children: a Capsule `Body` at `0, 1, 0` (remove its collider, material `Stone`), and a small Cube `Nose` at `0, 1.5, 0.45`, Scale `0.3, 0.2, 0.4` (remove its collider), so you can see which way it faces.
2. On `Player`: **Player Controller 3D** (it adds a Character Controller: Height `2`, Radius `0.4`, Center `0, 1, 0`). Facing **Face Movement**; Walk Speed `6`, Sprint Speed `9`; Jump Height `2.2`, Extra Air Jumps `0`; Can Crouch unticked.
3. **Health**: Max Health `3`, Invulnerable Time `1`, Health Variable `PlayerHealth`. **Respawner**: Respawn When Health Runs Out ticked.
4. A Quad `Player Shadow`, **not** a child of the player, material `Shadow`, no collider. On `Player`, **Blob Shadow 3D**: Shadow `Player Shadow`, Size `0.9`.
5. Make `Player` a prefab in `Sample/Prefabs`.

## Part 4 — The orbit camera

1. **GameObject → Cinemachine → Cinemachine Camera**. Name it `Orbit Camera`. Tracking Target `Player`.
2. **Position Control: Orbital Follow**. Orbit Style **Sphere**, Radius `7`, Target Offset `0, 1.2, 0`. Under **Vertical Axis**, Range `-10` to `60`, Value `20`.
3. **Rotation Control: Rotation Composer**, Target Offset `0, 1.2, 0`.
4. Click **Add Input Controller** (or **Add Component → Cinemachine Input Axis Controller**). For **Look Orbit X** and **Look Orbit Y**, set the **Input Action** to `Player/Look` from `Assets/_Course/Core/Input/InputSystem_Actions` if it's empty. If moving the mouse up turns the camera the wrong way, change the sign of Look Orbit Y's **Gain**.
5. **Add Extension → Cinemachine Deoccluder**, so islands between the camera and the player don't hide them.
6. On any object, add **Cursor Lock 3D**.
7. Press **Play** on a big flat Cube floor: the player walks relative to the camera, and the mouse orbits.

## Part 5 — Prefabs

In `Sample/Prefabs`:

| Prefab | Build |
|---|---|
| `Coin` | A Cylinder, Scale `0.6, 0.05, 0.6`, rotated `90, 0, 0`, material `Coin`. Replace its collider with a **Sphere Collider** (Is Trigger, Radius `0.8`). **Collectible**: Add To `Coins`, Amount `1`. **Spin 3D**: Spin `0, 0, 180` (it's on its side), Bob Height `0.15` |
| `Checkpoint` | A thin Cylinder pole, `Stone`, with a Box Collider trigger `2 × 3 × 2`, and **Checkpoint**. A child `Respawn Point` just in front |
| `Moving Platform` | A Cube `3 × 0.5 × 3`, `Stone`, **Moving Platform 3D**: Speed `2.5`, Wait Time `0.8`, Back And Forth; two child empties `A` and `B` |
| `Crumbling Platform` | A Cube `2 × 0.4 × 2`, `Grass` darkened, **Crumbling Platform 3D**: Hold Time `0.6`, Return Time `3` |
| `Bounce Pad` | A flat Cylinder `1.5 × 0.1 × 1.5`, `Danger`, with a Box Collider trigger above it, **Bounce Pad 3D**: Height `7` |
| `Patrol Enemy` | A Cube `1 × 1 × 1`, `Danger`, collider Is Trigger, a child Cube for eyes, **Patrol Enemy 3D**: Speed `2`, Damage `1`, Can Be Stomped ticked, Stomp Bounce `3`; two child empties for its points |

## Part 6 — The level

Build in the order the player meets it. Islands are scaled Cubes with `Grass` on top (a thin Cube) and `Stone` below. Keep gaps to 3 units or less (4 where the player can take a run-up and sprint), and every step up to 1.5 or less.

**Start** — an island `10 × 2 × 10` at the origin. `Player` on it. Five coins in a line leading toward Area 1.

**Area 1: Stepping Stones** — six small islands `3 × 1 × 3`, each a little higher than the last, with 2–3 unit gaps, curving to the left. A `Checkpoint` on the first one. Five coins, one above each gap, so collecting them means jumping.

**Area 2: Over the Drop** — a long gap crossed by two `Moving Platform`s (one moving sideways, one up and down), then a bridge of five `Crumbling Platform`s in a row. A `Checkpoint` before it. Five coins: two on the moving platforms' paths, three above the crumbling bridge.

**Area 3: The Tower** — a wide island with a tower of three stacked islands. Two `Patrol Enemy` walk the base. A `Bounce Pad` launches the player to the second level; a ledge climb of small steps reaches the top. A `Checkpoint` at the base. Five coins: two guarded by the enemies, three up the tower.

**Goal** — at the top, a tall pole with a cloth (a thin Cube, `Danger`) and a trigger with **Trigger Zone**: Only Once, Raise On Enter `LevelWon`.

**Kill Zone** — a big Box Collider trigger `400 × 2 × 400` at `y = -15`, with **Kill Zone**.

Count the coins: twenty.

## Part 7 — Islands Systems

An empty `Islands Systems`, made into a prefab, with:

**`HUD`** — UI Document `HUD` (Core), **UI Variable Binder**: `health-label` → `PlayerHealth` → `Hearts: {0}`; `score-label` → `Coins` → `Coins: {0} / 20`.

**`Reset`** — a **Variable Resetter** with `Coins` and `PlayerHealth`.

**`Pause Menu`**, **`Settings`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Won`** — UI Document `EndScreen`, hidden, shown on `LevelWon`; `score-label` → `Coins` → `Coins: {0} / 20`. Its Void Event Listener also calls **CursorLock3D → Unlock**.

## Part 8 — Menu

`Islands_Menu`, like the Platformer sample's menu, with Play loading `Islands_Level`. Scene List: `Islands_Menu`, `Islands_Level`.

## Part 9 — Test

- [ ] The pointer is hidden while playing, and back while paused and on the win screen.
- [ ] The mouse and right stick orbit the camera; up on the stick always moves away from the camera; the player turns to face where they walk.
- [ ] Holding Space jumps higher than tapping it; jumping just after walking off a ledge still works; Shift sprints.
- [ ] The blob shadow sits under the player on every surface, and shrinks the higher they are.
- [ ] Coins spin and bob, and count up on the HUD; all twenty can be reached.
- [ ] The player rides both moving platforms without sliding off.
- [ ] Crumbling platforms shake, fall, and return after 3 seconds.
- [ ] The bounce pad launches the player high enough to reach the tower's second level.
- [ ] Landing on an enemy removes it and bounces the player; walking into one costs a heart and gives a moment of invulnerability.
- [ ] At 0 hearts, or falling off, the player returns to the last checkpoint touched, with full health.
- [ ] Walls and islands between the camera and the player don't hide them for long.
- [ ] Touching the flag shows the win screen with the coin count.
- [ ] **Feel:** play the level twice. Note any jump that's too hard, and any spot where the camera gets in the way.

Note anything that fails, with the Console message.

## Part 10 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/Platformer3D` with **Assets → Export Package**, unticking Core and 3D scripts that Unity adds as dependencies.
