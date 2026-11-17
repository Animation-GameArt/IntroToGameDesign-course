---
title: "Scripts and the Console"
course: GAME 1303
week: 3
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Scripts and the Console

**Week 3 · [[Lecture] Week 3](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2003%20-%20Lecture.md)**

> [!abstract] In one sentence
> Unity runs a script's methods at set moments, and when something goes wrong the Console says what and where, if you read the first message.

## What this topic is for

Students in this course write little code, but they read errors every week. The goal is that a student facing a red message reads it, finds the object it names, and either fixes it or reports it precisely.

## Key ideas

- **The script lifecycle.** Unity calls methods with special names at set moments:

| Method | When |
|---|---|
| `Awake` | Once, when the object is created |
| `OnEnable` | Each time the object is switched on |
| `Start` | Once, just before the first frame it's active |
| `Update` | Every frame |
| `FixedUpdate` | On the physics clock, used for movement |
| `OnDisable` | Each time the object is switched off |

- **The Console's three kinds of message.** White messages are information, yellow are warnings, red are errors. A red error that appears while editing stops **all** scripts from compiling, so nothing new appears in Add Component until it's fixed.
- **Read the first red message.** Later errors are often caused by the first one. The message names a script and a line; double-clicking it opens that line.
- **The course scripts explain themselves.** Common mistakes, such as an empty field or a misspelled scene name, produce plain-language messages that name the object and the fix.
- **Logging and breakpoints.** A log message shows a value at one moment. A breakpoint stops the game at a line so every value can be inspected. Breakpoints come back in Week 10.

## In class

1. Cause three errors on purpose: an empty Input field, a misspelled scene name, a scene missing from the Scene List. Read each message aloud and fix it.
2. Click a message and show it highlighting the object in the Hierarchy.

## Common problems

| Students often… | Help them by… |
|---|---|
| Scroll to the newest error | Pointing to the first one |
| Report "it doesn't work" | Asking for the exact Console message |
| Ignore yellow warnings | Showing that the course's warnings usually name a missing setting |

## Where it comes up

- [Ex 01](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex01%20-%20Bootstrap.md), Part 9: reading the Scene Loader's messages.
- Every exercise's "If something goes wrong" table.

## Further resources

- Unity Manual, [Event function execution order](https://docs.unity.com/en-us/engine/6000.3/manual/scripting/managing-update-order/execution-order).
- Unity Manual, [Console window reference](https://docs.unity.com/en-us/engine/6000.3/manual/unity-editor/editor-windows-views-reference/console-window/console).
