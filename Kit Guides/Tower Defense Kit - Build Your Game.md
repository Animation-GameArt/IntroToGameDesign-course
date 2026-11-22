---
title: "Tower Defense Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Tower Defense Kit — Build Your Game

This guide takes you from your ten-pager to your own finished tower defense game, built with the Tower Defense Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Tower Defense Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Tower%20Defense%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `TD_Map` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **The map:** the path enemies take, and where towers can go | | One road with five bends; 8 build spots |
| **Towers:** each one's job, cost, range, damage, rate, and upgrade | | Archer (fast, cheap), Cannon (splash), Frost (slows); one upgrade each |
| **Enemies:** each one's speed, health, reward and lives taken | | Scout (fast), Soldier, Brute (tough), Swarmling (swarms) |
| **Waves:** what comes in each, and the bonus | | 10 waves, growing to mixed groups |
| **Money and lives:** what the player starts with | | $120, 20 lives |
| **Goal:** how the game ends | | Survive all 10 waves |
| **Theme and look:** setting, art, colors | | Kenney's Tower Defense (top-down) |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. One map, three towers with one upgrade each, four enemy types and ten waves is a complete tower defense game in eight weeks. Balancing takes the longest.

## Stage 1 — First Playable

The goal: your map with one tower and one enemy type, three waves, from the menu to winning or losing.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data

The sample's `Money`, `Lives`, `Wave` and events work as they are.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Tower%20Defense%20Kit%20-%20Building%20the%20Sample.md#part-1--data).

### 3. Your first tower and enemy

1. Duplicate the sample's `Archer` **Tower** asset (**Ctrl+D**), move the copy to `_Game/Data`, and set it from your table. Make a **Prefab Variant** of its tower prefab for the look.
2. Make a variant of the closest enemy (`Scout`, `Soldier`, `Brute`, `Swarmling`): **Speed**, **Reward**, **Lives Taken**, Health **Max Health**.

*Worked example:* [Part 2 — Projectiles and towers](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Tower%20Defense%20Kit%20-%20Building%20the%20Sample.md#part-2--projectiles-and-towers) and [Part 3 — Enemies](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Tower%20Defense%20Kit%20-%20Building%20the%20Sample.md#part-3--enemies).

### 4. Your map

1. In `_Game/Scenes`, create a 2D scene; set the camera's **Size** so the whole map fits.
2. Paint the ground and your road on Tilemaps.
3. Add a `Path` with **Enemy Path 2D**, with a child at each bend, starting and ending off screen.
4. Drag in a variant of `TD Systems`. Set the **Tower Wave Spawner**'s **Path**, **Starting Money**, **Starting Lives**, and your first three waves. On the **UI Build Menu**, set **Towers** to yours.
5. Place `Build Spot`s beside the road, on the insides of bends.

*Worked example:* [Part 4 — TD Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Tower%20Defense%20Kit%20-%20Building%20the%20Sample.md#part-4--td-systems) and [Part 5 — The map (`TD_Map`)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Tower%20Defense%20Kit%20-%20Building%20the%20Sample.md#part-5--the-map-td_map).

### 5. Your menu and Scene List

Copy the kit's `TD_Menu` into `_Game/Scenes`, make Play load your map, and change the title. In the Scene List: menu, then your map.

*Worked example:* [Part 6 — Menu](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Tower%20Defense%20Kit%20-%20Building%20the%20Sample.md#part-6--menu).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Enemies follow your path; leaking ones cost lives.
- [ ] Your first tower can be built, upgraded and sold, and kills enemies for money.
- [ ] Three waves can be started, cleared and won; 0 lives shows the lost screen.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every wave and every feature exists and works. Art and balance can still be rough.

### All your towers and enemies

Add every tower (with its upgrade) and every enemy in your table. Each tower needs a job no other tower does better.

### All your waves

Fill in every wave. Introduce each enemy alone first, then mix them. Give the last wave a real test of everything.

### Every screen

**How to Play.** Under your title on the menu, write one line saying what the game is, such as *Play cards to deal damage, block and heal against ever stronger enemies.* Then add a How to Play screen: copy Core's `HowToPlay` UXML into `_Game`, write your goal, controls and rules in a few short lines, and show it from a **How to Play** button on the menu. Players shouldn't have to work out the rules by trial and error.

Menu, pause, won and lost and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every tower, upgrade and enemy in your table is in.
- [ ] Every wave is in, and the game can be won.
- [ ] Each tower gets built in a normal game; if one never does, its job is fixed or it's cut.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] The menu says what the game is, and How to Play explains the goal, controls and rules.
- [ ] Every screen works: menu, pause, won and lost, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your art. Each tower must be recognisable at a glance, and so must each enemy, even when small and in a crowd.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: each **Tower 2D**'s **On Shoot**, enemies' Health **On Died**, a **Path Enemy 2D**'s **On Reached End** (a lost life), and the wave spawner's **On Wave Started** and **On Wave Cleared**. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch where enemies leak and how much money is left over. Work out each tower's damage per second (Damage × Shots Per Second) and compare it with each wave. Adjust one number at a time. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Shots, kills, lost lives and wave starts each have a sound.
- [ ] A first-time player can win, with some losses.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A wave starting or cleared | **Tower Wave Spawner** → On Wave Started, On Wave Cleared |
| Winning | **Tower Wave Spawner** → On Won, or the won event |
| An enemy leaking | **Path Enemy 2D** → On Reached End |
| A tower firing | **Tower 2D** → On Shoot |

| To make the kit do something… | Call |
|---|---|
| Start the next wave | **Tower Wave Spawner → StartNextWave** |
| Slow an enemy | **Path Enemy 2D → Slow** |
| Give money | **IntVariable → Add** on `Money` |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
