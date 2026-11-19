---
title: "Top-Down Adventure Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.12.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Top-Down Adventure Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Top-Down Adventure Kit**, not this page.

Everything goes in `Assets/_Course/Kits/TopDownAdventure/Sample/`, with folders `Data`, `Prefabs`, `Scenes` and `Tiles`.

## Before you start

1. Pull the template project. It should be version 0.12.0 or later, with no red errors in the Console.
2. **Art.** Download Kenney's **Tiny Dungeon** pack (link in `Assets/_Course/Art/Kenney/README.md`). Unzip it to `Assets/_Course/Art/Kenney/kenney_tiny-dungeon`, remove the non-Unity files, and choose **Collin Game → Art → Reapply Art Import Settings**. Its tiles are 16 pixels, so one tile is one unit. Push it, and I'll add it to `Course Credits`.
3. **Tags.** In **Project Settings → Tags and Layers**, add the tag `Enemy` if it isn't there.
4. **Panel Settings.** Every UI Document uses `CoursePanelSettings`. New UI Documents get it by themselves; **Collin Game → UI → Use Course Panel Settings in Open Scenes** fixes any that don't.

## Part 1 — Data

In `Sample/Data`:

| Asset | Type | Initial value |
|---|---|---|
| `PlayerHealth` | Int Variable | `5` |
| `Keys`, `Coins` | Int Variable | `0` |
| `Message` | String Variable | empty |
| `DungeonCleared` | Void Event Channel | |

## Part 2 — Prefabs

Build each in a new scene `Sample/Scenes/Adventure_Dungeon`, drag it into `Sample/Prefabs`, then delete it from the scene unless a step says to keep it.

### Player

1. Create a sprite from a Tiny Dungeon hero tile. Name it `Player`, tag it `Player`, and set its **Order in Layer** to `10`.
2. Add a **Circle Collider 2D**, Radius `0.35`, Offset `0, -0.1` (the feet).
3. Add **Top Down Controller 2D** (Max Speed `5`, Facing **Flip Sprite**). It adds the Rigidbody 2D.
4. Add **Health**: Max Health `5`, Invulnerable Time `1`, Health Variable `PlayerHealth`.
5. Add **Respawner** and **Knockback 2D** (defaults).
6. Add a child sprite `Swing` using a sword tile, pointing right, Order in Layer `11`.
7. Add **Melee Attack 2D**: Reach `0.8`, Radius `0.55`, Target Tag `Enemy`, Damage `1`, Knockback Force `8`, Swing Visual `Swing`.

### Slime

1. A sprite from a Tiny Dungeon slime tile, tag `Enemy`, Order in Layer `5`.
2. **Circle Collider 2D**, Radius `0.4`.
3. **Top Down Chaser 2D**: Wander Speed `0.8`, Wander Radius `1.5`, Notice Range `4`, Give Up Range `7`, Chase Speed `2`, Needs Line Of Sight ticked.
4. **Health**: Max Health `2`, Invulnerable Time `0.3`, When Health Runs Out **Destroy**.
5. **Knockback 2D**, **Damage On Touch** (Target Tag `Player`, Damage `1`).

### Bat

A **Slime** variant: a bat sprite, Chase Speed `3.5`, Wander Speed `2`, Needs Line Of Sight unticked, Max Health `1`.

### Pickups

| Prefab | Sprite | Components |
|---|---|---|
| `Coin` | Coin tile | Circle Collider 2D (trigger), **Collectible** (Add To `Coins`, Amount `1`) |
| `Heart` | Heart tile | Circle Collider 2D (trigger), **Collectible** (Heal `1`) |
| `Key` | Key tile | Circle Collider 2D (trigger), **Collectible** (Add To `Keys`, Amount `1`) |

### Locked Door

A door tile with a **Box Collider 2D** (not a trigger) covering the doorway, and **Key Door 2D**: Keys `Keys`, Keys Needed `1`, Use Up Keys ticked, Message Text `Message`.

### Sign and Treasure Chest

**Sign:** a sign tile with a solid **Box Collider 2D** on a child `Solid`, and on the root a **Box Collider 2D** trigger about twice the tile's size. Add **Interactable 2D**: Message Text `Message`, Lines `Swing your sword with Enter.` and `Find the key to open the door.`

