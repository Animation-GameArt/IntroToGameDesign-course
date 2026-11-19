---
title: "Arcade Classic Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.12.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Arcade Classic Kit — Building the Sample

**For the instructor.** These steps build the kit's three sample games once, in the template project. Building them tests every kit script, and the result is what students import. Students read **Arcade Classic Kit**, not this page.

Everything goes in `Assets/_Course/Kits/ArcadeClassic/Sample/`, with folders `Data`, `Prefabs` and `Scenes`.

## Before you start

1. Pull the template project. It should be version 0.12.0 or later, with no red errors in the Console.
2. **Art.** Download Kenney's **Puzzle Pack** (paddles, balls, bricks) and **Space Shooter Redux** (ship, lasers, meteors); links are in `Assets/_Course/Art/Kenney/README.md`. Unzip each to `Assets/_Course/Art/Kenney/` keeping Kenney's folder name, remove the non-Unity files, and choose **Collin Game → Art → Reapply Art Import Settings**. Push them, and I'll add them to `Course Credits`. Plain sprites from **Create → 2D → Sprites** work for testing.
3. **Tags.** In **Project Settings → Tags and Layers**, add `Enemy` if it isn't there.
4. **Camera.** In every game scene: Main Camera Orthographic, **Size** `5`, at `0, 0, -10`, background black. No Cinemachine.
5. **Panel Settings.** Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data

In `Sample/Data`:

| Asset | Type | Initial value |
|---|---|---|
| `ArcadeScore`, `BestBreakout`, `BestAsteroids` | Int Variable | `0` |
| `Lives` | Int Variable | `3` |
| `BricksLeft`, `AsteroidsLeft` | Int Variable | `0` |
| `LeftScore`, `RightScore` | Int Variable | `0` |
| `LevelCleared`, `GameOver` | Void Event Channel | |

## Part 2 — Arcade Systems

An empty GameObject at `0, 0, 0`, made into a prefab, with these children:

**`HUD`** — UI Document, Source Asset `ArcadeHUD` (from `Kits/ArcadeClassic/UI`), with a **UI Variable Binder**: `score-label` → `ArcadeScore` → `Score: {0}`; `lives-label` → `Lives` → `Lives: {0}`; `best-label` set per scene.

**`Pause Menu`** — as in the Platformer Kit sample.

**`Reset`** — a **Variable Resetter** with `ArcadeScore`, `Lives`, `LeftScore` and `RightScore`. Not `BricksLeft` or `AsteroidsLeft`: Counted Object sets those.

**`Lose`** — an **Int Variable Condition**: Variable `Lives`, At Most `0`, Raise Event `GameOver`.

**`Scene Changer`** — Scene Changer, Scene Name empty. **`To Menu`** — Scene Changer, Scene Name `Arcade_Menu`.

**`Cleared`** — UI Document `EndScreen`, Sort Order `2`, UI Screen hidden, a **Void Event Listener** on `LevelCleared` → **UIScreen → Show**; buttons → **ReloadScene** and To Menu **Load**.

**`Game Over`** — UI Document `GameOver`, Sort Order `3`, UI Screen hidden, a **Void Event Listener** on `GameOver` → **UIScreen → Show**; buttons `try-again-button` → **ReloadScene**, `menu-button` → To Menu **Load**.

## Part 3 — Breakout (`Arcade_Breakout`)

**Walls.** Three sprites with Box Collider 2D just outside the view: left at `x = -9.4`, right at `x = 9.4`, top at `y = 5.4`. No bottom wall.

**`Paddle`** — a paddle sprite at `0, -4.2`, about `2 × 0.35`, with a **Box Collider 2D** and **Paddle 2D**: Moves Along Horizontal, Player, Follow Mouse ticked, Speed `14`, Min `-7.8`, Max `7.8`.

**`Ball`** — a ball sprite, Scale about `0.35`, with a **Circle Collider 2D** and **Ball 2D**: Play Direction Up And Down, Start Speed `7`, Speed Up `0.3`, Max Speed `14`, Max Bounce Angle `60`, Min Angle `20`, Serve From `Paddle`, Serve Offset `0, 0.45`, Serve Direction `0.3, 1`, Auto Serve `0`.

**`Brick`** — a brick sprite about `1.4 × 0.5` with a **Box Collider 2D**, **Brick 2D** (Hits To Break `1`, Add To `ArcadeScore`, Amount `10`) and **Counted Object** (Count `BricksLeft`). **`Tough Brick`** is a variant: Hits To Break `3`, Amount `30`, Color By Hits Left: element 0 light red, 1 orange, 2 dark red.

**`Ball Goal`** — a Box Collider 2D trigger at `0, -5.8`, `20 × 1`, with **Ball Goal 2D**: Change Variable `Lives`, Amount `-1`, Reset Ball ticked.

**Layout.** Six rows of ten bricks from `y = 3.8` down, with a row of Tough Bricks at the top. Add a **High Score** (Score `ArcadeScore`, Best `BestBreakout`, Save Name `Breakout`) and an **Int Variable Condition** (`BricksLeft`, Equal To `0`, Raise Event `LevelCleared`). Bind `best-label` to `BestBreakout`.

## Part 4 — Pong (`Arcade_Pong`)

Replace the HUD's Source Asset with `PongHUD`, and bind `left-score` → `LeftScore` → `{0}` and `right-score` → `RightScore` → `{0}`. Untick the Lose condition.

**Walls.** Top at `y = 5.4` and bottom at `y = -5.4`. A dashed line down the middle, for looks.

