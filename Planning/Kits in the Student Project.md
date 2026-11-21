---
title: "Kits in the Student Project"
course: GAME 1303
status: draft
audience: instructor
tags:
  - game1303
  - instructor
  - planning
---

# Kits in the Student Project

**For instructors.** How the genre kits fit into a student's project, from pitch to Gold, and why each kit has three guides.

## The three guides for each kit

| Guide | Who it's for | What it does | When students use it |
|---|---|---|---|
| **[Kit name] Kit** | Students | Says what the kit does and doesn't do, how to install it, how the sample works, recipes and fixes | At the pitch, to check their idea fits; any time after, as a reference |
| **[Kit name] Kit — Build Your Game** | Students | Turns their design decisions into their own game, step by step, with checks for each milestone | Weeks 8 to 15 |
| **[Kit name] Kit — Building the Sample** | Instructors | Builds the kit's sample once, in the template project, with exact values. It tests the kit, and the result ships with the kit | Before the semester; afterwards, as a worked example students can look at |

## Why students don't follow "Building the Sample"

- **It builds our game, not theirs.** Its values are exact ("Slime, 28 health") so the sample can be tested. A student following it spends hours making a copy of a game they can already import.
- **It works inside `Assets/_Course`,** which students are told never to edit, and includes instructor steps: pulling the template, committing the sample, exporting the package.
- **They don't need to rebuild the sample to learn from it.** It ships with the kit. Opening it, playing it and clicking through its Hierarchy shows how a finished game is wired.

It's still useful to students as a **worked example**: each Build Your Game step links to the matching part of Building the Sample, so a student who's stuck can see the same step done with real values.

## Why a student version

Students see a finished game in their genre first (the sample), then build **their own** game with the same parts, step by step. Each step asks for one of their decisions instead of a fixed number: "Create a Crop for each row of your crop table", not "Create Mushrooms, 2 days, $20". That gives them:

- **Direction.** They always know the next step, and which milestone it's for.
- **Scaffolding.** They build with parts that already work, in the order that gets a playable game soonest.
- **Ownership.** Every value, name, level and piece of art is theirs.

## The flow, week by week

| Week | Student work | Where the kit comes in |
|---|---|---|
| 1 | Three Game Ideas | The Genre Map lists the genres with kits |
| 3 | Pitch | The kit guide's **does / doesn't do** table: anything their pitch needs that the kit doesn't do becomes an agreed custom script, or is cut |
| 4 | One-Sheet | — |
| 6 | Ten-Pager Draft | Page 10 names the kit, and starts the **decisions table** from the kit's Build Your Game guide |
| 7 | Ten-Pager | The decisions table is complete, with the custom scripts agreed at the pitch |
| 8 | Production Backlog | The Build Your Game steps, with their decisions, become the first tasks on the board |
| 8–9 | Building | Install the kit, play the sample, then follow Build Your Game up to its First Playable checks |
| 10 | First Playable | The First Playable checks in their Build Your Game guide |
| 11–12 | Building, Alpha | The rest of the steps; the Alpha checks |
| 13–14 | Polish, Beta | The polish steps; the Beta checks |
| 15 | Gold | — |

Custom scripts (agreed at the pitch) go in `Assets/_Game/Scripts`. Each Build Your Game guide says where they usually connect: an event to listen to, a UnityEvent to call, or a variable to read.

## The decisions table

Each Build Your Game guide starts with a table of the decisions that kit needs: for the Platformer, the character's feel, the levels and what each teaches, the collectibles, the enemies and hazards, and the goal. Students fill it in on **page 10 of the ten-pager**, so there's no extra assignment, and it's graded with the ten-pager. In class it's a good thing to check during ten-pager feedback: an empty or vague row is a decision the student hasn't made yet.

## Milestone checks

The Build Your Game guide ends each stage with checks: First Playable, Alpha and Beta. The milestone assignments point to them, so "is the main mechanic working?" becomes a list that matches the student's own kit.

## Status

| Kit | Build Your Game guide |
|---|---|
| Platformer | Written (2026-11-21); the pattern for the others |
| The other fourteen | To write once the Platformer one is reviewed |
