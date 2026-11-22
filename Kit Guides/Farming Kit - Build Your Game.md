---
title: "Farming Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Farming Kit — Build Your Game

This guide takes you from your ten-pager to your own finished farming game, built with the Farming Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Farming Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Farming%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Farm_Game` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **The farmer and the place:** who, where, and the art | | A farmer from Tiny Dungeon on a Tiny Town farm |
| **Crops:** each one's seed price, days to grow, sell price, regrowing, and dying when dry | | Mushrooms (quick, cheap), Berry Bush (regrows), Goldleaf (slow, valuable, dies dry) |
| **Tools:** which, and what each does | | Hoe, watering can, shovel |
| **Field:** size, and anything else to farm | | One 4 × 4 field |
| **Days:** seconds per day, and the last day | | 240 seconds; 14 days |
| **Energy:** how much, and what costs it | | 30 a day; 1 per tool use |
| **Shop:** what it sells and buys | | Seeds; buys every crop |
| **Goal:** how the game ends | | Earn $800 by day 14 |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. One field, three crops, one shop and a goal is a complete farming game in eight weeks. Villagers, animals and seasons are custom scripts, and big ones.

## Stage 1 — First Playable

The goal: one crop growing from seed to sale, over several days, from the menu to winning or running out of time.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data and soil

Create Int Variables for `Money`, `Day` and `Energy`, a String Variable `Clock`, and win and lose Void Event Channels in `_Game/Data`, with starting values from your table. Create two **Tile** assets for tilled and watered soil.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Farming%20Kit%20-%20Building%20the%20Sample.md#part-1--data) and [Part 2 — Soil tiles](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Farming%20Kit%20-%20Building%20the%20Sample.md#part-2--soil-tiles).

### 3. Your items and first crop

Create your tools and one crop's seed and produce as **Items** (**Create → Collin Game → Farming Kit → Item**), and its **Crop** (**Create → Collin Game → Farming Kit → Crop**): stage sprites, **Days Per Stage**, produce, regrowing. Point the seeds at the crop, and the crop at its produce.

*Worked example:* [Part 3 — Items and crops](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Farming%20Kit%20-%20Building%20the%20Sample.md#part-3--items-and-crops).

### 4. Your farmer

Make a **Prefab Variant** of the sample's `Player` (or build one the same way): **Inventory** with your tools and some seeds in **Starting Items**, **Farmer Tools 2D** with your Energy and **Energy Per Use**.

*Worked example:* [Part 4 — The player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Farming%20Kit%20-%20Building%20the%20Sample.md#part-4--the-player).

### 5. Your farm

1. Open `Farm_Game`, **File → Save As…** into `_Game/Scenes`.
2. Repaint the field on the `Farmland` tilemap, and the world around it. Set the **Farm Field**'s soil tiles to yours.
3. Swap your data into `Farm Systems`: the **Day Cycle** (day, clock, last day, Reset Each Morning), the win condition, **UI Shop** (For Sale, Money) and the **UI Variable Binder**.

*Worked example:* [Part 5 — Farm Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Farming%20Kit%20-%20Building%20the%20Sample.md#part-5--farm-systems) and [Part 6 — The farm (`Farm_Game`)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Farming%20Kit%20-%20Building%20the%20Sample.md#part-6--the-farm-farm_game).

### 6. Your menu and Scene List

Copy `Farm_Menu` into `_Game/Scenes`, make Play load your farm, and change the title. In the Scene List: menu, then your farm.

*Worked example:* [Part 7 — Menu](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Farming%20Kit%20-%20Building%20the%20Sample.md#part-7--menu).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Tilling, planting and watering work on your field, and use energy.
- [ ] Sleeping ends the day; watered crops grow; the morning report shows.
- [ ] A crop can be harvested and sold in the shop, and seeds bought.
- [ ] Reaching your goal wins; the last day ending without it loses.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every crop and every feature exists and works. Art and balance can still be rough.

### All your crops and tools

Add every crop, seed and tool in your table. Each crop should be best at something: quick, regrowing, or valuable.

### Your days and numbers

Play a whole game. Write down money at the end of each day. A good plan should reach the goal with a few days to spare; planting only the cheapest crop shouldn't.

### Every screen

**How to Play.** Under your title on the menu, write one line saying what the game is, such as *Play cards to deal damage, block and heal against ever stronger enemies.* Then add a How to Play screen: copy Core's `HowToPlay` UXML into `_Game`, write your goal, controls and rules in a few short lines, and show it from a **How to Play** button on the menu. Players shouldn't have to work out the rules by trial and error.

Menu, pause, the shop, the morning report, won and lost and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every crop, tool and shop item in your table is in.
- [ ] A good plan reaches the goal; doing nothing doesn't.
- [ ] The clock, sleep, energy and the morning report all work over a whole game.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] The menu says what the game is, and How to Play explains the goal, controls and rules.
- [ ] Every screen works: menu, pause, the shop, the morning report, won and lost, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your art. Each crop's stages and each seed should be easy to tell apart in the hotbar and on the field.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: each Farmer Tools 2D event (**On Till**, **On Water**, **On Plant**, **On Harvest**, **On Nothing**), the Day Cycle's **On Day Ended**, and buying and selling. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch which crops they never plant, and how much money they end with. Adjust prices, growing days and energy, one at a time. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Every tool use, harvest and sale has a sound.
- [ ] Every crop gets planted by playtesters; any that doesn't is changed or cut.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| Using a tool | **Farmer Tools 2D** → On Till, On Water, On Plant, On Harvest, On Clear |
| A day ending | **Day Cycle** → On Day Ended |
| Time running out | **Day Cycle** → On Time Up |
| Money changing | The money variable (its Changed event) |

| To make the kit do something… | Call |
|---|---|
| End the day | **Day Cycle → Sleep** |
| Give items | **Inventory → Add** |
| Show a message | **FarmMessage.Say** (from a script) |
| Open the shop | **UI Shop → Open** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
