---
title: "Dialogue with Yarn Spinner"
course: GAME 1303
week: 8
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Dialogue with Yarn Spinner

**Week 8 · [[Lecture] Week 8](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2008%20-%20Lecture.md)**

> [!abstract] In one sentence
> Yarn Spinner lets dialogue be written as a plain script with choices, which the game plays line by line.

## What this topic is for

Students making visual novels and dating sims rely on this. Everyone else should see it once, because a few lines of dialogue can tell a small game's story more cheaply than a cutscene.

## Key ideas

- **Dialogue is written in Yarn scripts:** lines of text, the speaker's name, and choices, grouped into **nodes**.
- **Choices jump to other nodes.** That's how branching works.
- **Variables remember choices,** such as whether the player was kind, and later lines can check them. Dating sims use this for relationship scores.
- **Commands** in the script can tell the game to do things: change the background, show a character, play a sound.
- **Every branch costs work.** Each one must be written, illustrated and tested. Keep branches few and endings small.

> [!note] Course scripts
> Yarn Spinner is the course's supported dialogue tool. The visual novel kit connects it to course UI screens and characters.

## In class

1. Write a three-node conversation with one choice, live.
2. Count the branches in a student's planned story, then the screens and lines they imply.

## Where it comes up

- [Genre Map](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Genre%20Map.md): visual novel and dating sim.
- [Ten-Pager](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Assignments/Ten-Pager.md), page 9.

## Further resources

- Yarn Spinner documentation, [Yarn Spinner for Unity](https://docs.yarnspinner.dev/yarn-spinner-for-unity/overview).
