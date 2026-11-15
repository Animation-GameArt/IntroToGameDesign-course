---
title: "Exercise 05 — Combat"
course: GAME 1303
week: 6
status: draft
course_version: 0.7.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 05 — Combat

**Week 6 · checked off in lab**

> **Choose one version.** This is the **real-time** version: health, an enemy that patrols, and falling rocks. If your game is a puzzle, tactics or strategy game, do **Exercise 05 — Combat (Turn-Based)** instead.

In this exercise the player gets health. Spikes stop being instant and start costing a point each, an enemy patrols the level, and a spawner drops rocks.

## What you'll learn

- How **Health** works, and how it announces damage and death
- How **Damage On Touch** makes spikes, enemies and rocks hurt in the same way
- How an enemy uses **states**: patrol and chase
- What a **prefab** is, and how a **Spawner** reuses copies of one
- How to turn all of this into a difficulty choice

## Part 1 — Start the scene

1. Open `Ex04_Level` and choose **File → Save As…**. Save it as `Ex05_Combat`.
2. Select `Scene Changer` and change its **Scene Name** to `Ex05_Combat`.
3. Add `Ex05_Combat` to the Scene List.
4. In `Assets/Scenes/Exercises`, create a folder named `Ex05_Data`.

## Part 2 — Give the player health

1. In `Ex05_Data`, choose **Create → Collin Game → Variables → Int Variable**. Name it `PlayerHealth`.
2. Select `Player` and add the **Health** component:
   - **Max Health:** `3`
   - **Invulnerable Time:** `1`
   - **Health Variable:** drag in `PlayerHealth`

The player already has a **Respawner**. When a Respawner and Health are on the same object, running out of health sends the object back to its checkpoint with full health. You don't need to connect them.

**Show the health**

1. Under `Main Camera`, select `Score Text` and duplicate it (**Ctrl+D**). Name the copy `Health Text`.
2. Set its Position to `6, 4.25, 10`.
3. In its **Variable Label**, set **Variable** to `PlayerHealth` and **Format** to `Health: {0}`.

## Part 3 — Spikes that hurt

In Exercise 04 the spikes sent the player straight back. Now they take one point of health.

1. Select `Hazard Tiles`.
2. On the **Kill Zone** component, click **⋮ → Remove Component**.
3. Add the **Damage On Touch** component. Leave **Damage** at `1`.

Press **Play** and touch the spikes. Health drops by 1. For one second you can't be hurt again. That's the invulnerable time, and it gives the player a chance to get clear. Lose all three points and you're back at the checkpoint with full health.

The pit still has a **Kill Zone**, so falling in takes all your health at once.

## Part 4 — An enemy

1. Create a **Square** sprite named `Enemy`. Give it a color that stands out.
2. Place it on the ground in the landing section, after the big gap.
3. Add a **Box Collider 2D**.
4. Add the **Patrol Enemy 2D** component. A **Rigidbody 2D** is added with it.
5. Add the **Damage On Touch** component.

Press **Play**. The enemy walks back and forth. It turns around at the edge of the ground and at anything solid, and touching it costs health.

**Give it a second state**

1. Stop the game. On **Patrol Enemy 2D**, set **Chase Range** to `4`.
2. Press **Play**. In the Scene view, select `Enemy`. A circle shows its chase range.

The enemy now has two states. In **Patrol** it walks its route. When the player comes inside the circle, it switches to **Chase** and walks toward the player. When the player leaves, it goes back to patrolling. It won't walk off a ledge in either state.

## Part 5 — Falling rocks

**Make a rock prefab**

1. Create a **Circle** sprite named `Rock`. Set its Scale to `0.6, 0.6, 1` and give it a color.
2. Add a **Circle Collider 2D** and a **Rigidbody 2D**.
3. Add **Damage On Touch** and tick **Remove Self After Hit**.
4. Add the **Lifetime** component and set **Seconds** to `4`.
5. Drag `Rock` from the Hierarchy into `Ex05_Data` in the Project window. It turns blue in the Hierarchy: it's now a **prefab**, a template you can make copies of.
6. Delete `Rock` from the Hierarchy. The prefab stays in the Project window.

**Make the spawner**

1. Create an empty GameObject named `Rock Spawner`. Place it high above the finish section, at about `y = 7`.
2. Add the **Spawner** component:
   - **Prefab:** drag in `Rock` from `Ex05_Data`
   - **Interval:** `1.5`
   - **Max At Once:** `4`
3. Right-click `Rock Spawner` and choose **Create Empty** three times. Spread the three children out sideways above the finish section.
4. Select `Rock Spawner`. Drag the three children into its **Spawn Points** list.

Press **Play** and run through the finish section. Rocks fall from a random point every 1.5 seconds. A rock that hits you costs health and disappears. A rock that misses disappears after 4 seconds.

The Spawner never has more than 4 rocks in the scene. When a rock disappears it's only switched off, and the Spawner switches it back on for the next drop. Reusing objects like this is called **pooling**.

## Part 6 — A way to heal

1. Duplicate a coin and name the copy `Heart`. Give it a red color and place it somewhere worth reaching.
2. In its **Collectible** component, clear the **Add To** field (select it and press **Delete**).
3. Under **On Collected**, click **+**. Drag `Player` from the Hierarchy into the field, and choose **Health → Heal (int)**. Set the number to `1`.

Press **Play**, take some damage, and collect the heart.

## Part 7 — Make a difficulty decision

Everything here has a number that makes the level easier or harder. Change at least one on purpose.

| What | Setting | Question to ask |
|---|---|---|
| Player | **Max Health** | How many mistakes is the player allowed? |
| Player | **Invulnerable Time** | How long does the player get to recover? |
| Enemy | **Patrol Speed**, **Chase Range**, **Chase Speed** | Can the player get past by timing, or only by running? |
| Spawner | **Interval**, **Max At Once** | Is there a safe rhythm to learn? |
| Level | Where the checkpoint and the heart are | How much does one death cost? |

Decide what you want the player to feel in the finish section: tense, rushed, careful, relieved. Then set the numbers to get it, and test with another student.

## Check-off

Show your instructor:

- [ ] The player has 3 health, shown on screen, and loses it to spikes, the enemy and rocks.
- [ ] Running out of health returns the player to the checkpoint with full health.
- [ ] The enemy patrols, turns at ledges, and chases when the player is close.
- [ ] The spawner drops rocks from a prefab.
- [ ] You can say which number you changed for difficulty, and what you wanted the player to feel.

## If something goes wrong

| What you see | What to do |
|---|---|
| Spikes do nothing | `Hazard Tiles` needs **Damage On Touch**, and `Player` needs **Health**. |
| Health drops but the text doesn't change | Check that the player's **Health Variable** and the label's **Variable** both hold `PlayerHealth`. |
| The player isn't sent back at 0 health | Check that `Player` still has a **Respawner**. |
| The enemy walks off the ground | Check that **Turn At Ledges** is ticked. |
| The enemy spins in place | It has no room. Give it a wider stretch of ground. |
| No rocks appear | Check that the Spawner's **Prefab** field holds the `Rock` from the Project window, not from the Hierarchy. |
| Rocks pile up forever | The `Rock` prefab needs the **Lifetime** component. |
