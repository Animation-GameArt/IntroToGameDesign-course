---
title: "GameObjects, Components and Prefabs"
course: GAME 1303
week: 3
type: topic
status: draft
tags:
  - game1303
  - topic
---

# GameObjects, Components and Prefabs

**Week 3 · [[Lecture] Week 3](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2003%20-%20Lecture.md)**

> [!abstract] In one sentence
> A GameObject is an empty container, components give it everything it does, and a prefab saves a finished GameObject as a reusable template.

## What this topic is for

This is the idea every later exercise depends on. Students should be able to look at any object in a scene and explain what each of its components contributes, and know when to make a prefab.

## Key ideas

- **A GameObject does nothing by itself.** It has a name, a position (its Transform) and a list of components.
- **Components add abilities:**

| Component | Gives the object |
|---|---|
| Sprite Renderer | Something to see |
| Collider 2D | A shape that can touch other shapes |
| Rigidbody 2D | Movement under physics: gravity, speed, collisions |
| A course script, such as Collectible | A behavior |

- **Composition.** Building objects by combining components is how nearly everything in the course works. A coin and a key are the same object with different settings on the same Collectible component.
- **Triggers and solid colliders.** A solid collider blocks. A collider with **Is Trigger** ticked notices touches but lets things pass through. A touch is only noticed if at least one of the two objects has a Rigidbody.
- **Prefabs.** Drag a finished GameObject into the Project window and it becomes a prefab. Copies placed in scenes stay linked to it, so changing the prefab changes them all.
- **Prefab variants.** A variant is a student's own version of a prefab that still follows the original. It's how students change kit prefabs without editing course files.

## In class

1. Build the ball from [Ex 02](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md) one component at a time, pressing Play after each: sprite, then collider, then Rigidbody.
2. Turn a coin into a prefab, place five, change the prefab's color, and watch all five change.

## Common problems

| What happens | Why |
|---|---|
| Objects pass through each other | One has no collider, or both colliders are triggers |
| A trigger never fires | Neither object has a Rigidbody 2D |
| Editing one copy didn't change the others | The edit was made on the copy, not the prefab |

## Where it comes up

- [Ex 02 — Events](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md): building from components.
- [Ex 05 — Combat](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat.md): the Rock prefab.
- [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md): prefab variants.

## Further resources

- Unity Manual, [Introduction to prefabs](https://docs.unity.com/en-us/engine/6000.3/manual/working-with-gameobjects/prefabs/introduction).
