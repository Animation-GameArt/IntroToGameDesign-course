---
title: "3D Platformer Kit"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - 3d
---

# 3D Platformer Kit

The 3D Platformer Kit is a starting point for 3D platformers: run, jump and explore a 3D space, collect things, and reach the goal. Examples: A Hat in Time, Super Mario 64 or Astro Bot (one small area of each).

The sample, *Sky Islands*, is one level of floating islands in three areas: stepping stones, moving and crumbling platforms over a drop, and a tower with a bounce pad and enemies to stomp. Twenty coins are scattered across it, and a flag at the top ends the level.

Read **About 3D games** on the Genre Map first. A 3D level takes longer to build and test than a 2D one, and the camera is a design problem of its own.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| A player moved relative to the camera, with sprint, crouch, jumps, double jumps and short hops | Wall jumps, ledge grabs, swimming, climbing |
| A camera that orbits the player with the mouse or right stick | Fixed camera angles that change by area (Cinemachine can, with more cameras) |
| Moving, crumbling and bouncy platforms | Rotating platforms that carry the player round |
| Enemies that patrol, and can be stomped | Enemies that chase, or shoot |
| Coins, health, checkpoints and falling out of the level | Several levels joined by a hub world |
| A blob shadow, so the player can judge jumps | Animated characters (use a capsule, or a model without animations) |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut. The Genre Map's advice stands: one level with twenty collectibles and three distinct areas.

## Install the kit

The 3D scripts it builds on (Player Controller 3D and friends) are already in the course project.

1. Download the 3D Platformer Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/Platformer3D/Sample/Scenes`, add `Islands_Menu` and `Islands_Level`, next to each other, in that order.
4. Open `Islands_Menu` and press **Play**.

| Action | Keyboard and mouse | Gamepad |
|---|---|---|
| Move | WASD | Left stick |
| Look around | Mouse | Right stick |
| Jump (hold for higher) | Space | Bottom face button |
| Sprint | Left Shift | Left stick press |
| Pause | Esc | Start |

## How it works

- **Player Controller 3D** moves the player relative to the camera: up on the stick is always away from the camera. The player turns to face where they walk.
- The camera is a **Cinemachine Camera** with **Orbital Follow**: it circles the player at a set distance, turned by the mouse or right stick. **Cursor Lock 3D** hides the mouse pointer while you play.
- **Coins** are Core **Collectibles** with a **Spin 3D** to catch the eye. **Checkpoints** and a **Kill Zone** under the level work as they do in 2D: fall, and you're back at the last checkpoint.
- **Moving Platform 3D** carries the player; **Crumbling Platform 3D** falls a moment after it's stepped on, and comes back; **Bounce Pad 3D** launches the player.
- **Patrol Enemy 3D** walks between points. Land on it to defeat it; touch it any other way and lose a heart.
- **Blob Shadow 3D** puts a dark circle on the ground under the player. In 3D it's hard to tell where you'll land without one.

## What's in the sample

| Object | What it is | Worth changing |
|---|---|---|
| `Player` | Capsule with Player Controller 3D, Health, Respawner, Blob Shadow 3D | **Walk Speed**, **Jump Height**, **Extra Air Jumps** |
| `Orbit Camera` | The Cinemachine Camera | **Radius**, the vertical range |
| `Area 1`, `Area 2`, `Area 3` | The three areas, each with a checkpoint | Everything |
| `Coin` | Prefab: Collectible + Spin 3D | |
| `Islands Systems` | HUD, pause, win screen, kill zone | |

## Start your own game

**[3D Platformer Kit — Build Your Game](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Build%20Your%20Game.md)** takes you from the decisions table on page 10 of your ten-pager to your finished game, step by step, with checks for First Playable, Alpha and Beta. The steps below are the short version.

1. Sketch your level from above on paper: where the player starts, the three areas, where the coins are, and the goal. Each area should teach one idea, then test it.
2. Open `Islands_Level`, **File → Save As…** into `Assets/_Game/Scenes`, and delete the three areas.
3. Block out your level with Unity's basic shapes (**GameObject → 3D Object → Cube**). Play it often while it's grey; add art only once it's fun.
4. Use the sample's prefabs (`Coin`, `Checkpoint`, `Moving Platform`, `Bounce Pad`, `Patrol Enemy`) as you need them.

### Designing 3D levels

- **Jump distances.** With the default settings the player jumps about 2 units high, and about 4 units across walking or 6 sprinting. Measure gaps with the grid; make the first ones easy.
- **Look before you leap.** Put the camera where the player can see the landing. Long jumps toward or away from the camera are hardest; sideways ones are easiest.
- **Landmarks.** Something tall and distinct in each area (a tower, a big tree) helps players know where they are.
- **Coins as a trail.** A line of coins shows players where to go, and where to jump.

## Recipes

**A double jump.** Set **Extra Air Jumps** to `1`.

**Floaty or snappy jumps.** Lower **Fall Gravity Multiplier** for floaty, raise it for snappy.

**A platform that starts when you step on it.** Tick **Wait For Start** on the Moving Platform 3D, and add a Trigger Zone on top whose **On Enter** calls **MovingPlatform3D → StartMoving**.

**A spike strip.** A Patrol Enemy 3D with no points and **Can Be Stomped** unticked.

**Coins that open the goal.** An **Int Variable Condition** (Coins at least 20) raises an event; a **Void Event Listener** on the goal's gate deactivates it.

**A fixed camera.** Replace Orbital Follow with **Follow** (as in 2.5D Tutorial 1) for a camera that stays behind the player, or position the camera by hand for a set angle.

## If something goes wrong

| What you see | What to do |
|---|---|
| The scene is pink | The camera's **Renderer** must be **Universal Renderer** (Main Camera → Rendering) |
| The player falls through the floor | The floor needs a collider; the player's pivot must be at their feet |
| Moving the mouse doesn't turn the camera | The Cinemachine Input Axis Controller needs the **Look** action (see the Building the Sample guide) |
| Up and down on the mouse are reversed | Flip the sign of **Look Orbit Y**'s **Gain** |
| The player slides off moving platforms | The platform needs Moving Platform 3D on the object with the collider |
| Coins don't count | Their collider needs **Is Trigger**, and the player the **Player** tag |
| Falling doesn't send you back | The Kill Zone needs a trigger collider wide enough, and the player a Respawner |
| The pointer stays hidden on the win screen | Call **CursorLock3D → Unlock** from the win event |
