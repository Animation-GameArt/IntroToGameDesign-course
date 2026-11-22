---
title: "Platformer Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Platformer Kit — Build Your Game

This guide takes you from your ten-pager to your own finished platformer, built with the Platformer Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Platformer Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from the menu to the win screen.
- [ ] You've opened `Platformer_Level1` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **The character:** who they are, and the art | | A green alien, from Kenney's Pixel Platformer |
| **Movement feel:** speed, jump height, double jump or not, floaty or snappy | | Max Speed `7`, Jump Height `3`, no double jump, a little snappy |
| **Health and lives:** hits per life, lives, what happens at 0 | | 3 health, 3 lives, Game Over screen |
| **Levels:** how many, and the one idea each level is about (teach, test, twist) | | 2: jumping and stomping; then moving platforms and flyers |
| **Collectibles:** what they are, how many per level, and what they're for | | Coins (score), hearts (heal), a key per level (opens a lock) |
| **Hazards and enemies:** which ones, and where they first appear | | Spikes and pits; walkers (stomp them), flyers (avoid them) |
| **Goal:** how a level ends, and how the game ends | | Touch the gem; after the last level, the win screen |
| **Theme and look:** tiles, background, colors | | Grass world, pale blue sky |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. Two or three levels, each built around one idea, is a complete game in eight weeks.

## Stage 1 — First Playable

The goal: one level, played from the menu to the goal or to Game Over, with grey boxes or the kit's art. No polish.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data

The sample's `Coins`, `Lives`, `PlayerHealth` and events (in the kit's `Sample/Data`) work as they are. Make your own only where your decisions differ:

- **A different starting number of lives:** create an **Int Variable** in `_Game/Data` (such as `MyLives`, Initial Value from your table), and use it everywhere the sample uses `Lives`: your player variant's **Health → On Died**, your `Level Systems` variant, the menu and the win scene.
- **A collectible with a different name or purpose:** create an Int Variable for it, such as `Gems` or `Score`.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md#part-1--data).

### 3. Your player

1. Right-click the kit's `Player` prefab → **Create → Prefab Variant**. Move it to `_Game/Prefabs` and name it after your character.
2. Open it. On **Platformer Controller 2D**, set the movement from your table. Use what you learned in Exercise 03: Max Speed and Acceleration for speed and weight; Jump Height and Fall Gravity Multiplier for floaty or snappy; Extra Air Jumps `1` for a double jump.
3. On **Health**, set Max Health from your table.
4. Placeholder art is fine for now. If your character art is ready, change the Sprite Renderer's sprite, and the Idle, Walk and In Air sprites on the **Platformer Sprite Animator**.

*Worked example:* [Part 3 — Prefabs, Player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md#player).

### 4. Your Level Systems

1. Make a **Prefab Variant** of the kit's `Level Systems`, in `_Game/Prefabs`.
2. If you made your own variables in step 2, swap them in: `Game Rules` (the Int Variable Condition and the Variable Resetter), and the **UI Variable Binder** on the HUD, Level Complete and Game Over.
3. Change the HUD's label formats to your words, such as `Gems: {0}`.
4. On `To Menu`, set Scene Name to your menu scene's name (you'll make it in step 7).

