---
title: "Genre Map"
course: GAME 1303
status: draft
tags:
  - game1303
  - guide
  - genres
---

# Genre Map

Your game this semester fits one of the genres on this page. Each one has a **kit**: a set of course scripts and a small sample game that you import in Week 8 and build on. Choosing from the map means the scripts for your game's main mechanics already exist, so your eight weeks of production go into the part of the game that is yours.

## How to use this page

1. Read the summary table and pick two or three genres that interest you.
2. Read those sections. Look closely at **A good scope** and **Leave out**.
3. Write your three game ideas (Week 1) and your pitch (Week 3) for a genre on this map. Your pitch names the genre.

Most games mix genres a little. Choose the **one** genre that describes what the player does most of the time. That decides your kit.

## Summary

| Genre | The player… | To finish in eight weeks |
|---|---|---|
| [Arcade classic](#arcade-classic) | plays one screen for a high score | Good first game |
| [Platformer](#platformer) | runs and jumps through levels | Good first game |
| [Top-down adventure](#top-down-adventure) | explores rooms, finds keys, fights | Good first game |
| [Turn-based battle](#turn-based-battle) | chooses actions in turns | Good first game |
| [Endless runner](#endless-runner) | dodges for as long as possible | Good first game |
| [Top-down shooter](#top-down-shooter) | aims and shoots at waves of enemies | Moderate |
| [Grid puzzle](#grid-puzzle) | solves levels one move at a time | Moderate |
| [Physics puzzle](#physics-puzzle) | launches, topples and cuts things that physics moves | Moderate |
| [Tower defense](#tower-defense) | places towers to stop waves | Moderate |
| [Management / strategy](#management--strategy) | spends resources and lives with the results | Moderate |
| [Visual novel](#visual-novel) | reads, and makes choices that change the story | Moderate |
| [Dating sim](#dating-sim) | builds relationships through choices | Moderate |
| [Card game](#card-game) | builds and plays a hand of cards | Ambitious |
| [Farming / life sim](#farming--life-sim) | plants, harvests and trades over days | Ambitious |
| [3D platformer](#3d-platformer) | runs and jumps through a 3D level | Ambitious |
| [Horror / stealth](#horror--stealth) | sneaks past something dangerous | Ambitious |

**Good first game** means the kit covers nearly everything and the risk is low. **Moderate** means one part, such as level design, writing or balance, takes real time. **Ambitious** means the genre has several systems that all have to work, so your scope must be small and your pitch must show that it is.

---

## Arcade classic

**Core loop:** play one screen, score points, lose, try again for a higher score.

**Examples:** Pong, Breakout, Asteroids, Space Invaders.

**The kit gives you:** paddles and balls, bricks, wrapping around the screen edges, lives, a score and a saved high score, and speed that increases over time.

**Kit guide:** [Arcade Classic Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Arcade%20Classic%20Kit.md)

**A good scope:** one classic with one twist of your own. For example, Breakout where the bricks fight back.

**Leave out:** several game modes. Polish one.

## Platformer

**Core loop:** run, jump, collect, avoid hazards, reach the end of the level.

**Examples:** Super Mario Bros., Celeste, Hollow Knight (for its movement).

**The kit gives you:** everything from the exercises (the controller, pickups, hazards, checkpoints, a patrolling enemy and a following camera), plus jumping on enemies, moving and one-way platforms, and a sequence of levels.

**Kit guide:** [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md)

**A good scope:** three short levels that each introduce one idea, and one signature ability, such as a dash or a wall jump.

**Leave out:** a large connected world with ability gates (a Metroidvania). It needs far more content than eight weeks allows.

## Top-down adventure

**Core loop:** explore a room, fight or avoid what's in it, find a key or item, open the way forward.

**Examples:** The Legend of Zelda (the original and A Link to the Past), Hyper Light Drifter.

**The kit gives you:** the top-down controller, a melee attack with knockback, enemies that chase, health as hearts, keys and locked doors, signs and people to talk to, and a camera that moves room by room.

**Kit guide:** [Top-Down Adventure Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit.md)

**A good scope:** one dungeon of five to eight rooms, two enemy types and one boss or final puzzle.

**Leave out:** an overworld, shops and a long item list.

## Turn-based battle

**Core loop:** read the situation, choose an action, watch the result, respond to the opponent's turn.

**Examples:** the battles in early Final Fantasy and Pokémon.

**The kit gives you:** everything from the turn-based exercise (turn order, attack and heal, a computer opponent, win and lose), plus more actions such as defend and a special move, several opponents, and stats stored as data.

**Kit guide:** [Turn-Based Battle Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Turn-Based%20Battle%20Kit.md)

**A good scope:** three to five battles in a row that get harder, with one or two characters on the player's side.

**Leave out:** exploration between battles, and a party of more than three.

## Endless runner

**Core loop:** move forward automatically, dodge and collect, survive as long as you can, beat your best distance.

**Examples:** Canabalt, Jetpack Joyride, Temple Run (in 2D form).

**The kit gives you:** automatic running, jump or lane controls, track pieces that are reused endlessly, difficulty that ramps up over time, and a distance score with a saved best.

**A good scope:** one environment, five or six obstacle patterns, and one power-up.

**Leave out:** shops, unlockable characters and missions.

## Top-down shooter

**Core loop:** move, aim, shoot, survive the wave, get stronger.

**Examples:** Geometry Wars, Enter the Gungeon (for its shooting), Galaga and other scrolling shooters.

**The kit gives you:** aiming with the mouse or the right stick, weapons stored as data (fire rate, spread, projectile), reused projectiles, enemy movement patterns, waves, and power-ups. A scrolling version is included.

**Kit guide:** [Top-Down Shooter Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit.md)

**A good scope:** one arena or one scrolling level, three enemy types, two weapons and a boss.

**Leave out:** procedurally generated rooms and long upgrade trees.

## Grid puzzle

**Core loop:** study the level, make a move, see what changed, undo and rethink, solve it.

**Examples:** Sokoban, Baba Is You (for its grid), Stephen's Sausage Roll.

**The kit gives you:** movement locked to a grid, blocks that can be pushed, a check for when the level is solved, undo and restart, and a list of levels.

**A good scope:** ten to fifteen levels built around one rule of your own, ordered so each teaches something.

**Leave out:** many different mechanics. One good rule makes a better puzzle game than five.

**Expect:** most of your time goes into designing and testing levels, not building features.

## Physics puzzle

**Core loop:** study the structure, aim or cut, watch physics play out, try a better shot.

**Examples:** Angry Birds, Cut the Rope, World of Goo.

**The kit gives you:** a slingshot launcher with aiming dots, limited shots, blocks that break when hit hard enough, targets to destroy, ropes that swing and can be cut by swiping, a score, and win and lose screens. Unity's own joints, materials and effectors do the rest.

**Kit guide:** [Physics Puzzle Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit.md)

**A good scope:** ten to twelve levels, three materials, one kind of projectile, and one twist of your own, such as wind or ropes.

**Leave out:** projectiles with special powers, moving enemies, and stars saved per level.

**Expect:** physics can surprise you. Most of your time goes into building and testing levels until they behave the same way every time.

## Tower defense

**Core loop:** earn currency, place or upgrade a tower, start the wave, watch what gets through, adjust.

**Examples:** Bloons TD, Kingdom Rush, Plants vs. Zombies.

**The kit gives you:** a path for enemies, towers stored as data (range, damage, rate), targeting, waves, currency and fixed building spots.

**A good scope:** one map, three tower types, four enemy types and ten waves.

**Leave out:** several maps and long upgrade trees.

**Expect:** balancing costs, damage and wave strength takes many playtests.

## Management / strategy

**Core loop:** look at your resources, make a few decisions, end the turn, see what happened, plan the next one.

**Examples:** Hammurabi, Reigns, the smallest town builders.

**The kit gives you:** turns or timed ticks, resources, choices and buildings stored as data, random events, an end-of-turn report, and UI screens where things can be dragged and dropped.

**A good scope:** three resources, about ten turns to a win or a loss, and five or six events. Or one small map with five building types.

**Leave out:** armies, opponents controlled by the computer, research trees and a large map (a Civilization-style game).

**Expect:** this is almost entirely a UI game, so your screen layout assignment matters more than usual.

## Visual novel

**Core loop:** read a scene, make a choice, see where the story goes.

**Examples:** Phoenix Wright (for its presentation), Doki Doki Literature Club, Florence.

**The kit gives you:** dialogue with choices, characters with different expressions, backgrounds, music cues and saving.

**A good scope:** one story of fifteen to twenty minutes with two or three endings and three or four characters.

**Leave out:** a long branching story. Every branch has to be written, illustrated and tested.

**Expect:** most of your time goes into writing and art.

## Dating sim

**Core loop:** spend time with a character, choose what to say, watch the relationship change, reach an ending.

**Examples:** Hatoful Boyfriend, Dream Daddy, Monster Prom.

**The kit gives you:** everything in the visual novel kit, plus relationship scores that your choices raise and lower, and endings chosen by those scores.

**A good scope:** two or three characters, a handful of scenes with each, and one ending per character.

**Leave out:** a calendar, stats to train and mini-games.

## Card game

**Core loop:** draw a hand, choose which cards to play, see the effects, end the turn.

**Examples:** Slay the Spire (for its battles), Hearthstone (in very small form).

**The kit gives you:** cards stored as data, a deck, a hand and a discard pile, basic card effects (damage, block, draw, heal), and turn phases.

**A good scope:** twelve to fifteen cards, one fixed deck, and three battles against opponents that follow simple rules.

**Leave out:** building your own deck between battles, a map of branching paths, and a second human player.

**Expect:** every card effect is something that has to be built and balanced. Start with five cards.

## Farming / life sim

**Core loop:** plant, water, wait for the day to pass, harvest, sell, buy something that lets you plant more.

**Examples:** Stardew Valley, Harvest Moon.

**The kit gives you:** a day cycle, soil tiles that can be tilled, planted and watered, crops stored as data with growth stages, an inventory and a shop.

**A good scope:** one field, three crops, one shop and a goal to reach by a set day.

**Leave out:** villagers, relationships, animals, mining, fishing and seasons. The games above took years.

## 3D platformer

**Core loop:** run, jump and explore a 3D space, collect things, reach the goal.

**Examples:** A Hat in Time, Super Mario 64 (one small area of it).

**The kit gives you:** a third-person character with a following camera, jumping, pickups, checkpoints and moving platforms.

**A good scope:** one level with twenty collectibles and three distinct areas.

**Leave out:** several worlds, and enemies that need animation.

**Expect:** see **About 3D games**.

## Horror / stealth

**Core loop:** move carefully, watch the threat, hide or slip past, reach the objective.

**Examples:** Amnesia, Alien: Isolation, and the stealth sections of many games.

**The kit gives you:** a first-person or third-person character, one enemy that patrols, sees and hears, places to hide, a flashlight and an alert meter.

**A good scope:** one building or level, one enemy, three objectives to collect and an exit.

**Leave out:** combat, several enemy types and a long story.

**Expect:** see **About 3D games**. Fear comes from sound, lighting and pacing, so leave time for all three.

---

## About 3D games

The lectures and the exercises in Weeks 1–7 are in 2D, and everyone does them. Nearly everything they teach carries over to 3D: events, variables, health, checkpoints, UI and the Input Reader are the same.

If your approved pitch is a 3D game, you build it in the same course project you've used since Week 2. It holds the 2D and 3D scripts and kits, and the same UI, data and Core scripts work in both. Your game's scenes are 3D scenes. Plan for the differences:

- **Art takes longer.** A 3D game needs models, materials and lighting. Plan to use free asset packs, and credit them.
- **The camera is harder.** A 3D camera can be blocked by walls and has to be controlled by the player.
- **Enemies need navigation.** In 3D, enemies find their way with a navigation mesh, which you set up for each level.

Two tutorials get a 3D game moving: **[2.5D Tutorial 1 — Third-Person Controller](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Tutorials/2.5D%20Tutorial%201%20-%20Third-Person%20Controller.md)** (a player turned and moved relative to themselves, with a camera behind) and **[2.5D Tutorial 2 — Rail Runner](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Tutorials/2.5D%20Tutorial%202%20-%20Rail%20Runner.md)** (a winding path the player can't fall off, seen from behind or from the side).

A 3D game is a fine choice if you already have some 3D experience or a clear, small idea. If you're unsure, a 2D version of the same idea is almost always the faster route to a finished game.

## Not on the map

- **VR and AR.** These have their own projects in other courses.
- **Very large genres.** Open-world games, online multiplayer games, Metroidvanias, roguelikes, real-time strategy and fighting games each need more than one person can build in eight weeks.

If your idea isn't on the map, talk to your instructor **before** pitch week. Often a small version of it fits a genre that is here: one room of a roguelike is a top-down shooter, and one battle of an RPG is a turn-based battle.
