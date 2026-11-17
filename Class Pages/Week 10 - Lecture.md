---
title: "[Lecture] Week 10"
course: GAME 1303
week: 10
status: draft
tags:
  - game1303
  - lecture-page
---

# Week 10 — Ex 09: Debug & Profile · First Playable due

**Exercise:** Ex 09 — Debug & Profile. A bug list, one bug found and fixed, one Profiler reading, and a triage.

**Also due:** First Playable, uploaded by 11:59 PM the night before class: one complete pass through the core loop, running outside the Editor.

## Lecture topics, expanded

**Reproducing a bug.** A bug that can't be made to happen on purpose can't be fixed with confidence. Teach the habit: write down the exact steps, make it happen twice, then change one thing at a time. Most student bugs fall into a few families, and the Console names them: a field left empty in the Inspector, an object that was destroyed while something still pointed at it, a name that was misspelled.

**Reading errors, and breakpoints.** Read the first red error, not the last. It names a script and a line, and double-clicking it opens that line. A log message shows a value at one moment. A breakpoint stops the game at a line so every value can be inspected. Demonstrate one real bug found each way. Students don't need to become programmers; they need to be able to report a problem precisely enough to get help.

**The Profiler.** When a game stutters, guessing is slow and usually wrong. The Profiler shows how long each frame took and what the time was spent on. Open it on a scene that spawns too many objects, find the spike, and fix it with the Spawner's limit. One reading, before and after, is the whole skill at this level.

**Triage, cutting and milestones.** Sort every bug by how bad it is and how often it happens: must fix, should fix, won't fix. Deciding not to fix something is a legitimate, professional choice. The same goes for features: cut the nice-to-haves now, on purpose, or lose them later by accident. Then define the remaining milestones in one line each. First Playable: the loop works once. Alpha: every feature exists. Beta: all content is in. Gold: released.

## Topic notes

Each topic has its own page with the lecture's intent, key ideas, an in-class plan and further resources.

- [Finding and Fixing Bugs](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Finding%20and%20Fixing%20Bugs.md)
- [The Profiler](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/The%20Profiler.md)
- [Bug Triage and Cutting Scope](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Bug%20Triage%20and%20Cutting%20Scope.md)

## Connecting it forward

This is the last lecture. From next week each class opens with a stand-up and a short topic, and the rest is studio time. The bug list started today is used at every milestone, and the bug bash in Week 14 adds to it.
