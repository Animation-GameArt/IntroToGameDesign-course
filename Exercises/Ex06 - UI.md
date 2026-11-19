---
title: "Exercise 06 — UI"
course: GAME 1303
week: 7
status: draft
course_version: 0.12.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 06 — UI

**Week 7 · checked off in lab**

In this exercise you finish the sandbox game. You replace the floating score text with a real HUD, add a pause menu and a win screen, build a main menu in its own scene, and make damage show as numbers above the player.

> **If you did the turn-based Exercise 05:** follow the same steps, starting from `Ex05_TurnBased`. Use `HeroHealth` wherever these steps say `PlayerHealth`. Skip Part 4's first step and connect the win screen to the Turn Manager, as described there.

## What you'll learn

- How a **UI Document** puts a UI Toolkit screen into a scene
- How a HUD stays up to date by listening to **variables**
- How **pausing** stops time and switches off the player's controls
- How the event from Exercise 04 can show a **win screen** without the goal knowing about it
- How a game flows between scenes: menu, play, pause, win, and back

## Part 1 — Start the scene

1. Open `Ex05_Combat` and choose **File → Save As…**. Save it as `Ex06_UI`.
2. Select `Scene Changer` and change its **Scene Name** to `Ex06_UI`.
3. Add `Ex06_UI` to the Scene List.
4. In `Assets/Scenes/Exercises`, create a folder named `Ex06_Data`.

## Part 2 — The HUD

1. Choose **GameObject → UI Toolkit → UI Document**. Name it `HUD`.
2. In the **UI Document** component, drag `HUD` from `Assets/_Course/Core/UI` into the **Source Asset** field.
   Check that **Panel Settings** says `CoursePanelSettings`. It's filled in for you, and every screen in this exercise uses it, so they all scale the same way. If it's empty or says something else, drag in `CoursePanelSettings` from `Assets/_Course/Core/UI`.
3. Add the **UI Variable Binder** component. Under **Bindings**, click **+** twice and fill them in:

| Label Name | Variable | Format |
|---|---|---|
| `health-label` | `PlayerHealth` | `Health: {0}` |
| `score-label` | `Score` | `Score: {0}` |

4. Under `Main Camera`, delete `Score Text` and `Health Text`. The HUD replaces them.

Press **Play**. Health and score now sit at the top of the screen and stay there as the camera moves.

The HUD doesn't know about the player, the coins or the spikes. It listens to the same `Score` variable you made in Exercise 02, and the same `PlayerHealth` from Exercise 05.

## Part 3 — A pause menu

1. Create another **UI Document** and name it `Pause Menu`.
2. Set its **Source Asset** to `PauseMenu` from `Assets/_Course/Core/UI`, and its **Sort Order** to `1`, so it draws in front of the HUD.
3. Add the **UI Screen** component:
   - Tick **Hidden At Start**
   - **Select When Shown:** `resume-button`
4. Add the **Pause Controller** component. **Input** and **Pause Screen** should fill themselves in. If they're empty, drag in `InputReader` and the `Pause Menu` object.
5. Add the **UI Button Events** component. Under **Buttons**, click **+** twice:

| Button Name | On Click |
|---|---|
| `resume-button` | Drag in `Pause Menu`, choose **PauseController → Resume** |
| `restart-button` | Drag in `Scene Changer`, choose **SceneChanger → ReloadScene** |

Press **Play**, then press **Esc** (or **Start** on a gamepad). The game freezes and the menu appears. **Resume** continues, and **Restart** starts the level again. The Main Menu button comes in Part 5. The **Settings** button does nothing yet; you connect it in Exercise 08.

While paused, time is stopped and the player's controls are off. The Pause button itself keeps working, so Esc also un-pauses.

## Part 4 — A win screen

