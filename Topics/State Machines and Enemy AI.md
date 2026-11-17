---
title: "State Machines and Enemy AI"
course: GAME 1303
week: 6
type: topic
status: draft
tags:
  - game1303
  - topic
---

# State Machines and Enemy AI

**Week 6 · [[Lecture] Week 6](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2006%20-%20Lecture.md)**

> [!abstract] In one sentence
> An enemy that feels alive is usually in one of a few states, with simple rules for moving between them, and good enemies show the player which state they're in.

## What this topic is for

Students meet the state machine through the course's patrolling enemy, and learn to describe any enemy, or their own, as circles and arrows before building it.

## Key ideas

- **States.** What the enemy is doing right now: patrolling, chasing, attacking, stunned.
- **Transitions.** The rules for changing state: "if the player is within 4 units, chase"; "if the player leaves, patrol."
- **One state at a time.** Each state does one clear thing, which makes enemies easy to reason about and to debug.
- **Readable enemies.** Players should be able to see what an enemy is about to do. A pause before a charge, a color change when it notices you. A player should lose to their own mistake, not to a surprise.
- **Simple rules go a long way.** Turning at walls and ledges, and chasing within a range, produces behavior that feels purposeful.

## In the course project

**Patrol Enemy 2D** has two states:

| State | Does | Changes when |
|---|---|---|
| Patrol | Walks; turns at walls and ledges | The player comes within Chase Range |
| Chase | Walks toward the player; won't walk off a ledge | The player leaves Chase Range |

Selecting the enemy shows its chase range as a circle in the Scene view.

## In class

1. Draw the patrol enemy as two circles and two arrows.
2. Draw a third state on the board, such as "stunned after being stomped," and ask what transitions in and out of it.
3. Have students draw a state machine for one enemy in their own game.

## Where it comes up

- [Ex 05 — Combat](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat.md), Part 4.
- [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md): the Walker uses this enemy.
- The horror and stealth kit uses more states: patrol, investigate, chase.

## Further resources

- Robert Nystrom, *Game Programming Patterns*, [State](https://gameprogrammingpatterns.com/state.html).
