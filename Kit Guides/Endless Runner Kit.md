---
title: "Endless Runner Kit"
course: GAME 1303
status: draft
course_version: 0.15.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Endless Runner Kit

The Endless Runner Kit is a starting point for games where the player runs by themselves, faster and faster, and the only question is how long they last. The player decides one thing at a time: when to jump, when to fly, or which lane to be in.

It supports three styles:

| Style | The player… | Like |
|---|---|---|
| **Jump** | jumps over gaps and obstacles, and slides under them by holding down | Canabalt, Alto's Adventure |
| **Jetpack** | holds Jump to fly up and lets go to fall | Jetpack Joyride |
| **Lanes** | moves up and down between lanes | a 2D take on Subway Surfers, or a top-down road |

The track is built from **chunks**, short pieces you design by hand. The kit picks them at random as the player runs, and brings in harder ones as the speed goes up. The sample is a jumping runner with ten chunks.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Running that speeds up over time, which is the difficulty ramp | Levels with an end (use the Platformer Kit) |
| Jumping, double jumps, sliding, jetpack, lanes | Wall-running or grappling |
| A track that never ends, built from chunks you design | Randomly generated terrain |
| Harder chunks as the speed rises | Missions and achievements |
| Distance score and a saved best | Online leaderboards |
| Coins and a magnet power-up | Shops and unlockable characters |
| Background layers that scroll at different speeds | |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Endless Runner Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/EndlessRunner/Sample/Scenes`, add `Runner_Menu` and `Runner_Game`, next to each other, in that order.
4. Open `Runner_Menu` and press **Play**.

| Action | Keyboard | Gamepad |
|---|---|---|
| Jump (tap for a short hop, hold for a full jump) | **Space** | South button |
| Slide | **S** or ↓ (hold) | Left stick down |
| Pause | **Esc** | **Start** |

## What's in the sample

| Prefab | What it is | Settings worth changing |
|---|---|---|
| `Runner` | Runner Controller 2D (Jump style), Health, Coin Magnet 2D | **Start Speed**, **Max Speed**, **Speed Gain Per Second**, **Jump Height** |
| `Chunk Start` | Flat ground, no obstacles: always first | |
| `Chunk Flat`, `Chunk Gap`, `Chunk Crates` | Easy chunks: difficulty 0 and up | **Min Difficulty**, **Weight** |
| `Chunk Steps`, `Chunk Low Bar`, `Chunk Double Gap` | Medium: difficulty 0.3 and up | |
| `Chunk Spikes`, `Chunk Platforms`, `Chunk Gauntlet` | Hard: difficulty 0.6 and up | |
| `Coin`, `Magnet` | A coin; a magnet power-up | Magnet **Duration** |
| `Runner Systems` | Camera, track spawner, background layers, HUD, game over | **Chunks** on the Track Spawner 2D |

Select a chunk prefab to see a green line where it starts and a red line where it ends.

## How the sample fits together

**Running.** The Runner Controller 2D sets the runner's speed every physics step. It starts at **Start Speed** and gains **Speed Gain Per Second** until it reaches **Max Speed**. That's the whole difficulty ramp: faster running gives less time to react. Its **Difficulty** goes from 0 at the start to 1 at top speed.

**The track.** The **Track Spawner 2D** places `Chunk Start` first, then keeps 40 units of track built ahead of the runner. Each new chunk is picked at random from those whose difficulty range includes the current Difficulty, more often if its **Weight** is higher, and never the same one twice in a row. Chunks the runner has passed are removed.

**Dying.** Obstacles have **Damage On Touch**, and the runner has 1 health, so any hit ends the run. A **Kill Zone** below the track catches falls. When health runs out, the runner stops and `PlayerDied` shows the Game Over screen.

**Score.** The runner writes the distance run to `Distance`. A **High Score** keeps the best in `BestDistance`, and saves it between sessions. Coins are **Collectibles** that add to `Coins`.

**The magnet.** Picking up a `Magnet` turns on the runner's **Coin Magnet 2D** for 8 seconds, pulling in nearby coins.

**Background.** Three layers with **Parallax 2D** scroll at different speeds, so the far hills seem far away.

## Start your own game

**[Endless Runner Kit — Build Your Game](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit%20-%20Build%20Your%20Game.md)** takes you from the decisions table on page 10 of your ten-pager to your finished game, step by step, with checks for First Playable, Alpha and Beta. The steps below are the short version.

1. Create a new 2D scene in `Assets/_Game/Scenes`.
2. Drag in `Runner Systems` and `Runner` from the kit's `Sample/Prefabs`.
3. Press **Play**: you have the sample's track.
4. Make your own chunks (below), and replace the sample's in the Track Spawner 2D's **Chunks** list.

### Making a chunk

1. Create an empty GameObject at `0, 0, 0` and add a **Track Chunk**. Set its **Length**, such as `20`.
2. Add children: ground (sprites with Box Collider 2D, or a small Tilemap), obstacles, coins. Keep the ground's top at the same height as the sample chunks (`y = 0`), so chunks join without a step.
3. Check the gaps can be jumped at top speed, and the obstacles can be cleared.
4. Set **Min Difficulty** and **Max Difficulty**, drag it into `Assets/_Game/Prefabs`, delete it from the scene, and add the prefab to the Track Spawner 2D's **Chunks**.

> [!tip] Testing one chunk
> To test a new chunk, temporarily make it the spawner's **First Chunk**, or the only entry in **Chunks**.

## Recipes

**A jetpack game.** Set the runner's **Style** to **Jetpack**. Build chunks with a floor and a ceiling, and obstacles at different heights.

**A lanes game.** Set **Style** to **Lanes** and **Lane Heights** to three heights, such as `-2.5`, `0`, `2.5`. The Lanes style has no gravity, so chunks need no ground: place obstacles and coins on the lanes. Draw the art from above, such as a road with three lanes, and it becomes a top-down racer.

**A double jump.** Set **Extra Air Jumps** to `1`.

**A slower ramp.** Lower **Speed Gain Per Second** to `0.05`: top speed now takes about three minutes.

**An enemy to jump on.** A Walker from the Platformer Kit (Patrol Enemy 2D and Stompable Enemy 2D) works on a runner too: landing on it bounces the runner, running into it costs health.

**Coins in an arc over a gap.** Place five coins along the top of a jump at the speed that chunk appears.

**Sound and juice.** The runner has **On Jump**, **On Land** and **On Stopped** events. Play a sound on each, and shake the camera on **On Stopped**.

## If something goes wrong

| What you see | What to do |
|---|---|
| The runner doesn't move | It waits **Start Delay** seconds. Check its Input field and that the runner isn't stuck in the ground |
| The runner can't jump | It needs to be on ground: the ground's collider must be solid, on a layer in **Ground Layers** |
| Gaps open between chunks | A chunk's **Length** doesn't match where its ground ends. Select it and compare the red line with the ground |
| A step where chunks meet | The chunks' ground isn't at the same height |
| The same few chunks keep coming | Check each chunk's difficulty range, and that harder chunks are in the list |
| The game gets impossible | Lower **Max Speed**, or check the hard chunks' gaps at top speed |
| The background jumps | The background sprite's left and right edges must match, with Draw Mode **Tiled** and Width three times the sprite |
| The best distance never saves | Add a **High Score** with Score `Distance` and Best `BestDistance` |
