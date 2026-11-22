---
title: "Farming Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.19.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Farming Kit — Building the Sample

**For the instructor.** These steps build the kit's sample farm once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Farming Kit**, not this page.

Everything goes in `Assets/_Course/Kits/Farming/Sample/`, with folders `Data`, `Items`, `Crops`, `Tiles`, `Prefabs` and `Scenes`.

> [!tip] The quick way
> **Collin Game → Kit Samples → Build Farming Sample** builds everything on this page in a few seconds and opens the menu scene; press **Play**. It replaces the kit's `Sample` folder. The farm map is drawn from a text map; the camera shows all of it, so it needs no Cinemachine camera. Then work through **Test** to check it. Building by hand, step by step, is still the way to learn the kit, and checks this guide.

## Before you start

1. Pull the template project. It should be version 0.19.0 or later, with no red errors in the Console.
2. **Art.** Kenney's **Tiny Town** (`kenney_tiny-town/Tiles`) for the world, crops and tools, and **Tiny Dungeon** (`kenney_tiny-dungeon/Tiles`) for the farmer. Both are 16 pixels, so one tile is one unit.
3. Every UI Document uses `CoursePanelSettings`.

The Tiny Town tiles this page uses:

| Tile | What it is |
|---|---|
| `tile_0000`, `tile_0001`, `tile_0002` | Grass |
| `tile_0025` | Plain soil |
| `tile_0040` | Dirt path |
| `tile_0017` | Sprout |
| `tile_0029` | Mushrooms |
| `tile_0005` | Bush |
| `tile_0016`, `tile_0015` | Small green tree, small golden tree |
| `tile_0044`–`tile_0047`, `tile_0056`–`tile_0059` | Fences |
| `tile_0083` | Sign |
| `tile_0104` | Bed |
| `tile_0127`, `tile_0128`, `tile_0131` | Hoe, shovel, bucket of water |

## Part 1 — Data

In `Sample/Data`:

| Asset | Type | Initial value |
|---|---|---|
| `Money` | Int Variable | `60` |
| `Day` | Int Variable | `1` |
| `Energy` | Int Variable | `30` |
| `Clock` | String Variable | `6:00 AM` |
| `FarmWon`, `FarmLost` | Void Event Channel | |

## Part 2 — Soil tiles

In `Sample/Tiles`, two **Tile** assets (**Create → 2D → Tiles → Tile**):

| Tile | Sprite | Color |
|---|---|---|
| `Tilled Soil` | `tile_0025` | White |
| `Watered Soil` | `tile_0025` | `A68070` (a darker brown) |

## Part 3 — Items and crops

Create the items first, then the crops, then go back and set each seed's **Crop**.

**Items** in `Sample/Items` (**Create → Collin Game → Farming Kit → Item**):

| Item | Icon | Use | Crop | Used Up | Buy | Sell |
|---|---|---|---|---|---|---|
| `Hoe` | `tile_0127` | Till | — | No | `0` | `0` |
| `Watering Can` | `tile_0131` | Water | — | No | `0` | `0` |
| `Shovel` | `tile_0128` | Clear | — | No | `0` | `0` |
| `Mushroom Spores` | `tile_0017` | Plant | Mushrooms | Yes | `10` | `0` |
| `Berry Seeds` | `tile_0017` | Plant | Berry Bush | Yes | `20` | `0` |
| `Goldleaf Seeds` | `tile_0017` | Plant | Goldleaf | Yes | `60` | `0` |
| `Mushroom` | `tile_0029` | Nothing | — | No | `0` | `20` |
| `Berries` | `tile_0005` | Nothing | — | No | `0` | `15` |
| `Goldleaf` | `tile_0015` | Nothing | — | No | `0` | `150` |

Give each a one-line **Description**, such as *Quick and safe. Ready in 2 days.*

**Crops** in `Sample/Crops` (**Create → Collin Game → Farming Kit → Crop**):

| Crop | Stages | Days Per Stage | Produce | Amount | Regrow Days | Dies After Dry Days |
|---|---|---|---|---|---|---|
| `Mushrooms` | `tile_0017`, `tile_0029` | `2` | Mushroom | `1` | `0` | `0` |
| `Berry Bush` | `tile_0017`, `tile_0005` | `4` | Berries | `1` | `2` | `0` |
| `Goldleaf` | `tile_0017`, `tile_0016`, `tile_0015` | `3` | Goldleaf | `1` | `0` | `2` |

## Part 4 — The player

`Player` prefab, in `Sample/Prefabs`, tagged **Player**:

1. **Sprite Renderer**: Tiny Dungeon `tile_0098`, Order in Layer `20`.
2. **Rigidbody 2D**: Gravity Scale `0`, Freeze Rotation Z.
3. **Capsule Collider 2D**: Size `0.6, 0.5`, Offset `0, -0.2` (just the feet).
4. **Top Down Controller 2D**: Move Speed `4`, Facing **Flip Sprite**.
5. **Inventory**: Size `8`; Starting Items: Hoe `1`, Watering Can `1`, Shovel `1`, Mushroom Spores `5`.
6. **Farmer Tools 2D**: Reach `1.6`, Feet Offset `0, -0.3`, Energy `Energy`, Energy Per Use `1`.

## Part 5 — Farm Systems

An empty `Farm Systems`, made into a prefab, with these children:

**`Day Cycle`** — **Day Cycle**: Day `Day`, Last Day `14`, Seconds Per Day `240`, Start Hour `6`, End Hour `26`, Clock `Clock`; Player (set in the scene), Wake Up Point (set in the scene); Reset Each Morning `Energy`; Raise When Time Up `FarmLost`.