**Treasure Chest:** the same layout with a chest tile. **Interactable 2D**: Lines `You found the treasure!`, Only Once ticked; On Used → `DungeonCleared` **Raise**.

### Room

An empty GameObject `Room` with a **Box Collider 2D**, Is Trigger ticked, Size `16 × 9` (one screen), and **Camera Room 2D**.

### Level Systems

An empty GameObject at `0, 0, 0` with these children:

Keep the cameras out of the prefab, in the level scene: the Main Camera with a **Cinemachine Brain**, and a **Cinemachine Camera** (Orthographic Size `4.5`, Tracking Target `Player`) with a **Position Composer** and a **Cinemachine Confiner 2D**. Leave the Confiner's Bounding Shape 2D empty; the Rooms fill it in.

**`HUD`** — UI Document, Source Asset `AdventureHUD` (from `Kits/TopDownAdventure/UI`), with:
- **UI Heart Row**: Health `PlayerHealth`, Max Hearts `5`.
- **UI Variable Binder**: `keys-label` → `Keys` → `Keys: {0}`; `coins-label` → `Coins` → `Coins: {0}`.
- **UI Message Box**: Message `Message`, Clear After `4`.

**`Pause Menu`** — as in the Platformer Kit sample (`PauseMenu`, UI Screen hidden, Pause Controller, UI Button Events for resume, restart and menu).

**`Win`** — a **Void Event Listener** on `DungeonCleared` → a **Scene Changer** with Scene Name `Adventure_Win` → **Load**.

**`Reset Data`** — a **Variable Resetter** with `Keys`, `Coins` and `Message`.

## Part 3 — The dungeon

Three rooms side by side, each 16 × 9 tiles:

| Room | Contents | Teaches |
|---|---|---|
| 1 — Entrance | The Player, a Sign, two Coins, a Checkpoint | Moving, reading signs |
| 2 — Slime room | Two Slimes under a `Room Contents` object, a Key, a Heart, a Checkpoint at the door | Fighting, knockback, keys |
| 3 — Treasure room | A Locked Door at its entrance, a Bat under `Room Contents`, the Treasure Chest | Locked doors, a faster enemy, winning |

1. Paint floors on one Tilemap and walls on another. Give the walls Tilemap a **Tilemap Collider 2D** with Composite Operation **Merge**, a **Composite Collider 2D**, and set its Rigidbody 2D to **Static**.
2. Leave a gap in the wall between rooms for the doorway.
3. Place one `Room` over each room, edges touching. In rooms 2 and 3, drag `Room Contents` into the Room's **Room Contents**.
4. Put the Player in room 1.

## Part 4 — Menu and win scenes

Build `Adventure_Menu` and `Adventure_Win` as in the Platformer Kit sample. The win screen shows `Coins: {0}`.

## Part 5 — Scene List

`Adventure_Menu`, `Adventure_Dungeon`, `Adventure_Win`, in that order.

## Part 6 — Test

- [ ] The hero moves in eight directions and faces the way they walk.
- [ ] The sword shows briefly in the direction faced, and hits slimes in front.
- [ ] A hit slime is pushed back; after 2 hits it disappears.
- [ ] A slime touching the hero costs a heart and pushes the hero back.
- [ ] Hearts in the HUD empty and refill with the Heart pickup.
- [ ] Losing every heart sends the hero to the last checkpoint with full hearts.
- [ ] Slimes don't notice the hero through walls; the bat does.
- [ ] Reading the sign shows each line, then closes.
- [ ] The locked door shows "Locked" without a key, and opens with one.
- [ ] The camera stays inside each room and moves when the hero walks through a doorway.
- [ ] Leaving room 2 and coming back brings the slimes back, but not the key.
- [ ] Opening the chest shows the win scene.
- [ ] Esc pauses; the sword and signs don't respond while paused.

Note anything that fails, with the Console message.

## Part 7 — Commit

Commit and push the `Sample` folder with its `.meta` files, and the Tiny Dungeon art folder.

## Later — Exporting the kit

Export `Assets/_Course/Kits/TopDownAdventure` and the Tiny Dungeon art folder with **Assets → Export Package**, unticking Core and 2D scripts that Unity adds as dependencies.
