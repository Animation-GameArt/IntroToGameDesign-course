---
title: "Physics Puzzle Kit"
course: GAME 1303
status: draft
course_version: 0.11.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Physics Puzzle Kit

The Physics Puzzle Kit is a starting point for games where physics does the work: launching things at structures until they topple (Angry Birds style), or cutting ropes so things fall into place (Cut the Rope style). It adds a launcher, breakable objects, targets, puzzle rules and ropes to the course scripts, and a small sample game with three levels.

Before you start, read [Physics in Unity](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Physics%20in%20Unity.md). Everything in this kit is built on it.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| A slingshot launcher with aiming dots, by mouse, touch, keyboard or gamepad | Several kinds of projectile with special powers |
| Limited shots per level | Saving stars per level |
| Objects that break when hit hard enough | Objects that crack into pieces by themselves (you can spawn a prefab of pieces) |
| Targets to destroy, and a win when they're all gone | Enemies that move or fight back |
| Ropes that swing and can be cut by swiping | Ropes that can be re-attached |
| Score, a HUD, win and lose screens | Level editors |
| Unity's own joints, materials and effectors | Liquids or soft bodies |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Physics Puzzle Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/PhysicsPuzzle/Sample/Scenes`, add these scenes, next to each other and in this order: `Puzzle_Menu`, `Puzzle_Level1`, `Puzzle_Level2`, `Puzzle_Level3`, `Puzzle_Win`.
4. Open `Puzzle_Menu` and press **Play**.

Play the sample through once before you change anything.

| Action | Mouse or touch | Keyboard | Gamepad |
|---|---|---|---|
| Aim and launch | Press near the launcher, drag back, release | Hold **Enter**, aim with **WASD**, release | Hold the left face button, aim with the left stick, release |
| Cut a rope | Swipe across it | — | — |
| Pause | — | **Esc** | **Start** |

## What's in the sample

| Prefab | What it is | Settings worth changing |
|---|---|---|
| `Launcher` | The slingshot. Takes shots from `ShotsLeft` | **Max Pull**, **Power**, **Projectile Prefab** |
| `Ball` | The projectile | Rigidbody 2D **Mass**; its Physics Material |
| `Glass Block`, `Wood Block`, `Stone Block` | Breakable blocks of three strengths | **Break Speed**, Rigidbody **Mass**, **Amount** (points) |
| `Target` | Must be destroyed to win. Breakable, and counted by `TargetsLeft` | **Break Speed** |
| `Rope Anchor` | Builds a rope down to a hanging object | **Link Count**, **Hanging Body** |
| `Level Systems` | HUD, pause, win and lose screens, rules, the swipe cutter | **Starting Shots** on Puzzle Rules |

Select the `Launcher` in the Scene view to see the circle where a press starts aiming. Select a `Rope Anchor` to see where its rope will hang.

## How the sample fits together

**Shots.** Puzzle Rules sets `ShotsLeft` to **Starting Shots** when the level starts. The Launcher takes one for each launch, and stops at 0. When a projectile comes to rest, the Launcher raises `ShotFinished`.

**Targets.** Each Target counts itself into `TargetsLeft` when the level starts, and counts itself out when it breaks or falls off the level.

**Winning and losing.** Puzzle Rules watches both. When `TargetsLeft` reaches 0, it adds points for unused shots and raises `PuzzleWon`. When `ShotFinished` arrives with no shots left and targets remaining, it raises `PuzzleLost`. The win and lose screens listen for those events, as in Exercise 06.

**Breaking.** A Breakable 2D breaks when something hits it faster than its **Break Speed**. A heavy ball moving fast breaks glass easily and stone rarely. Give a breakable a **Health** component and it takes several hard hits instead of one.

## Start your own game

**[Physics Puzzle Kit — Build Your Game](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Build%20Your%20Game.md)** takes you from the decisions table on page 10 of your ten-pager to your finished game, step by step, with checks for First Playable, Alpha and Beta. The steps below are the short version.

1. Create a new 2D scene in `Assets/_Game/Scenes` for your first level.
2. Drag in `Level Systems` and `Launcher` from the kit's `Sample/Prefabs`.
3. Add ground: a Tilemap with a solid collider, or a long sprite with a Box Collider 2D.
4. Build a structure from the block prefabs, with at least one `Target`. Leave tiny gaps between blocks, so the stack doesn't push itself apart when the level starts.
5. Set **Starting Shots** on `Level Systems` → `Rules`.
6. Press **Play**, launch, and adjust.

For a rope-cutting level, skip the launcher: add a `Rope Anchor`, drag a hanging object into its **Hanging Body**, and put a `Target` or a goal where the object should land.

### Changing a prefab

Make a **Prefab Variant** (right-click the prefab → **Create → Prefab Variant**), move it to `Assets/_Game/Prefabs`, and change the variant.

## Recipes

**A new material.** Make a variant of `Wood Block`. Change its sprite, its Rigidbody 2D **Mass**, and its **Break Speed**.

**A block that takes three hits.** Add a **Health** component to a block variant with Max Health `3` and Invulnerable Time `0.2`. Breakable 2D then takes 1 health per hard hit.

**A bouncy wall.** Create a **Physics Material 2D** with Bounciness `0.9` and put it on a wall's collider.

**A seesaw or a swinging plank.** A plank with a Rigidbody 2D and a **Hinge Joint 2D**. See Part 8 of Exercise 05.

**Wind or a conveyor.** A trigger collider with **Used By Effector** ticked and an **Area Effector 2D**.

**A heavier, slower projectile.** Make a `Ball` variant with higher **Mass** and a larger sprite, and drag it into the Launcher's **Projectile Prefab**. Raise **Power** if it no longer reaches.

**Pieces when something breaks.** Make a small prefab of three or four little sprites with Rigidbody 2D and a **Lifetime** of `2` seconds, and drag it into a Breakable's **Spawn When Broken**.

**A sound and a shake on breaking.** On a Breakable's **On Broken**, add **SoundEffect → Play** and **CameraShake → Shake**, as in Exercise 07.

## If something goes wrong

| What you see | What to do |
|---|---|
| Blocks break as soon as the level starts | Leave small gaps so they don't overlap, and keep **Settle Time** at `1` |
| The level is won straight away | No targets were counted. Each target needs a **Puzzle Target 2D** using `TargetsLeft` |
| The launcher won't aim | Press inside the yellow circle. Check **Shots Left** isn't 0 and **Projectile Prefab** is set |
| The ball passes through thin blocks | Set the Ball's Rigidbody 2D **Collision Detection** to **Continuous** |
| Swiping doesn't cut the rope | The level needs a **Cutter 2D**. It's in `Level Systems` |
| The rope stretches or jitters | Use fewer, heavier links, or a lighter hanging object |
