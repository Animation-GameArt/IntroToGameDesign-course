---
title: "The Profiler"
course: GAME 1303
week: 10
type: topic
status: draft
tags:
  - game1303
  - topic
---

# The Profiler

**Week 10 · [[Lecture] Week 10](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2010%20-%20Lecture.md)**

> [!abstract] In one sentence
> When a game stutters, the Profiler shows how long each frame took and where the time went, so you can stop guessing.

## What this topic is for

Students take one Profiler reading of their own game in Ex 09. At this level the skill is narrow: find a spike, find what caused it, change one thing, measure again.

## Key ideas

- **Frames.** A smooth game draws about 60 frames a second, so each frame has roughly 16 milliseconds.
- **The Profiler** (**Window → Analysis → Profiler**) records frames while the game plays, as a graph.
- **Spikes** are frames that took much longer than the rest. They're what the player feels as a stutter.
- **Select a spike** to see which scripts and systems used the time.
- **Common causes in student games:** spawning without limits, creating and destroying many objects, very large images, and too many lights.
- **Measure before and after** a change, so the fix is proven.

## In class

1. Set a Spawner to no limit and a short interval. Record, find the spike, and select it.
2. Restore the limit and record again.

## Where it comes up

- [Ex 09 — Debug & Profile](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex09%20-%20Debug%20%26%20Profile.md).
- [Spawners and Pooling](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Spawners%20and%20Pooling.md).

## Further resources

- Unity Manual, [Profiler window](https://docs.unity.com/en-us/engine/6000.3/manual/analysis/profiler/window).
