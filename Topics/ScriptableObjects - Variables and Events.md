---
title: "ScriptableObjects: Variables and Events"
course: GAME 1303
week: 3
type: topic
status: draft
tags:
  - game1303
  - topic
---

# ScriptableObjects: Variables and Events

**Week 3 · [[Lecture] Week 3](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2003%20-%20Lecture.md)**

> [!abstract] In one sentence
> A ScriptableObject is data saved as a file, and the course uses two kinds, variables and event channels, so objects can share information without knowing about each other.

## What this topic is for

This is the course's main architecture. Once students understand it, the HUD, pickups, doors, lives, game over and win screens all work the same way. They should leave able to explain why the key in Ex 02 doesn't need to know about the door.

## Key ideas

- **Data that lives outside the scene.** A ScriptableObject is an asset in the Project window, like a sprite or a sound. It keeps its value when scenes change.
- **Variables share a value.** An Int Variable named `Score` holds one number. A coin adds to it. A label shows it. Neither knows the other exists.
- **Event channels share a moment.** A Void Event Channel named `KeyCollected` is raised by the key. A door listens and hides itself. More listeners can be added without touching the key.
- **Direct references break; shared assets don't.** If the coin held a reference to the score text, deleting or renaming the text would break the coin. With a shared variable, any number of texts can come and go.
- **Variables reset when the game starts, not when a scene loads.** That's why the score carries between levels, and why a Variable Resetter exists for scenes that should start fresh.
- **Inspector helpers.** During Play, a variable shows its current value in the Inspector, and a Void Event Channel has a **Raise** button for testing.

## In class

1. Draw two diagrams: coin → text, with a direct link; and coin → `Score` ← text. Delete the text in each and ask what breaks.
2. In Play mode, click **Raise** on `KeyCollected` and watch the door open with no key collected.

## The course's assets

| Asset | Create menu | Typical use |
|---|---|---|
| Int, Float, Bool, String Variable | Create → Collin Game → Variables | Score, health, paused, a message |
| Void Event Channel | Create → Collin Game → Events | Key collected, level complete, game over |
| Int, Float, Bool, String, GameObject Event Channel | Create → Collin Game → Events | An event that carries a value |

## Where it comes up

- [Ex 02 — Events](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md): introduced.
- [Ex 04](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md): `LevelCompleted`.
- [Ex 06](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md): the HUD listens to the same variables.
- [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md): lives and game over.

## Further resources

- Unity Manual, [ScriptableObject data assets](https://docs.unity.com/en-us/engine/6000.3/manual/scripting/get-started/fundamental-unity-types/class-scriptable-object).
- Robert Nystrom, *Game Programming Patterns*, [Observer](https://gameprogrammingpatterns.com/observer.html): the pattern behind event channels, explained for game developers.
