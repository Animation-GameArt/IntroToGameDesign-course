---
title: "Four Kinds of UI"
course: GAME 1303
week: 7
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Four Kinds of UI

**Week 7 · [[Lecture] Week 7](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2007%20-%20Lecture.md)**

> [!abstract] In one sentence
> Game UI can sit on the screen, live in the world, float in the world, or change the screen itself, and choosing the right kind is a design decision.

## What this topic is for

Students get a vocabulary for UI choices and sort their own layout sketches with it. Some will move a HUD element into the world; most will simply be able to explain why theirs is on screen.

## Key ideas

| Kind | Part of the world? | Characters aware of it? | Examples | Built with |
|---|---|---|---|---|
| **Screen** (non-diegetic) | No | No | Menus, HUD | UI Toolkit, screen space |
| **Diegetic** | Yes | Yes | A computer terminal, a health bar on a suit | UI Toolkit in world space, or sprites |
| **Spatial** | Placed in it | No | A name above a character, damage numbers, a waypoint arrow | TextMeshPro text in the world |
| **Meta** | No | No, but it shows the character's state | A red flash when hurt, a blurred screen when dizzy | Screen effects |

- **Screen UI is the default** and the easiest to read.
- **Diegetic UI adds immersion** but must still be readable at a glance.
- **Spatial UI puts information where the player is already looking.** The course's Health Popups are spatial.
- **Meta UI is felt more than read.** Use it for states, not numbers.

## In class

1. Show one example of each from well-known games.
2. Have students label each element in their own screen layout with its kind.

## Where it comes up

- [Ex 06 — UI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md): the HUD (screen) and damage numbers (spatial).
- [Screen Layout](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Assignments/Screen%20Layout.md): the HUD note asks which elements are on screen and which are in the world.
- [Ten-Pager](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Assignments/Ten-Pager.md), page 6.
