---
title: "Top-Down Shooter Kit"
course: GAME 1303
status: draft
course_version: 0.14.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Top-Down Shooter Kit

The Top-Down Shooter Kit is a starting point for shooters seen from above. It covers two styles:

- **Arena shooters**, also called twin-stick shooters: move with one stick, aim with the other or with the mouse, and survive waves of enemies. Examples: Geometry Wars, Enter the Gungeon's fights, Nuclear Throne.
- **Scrolling shooters**: the screen moves steadily up a level, and enemies fly in to meet you. Examples: 1942, Raiden, Galaga's descendants.

It adds weapons stored as assets, aiming, projectiles that are reused rather than created for every shot, enemy movement patterns, waves, power-ups and drops, and a scrolling camera. The sample has one of each: an arena with four waves and a boss, and a short scrolling level.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Aiming with the mouse or the right stick, separately from moving | Lock-on, homing or charge shots |
| Weapons as assets: fire rate, spread, accuracy, damage, projectile | Ammo and reloading |
| Hundreds of bullets at once, running smoothly | Bullets that bounce or pierce |
| Enemies that chase, fly straight, weave, circle or keep their distance | Enemies that find their way around walls |
| Waves that start when the last one is cleared, and endless waves | Randomly generated rooms |
| Power-ups that swap the weapon for a time, and random drops | Upgrade trees and shops |
| A scrolling camera, enemies that wake as they scroll into view | Scrolling backgrounds with several layers |
| A boss: an enemy with lots of health and several weapons | Boss attack phases (a custom script) |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Top-Down Shooter Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/TopDownShooter/Sample/Scenes`, add these scenes, next to each other and in this order: `Shooter_Menu`, `Shooter_Arena`, `Shooter_Scrolling`, `Shooter_Win`.
4. Open `Shooter_Menu` and press **Play**.

| Action | Keyboard and mouse | Gamepad |
|---|---|---|
| Move | **WASD** | Left stick |
| Aim | Mouse | Right stick |
| Fire | Left mouse button or **Enter** (hold) | Left face button (hold) |
| Pause | **Esc** | **Start** |

## What's in the sample

| Prefab or asset | What it is | Settings worth changing |
|---|---|---|
| `Player Ship` | Top Down Controller 2D, Aim 2D, Weapon Shooter 2D, Health, Keep On Screen 2D | Max Speed; Health **Max Health** |
| `Blaster`, `Spread Shot`, `Rapid Fire` | The player's weapons (Weapon assets) | **Shots Per Second**, **Projectiles Per Shot**, **Spread Angle**, **Damage** |
| `Enemy Shot`, `Boss Spread` | The enemies' weapons | |
| `Player Bullet`, `Enemy Bullet` | Projectiles: one hurts `Enemy`, the other `Player` | **Target Tag**, **Lifetime** |
| `Drone` | Chases the player; hurts on touch | Enemy Mover 2D **Speed** |
| `Gunship` | Circles the player at a distance and fires at them | **Preferred Distance**, **Auto Fire Interval** |
| `Weaver` | Flies down the screen, weaving; for the scrolling level | **Wave Width**, **Waves Per Second** |
| `Boss` | Lots of health; keeps its distance and fires a spread | Health **Max Health**, its weapon |
| `Spread Power-Up`, `Rapid Power-Up` | Give the player a weapon for 10 seconds | **Weapon**, **Duration** |
| `Arena Systems` | HUD, pause, win and game over screens, and the wave spawner | The waves on **Wave Spawner 2D** |

## How the sample fits together

**Aiming and firing.** The player's **Aim 2D** works out where they're aiming: at the mouse pointer, or the way the right stick points. Their **Weapon Shooter 2D** fires the current weapon that way while the fire button is held. The **Weapon** asset says how fast, how many bullets, how spread out and how much damage.

**Bullets.** Each bullet is a **Projectile 2D**. It flies straight, damages the first thing it hits that has Health and the right tag, and is then put away to be reused. Player bullets hurt `Enemy`; enemy bullets hurt `Player`. Neither ever hits whoever fired it.

**Enemies.** An **Enemy Mover 2D** gives each enemy a pattern. Gunships and the Boss also have a Weapon Shooter 2D set to **Automatic** and **At Target**, so they fire at the player on a timer. When an enemy's health runs out, its Health's **On Died** adds to `Score`, and its **Drop On Death 2D** sometimes leaves a power-up or a heart.

**Waves.** The arena's **Wave Spawner 2D** lists four waves. Each wave's enemies appear at random spawn points just off screen; the next wave starts once every enemy of the current one is gone. After the last wave it raises `ArenaCleared`, which shows the win screen. The HUD shows the wave number and the current weapon.

**Scrolling.** In the scrolling level, the Main Camera has a **Scroll Camera 2D** that moves it up the level. The player's **Keep On Screen 2D** carries them along. Enemies are placed along the level ahead of time; each one's **Wake On Screen 2D** keeps it still until it comes into view, and removes it once it leaves. When the camera reaches the end, it raises `ReachedBoss`, which wakes the boss.

## Start your own game

**[Top-Down Shooter Kit — Build Your Game](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Build%20Your%20Game.md)** takes you from the decisions table on page 10 of your ten-pager to your finished game, step by step, with checks for First Playable, Alpha and Beta. The steps below are the short version.

**An arena shooter:**
1. Create a new 2D scene in `Assets/_Game/Scenes`.
2. Drag in `Arena Systems` and `Player Ship` from the kit's `Sample/Prefabs`.
3. Set the Main Camera's **Size** so the arena fits, and surround the arena with walls (sprites with Box Collider 2D).
4. On `Arena Systems` → `Waves`, move the spawn points to just outside your walls or the screen's edge, and set up your waves.
5. Press **Play**.

**A scrolling shooter:** start from a copy of `Shooter_Scrolling` (**File → Save As…** into `Assets/_Game/Scenes`), and place your own enemies along the level.

### Changing a prefab or a weapon

Make a **Prefab Variant** (right-click the prefab → **Create → Prefab Variant**), or **duplicate** a Weapon asset (**Ctrl+D** / **Cmd+D**), move it to `Assets/_Game`, and change the copy.

## Recipes

**A new weapon.** In `Assets/_Game`, **Create → Collin Game → Top-Down Shooter Kit → Weapon**. Set its Projectile Prefab to `Player Bullet`, then try Shots Per Second `12`, Inaccuracy `8` for a machine gun, or Projectiles Per Shot `5`, Spread Angle `60`, Shots Per Second `2` for a shotgun.

**A power-up that lasts for good.** On a Power Up 2D, set **Duration** to `0`.

**An enemy that fires straight down.** A Weapon Shooter 2D with Fire When **Automatic**, Direction **Forward**, and the enemy rotated `180` on Z (its up arrow pointing down).

**A tougher wave.** Add a wave with two groups, such as 8 Drones and 3 Gunships, and lower **Seconds Between Enemies**.

**Endless mode.** Tick **Loop** on the Wave Spawner 2D. Show the score with a **High Score** component, as in Exercise 08.

**A boss with two weapons.** Give the boss a child object with a second Weapon Shooter 2D (and its own weapon and interval).

**Screen shake on every hit.** On the Player Ship's Health **On Damaged**, add **CameraShake → Shake**. (A scrolling level's camera moves by itself, so use **Hit Stop** there instead.)

**Sounds.** Each Weapon asset has a **Sound**. Enemies' Health **On Died** can play an explosion.

## If something goes wrong

| What you see | What to do |
|---|---|
| Nothing fires | The Weapon Shooter 2D needs a **Weapon**, and the weapon needs a **Projectile Prefab** |
| Bullets go through enemies | The enemy needs Health, a collider, and the tag in the bullet's **Target Tag** (`Enemy`) |
| Bullets hit walls they shouldn't | Untick **Stopped By Walls** on the projectile, or make the wall's collider a trigger |
| The aim is stuck | The mouse takes over when it moves. On a gamepad, push the right stick past **Stick Dead Zone** |
| The ship flips the wrong way | On the Top Down Controller 2D, set **Facing** to **None**; Aim 2D flips the sprite instead |
| A wave never ends | An enemy is stuck somewhere off screen. Move the spawn points closer, or check its Enemy Mover 2D |
| Enemies in the scrolling level never move | Their Wake On Screen 2D wakes them when the camera reaches them; check the camera is scrolling |
| The ship is pushed off the bottom | Keep On Screen 2D needs the main camera to be **Orthographic** |
| The game slows down with many bullets | Lower the projectile's **Lifetime**, so bullets are put away sooner |
