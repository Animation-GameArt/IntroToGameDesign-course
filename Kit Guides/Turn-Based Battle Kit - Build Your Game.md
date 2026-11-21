---
title: "Turn-Based Battle Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Turn-Based Battle Kit — Build Your Game

This guide takes you from your ten-pager to your own finished turn-based battle game, built with the Turn-Based Battle Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Turn-Based Battle Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Turn-Based%20Battle%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Battle_2` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **The party:** who fights for the player, and their stats | | Hero (20 health, Attack 1), Healer (14 health) |
| **Opponents:** who they fight, and their stats | | Slimes (8 health); an Ogre (30 health, Attack 2, Defense 2) |
| **Actions:** each fighter's actions, with effect, target, power, accuracy and uses | | Hero: Slash, Power Strike, Defend, Potion, Firestorm. Healer: Staff, Heal, Defend |
| **Battles:** how many, who's in each, and what each teaches | | 3: choosing; targets and healing; defending |
| **Turn order:** who goes when | | Party first, then opponents |
| **Between battles:** what carries over | | Nothing: each battle starts fresh |
| **Goal:** how the game ends | | Win all three battles |
| **Theme and look:** setting, characters, backdrop | | Fantasy, Tiny Dungeon characters |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. Three to five battles, two or three party members and six to ten actions is a complete battle game in eight weeks.

## Stage 1 — First Playable

The goal: one battle, played from the menu to winning or losing, with your fighters and actions.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data and actions

The sample's `BattleStatus`, `BattleLog`, `BattleRound` and events work as they are. Create your **Battle Action** assets in `_Game/Data` (**Create → Collin Game → Turn-Based Battle Kit → Battle Action**), one per action in your table: Effect, Target, Power, Accuracy, Uses Per Battle, and a short description.

*Worked example:* [Part 1 — Data and actions](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Turn-Based%20Battle%20Kit%20-%20Building%20the%20Sample.md#part-1--data-and-actions).

### 3. Your fighters

For each fighter in your table, make a **Prefab Variant** of `Hero` (party) or `Slime` (opponent) in `_Game/Prefabs`. Set its name, sprite, **Attack**, **Defense**, Health **Max Health** (keep **Invulnerable Time** at `0`), and its **Actions**.

*Worked example:* [Fighters](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Turn-Based%20Battle%20Kit%20-%20Building%20the%20Sample.md#fighters).

### 4. Your first battle

1. In `_Game/Scenes`, create a new 2D scene. Drag in a variant of `Battle Systems` and your fighters: party on the left, opponents on the right.
2. On the Turn Manager, set **Turn Order** from your table.
3. Press **Play** and fight it several times, choosing differently.

*Worked example:* [Battle Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Turn-Based%20Battle%20Kit%20-%20Building%20the%20Sample.md#battle-systems) and [Part 3 — Battles](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Turn-Based%20Battle%20Kit%20-%20Building%20the%20Sample.md#part-3--battles).

### 5. Your menu, win scene and Scene List

1. Copy the kit's `Battle_Menu` and `Battle_Win` into `_Game/Scenes`, point their Scene Changers at your scenes, and change the title.
2. **File → Build Profiles → Open Scene List**: menu, your battles in order, win. The win screen's **Next** loads the next scene in the list.

*Worked example:* [Part 4 — Menu and win scenes](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Turn-Based%20Battle%20Kit%20-%20Building%20the%20Sample.md#part-4--menu-and-win-scenes).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your first battle can be won and lost, and both screens appear.
- [ ] Your party has its own actions, and the menu shows them, with uses left.
- [ ] The log shows what each action did.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every battle and every feature exists and works. Art and balance can still be rough.

### Your other battles

Duplicate your first battle for each one in your table, change the fighters and turn order, and add it to the Scene List. Each battle should need something the last one didn't: healing, a different target, defending.

### All your actions, and custom scripts

Every action in your table is on a fighter and has been used in a test battle.

### Every screen

Menu, pause, win and lose and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every battle in your table is in, in order, and each can be won.
- [ ] Every fighter and action in your table is in.
- [ ] The game can be played from the menu, through every battle, to the end.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, win and lose, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your fighters' art and a backdrop for each battle. Make the party and the opponents easy to tell apart.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Give each **Battle Action** its **Sound**. On each fighter's Health **On Damaged**, add **CameraShake → Shake** for weight. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch which actions they never use, and which battle they lose. Damage is Power + Attack − Defense: adjust those first, then health, then uses. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Every action has a sound.
- [ ] Every action gets used by playtesters; any that doesn't is changed or cut.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A battle being won or lost | The `BattleWon` and `BattleLost` events |
| A fighter being hurt or defeated | **Health** events: On Damaged, On Died |
| A turn starting | **Turn Taker** → On Turn Started |
| A new round | The `BattleRound` variable (its Changed event) |

| To make the kit do something… | Call |
|---|---|
| Damage or heal a fighter | **Health → TakeDamage**, **Heal** |
| End a turn | **Turn Taker → EndTurn** |
| Write to the log | **Battle Log → Add** |
| Show a screen | **UIScreen → Show** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
