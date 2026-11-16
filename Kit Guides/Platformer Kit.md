---
title: "Platformer Kit"
course: GAME 1303
status: draft
course_version: 0.9.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Platformer Kit

The Platformer Kit is a starting point for side-view run-and-jump games. It adds a few scripts to the ones you used in the exercises, a set of ready-made prefabs, and a small sample game with two levels that you can play, take apart and build on.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Running and jumping, with every setting from Exercise 03 | Wall jumps, dashes, ladders, swimming |
| Stomping on enemies | Shooting or melee attacks |
| Walking and flying enemies | Bosses |
| Moving platforms, one-way platforms, springs | Slopes |
| Coins, hearts, keys and locks | An inventory |
| Spikes, pits, checkpoints | |
| Lives, Game Over, a sequence of levels | Saving progress between sessions |
| A HUD, pause menu, main menu and credits | |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Platformer Kit package from the course project's **Releases** page.
2. With your project open in Unity, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/Platformer/Sample/Scenes`, add these four scenes, next to each other and in this order:
   1. `Platformer_Menu`
   2. `Platformer_Level1`
   3. `Platformer_Level2`
   4. `Platformer_Win`
4. Open `Platformer_Menu` and press **Play**.

Play the sample through once before you change anything.

## What's in the sample

Open `Platformer_Level1` and click through the Hierarchy. Everything in the level is one of these prefabs, from `Sample/Prefabs`.

| Prefab | What it is | Settings worth changing |
|---|---|---|
| `Player` | The character: controller, health, respawning, sprite animation | Everything on **Platformer Controller 2D**; **Max Health** |
| `Coin` | Adds 1 to `Coins` | **Amount** |
| `Heart` | Gives back 1 health | **Heal** |
| `Key` and `Lock` | The key raises `KeyCollected`; the lock hears it and disappears | |
| `Goal Gem` | Raises `LevelCompleted` | |
| `Spikes` | Costs health on touch | **Damage** |
| `Spring` | Launches the player | **Bounce Height** |
| `One-Way Platform` | Can be jumped through from below | |
| `Moving Platform` | Carries the player along a path | **Stops**, **Speed**, **Wait At Stops** |
| `Checkpoint` | Where the player returns after dying | |
| `Walker` | Patrols; can be stomped; hurts from the side | **Patrol Speed**, **Chase Range**, **Bounce Height** |
| `Flyer` | Flies along a path; hurts on touch | **Stops**, **Speed** |
| `Level Systems` | The HUD, pause menu, Level Complete and Game Over screens, the rules and the pit | |

Select a `Moving Platform` or a `Flyer` in the Scene view to see its path drawn as a line.

## How the sample fits together

It's built the way the exercises were: objects announce things, and other objects listen.

**Losing a life.** When the player's Health runs out, it does two things. It subtracts 1 from the `Lives` variable, and the Respawner sends the player back to the last checkpoint. In `Level Systems`, `Game Rules` watches `Lives`. When it reaches 0, it raises the `GameOver` event, and the Game Over screen, which listens for that event, appears.

**Finishing a level.** The `Goal Gem` raises `LevelCompleted`. The Level Complete screen listens for it and appears. Its **Next Level** button loads whichever scene comes next in the Scene List, so the order of that list is the order of your levels.

**Carrying things between levels.** `Coins` and `Lives` are variable assets, so they keep their values when the scene changes. They are reset in the menu scene, which is why going back to the menu starts a new game.

## Start your own game

1. In `Assets/_Game`, create a `Scenes` folder. Create a new 2D scene there for your first level.
2. Drag in `Level Systems` and `Player` from the kit's `Sample/Prefabs`.
3. Add a Cinemachine camera that follows the player, with bounds, as in Exercise 04.
4. Create a Tilemap for the ground, as in Exercise 04. Open **Window → 2D → Tile Palette** and choose `Platformer Palette` to paint with the kit's tiles.
5. Place prefabs to build the level.
6. Copy the menu and win scenes into `Assets/_Game/Scenes`, and put **your** scenes in the Scene List in the order they should be played.

### Changing a prefab

Don't edit the kit's prefabs: an update to the kit would undo your changes. Make a **variant**, which is your own version that still follows the original.

1. Right-click the prefab in the Project window and choose **Create → Prefab Variant**.
2. Move the variant into `Assets/_Game/Prefabs` and rename it.
3. Edit the variant, and use it in your levels.

### Using your own data

The sample's `Coins`, `Lives` and events are in the kit's `Sample/Data` folder, and you can use them as they are. If you want different starting values, such as 5 lives, create your own variables in `Assets/_Game/Data` and put them into your prefab variants.

## Recipes

**Change the character's look.** Make a variant of `Player`. Change the Sprite Renderer's sprite, and the **Idle**, **Walk** and **In Air** sprites on the Platformer Sprite Animator. The art pack has five characters in `Tiles/Characters`.

**A double jump.** On your `Player` variant, set **Extra Air Jumps** to `1`.

**An enemy that takes two stomps.** On a `Walker` variant, add a **Health** component with Max Health `2`, Invulnerable Time `0.3` and When Health Runs Out set to **Deactivate**.

**A faster or wider-ranging platform.** Change **Speed** and **Stops** on a `Moving Platform`. A second stop makes an L-shaped path, and **Path Mode: Loop** makes it circle.

**A door that needs ten coins.** Add an **Int Variable Condition** to a `Lock`: Variable `Coins`, Comparison **At Least**, Value `10`. Under **On Became True**, hide the lock with **GameObject → SetActive**, unticked.

**Enemies worth points.** On a `Walker` variant, set the Stompable Enemy's **Add To** to `Coins`, or to a score variable of your own.

**A level with no lives.** Remove the **Int Variable Condition** from `Game Rules` in a `Level Systems` variant. The player then respawns forever.

**Another theme.** The palette has sand and snow versions of the ground. Paint with those for a desert or winter level.

## If something goes wrong

| What you see | What to do |
|---|---|
| **Next Level** does nothing | Check the Scene List. The next level must come right after the current one. The Console says so if it's missing. |
| The player slides off moving platforms | The platform must have a **Waypoint Mover 2D**, and the player must use the **Platformer Controller 2D**. |
| Stomping hurts the player | The enemy needs **Stompable Enemy 2D** and must not also have **Damage On Touch**. Its collider must not be a trigger. |
| Thin lines show between tiles | Create a **Sprite Atlas** (**Create → 2D → Sprite Atlas**), add the art pack's `Tiles` folder to it, and set its Filter Mode to **Point** and its Padding to `4`. |
| Lives don't reset for a new game | Start from the menu scene. Its `Game Rules` object resets `Lives` and `Coins`. |
| The HUD is tiny or huge | Check that each UI Document's **Panel Settings** is `CoursePanelSettings`. |
