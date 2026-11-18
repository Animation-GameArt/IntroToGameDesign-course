---
title: "Exercise 00 — Setup"
course: GAME 1303
week: 1
status: draft
course_version: 0.10.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 00 — Setup

**Week 1 · checked off in lab**

In this exercise you install Unity, make a practice project, and learn your way around the Editor. The practice project is thrown away afterwards. Next week you download the real course project.

> **On a lab computer?** Unity Hub and Unity are already installed. Skip Part 1 and start at Part 2.

## What you'll learn

- How Unity Hub manages Unity versions and projects
- The six Editor windows you'll use every week
- What Play mode is, and why changes made in it disappear
- The difference between an object in a scene and a file in the project

## Part 1 — Install Unity (your own computer)

1. Download and install **Unity Hub** from [unity.com/download](https://unity.com/download).
2. Open Unity Hub and sign in with a Unity account. Creating one is free.
3. Choose **Installs → Install Editor**. Find **Unity 6000.3.10f1**. If it isn't listed under the current releases, look in the **Archive** tab.
4. When asked for modules, tick:
   - **Web Build Support**: you'll use it to publish your game in Week 9.
   - The build support for your own computer (Windows or Mac), if it's offered.
5. Click **Install** and wait. It's a large download, so start it early.

> **Check:** Installs lists **6000.3.10f1**. Everyone in the course uses exactly this version.

## Part 2 — Make a practice project

1. In Unity Hub, choose **Projects → New project**.
2. Check that the Editor version at the top is **6000.3.10f1**.
3. Choose the **Universal 2D** template.
4. Name the project `Practice`, choose where to save it (your laptop or SSD), and click **Create project**.

The first time a project opens takes a few minutes.

## Part 3 — Tour the Editor

Find each window. If one is missing, open it from the **Window** menu.

| Window | What it shows | Try this |
|---|---|---|
| **Scene** | The level, for building it | Scroll to zoom. Hold the middle mouse button (or **Alt** and drag on a trackpad) to move around |
| **Game** | What the player sees | Click its tab |
| **Hierarchy** | Every object in the open scene | Click **Main Camera** |
| **Inspector** | The settings of whatever is selected | With Main Camera selected, find its **Camera** component |
| **Project** | Every file in the project | Open the `Assets` folder |
| **Console** | Messages and errors | Find it under **Window → General → Console** if it isn't open |

## Part 4 — Add something to the scene

1. Choose **GameObject → 2D Object → Sprites → Square**. A white square appears in the Scene view and in the Hierarchy.
2. With the square selected, look at the Inspector. Find the **Transform** and change **Position** to `2, 1, 0`.
3. Find the **Sprite Renderer** and change its **Color**.
4. Use the tools in the top-left of the Scene view to **Move** (W), **Rotate** (E) and **Scale** (R) the square by dragging.

> **Scene objects and project files.** The square you made is an **object in the scene**. It's listed in the Hierarchy. A **file in the project** is listed in the Project window and can be used in many scenes. Some Unity tools only accept files. Keep the difference in mind; it comes up again in Exercise 04.

## Part 5 — Play mode

1. Press **Play** (the triangle at the top of the Editor). The Game view shows what the player would see.
2. While the game is playing, select the square and change its **Color** in the Inspector.
3. Press **Play** again to stop.

The color goes back to what it was. **Anything you change during Play mode is lost when you stop.** This is the most common way students lose work in Unity. Before you change something, check whether the Play button is lit.

## Part 6 — Save

1. Choose **File → Save** (**Ctrl+S**, or **Cmd+S** on Mac).
2. Close Unity, then open the project again from Unity Hub. Your square is still there.

## Part 7 — Your design decision

Using only sprites (squares, circles, capsules and triangles from **GameObject → 2D Object → Sprites**), arrange a scene that suggests one of your three game ideas. Change colors, sizes and positions. Be ready to say what the idea is and what each shape stands for.

## Check-off

Show your instructor:

- [ ] Unity 6000.3.10f1 opens your practice project.
- [ ] You can name the six windows and say what each one is for.
- [ ] You can show what happens to a change made during Play mode.
- [ ] Your scene of shapes, and the game idea it suggests.

## If something goes wrong

| What you see | What to do |
|---|---|
| 6000.3.10f1 isn't in the list | Look in the **Archive** tab of Install Editor |
| The install fails | Check free disk space. Unity needs several gigabytes |
| A window is missing | Open it from the **Window** menu, or choose **Window → Layouts → Default** |
| Changes disappeared | They were made during Play mode |

## Related topics

- [Unity Hub and the Editor](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Unity%20Hub%20and%20the%20Editor.md)
- [Core Loops](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Core%20Loops.md)
