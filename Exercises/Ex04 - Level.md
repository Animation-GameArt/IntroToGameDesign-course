---
title: "Exercise 04 — Level"
course: GAME 1303
week: 5
status: draft
course_version: 0.7.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 04 — Level

**Week 5 · checked off in lab**

In this exercise your level grows past the edge of the screen. You paint new ground with a Tilemap, add a pit and spikes, place a checkpoint, and give the player a camera that follows. Then you design two short sections of your own: one that teaches, and one that tests.

## What you'll learn

- How to paint a level with a **Tilemap**
- How **hazards** and **checkpoints** set the cost of a mistake
- How a **Cinemachine** camera follows the player and stays inside the level
- How to end a level with a **Trigger Zone** and an event
- How to design a **teach beat** and a **test beat**

## Part 1 — Start the scene

1. Open `Ex03_Player` and choose **File → Save As…**. Save it as `Ex04_Level`.
2. Delete `Wall Right`. The level is about to continue past it.
3. In `Assets/Scenes/Exercises`, create a folder named `Ex04_Data`.

## Part 2 — A pit, and a way back

1. Select `Player` and add the **Respawner** component. It remembers where the player started.
2. Create an empty GameObject named `Pit`. Set its Position to `20, -8, 0`.
3. Add a **Box Collider 2D**. Tick **Is Trigger** and set its **Size** to `100, 2`.
4. Add the **Kill Zone** component.

Press **Play** and walk off the right end of the ground. The player falls, touches the pit, and is back at the start.

## Part 3 — Paint the ground with a Tilemap

**Make a tile**

A tile is made from a sprite **asset**: a file in the Project window. A sprite object in the Hierarchy won't work.

1. In the **Project** window, open `Ex04_Data`. Right-click an empty part of the folder and choose **Create → 2D → Sprites → Square**. A new file appears in the folder. Name it `GroundTile`.
2. Choose **Window → 2D → Tile Palette**.
3. In the Tile Palette, open the palette dropdown and choose **Create New Palette**. Name it `Ex04 Palette` and save it in `Ex04_Data`.
4. Drag `GroundTile` from the **Project** window into the empty palette. A dialog asks where to save the tile: choose `Ex04_Data`.

> **Check:** `Ex04_Data` now holds three things: the `GroundTile` sprite, a `GroundTile` tile, and `Ex04 Palette`. If no dialog appeared in step 4, the tile wasn't made. Check that you dragged the file from the Project window.

**Make the Tilemap**

1. Choose **GameObject → 2D Object → Tilemap → Rectangular**. This creates a `Grid` with a `Tilemap` inside it.
2. Rename the Tilemap `Ground Tiles`.
3. Select `Grid` and set its Position to `0, 0.25, 0`. This lines the tiles up with the ground you already have.
4. Select `Ground Tiles`. In the **Tilemap** component, pick a **Color** for your ground.

**Paint**

1. In the Tile Palette, check that **Active Target** is `Ground Tiles`. Select the **Paint** tool (the brush, or press **B**) and click your tile. When you move the mouse over the Scene view, you should see the tile itself under the cursor, not only an outline.
2. In the Scene view, paint a row of tiles that continues the ground to the right, starting where `Ground` ends. The top of the tiles should be level with the top of `Ground`.
3. Paint this layout, counting tiles from left to right:

| Section | Tiles | What to paint |
|---|---|---|
| Run-up | 8 | Ground |
| Small gap | 2 | Nothing on the ground row. Paint 2 tiles one row lower, so there is a floor in the gap |
| Middle | 8 | Ground |
| Big gap | 4 | Nothing at all |
| Landing | 6 | Ground |
| Spike run | 8 | Ground |
| Finish | 6 | Ground |

Use the **Erase** tool to remove a tile.

**Make it solid**

1. Select `Ground Tiles` and add a **Tilemap Collider 2D**.
2. Add a **Composite Collider 2D**. A **Rigidbody 2D** is added with it: set its **Body Type** to **Static**.
3. On the **Tilemap Collider 2D**, set **Composite Operation** to **Merge**. This joins the tiles into one smooth shape, so the player doesn't catch on the seams.

Press **Play**. Run to the right. The small gap has a floor, so falling in costs nothing. The big gap drops into the pit.

## Part 4 — Spikes

1. In the Hierarchy, right-click `Grid` and choose **2D Object → Tilemap → Rectangular**. Name the new Tilemap `Hazard Tiles`.
2. In its **Tilemap** component, set the **Color** to red.
3. In the Tile Palette, change **Active Target** to `Hazard Tiles`.
4. In the middle of the spike run, paint 2 tiles **on top of** the ground, one row above it.
5. Select `Hazard Tiles`. Add a **Tilemap Collider 2D** and tick **Is Trigger**.
6. Add the **Kill Zone** component.

Press **Play**. Touching the red tiles sends the player back to the start. Jumping over them is safe.

## Part 5 — A checkpoint

Going all the way back to the start after every mistake gets old fast.

1. Create a **Square** sprite named `Checkpoint`. Set its Scale to `0.3, 2, 1` and give it a grey color.
2. Stand it on the ground in the middle section, a few tiles before the big gap.
3. Add a **Box Collider 2D** and tick **Is Trigger**.
4. Add the **Checkpoint** component. Drag the `Checkpoint` object itself into the **Indicator** field.

