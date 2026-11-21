---
title: "Management Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Management Kit — Build Your Game

This guide takes you from your ten-pager to your own finished management game, built with the Management Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Management Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Management%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Village_Game` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **Resources:** three or four, with starting values | | People 12, Food 40, Gold 60, Wood 10 |
| **Rules:** what happens every turn, in order | | Eating, Hunger, Taxes, Growth |
| **Buildings:** each one's cost and every-turn effect | | Farm, Lumber Camp, House, Market |
| **Events:** what can happen, and the choices | | Rats, Good Harvest, Storm, Plague; Merchant and Festival with choices |
| **Turns:** button or timer, and how many to win | | End Turn button; survive 10 years |
| **Losing:** what ends the game | | No people left |
| **Theme and look:** setting, art, colors | | A medieval village, Kenney's Tiny Town |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. Three or four resources, four buildings, a handful of rules and eight events is a complete management game in eight weeks. Play it on paper first.

## Stage 1 — First Playable

The goal: your resources, rules and two buildings working through a full game, from the menu to winning or losing.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your resources

Create an **Int Variable** for each resource in `_Game/Data`, with its starting value, plus a `Year` (or `Turn`) variable, a `Report` String Variable, and win and lose Void Event Channels.

*Worked example:* [Part 1 — Resources and events](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Management%20Kit%20-%20Building%20the%20Sample.md#part-1--resources-and-events).

### 3. Your rules

Create a **Turn Rule** for each rule in your table (**Create → Collin Game → Management Kit → Turn Rule**), with its effects. Order matters: a rule that checks for hunger runs after the rule that eats.

*Worked example:* [Part 2 — Turn Rules](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Management%20Kit%20-%20Building%20the%20Sample.md#part-2--turn-rules).

### 4. Your first buildings

Create two **Buildings** from your table, with **Cost** and **Every Turn** effects, an icon and a description.

*Worked example:* [Part 3 — Buildings](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Management%20Kit%20-%20Building%20the%20Sample.md#part-3--buildings).

### 5. Your game scene

1. Open `Village_Game`, **File → Save As…** into `_Game/Scenes`.
2. On the **Turn Cycle**: your rules in order, your resources, Turns To Win, your win event. On **UI Build Grid**: your buildings, and your resources in **Watch Resources**. On the **UI Variable Binder**: your resources on the four resource labels.
3. Set the lose **Int Variable Condition** to your losing resource.
4. Play ten turns. Change one number and play again.

*Worked example:* [Part 5 — Village Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Management%20Kit%20-%20Building%20the%20Sample.md#part-5--village-systems) and [Part 6 — Scenes](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Management%20Kit%20-%20Building%20the%20Sample.md#part-6--scenes).

### 6. Your menu and Scene List

Copy `Village_Menu` into `_Game/Scenes`, make Play load your game, and change the title. In the Scene List: menu, then your game.

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your resources show on the HUD and change each turn by your rules.
- [ ] Two buildings can be built (and removed), and pay off each turn.
- [ ] The report shows what changed.
- [ ] The game can be won by lasting, and lost.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every part of your economy and every feature exists and works. Art and balance can still be rough.

### All your buildings and events

Add every building and event in your table (**Create → Collin Game → Management Kit → Event**). Events with choices need two or three **Choices**, each with its own effects and a result line.

### Your numbers

Play on paper, or in a spreadsheet, a turn per row. A good strategy should win most of the time; doing nothing should usually lose.

### Every screen

Menu, pause, won and lost and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every resource, rule, building and event in your table is in.
- [ ] A good strategy wins, and doing nothing loses.
- [ ] Every event's text explains what it did.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, won and lost, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your art: building icons, and a background for the screen. Make the resource numbers the easiest thing to read.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: the Turn Cycle's **On Turn Ended**, building (a sound per card dropped), event panels appearing, and winning and losing. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch which buildings they never build, and when they lose. Every choice should cost something. Change one number at a time, and replay the same strategy to compare. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Ending a turn, building and events each have a sound.
- [ ] Every building gets built by playtesters; any that doesn't is changed or cut.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A turn ending | **Turn Cycle** → On Turn Ended |
| Winning | **Turn Cycle** → On Won, or its win event |
| A resource changing | The resource variable (its Changed event) |

| To make the kit do something… | Call |
|---|---|
| End the turn | **Turn Cycle → EndTurn** |
| Answer an event | **Turn Cycle → Choose** |
| Add a building from code | **Turn Cycle → AddBuilding** |
| Stop the game | **Turn Cycle → StopGame** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
