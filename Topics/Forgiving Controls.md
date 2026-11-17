---
title: "Forgiving Controls"
course: GAME 1303
week: 4
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Forgiving Controls

**Week 4 · [[Lecture] Week 4](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2004%20-%20Lecture.md)**

> [!abstract] In one sentence
> Players press buttons a little early and a little late, and coyote time, jump buffering and short hops quietly forgive that so the game feels fair.

## What this topic is for

These three settings are invisible when they work and obvious when they don't. Students should feel the difference by switching each one off, and understand that difficulty should come from the level, not from the controls.

## Key ideas

- **Coyote time.** For a moment after walking off a ledge, the player can still jump. Without it, players feel the game ignored a press they made in time.
- **Jump buffering.** A jump pressed just before landing is remembered and happens on landing. Without it, quick repeated jumps fail at random.
- **Short hops.** Letting go of Jump early cuts the jump short, so a tap gives a small hop and a hold gives a full jump. It gives the player control over height with one button.
- **Unfair is different from hard.** A hard game asks for skill. An unforgiving control scheme punishes the player for timing the game can't see.

| Setting on Platformer Controller 2D | Default | Off |
|---|---|---|
| Coyote Time | `0.1` | `0` |
| Jump Buffer Time | `0.1` | `0` |
| Short Hop Speed Kept | `0.5` | `1` |

## In class

1. Switch each setting off in front of the class and have a student play the same section.
2. Ask the student to describe what went wrong. They usually blame themselves, which is the point.

## Where it comes up

- [Ex 03 — Player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex03%20-%20Player.md), "Three tricks that make jumping feel fair."
- [Game Feel](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Game%20Feel.md).
