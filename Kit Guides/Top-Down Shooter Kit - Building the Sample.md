---
title: "Top-Down Shooter Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.14.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Top-Down Shooter Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Top-Down Shooter Kit**, not this page.

Everything goes in `Assets/_Course/Kits/TopDownShooter/Sample/`, with folders `Data`, `Prefabs`, `Scenes` and `Weapons`.

## Before you start

1. Pull the template project. It should be version 0.14.0 or later, with no red errors in the Console.
2. **Art.** Kenney's **Pixel Shmup** pack is already in `Assets/_Course/Art/Kenney/kenney_pixel-shmup`. Its sprites are 16 pixels, so one tile is one unit.
3. **Tags.** In **Project Settings → Tags and Layers**, add `Enemy` if it isn't there.
4. **Panel Settings.** Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data

In `Sample/Data`:

| Asset | Type | Initial value |
|---|---|---|
| `Score`, `Wave` | Int Variable | `0` |
| `PlayerHealth` | Int Variable | `5` |
| `WeaponName` | String Variable | empty |
| `ArenaCleared`, `PlayerDied`, `ReachedBoss`, `BossDefeated` | Void Event Channel | |

## Part 2 — Projectiles and weapons

**Projectiles**, built in a scratch scene and saved to `Sample/Prefabs`:

| Prefab | Sprite | Collider | Projectile 2D |
|---|---|---|---|
| `Player Bullet` | a small yellow shot, pointing up, Order in Layer `8` | Circle Collider 2D, **Is Trigger**, Radius `0.15` | Target Tag `Enemy`, Lifetime `1.5` |
| `Enemy Bullet` | a small red or pink shot, Order in Layer `8` | Circle Collider 2D, **Is Trigger**, Radius `0.15` | Target Tag `Player`, Lifetime `3` |

Each gets a Rigidbody 2D from the Projectile 2D.

**Weapons**, in `Sample/Weapons` (**Create → Collin Game → Top-Down Shooter Kit → Weapon**):

| Asset | Projectile | Speed | Damage | Shots per second | Per shot | Spread | Inaccuracy |
|---|---|---|---|---|---|---|---|
| `Blaster` | Player Bullet | `14` | `1` | `6` | `1` | — | `0` |
| `Spread Shot` | Player Bullet | `13` | `1` | `4` | `5` | `50` | `0` |
| `Rapid Fire` | Player Bullet | `16` | `1` | `14` | `1` | — | `6` |
| `Enemy Shot` | Enemy Bullet | `6` | `1` | `1` | `1` | — | `3` |
| `Boss Spread` | Enemy Bullet | `5` | `1` | `1` | `7` | `90` | `0` |

All player weapons have Hold To Fire ticked.

## Part 3 — The player

**`Player Ship`** (arena version):

1. An empty `Player Ship`, tag `Player`.
2. A child `Turret` at `0, 0, 0`, and under it a child sprite `Hull` using a ship sprite, Order in Layer `10`. The ship sprite points up, so set the Hull's Rotation Z to `-90`: Aim 2D turns `Turret` to the aim, and expects it to point right.
3. On `Player Ship`: a **Circle Collider 2D** (Radius `0.4`), **Top Down Controller 2D** (Max Speed `6`, **Facing None**), **Aim 2D** (Aim With **Mouse Or Stick**, Turn To Aim `Turret`), **Weapon Shooter 2D** (Weapon `Blaster`, Fire When **Attack Button**, Direction **Aim**, Weapon Name `WeaponName`), **Health** (Max Health `5`, Invulnerable Time `1`, Health Variable `PlayerHealth`, Raise On Died `PlayerDied`, When Health Runs Out **Deactivate**) and **Keep On Screen 2D** (Margin `0.5`).

**`Player Ship (Scrolling)`**: a Prefab Variant of `Player Ship`. Aim 2D: Aim With **Fixed Direction**, Fixed Direction `0, 1`, Turn To Aim empty. Set `Turret` rotation to `0, 0, 90` so the ship points up.

## Part 4 — Enemies

Every enemy: a sprite, Order in Layer `5`, tag `Enemy`, a **Circle Collider 2D**, **Enemy Mover 2D** (adds the Rigidbody 2D), **Health** (When Health Runs Out **Destroy**, Invulnerable Time `0`, On Died → `Score` **Add**), and **Damage On Touch** (Target Tag `Player`).

| Prefab | Enemy Mover 2D | Health | Score | Also |
|---|---|---|---|---|
| `Drone` | Chase, Speed `2.5` | `1` | `10` | **Drop On Death 2D**: Chance `0.1`, Drops `Heart` |
| `Gunship` | Circle, Speed `2`, Preferred Distance `4` | `3` | `30` | **Weapon Shooter 2D**: Weapon `Enemy Shot`, **Automatic**, **At Target**, Auto Fire Interval `1.5`, First Shot Delay `1`. **Drop On Death 2D**: Chance `0.3`, Drops `Spread Power-Up`, `Rapid Power-Up` |
| `Weaver` | Wave, Speed `2`, Fly Direction `0, -1`, Wave Width `1.5` | `2` | `20` | **Weapon Shooter 2D**: `Enemy Shot`, Automatic, At Target, interval `2`. **Wake On Screen 2D** |
| `Boss` | Keep Away, Speed `1.5`, Preferred Distance `5`. Scale `3` | `40` | `500` | **Weapon Shooter 2D**: `Boss Spread`, Automatic, At Target, interval `1.2`. Health **Raise On Died** `BossDefeated` |

