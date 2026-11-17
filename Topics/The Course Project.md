---
title: "The Course Project"
course: GAME 1303
week: 2
type: topic
status: draft
tags:
  - game1303
  - topic
---

# The Course Project

**Week 2 · [[Lecture] Week 2](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2002%20-%20Lecture.md)**

> [!abstract] In one sentence
> Every student works in one Unity project, downloaded once, with clear rules about which folders are the course's and which are theirs.

## What this topic is for

The course project replaces separate script collections, which caused errors when mixed. Students should leave this lecture knowing where everything lives, which folders they must not edit, and why Play works from any scene.

## Key ideas

- **One download.** Students download the project ZIP from the template's **Releases** page, unzip it fully, rename the folder, and add it in Unity Hub with **Add → Add project from disk**.
- **Folder ownership:**

| Folder | Whose | Rule |
|---|---|---|
| `Assets/_Course/` | The course | Never edit, move or rename anything here. Updates overwrite it |
| `Assets/_Game/` | The student | Everything for their own game |
| `Assets/Scenes/Exercises/` | The student | Their **Save As** copies of exercise scenes |

- **Copy to change.** To change a course script, prefab or screen, copy it into `_Game` and edit the copy, or make a prefab variant.
- **Updates.** Fixes come as a `.unitypackage` on the Releases page. Importing one only changes `_Course`. `Assets/_Course/VERSION.txt` shows which version a student has.
- **The Scene List.** A scene can only be loaded during play if it is in **File → Build Profiles → Scene List**. The first scene in the list is the one a built game starts with.
- **The Bootstrapper.** Before any scene loads, the course creates a `[Course Services]` object that holds the Scene Loader. It's never added by hand, so Play works from any scene. Students can see it under **DontDestroyOnLoad** in the Hierarchy while the game runs.

## In class

1. Download, unzip, add and open the project live.
2. Tour the folders and the rules.
3. Press Play and show `[Course Services]` appear.

## Common problems

| What happens | Why |
|---|---|
| Unity can't open the project | It's still inside the ZIP, or the Unity version is wrong |
| "Can't find a scene named…" | The scene isn't in the Scene List, or the name is misspelled |
| A student's change to a course file disappeared | An update overwrote `_Course` |

## Where it comes up

- [Ex 01 — Bootstrap](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex01%20-%20Bootstrap.md).
- [Project Setup Check](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Assignments/Project%20Setup%20Check.md).
- [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md): kits install into `_Course` too.
