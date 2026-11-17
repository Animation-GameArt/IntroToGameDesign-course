---
title: "[Lecture] Week 2"
course: GAME 1303
week: 2
status: draft
tags:
  - game1303
  - lecture-page
---

# Week 2 — Ex 01: Bootstrap · Project setup check

**Exercise:** Ex 01 — Bootstrap. Download the course project, set up a backup, and switch between two scenes with a fade.

**Also due:** the project setup check, done in person: the project opens, and the student can show how it's backed up. The pitch post is due by 11:59 PM the night before next class.

## Lecture topics, expanded

**How to pitch.** A pitch answers three questions fast: what does the player do, why is it fun, and why this game. Teach the **logline** (one sentence with the player, the action and the hook), the core loop from last week, and one or two comparable games. Students have about two minutes each on Pitch Day, presented from their Canvas post. Model one good pitch and one vague one, and let the class say what the vague one is missing.

**Scope.** Students have eight weeks of production, weeks 8 to 15, working alone. Give them concrete measures: one core mechanic, one level done well before a second is started, and a count of every sprite and sound the game needs. Introduce **must have** and **nice to have**, and the rule that a smaller finished game beats a bigger unfinished one. The supported genre list is a scope tool too: the scripts for those genres already exist.

**Task boards, milestones and backups.** Show a three-column board: To Do, Doing, Done. Name the milestones students will hit: First Playable, Alpha, Beta, Gold. Then cover backups, because the first lost project usually happens before midterm. Students choose Unity Version Control, with a check-in at the end of every session, or an SSD plus a weekly copy to a second device at home. Explain why a cloud-synced folder such as OneDrive is a poor place for a Unity project.

**The course project and the Bootstrapper.** Tour the folders: `_Course` belongs to the course and is never edited, `_Game` belongs to the student, and exercise scenes are saved as copies in `Scenes/Exercises`. Explain the **Scene List**: a scene can only be loaded during play if it's on that list. Then show the `[Course Services]` object in the Hierarchy during Play. The Bootstrapper creates it before any scene loads, so the Scene Loader is always there and Play works from any scene.

## Topic notes

Each topic has its own page with the lecture's intent, a demo plan, common problems and further resources.

- [How to Pitch](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/How%20to%20Pitch.md)
- [Scope](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Scope.md)
- [Task Boards and Milestones](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Task%20Boards%20and%20Milestones.md)
- [Backing Up Your Project](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Backing%20Up%20Your%20Project.md)
- [The Course Project](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/The%20Course%20Project.md)

## Connecting it forward

The two scenes from today become the starting point for Ex 02, through **Save As**, and that habit continues through Ex 06. The Scene Changer returns whenever a level needs to restart or a menu needs a button. On the design side, the pitch post due before next class is the first document in a chain: pitch, one-sheet, screen layout, ten-pager.