1. Select `Scene Changer`. Remove its **Void Event Listener** (**⋮ → Remove Component**). Reaching the goal should no longer restart the level by itself.
2. Create a **UI Document** named `Win Screen`. Set its **Source Asset** to `EndScreen` and its **Sort Order** to `2`.
3. Add the **UI Screen** component:
   - Tick **Hidden At Start**
   - **Select When Shown:** `play-again-button`
4. Add a **UI Variable Binder** with one binding: `score-label`, `Score`, `Score: {0}`.
5. Add a **Void Event Listener**. Set its **Channel** to `LevelCompleted`, from `Ex04_Data`.
6. Under **Response**, click **+** twice:
   - Drag in `Win Screen` and choose **UIScreen → Show**.
   - Drag in the `InputReader` asset from `Assets/_Course/Core/Input` and choose **InputReader → DisablePlayerInput**.
7. Add **UI Button Events** with one button for now:

| Button Name | On Click |
|---|---|
| `play-again-button` | Drag in `Scene Changer`, choose **SceneChanger → ReloadScene** |

Press **Play** and reach the goal. The win screen appears with your score, and the player stops responding. **Play Again** restarts the level.

The goal still only raises `LevelCompleted`, exactly as it did in Exercise 04. You changed what listens to it, and the goal never needed to know.

> **Turn-based version:** skip step 1. In step 5, don't add a Void Event Listener. Select `Battle` and, under **On Player Won**, add the two responses from step 6. You can delete `Win Text`.

## Part 5 — A main menu

**Make the menu scene**

1. Choose **File → New Scene**, pick the 2D scene template, and save it in `Assets/Scenes/Exercises` as `Ex06_MainMenu`.
2. Create a **UI Document** named `Main Menu`. Set its **Source Asset** to `MainMenu`.
3. Add a **UI Screen** and set **Select When Shown** to `play-button`.
4. Add a **Scene Changer** and set its **Scene Name** to `Ex06_UI`.
5. Add **UI Button Events** with two buttons:

| Button Name | On Click |
|---|---|
| `play-button` | Drag in `Main Menu`, choose **SceneChanger → Load** |
| `quit-button` | Drag in `Main Menu`, choose **SceneChanger → QuitGame** |

**Add a credits screen**

Every asset you didn't make yourself must be credited. The credits are plain text files, so they're easy to keep up to date.

1. In the Project window, open `Assets/_Game` and double-click `Credits`. Replace the title and name with your own, and save.
2. Create a **UI Document** named `Credits`. Set its **Source Asset** to `Credits` from `Assets/_Course/Core/UI`, and its **Sort Order** to `1`.
3. Add a **UI Screen**. Tick **Hidden At Start** and set **Select When Shown** to `back-button`.
4. Add the **UI Credits** component. Under **Credit Files**, click **+** twice. Drag in your `Credits` file from `Assets/_Game` first, then `Course Credits` from `Assets/_Course/Credits`.
5. Add **UI Button Events** with one button:

| Button Name | On Click |
|---|---|
| `back-button` | Drag in `Credits`, choose **UIScreen → Hide** |

