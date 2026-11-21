---
title: "Management Kit"
course: GAME 1303
status: draft
course_version: 0.18.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Management Kit

The Management Kit is a starting point for management and strategy games played in turns: look at your resources, make a few decisions, end the turn, see what happened, plan the next one. Examples: Hammurabi, Reigns, the smallest town builders.

The sample is a small take on Hammurabi. You run a village for ten years. People eat food every year; taxes bring in gold; buildings you drag onto plots produce food, wood, people and gold; and random events (rats, storms, a travelling merchant) force choices. Let the people starve and the game is lost.

Almost all of a management game is **numbers and screens**. The kit keeps the numbers in assets you edit in the Inspector, and the screen in one UXML file, so your design work goes into the rules, the events and the layout you drew for your screen layout assignment.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Any number of resources (each an Int Variable) | Resources with decimals |
| Rules that run every turn, as lists of simple effects | Rules that need real formulas (a custom script) |
| Random events, some with two or three choices | Chains of events that remember each other's answers |
| Buildings dragged onto plots, with costs and every-turn effects | A scrolling map, roads or placement rules |
| Turns ended with a button, or by a timer | Armies, opponents or research trees |
| An end-of-turn report of what changed | Saving a game in progress |
| Winning by lasting a number of turns; losing by a resource running out | |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut.

## Install the kit

1. Download the Management Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/Management/Sample/Scenes`, add `Village_Menu` and `Village_Game`, next to each other, in that order.
4. Open `Village_Menu` and press **Play**.

Drag a building card onto a plot to build it. Drag a built building back onto the cards to remove it. Click **End Turn** to end the year. The game is played with the mouse or a touch screen; **Esc** pauses.

## How it works

Everything is built from one idea: an **Effect**, a change to one resource. For example:

| Effect | Amount | Times Each | Divide By | Only When |
|---|---|---|---|---|
| Food −1 per person | Food, `-1` | People | `1` | Always |
| Gold +1 per 3 people | Gold, `1` | People | `3` | Always |
| People −3 (give or take 1) if out of food | People, `-3`, Random Extra `1` | — | `1` | Food at most `0` |
| People +1 if food is plentiful | People, `1` | — | `1` | Food at least `30` |

Effects appear in three places:

- **Turn Rules** (assets) happen every turn, in order. The sample has *Eating*, *Hunger*, *Taxes* and *Growth*, in that order. Order matters: *Hunger* checks food after *Eating* has taken it.
- **Buildings** (assets) have a **Cost** (paid once, when built) and **Every Turn** effects (per building built). A Farm costs Gold 20 and gives Food +6 each turn.
- **Events** (assets) can happen at the end of a turn. Some just happen (*Rats in the Granary*: Food −10). Others ask a question, with a button per **Choice**, each with its own effects (*A Merchant Arrives*: buy grain, sell wood, or send him away).

The **Turn Cycle** runs it all. When the turn ends, it applies the rules, then the buildings, then perhaps an event (waiting for the player's choice), then writes the report and counts the turn. After **Turns To Win** turns, the player wins. Losing is an **Int Variable Condition** from the Core scripts: People at most 0.

## What's in the sample

| Asset | What it is | Worth changing |
|---|---|---|
| `People`, `Food`, `Gold`, `Wood` | The resources (Int Variables) | **Initial Value** |
| `Eating`, `Hunger`, `Taxes`, `Growth` | Turn Rules | The effects' numbers |
| `Farm`, `Lumber Camp`, `House`, `Market` | Buildings | **Cost**, **Every Turn** |
| `Rats`, `Good Harvest`, `Storm`, `Plague`, `Merchant`, `Festival` | Events; the last two have choices | **Weight**, **Earliest Turn**, choices |
| `Village Systems` | The Turn Cycle, the screen, win and lose | **Turns To Win**, **Event Chance** |

The sample's numbers were checked with a quick simulation: building farms early and then houses and markets wins every time; building nothing loses almost every time, around year 6.

## Start your own game

**[Management Kit — Build Your Game](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Management%20Kit%20-%20Build%20Your%20Game.md)** takes you from the decisions table on page 10 of your ten-pager to your finished game, step by step, with checks for First Playable, Alpha and Beta. The steps below are the short version.

1. Decide your resources (three or four is plenty). Create an **Int Variable** for each in `Assets/_Game/Data`, with a starting value.
2. Write your rules on paper first: what happens every turn? Then create a **Turn Rule** for each (**Create → Collin Game → Management Kit → Turn Rule**).
3. Create your **Buildings** and **Events** the same way.
4. Open `Village_Game`, **File → Save As…** into `Assets/_Game/Scenes`, and on `Village Systems`:
   - **Turn Cycle**: your rules (in order), your resources, your events.
   - **UI Build Grid**: your buildings, and your resources in **Watch Resources**.
   - **UI Variable Binder** on the screen: point the `resource-1-label` … `resource-4-label` at your resources.
5. Press **Play** and play ten turns. Then change one number and play again.

### Designing the numbers

- **Play on paper first.** A spreadsheet with a row per turn shows quickly whether a strategy works.
- **Every choice should cost something.** A building that is always worth it isn't a decision.
- **Pressure should grow.** In the sample, more people eat more food, so the farms you built early stop being enough.
- **Tell the player why.** The report shows every resource's change; make sure an event's text explains surprises.

## Recipes

**A Reigns-style game.** No buildings: hide the build area in the UXML, set **Event Chance** to `1`, and make every event a choice. Four resources that must stay between limits (lose if any reaches 0, or 100).

**A game that runs by itself.** Set **Seconds Per Turn** on the Turn Cycle, such as `5`, for a small real-time town. Events still pause it.

**An event only once.** Tick **Only Once** on the event.

**An event that needs a condition.** Set the event's **Condition**, such as Gold at least 100 for *Bandits*.

**A building that needs people.** Give a House the every-turn effect People +1, and a Mine the cost People −2.

**Winning by reaching a goal.** Set **Turns To Win** to `0`, and add an **Int Variable Condition**: Gold at least 500 → raise the win event.

**Sounds.** Play a sound on the Turn Cycle's **On Turn Ended**.

## If something goes wrong

| What you see | What to do |
|---|---|
| End Turn does nothing | The screen needs **UI Management Screen**, and the scene a **Turn Cycle**. If an event is showing, answer it first |
| A resource never changes | Check the rule's effect has the **Resource** set, and its **Only When** condition can be met |
| Resources go negative | Tick **No Negative Resources**, and list the resource in **Resources** |
| A card can't be dragged | It's greyed out: you can't afford it |
| A card stays grey after earning money | Add that resource to **Watch Resources** on the UI Build Grid |
| Buildings do nothing | Their effects are in **Every Turn**, not **Cost** |
| The report is empty | List your resources in the Turn Cycle's **Resources** |
| The game ends at once | A lose condition is already true: check starting values |
