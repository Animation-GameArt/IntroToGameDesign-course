---
title: "Exercise 03 — Player"
course: GAME 1303
week: 4
status: draft
course_version: 0.4.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 03 — Player

**Week 4 · checked off in lab**

In this exercise you replace the rolling ball with a character you control. You build a small level with platforms, then tune how the character feels to play. At the end you swap in a top-down controller to see a different style of movement.

## What you'll learn

- How a player controller turns input into movement
- What the **Input Reader** is, and why scripts ask it for input and not the keyboard
- What **game feel** is, and how a few numbers change it
- Three tricks most platformers use: **coyote time**, **jump buffering** and **short hops**
- How a platformer controller and a top-down controller differ

## Part 1 — Start the scene

1. Open `Ex02_Events` from `Assets/Scenes/Exercises`.
2. Choose **File → Save As…** and save it in the same folder as `Ex03_Player`.
3. Delete the `Ball`.
4. Delete the `Scene Changer`. It restarts the scene when you press Space, and Space is about to become the jump button.

## Part 2 — Rebuild the level

**The ground**

1. Select `Ramp` and rename it `Ground`.
2. Set its **Transform** to:
   - Position: `0, -1, 0`
   - Rotation: `0, 0, 0`
   - Scale: `18, 0.5, 1`

**Walls**, so the character can't leave the screen:

1. Create a **Square** sprite named `Wall Left`. Position `-8.75, 2, 0`, Scale `0.5, 10, 1`. Add a **Box Collider 2D**.
2. Duplicate it (**Ctrl+D**), name the copy `Wall Right`, and set its Position to `8.75, 2, 0`.

**Platforms**

1. Create a **Square** sprite named `Platform A`. Position `-3, 0.75, 0`, Scale `3, 0.5, 1`. Add a **Box Collider 2D**.
2. Duplicate it, name the copy `Platform B`, and set its Position to `1.5, 2.5, 0`.

**Move the pickups, door and text**

| Object | Position | Scale |
|---|---|---|
| `Coin` | `-6, 0, 0` | unchanged |
| `Coin (1)` | `-3, 1.75, 0` | unchanged |
| `Key` | `1.5, 3.5, 0` | unchanged |
| `Door` | `4.5, 3.25, 0` | `0.5, 8, 1` |
| `Score Text` | `-6, 4.25, 0` | unchanged |

**A treasure behind the door**

1. Duplicate a coin and name the copy `Treasure`. Position `7, 0, 0`, Scale `1, 1, 1`.
2. In its **Collectible** component, set **Amount** to `10`.

## Part 3 — Create the player

1. Choose **GameObject → 2D Object → Sprites → Capsule**. Name it `Player`.
2. Set its Position to `-7, 1, 0` and give it a color.
3. Set its **Tag** to **Player**, so it can collect things.
4. Add a **Capsule Collider 2D**.
5. Add the **Platformer Controller 2D** component. A **Rigidbody 2D** is added with it.
6. Look at the controller's **Input** field. It should already hold `InputReader`. If it's empty, drag `InputReader` in from `Assets/_Course/Core/Input`.

Press **Play** and click in the Game view.

| Action | Keyboard | Gamepad |
|---|---|---|
| Move | **A / D** or the **arrow keys** | Left stick |
| Jump | **Space** | Bottom face button |

Collect the coins, get the key from the top platform, and go through the door to the treasure.

## Part 4 — Where the input comes from

The controller never checks the keyboard. It asks the **Input Reader**: "which way is Move pointing?" and "tell me when Jump is pressed."

1. In the Project window, open `Assets/_Course/Core/Input` and double-click `InputSystem_Actions`.
2. Select the **Player** action map, then the **Move** action. Its bindings include WASD, the arrow keys and the gamepad's left stick.
3. Select **Jump**. Its bindings include Space and the gamepad's bottom button.
4. Close the window without changing anything.

