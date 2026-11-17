---
title: "Spawners and Pooling"
course: GAME 1303
week: 6
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Spawners and Pooling

**Week 6 · [[Lecture] Week 6](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2006%20-%20Lecture.md)**

> [!abstract] In one sentence
> A spawner creates objects over time from a prefab, pooling reuses them instead of creating and destroying them, and the spawner's timing is a difficulty curve.

## What this topic is for

Students build their first spawner and learn the design layer on top of it: how many, how often and what kind is a schedule that shapes difficulty over time.

## Key ideas

- **Spawners make copies of a prefab** at one or more spawn points, on a timer.
- **Limits keep it under control.** A maximum number at once, and optionally a total.
- **Pooling.** Creating and destroying objects is slow when it happens often. A pool switches finished objects off and switches them back on for the next spawn. The course's Spawner pools automatically: objects that are switched off by Health, Lifetime or Damage On Touch are reused.
- **Lifetime.** Objects that might never be destroyed, such as a rock that misses, need a Lifetime so they're switched off after a few seconds.
- **Difficulty is a curve.** Draw it before touching settings: a ramp, a plateau, a spike, a rest. The spawner's interval and maximum are how the curve is built.

## In the course project

| Setting on Spawner | Controls |
|---|---|
| Prefab | What is made |
| Spawn Points | Where, chosen at random |
| Interval, Start Delay | How often, and when it begins |
| Max At Once, Total To Spawn | How many |

## In class

1. Draw a difficulty curve on the board for a two-minute section.
2. Set a spawner to match the first part of it, then change Interval live.
3. Set Max At Once to `0` (no limit) with a short interval, and open the Profiler (Week 10 preview) to show why limits matter.

## Where it comes up

- [Ex 05 — Combat](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat.md), Part 5: falling rocks.
- Tower defense, shooter and runner kits use spawners for waves and obstacles.

## Further resources

- Robert Nystrom, *Game Programming Patterns*, [Object Pool](https://gameprogrammingpatterns.com/object-pool.html).
- Unity Manual, [Reusable code](https://docs.unity.com/en-us/engine/6000.3/manual/analysis/performance-memory/managed-memory/optimizing-code-managed-memory/reusable-code), including Unity's built-in object pool.
