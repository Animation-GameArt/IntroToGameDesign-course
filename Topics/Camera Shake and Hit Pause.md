---
title: "Camera Shake and Hit Pause"
course: GAME 1303
week: 8
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Camera Shake and Hit Pause

**Week 8 · [[Lecture] Week 8](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2008%20-%20Lecture.md)**

> [!abstract] In one sentence
> A brief camera shake and a few frozen frames on impact make hits feel heavy, as long as they're saved for moments that deserve them.

## What this topic is for

Students add one camera shake to their game in Ex 07, and learn to use it with restraint.

## Key ideas

- **Camera shake** moves the camera a little for a fraction of a second. Cinemachine does this with an **Impulse**: an Impulse Source sends a shake, and an Impulse Listener on the camera receives it.
- **Hit pause** freezes the game for a few frames on a strong impact. It gives the eye time to register the hit.
- **Strength and length.** Short and small for most hits. Larger only for the biggest moments.
- **Restraint.** Constant shaking hides what's happening and can make some players feel ill. Consider an option to turn it off.
- **Direction.** A shake in the direction of the hit reads better than a random one.

> [!note] Course scripts
> A course helper for triggering a shake from an event is planned for the Week 8 scripts. Until then, Cinemachine's own Impulse components can be used directly.

## In class

1. Add a shake to a hit in the course project. Then add it to every coin, and ask the class what happened.
2. Freeze three frames on a stomp and compare.

## Where it comes up

- Ex 07 — Juice & Audio.
- [Feedback and Juice](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Feedback%20and%20Juice.md).
- [Cameras with Cinemachine](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Cameras%20with%20Cinemachine.md).

## Further resources

- Cinemachine manual, [Cinemachine Impulse](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineImpulse.html).
- Jan Willem Nijman, "The Art of Screenshake" (INDIGO 2013).
