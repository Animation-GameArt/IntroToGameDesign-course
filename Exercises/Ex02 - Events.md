---
title: "Exercise 02 — Events"
course: GAME 1303
week: 3
status: draft
course_version: 0.3.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 02 — Events

**Week 3 · checked off in lab**

In this exercise a ball rolls down a ramp and collects coins. The coins add to a score, a text shows the score, and a key opens a door. None of these objects know about each other. They are connected only through two small assets: a **variable** and an **event channel**.

## What you'll learn

- How colliders, triggers and a Rigidbody make objects touch and react
- What a **ScriptableObject** asset is: data that lives in the Project window, outside any scene
- How a **variable asset** shares a value, such as the score, between objects
- How an **event channel** lets one object announce something and other objects react
- Why this keeps objects independent, so you can add, remove or swap them without breaking anything

## Part 1 — Start the scene

1. Open `Ex01_Bootstrap` from `Assets/Scenes/Exercises`.
2. Choose **File → Save As…** and save it in the same folder as `Ex02_Events`.
3. In the Hierarchy, delete the `Scene Changer` object. You'll add a new one later.

## Part 2 — Build the ramp and the ball

**The ramp**

1. Choose **GameObject → 2D Object → Sprites → Square**. Name it `Ramp`.
2. In the Inspector, set its **Transform**:
   - Position: `0, -1, 0`
   - Rotation: `0, 0, -10`
   - Scale: `10, 0.5, 1`
3. Click **Add Component** and add a **Box Collider 2D**.

**The ball**

1. Choose **GameObject → 2D Object → Sprites → Circle**. Name it `Ball`.
2. Set its Position to `-4, 2, 0`.
3. Add a **Circle Collider 2D**.
4. Add a **Rigidbody 2D**. This makes the ball fall and roll.
5. At the top of the Inspector, open the **Tag** dropdown and choose **Player**.

Press **Play**. The ball drops onto the ramp, rolls down it and falls off the end. Stop the game.

## Part 3 — Add coins

1. Create another **Circle** sprite. Name it `Coin`.
2. Set its Position to `-2, 0.1, 0` and its Scale to `0.5, 0.5, 1`.
3. In the **Sprite Renderer**, change **Color** to yellow.
4. Add a **Circle Collider 2D** and tick **Is Trigger**. A trigger notices when something touches it, but doesn't block it.
5. Add the **Collectible** component. Leave its settings as they are.
6. Select the coin and press **Ctrl+D** (**Cmd+D** on Mac) twice to make two copies. Set their Positions to:
   - `0, -0.25, 0`
   - `2, -0.6, 0`

Press **Play**. Each coin disappears when the ball touches it. Nothing is counting them yet.

> **Why the ball can collect coins:** the Collectible only reacts to objects tagged **Player**. That's why you set the ball's tag.

## Part 4 — Create a Score variable

1. In the Project window, open `Assets/Scenes/Exercises` and create a folder named `Ex02_Data`.
2. Open the folder. Right-click in it and choose **Create → Collin Game → Variables → Int Variable**. Name it `Score`.
3. Select `Score`. In the Inspector, check that **Initial Value** is `0`.
4. In the Hierarchy, select all three coins (click the first, then **Shift**-click the last).
5. In the **Collectible** component, drag `Score` from the Project window into the **Add To** field. Leave **Amount** at `1`.

Press **Play**, then click the `Score` asset in the Project window. The Inspector shows **Current Value** going up as the ball collects coins.

`Score` is not in the scene. It's an asset, like a sprite or a sound, that holds one number. Any object in any scene can use it.

## Part 5 — Show the score

1. Choose **GameObject → 3D Object → Text - TextMeshPro**. Name it `Score Text`.
2. Set its Position to `0, 4, 0`.
3. In the **TextMeshPro** component, set **Font Size** to `8` and set the **Alignment** to center.
4. Add the **Variable Label** component and set:
   - **Variable:** drag in `Score`
   - **Format:** `Score: {0}`

Press **Play**. The text counts up as coins are collected.

