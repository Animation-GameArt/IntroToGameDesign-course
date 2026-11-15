---
title: "Exercise 01 — Bootstrap"
course: GAME 1303
week: 2
status: draft
course_version: 0.2.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 01 — Bootstrap

**Week 2 · checked off in lab**

In this exercise you get the course project running, set up your backup, and make two scenes that switch back and forth with a fade.

## What you'll learn

- How to get the course project and open it in Unity Hub
- How to save your own copy of a scene
- What the **Scene List** is, and why a scene must be in it
- How to add a component and set it up in the Inspector
- What the **Bootstrapper** does: it creates the course services before any scene loads, so you can press Play from any scene

## Part 1 — Get the course project

1. Go to the course project's page on GitHub and open **Releases**.
2. Download the latest project ZIP.
3. **Unzip it fully** to your laptop or SSD. Unity can't open a project from inside a ZIP.
4. Rename the folder to your own project name, for example `GAME1303_YourName`.
5. Open **Unity Hub**. Choose **Add → Add project from disk** and select your folder.
6. Open the project. The first time takes several minutes while Unity builds its `Library` folder.

> **Check:** the Console (Window → General → Console) shows no red error messages.

## Part 2 — Set up your backup

Choose one, and tell your instructor which.

- **Unity Version Control:** in Unity Hub, open your project's menu (⋯) and choose **Use Unity Version Control**, then **Connect to Version Control**. At the end of every work session, open **Window → Unity Version Control** in Unity, write a short comment, and check in.
- **SSD:** work from your SSD. Once a week, copy the whole project folder to a second device at home. Don't keep the project in a cloud-synced folder such as OneDrive.

## Part 3 — Look at the project folders

In the **Project** window, open `Assets`:

| Folder | Whose | Rule |
|---|---|---|
| `_Course` | The course | Don't edit, move or rename anything in here |
| `_Game` | Yours | Everything for your own game goes here (from week 8) |
| `Scenes/Exercises` | Yours | Your saved copies of the exercise scenes |

## Part 4 — Make scene A

1. In the Project window, open `Assets/Scenes` and double-click **SampleScene**.
2. Choose **File → Save As…** and save it in `Assets/Scenes/Exercises` as `Ex01_Bootstrap`.
3. In the **Hierarchy**, select **Main Camera**.
4. In the **Inspector**, find the **Camera** component, open **Environment**, and change the **Background** color to any color you like.
5. Save the scene (**Ctrl+S**, or **Cmd+S** on Mac).

## Part 5 — Make scene B

1. Choose **File → Save As…** again and save the scene in the same folder as `Ex01_SceneB`.
2. Change the Main Camera's **Background** to a clearly different color.
3. Save the scene.

You now have two scenes that look different, so you can tell which one is showing.

## Part 6 — Add both scenes to the Scene List

Unity can only load a scene while the game is running if the scene is in the Scene List.

1. Choose **File → Build Profiles**.
2. Select **Open Scene List**.
3. Drag `Ex01_Bootstrap` and `Ex01_SceneB` from the Project window into the list.
4. Remove SampleScene from the list by selecting it a hitting the backspace
5. Close the Build Profiles window.

## Part 7 — Add a Scene Changer to each scene

**In `Ex01_SceneB`** (the scene you have open):

1. In the Hierarchy, right-click and choose **Create Empty**. Name the new object `Scene Changer`.
2. With it selected, click **Add Component** in the Inspector and search for **Scene Changer**. Add it.
3. Set its fields:
   - **Scene Name:** `Ex01_Bootstrap`
   - **Load After Seconds:** `0`
   - **Load On Action:** click the small circle at the right of the field and choose **Player/Jump**.
4. Save the scene.

**In `Ex01_Bootstrap`:**

1. Open `Ex01_Bootstrap` from the Project window.
2. Repeat steps 1–3, but set **Scene Name** to `Ex01_SceneB`.
3. Save the scene.

> **Spelling matters.** The Scene Name must match the scene's file name exactly, without `.unity`.

## Part 8 — Play

1. Press **Play**.
2. Click once in the **Game** view, then press **Space** (or the bottom face button on a gamepad). The screen fades out, the other scene loads, and the screen fades in.
3. Press Space again to go back.
4. While the game is running, look at the Hierarchy. Under **DontDestroyOnLoad** there is an object named **[Course Services]**. Select it: it has a **Scene Loader** and a **Screen Fader**.
5. Stop the game. Open `Ex01_SceneB` and press Play from there. It works the same way.

You never added [Course Services] to either scene. The **Bootstrapper** creates it when the game starts, before the first scene loads, and it stays alive when scenes change. That's why you can press Play from any scene.

## Part 9 — Experiment

Try each of these, press Play, and watch what happens. Put each one back afterwards.

1. **A timer.** On one Scene Changer, set **Load After Seconds** to `3`. The scene now changes by itself after 3 seconds.
2. **A wrong name.** Change one **Scene Name** to `Ex01_SceneC`. Press Space, then read the red message in the Console. It tells you what's wrong and how to fix it.
3. **A missing scene.** Fix the name, then remove `Ex01_SceneB` from the Scene List (File → Build Profiles → Scene List) and try again. Read the Console message, then add the scene back.

Reading Console messages is how you'll find most problems this semester.

## Check-off

Show your instructor:

- [ ] Your project opens with no red errors in the Console.
- [ ] Your backup is set up (Unity Version Control, or SSD plus a second copy at home).
- [ ] `Ex01_Bootstrap` and `Ex01_SceneB` are saved in `Assets/Scenes/Exercises`.
- [ ] Pressing Space switches between the two scenes with a fade, starting from either scene.
- [ ] You can point to [Course Services] in the Hierarchy while the game runs, and say what creates it.

## If something goes wrong

| What you see | What to do |
|---|---|
| Nothing happens when you press Space | Click in the Game view first. Check that **Load On Action** is set to **Player/Jump**. |
| "can't find a scene named…" in the Console | Check the spelling of **Scene Name**, and check that the scene is in the Scene List. |
| The scene changes back straight away | That's the timer. Set **Load After Seconds** to `0`. |
| You can't find **Scene Changer** in Add Component | Check the Console for red errors. Scripts don't appear until all errors are fixed. |
