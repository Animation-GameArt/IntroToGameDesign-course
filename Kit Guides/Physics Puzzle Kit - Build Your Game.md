---
title: "Physics Puzzle Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Physics Puzzle Kit — Build Your Game

This guide takes you from your ten-pager to your own finished physics puzzle game, built with the Physics Puzzle Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Physics Puzzle Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Puzzle_Level1` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **What you throw or drop:** the projectile, and its weight | | A ball, Mass `1` |
| **What you destroy or reach:** the targets, and why they matter | | Green targets inside towers |
| **Materials:** which blocks, and how strong each is | | Glass (weak), wood, stone (strong) |
| **Puzzle type:** launching, cutting ropes, or both | | Launching in levels 1–2, ropes in level 3 |
| **Levels:** how many, and the one idea each teaches | | 3: launching; materials; ropes and joints |
| **Shots per level, and scoring:** what earns points | | 3 shots; points for breaking blocks and for unused shots |
| **Win and lose:** how a level ends | | Win when every target is gone; lose when shots run out first |
| **Theme and look:** setting, art, colors | | Kenney's Physics Assets |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. Three to five levels, each built around one idea, is a complete physics puzzle game in eight weeks. Physics levels take many test runs to tune.

## Stage 1 — First Playable

The goal: one level, played from the menu to winning or losing, with grey boxes or the kit's art.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data

The sample's `ShotsLeft`, `TargetsLeft`, `PuzzleScore` and events (in the kit's `Sample/Data`) work as they are. Make your own only if your game counts something else, such as `Stars`. For new materials, create **Physics Material 2D** assets in `_Game/Data` (friction and bounciness).

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-1--data).

### 3. Your projectile and blocks

1. Make a **Prefab Variant** of `Ball` (right-click → **Create → Prefab Variant**) in `_Game/Prefabs` for your projectile. Set its Rigidbody 2D **Mass** and sprite.
2. For each material in your table, make a variant of the closest block (`Glass Block`, `Wood Block` or `Stone Block`) and set its **Break Speed** (lower breaks more easily), Mass, Physics Material and **Amount** (points).
3. Make a variant of `Target` for your target.

*Worked example:* [Ball](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#ball) and [Blocks](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#blocks).

### 4. Your launcher and Level Systems

1. Make variants of `Launcher` and `Level Systems`. On your launcher, set **Projectile Prefab** to your projectile; tune **Max Pull** and **Power** later.
2. On your Level Systems variant → `Rules`, set **Starting Shots** from your table. If you made your own variables, swap them into the HUD's **UI Variable Binder** and the rules.

*Worked example:* [Launcher](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#launcher) and [Level Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#level-systems).

### 5. Your first level

1. In `_Game/Scenes`, create a new 2D scene for level 1. Drag in your Level Systems and launcher (or a `Rope Anchor`, for a rope level).
2. Add ground: a Tilemap with a solid collider, or a long sprite with a Box Collider 2D.
3. Build the structure your table's first idea needs, with at least one target. Leave tiny gaps between stacked blocks.
4. Press **Play** many times. If the level can be won with the first shot every time, it's too easy; if you can't win it, it's too hard.

*Worked example:* [Part 3 — Levels](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-3--levels).

### 6. Your menu, win scene and Scene List

1. Copy the kit's `Puzzle_Menu` and `Puzzle_Win` into `_Game/Scenes` (select, **Ctrl+D**, move and rename).
2. Point their Scene Changers at your first level and your menu. Change the title to your game's name.
3. **File → Build Profiles → Open Scene List**: remove the sample scenes; add yours in order: menu, levels, win.

*Worked example:* [Part 4 — Menu and win scenes](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-4--menu-and-win-scenes).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Level 1 can be won by destroying every target, and lost by running out of shots; both screens appear.
- [ ] Your projectile and at least two of your materials are in, and break as you intend.
- [ ] The score counts on the HUD, and Retry works.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every level and every feature exists and works. Art and balance can still be rough.

### Your other levels

For each level in your table: duplicate your level 1 scene, rebuild the structure around that level's idea, and add it to the Scene List before the win scene. Bring earlier ideas back in new combinations.

### All your pieces, and custom scripts

Every material, target and projectile in your table is in at least one level. For ropes, add `Rope Anchor`s and set their **Hanging Body**. For seesaws, wind or bounce, use Unity's joints, effectors and Physics Materials (see the recipes in **Physics Puzzle Kit**).

### Every screen

**How to Play.** Under your title on the menu, write one line saying what the game is, such as *Play cards to deal damage, block and heal against ever stronger enemies.* Then add a How to Play screen: copy Core's `HowToPlay` UXML into `_Game`, write your goal, controls and rules in a few short lines, and show it from a **How to Play** button on the menu. Players shouldn't have to work out the rules by trial and error.

Menu, pause, win and lose and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every level in your table is in the build, and each can be won.
- [ ] Every material, projectile and puzzle type in your table is in.
- [ ] The game can be played from the menu, through every level, to the win screen, and back to the menu.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] The menu says what the game is, and How to Play explains the goal, controls and rules.
- [ ] Every screen works: menu, pause, win and lose, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your art, or with art packs listed in your ten-pager. Make the materials easy to tell apart at a glance: the player should know glass from stone before they shoot. Keep the sprites' sizes matched to their colliders.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: a Breakable's **On Broken**, the launcher's launch, a target breaking, and the win and lose screens. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch which levels they win on the first shot, and which they give up on. Adjust **Break Speed**, **Starting Shots**, the launcher's **Power**, and the structures. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Breaking, launching and winning each have a sound.
- [ ] Every level has been won by a playtester.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A block or target breaking | **Breakable 2D** → On Broken |
| A shot finishing | The `ShotFinished` event, with a **Void Event Listener** |
| Winning or losing a level | The `PuzzleWon` and `PuzzleLost` events |
| The score changing | The score variable (its Changed event) |

| To make the kit do something… | Call |
|---|---|
| Add or take shots | **IntVariable → Add** on `ShotsLeft` |
| Break something on purpose | **Breakable 2D → Break** |
| Show a screen | **UIScreen → Show** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
