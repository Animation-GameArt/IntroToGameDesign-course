---
title: "Cameras with Cinemachine"
course: GAME 1303
week: 5
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Cameras with Cinemachine

**Week 5 · [[Lecture] Week 5](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2005%20-%20Lecture.md)**

> [!abstract] In one sentence
> Once a level is wider than the screen, the camera becomes part of the design, and Cinemachine lets students set its behavior with a few settings instead of code.

## What this topic is for

Students should be able to add a following camera, keep it inside the level, and change how closely it follows. They should also understand that what the camera shows decides what is fair.

## Key ideas

- **A Cinemachine camera directs the Main Camera.** The Main Camera does the drawing; the Cinemachine camera decides where it points.
- **Tracking Target.** The object the camera follows, usually the player.
- **Orthographic Size.** Half the height of the view, in units. Size `5` shows ten units top to bottom.
- **Position Composer settings:**

| Setting | Effect |
|---|---|
| Damping | How quickly the camera catches up. Higher is smoother but lags |
| Dead Zone | An area the player can move in without the camera moving |
| Lookahead | Shifts the view ahead of the player's movement |

- **Bounds.** A Cinemachine Confiner 2D keeps the camera inside a shape, usually a trigger Box Collider 2D around the level, so it never shows empty space past the edges.
- **The camera decides fairness.** A hazard the player couldn't see in time isn't a challenge. Lookahead and a wider view help fast games.

## In class

1. Add a 2D Cinemachine camera following the player.
2. Change Damping and Dead Zone live and have the class describe each.
3. Add bounds and show the empty space disappear.

## Common problems

| What happens | Why |
|---|---|
| The camera doesn't move | Tracking Target is empty |
| The camera sticks or jumps at edges | The bounds shape is smaller than the view |
| The player stops jumping after bounds were added | The bounds collider isn't a trigger, so the player is standing inside it |

## Where it comes up

- [Ex 04 — Level](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md), Parts 6 and 9.
- [Platformer Kit sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md), Part 5.
- 3D games in Week 8 use a different Cinemachine setup.

## Further resources

- Cinemachine manual, [Cinemachine and 2D graphics](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/Cinemachine2D.html).
- Cinemachine manual, [Position Composer](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachinePositionComposer.html).
- Cinemachine manual, [Cinemachine Confiner 2D](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineConfiner2D.html).
