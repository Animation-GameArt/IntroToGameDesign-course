---
title: "Turn-Based Battle Kit"
course: GAME 1303
status: draft
course_version: 0.12.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Turn-Based Battle Kit

The Turn-Based Battle Kit is a starting point for games where fighters take turns choosing actions from a menu, as in classic role-playing games and many roguelike deckbuilders. It adds actions you create as assets, fighters with stats, a battle menu, a battle log and health bars. The sample is a short series of three battles: a party of two against slimes, then a bigger monster.

It builds on the Turn Manager and Turn Taker you used in the turn-based version of Exercise 05. If you did the real-time version, read that exercise's Part 1 first; it's short.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| A party of one or more fighters against one or more opponents | Moving on a grid during battle (that's tactics; ask about the grid puzzle kit) |
| Attacks, heals and defending, with accuracy and limited uses | Status effects such as poison or sleep |
| Attack and Defense stats | Levels, experience points or equipment |
| A menu of actions and targets, for mouse, keyboard or gamepad | Speed-based turn order (turns go in a fixed order) |
| Computer fighters that heal when low and attack otherwise | Clever AI that picks the best move |
| A battle log, a round counter, health bars and win and lose screens | Exploring a map between battles (combine with the Top-Down Adventure Kit) |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Turn-Based Battle Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/TurnBasedBattle/Sample/Scenes`, add these scenes, next to each other and in this order: `Battle_Menu`, `Battle_1`, `Battle_2`, `Battle_3`, `Battle_Win`.
4. Open `Battle_Menu` and press **Play**.

Choose actions with the mouse, or with the arrow keys and **Enter**, or with a gamepad's stick and south button. **Esc** pauses.

## What's in the sample

| Prefab or asset | What it is | Settings worth changing |
|---|---|---|
| `Hero` | Player fighter with Slash, Power Strike, Defend and Potion | **Actions**, **Attack**, **Defense**, Health **Max Health** |
| `Healer` | Player fighter with Staff, Heal and Defend | **Actions** |
| `Slime` | Computer fighter with Bite | **Attack**, **Heal Below** |
| `Ogre` | A stronger computer fighter with Club and Roar (defend) | **Attack**, **Defense**, **Max Health** |
| Actions in `Sample/Actions` | One asset per action | **Power**, **Accuracy**, **Uses Per Battle**, **Target** |
| `Battle Systems` | Turn Manager, battle screen, log, win and lose screens | **Turn Order** on the Turn Manager |

## How the sample fits together

**Turns.** The Turn Manager goes through its **Turn Order**, as in Exercise 05. Each fighter's Turn Taker tells its Battle Actor that the turn has started.

**Choosing.** A computer fighter waits a moment, then picks an action and a target by itself. For a player fighter, the **UI Battle Menu** shows one button per action. Actions with limited uses show how many are left, and are greyed out at 0. After an action is picked, the menu shows the possible targets, unless there's only one.

**Actions.** Each action is a **Battle Action** asset. Its **Effect** is Damage, Heal or Defend; its **Target** is one opponent, all opponents, the user, or one ally.
- **Damage** = Power + the user's Attack − the target's Defense, at least 1. A defending target takes half.
- A damage action can miss: **Accuracy** is the chance to hit, out of 100.
- **Defend** lasts until the defender's next turn.

**The log.** Every action writes a line, such as "Slime uses Bite. Hero takes 2." The **Battle Log** keeps the last four lines in `BattleLog`, which the battle screen shows.

**Winning and losing.** The Turn Manager raises `BattleWon` when no opponent can act, and `BattleLost` when no player fighter can. The win screen's Next button loads the next battle.

## Start your own game

1. Create a new 2D scene in `Assets/_Game/Scenes`.
2. Drag in `Battle Systems` and two fighters from the kit's `Sample/Prefabs`: one `Hero` and one `Slime`.
3. On `Battle Systems` → `Turn Manager`, add both to **Turn Order**.
4. Press **Play**.

Then make your own fighters and actions:

- **A new action:** in `Assets/_Game`, **Create → Collin Game → Turn-Based Battle Kit → Battle Action**. Set its name, description, effect, target and power. Add it to a fighter's **Actions**.
- **A new fighter:** a variant of `Hero` or `Slime` (right-click → **Create → Prefab Variant**), moved to `Assets/_Game/Prefabs`, with a new sprite, stats and actions.

Every fighter's Health needs **Invulnerable Time** at `0`, or a second hit in the same round is ignored. The Console warns you if this happens.

## Recipes

**A fire spell that hits every enemy.** An action with Effect **Damage**, Target **All Opponents**, Power `2`, Uses Per Battle `2`.

**A potion with three uses.** Effect **Heal**, Target **Self**, Power `5`, Uses Per Battle `3`.

**A heal for the whole party.** Make it Target **One Ally** to choose who, or add two heal actions. (A heal for everyone at once is a custom script.)

**A boss.** An `Ogre` variant with Max Health `30`, Defense `2`, and three actions. Put it in the Turn Order twice to give it two turns per round.

**A fighter that hits hard but misses often.** Give its attack Power `6` and Accuracy `60`.

**Sound and shake.** Give each action a **Sound** (a Sound Effect asset from Exercise 07). On each fighter's Health **On Damaged**, add **CameraShake → Shake**.

**Health bars.** The sample fighters have a **Health Bar 2D** over their heads. For a number instead, give the fighter's Health a **Health Variable** and show it with a UI Variable Binder.

**Battles in an adventure.** Make each battle its own scene. In the Top-Down Adventure Kit, an enemy's Damage On Touch can be replaced by a **Trigger Zone** that loads the battle scene. To return to the exact spot afterwards needs a custom script.

## If something goes wrong

| What you see | What to do |
|---|---|
| Nothing happens when the battle starts | Check the Turn Manager's **Turn Order**, and that **Start Automatically** is ticked |
| The menu never appears | The battle screen needs a **UI Battle Menu**, and the player fighter's **Controlled By** must be **Player** |
| "A hit was ignored because Health is still invulnerable" | Set that fighter's Health **Invulnerable Time** to `0` |
| An action button is greyed out | It has no uses left, or there's no one it can target |
| The battle is won straight away | Each opponent needs a Turn Taker with **Player Side** unticked, in the Turn Order |
| Keyboard keys don't move between buttons | Click the Game view first, so it has keyboard focus |
| Every action does 1 damage | The target's **Defense** is higher than the action's Power plus the user's Attack |
