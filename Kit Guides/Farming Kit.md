---
title: "Farming Kit"
course: GAME 1303
status: draft
course_version: 0.19.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Farming Kit

The Farming Kit is a starting point for farming and life sims: till the ground, plant seeds, water them, sleep, harvest, sell, and buy better seeds. Examples: Stardew Valley, Harvest Moon, the farming in many cozy games.

The sample is one small field. You have two weeks and $60 to earn $800. Mushrooms are cheap and quick, berry bushes keep giving, and the golden trees are expensive and slow but sell for a lot. Every day costs energy, and a crop that isn't watered doesn't grow.

A farming game is **several small systems that feed each other**: the clock, the soil, the crops, the bag and the shop. The kit gives you each one, so your time goes into what makes your farm different: its crops, its numbers and how it feels to play.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Days that end by sleeping, or when the clock runs out | Seasons, weather other than rain, a calendar |
| A field on a tilemap: till, water, plant, harvest, clear | Trees to chop, rocks to mine, fishing |
| Crops as assets, with growth stages, regrowing, and dying of thirst | Fertilizer, crop quality, giant crops |
| A hotbar inventory, chosen with number keys, the mouse wheel or a tap | Chests, crafting, dragging items between slots |
| A shop that buys and sells | Villagers, gifts, relationships, animals |
| Energy that refills each morning | Health, combat |
| A goal by a deadline, or no end at all | Saving a game in progress |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut. The Genre Map's advice stands: one field, three crops, one shop and a goal.

## Install the kit