**`Win`** — **Int Variable Condition**: Variable `Money`, At Least `800`, Raise Event `FarmWon`. And a **Void Event Listener** on `FarmWon` → `Day Cycle`, **DayCycle → StopGame**.

**`Screen`** — UI Document `FarmHUD` (from `Kits/Farming/UI`), with:
- **UI Farm Screen**: Inventory (set in the scene), Day Cycle `Day Cycle`.
- **UI Shop**: Shop Name `General Store`; For Sale `Mushroom Spores`, `Berry Seeds`, `Goldleaf Seeds`; Money `Money`; Inventory (set in the scene).
- **UI Variable Binder**: `day-label` → `Day` → `Day {0} of 14`; `clock-label` → `Clock` → `{0}`; `money-label` → `Money` → `${0} / $800`; `energy-label` → `Energy` → `Energy: {0}`.

**`Reset`** — a **Variable Resetter** with `Money`, `Day`, `Energy` and `Clock`.

**`Pause Menu`**, **`Settings`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Won`** — UI Document `EndScreen`, hidden, shown on `FarmWon`; `score-label` → `Day` → `You made it on day {0}!`.

**`Lost`** — UI Document `GameOver`, hidden, shown on `FarmLost`; Try Again → **ReloadScene**.

## Part 6 — The farm (`Farm_Game`)

1. Main Camera: Orthographic, Size `5`. Add **Cinemachine Camera** following `Player`, with a **Cinemachine Confiner 2D** if the map is bigger than the view.
2. A **Grid** with three Tilemaps:
   - `Ground` (Order in Layer `0`): grass everywhere, with a dirt path from the house to the field and to the shop.
   - `Farmland` (Order in Layer `1`): grass (`tile_0000`) on a **4 × 4** block, the field. Add **Farm Field** to the Grid: Farmland `Farmland`, Soil `Soil`, Tilled Tile `Tilled Soil`, Watered Tile `Watered Soil`, Crop Order `5`, Crop Offset `0, 0`, Empty Soil Lasts `3`, Rain Chance `0.15`.
   - `Soil` (Order in Layer `2`): empty.
3. `Walls`: a fourth Tilemap with fences around the field (leaving a gap) and around the edge of the map, with a **Tilemap Collider 2D**.
4. `Bed`: `tile_0104`, Order `3`, with a child `Wake Up Point` just below it. Add a **Box Collider 2D** (Is Trigger, Size `1.6, 1.6`) and **Interact Zone 2D**: Prompt `E: Sleep`, On Used → `Day Cycle`, **DayCycle → Sleep**.
5. `Shop`: a sign (`tile_0083`) and a counter or small house from the Tiny Town tiles, with a trigger area in front and **Interact Zone 2D**: Prompt `E: Shop`, On Used → `Screen`, **UIShop → Open**.
6. `Player`, by the bed. And `Cursor`, at the top level of the scene (not a child of the player): Unity's **Square** sprite (**Create → 2D → Sprites → Square**), Scale `1`, Color white at 35% alpha, Order in Layer `15`. Drag it into the Player's Farmer Tools 2D → **Cursor**.
7. `Farm Systems`, with Day Cycle → **Player** `Player` and **Wake Up Point** `Wake Up Point`, and `Screen`'s **Inventory** fields set to the Player.
8. Optional: `Night`, a Square sprite as a child of the Main Camera, Scale `40, 25`, Order in Layer `100`, dragged into the Day Cycle's **Overlay**.

## Part 7 — Menu

`Farm_Menu`, like the Platformer sample's menu, with Play loading `Farm_Game`.

Scene List: `Farm_Menu`, `Farm_Game`.

## Part 8 — Test

- [ ] The HUD shows Day 1 of 14, 6:00 AM, $60 / $800, Energy: 30; the hotbar shows the hoe, watering can, shovel and 5 spores, with the hoe chosen.
- [ ] 1–8, the mouse wheel and clicking a slot choose an item; its name shows above the hotbar.
- [ ] The cursor shows on the cell in front of the player, or under the mouse within reach, and only over the field.
- [ ] The hoe tills grass in the field and nothing outside it; each use costs 1 energy.
- [ ] Spores plant only on tilled soil and go down by one; the watering can darkens the soil.
- [ ] At 0 energy, a message says to go to bed, and tools do nothing.
- [ ] E at the bed (or clicking the prompt) ends the day: the morning report shows, the player is by the bed, energy is 30 again, the day is 2.
- [ ] Watered crops grow one stage per Days Per Stage nights; unwatered ones don't; the soil is dry again each morning.
- [ ] Clicking a ripe crop with anything chosen harvests it into the bag; a full bag says so.
- [ ] Berry bushes go back to a sprout after harvesting, and are ripe again after 2 watered nights.
- [ ] Goldleaf left dry for 2 nights dies, and the report says so. Sometimes it rains, and the report says so.
- [ ] The shop opens with E; the player can't move and the clock stops; seeds you can't afford are grey; buying and selling change money and the bag; Leave closes it.
- [ ] The clock runs from 6:00 AM, and at 2 AM the day ends by itself.
- [ ] Reaching $800 shows the won screen; finishing day 14 without it shows the lost screen.
- [ ] On a touch screen (or the Device Simulator), tapping a cell next to the player uses the item, tapping a slot chooses it, and tapping the prompt sleeps or shops.
- [ ] Esc pauses, and the clock stops.

Note anything that fails, with the Console message.

## Part 9 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/Farming` and the Tiny Town and Tiny Dungeon art folders with **Assets → Export Package**, unticking Core and 2D scripts that Unity adds as dependencies.