Press **Play**. Touch the checkpoint: it turns green. Now fall into the big gap. You come back at the checkpoint, not the start.

## Part 6 — A camera that follows

1. In the Hierarchy, select `Player`. Then choose **Right Click → Cinemachine → Targeted Cameras → 2D Camera**.
2. Select the new Cinemachine camera. Check that **Tracking Target** is `Player`. If it's empty, drag `Player` in.
3. Under **Lens**, set **Orthographic Size** to `5`.

Press **Play**. The camera follows the player through the level. It also shows empty space past the left wall and below the ground, which the next steps fix.

**Keep the camera inside the level**

1. Create an empty GameObject named `Camera Bounds`. Set its Position to `22, 1, 0`.
2. Add a **Box Collider 2D**. Tick **Is Trigger** and set its **Size** to `64, 12`.
3. Select the Cinemachine camera. Click **Add Extension** and choose **Cinemachine Confiner 2D**.
4. Drag `Camera Bounds` into the confiner's **Bounding Shape 2D** field.

If your level is longer or shorter than the bounds, change the collider's Size and the object's Position until the box covers the whole level.

**Keep the score on screen**

The score text is in the world, so the camera leaves it behind.

1. In the Hierarchy, drag `Score Text` onto `Main Camera`, so it becomes a child of the camera.
2. Set its Position to `-6, 4.25, 10`.

It now travels with the camera. In Exercise 06 you'll replace it with a real HUD.

## Part 7 — A goal

1. In `Ex04_Data`, choose **Create → Collin Game → Events → Void Event Channel**. Name it `LevelCompleted`.
2. Create a **Square** sprite named `Goal`. Give it a bright color and stand it at the far end of the finish section.
3. Add a **Box Collider 2D** and tick **Is Trigger**.
4. Add the **Trigger Zone** component. Tick **Only Once**, and drag `LevelCompleted` into **Raise On Enter**.

The goal now announces that the level is complete. Something has to react.

5. Create an empty GameObject named `Scene Changer`. Add the **Scene Changer** component and set **Scene Name** to `Ex04_Level`. Leave **Load On Action** empty.
6. On the same object, add a **Void Event Listener**. Set its **Channel** to `LevelCompleted`.
7. Under **Response**, click **+**, drag the `Scene Changer` object into the field, and choose **SceneChanger → Load**.
8. Add `Ex04_Level` to the Scene List (**File → Build Profiles → Open Scene List → Add Open Scenes**).

Press **Play** and reach the goal. The level restarts. In Exercise 06, the same event will show a win screen.

## Part 8 — Design a teach beat and a test beat

The layout you painted already has one pair. The small gap is a **teach beat**: the player learns to jump a gap, and failing costs nothing. The big gap is the **test beat**: the same skill, with the pit below.

Now design a pair of your own for the spikes.

1. **Teach.** Before the spike run, add a place where the player meets a spike with no real risk. For example, one spike tile with plenty of room, right after a checkpoint.
2. **Test.** Later, make the player use what they learned under pressure. For example, spikes on both sides of a narrow landing.
3. Add or move checkpoints so that failing the test doesn't mean replaying the teaching.
4. Play it, then ask someone else to play it. Watch where they fail. Don't help.

You can repaint anything, make the level longer, and add coins to guide the player. A trail of coins is a good way to show where to jump.

## Part 9 — Experiment with the camera

Select the Cinemachine camera and find its **Position Composer** settings. Try each of these while playing.

| Setting | Try | What changes |
|---|---|---|
| **Damping** | `0`, then `3` | The camera is locked to the player, then drifts behind |
| **Dead Zone** | Make it larger | The player can move a little without the camera moving |
| **Lookahead Time** | `0.5` | The camera shifts ahead of the player, in the direction they move |

## Check-off

Show your instructor:

- [ ] The level continues past the first screen on a Tilemap, and the camera follows the player.
- [ ] The camera never shows past the edges of the level.
- [ ] The pit and the spikes send the player back, and the checkpoint changes where they come back.
- [ ] Reaching the goal restarts the level.
- [ ] You can point to your own teach beat and test beat, and say what each one is for.

## If something goes wrong

| What you see | What to do |
|---|---|
| The player falls through the tiles | `Ground Tiles` needs a **Tilemap Collider 2D**. Check that **Is Trigger** is not ticked on it. |
| The tiles don't line up with `Ground` | Check that `Grid` is at Position `0, 0.25, 0`. |
| Painting shows only an outline and places nothing | The palette has no real tile in it. `Ex04_Data` must hold a `GroundTile` sprite **and** a `GroundTile` tile. If it doesn't, delete `Ex04 Palette` and redo the "Make a tile" steps in Part 3. |
| Painting does nothing | Check **Active Target** in the Tile Palette, and that the Paint tool and a tile are selected. |
| The spikes are solid and don't hurt | Tick **Is Trigger** on the `Hazard Tiles` collider, and check it has a **Kill Zone**. |
| The checkpoint doesn't turn green | Check that `Player` has a **Respawner**, and that the checkpoint's collider has **Is Trigger** ticked. |
| The camera doesn't move | Check that the Cinemachine camera's **Tracking Target** is `Player`. |
| The camera jumps or sticks at the edges | Make `Camera Bounds` bigger. It must be taller than the camera's view, which is 10 units. |
| The player can't jump after the camera was added | The `Camera Bounds` collider must have **Is Trigger** ticked. |