The coins don't know the text exists, and the text doesn't know the coins exist. Both only know `Score`. You could delete the text, or add a second one, and the coins would work exactly the same.

## Part 6 — A key and a door

A variable shares a value. An **event channel** shares a moment: "this just happened."

**The door**

1. Create a **Square** sprite. Name it `Door`.
2. Set its Position to `3.5, -0.4, 0` and its Scale to `0.5, 2, 1`. Give it any color.
3. Add a **Box Collider 2D**.

Press **Play**. The ball now stops at the door. Stop the game.

**The event channel**

1. In `Ex02_Data`, right-click and choose **Create → Collin Game → Events → Void Event Channel**. Name it `KeyCollected`.

**The key**

1. Select the last coin, the one at `2, -0.6, 0`. Rename it `Key` and give it a different color.
2. In its **Collectible** component, drag `KeyCollected` into the **Raise Event** field.

**Make the door listen**

1. Select `Door` and add the **Void Event Listener** component.
2. Drag `KeyCollected` into its **Channel** field.
3. Under **Response**, click **+**.
4. Drag the `Door` object from the Hierarchy into the empty object field.
5. Open the function dropdown and choose **GameObject → SetActive (bool)**. Leave the checkbox **unticked**.

Press **Play**. When the ball collects the key, the door disappears and the ball rolls on.

The key announces "key collected" on the channel. The door listens to that channel and hides itself. The key doesn't know there is a door.

> **Try it by hand:** press Play, quickly select `KeyCollected` in the Project window, and click **Raise** in the Inspector. The door opens even though the ball hasn't reached the key.

## Part 7 — Restart, and reset the score

1. Add `Ex02_Events` to the Scene List (**File → Build Profiles → Open Scene List**, then drag the scene in).
2. Create an empty GameObject named `Scene Changer` and add the **Scene Changer** component:
   - **Scene Name:** `Ex02_Events`
   - **Load On Action:** `Player/Jump`
3. Press **Play**. Let the ball collect everything, then press **Space** to restart the scene.

Watch the score. After the restart it keeps counting from where it was: 3, then 6. The scene started again, but `Score` lives outside the scene, so it kept its value. That's useful when a score should carry from level to level. Here, it should start again.

4. Create an empty GameObject named `Game Setup` and add the **Variable Resetter** component.
5. Under **Variables**, click **+** and drag in `Score`.
6. Press **Play** and restart with Space. The score now starts at 0 each time.

## Part 8 — Experiment

1. **Worth more.** Set one coin's **Amount** to `5`.
2. **Two listeners.** Add a second `Score Text` somewhere else with a different Format, such as `Coins: {0}`. Both update.
3. **A second reaction.** Make something else react to `KeyCollected`: add a **Void Event Listener** to the `Ramp`, and use its Response to hide another object or show a hidden one.
4. **See the messages.** Select `Score` and tick **Log Changes**. Select `KeyCollected` and tick **Log When Raised**. Play, and read the Console.

## Check-off

Show your instructor:

- [ ] The ball rolls down the ramp and collects the coins.
- [ ] The score text counts up, and starts at 0 again after a restart.
- [ ] Collecting the key opens the door.
- [ ] You can explain what `Score` and `KeyCollected` are, and where they live.
- [ ] You can explain why the key doesn't need to know about the door.

## If something goes wrong

| What you see | What to do |
|---|---|
| The ball falls through the ramp | The ramp needs a **Box Collider 2D**, and the ball needs a **Circle Collider 2D**. |
| The ball bounces off the coins | Tick **Is Trigger** on each coin's Circle Collider 2D. |
| The coins don't disappear | Check that the ball's **Tag** is **Player** and that it has a **Rigidbody 2D**. |
| The score text doesn't change | Check that the coins' **Add To** field and the label's **Variable** field both hold `Score`. |
| The door doesn't open | Check that the key's **Raise Event** and the door's **Channel** both hold `KeyCollected`, and that the Response is set to **GameObject → SetActive** with the box unticked. |
| The text is huge or missing | Check **Font Size** is `8` and Position is `0, 4, 0`. |
