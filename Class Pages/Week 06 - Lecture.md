---
title: "[Lecture] Week 6"
course: GAME 1303
week: 6
status: draft
tags:
  - game1303
  - lecture-page
---

# Week 6 — Ex 05: Combat · Ten-pager draft

**Exercise:** Ex 05 — Combat. Real-time (enemy, damage, spawner, respawn) or turn-based (turn manager, turns, attacks, win and lose).

**Also due:** the ten-pager draft, in Canvas by 11:59 PM the night before class, for peer review during lab. It doesn't need to be finished, but every page needs something on it.

## Lecture topics, expanded

**Health, damage and respawning.** Health is a number with consequences. The course's health component announces what happens to it, through events, so nothing has to check it every frame: damage taken, healed, died. A hazard, an enemy and a falling rock all deal damage the same way. Cover a short spell of invulnerability after a hit, so one touch doesn't drain every point, and respawning at the last checkpoint from Week 5. Then ask the design question: how many mistakes should a player be allowed?

**Spawners and object pooling.** A spawner creates objects on a timer or in waves. Creating and destroying hundreds of objects is slow, so a **pool** keeps a set of them and reuses each one. The design layer matters more than the code: difficulty over time is a schedule of how many, how often and what kind. Draw it as a curve on the board, with a ramp, a plateau and a spike, before touching the spawner's settings.

**State machines and simple enemy AI.** An enemy that feels alive is usually in one of a few **states**: patrolling, chasing, attacking. A state machine is the list of states plus the rules for moving between them. Draw one as circles and arrows, then show the patrolling enemy doing exactly that. Good enemies are readable. They signal what they're about to do, so the player loses to a mistake and not to a surprise.

**Turn-based systems, and winning and losing.** Some games swap reflexes for decisions. A **turn manager** keeps track of whose turn it is and what they're allowed to do, and the same health and damage sit underneath. Students whose game is a puzzle, tactics or strategy game should take the turn-based version of the exercise. Close with win and lose conditions: every game needs both to be stated plainly, and both are events the rest of the game reacts to.

**Physics in Unity.** Students have used physics since Exercise 02 without choosing its settings, because the course scripts chose them. Open the box: dynamic, kinematic and static bodies, mass and gravity, setting speed versus adding force, physics materials for friction and bounce, joints, effectors, and the layer collision matrix. Demonstrate with a seesaw, crates of different mass, a bouncy floor and a breakable hinge. The optional physics part of Exercise 05 lets students try each, and the Physics Puzzle Kit builds a whole genre on it.

## Topic notes

Each topic has its own page with the lecture's intent, a demo plan, common problems and further resources.

- [Health and Damage](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Health%20and%20Damage.md)
- [Spawners and Pooling](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Spawners%20and%20Pooling.md)
- [State Machines and Enemy AI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/State%20Machines%20and%20Enemy%20AI.md)
- [Turn-Based Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Turn-Based%20Systems.md)
- [Physics in Unity](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Physics%20in%20Unity.md)

## Connecting it forward

Health, score and the win and lose conditions exist after today, but the player can't see any of them except in the Inspector. Next week's HUD and menus put them on screen, using the screen layouts from Week 5. The peer-review notes from lab feed the final ten-pager, due the night before next class, which closes pre-production.
