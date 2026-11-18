---
title: "Finding and Fixing Bugs"
course: GAME 1303
week: 10
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Finding and Fixing Bugs

**Week 10 · [[Lecture] Week 10](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2010%20-%20Lecture.md)**

> [!abstract] In one sentence
> A bug can only be fixed with confidence once it can be made to happen on purpose, and the Console and breakpoints show why it happens.

## What this topic is for

Students start a bug list in Ex 09, find and fix one real bug, and learn to report a problem precisely enough to get help.

## Key ideas

- **Reproduce it.** Write the exact steps. Make it happen twice. A bug that can't be repeated can't be confirmed fixed.
- **Change one thing at a time.** Then test again.
- **Read the first red error.** It names a script and a line. Later errors are often caused by it. See [Scripts and the Console](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Scripts%20and%20the%20Console.md).
- **Common families of student bugs:**

| Symptom | Usual cause |
|---|---|
| "…is empty" or "not set" | A field left empty in the Inspector |
| Works once, then stops | An object was destroyed while something still used it |
| Nothing happens | A misspelled name, a wrong tag, a missing collider or trigger |
| Works in the Editor, not in the build | A scene missing from the Scene List |

- **Log messages** show a value at one moment. **Breakpoints** stop the game at a line so every value can be inspected, using the code editor attached to Unity.
- **A good bug report:** what you did, what you expected, what happened, and the Console message.

## In class

1. Fix one bug live using only the Console.
2. Fix another by setting a breakpoint and inspecting a value.

## Where it comes up

- [Ex 09 — Debug & Profile](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex09%20-%20Debug%20%26%20Profile.md).
- [Bug Triage and Cutting Scope](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Bug%20Triage%20and%20Cutting%20Scope.md).
- [Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md): common Console messages.

## Further resources

- Unity Manual, [Set up C# debugging](https://docs.unity.com/en-us/engine/6000.3/manual/programming-environment/environment-and-tools/debugging-and-diagnostics/managed-code-debugging).
