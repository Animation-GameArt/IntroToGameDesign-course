---
title: "Arcade Classic Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Arcade Classic Kit — Build Your Game

This guide takes you from your ten-pager to your own finished arcade game, built with the Arcade Classic Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Arcade Classic Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Arcade%20Classic%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Arcade_Breakout` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **Closest classic:** Breakout, Pong or Asteroids, and your twist | | All three, plain |
| **The player's piece:** paddle or ship, and its feel | | Paddle Speed `14`, following the mouse; a ship that turns, thrusts and drifts |
| **What's in play:** ball, bricks, asteroids, and how they behave | | Ball starts at speed `7` and speeds up each hit; bricks take 1 or 3 hits; asteroids split twice |
| **Lives and losing:** how many, and what costs one | | 3 lives; a missed ball or a crash |
| **Score:** what earns points, and best score | | Bricks and asteroids by size; best score saved |
| **Getting harder:** how play speeds up or fills up | | Ball speeds up; asteroids are faster when smaller |
| **Goal:** clear the screen, reach a score, or survive | | Clear all bricks or asteroids; first to 5 in Pong |
| **Theme and look:** colors, art, mood | | Kenney's Puzzle Pack 2 and Space Shooter Remastered |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. One screen, one twist on a classic, and a few rounds that get harder is a complete arcade game in eight weeks. The twist is your design.

## Stage 1 — First Playable

The goal: your one screen, played from the menu to winning or losing.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data

The sample's `ArcadeScore`, `Lives`, best-score variables and events work as they are. For your own best score, create an Int Variable in `_Game/Data` and set it on the **High Score** component.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Arcade%20Classic%20Kit%20-%20Building%20the%20Sample.md#part-1--data).

### 3. Your Arcade Systems

Make a **Prefab Variant** of `Arcade Systems` in `_Game/Prefabs`. If you made your own variables, swap them into its binders and conditions.

*Worked example:* [Part 2 — Arcade Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Arcade%20Classic%20Kit%20-%20Building%20the%20Sample.md#part-2--arcade-systems).

### 4. Your screen

1. Open the sample scene closest to your classic (`Arcade_Breakout`, `Arcade_Pong` or `Arcade_Asteroids`), and **File → Save As…** into `_Game/Scenes` with your game's name.
2. Replace `Arcade Systems` with your variant.
3. Make **Prefab Variants** of the pieces you change (paddle, ball, bricks, ship, asteroids) and set them from your table.
4. Add your twist. If it needs something none of the kit's scripts do, it's a custom script.

*Worked example:* [Part 3 — Breakout (`Arcade_Breakout`)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Arcade%20Classic%20Kit%20-%20Building%20the%20Sample.md#part-3--breakout-arcade_breakout). Pong and Asteroids are in the parts after it.

### 5. Your menu and Scene List

1. Copy the kit's `Arcade_Menu` into `_Game/Scenes`, and make its button load your game. Change the title.
2. **File → Build Profiles → Open Scene List**: your menu first, then your game.

*Worked example:* [Part 6 — Menu](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Arcade%20Classic%20Kit%20-%20Building%20the%20Sample.md#part-6--menu).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your player piece moves with the feel in your table.
- [ ] You can lose a life, lose the game, and clear the screen (or reach your goal).
- [ ] The score counts, and the best score is kept.
- [ ] Your twist is in, even if rough.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every round and every feature exists and works. Art and balance can still be rough.

### Getting harder

Make the game ramp up as your table says: faster balls, tougher bricks, more asteroids, or new rounds. A second layout can be a second scene, loaded after the first is cleared.

### All your pieces, and custom scripts

Every piece and your twist work together, from the first serve to game over.

### Every screen

Menu, pause, game over and win and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] The game ramps up the way your table says.
- [ ] Every piece in your table is in, and your twist works.
- [ ] The game can be played from the menu to game over or the win, and again.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, game over and win, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Arcade games live on clarity: the player's piece, the ball or bullets, and dangers should each be a different, bright color on a dark background.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: every bounce, a brick or asteroid breaking, losing a life, and the serve. Arcade games feel empty without them. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch how long a game lasts. Under a minute is too hard; over ten without danger is too easy. Adjust speed-up, lives and counts. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Every bounce, break, shot and lost life has a sound.
- [ ] A game lasts as long as your table intends.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A life lost | The `Lives` variable (its Changed event) |
| The screen cleared | The `LevelCleared` event |
| Game over | The `GameOver` event |
| A brick or asteroid destroyed | **Brick 2D** → On Broken, or Health → On Died |

| To make the kit do something… | Call |
|---|---|
| Serve the ball | **Ball 2D → Serve** |
| Add points | **IntVariable → Add** on the score |
| Show a screen | **UIScreen → Show** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
