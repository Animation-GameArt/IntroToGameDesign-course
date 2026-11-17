---
title: "Exercise 05 — Combat (Turn-Based)"
course: GAME 1303
week: 6
status: draft
course_version: 0.7.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 05 — Combat (Turn-Based)

**Week 6 · checked off in lab**

> **Choose one version.** This is the **turn-based** version, for puzzle, tactics and strategy games. If your game is an action game, do **Exercise 05 — Combat** instead.

In this exercise a hero and a slime take turns. On your turn you choose: attack, or heal. Heals are limited, so the choice matters. The same Health component from the real-time version is underneath.

## What you'll learn

- How **Health** works, and how it announces damage and death
- How a **Turn Manager** decides whose turn it is
- How an opponent can follow a simple rule to choose its action
- How to state a **win** and a **lose** condition
- How a few numbers turn a fight into an interesting decision

## Part 1 — Start the scene

1. Open `Ex01_Bootstrap` and choose **File → Save As…**. Save it as `Ex05_TurnBased`.
2. Delete the `Scene Changer`.
3. In `Assets/Scenes/Exercises`, create a folder named `Ex05_Data`.

## Part 2 — Create the data

In `Ex05_Data`, create these assets with **Create → Collin Game → Variables**:

| Asset | Type |
|---|---|
| `HeroHealth` | Int Variable |
| `SlimeHealth` | Int Variable |
| `TurnStatus` | String Variable |
| `BattleLog` | String Variable |

## Part 3 — The hero and the slime

**The hero**

1. Create a **Square** sprite named `Hero`. Position `-4, 0, 0`. Give it a color.
2. Add the **Health** component:
   - **Max Health:** `10`
   - **Invulnerable Time:** `0`
   - **Health Variable:** `HeroHealth`
3. Add the **Turn Taker** component. Leave **Player Side** ticked.

**The slime**

1. Create a **Circle** sprite named `Slime`. Position `4, 0, 0`. Give it a color.
2. Add the **Health** component:
   - **Max Health:** `8`
   - **Invulnerable Time:** `0`
   - **When Health Runs Out:** **Deactivate**
   - **Health Variable:** `SlimeHealth`
3. Add the **Turn Taker** component. **Untick** Player Side.

## Part 4 — What each one can do

**The hero**

1. Select `Hero` and add the **Turn Actions** component:
   - **Controlled By:** **Player**
   - **Input:** should already hold `InputReader`
   - **Attack Target:** drag in `Slime`
   - **Attack Damage:** `2`
   - **Heal Amount:** `3`
   - **Heals Available:** `2`
   - **Message Text:** `BattleLog`

**The slime**

1. Select `Slime` and add the **Turn Actions** component:
   - **Controlled By:** **Computer**
   - **Attack Target:** drag in `Hero`
   - **Attack Damage:** `2`
   - **Heals Available:** `1`
   - **Heal When Health At Or Below:** `2`
   - **Message Text:** `BattleLog`

## Part 5 — The Turn Manager

1. Create an empty GameObject named `Battle` and add the **Turn Manager** component.
2. Under **Turn Order**, click **+** twice. Drag in `Hero` first, then `Slime`.
3. Set **Status Text** to `TurnStatus`.

## Part 6 — Show what's happening

Create four texts with **GameObject → 3D Object → Text - TextMeshPro**. For each one, set **Font Size** to `6`, set the **Alignment** to center and middle, and add a **Variable Label**.

| Name | Position | Variable | Format |
|---|---|---|---|
| `Status Text` | `0, 4, 0` | `TurnStatus` | `{0}` |
| `Log Text` | `0, 3, 0` | `BattleLog` | `{0}` |
| `Hero Health Text` | `-4, 1.5, 0` | `HeroHealth` | `Hero: {0}` |
| `Slime Health Text` | `4, 1.5, 0` | `SlimeHealth` | `Slime: {0}` |

Add one more text named `Help Text` at Position `0, -3.5, 0`, with no Variable Label. Type this as its text: `Attack: Enter     Heal: E`

Press **Play** and click once in the Game view.

| Action | Keyboard | Gamepad |
|---|---|---|
| Attack | **Enter** | Left face button |
| Heal | **E** | Top face button |

On your turn, attack or heal. The slime then waits a second and takes its turn. The battle ends when one side has no health left, and the status text says who won.

## Part 7 — Restart, and reset the texts

1. Create an empty GameObject named `Scene Changer`. Add the **Scene Changer** component:
   - **Scene Name:** `Ex05_TurnBased`
   - **Load On Action:** `Player/Jump`
2. Add `Ex05_TurnBased` to the Scene List.
3. Create an empty GameObject named `Game Setup`. Add the **Variable Resetter** component and add `TurnStatus` and `BattleLog` to its list.
4. Add `Restart: Space` to the end of the `Help Text`.

Press **Play**. After a battle, press **Space** to play again.

## Part 8 — Win and lose

The Turn Manager knows when the battle is over. Make the scene react.

1. Create a text named `Win Text` at Position `0, 0, 0` with the text `Victory!` and a **Font Size** of `12`. Untick the checkbox at the top of the Inspector to hide it.
2. Duplicate it, name the copy `Lose Text`, and change its text to `Defeated`.
3. Select `Battle`. Under **On Player Won**, click **+**, drag in `Win Text`, and choose **GameObject → SetActive (bool)**. **Tick** the checkbox.
4. Under **On Player Lost**, do the same with `Lose Text`.

Press **Play** and win a battle. Then let the slime win one.

## Part 9 — Make it a real decision

A turn-based game is only as interesting as its choices. Right now, is there ever a reason not to attack?

Play several battles and change the numbers until both options are worth thinking about.

| What | Setting | Question to ask |
|---|---|---|
| Hero | **Max Health**, **Attack Damage** | How many turns does a battle last? |
| Hero | **Heal Amount**, **Heals Available** | Is a heal worth giving up an attack? |
| Slime | **Max Health**, **Attack Damage** | Can the player win without healing? Should they be able to? |
| Slime | **Heal When Health At Or Below** | Does the slime's heal change what the player should do? |
| Battle | **Turn Order** | Does going first decide the battle? |

A good target: the player wins most battles, but only if they heal at the right moment.

**Go further.** Duplicate `Slime` to add a second opponent, add it to the **Turn Order**, and point its **Attack Target** at `Hero`. The hero can only attack one target, so decide which.

## Check-off

Show your instructor:

- [ ] The hero and the slime take turns, and both health values show on screen.
- [ ] You can attack and heal, and heals run out.
- [ ] The slime attacks, and heals when its health is low.
- [ ] Winning and losing each show a message, and Space restarts the battle.
- [ ] You can say which numbers you changed, and what decision they give the player.

## If something goes wrong

| What you see | What to do |
|---|---|
| Nothing happens when you press Enter | Click in the Game view. Check that the hero's **Controlled By** is **Player** and its **Input** field holds `InputReader`. |
| The first click in the Game view attacks | The left mouse button is also bound to Attack. Use **Enter** to attack. |
| An attack does no damage | Check **Attack Target**, and check that **Invulnerable Time** is `0` on both Health components. |
| The slime never takes its turn | Check that the slime's **Controlled By** is **Computer** and that it's in the **Turn Order**. |
| The battle never ends | Check that **Player Side** is ticked on the hero and unticked on the slime. |
| A text shows nothing | Check the label's **Variable**, and that the same asset is set on the Health, Turn Manager or Turn Actions component. |

## Related topics

- [Health and Damage](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Health%20and%20Damage.md)
- [Turn-Based Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Turn-Based%20Systems.md)
