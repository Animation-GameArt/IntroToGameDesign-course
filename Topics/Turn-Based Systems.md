---
title: "Turn-Based Systems"
course: GAME 1303
week: 6
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Turn-Based Systems

**Week 6 · [[Lecture] Week 6](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2006%20-%20Lecture.md)**

> [!abstract] In one sentence
> Turn-based games swap reflexes for decisions, and they're only as interesting as the choices they offer on each turn.

## What this topic is for

Students making puzzle, tactics, strategy or card games take the turn-based version of Ex 05. Everyone should leave knowing how a turn manager works, and how to state a win and a lose condition for any game.

## Key ideas

- **A turn manager** keeps the order, tells each participant when their turn starts, and checks after every turn whether the battle is over.
- **A turn ends with an action.** The player chooses; the computer follows a rule.
- **Simple rules for opponents.** "Heal if health is low and a heal is left; otherwise attack" is enough to feel deliberate.
- **Interesting choices need costs.** If attacking is always best, there's no decision. Limited heals, defending, or a stronger attack that costs something create one.
- **Win and lose conditions.** Every game states both plainly. Here: the player wins when no opponents can act, and loses when nobody on their side can.
- **The same Health underneath.** Turn-based combat uses the same Health component as real-time, with invulnerable time at zero.

## In the course project

| Component | Role |
|---|---|
| Turn Manager | Turn order, rounds, win and lose |
| Turn Taker | Marks a participant, and which side it's on |
| Turn Actions | Attack and heal; controlled by the player or the computer |

## In class

1. Play the turn-based exercise with default numbers, and ask whether there's ever a reason to heal.
2. Change one number until there is.
3. Ask every student to write the win and lose conditions of their own game in one line each.

## Where it comes up

- [Ex 05 — Combat (Turn-Based)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat%20%28Turn-Based%29.md).
- The turn-based battle, card game, management and strategy kits.
- [Ten-Pager](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Assignments/Ten-Pager.md), page 2: win and lose conditions.
