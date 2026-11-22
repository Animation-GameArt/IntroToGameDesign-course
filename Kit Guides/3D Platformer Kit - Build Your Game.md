---
title: "3D Platformer Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# 3D Platformer Kit — Build Your Game

This guide takes you from your ten-pager to your own finished 3D platformer, built with the 3D Platformer Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[3D Platformer Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Islands_Level` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **The character:** who, and the art (a capsule is fine until Beta) | | A capsule with a nose |
| **Movement feel:** speed, jump height, double jump, floaty or snappy | | Walk `6`, sprint `9`, Jump Height `2.2`, a double jump |
| **Camera:** orbiting, or fixed behind | | Orbiting, Radius `7` |
| **Areas:** how many, and the one idea each teaches | | 3: stepping stones; moving and crumbling platforms; a tower with enemies |
| **Collectibles:** what, how many, and what they're for | | 20 coins, for score |
| **Enemies and hazards:** which, and where they first appear | | Patrolling enemies to stomp; falling |
| **Health:** hearts, and what a fall does | | 3 hearts; falling returns you to the last checkpoint |
| **Goal:** how the level ends | | Reach the flag at the top |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. One level with three areas and twenty collectibles is a complete 3D platformer in eight weeks. 3D levels take longer to build and test than 2D ones.

## Stage 1 — First Playable

The goal: your character and camera, and your first area, from the menu to the goal or falling, in grey boxes.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data and materials

Create `Coins` and `PlayerHealth` Int Variables and a `LevelWon` Void Event Channel in `_Game/Data`, and a few plain materials to tell surfaces apart.

*Worked example:* [Part 1 — Data and materials](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Building%20the%20Sample.md#part-1--data-and-materials).

### 3. Your scene, player and camera

1. Create a 3D scene in `_Game/Scenes`; set the camera's **Renderer** to **Universal Renderer**.
2. Build your player (or copy the sample's): **Player Controller 3D** with the feel from your table, **Health**, **Respawner**, and **Blob Shadow 3D**.
3. Add the orbit camera, and **Cursor Lock 3D**.
4. Walk and jump on a big flat floor until the movement feels like your table.

*Worked example:* [Part 3 — The player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Building%20the%20Sample.md#part-3--the-player) and [Part 4 — The orbit camera](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Building%20the%20Sample.md#part-4--the-orbit-camera).

### 4. Your first area

1. Block out your first area with Cubes. Measure gaps: about 4 units across walking, 6 sprinting, 2 units up.
2. Add a Checkpoint at its start, coins along the route, and a Kill Zone below everything.
3. Add your goal (a Trigger Zone raising `LevelWon`) at the end, for now.

*Worked example:* [Part 5 — Prefabs](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Building%20the%20Sample.md#part-5--prefabs) and [Part 6 — The level](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Building%20the%20Sample.md#part-6--the-level).

### 5. Systems, menu and Scene List

Copy the sample's `Islands Systems` (HUD, pause, win screen) into your scene with your variables, and copy `Islands_Menu` into `_Game/Scenes` with Play loading your level. In the Scene List: menu, then your level.

*Worked example:* [Part 7 — Islands Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Building%20the%20Sample.md#part-7--islands-systems) and [Part 8 — Menu](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/3D%20Platformer%20Kit%20-%20Building%20the%20Sample.md#part-8--menu).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your character moves relative to the camera, with the feel in your table; the camera orbits with the mouse and right stick.
- [ ] Your first area can be crossed; falling returns you to the checkpoint.
- [ ] Coins count on the HUD; the goal shows the win screen with the pointer back.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every area and every feature exists and works. Art and balance can still be rough.

### Your other areas

Block out each area in your table around its idea: moving and crumbling platforms, bounce pads, enemies. Put a Checkpoint at the start of each, and a landmark players can see from far away.

### All your pieces

Every collectible, enemy and platform in your table is in, and all collectibles can be reached.

### Every screen

**How to Play.** Under your title on the menu, write one line saying what the game is, such as *Play cards to deal damage, block and heal against ever stronger enemies.* Then add a How to Play screen: copy Core's `HowToPlay` UXML into `_Game`, write your goal, controls and rules in a few short lines, and show it from a **How to Play** button on the menu. Players shouldn't have to work out the rules by trial and error.

Menu, pause, the win screen and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every area in your table is in, and the level can be finished.
- [ ] Every collectible can be reached, and every enemy and platform type is in.
- [ ] The camera never leaves the player hidden for long (add a Cinemachine Deoccluder if it does).
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] The menu says what the game is, and How to Play explains the goal, controls and rules.
- [ ] Every screen works: menu, pause, the win screen, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace grey boxes with your art, or a 3D art pack from your ten-pager. Keep the player's path readable: walkable surfaces one color family, hazards another.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: Player Controller 3D's **On Jump** and **On Landed**, coins' **On Collected**, **Bounce Pad 3D**'s **On Bounce**, Patrol Enemy 3D's **On Stomped**, and Health's **On Damaged**. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch where they fall and where the camera gets in the way. Adjust gaps, checkpoint spacing and the camera's distance. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Jumping, landing, coins, stomps and hits each have a sound.
- [ ] A playtester finished the level without help.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| Jumping or landing | **Player Controller 3D** → On Jump, On Landed |
| A stomp | **Patrol Enemy 3D** → On Stomped |
| A platform crumbling | **Crumbling Platform 3D** → On Crumble |
| Being hurt | **Health** → On Damaged |

| To make the kit do something… | Call |
|---|---|
| Launch the player | **Player Controller 3D → Bounce** |
| Start a platform | **Moving Platform 3D → StartMoving** |
| Show the pointer | **Cursor Lock 3D → Unlock** |
| Send the player back | **Respawner → Respawn** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
