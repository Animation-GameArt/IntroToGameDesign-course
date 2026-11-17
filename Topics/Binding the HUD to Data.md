---
title: "Binding the HUD to Data"
course: GAME 1303
week: 7
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Binding the HUD to Data

**Week 7 · [[Lecture] Week 7](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2007%20-%20Lecture.md)**

> [!abstract] In one sentence
> The HUD listens to the same variable assets the game changes, so it is always correct and never needs to know the player exists.

## What this topic is for

This closes the loop started in Week 3. Students see that the `Score` variable a coin changed in Ex 02 is the same one the HUD shows in Ex 06, and why that design survives the player being respawned, levels changing and objects being deleted.

## Key ideas

- **Listen, don't ask.** The UI Variable Binder is told when a variable changes. It doesn't check every frame.
- **The HUD knows values, not objects.** It shows `PlayerHealth` and `Score`. It has no reference to the player or the coins.
- **The alternative breaks.** A HUD that reaches into the player object every frame breaks when the player is respawned, renamed or replaced.
- **One value, many views.** The same `Score` can appear on the HUD, the win screen and a world-space label at once.

## In the course project

| Component | Shows variables in |
|---|---|
| UI Variable Binder | A UI Document's labels (screen UI) |
| Variable Label | A TextMeshPro text in the world |

Both use a **Format** such as `Score: {0}`.

## In class

1. Show a HUD that reads the player directly, then delete and respawn the player. Watch it fail.
2. Replace it with the UI Variable Binder and repeat.

## Where it comes up

- [Ex 06 — UI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md), Part 2.
- [ScriptableObjects: Variables and Events](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/ScriptableObjects%20-%20Variables%20and%20Events.md).
- [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md): health, lives and coins.
