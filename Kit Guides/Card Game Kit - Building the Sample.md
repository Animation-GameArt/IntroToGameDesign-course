---
title: "Card Game Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.21.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Card Game Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Card Game Kit**, not this page.

Everything goes in `Assets/_Course/Kits/CardGame/Sample/`, with folders `Data`, `Cards`, `Enemies` and `Scenes`.

## Before you start

1. Pull the template project. It should be version 0.21.0 or later, with no red errors in the Console.
2. **Art.** Run **Collin Game → Art → Reapply Art Import Settings** once, so Kenney's **Playing Cards Pack** (`kenney_playing-cards-pack/PNG/Cards (large)`) gets pixel-art settings. The enemies are from **Tiny Dungeon**.
3. Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data

In `Sample/Data`: `PlayerHealth` (Int Variable, `40`), `RunWon` and `RunLost` (Void Event Channels).

## Part 2 — Cards

In `Sample/Cards` (**Create → Collin Game → Card Game Kit → Card**). For every card: **Face** is the Kenney card named in the table, **Show Name** unticked, and one effect.

| Card | Face | Cost | Effect |
|---|---|---|---|
| `Spades 2` … `Spades 7` (six cards) | `card_spades_02` … `card_spades_07` | `1` | Damage, the card's number |
| `King of Spades` | `card_spades_K` | `2` | Damage `10` |
| `Diamonds 3` … `Diamonds 6` (four cards) | `card_diamonds_03` … `card_diamonds_06` | `1` | Block, the card's number |
| `Hearts 3`, `Hearts 4` | `card_hearts_03`, `card_hearts_04` | `1` | Heal, the card's number |
| `Clubs 2` | `card_clubs_02` | `1` | Draw `2` |
| `Jack of Clubs` | `card_clubs_J` | `0` | Energy `2` |

Fifteen cards. Making one and duplicating it (**Ctrl+D**) is quickest.

## Part 3 — Enemies

In `Sample/Enemies` (**Create → Collin Game → Card Game Kit → Enemy**):

| Enemy | Portrait (Tiny Dungeon) | Max Health | Moves |
|---|---|---|---|
| `Slime` | `tile_0108` | `28` | Attack `6`; Attack `6`; Block `4` |
| `Knight` | `tile_0096` | `42` | Block `10`; Attack `11`; Attack `8` |
| `Demon` | `tile_0110` | `62` | Attack `4` × `3` times; Block `10`; Attack `15` |

Random Order unticked for all three.

## Part 4 — Card Systems

An empty `Card Systems`, made into a prefab, with these children:

**`Battle`** — **Card Battle**: Deck: all fifteen cards; Max Health `40`, Energy Per Turn `3`, Hand Size `5`, Max Hand Size `10`, Player Health `PlayerHealth`; Enemies `Slime`, `Knight`, `Demon`; Heal Between Battles `10`; Enemy Turn Pause `0.6`; Pause Between Battles `1.5`; Raise On Win `RunWon`, Raise On Lose `RunLost`.

**`Screen`** — UI Document `CardBattle` (from `Kits/CardGame/UI`), with **UI Card Battle**: Battle `Battle`, Blank Card `card_empty`.

**`Reset`** — a **Variable Resetter** with `PlayerHealth`.

**`Pause Menu`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Won`** — UI Document `EndScreen`, hidden, shown on `RunWon`; `score-label` → `PlayerHealth` → `Health left: {0}`.

**`Lost`** — UI Document `GameOver`, hidden, shown on `RunLost`; Try Again → **ReloadScene**.

## Part 5 — Scenes

**`Cards_Game`**: a new 2D scene with a camera and `Card Systems`.

**`Cards_Menu`**: like the Platformer sample's menu, with Play loading `Cards_Game`.

Scene List: `Cards_Menu`, `Cards_Game`.

## Part 6 — Test

- [ ] The screen shows Battle 1 of 3, the Slime with 28 / 28 and *Next: Attack 6*, the player with 40 / 40 and Energy 3 / 3, five cards, Draw: 10 and Discard: 0.
- [ ] The cards are crisp pixel art; each shows its cost and its text underneath ("Deal 4", "Block 5", "Heal 3", "Draw 2 cards", "Gain 2 energy").
- [ ] Pointing at a card lifts it; clicking, tapping or pressing its number plays it; cards costing more than the energy left are faded and can't be played.
- [ ] Damage lowers the enemy's health; block shows under the health bar and is used up first.
- [ ] End Turn (or E, or Enter) discards the hand; the enemy makes the move it showed; a new hand is drawn and energy refills; the player's block is gone.
- [ ] The Demon's *Attack 4 x3* hits three times, one after another.
- [ ] When the draw pile runs out, the discard pile is shuffled into it.
- [ ] Beating an enemy heals 10 and starts the next battle after a moment.
- [ ] Beating the Demon shows the won screen with the health left; reaching 0 health shows the lost screen.
- [ ] End Turn is greyed out during the enemy's turn, and cards can't be played then.
- [ ] Esc pauses; nothing can be played while paused.
- [ ] **Balance:** play two runs carefully and one choosing cards at random. Note how each ends.

Note anything that fails, with the Console message.

## Part 7 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/CardGame`, the Playing Cards Pack and the Tiny Dungeon art folder with **Assets → Export Package**, unticking Core scripts that Unity adds as dependencies.
