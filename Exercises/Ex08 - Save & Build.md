---
title: "Exercise 08 — Save & Build"
course: GAME 1303
week: 9
status: draft
course_version: 0.10.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 08 — Save & Build

**Week 9 · in your own game · submitted at the end of class**

In this exercise you add a Settings screen, save one thing that matters, then make your first build and put it on a private itch.io page. Every milestone from here on is a link to that page.

> **Before class:** your game must have **no red errors** in the Console, or it can't be built. Create a free account on [itch.io](https://itch.io).

## What you'll learn

- How settings are shown and saved
- How to save progress or a high score so it survives closing the game
- How to make a Web build
- How to publish a build privately on itch.io

## Part 1 — A Settings screen

Do this in your menu scene.

1. Create a **UI Document** named `Settings`. Set its **Source Asset** to `Settings` from `Assets/_Course/Core/UI`, and its **Sort Order** to `1`.
2. Add a **UI Screen**. Tick **Hidden At Start** and set **Select When Shown** to `music-slider`.
3. Add the **UI Settings** component. Optional: drag one of your Sound Effects into **Preview Sound**, so moving the effects slider plays it.
4. Add **UI Button Events** with one button:

| Button Name | On Click |
|---|---|
| `back-button` | Drag in `Settings`, choose **UIScreen → Hide** |

5. Select your `Main Menu`. In its **UI Button Events**, add:

| Button Name | On Click |
|---|---|
| `settings-button` | Drag in `Settings`, choose **UIScreen → Show** |

Press **Play** and open Settings. Move the sliders while music plays. Stop the game and play again: the volumes are remembered.

**In the pause menu too.** In each level, the Pause Menu also has a **Settings** button. Add a `Settings` UI Document to the level the same way, with **Sort Order** `2`, and connect `settings-button` in the Pause Menu's **UI Button Events**.

## Part 2 — Save one thing

Decide what your player would be upset to lose. Then do **one** of these.

### A — A high score

For arcade games, runners and shooters.

1. In `Assets/_Game/Data`, create an **Int Variable** named `BestScore`.
2. In your level, add the **High Score** component to an object such as `Game Rules`. Set **Score** to your score variable and **Best** to `BestScore`.
3. Show `BestScore` on your HUD or end screen, with a **UI Variable Binder** binding such as `Best: {0}`. If the screen has no spare label, copy the screen's UXML into `Assets/_Game` and add a label in UI Builder.

### B — Progress

For games with levels, collections or unlocks.

1. Decide which variables are progress, such as `Coins` or a `LevelsUnlocked` number.
2. Add the **Variable Saver** component to an object in each level. List those variables under **Variables**.
3. Make it save at a sensible moment. For example, on the Level Complete screen's listener, add a response: **VariableSaver → Save**. Or tick **Save When Scene Ends**.
4. If your menu has a "New Game" path, add **VariableSaver → DeleteSave** to it.

> **Saving and resetting.** If the same scene also has a **Variable Resetter** that resets these variables when the scene starts, it will undo the load. Untick its **Reset When Scene Starts**.

**Test it:** play, change the value, stop, and play again. The value should still be there.

## Part 3 — Make a Web build

1. Open **File → Build Profiles**.
2. Under **Platforms**, select **Web**. If it says the module isn't installed, add **Web Build Support** to Unity 6000.3.10f1 from Unity Hub's **Installs** page, then restart Unity.
3. Click **Switch Platform** and wait.
4. Open the **Scene List**. Check that it has every scene in your game, in order, and that your **menu scene is first**. Untick any exercise scenes.
5. Click **Player Settings**. Set **Company Name** to your name and **Product Name** to your game's title. Under **Publishing Settings**, tick **Decompression Fallback**.
6. Back in Build Profiles, click **Build And Run**. Create a folder named `Builds` next to your `Assets` folder (not inside it) and choose it.

When the build finishes, it opens in your browser. Play it start to finish.

> [!tip] For every build after this one
> **[Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)** has these steps, plus Windows and macOS builds, and what to do when a build goes wrong.

> **Write down anything that's different from the Editor.** Missing scenes, text that doesn't fit, sounds that don't play. Fixing them is today's lab.

## Part 4 — Publish privately on itch.io

1. In the `Builds` folder, select **everything inside it** (the `index.html` file and the folders next to it) and compress it into a ZIP. `index.html` must be at the top level of the ZIP, not inside another folder.
2. On itch.io, choose **Upload new project**.
3. Set:
   - **Title:** your game's title
   - **Kind of project:** HTML
   - **Uploads:** your ZIP. Tick **This file will be played in the browser**.
   - **Embed options:** a viewport of `960` × `540`, and tick **Fullscreen button**.
   - **Visibility & access:** **Draft** for now.
4. Click **Save**, then **View page**, and play the game on the page.

## Part 5 — Your design decision

Write two sentences: what your game saves, and when it saves it. Say what the player would lose without it. If your game saves nothing but settings, say why that's right for your game.

## Check-off

Submit in Canvas, by the end of class: the link to your itch.io page (as a draft, it's only visible to you, so also add a screenshot of it running), and your two sentences.

- [ ] The Settings screen opens from the main menu, and volume changes are remembered.
- [ ] One thing is saved and loads again after the game is closed.
- [ ] A Web build runs in the browser, starting at your menu.
- [ ] The build is uploaded to a private itch.io page and plays there.
- [ ] Two sentences on what you save and why.

## If something goes wrong

| What you see | What to do |
|---|---|
| The build fails | Read the first red error in the Console. A project with errors can't be built |
| The build starts on the wrong scene | Drag your menu scene to the top of the Scene List |
| A level is missing in the build | Add its scene to the Scene List |
| itch.io shows a blank page or a loading error | Tick **Decompression Fallback** in Player Settings, rebuild, and upload again |
| itch.io says it can't find `index.html` | The ZIP has an extra folder level. Zip the files inside `Builds`, not the folder |
| The saved value doesn't come back | A **Variable Resetter** is resetting it, or **Save** was never called |
| The sliders do nothing | The **UI Settings** component is missing, or the slider names were changed |

## Related topics

- [Saving Progress](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Saving%20Progress.md)
- [Settings Players Expect](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Settings%20Players%20Expect.md)
- [Making a Build](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Making%20a%20Build.md)
- [Publishing on itch.io](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Publishing%20on%20itch.io.md)