**`Pong Paddle`** — a paddle sprite turned upright, about `0.35 × 2`, with a Box Collider 2D and **Paddle 2D**: Moves Along Vertical, Speed `10`, Min `-4`, Max `4`, Follow Mouse unticked. Place it at `x = -8` (Player) and a second one at `x = 8` (Controlled By Computer, Computer Speed `0.6`, Dead Zone `0.3`).

**`Pong Ball`** — a Ball variant: Play Direction **Side To Side**, Start Speed `7`, Min Angle `20`, Serve From empty (it waits in the middle), Serve Direction `1, 0.4`, Random Serve Side ticked, Auto Serve `1`, Input empty.

**Goals.** A Ball Goal 2D trigger behind each paddle:
- Left goal at `x = -9.8`: Change Variable `RightScore`, Amount `1`, Next Serve Direction `-1, 0.4`.
- Right goal at `x = 9.8`: Change Variable `LeftScore`, Amount `1`, Next Serve Direction `1, 0.4`.

**Winning.** Int Variable Condition `LeftScore` At Least `5` → `LevelCleared`; another on `RightScore` At Least `5` → `GameOver`.

## Part 5 — Asteroids (`Arcade_Asteroids`)

**`Bullet`** — a laser sprite, Scale `0.5`, with a **Box Collider 2D** (Is Trigger), a **Rigidbody 2D** (Gravity Scale `0`), **Damage On Touch** (Target Tag `Enemy`, Damage `1`, Remove Self After Hit ticked), **Lifetime** (`1` second) and **Screen Wrap 2D**.

**`Ship`** — a ship sprite pointing up, Scale `0.5`, tag `Player`, with a **Polygon Collider 2D**, **Ship Controller 2D** (defaults), a child `Muzzle` at the nose, a child `Flame` sprite behind it in **Engine Flame**, **Shooter 2D** (Projectile Prefab `Bullet`, Muzzle `Muzzle`, Aim Muzzle Up, Speed `14`, Shots Per Second `5`, Max On Screen `4`), **Screen Wrap 2D**, **Health** (Max Health `1`, When Health Runs Out **Nothing**, On Died → `Lives` **Add** `-1`), and a **Respawner** (On Respawn → **ShipController2D → StopAndFaceUp**).

**Asteroids.** Three prefabs, each a meteor sprite with a **Circle Collider 2D** (Is Trigger), **Rigidbody 2D**, tag `Enemy`, **Drift 2D**, **Screen Wrap 2D**, **Damage On Touch** (Target Tag `Player`), **Counted Object** (Count `AsteroidsLeft`) and **Health** (Max Health `1`, Invulnerable Time `0`, When Health Runs Out **Destroy**, On Died → `ArcadeScore` **Add**):

| Prefab | Scale | Drift speed | Points | Split On Death 2D |
|---|---|---|---|---|
| `Asteroid Large` | `1` | `0.8`–`1.5` | `20` | Piece Prefab `Asteroid Medium`, Pieces `2` |
| `Asteroid Medium` | `0.6` | `1.2`–`2.2` | `50` | Piece Prefab `Asteroid Small`, Pieces `2` |
| `Asteroid Small` | `0.35` | `1.8`–`3` | `100` | none |

**Layout.** The Ship in the middle. Four large asteroids near the corners, away from the ship. A **High Score** (`ArcadeScore`, `BestAsteroids`, Save Name `Asteroids`), and an Int Variable Condition (`AsteroidsLeft`, Equal To `0`, `LevelCleared`). Bind `best-label` to `BestAsteroids`.

## Part 6 — Menu

`Arcade_Menu`: a copy of the course MainMenu with three buttons, each with a Scene Changer: `Arcade_Breakout`, `Arcade_Pong`, `Arcade_Asteroids`. Show the two best scores with a UI Variable Binder.

## Part 7 — Scene List

`Arcade_Menu`, `Arcade_Breakout`, `Arcade_Pong`, `Arcade_Asteroids`.

## Part 8 — Test

**Breakout**
- [ ] The ball waits on the paddle and Space serves it.
- [ ] Hitting with the paddle's ends sends the ball off at a steep angle; the middle sends it straight up.
- [ ] The ball never gets stuck going sideways, and never slows down.
- [ ] Bricks break and add points; tough bricks change color and take three hits.
- [ ] Missing the ball costs a life and the ball returns to the paddle; at 0 lives, Game Over.
- [ ] Breaking every brick shows the cleared screen; the best score is kept after restarting the game.
- [ ] The mouse moves the paddle; so do the keys after the mouse stops.

**Pong**
- [ ] The ball serves by itself after a second, randomly left or right.
- [ ] The computer paddle follows the ball and can be beaten.
- [ ] A missed ball scores for the other side, and the next serve goes toward the player who missed.
- [ ] Reaching 5 ends the game.

**Asteroids**
- [ ] The ship turns, thrusts, drifts and slows gently; the flame shows while thrusting.
- [ ] The ship, bullets and asteroids wrap at every edge.
- [ ] No more than 4 bullets at once.
- [ ] Large asteroids split into two medium, medium into two small; small ones disappear.
- [ ] The cleared screen shows only when every piece is gone, not when the last large one splits.
- [ ] Touching an asteroid costs a life and the ship respawns in the middle, facing up and still.

**All**
- [ ] Esc pauses; serving and shooting don't work while paused.

Note anything that fails, with the Console message.

## Part 9 — Commit

Commit and push the `Sample` folder with its `.meta` files, and the two art folders.

## Later — Exporting the kit

Export `Assets/_Course/Kits/ArcadeClassic` and both art folders with **Assets → Export Package**, unticking Core scripts that Unity adds as dependencies.
