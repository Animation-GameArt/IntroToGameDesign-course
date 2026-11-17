---
title: "Menus, Pause and Usability"
course: GAME 1303
week: 7
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Menus, Pause and Usability

**Week 7 · [[Lecture] Week 7](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2007%20-%20Lecture.md)**

> [!abstract] In one sentence
> Every game needs the same few screens, pausing is a game state the rest of the game respects, and usable UI is readable, escapable and works with a gamepad.

## What this topic is for

Students build the screen flow every finished game has, and learn the basic usability checks that decide whether a game feels finished.

## Key ideas

- **The screen flow:** title → play → pause → win or lose → back to the title. Every screen except the HUD has a way out.
- **Pause is a state.** Time stops, the player's controls switch off, and the pause menu appears. The Pause button keeps working so the game can be un-paused.
- **Win and lose screens listen for events.** The goal raises `LevelCompleted`; the screen shows itself. The goal never knows about the screen.
- **Gamepad navigation.** A menu needs a selected button when it appears, or a gamepad can't use it. Set **Select When Shown** on its UI Screen.
- **Readable text.** Large enough to read from a normal distance, with strong contrast against what's behind it.
- **Less is more on the HUD.** Show what the player needs every moment. Everything else goes in a menu or nowhere.
- **Credits.** Every finished game has a credits screen. The course's version reads text files, so it's easy to keep current.

## In the course project

| Component | Role |
|---|---|
| UI Screen | Shows and hides a screen; selects the first button |
| UI Button Events | Connects buttons to actions |
| Pause Controller | The pause state |
| UI Credits | Fills the credits screen |

## In class

1. Walk the screen flow of a finished game, counting screens.
2. Try a student's menu with a gamepad only.

## Where it comes up

- [Ex 06 — UI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md), Parts 3 to 5.
- [The Polish Checklist](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/The%20Polish%20Checklist.md) (Week 14).
- [Credits and Licenses](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Credits%20and%20Licenses.md).
