---
title: "Top-Down Adventure Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Top-Down Adventure Kit — Build Your Game

This guide takes you from your ten-pager to your own finished top-down adventure, built with the Top-Down Adventure Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Top-Down Adventure Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Adventure_Dungeon` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **The hero:** who they are, and the art | | A hero from Kenney's Tiny Dungeon |
| **Combat:** sword reach and damage, hearts | | A short sword, 1 damage, 5 hearts |
| **Rooms:** how many, and what each is for | | 3: entrance, slime room, treasure room |
| **Enemies:** which ones, how many hits each takes, where they first appear | | Slimes (2 hits) in room 2; a bat (fast, flies) in room 3 |
| **Keys and doors:** what's locked, and where its key is | | One locked door to the treasure room; its key is in the slime room |
| **Things to read or talk to:** signs, people, chests, and what they say | | A sign at the entrance; the treasure chest |
| **Collectibles:** coins, hearts, anything else, and what they're for | | Coins (score), hearts (heal) |
| **Goal:** how the game ends | | Open the treasure chest |
| **Theme and look:** setting, tiles, colors | | A stone dungeon |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. Five to eight rooms, three enemy types and one goal is a complete adventure in eight weeks.

## Stage 1 — First Playable

The goal: two or three rooms, played from the menu to the goal or to dying, with the kit's art or grey boxes.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data

The sample's `PlayerHealth`, `Keys`, `Coins`, `Message` and `DungeonCleared` (in the kit's `Sample/Data`) work as they are. Make your own where your decisions differ, such as a different number of hearts (an Int Variable with that Initial Value) or a collectible of your own.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Building%20the%20Sample.md#part-1--data).

### 3. Your hero

Make a **Prefab Variant** of `Player` in `_Game/Prefabs`. Set **Max Health** from your table, the **Melee Attack 2D**'s **Reach**, **Radius** and **Damage**, and the **Top Down Controller 2D**'s speed. Change the sprite when your art is ready.

*Worked example:* [Player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Building%20the%20Sample.md#player).

### 4. Your Level Systems

Make a variant of `Level Systems`. If you made your own variables, swap them into the HUD's **UI Heart Row** (Max Hearts) and **UI Variable Binder**.

*Worked example:* [Level Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Building%20the%20Sample.md#level-systems).

### 5. Your first rooms

1. In `_Game/Scenes`, create a new 2D scene. Drag in your Level Systems and hero.
2. Paint floors on one Tilemap and walls on another (walls with **Tilemap Collider 2D** and **Composite Collider 2D**), as in Exercise 04.
3. Add a `Room` over each room, sized to cover it exactly. Put each room's enemies under one object and drag it into that Room's **Room Contents**.
4. Add a Checkpoint near the start, and the pieces your first rooms need.

*Worked example:* [Part 3 — The dungeon](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Building%20the%20Sample.md#part-3--the-dungeon).

### 6. Your pieces

For each enemy, pickup and object in your table, make a variant of the closest kit prefab:

| Your piece is like… | Start from | Usually change |
|---|---|---|
| A ground enemy | `Slime` | Max Health, **Notice Range**, **Chase Speed**, Damage |
| A fast or flying enemy | `Bat` | **Chase Speed**, **Needs Line Of Sight** |
| Something to collect | `Coin`, `Heart` | Add To, Amount, Heal |
| A key and what it opens | `Key`, `Locked Door` | **Keys Needed**, the sprites |
| A sign or a person | `Sign` | **Lines** |
| The goal | `Treasure Chest` | **Lines**, what **On Used** raises |

*Worked example:* [Pickups](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Building%20the%20Sample.md#pickups) and [Sign and Treasure Chest](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Building%20the%20Sample.md#sign-and-treasure-chest).

### 7. Your menu, win scene and Scene List

1. Copy the kit's `Adventure_Menu` and `Adventure_Win` into `_Game/Scenes`. Point their Scene Changers at your scenes, and change the title.
2. **File → Build Profiles → Open Scene List**: remove the sample scenes; add yours: menu, your game scene(s), win.

*Worked example:* [Part 4 — Menu and win scenes](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Building%20the%20Sample.md#part-4--menu-and-win-scenes).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your hero moves and attacks with the reach and damage in your table.
- [ ] At least two rooms, with the camera staying inside each room.
- [ ] At least one enemy type fights back and can be defeated; losing all hearts returns you to a checkpoint.
- [ ] The goal can be reached, and shows the win screen.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every room and every feature exists and works. Art and balance can still be rough.

### Your other rooms

Build the rest of your rooms. Give each one a job: teach an enemy, hide a key, test what was taught. Put signs where the player needs a hint.

### All your pieces, and custom scripts

Every enemy, key, door and talking object in your table is in. Check every locked door has its key reachable before it.

### Every screen

Menu, pause, the win screen and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every room in your table is in, and the whole game can be played from the first room to the goal.
- [ ] Every enemy, key, door and sign in your table is in.
- [ ] Returning to a room brings its enemies back, and the camera never shows outside a room.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, the win screen, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your art, or art packs listed in your ten-pager. Make enemies and pickups stand out from the floor. Keep the tiles' Pixels Per Unit the same across all your art.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: the sword swing (**Melee Attack 2D**), Health **On Damaged** for the hero and enemies, Collectible **On Collected**, a door opening, and the chest. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch where they lose hearts and where they wander lost. Adjust enemy speed and health, heart pickups, checkpoint spacing, and signs. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Every hit, pickup and door has a sound.
- [ ] A playtester finished the game without help.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| The hero being hurt or dying | **Health** events: On Damaged, On Died |
| A sword hit | **Melee Attack 2D** → On Hit |
| Picking something up | **Collectible** → On Collected |
| Entering a room | **Camera Room 2D** → On Entered |
| Talking or opening | **Interactable 2D** → On Used |

| To make the kit do something… | Call |
|---|---|
| Hurt or heal | **Health → TakeDamage**, **Heal** |
| Show a message | **StringVariable → SetValue** on `Message` |
| Change a number | **IntVariable → Add**, **SetValue** |
| Show a screen | **UIScreen → Show** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
