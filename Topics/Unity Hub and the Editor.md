---
title: "Unity Hub and the Editor"
course: GAME 1303
week: 1
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Unity Hub and the Editor

**Week 1 · [[Lecture] Week 1](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2001%20-%20Lecture.md)**

> [!abstract] In one sentence
> Unity Hub installs Unity and opens projects; the Editor is where the game is built, through six windows students use every week.

## What this topic is for

Students leave the first class with Unity installed, a practice project open, and enough orientation to follow the Week 2 exercise. Nobody should be lost on "which window is the Inspector?" in Week 2.

## Key ideas

- **One version for everyone.** The course uses **Unity 6000.3.10f1** (Unity 6.3 LTS). The course project only opens cleanly in that version. Unity Hub can hold several versions side by side.
- **The Hub manages projects.** Students add a project to the Hub once, then open it from there.
- **The six windows:**

| Window | What it shows |
|---|---|
| Scene | The level, for building it |
| Game | What the player sees |
| Hierarchy | Every object in the open scene |
| Project | Every file in the project |
| Inspector | The settings of whatever is selected |
| Console | Messages and errors |

- **Play mode is temporary.** Changes made while the game is playing are lost when it stops. Teach this on day one; it prevents a lot of lost work.
- **Scene objects and project files are different things.** An object in the Hierarchy lives in the scene. A file in the Project window lives on disk and can be used in many scenes. Students mix these up often, and some Unity tools only accept files.

## In class

1. Install Unity Hub and Unity 6000.3.10f1 together, from the Hub's **Installs** page.
2. Create a practice project from the **Universal 2D** template.
3. Tour the six windows. Add a sprite, move it, press Play, change it during Play, stop, and watch the change disappear.

## Common problems

| What happens | Why |
|---|---|
| The install takes very long or fails | Disk space or network. Check before class, especially on laptops |
| A student's changes vanished | They were made during Play mode |
| A tool won't accept something dragged from the Hierarchy | It needs a file from the Project window |

## Where it comes up

- [Ex 00 — Setup](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex00%20-%20Setup.md) (Week 1).
- [Ex 01 — Bootstrap](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex01%20-%20Bootstrap.md): adding the course project in the Hub.
- [Ex 04 — Level](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md): the Tile Palette needs a sprite file from the Project window.

## Further resources

- Unity Manual, [Unity Editor interface](https://docs.unity.com/en-us/engine/6000.3/manual/unity-editor).
- Unity Hub documentation, [Create a new project](https://docs.unity.com/en-us/hub/project-create).
- Unity Learn, [Unity Essentials](https://learn.unity.com/pathway/unity-essentials): a free self-paced introduction for students who want more practice.
