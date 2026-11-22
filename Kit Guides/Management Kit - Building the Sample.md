---
title: "Management Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.18.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Management Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Management Kit**, not this page.

Everything goes in `Assets/_Course/Kits/Management/Sample/`, with folders `Data`, `Rules`, `Buildings`, `Events` and `Scenes`. The art is Kenney's **Tiny Town**, already in the project (`kenney_tiny-town`); pick a tile for each building's icon.

## Before you start

1. Pull the template project. It should be version 0.18.0 or later, with no red errors in the Console.
2. Every UI Document uses `CoursePanelSettings`.

## Part 1 — Resources and events

In `Sample/Data`:

| Asset | Type | Initial value |
|---|---|---|
| `People` | Int Variable | `12` |
| `Food` | Int Variable | `40` |
| `Gold` | Int Variable | `60` |
| `Wood` | Int Variable | `10` |
| `Year` | Int Variable | `1` |
| `Report` | String Variable | |
| `VillageWon`, `VillageLost` | Void Event Channel | |

## Part 2 — Turn Rules

In `Sample/Rules` (**Create → Collin Game → Management Kit → Turn Rule**), one effect each:

| Rule | Resource | Amount | Times Each | Divide By | Random Extra | Only When |
|---|---|---|---|---|---|---|
| `Eating` | Food | `-1` | People | `1` | `0` | Always |
| `Hunger` | People | `-3` | — | `1` | `1` | Food At Most `0` |
| `Taxes` | Gold | `1` | People | `3` | `0` | Always |
| `Growth` | People | `1` | — | `1` | `0` | Food At Least `30` |

## Part 3 — Buildings

In `Sample/Buildings` (**Create → Collin Game → Management Kit → Building**):

| Building | Icon (Tiny Town) | Cost | Every Turn | Description |
|---|---|---|---|---|
| `Farm` | a field or wheat tile | Gold `-20` | Food `6` | +6 Food each year |
| `Lumber Camp` | a tree or log tile | Gold `-15` | Wood `4` | +4 Wood each year |
| `House` | a house tile | Wood `-12` | People `1` | +1 Person each year |
| `Market` | a stall or shop tile | Gold `-30`, Wood `-10` | Gold `6` | +6 Gold each year |

## Part 4 — Events

In `Sample/Events` (**Create → Collin Game → Management Kit → Event**):

| Event | Text | Weight | Earliest | Effects or choices |
|---|---|---|---|---|
| `Rats` (title *Rats in the Granary*) | Rats got into the grain store. | `1` | `1` | Food `-10` |
| `Good Harvest` | The weather was kind this year. | `1` | `1` | Food `15` |
| `Storm` | A storm blew down a woodpile. | `1` | `1` | Wood `-5` |
| `Plague` | Sickness spread through the village. | `0.5` | `4`, Only Once | People `-3` |
| `Merchant` (title *A Merchant Arrives*) | A merchant offers to trade. | `1.5` | `2` | Choices: **Buy grain** (Gold `-15`, Food `20`); **Sell wood** (Wood `-8`, Gold `12`); **Send him away** (nothing) |
| `Festival` | The people ask for a harvest festival. | `1` | `3` | Choices: **Hold the festival** (Gold `-10`, People `2`); **Not this year** (nothing; result *The people grumble.*) |

## Part 5 — Village Systems

An empty `Village Systems`, made into a prefab, with these children:

**`Turn Cycle`** — **Turn Cycle**: Turn Number `Year`, Turns To Win `10`, Seconds Per Turn `0`; Rules `Eating`, `Hunger`, `Taxes`, `Growth` in that order; Resources `People`, `Food`, `Gold`, `Wood`; No Negative Resources ticked; Events: all six; Event Chance `0.5`; Report `Report`; Raise On Win `VillageWon`.

**`Lose`** — **Int Variable Condition**: Variable `People`, At Most `0`, Raise Event `VillageLost`. And a **Void Event Listener** on `VillageLost` → `Turn Cycle`, **TurnCycle → StopGame**.

**`Screen`** — UI Document `ManagementHUD` (from `Kits/Management/UI`), with:
- **UI Management Screen** (Turn Cycle `Turn Cycle`).
- **UI Build Grid**: Buildings `Farm`, `Lumber Camp`, `House`, `Market`; Plots `12`; Plots Per Row `4`; Starting Buildings empty; Watch Resources `People`, `Food`, `Gold`, `Wood`.
- **UI Variable Binder**: `turn-label` → `Year` → `Year {0}`; `resource-1-label` → `People` → `People: {0}`; `resource-2-label` → `Food` → `Food: {0}`; `resource-3-label` → `Gold` → `Gold: {0}`; `resource-4-label` → `Wood` → `Wood: {0}`.

**`Reset`** — a **Variable Resetter** with the four resources and `Year`.

**`Pause Menu`**, **`Settings`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Won`** — UI Document `EndScreen`, hidden, shown on `VillageWon`; `score-label` → `People` → `Your village has {0} people`.

**`Lost`** — UI Document `GameOver`, hidden, shown on `VillageLost`; Try Again → **ReloadScene**.

## Part 6 — Scenes

**`Village_Game`**: a new 2D scene with a camera (any background; the screen covers it) and `Village Systems`.

**`Village_Menu`**: like the Platformer sample's menu, with Play loading `Village_Game`.

Scene List: `Village_Menu`, `Village_Game`.

## Part 7 — Test

- [ ] The screen shows Year 1, the four resources, twelve empty plots and four cards.
- [ ] Cards you can't afford are faded and can't be dragged.
- [ ] Dragging a card shows a ghost; the plot under it is outlined; dropping builds it and pays the cost.
- [ ] Dragging a building from a plot onto the cards removes it; onto an empty plot moves it.
- [ ] End Turn applies the rules and buildings, and the report lists every resource's change.
- [ ] About every other turn an event happens; the Merchant and Festival show the event panel with buttons, and End Turn waits until one is chosen.
- [ ] Running out of food makes people leave; at 0 people the lost screen shows and End Turn stops.
- [ ] Surviving ten years shows the won screen.
- [ ] Doing nothing loses around year 6; building farms early wins.
- [ ] Esc pauses; nothing can be dragged while paused.

Note anything that fails, with the Console message.

## Part 8 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/Management` and the Tiny Town art folder with **Assets → Export Package**, unticking Core scripts that Unity adds as dependencies.
