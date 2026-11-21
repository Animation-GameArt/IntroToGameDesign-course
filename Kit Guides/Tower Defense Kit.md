---
title: "Tower Defense Kit"
course: GAME 1303
status: draft
course_version: 0.17.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Tower Defense Kit

The Tower Defense Kit is a starting point for games where enemies walk a path and the player stops them by building towers beside it. The loop: earn money, build or upgrade a tower, start the wave, watch what gets through, and adjust. Examples: Bloons TD, Kingdom Rush, the early waves of Plants vs. Zombies.

The sample is one map with three towers (each with an upgrade), four kinds of enemy and ten waves.

Most of the work in a tower defense game is **balancing**: tower costs, damage, enemy health and wave sizes. The kit keeps all of those as numbers in assets and Inspector fields, so you can change them between playtests without touching code.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| A path with any number of corners | Enemies that choose their own way through a maze |
| Towers as assets: cost, range, damage, fire rate, projectile, splash, slow | Towers with special abilities you trigger by hand |
| Targeting the first, closest or strongest enemy in range | Air and ground enemies that only some towers can hit |
| Fixed building spots, build menu, upgrades and selling | Placing towers anywhere on the map |
| Waves started by the player or by themselves, with a bonus for clearing each | Several maps with a world map |
| Money, lives, win and lose | Long upgrade trees |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Tower Defense Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/TowerDefense/Sample/Scenes`, add `TD_Menu` and `TD_Map`, next to each other, in that order.
4. Open `TD_Menu` and press **Play**.

Tower defense is played with the **mouse** (or a touch screen): click a stone pad to build, click a tower to upgrade or sell it, click **Start Wave** when you're ready. **Esc** pauses.

## What's in the sample

| Asset or prefab | What it is | Settings worth changing |
|---|---|---|
| `Archer`, `Archer II` | Tower assets: cheap, fast, short range; the upgrade hits harder | **Cost**, **Range**, **Damage**, **Shots Per Second** |
| `Cannon`, `Cannon II` | Slow, expensive, splash damage | **Splash Radius** |
| `Frost`, `Frost II` | No damage, but slows enemies | **Slow To**, **Slow Seconds** |
| `Scout`, `Soldier`, `Brute`, `Swarmling` | Enemies: fast and weak, average, slow and tough, tiny in large groups | Path Enemy 2D **Speed**, **Reward**, **Lives Taken**; Health **Max Health** |
| `Build Spot` | A stone pad that takes one tower | |
| `TD Systems` | HUD, build menu, wave spawner, win and lose screens | The waves on **Tower Wave Spawner** |

## How the sample fits together

**The path.** `Path` is an **Enemy Path 2D**: its children are the corners, in order. Select it to see the route (green start, red end).

**Enemies.** The **Tower Wave Spawner** creates each enemy at the start of the path and hands it the path. A **Path Enemy 2D** walks from corner to corner. If it reaches the end, the player loses **Lives Taken** lives; if its Health runs out first, the player earns its **Reward**.

**Towers.** A **Tower** asset holds a tower's numbers. A **Tower 2D**, on the tower prefab, looks for enemies within range, picks one by its **Targeting** (First, the one furthest along, is usually best), turns its turret, and fires. With a projectile, a **Tower Projectile 2D** flies to the enemy; without one, the hit is instant. Splash damage hits every enemy near the target; frost slows them.

**Building.** Clicking a **Build Spot 2D** opens the **UI Build Menu**: a button per tower with its price, greyed out if the player can't afford it. On a spot with a tower, the menu offers the upgrade and a sale (which returns part of what was spent), and shows the tower's range.

**Waves.** The player presses **Start Wave**. When every enemy of the wave is gone, the player gets the wave's **Bonus**, and the button lights up again. Clearing the last wave raises `MapWon`. Lives reaching 0 raises `MapLost` through an Int Variable Condition.

## Start your own game

1. Create a new 2D scene in `Assets/_Game/Scenes`, and set the Main Camera's **Size** so the whole map fits.
2. Paint the ground and the road (a Tilemap works well).
3. Add an empty `Path` with **Enemy Path 2D**, and an empty child for each corner of the road, in order. Put the first just off screen where enemies enter, and the last where they leave.
4. Drag in `TD Systems` from the kit's `Sample/Prefabs`, and set the Tower Wave Spawner's **Path** to your path.
5. Place `Build Spot` prefabs beside the road. Spots on the inside of bends reach the most road.
6. Press **Play**, build, and start a wave.

### Changing towers and enemies

Duplicate a Tower asset or make a Prefab Variant of an enemy (right-click → **Create → Prefab Variant**), move it to `Assets/_Game`, and change the copy. Add new towers to the UI Build Menu's **Towers** list.

## Balancing

- **Start with money for one tower**, and make the first wave beatable with one well-placed tower.
- **Each tower needs a job.** Fast single-target, slow splash, slowing. If one tower is best at everything, nobody builds the others.
- **Work out damage per second:** Damage × Shots Per Second. Compare it with the enemies' health × how many come per second.
- **Change one number at a time** between playtests, and write down what changed.
- **Watch where enemies leak.** That's the spot that needs a tower, or the wave that's too strong.

## Recipes

**A sniper.** Range `8`, Damage `5`, Shots Per Second `0.4`, Targeting **Strongest**.

**A machine gun.** Range `2.5`, Damage `1`, Shots Per Second `6`, no projectile (instant hits).

**A boss.** An enemy variant with Max Health `200`, Speed `0.8`, Lives Taken `10`, and a larger sprite. Put one at the end of the last wave.

**Waves that start by themselves.** Tick **Start Waves Automatically** on the Tower Wave Spawner, and set **Seconds Between Waves**.

**A harder map.** Lower **Starting Money** and **Starting Lives**, and raise each wave's counts.

**Sounds.** Each Tower asset has a **Sound** for its shots; Build Spot 2D has **On Built** and **On Sold**; Path Enemy 2D has **On Reached End**.

## If something goes wrong

| What you see | What to do |
|---|---|
| Enemies don't move | The Tower Wave Spawner needs a **Path** with at least two child points |
| Enemies walk off in a straight line | The path's corners must be **children** of the Path object, in order |
| Clicking a spot does nothing | The spot needs a 2D collider. Check nothing in the UI (such as a full-screen panel) covers it |
| The build buttons are greyed out | Not enough money. Check **Starting Money**, or the tower's **Cost** |
| Towers don't shoot | The tower prefab needs a **Tower 2D**, and it gets its numbers from the Tower asset that built it; place towers by building them, not by dragging the prefab in |
| Towers shoot the wrong enemy | Change **Targeting** on the tower prefab |
| Projectiles miss | Fast enemies can outrun slow projectiles: raise **Projectile Speed** |
| Start Wave stays grey | A wave is still in progress: some enemy is still on the path |
| The game never ends | The last wave must be cleared; check every enemy can reach the end or be defeated |