Because the controller only knows "Move" and "Jump", it works with every device in that list. If a gamepad is available, plug it in and play. No settings need to change.

## Part 5 — Tune the game feel

**Game feel** is how the controls feel in your hands: heavy or light, sharp or slippery. It comes from a handful of numbers on the controller.

Select `Player`, press **Play**, and change the values below while the game runs. Change one at a time, and put each back before trying the next.

| Setting | Try | What changes |
|---|---|---|
| **Max Speed** | `3`, then `12` | How fast the character runs |
| **Acceleration** and **Deceleration** | `10` each | The character takes time to speed up and slides to a stop, like ice |
| **Acceleration** and **Deceleration** | `500` each | The character starts and stops at once |
| **Air Control** | `0`, then `1` | How much you can steer in mid-air |
| **Jump Height** | `1.5`, then `5` | How high a full jump goes, in units |
| **Gravity Scale** | `1`, then `6` | Floaty jumps, then fast and heavy ones |
| **Extra Air Jumps** | `1` | A double jump |

> **Values changed during Play are lost when you stop.** To keep them: while still playing, click the **⋮** menu on the component and choose **Copy Component**. Stop the game, then choose **⋮ → Paste Component Values**.

### Three tricks that make jumping feel fair

Players don't press buttons at exactly the right moment. These settings forgive small mistakes. Set each one to `0` to feel the game without it, then put it back.

1. **Coyote Time** (default `0.1`). Run off the edge of a platform and press Jump just after leaving it. With coyote time, the jump still works. Set it to `0` and the same press does nothing.
2. **Jump Buffer** (default `0.1`). Jump, and press Jump again just before landing. With a buffer, the character jumps again the moment it lands. Set it to `0` and the early press is ignored.
3. **Short Hop Speed Kept** (default `0.5`). Tap Jump quickly, then hold it down. A tap gives a low hop; a hold gives a full jump. Set it to `1` and every jump is the same height.

When you've found values you like, copy them and paste them after stopping, as described above.

## Part 6 — A top-down version

The same level, seen as if from above, with a different controller.

1. Choose **File → Save As…** and save the scene as `Ex03_TopDown`.
2. Select `Player`. On the **Platformer Controller 2D**, click **⋮ → Remove Component**.
3. Add the **Top Down Controller 2D** component. Check that its **Input** field holds `InputReader`.

Press **Play**. The character now moves in all four directions with **W A S D**, and there is no gravity or jumping. The ground, walls and platforms are now all just walls.

4. Change **Facing** to **Rotate To Movement** and play again. The character turns to point the way it moves.
5. Move the coins, key and treasure to places that make sense for a top-down room.

The pickups, the score, the key and the door all work exactly as before. Nothing about them had to change, because they never knew what kind of player was collecting them.

## Check-off

Show your instructor:

- [ ] In `Ex03_Player`, the character runs, jumps, collects the coins and key, and reaches the treasure.
- [ ] You changed at least three movement settings from their defaults, and can say why.
- [ ] You can show what coyote time and jump buffering do by turning each one off.
- [ ] In `Ex03_TopDown`, the character moves in all directions and can still collect everything.
- [ ] You can explain what the Input Reader is for.

## If something goes wrong

| What you see | What to do |
|---|---|
| The scene restarts when you press Space | Delete the `Scene Changer` object. |
| The character doesn't move | Click in the Game view. Check that the controller's **Input** field holds `InputReader`. |
| The character falls through the ground | The player needs a **Capsule Collider 2D**, and the ground needs a **Box Collider 2D**. |
| The character can't jump | Check that **Ground Layers** is set to **Everything**, and that **Jump Height** isn't `0`. |
| The character can jump over the door | Check the door's Position and Scale against the table in Part 2. |
| A red message says "Input is empty" | Drag `InputReader` from `Assets/_Course/Core/Input` into the controller's **Input** field. |