## Part 5 — Pickups

| Prefab | Components |
|---|---|
| `Heart` | Circle Collider 2D (trigger), **Collectible**: Heal `1` |
| `Spread Power-Up` | Circle Collider 2D (trigger), **Power Up 2D**: Weapon `Spread Shot`, Duration `10`, Disappear After `8` |
| `Rapid Power-Up` | The same with `Rapid Fire` |

## Part 6 — Arena Systems

An empty `Arena Systems` at `0, 0, 0`, made into a prefab, with these children:

**`HUD`** — UI Document `ShooterHUD` (from `Kits/TopDownShooter/UI`), with a **UI Variable Binder**: `health-label` → `PlayerHealth` → `Health: {0}`; `score-label` → `Score` → `Score: {0}`; `wave-label` → `Wave` → `Wave {0}`; `weapon-label` → `WeaponName` → `{0}`.

**`Pause Menu`**, **`Settings`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Game Over`** — UI Document `GameOver`, hidden, shown by a **Void Event Listener** on `PlayerDied`; `score-label` bound to `Score`; Try Again → **ReloadScene**.

**`Cleared`** — UI Document `LevelComplete` (from `Kits/Platformer/UI`), hidden, shown on `ArenaCleared`; Next → **LoadNextScene**.

**`Reset`** — a **Variable Resetter** with `Score`, `Wave` and `WeaponName`.

**`Waves`** — a **Wave Spawner 2D** with eight children as spawn points, two just outside each edge of the screen. Waves:

| Wave | Groups | Seconds between enemies |
|---|---|---|
| 1 | 6 Drones | `0.6` |
| 2 | 8 Drones, 2 Gunships | `0.5` |
| 3 | 10 Drones, 4 Gunships | `0.4` |
| 4 | 1 Boss, 6 Drones | `0.8` |

Wave Number `Wave`; Raise When Cleared `ArenaCleared`.

## Part 7 — The arena (`Shooter_Arena`)

1. Main Camera: Orthographic, Size `7`, dark background. No Cinemachine.
2. A floor: a large sprite or a Tilemap from Pixel Shmup's ground tiles.
3. Four walls just inside the camera's edges: sprites with Box Collider 2D, Order in Layer `1`.
4. `Player Ship` in the middle, and `Arena Systems`.

## Part 8 — The scrolling level (`Shooter_Scrolling`)

1. Main Camera: Orthographic, Size `7`, with **Scroll Camera 2D** (Direction `0, 1`, Speed `2`, Stop After `80`, Raise At End `ReachedBoss`).
2. A long floor or background, 18 wide and 100 tall, starting below the camera.
3. `Player Ship (Scrolling)` near the bottom of the view.
4. `Arena Systems`, with the `Waves` child switched off (this level places its enemies by hand).
5. Place about 20 `Weaver`s and a few `Gunship`s (each with a **Wake On Screen 2D** added) along the level, in small groups.
6. A `Boss` at the top of the level, with **Wake On Screen 2D**, so it wakes when the camera stops.
7. On `Arena Systems` → `Cleared`, change its listener from `ArenaCleared` to `BossDefeated`.

## Part 9 — Menu and win scenes

Build `Shooter_Menu` (Play loads `Shooter_Arena`) and `Shooter_Win` as in the Platformer Kit sample, showing `Score`.

## Part 10 — Scene List

`Shooter_Menu`, `Shooter_Arena`, `Shooter_Scrolling`, `Shooter_Win`, in that order.

## Part 11 — Test

- [ ] The ship moves with WASD and aims at the mouse; on a gamepad it aims with the right stick.
- [ ] Holding fire shoots steadily; bullets disappear at walls and after a while.
- [ ] Drones chase; Gunships circle and fire at the ship; enemy bullets cost health.
- [ ] The HUD shows health, score, wave and weapon.
- [ ] Each wave starts after the last is cleared; the boss arrives in wave 4.
- [ ] Power-ups change the weapon for 10 seconds, then the Blaster comes back; the HUD shows the weapon's name.
- [ ] Hearts heal.
- [ ] Losing all health shows Game Over; Try Again restarts the arena with score 0.
- [ ] Clearing wave 4 shows the cleared screen; Next loads the scrolling level.
- [ ] The camera scrolls up; the ship is carried along and can't leave the screen.
- [ ] Weavers stay still until they scroll into view, then weave and fire; they disappear after leaving the screen.
- [ ] The camera stops at the boss; defeating it shows the cleared screen; Next loads the win scene.
- [ ] With 200 or more bullets on screen, the game still runs smoothly (check the Stats panel in the Game view).
- [ ] Esc pauses; nothing fires while paused.

Note anything that fails, with the Console message.

## Part 12 — Commit

Commit and push the `Sample` folder with its `.meta` files, and the Pixel Shmup art folder.

## Later — Exporting the kit

Export `Assets/_Course/Kits/TopDownShooter` and the Pixel Shmup art folder with **Assets → Export Package**, unticking Core and 2D scripts that Unity adds as dependencies. The Cleared screen uses `LevelComplete` from the Platformer Kit: tick it in the export, or copy it into this kit's `UI` folder first.
