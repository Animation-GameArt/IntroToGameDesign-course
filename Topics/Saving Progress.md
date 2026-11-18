---
title: "Saving Progress"
course: GAME 1303
week: 9
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Saving Progress

**Week 9 · [[Lecture] Week 9](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2009%20-%20Lecture.md)**

> [!abstract] In one sentence
> Saving is a design question first: decide what the player would be upset to lose, then save only that, at predictable moments.

## What this topic is for

Students add saving to their game in Ex 08. Most small games need very little, and the lecture should make students comfortable choosing the smallest system that works.

## Key ideas

- **What would hurt to lose?** Levels unlocked, a high score, collected items, settings. Many small games only need a high score and settings, and that's a fine answer.
- **When to save.** At checkpoints, at the end of a level, and when settings change. Predictable saving is safer than saving all the time.
- **Session state isn't saved state.** Variable assets keep values between scenes, but not after the game is closed. Saving writes chosen values to a file.
- **Loading.** On start, read the file if it exists; if it doesn't, start fresh.
- **A way to reset.** Testers and players both need a "new game" that clears saved progress.

> [!note] Course scripts
> **Variable Saver** saves and loads chosen variable assets; **High Score** keeps the best score. Both store their data on the player's computer and work in Web builds. See the [Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md).

## In class

1. Ask what each student's game would need to save. Most lists are short.
2. Show a save file on disk, and delete it to show a fresh start.

## Where it comes up

- [Ex 08 — Save & Build](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex08%20-%20Save%20%26%20Build.md).
- [Settings Players Expect](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Settings%20Players%20Expect.md).
