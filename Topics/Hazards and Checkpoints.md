---
title: "Hazards and Checkpoints"
course: GAME 1303
week: 5
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Hazards and Checkpoints

**Week 5 · [[Lecture] Week 5](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2005%20-%20Lecture.md)**

> [!abstract] In one sentence
> A hazard gives a mistake a cost, a checkpoint decides how big that cost is, and placing both well is what makes a hard level fair.

## What this topic is for

Students learn that difficulty is two decisions: how hard a section is, and how much the player loses by failing it. They also see their first respawn system, which Week 6 extends with health.

## Key ideas

- **Hazards.** Pits, spikes, enemies. A hazard is only fair if the player can see it before it matters.
- **The cost of failing.** Losing a life, going back to a checkpoint, going back to the start. The bigger the cost, the more a section must be learnable.
- **Checkpoints after the hard part.** A checkpoint right after a hard section means failing the next one doesn't make the player replay it.
- **Checkpoints that are too frequent** remove tension. Too rare, and players replay easy parts to retry hard ones.
- **Events.** "The player died" and "checkpoint reached" are moments that other things react to: the camera, the HUD, a sound.

## In the course project

| Component | What it does |
|---|---|
| Respawner | On the player. Remembers where to come back to |
| Checkpoint | A trigger. Moves the player's respawn point here, and can change color |
| Kill Zone | A trigger or solid. Sends the player back at once, or takes all their health |
| Damage On Touch | Takes one point of health (Week 6) |

## In class

1. Play a section with a checkpoint at its end, then the same section with the checkpoint moved before it. Ask which felt fair.
2. Show a hazard that appears just off screen, then move the camera so it's visible in time.

## Where it comes up

- [Ex 04 — Level](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md): pit, spikes, checkpoint.
- [Ex 05 — Combat](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat.md): spikes that cost health instead.
- [Health and Damage](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Health%20and%20Damage.md).
