---
title: "Turn-Based Battle Kit — Building the Sample"
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

# Turn-Based Battle Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Turn-Based Battle Kit**, not this page.

Everything goes in `Assets/_Course/Kits/TurnBasedBattle/Sample/`, with folders `Actions`, `Data`, `Prefabs` and `Scenes`.


> [!tip] The quick way
> **Collin Game → Kit Samples → Build Turn-Based Battle Sample** builds everything on this page in a few seconds and opens the menu scene; press **Play**. It replaces the kit's `Sample` folder. Then work through **Test** to check it. Building by hand, step by step, is still the way to learn the kit, and checks this guide.

## Before you start

1. Pull the template project. It should be version 0.12.0 or later, with no red errors in the Console.
2. **Art.** The sample uses Kenney's **Tiny Dungeon** pack, the same as the Top-Down Adventure Kit (`Assets/_Course/Art/Kenney/kenney_tiny-dungeon`). Scale the fighters up to `3` so they read well on the battle screen.
3. **Panel Settings.** Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data and actions

In `Sample/Data`:

| Asset | Type |
|---|---|
| `BattleStatus`, `BattleLog` | String Variable |
| `BattleRound` | Int Variable |
| `BattleWon`, `BattleLost` | Void Event Channel |

In `Sample/Actions`, create these with **Create → Collin Game → Turn-Based Battle Kit → Battle Action**:

| Asset | Effect | Target | Power | Accuracy | Uses | Description |
|---|---|---|---|---|---|---|
| `Slash` | Damage | One Opponent | `3` | `95` | `0` | A quick, reliable cut. |
| `Power Strike` | Damage | One Opponent | `6` | `70` | `0` | Hits hard, but often misses. |
| `Defend` | Defend | Self | `0` | `100` | `0` | Take half damage until your next turn. |
| `Potion` | Heal | Self | `5` | `100` | `2` | Recover 5 health. Two per battle. |
| `Staff` | Damage | One Opponent | `2` | `95` | `0` | A weak blow. |
| `Heal` | Heal | One Ally | `4` | `100` | `3` | Recover 4 health for one ally. |
| `Bite` | Damage | One Opponent | `2` | `90` | `0` | |
| `Club` | Damage | One Opponent | `4` | `85` | `0` | |
| `Roar` | Defend | Self | `0` | `100` | `0` | |
| `Firestorm` | Damage | All Opponents | `2` | `100` | `1` | Burns every enemy. Once per battle. |

## Part 2 — Prefabs

Build each in a new scene `Sample/Scenes/Battle_1`, drag it into `Sample/Prefabs`, then delete it from the scene unless a step says to keep it.

### Fighters

Each fighter is an empty GameObject with a child sprite `Sprite` (Scale `3`) and these components on the root:

| Component | Settings |
|---|---|
| **Turn Taker** | Display Name; Player Side ticked for Hero and Healer |
| **Health** | Max Health (below), **Invulnerable Time `0`**, When Health Runs Out **Deactivate** |
| **Battle Actor** | Controlled By, Actions, Attack, Defense (below) |
| **Health Bar 2D** | Fill: the bar's `Fill` child (below) |

| Prefab | Controlled By | Max Health | Attack | Defense | Actions |
|---|---|---|---|---|---|
| `Hero` | Player | `20` | `1` | `1` | Slash, Power Strike, Defend, Potion, Firestorm |
| `Healer` | Player | `14` | `0` | `0` | Staff, Heal, Defend |
| `Slime` | Computer | `8` | `0` | `0` | Bite |
| `Ogre` | Computer | `30` | `2` | `2` | Club, Roar |

**Health bar.** Under each fighter, a child `Health Bar` at `0, 1.6`, with two sprites from **Create → 2D → Sprites → Square**: `Background` (Scale `1.2 × 0.15`, dark grey, Order in Layer `20`) and `Fill` (same scale, green, Order in Layer `21`). Drag `Fill` into the Health Bar 2D's **Fill**.

Turn the opponents' sprites to face left (Flip X).

### Battle Systems

An empty GameObject at `0, 0, 0` with these children:

