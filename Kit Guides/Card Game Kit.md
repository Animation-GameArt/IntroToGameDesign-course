---
title: "Card Game Kit"
course: GAME 1303
status: draft
course_version: 0.21.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Card Game Kit

The Card Game Kit is a starting point for card battle games: draw a hand, spend energy to play cards, see what the enemy is about to do, and end your turn. Examples: Slay the Spire (its battles), Monster Train, Balatro (for its feel of playing a hand).

The sample, *Suit Duel*, turns an ordinary deck of playing cards into a battle deck. Spades attack, diamonds block, hearts heal, and clubs draw more cards. The number on the card is how strong it is. You fight three enemies in a row; your health carries over between fights, and you rest a little after each one.

A card game is **rules and numbers**. Every card is something that has to be designed and balanced, so the kit keeps cards and enemies as assets you edit in the Inspector, and leaves your time for designing the deck.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| A deck, a hand, a draw pile and a discard pile, shuffled when the draw pile runs out | Building your deck between battles, or card rewards |
| Energy, and cards that cost it | Cards that target one of several enemies |
| Damage, block, heal, draw and energy effects, each once or several times | Poison, strength and other effects that last (a custom script) |
| Cards that are used up for the battle (Exhaust) | Upgrading cards |
| Enemies whose next move is shown, in order or at random | Several enemies at once, or bosses with phases |
| A run of battles, with health carrying over | A map of branching paths, shops, relics |
| Mouse, touch and keyboard | A second human player |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut. The Genre Map's advice stands: twelve to fifteen cards, one fixed deck, three battles.

## Install the kit

1. Download the Card Game Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/CardGame/Sample/Scenes`, add `Cards_Menu` and `Cards_Game`, next to each other, in that order.
4. Open `Cards_Menu` and press **Play**.

Click or tap a card to play it (it lifts when you point at it). The number keys 1–9 play the cards in order. **End Turn**, E or Enter ends your turn. Esc pauses.

## How it works

- **Cards** (assets) have a **Cost** in energy and a list of **Effects**: Damage, Block, Heal, Draw or Energy, each with an **Amount** and how many **Times**. The text under the card is written from its effects unless you write your own.
- **Enemies** (assets) have health, a picture, and a list of **Moves**: Attack, Block or Heal. The screen always shows the next move, so the player can plan: block when an attack is coming, attack when it isn't.
- **Block** lasts until the blocker's next turn. It's used up before health.
- The **Card Battle** runs it all: at the start of each turn the player's block resets, energy refills and five cards are drawn. Playing cards spends energy. Ending the turn discards the hand, and the enemy makes its move.
- When the enemy is beaten, the next battle starts. Beat them all to win; run out of health to lose.

## What's in the sample

| Cards | Effect | Cost | In the deck |
|---|---|---|---|
| Spades 2–7 | Deal the card's number | 1 | 6 |
| King of Spades | Deal 10 | 2 | 1 |
| Diamonds 3–6 | Block the card's number | 1 | 4 |
| Hearts 3–4 | Heal the card's number | 1 | 2 |
| 2 of Clubs | Draw 2 cards | 1 | 1 |
| Jack of Clubs | Gain 2 energy | 0 | 1 |

| Enemy | Health | Moves, in order |
|---|---|---|
| Slime | 28 | Attack 6, Attack 6, Block 4 |
| Knight | 42 | Block 10, Attack 11, Attack 8 |
| Demon | 62 | Attack 4 three times, Block 10, Attack 15 |

You have 40 health, 3 energy a turn, and heal 10 after each battle. The numbers were checked with a simulation: a player who blocks when an attack is coming and attacks otherwise wins about four runs in five; a player who plays cards at random wins about one in four, and almost always loses to the Demon.

## Start your own game

1. Design five cards on paper first, and play a few turns with paper cards against a made-up enemy. Then add more.
2. Create your **Cards** (**Create → Collin Game → Card Game Kit → Card**) and **Enemies** (**Create → Collin Game → Card Game Kit → Enemy**).
3. Open `Cards_Game`, **File → Save As…** into `Assets/_Game/Scenes`, and on the **Card Battle**: your cards in **Deck** (twice for two copies), your enemies in **Enemies**, and the player's **Max Health**, **Energy Per Turn** and **Hand Size**.
4. Press **Play** and play a full run. Then change one number and play again.

Card art: use the **Face** for a whole picture of the card. Leave Face empty to use the blank card with the name written on it, which is quickest while you're still designing.

### Designing the cards

- **Each card should be best somewhere.** A card that's always worse than another never gets played.
- **Cost is the main lever.** A 2-energy card has to be worth more than two 1-energy cards, or nobody plays it.
- **Enemy moves are the puzzle.** A big attack telegraphed a turn ahead makes the player choose between blocking now and attacking now.
- **Test with a random player.** Play a run choosing cards without thinking. If you win easily, it's too easy.

## Recipes

**A card that hits several times.** One Damage effect with **Times** `3`.

**A card that does two things.** Two effects, such as Damage 5 and Block 5.

**A powerful one-off.** Tick **Exhaust**: once played, it's gone for the rest of the battle.

**An unpredictable enemy.** Tick **Random Order** on the enemy.

**A run that's one long battle.** Put one enemy in **Enemies** with a lot of health.

**Sounds.** The Card Battle's **On Card Played**, **On Enemy Hit**, **On Player Hit**, **On Block** and **On Enemy Defeated** can each play a Sound Effect. Kenney's Casino Audio has card sounds.

## If something goes wrong

| What you see | What to do |
|---|---|
| Nothing appears | The Card Battle needs cards in **Deck** and at least one enemy |
| A card can't be played | It's faded: it costs more energy than you have left |
| Cards are blank | Set each card's **Face**, or the UI Card Battle's **Blank Card** |
| The card text is wrong | Clear the card's **Description**, and it's written from the effects |
| The enemy does nothing | Give it at least one move |
| The game ends at once | The player's **Max Health** is 0, or the first enemy has 0 health |
