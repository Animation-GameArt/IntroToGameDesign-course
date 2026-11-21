---
title: "Endless Runner Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Endless Runner Kit — Build Your Game

This guide takes you from your ten-pager to your own finished endless runner, built with the Endless Runner Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Endless Runner Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Runner_Game` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **Style:** jump, jetpack, or lanes | | Jump, with sliding |
| **The runner:** who they are, and the art | | A character from Kenney's Pixel Platformer |
| **Speed:** start, top speed, and how fast it ramps up | | Start `6`, top `14`, gaining `0.1` per second |
| **Chunks:** the pieces of track, and which are easy, medium and hard | | 9 chunks: flat, gaps, crates; steps, bars; spikes, platforms, a gauntlet |
| **Hazards:** what ends a run | | Spikes, crates, bars and pits: one hit ends the run |
| **Pickups:** coins and power-ups, and what they do | | Coins; a magnet that pulls in coins for 8 seconds |
| **Score:** distance, coins, or both; best score | | Distance, with the best saved |
| **Theme and look:** setting, background layers | | Grassland with three parallax layers |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. One style, eight to twelve chunks and one or two power-ups is a complete runner in eight weeks. Chunks are your levels.

## Stage 1 — First Playable

The goal: your runner on a track of your first chunks, from the menu to dying and trying again.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data

The sample's `Distance`, `BestDistance`, `Coins` and `PlayerDied` work as they are. Make your own only for a different score, such as `Gems`.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit%20-%20Building%20the%20Sample.md#part-1--data).

### 3. Your runner

Make a **Prefab Variant** of `Runner` in `_Game/Prefabs`. On **Runner Controller 2D**, set **Style**, **Start Speed**, **Max Speed**, **Speed Gain Per Second** and **Jump Height** from your table. Change the sprite when your art is ready.

*Worked example:* [Part 2 — The runner and pickups](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit%20-%20Building%20the%20Sample.md#part-2--the-runner-and-pickups).

### 4. Your first chunks

Make three easy chunks (see **Making a chunk** in the **Endless Runner Kit** guide): an empty GameObject with a **Track Chunk**, ground at `y = 0`, and your obstacles and coins as children. Set **Min Difficulty** `0`. Save each as a prefab in `_Game/Prefabs`.

*Worked example:* [Part 3 — Chunks](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit%20-%20Building%20the%20Sample.md#part-3--chunks).

### 5. Your game scene

1. In `_Game/Scenes`, create a 2D scene. Drag in a variant of `Runner Systems` and your runner.
2. On its **Track Spawner 2D**, replace **Chunks** with yours.
3. Press **Play** and run. Check every gap can be jumped at top speed.

*Worked example:* [Part 4 — Runner Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit%20-%20Building%20the%20Sample.md#part-4--runner-systems) and [Part 5 — The game scene (`Runner_Game`)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit%20-%20Building%20the%20Sample.md#part-5--the-game-scene-runner_game).

### 6. Your menu and Scene List

Copy the kit's `Runner_Menu` into `_Game/Scenes`, make Play load your game scene, and change the title. In the Scene List: menu, then your game.

*Worked example:* [Part 6 — Menu](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit%20-%20Building%20the%20Sample.md#part-6--menu).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your runner runs, speeds up, and jumps (or flies, or changes lanes) as your table says.
- [ ] At least three of your chunks join without a step.
- [ ] Hitting a hazard or falling ends the run; Game Over shows the distance, and Try Again works.
- [ ] The best distance is kept.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every chunk and every feature exists and works. Art and balance can still be rough.

### All your chunks

Make the rest of your chunks: medium ones (**Min Difficulty** about `0.3`) and hard ones (about `0.6`). Give chunks you want more often a higher **Weight**. Test each new chunk alone by making it the spawner's **First Chunk** for a moment.

### All your pickups, and custom scripts

Every pickup and power-up in your table is in, and appears often enough to be found.

### Every screen

Menu, pause, Game Over and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every chunk in your table is in, and the hard ones appear once the runner is fast.
- [ ] Every pickup and power-up in your table is in.
- [ ] A run can last at least two minutes for a careful player, and the best score saves between sessions.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, Game Over, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your art, including the three background layers. The runner and hazards must stand out from every background layer.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: the runner's **On Jump** and **On Land**, coins' **On Collected**, the magnet, and the runner's Health **On Died**. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch how long runs last and what ends them. If the same chunk always ends runs, it's too hard for its difficulty. Adjust Speed Gain Per Second, chunks' difficulty ranges and weights. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Jumping, landing, coins and dying each have a sound.
- [ ] No chunk ends most runs on its own.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| The runner jumping or landing | **Runner Controller 2D** → On Jump, On Land |
| The run ending | The `PlayerDied` event, or **Runner Controller 2D** → On Stopped |
| Distance changing | The `Distance` variable (its Changed event) |
| A new best | **High Score** → On New Best |

| To make the kit do something… | Call |
|---|---|
| Stop the runner | **Runner Controller 2D → Stop** |
| Change lane | **Runner Controller 2D → GoToLane** |
| Add coins or points | **IntVariable → Add** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