**`Turn Manager`** — **Turn Manager**: Turn Order filled in each scene; Start Automatically ticked; Pause Between Turns `0.6`; Status Text `BattleStatus`; Round Variable `BattleRound`; Raise On Player Won `BattleWon`; Raise On Player Lost `BattleLost`.

**`Battle Log`** — **Battle Log**: Log Text `BattleLog`, Lines To Keep `4`.

**`Battle Screen`** — UI Document, Source Asset `BattleUI` (from `Kits/TurnBasedBattle/UI`), with **UI Battle Menu** (defaults), and a **UI Variable Binder**: `status-label` → `BattleStatus` → `{0}`; `log-label` → `BattleLog` → `{0}`.

**`Pause Menu`** — as in the Platformer Kit sample.

**`Settings`** — as in the Platformer Kit sample (`Settings`, Sort Order `4`, UI Screen hidden, UI Settings, `back-button` hides it), with the Pause Menu's `settings-button` showing it.


**`Scene Changer`** — Scene Changer, Scene Name empty. **`To Menu`** — Scene Changer, Scene Name `Battle_Menu`.

**`Victory`** — UI Document `LevelComplete` (from `Kits/Platformer/UI`), Sort Order `2`, UI Screen hidden, a **Void Event Listener** on `BattleWon` → **UIScreen → Show**, buttons `next-button` → **SceneChanger → LoadNextScene**, `menu-button` → To Menu **Load**. Hide its coins label, or bind it to `BattleRound` with `Rounds: {0}`.

**`Defeat`** — UI Document `GameOver`, Sort Order `3`, UI Screen hidden, a **Void Event Listener** on `BattleLost` → **UIScreen → Show**, buttons `try-again-button` → **SceneChanger → ReloadScene**, `menu-button` → To Menu **Load**.

Keep one `Battle Systems` in the scene.

## Part 3 — Battles

Place the player's party on the left at about `x = -4` and the opponents on the right at about `x = 4`, a little above the screen's middle so the menu doesn't cover them. Put a simple floor or backdrop behind them.

| Scene | Party | Opponents | Turn Order | Teaches |
|---|---|---|---|---|
| `Battle_1` | Hero | Slime | Hero, Slime | Choosing an action |
| `Battle_2` | Hero, Healer | Slime, Slime (name them Slime A and Slime B) | Hero, Healer, Slime A, Slime B | Choosing targets, healing allies, Firestorm |
| `Battle_3` | Hero, Healer | Ogre | Hero, Healer, Ogre | Defending against a strong hit |

## Part 4 — Menu and win scenes

Build `Battle_Menu` and `Battle_Win` as in the Platformer Kit sample, without the coin count.

## Part 5 — Scene List

`Battle_Menu`, `Battle_1`, `Battle_2`, `Battle_3`, `Battle_Win`, in that order.

## Part 6 — Test

- [ ] The status shows the round and whose turn it is.
- [ ] On the Hero's turn the menu shows every action; Potion shows `(2)`.
- [ ] The mouse, the arrow keys with Enter, and a gamepad all choose actions.
- [ ] Selecting a button shows its description.
- [ ] With two slimes, Slash asks for a target; Back returns to the actions.
- [ ] Firestorm hits both slimes, and is greyed out after one use.
- [ ] Power Strike sometimes misses, and the log says so.
- [ ] Defend halves the next hit, and the log says "(defending)".
- [ ] The Healer can heal the Hero.
- [ ] The slime heals when low if given a heal action, and otherwise attacks.
- [ ] Health bars shrink from the right.
- [ ] A defeated fighter disappears and is skipped.
- [ ] Winning shows Victory; Next loads the next battle. Losing shows Defeat.
- [ ] Esc pauses, and the menu can't be used while paused.
- [ ] No "invulnerable" warnings in the Console.

Note anything that fails, with the Console message.

## Part 7 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/TurnBasedBattle` and the Tiny Dungeon art folder with **Assets → Export Package**, unticking Core and 2D scripts that Unity adds as dependencies. The Victory screen uses `LevelComplete` from the Platformer Kit: tick it in the export, or copy it into the kit's `UI` folder first.