*Worked example:* [Part 3 — Prefabs, Level Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md#level-systems).

### 5. Your first level, blocked in

Build level 1 from your table: the one idea it teaches.

1. In `_Game/Scenes`, create a new 2D scene named after your game, such as `Glowbug_Level1`.
2. Drag in your `Level Systems` variant and your player variant.
3. Add a Cinemachine camera that follows the player, with bounds, as in Exercise 04.
4. Add a Tilemap with a **Tilemap Collider 2D** for the ground, as in Exercise 04. Paint the level's shape with the kit's `Platformer Palette` (or plain squares).
5. Place a checkpoint near the start, the goal (`Goal Gem` or your variant) at the end, and the pit below everything (it's in Level Systems; move it if your level goes lower).
6. Add only what this level's idea needs: if it's about jumping, gaps and platforms; if it's about stomping, a few `Walker`s.

> [!tip] Teach, test, twist
> Show the idea somewhere safe first, then test it where a mistake costs something, then twist it once. That's a whole level.

*Worked example:* [Part 5 — Level 1](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md#part-5--level-1).

### 6. Your pieces

For each collectible, hazard and enemy in your table, make a **Prefab Variant** of the closest kit prefab in `_Game/Prefabs`, and change it:

| Your piece is like… | Start from | Usually change |
|---|---|---|
| Something to collect | `Coin` | Add To (your variable), Amount, the sprite |
| Something that heals | `Heart` | Heal |
| Something that opens a way | `Key` and `Lock` | The sprites; for "collect ten", see the recipe in **Platformer Kit** |
| A ground enemy | `Walker` | Patrol Speed, Chase Range; Health for two stomps |
| A flying enemy or moving hazard | `Flyer` | Stops, Speed |
| A fixed hazard | `Spikes` | Damage, the sprite |
| Something that launches the player | `Spring` | Bounce Height |

Anything in your table that none of these can do is a custom script: see **Custom scripts** below.

### 7. Your menu and win scenes

1. Copy the kit's `Platformer_Menu` and `Platformer_Win` scenes into `_Game/Scenes` (select them, **Ctrl+D**, then move and rename the copies).
2. In your menu, set the **Scene Changer** on `Main Menu` to load your first level. In your win scene, set `To Level 1` and `To Menu` to your scenes.
3. If you made your own variables, swap them into both scenes' `Game Rules` and binders.
4. Change the title text to your game's name. You can copy the UXML into `_Game` and edit it in the UI Builder, or leave the kit's look for now.

*Worked example:* [Part 7 — Menu scene](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md#part-7--menu-scene) and [Part 8 — Win scene](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md#part-8--win-scene).

### 8. Your Scene List

**File → Build Profiles → Open Scene List**: remove the kit's sample scenes, and add yours in order: menu, level 1, (later levels), win. **Next Level** loads whichever scene comes next.

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your character moves and jumps with the feel in your table.
- [ ] Level 1 can be played from start to goal; reaching the goal shows Level Complete.
- [ ] Losing all health costs a life and returns you to the checkpoint; losing all lives shows Game Over, and Try Again works.
- [ ] Your main collectible counts on the HUD.
- [ ] At least one enemy or hazard from your table is in.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every level and every feature exists and works. Art and balance can still be rough.

### 9. Your other levels

For each level in your table:

1. Duplicate your level 1 scene, rename it, and clear out the level (keep Level Systems, the player and the camera).
2. Build it around that level's idea. Bring back earlier ideas in new combinations; that's how levels get harder without new rules.
3. Add it to the Scene List, before the win scene.

### 10. All your pieces, and custom scripts

Every collectible, hazard and enemy in your table is in at least one level, and each custom script is working (see below).

### 11. Every screen

**How to Play.** Under your title on the menu, write one line saying what the game is, such as *Play cards to deal damage, block and heal against ever stronger enemies.* Then add a How to Play screen: copy Core's `HowToPlay` UXML into `_Game`, write your goal, controls and rules in a few short lines, and show it from a **How to Play** button on the menu. Players shouldn't have to work out the rules by trial and error.

Menu, pause, Level Complete, Game Over, win and credits all work. Add your own assets to the credits: create a text file like the kit's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every level in your table is in the build and can be played through.
- [ ] Every collectible, hazard and enemy in your table is in.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] The game can be played from the menu, through every level, to the win screen, and back to the menu with lives and score reset.
- [ ] The menu says what the game is, and How to Play explains the goal, controls and rules.
- [ ] Every screen works: menu, pause, Level Complete, Game Over, win, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### 12. Art

Replace placeholders with your art, or with art packs listed in your ten-pager. Make sprite variants of your prefabs rather than editing the kit's. Keep sizes consistent: the kit's tiles are 18 pixels, at 18 pixels per unit.

### 13. Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events: the player's **On Jump** and **On Land**, a collectible's **On Collected**, an enemy's stomp, Health's **On Damaged**. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### 14. Balance

Playtest with someone who hasn't played it (Exercise 10). Watch where they die and where they get bored. Change one number at a time: gap widths, enemy speed, checkpoint spacing, lives.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Every collectible, jump, stomp, hit and death has a sound.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| The player being hurt or dying | **Health** events: On Damaged, On Died |
| A collectible being picked up | **Collectible** → On Collected, or the variable it adds to (its Changed event) |
| A level ending | The `LevelCompleted` event, with a **Void Event Listener** |
| The player jumping or landing | **Platformer Controller 2D** → On Jump, On Land |

| To make the kit do something… | Call |
|---|---|
| Damage or heal the player | **Health → TakeDamage**, **Heal** |
| Send the player back | **Respawner → Respawn** |
| Change a number | **IntVariable → Add**, **SetValue** |
| Show a screen | **UIScreen → Show** |

Your instructor can help you plan a custom script; the **Script Reference** lists everything the kit's scripts can do.