1. Download the Farming Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/Farming/Sample/Scenes`, add `Farm_Menu` and `Farm_Game`, next to each other, in that order.
4. Open `Farm_Menu` and press **Play**.

| Action | Keyboard and mouse | Gamepad | Touch |
|---|---|---|---|
| Move | WASD or arrow keys | Left stick | — |
| Use the chosen item | Left click, or Enter | Left face button | Tap a cell next to the player |
| Choose an item | 1–8, or the mouse wheel | D-pad left and right | Tap a hotbar slot |
| Sleep, shop | E | Top face button | Tap the prompt |
| Pause | Esc | Start | — |

## How it works

- **The field** is a tilemap. Every cell painted on the `Farmland` tilemap can be tilled. Tilled and watered soil are drawn on a second tilemap, `Soil`, by the **Farm Field**.
- **Items** (assets) are everything in the bag. An item's **Use** says what it does on the field: **Till** (a hoe), **Water** (a watering can), **Plant** (seeds, with the **Crop** they grow), **Clear** (a shovel) or **Nothing** (a crop to sell). Each item has a **Buy Price** and a **Sell Price**.
- **Crops** (assets) have a sprite for each **stage**, and **Days Per Stage**. A crop grows one day for every night its soil was watered. The last stage is ripe. A crop with **Regrow Days** grows back after harvesting.
- **Farmer Tools 2D**, on the player, uses the chosen item on the cell in front of the player, or the cell clicked. A ripe crop is harvested whatever is chosen.
- **The Day Cycle** runs the clock. When the player sleeps, or the clock reaches 2 AM, the night passes: watered crops grow, the soil dries, it may rain, energy refills, and the player wakes up by the bed with a short report.
- **Interact Zones** are places to stand and press E: the bed (**Day Cycle → Sleep**) and the shop counter (**UI Shop → Open**).
- **Winning** is an **Int Variable Condition** from the Core scripts: Money at least 800. **Losing** is the Day Cycle's **Raise When Time Up**, after the last day.

## What's in the sample

| Asset | What it is | Worth changing |
|---|---|---|
| `Money`, `Day`, `Energy`, `Clock` | Variables for the HUD | `Money` and `Energy`: **Initial Value** |
| `Mushrooms`, `Berry Bush`, `Goldleaf` | Crops | **Days Per Stage**, **Regrow Days**, **Dies After Dry Days** |
| `Hoe`, `Watering Can`, `Shovel`, three seeds, three crops to sell | Items | **Buy Price**, **Sell Price** |
| `Farm Systems` | The Day Cycle, the screen, the shop, win and lose | **Last Day**, **Seconds Per Day**, the win amount |
| `Player` | The farmer: Top Down Controller 2D, Inventory, Farmer Tools 2D | **Starting Items**, **Energy Per Use** |

| Crop | Seeds cost | Watered days to ripe | Sells for | Notes |
|---|---|---|---|---|
| Mushrooms | $10 | 2 | $20 | Quick and safe |
| Berry Bush | $20 | 4 | $15 | Grows back every 2 days |
| Goldleaf | $60 | 6 | $150 | Slow, and dies after 2 dry days |

The sample's numbers were checked with a quick simulation. Planting only mushrooms all two weeks ends around $880; saving up and switching to Goldleaf in the first week ends above $1,000; doing nothing ends with the $60 you started with.

## Start your own game

1. Decide your crops (three is plenty) and what makes your farm yours: where it is, what grows, what the goal is.
2. Create an **Item** for each tool, each kind of seed and each crop to sell (**Create → Collin Game → Farming Kit → Item**), and a **Crop** for each crop (**Create → Collin Game → Farming Kit → Crop**). Seeds point at their Crop; the Crop points at the item it produces.
3. Open `Farm_Game`, **File → Save As…** into `Assets/_Game/Scenes`, and:
   - Paint your field on the `Farmland` tilemap, and your world around it.
   - On the player's **Inventory**, set **Starting Items**.
   - On `Shop`'s **UI Shop**, set **For Sale**.
   - Set your goal on `Win` and your deadline on the Day Cycle's **Last Day**.
4. Press **Play** and play a few days. Then change one number and play again.

### Designing the numbers

- **Play on paper first.** A row per day with money, energy and what's planted shows quickly whether a crop is worth it.
- **Each crop should be best at something.** In the sample, mushrooms are safest, berries need the least work, and Goldleaf earns the most if you can afford it and keep it watered.
- **Energy is the real limit.** It decides how big a field the player can keep watered. Raise it and the game gets easier.
- **Make the goal need a plan.** If planting the cheapest crop everywhere wins, players never make a decision.

## Recipes

**A game without an end.** Set **Last Day** to `0`, and leave the win condition out.

**Days that end only by sleeping.** Set **Seconds Per Day** to `0`. The clock stays at the morning.

**Night falls.** Add a sprite that covers the view (Unity's Square sprite, scaled up, as a child of the camera, high **Order in Layer**), and drag it into the Day Cycle's **Overlay**. The **Overlay Color** gradient tints it through the day.

**A crop that never dies.** Set **Dies After Dry Days** to `0`.

**A tool that costs no energy.** Set **Energy Per Use** to `0`, or leave **Energy** empty.

**More slots.** Change the Inventory's **Size**, up to 10. The hotbar grows to match.

**Sounds.** Each Farmer Tools 2D event (**On Till**, **On Water**, **On Plant**, **On Harvest**, **On Clear**, **On Nothing**) can play a Sound Effect.

## If something goes wrong

| What you see | What to do |
|---|---|
| Clicking does nothing | The cell must be within **Reach** of the player. Check the chosen item's **Use** |
| Can't till anywhere | The ground must be painted on the `Farmland` tilemap, and the Farm Field's **Farmland** set to it |
| Tilled soil doesn't show | Set the Farm Field's **Soil** and **Tilled Tile**; give `Soil` a higher **Order in Layer** than `Farmland` |
| Crops never grow | They only grow on nights their soil was watered. Sleep, or wait for the clock |
| Crops show under the soil | Raise the Farm Field's **Crop Order** above the `Soil` tilemap's **Order in Layer** |
| The cursor is in the wrong cell | Set **Feet Offset** on Farmer Tools 2D to where the player's feet are |
| "You're too tired" | Energy is used up. Sleep, or raise **Energy**'s Initial Value |
| The prompt never shows | The Interact Zone needs a trigger collider, and the player the **Player** tag and a Rigidbody 2D |
| The player can't move after the shop | Close it with **Leave**; the shop turns movement back on |
| The game ends at once | A win or lose condition is already true: check starting values |
