---
title: "Game Feel"
course: GAME 1303
week: 4
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Game Feel

**Week 4 · [[Lecture] Week 4](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2004%20-%20Lecture.md)**

> [!abstract] In one sentence
> Game feel is what the controls feel like in the player's hands, and it comes from a handful of numbers that are tuned, not guessed.

## What this topic is for

Students learn that "it feels bad" has causes that can be found and changed. By the end of Ex 03 they should have changed several movement settings on purpose and be able to name the feel they were after.

## Key ideas

- **Feel has a vocabulary.** Heavy, floaty, sharp, slippery, responsive, sluggish. Naming the feel is the first step to tuning it.
- **The numbers behind it:**

| Setting | Feel |
|---|---|
| Max Speed | Fast or slow |
| Acceleration and Deceleration | Sharp, or heavy and slippery |
| Air Control | Committed jumps, or steerable ones |
| Jump Height | Measured in units, so levels can be planned around it |
| Gravity Scale | Floaty or snappy jumps |
| Fall Gravity Multiplier | Falling faster than rising, which most platformers do |

- **Change one thing at a time.** Two changes at once make it impossible to tell which one helped.
- **Tune during Play, then keep the values.** Changes made in Play mode are lost. Copy the component during Play and paste its values after stopping.
- **Jump height and level design go together.** A three-unit jump clears a two-unit wall. The level is built around the jump, so the jump is tuned first.

## In class

1. Change each setting live in front of the class and have students name the result.
2. Hand the controller to a student, change a value without saying which, and ask them to describe what changed.

## Where it comes up

- [Ex 03 — Player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex03%20-%20Player.md), Part 5.
- [Forgiving Controls](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Forgiving%20Controls.md): the settings that forgive mistakes.
- The sprint review in Week 11: "a tuning pass."

## Further resources

- Steve Swink, *Game Feel: A Game Designer's Guide to Virtual Sensation* (2008).
