---
title: "Top-Down Adventure Kit"
course: GAME 1303
status: draft
course_version: 0.12.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Top-Down Adventure Kit

The Top-Down Adventure Kit is a starting point for games seen from above in which the player explores, fights and finds things, in the style of the early Zelda games. It adds a sword attack, enemies that chase, knockback, keys and locked doors, signs and people to talk to, and a camera that moves room by room. The sample is a small dungeon of three rooms.

It builds on the Top Down Controller 2D from Exercise 03.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Walking in eight directions, with a sword swing in the direction you face | Bows, magic, or switching weapons (a Shooter 2D from the Arcade Classic Kit can fire arrows) |
| Enemies that wander, notice you, chase you and give up | Bosses with attack patterns |
| Knockback when anything is hit | Enemies that block or dodge |
| Hearts, coins, keys and locked doors | An inventory screen or shops |
| Signs, people and chests that show text when you press Interact | Branching conversations (the visual novel kit uses Yarn Spinner) |
| A camera that stays inside each room, and enemies that come back when you return | A scrolling world map or a minimap |
| A HUD with a row of hearts and a message box | Saving progress between sessions |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Top-Down Adventure Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/TopDownAdventure/Sample/Scenes`, add these scenes, next to each other and in this order: `Adventure_Menu`, `Adventure_Dungeon`, `Adventure_Win`.
4. Open `Adventure_Menu` and press **Play**.

Play the sample through once before you change anything.

| Action | Keyboard | Gamepad |
|---|---|---|
| Move | **WASD** or arrow keys | Left stick |
| Sword | **Enter** or left mouse button | Left face button |
| Read a sign, talk, open a chest | **E** | Top face button |
| Pause | **Esc** | **Start** |

## What's in the sample

| Prefab | What it is | Settings worth changing |
|---|---|---|
| `Player` | The hero: Top Down Controller 2D, Health, Respawner, Knockback 2D and Melee Attack 2D | **Max Speed**; **Max Health**; **Reach**, **Radius** and **Damage** on Melee Attack 2D |
| `Slime` | Wanders slowly, chases when it sees you, hurts on touch, takes 2 hits | **Notice Range**, **Chase Speed**, Health **Max Health** |
| `Bat` | Fast and flies over everything: it doesn't need to see you | **Chase Speed**, **Needs Line Of Sight** (off) |
| `Coin`, `Heart`, `Key` | Collectibles: add to `Coins`, heal 1, add to `Keys` | **Amount**, **Heal** |
| `Locked Door` | Opens when touched with a key, and uses the key up | **Keys Needed**, **Use Up Keys** |
| `Sign` | Shows its lines one at a time when you press Interact | **Lines** |
| `Treasure Chest` | Shows a line, then raises `DungeonCleared` | **Lines**, **On Used** |
| `Room` | A Camera Room 2D: the camera stays inside it while you're in it | The size of its Box Collider 2D; **Room Contents** |
| `Level Systems` | HUD, pause menu, win screen, camera | |

Select the `Player` in the Scene view to see the circle the sword reaches. Select an enemy to see how far it wanders (blue), when it notices you (yellow) and when it gives up (red).

## How the sample fits together

**Fighting.** Pressing Attack swings the sword: everything tagged `Enemy` with Health inside the red circle takes damage and, if it has a Knockback 2D, is pushed away. Enemies hurt the player with Damage On Touch, and the player's Knockback 2D pushes the player away from whatever touched them. Knockback briefly switches off the movement scripts, so the push isn't cancelled straight away.

**Health and hearts.** The player's Health writes to `PlayerHealth`. The HUD's **UI Heart Row** draws one heart per point of **Max Hearts**, filled up to `PlayerHealth`. When health runs out, the Respawner sends the player back to the last Checkpoint with full health.

**Keys and doors.** A Key is a Collectible that adds 1 to `Keys`. A Locked Door checks `Keys` when touched. Without enough keys, it writes "Locked." to `Message`, and the HUD's **UI Message Box** shows it for a few seconds.

**Signs.** An Interactable 2D has a trigger area. While the player stands in it, Interact shows the next line in `Message`. After the last line, the box closes.

**Rooms.** Each `Room` covers one screen-sized area with a trigger. When the player walks in, its Camera Room 2D tells the Cinemachine Confiner 2D to keep the camera inside that room. Each room's enemies are under one object, dragged into **Room Contents**: they're switched off while you're elsewhere, and come back when you return.

**Winning.** The Treasure Chest raises `DungeonCleared`, which shows the win screen.

## Start your own game

**[Top-Down Adventure Kit — Build Your Game](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit%20-%20Build%20Your%20Game.md)** takes you from the decisions table on page 10 of your ten-pager to your finished game, step by step, with checks for First Playable, Alpha and Beta. The steps below are the short version.

1. Create a new 2D scene in `Assets/_Game/Scenes`.
2. Drag in `Level Systems` and `Player` from the kit's `Sample/Prefabs`.
3. Paint the floor and walls with a Tilemap, as in Exercise 04: walls on their own Tilemap with a **Tilemap Collider 2D** and **Composite Collider 2D**.
4. Add a `Room` for each screen of your level, sized to cover it exactly. Rooms may touch; they shouldn't overlap.
5. Add enemies, keys, doors and signs from the prefabs.
6. Press **Play** and adjust.

For a game that's one big area instead of rooms, use a single `Room` covering the whole level, or remove the Confiner 2D so the camera follows freely.

### Changing a prefab

Make a **Prefab Variant** (right-click the prefab → **Create → Prefab Variant**), move it to `Assets/_Game/Prefabs`, and change the variant.

## Recipes

**A tougher enemy.** A `Slime` variant with Max Health `4`, a different sprite, and **Damage** `2` on its Damage On Touch.

**An enemy that guards one spot.** Set **Wander Speed** to `0`. It stands still until it notices you, and returns there afterwards.

**A key that appears when the enemies are beaten.** Place a `Key` in the room and untick it in the Inspector, so it starts hidden. On the last enemy's Health **On Died**, drag in the Key and choose **GameObject → SetActive**, ticked. Keep the Key outside **Room Contents**.

**A person to talk to.** A `Sign` variant with a character sprite and several **Lines**.

**A lever that opens a door.** An `Interactable 2D` with **Only Once** ticked. In **On Used**, drag in the door and choose **KeyDoor2D → Open**. Set the door's **Keys Needed** to `0` only if touching it should also open it.

**Music for each room.** On a Room's **On Entered**, add **MusicPlayer → Play** with that room's music, as in Exercise 07.

**A sword sound and a shake.** On the player's Melee Attack 2D, add a **SoundEffect → Play** to **On Swing**, and **CameraShake → Shake** and **HitStop → Stop** to **On Hit**.

**A whole dungeon.** Copy the sample scene's layout: one `Room` per screen, a `Checkpoint` at each door, and a Locked Door between the areas you want the player to reach in order.

## If something goes wrong

| What you see | What to do |
|---|---|
| The sword doesn't hurt enemies | The enemy needs the tag `Enemy`, a Health component and a collider. Check the red circle reaches it |
| Enemies don't chase | Check **Chase Tag** is `Player` and the player has that tag. With **Needs Line Of Sight** on, walls must not be between you |
| Enemies can see through walls | Walls need a solid collider (not a trigger) on a layer in **Sight Blockers** |
| The player slides away after being hit | Lower **Force When Touched**, or **Stun Time**, on the player's Knockback 2D |
| The camera doesn't stay in the room | The Cinemachine Camera needs a **Cinemachine Confiner 2D**, and each Room's collider must have **Is Trigger** ticked |
| The camera jumps at the start | The player must start inside a Room |
| Keys come back when you return to a room | Keep keys outside **Room Contents**; only enemies should be inside |
| No hearts in the HUD | The HUD needs **UI Heart Row** with **Health** set to `PlayerHealth`, and the player's Health needs `PlayerHealth` in **Health Variable** |
| Pressing E does nothing at a sign | Stand inside its trigger area. Check its **Input** field and the `Player` tag |