6. Select `Main Menu`. In its **UI Button Events**, add a third button (the menu's **Settings** button is connected in Exercise 08):

| Button Name | On Click |
|---|---|
| `credits-button` | Drag in `Credits`, choose **UIScreen → Show** |

**Finish the menu scene**

1. Save the scene.
2. Open the Scene List (**File → Build Profiles → Open Scene List**). Add `Ex06_MainMenu` and drag it to the **top** of the list. The first scene in the list is the one a built game starts with.

**Connect the Main Menu buttons in the level**

1. Open `Ex06_UI`.
2. Create an empty GameObject named `To Main Menu`. Add a **Scene Changer** and set its **Scene Name** to `Ex06_MainMenu`.
3. Select `Pause Menu`. In **UI Button Events**, add a third button:

| Button Name | On Click |
|---|---|
| `menu-button` | Drag in `To Main Menu`, choose **SceneChanger → Load** |

4. Select `Win Screen` and add the same `menu-button` entry to its **UI Button Events**.

Open `Ex06_MainMenu` and press **Play**. You can now go from the menu into the level, pause, return to the menu, win, and play again. In the Editor, **Quit** stops Play mode. In a built game it closes the game.

## Part 6 — Damage numbers

1. In `Ex06_UI`, select `Player` and add the **Health Popups** component.

Press **Play** and touch the spikes. A red `-1` floats up from the player. Collect the heart and a green `+1` appears.

This is **spatial UI**: it's placed in the game world, at the thing it describes, and it isn't part of the HUD.

## Part 7 — Make the HUD yours

The course's UI files are in `_Course`, so you change them by working on a copy.

1. In the Project window, open `Assets/_Course/Core/UI` and select `HUD`.
2. Press **Ctrl+D** (**Cmd+D** on Mac) to duplicate it. Drag the copy into `Ex06_Data` and rename it `MyHUD`.
3. Double-click `MyHUD`. It opens in the **UI Builder**.
4. Change the layout. Some things to try:
   - Select a label in the **Hierarchy** panel and change its **Text**.
   - Drag the labels into a different order.
   - Select `hud` and, under **Flex** or **Align**, change how its contents are arranged.
5. Save with **Ctrl+S**.
6. Select the `HUD` object in your scene and set its **Source Asset** to `MyHUD`.

Keep the names `health-label` and `score-label`, because the UI Variable Binder finds the labels by those names.

Use your screen layout from Week 5 as the plan. Decide what the player needs to see at every moment, where it goes, and what you can leave off.

**Go further.** Copy `MainMenu` in the same way and give the game a title and your name.

## Check-off

Show your instructor:

- [ ] The HUD shows health and score, and updates as you play.
- [ ] Esc pauses and un-pauses, and the pause menu's three buttons work.
- [ ] Reaching the goal shows the win screen with the score.
- [ ] The game starts at the main menu, and you can get from every screen to every other.
- [ ] The Credits screen shows your name and the course credits.
- [ ] Damage and healing show as floating numbers.
- [ ] You changed the HUD's layout, and can say why it shows what it shows.

The sandbox game is complete. Every script in it is one you can use in your own game, starting next week.

## If something goes wrong

| What you see | What to do |
|---|---|
| A screen shows nothing | Check the UI Document's **Source Asset**. Check that **Panel Settings** is `CoursePanelSettings`; if not, choose **Collin Game → UI → Use Course Panel Settings in Open Scenes**. |
| Screens are different sizes, or text is tiny | Choose **Collin Game → UI → Use Course Panel Settings in Open Scenes**, then save the scene. |
| The HUD shows "Score: 0" and never changes | Check the **Label Name** spelling and the **Variable** in the UI Variable Binder. |
| Buttons don't react to clicks | Check the **Button Name** spelling in UI Button Events, and read the Console for a warning that names the missing button. |
| The pause menu shows at the start | Tick **Hidden At Start** on its UI Screen. |
| Esc does nothing | Check that the Pause Controller's **Input** field holds `InputReader`. Click in the Game view first. |
| The Credits screen is empty | Check that **Credit Files** on the UI Credits component holds both text files. |
| The pause menu is behind the HUD | Set the Pause Menu's **Sort Order** higher than the HUD's. |
| After winning, the player can't move in the next round | This is fixed when a scene loads. Use **Play Again** or **Main Menu**, not the Editor's Play button, to continue. |
| A menu can't be used with a gamepad | Set **Select When Shown** on its UI Screen to the name of its first button. |

## Related topics

- [UI Toolkit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/UI%20Toolkit.md)
- [Binding the HUD to Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Binding%20the%20HUD%20to%20Data.md)
- [Four Kinds of UI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Four%20Kinds%20of%20UI.md)
- [Menus, Pause and Usability](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Menus%2C%20Pause%20and%20Usability.md)
- [ScriptableObjects: Variables and Events](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/ScriptableObjects%20-%20Variables%20and%20Events.md)
- [Health and Damage](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Health%20and%20Damage.md)
