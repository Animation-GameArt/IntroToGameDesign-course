---
title: "Top-Down Shooter Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Top-Down Shooter Kit — Build Your Game

This guide takes you from your ten-pager to your own finished top-down shooter, built with the Top-Down Shooter Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Top-Down Shooter Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Shooter_Arena` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **Arena or scrolling:** one arena with waves, or a level that scrolls | | Both: a 4-wave arena, and a scrolling level with a boss |
| **The player:** ship or character, speed, health | | A ship, Max Speed `6`, 5 health |
| **Weapons:** each one's fire rate, bullets per shot, spread, damage | | Blaster; Spread Shot and Rapid Fire as 10-second power-ups |
| **Enemies:** each one's movement, health, points, and whether it shoots | | Drone (chases), Gunship (circles and shoots), Weaver (weaves down), Boss |
| **Waves or layout:** what comes when | | Waves of 6 drones, then drones and gunships, then the boss |
| **Pickups and drops:** what enemies leave behind | | Weapon power-ups and hearts, sometimes |
| **Goal:** how the game ends | | Clear the last wave, or defeat the boss |
| **Theme and look:** setting, art, colors | | Space, Kenney's Pixel Shmup |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. One arena with five or six waves, or one scrolling level with a boss, is a complete shooter in eight weeks.

## Stage 1 — First Playable

The goal: your player shooting your first enemies, in one arena or the first part of a level, from the menu to winning or dying.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data and weapons

The sample's `Score`, `PlayerHealth`, `WeaponName` and events work as they are. Create your **Weapon** assets in `_Game/Data` (**Create → Collin Game → Top-Down Shooter Kit → Weapon**), or duplicate the sample's (**Ctrl+D**) and change the copies: **Shots Per Second**, **Projectiles Per Shot**, **Spread Angle**, **Damage**.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Building%20the%20Sample.md#part-1--data) and [Part 2 — Projectiles and weapons](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Building%20the%20Sample.md#part-2--projectiles-and-weapons).

### 3. Your player

Make a **Prefab Variant** of `Player Ship` in `_Game/Prefabs`. Set its speed, **Max Health**, and its Weapon Shooter 2D's **Weapon** from your table. Change the sprite when your art is ready.

*Worked example:* [Part 3 — The player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Building%20the%20Sample.md#part-3--the-player).

### 4. Your first enemies

For each enemy in your table, make a variant of the closest kit enemy (`Drone`, `Gunship`, `Weaver` or `Boss`). Set its **Enemy Mover 2D** pattern and speed, its Health, the points its **On Died** adds, and its weapon if it shoots. Start with one or two kinds.

*Worked example:* [Part 4 — Enemies](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Building%20the%20Sample.md#part-4--enemies).

### 5. Your first arena or level

**An arena:** in `_Game/Scenes`, create a 2D scene. Drag in a variant of `Arena Systems` and your player. Set the camera's **Size**, add walls, move the spawn points to just outside the walls, and set your first two waves on **Wave Spawner 2D**.

**A scrolling level:** open `Shooter_Scrolling`, **File → Save As…** into `_Game/Scenes`, replace the player and enemies with yours, and place enemies along the first stretch.

*Worked example:* [Part 6 — Arena Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Building%20the%20Sample.md#part-6--arena-systems) and [Part 7 — The arena (`Shooter_Arena`)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Building%20the%20Sample.md#part-7--the-arena-shooter_arena).

### 6. Your menu, win scene and Scene List

Copy the kit's `Shooter_Menu` and `Shooter_Win` into `_Game/Scenes`, point their Scene Changers at your scenes, and change the title. In the Scene List: menu, your game, win.

*Worked example:* [Part 9 — Menu and win scenes](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit%20-%20Building%20the%20Sample.md#part-9--menu-and-win-scenes).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your player moves, aims and fires your first weapon, with mouse and with a gamepad.
- [ ] At least one enemy type from your table attacks and can be destroyed for points.
- [ ] Dying shows Game Over; clearing the first waves (or reaching the end) shows the win screen.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every wave and every feature exists and works. Art and balance can still be rough.

### All your waves or your whole level

Fill in every wave on **Wave Spawner 2D**, or place enemies along the whole scrolling level, ending with your boss. Each wave or stretch should add something: a new enemy, more at once, a new direction.

### All your weapons, enemies and pickups

Every weapon, enemy and drop in your table is in. Weapons the player picks up are **Power-Up** prefabs with your Weapon and a **Duration**; enemies leave them with **Drop On Death 2D**.

### Every screen

Menu, pause, Game Over and win and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every wave or stretch in your table is in, and the game can be finished.
- [ ] Every weapon, enemy and pickup in your table is in.
- [ ] The HUD shows score, health, wave and weapon.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, Game Over and win, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your art. In a shooter, bullets must be impossible to miss: the player's and the enemies' bullets should be different, bright colors that stand out from the background.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: each **Weapon Shooter 2D**'s **On Shoot**, enemies' Health **On Died**, the player's **On Damaged**, power-ups' **On Collected**, and each wave's **On Wave Started**. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch where they die and how long each wave takes. Adjust enemy counts and health, fire rates and damage, and how often drops appear. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Shooting, hits, explosions and pickups each have a sound.
- [ ] Bullets are easy to see against every background.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A wave starting, or all waves cleared | **Wave Spawner 2D** → On Wave Started, On Cleared |
| An enemy destroyed | Its **Health** → On Died |
| The player firing | **Weapon Shooter 2D** → On Shoot |
| The scrolling camera reaching the end | **Scroll Camera 2D** → On Reached End |

| To make the kit do something… | Call |
|---|---|
| Give the player a weapon | **Weapon Shooter 2D → SetWeapon** |
| Start the waves | **Wave Spawner 2D → Begin** |
| Stop or restart scrolling | **Scroll Camera 2D → PauseScrolling**, **ResumeScrolling** |
| Add points | **IntVariable → Add** on `Score` |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
