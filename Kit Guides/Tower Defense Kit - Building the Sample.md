---
title: "Tower Defense Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.17.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Tower Defense Kit — Building the Sample

**For the instructor.** These steps build the kit's sample map once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Tower Defense Kit**, not this page.

Everything goes in `Assets/_Course/Kits/TowerDefense/Sample/`, with folders `Data`, `Towers`, `Prefabs` and `Scenes`.

## Before you start

1. Pull the template project. It should be version 0.17.0 or later, with no red errors in the Console.
2. **Art.** Kenney's **Tower Defense (top-down)** pack is already in `Assets/_Course/Art/Kenney/kenney_tower-defense-top-down` (use `PNG/Default size`). Its tiles are 64 pixels, so one tile is one unit.
3. Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data

In `Sample/Data`:

| Asset | Type |
|---|---|
| `Money`, `Lives`, `Wave` | Int Variable |
| `MapWon`, `MapLost` | Void Event Channel |

## Part 2 — Projectiles and towers

**Projectiles** (prefabs with **Tower Projectile 2D**, a small sprite pointing right, Order in Layer `20`): `Arrow`, `Cannonball` (Hit Effect: a small explosion sprite with a **Lifetime** of `0.3`), `Frost Bolt` (tinted pale blue).

**Tower prefabs**: each a base sprite (Order in Layer `5`) with **Tower 2D**, a child `Turret` sprite pointing right (Order `6`), and a child `Range` using a circle sprite 1 unit across, tinted white at 20% opacity (Order `1`), dragged into **Range Indicator**. Make `Archer Tower`, `Cannon Tower` and `Frost Tower`, with a different turret sprite each. Targeting **First**.

**Tower assets**, in `Sample/Towers` (**Create → Collin Game → Tower Defense Kit → Tower**):

| Asset | Prefab | Cost | Range | Damage | Shots/s | Projectile | Splash | Slow | Upgrades to |
|---|---|---|---|---|---|---|---|---|---|
| `Archer` | Archer Tower | `50` | `3` | `1` | `2` | Arrow, speed `12` | `0` | `1` | Archer II |
| `Archer II` | — | `60` | `3.5` | `2` | `2.5` | Arrow, speed `14` | `0` | `1` | — |
| `Cannon` | Cannon Tower | `90` | `2.5` | `3` | `0.6` | Cannonball, speed `6` | `1.2` | `1` | Cannon II |
| `Cannon II` | — | `110` | `3` | `5` | `0.7` | Cannonball, speed `7` | `1.5` | `1` | — |
| `Frost` | Frost Tower | `70` | `2.5` | `0` | `1` | Frost Bolt, speed `10` | `0.8` | `0.5`, `2` s | Frost II |
| `Frost II` | — | `70` | `3` | `0` | `1.2` | Frost Bolt, speed `12` | `1.2` | `0.35`, `2.5` s | — |

Upgrades leave Prefab empty, so the same tower object carries on with the new numbers.

## Part 3 — Enemies

Each: a sprite (Order in Layer `10`), **Health** (When Health Runs Out **Destroy**, Invulnerable Time `0`), **Path Enemy 2D**. No collider.

| Prefab | Health | Speed | Reward | Lives Taken |
|---|---|---|---|---|
| `Scout` | `3` | `2.5` | `4` | `1` |
| `Soldier` | `8` | `1.5` | `6` | `1` |
| `Brute` | `30` | `0.9` | `15` | `3` |
| `Swarmling` (smaller sprite) | `2` | `2` | `2` | `1` |

## Part 4 — TD Systems

An empty `TD Systems`, made into a prefab, with these children:

**`Waves`** — **Tower Wave Spawner**: Path (set in the scene), Money `Money`, Starting Money `120`, Lives `Lives`, Starting Lives `20`, Wave Number `Wave`, Raise When Won `MapWon`. Waves:

| Wave | Groups (count × enemy, seconds between) | Bonus |
|---|---|---|
| 1 | 6 × Scout, `1.2` | `20` |
| 2 | 10 × Scout, `0.9` | `20` |
| 3 | 6 × Soldier, `1.2` | `25` |
| 4 | 8 × Scout `0.6`; 6 × Soldier `1` | `25` |
| 5 | 2 × Brute, `3` | `30` |
| 6 | 20 × Swarmling, `0.4` | `30` |
| 7 | 10 × Soldier `0.8`; 2 × Brute `2.5` | `35` |
| 8 | 30 × Swarmling `0.3`; 8 × Scout `0.5` | `35` |
| 9 | 4 × Brute `2`; 12 × Soldier `0.6` | `40` |
| 10 | 25 × Swarmling `0.3`; 6 × Brute `2`; 15 × Soldier `0.5` | `0` |

**`Lose`** — **Int Variable Condition**: Variable `Lives`, At Most `0`, Raise Event `MapLost`.

**`HUD`** — UI Document `TowerHUD` (from `Kits/TowerDefense/UI`), with **UI Build Menu** (Towers: `Archer`, `Cannon`, `Frost`; Money `Money`; Spawner `Waves`), and a **UI Variable Binder**: `money-label` → `Money` → `${0}`; `lives-label` → `Lives` → `Lives: {0}`; `wave-label` → `Wave` → `Wave {0} / 10`.

**`Pause Menu`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Won`** — UI Document `EndScreen`, hidden, shown by a **Void Event Listener** on `MapWon`; `score-label` → `Lives` → `Lives left: {0}`.

**`Lost`** — UI Document `GameOver`, hidden, shown on `MapLost`; Try Again → **ReloadScene**.

## Part 5 — The map (`TD_Map`)

1. Main Camera: Orthographic, Size `6`, at `0, 0, -10`. No Cinemachine.
2. A Tilemap of grass covering the view, and a second Tilemap for the road, winding from the left edge to the right edge with five or six bends.
3. `Path`: an **Enemy Path 2D** with a child at each bend of the road, starting just off the left edge and ending just off the right.
4. Eight `Build Spot` prefabs (a stone pad sprite with a **Circle Collider 2D** of radius `0.45` and **Build Spot 2D**), on the insides of bends where they reach two stretches of road.
5. `TD Systems`, with Waves → **Path** set to `Path`.

## Part 6 — Menu

`TD_Menu`, like the Platformer sample's menu, with Play loading `TD_Map`.

## Part 7 — Scene List

`TD_Menu`, `TD_Map`.

## Part 8 — Test

- [ ] Money starts at 120, lives at 20; the HUD shows them.
- [ ] Clicking a pad opens the build menu; towers you can't afford are grey; clicking grass closes it.
- [ ] Building takes the money and places the tower; the turret turns to enemies in range.
- [ ] Clicking a tower shows its range, the upgrade price and the sale value.
- [ ] Upgrading changes the tower's numbers; selling returns 60% of what was spent.
- [ ] Start Wave is grey during a wave and lights up after it, with the bonus added.
- [ ] Arrows hit one enemy; cannonballs hit a group; frost slows enemies visibly.
- [ ] Enemies reaching the end cost lives; at 0 lives, the lost screen shows.
- [ ] Clearing wave 10 shows the won screen with lives left.
- [ ] Clicking the HUD's buttons never opens or closes the build menu by mistake.
- [ ] Esc pauses.
- [ ] **Balance:** a first-time player can win with some losses. Note which waves feel too easy or too hard.

Note anything that fails, with the Console message.

## Part 9 — Commit

Commit and push the `Sample` folder with its `.meta` files, and the art folder.

## Later — Exporting the kit

Export `Assets/_Course/Kits/TowerDefense` and the art folder with **Assets → Export Package**, unticking Core scripts that Unity adds as dependencies.
