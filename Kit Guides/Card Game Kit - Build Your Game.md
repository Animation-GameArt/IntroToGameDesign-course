---
title: "Card Game Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Card Game Kit — Build Your Game

This guide takes you from your ten-pager to your own finished card battle game, built with the Card Game Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Card Game Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Card%20Game%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Cards_Game` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **Cards:** each one's name, cost and effects, and copies in the deck | | 15 playing cards: spades attack, diamonds block, hearts heal, clubs draw |
| **The player:** health, energy per turn, hand size | | 40 health, 3 energy, 5 cards |
| **Enemies:** each one's health and moves, in order | | Slime (28), Knight (42), Demon (62) |
| **Battles:** how many, and healing between | | 3; heal 10 between |
| **Card look:** your own pictures, or the blank card with names | | Kenney's playing cards |
| **Goal:** how the run ends | | Beat all three |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. Twelve to fifteen cards, one fixed deck and three enemies is a complete card game in eight weeks. Play it with paper cards first.

## Stage 1 — First Playable

The goal: a battle against your first enemy with your first cards, from the menu to winning or losing.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data

Create a `PlayerHealth` Int Variable and win and lose Void Event Channels in `_Game/Data`.

*Worked example:* [Part 1 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Card%20Game%20Kit%20-%20Building%20the%20Sample.md#part-1--data).

### 3. Your first cards

Create five cards from your table (**Create → Collin Game → Card Game Kit → Card**): **Cost** and **Effects**. Leave **Face** empty for now: the blank card with the name is quickest while you design.

*Worked example:* [Part 2 — Cards](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Card%20Game%20Kit%20-%20Building%20the%20Sample.md#part-2--cards).

### 4. Your first enemy

Create one **Enemy** (**Create → Collin Game → Card Game Kit → Enemy**): health, a portrait, and its **Moves** in order.

*Worked example:* [Part 3 — Enemies](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Card%20Game%20Kit%20-%20Building%20the%20Sample.md#part-3--enemies).

### 5. Your battle scene

1. Open `Cards_Game`, **File → Save As…** into `_Game/Scenes`.
2. On **Card Battle**: your cards in **Deck** (twice for two copies), your enemy, the player's health, energy and hand size, your win and lose events.
3. Play several battles. Can you always win? Can you always lose by playing badly?

*Worked example:* [Part 4 — Card Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Card%20Game%20Kit%20-%20Building%20the%20Sample.md#part-4--card-systems) and [Part 5 — Scenes](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Card%20Game%20Kit%20-%20Building%20the%20Sample.md#part-5--scenes).

### 6. Your menu and Scene List

Copy `Cards_Menu` into `_Game/Scenes`, make Play load your game, and change the title. In the Scene List: menu, then your game.

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your cards can be played; energy, block and damage work as your table says.
- [ ] Your first enemy shows its next move and makes it.
- [ ] The battle can be won and lost, and both screens appear.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every card and enemy and every feature exists and works. Art and balance can still be rough.

### All your cards and enemies

Add every card and enemy in your table. Each enemy should need a different plan: block big hits, race a healer, outlast a swarm of small hits.

### Your numbers

Play a run choosing carefully, and one choosing at random. The careful run should usually win; the random one usually lose.

### Every screen

Menu, pause, won and lost and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every card and enemy in your table is in, and the run can be won.
- [ ] Every card gets played in a normal run; any that doesn't is changed or cut.
- [ ] Careful play usually wins; random play usually loses.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, won and lost, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your card art (each card's **Face**) and enemy portraits. Cards must be readable at the size they're drawn in the hand.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: the Card Battle's **On Card Played**, **On Enemy Hit**, **On Player Hit**, **On Block** and **On Enemy Defeated**. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch which cards they always play first and which they never play. Cost is your main lever. Adjust one card at a time. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Playing, hitting, blocking and defeating each have a sound.
- [ ] Every card has its final art.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A card being played | **Card Battle** → On Card Played |
| Hits and blocks | **Card Battle** → On Enemy Hit, On Player Hit, On Block |
| An enemy defeated | **Card Battle** → On Enemy Defeated |
| Anything on screen changing | **Card Battle**'s Changed event (from a script) |

| To make the kit do something… | Call |
|---|---|
| Play a card | **Card Battle → PlayCard** |
| End the turn | **Card Battle → EndTurn** |
| Show a screen | **UIScreen → Show** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
