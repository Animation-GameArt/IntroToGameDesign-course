---
title: "Arcade Classic Kit"
course: GAME 1303
status: draft
course_version: 0.12.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Arcade Classic Kit

The Arcade Classic Kit is a starting point for single-screen arcade games: a fixed camera, simple controls, a score, lives, and play that gets faster. Its sample is three tiny games you can take apart: **Breakout**, **Pong** and **Asteroids**. Most arcade-style pitches are a twist on one of the three.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| A paddle moved by keys, stick or mouse, or by the computer | Two human players on one keyboard (a second Input Reader is a custom script) |
| A ball that speeds up and bounces at an angle that depends on where it hits | Several balls at once from a power-up |
| Bricks that take one or more hits | Falling power-ups that change the paddle |
| A ship that turns, thrusts and drifts, and wraps around the screen | Scrolling levels (see the top-down shooter kit) |
| Shooting, with a limit on shots at once | Several weapon types |
| Asteroids that drift, spin and split | Enemy ships that hunt the player |
| Score, best score, lives, and knowing when everything is cleared | Online leaderboards |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Arcade Classic Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/ArcadeClassic/Sample/Scenes`, add these scenes: `Arcade_Menu`, `Arcade_Breakout`, `Arcade_Pong`, `Arcade_Asteroids`.
4. Open `Arcade_Menu` and press **Play**. The menu has a button for each game.

| Game | Controls |
|---|---|
| Breakout | Move the paddle with **A/D**, the arrow keys, the left stick or the mouse. **Space** serves |
| Pong | Move with **W/S** or the arrow keys or the left stick. Serves by itself. First to 5 wins |
| Asteroids | Turn with **A/D**, thrust with **W**, shoot with **Enter** or the left mouse button |

## What's in the sample

| Prefab | What it is | Settings worth changing |
|---|---|---|
| `Paddle` | Breakout paddle: horizontal, player or mouse | **Speed**, **Min Position**, **Max Position** |
| `Pong Paddle` | Vertical paddle; the right one is controlled by the computer | **Controlled By**, **Computer Speed**, **Computer Dead Zone** |
| `Ball` | Bounces at a steady speed; speeds up on each paddle hit | **Start Speed**, **Speed Up Per Paddle Hit**, **Max Bounce Angle**, **Play Direction** |
| `Brick`, `Tough Brick` | Break after 1 or 3 hits, for points | **Hits To Break**, **Color By Hits Left**, **Amount** |
| `Ship` | Asteroids ship: turns, thrusts, shoots, wraps | **Turn Speed**, **Thrust**, **Max Speed**, **Drag**; **Shots Per Second**, **Max On Screen** |
| `Bullet` | The ship's shot. Damage On Touch and Lifetime | **Lifetime** |
| `Asteroid Large`, `Medium`, `Small` | Drift and spin; each splits into two of the next size | **Min Speed**, **Max Speed**; **Pieces** |
| `Arcade Systems` | HUD, pause, game over and win screens | |

Select a paddle in the Scene view to see the line it can move along.

## How the sample fits together

**The ball.** The Ball 2D keeps its speed the same after every bounce, and never travels so flat that it would bounce between two walls forever. Where it hits a paddle decides the angle it leaves at: the middle sends it straight back, the ends at up to **Max Bounce Angle**. That's what gives the player control.

**Serving.** Before each serve the ball waits on the paddle (Breakout, **Serve From**) or in the middle (Pong). The Jump or Attack button serves it, or **Auto Serve** does after a delay.

**Goals.** A **Ball Goal 2D** is a trigger just past an edge. In Breakout, the one below the paddle takes 1 from `Lives`. In Pong, the one behind each paddle adds 1 to the other player's score, and serves toward the player who lost the point.

**Counting.** Each brick and asteroid has a **Counted Object** that keeps `BricksLeft` or `AsteroidsLeft` up to date, including pieces of split asteroids. An **Int Variable Condition** on each count raises `LevelCleared` when it reaches 0.

**Losing.** An Int Variable Condition on `Lives` (At Most 0) raises `GameOver`.

**Asteroids.** Each asteroid has Health (1, Destroy), Drift 2D, Screen Wrap 2D, Damage On Touch (hurts the player) and Split On Death 2D. The ship's bullets have Damage On Touch (hurts `Enemy`). When a large asteroid's health runs out, it creates two medium ones, which create two small ones. Each size adds points on its Health's **On Died**.

## Start your own game

1. Create a new 2D scene in `Assets/_Game/Scenes`.
2. Set the Main Camera's **Size** to `5` and leave it still: arcade games fit on one screen.
3. Drag in `Arcade Systems` and the prefabs for the game you're closest to.
4. Add walls: sprites with a Box Collider 2D just outside the camera's view, on the sides the ball should bounce off.
5. Press **Play** and adjust.

### Changing a prefab

Make a **Prefab Variant** (right-click the prefab → **Create → Prefab Variant**), move it to `Assets/_Game/Prefabs`, and change the variant.

## Recipes

**Faster, harder Breakout.** Raise **Speed Up Per Paddle Hit** to `0.6` and lower **Max Bounce Angle** to `50`.

**A brick that can't be broken.** A sprite with a Box Collider 2D and no Brick 2D. Don't give it a Counted Object, or the level can never be cleared.

**A brick that leaves something behind.** Drag a prefab into a brick's **Spawn When Broken**, such as a Coin that falls (Rigidbody 2D with gravity) and a Collectible.

**An easier Pong opponent.** Lower **Computer Speed** to `0.45`, or raise **Computer Dead Zone** to `0.8`.

**Pong to 5.** An Int Variable Condition on each player's score (At Least `5`) raises `GameOver` or `LevelCleared`.

**Rapid fire.** On the Ship's Shooter 2D, tick **Hold To Fire**, raise **Shots Per Second** to `8` and **Max On Screen** to `0`.

**Shoot downward from a turret (Space Invaders style).** A Shooter 2D with Aim **Muzzle Up** on a muzzle child turned 180°.

**Waves of asteroids.** On `LevelCleared`, call **Spawner → StartSpawning** on a Spawner with the large asteroid and **Total To Spawn** `4`, instead of showing the win screen.

**A shield after respawning.** Raise the ship's Health **Invulnerable Time** and give it a flashing animation on **On Damaged**. (Being safe right after respawning is a custom script.)

**Sounds.** Ball 2D has **On Paddle Hit** and **On Bounce**; Brick 2D has **On Broken**; Shooter 2D has **On Shoot**. Add **SoundEffect → Play** to each, as in Exercise 07.

## If something goes wrong

| What you see | What to do |
|---|---|
| The ball slows down or sticks to walls | Walls must be solid colliders, not triggers. Don't give walls a Physics Material; the ball sets its own |
| The ball goes straight up and down forever | Raise **Min Angle** on the Ball |
| The ball passes through the paddle | The paddle needs a Box Collider 2D. The Ball sets its Collision Detection to Continuous by itself |
| The paddle goes off the screen | Set **Min Position** and **Max Position**; select the paddle to see the line |
| The level is cleared straight away | Each brick or asteroid needs a **Counted Object** using the same variable as the condition. Don't use a Variable Resetter on that variable |
| Losing a life serves twice | Only one Ball Goal 2D should be below the paddle |
| Bullets hit the ship | They can't, by design; check that the bullet's Damage On Touch **Target Tag** is `Enemy`, and asteroids are tagged `Enemy` |
| Asteroids bounce off each other | Tick **Is Trigger** on the asteroids' colliders |
| Objects don't wrap at the edge | The camera must be Orthographic and not move |
