---
title: "Grid Puzzle Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Grid Puzzle Kit — Build Your Game

This guide takes you from your ten-pager to your own finished grid puzzle game, built with the Grid Puzzle Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Grid Puzzle Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Grid%20Puzzle%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Puzzle_03` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **The rule:** what the player pushes or collects, and how a level is solved | | Push boxes onto targets |
| **Pieces:** player, pushable, solid, items, and any kinds | | Boxes, red boxes for red targets, rocks, gems |
| **Pushing:** how many in a row can be pushed | | One, as in Sokoban |
| **Levels:** how many, and the one idea each teaches | | 8, from "First Push" to combining everything |
| **Solving:** targets, collecting every item, reaching the exit | | Every target filled; some levels need every gem |
| **Moves:** about how many moves each level should take | | 2 to 23 |
| **Theme and look:** setting, art, colors | | Warehouse, Kenney's Sokoban pack |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. One rule, plus one twist, over eight to twelve levels is a complete puzzle game in eight weeks. Level design is most of the work.

## Stage 1 — First Playable

The goal: your rule working in three levels, chosen from a level select, with undo and restart.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your Level List

Create a **Level List** in `_Game/Data` (**Create → Collin Game → Grid Puzzle Kit → Level List**) and give it a **Save Name** of your own, so your progress doesn't mix with the sample's.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Grid%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-1--data).

### 3. Your pieces

For each piece in your table, make a **Prefab Variant** of the closest kit prefab (`Player`, `Box`, `Red Box`, `Rock`, `Gem`, `Target`, `Red Target`, `Exit`) in `_Game/Prefabs`. Set **Kind** for pieces that only fit their own goals. Change the sprites when your art is ready.

*Worked example:* [Part 2 — Prefabs](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Grid%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-2--prefabs).

### 4. Your first level

1. Open `Puzzle_01`, **File → Save As…** into `_Game/Scenes` as your level 1.
2. On `Puzzle Systems` → `Board`, set **Level List** to yours, and **Max Pushed In A Row** and **Need All Items** from your table.
3. Repaint the walls and place your pieces and goals. Solve it, and count the moves.
4. Add the scene's name to your Level List and the Scene List.

*Worked example:* [Part 3 — Puzzle Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Grid%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-3--puzzle-systems) and [Part 4 — The level template (`Puzzle_01`)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Grid%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-4--the-level-template-puzzle_01).

### 5. Two more levels

Save As again for levels 2 and 3, each teaching one idea from your table. Add each to the Level List and the Scene List.

*Worked example:* [Part 5 — Eight levels](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Grid%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-5--eight-levels).

### 6. Your menu, level select and Scene List

Copy the kit's `Puzzle_Menu` and `Puzzle_Select` into `_Game/Scenes`. Set their **Puzzle Level Loader**'s **Level List** to yours, and change the title. In the Scene List: menu, level select, then your levels in order.

*Worked example:* [Part 6 — Menu and level select](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Grid%20Puzzle%20Kit%20-%20Building%20the%20Sample.md#part-6--menu-and-level-select).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your rule works: pieces move, push and fill goals as your table says.
- [ ] Three levels can be solved, and solving one unlocks the next.
- [ ] Undo (Z) and Restart (R) work.
- [ ] The level select shows locked, unlocked and solved levels.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every level and every feature exists and works. Art and balance can still be rough.

### All your levels

Build the rest of your levels. Write each level's idea before you build it. Solve each one yourself and note the moves. Order them so each teaches before it tests.

### Your twist, and custom scripts

Your rule's twist (a kind of piece, items to collect, an exit) is in at least three levels.

### Every screen

**How to Play.** Under your title on the menu, write one line saying what the game is, such as *Play cards to deal damage, block and heal against ever stronger enemies.* Then add a How to Play screen: copy Core's `HowToPlay` UXML into `_Game`, write your goal, controls and rules in a few short lines, and show it from a **How to Play** button on the menu. Players shouldn't have to work out the rules by trial and error.

Menu, pause, level select and solved and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every level in your table is in, in order, and each has been solved.
- [ ] Every piece in your table is in.
- [ ] Progress saves: quitting and coming back keeps solved levels.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] The menu says what the game is, and How to Play explains the goal, controls and rules.
- [ ] Every screen works: menu, pause, level select and solved, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your art. Every kind of piece and goal must be recognisable at a glance, including which goal each kind fits.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: a piece's **On Moved**, the board's **On Blocked** (a bump) and **On Undo**, a goal's **On Filled**, and the board's **On Solved**. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch silently where they get stuck. A level nobody solves needs a hint or a simpler layout; one everyone solves instantly can be cut or made later. Reorder levels if needed. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Moving, pushing, being blocked, undoing and solving each have a sound.
- [ ] Every level has been solved by a playtester without help, or simplified.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A level being solved | **Grid Board** → On Solved |
| A move being blocked | **Grid Board** → On Blocked |
| An undo | **Grid Board** → On Undo |
| A piece moving, or an item collected | **Grid Piece** → On Moved, On Collected |
| A goal filled or emptied | **Grid Goal** → On Filled, On Emptied |

| To make the kit do something… | Call |
|---|---|
| Undo or restart | **Grid Board → Undo**, **Restart** |
| Load a level | **Puzzle Level Loader → LoadNextLevel**, **LoadLevel**, **LoadFirstUnsolved** |
| Show a screen | **UIScreen → Show** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
