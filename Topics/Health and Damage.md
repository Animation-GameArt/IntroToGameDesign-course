---
title: "Health and Damage"
course: GAME 1303
week: 6
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Health and Damage

**Week 6 · [[Lecture] Week 6](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2006%20-%20Lecture.md)**

> [!abstract] In one sentence
> Health turns a mistake from instant failure into a cost, and how much health the player has is a decision about how many mistakes the game allows.

## What this topic is for

Students add health to the player and to opponents, and learn that every number around it (maximum health, damage, invulnerable time, healing) is a difficulty choice.

## Key ideas

- **Health announces what happens to it.** The Health component raises events when damage is taken, health is regained, or it runs out. Nothing needs to check it every frame.
- **Everything hurts the same way.** Spikes, an enemy and a falling rock all use Damage On Touch, which calls the same `TakeDamage` on whatever Health it touches.
- **Invulnerable time.** After a hit, the player can't be hurt again for a moment. Without it, standing in spikes drains all health in a fraction of a second.
- **What happens at zero.** On the player, a Respawner sends them back to the last checkpoint with full health. On an enemy, Health can switch the object off or remove it.
- **Healing is pacing.** A heart placed after a hard section is a reward and a breath. Its placement matters as much as its amount.
- **How many mistakes?** Three health means three mistakes per checkpoint. That number shapes how every section should be designed.

## In the course project

| Component | Role |
|---|---|
| Health | Max Health, Invulnerable Time, what happens at zero, an optional Health Variable for the HUD |
| Damage On Touch | Damage per hit; hit again while touching; optionally removes itself after a hit |
| Respawner | Refills health and returns to the checkpoint when health runs out |
| Collectible with **Heal** | A heart or health pack |
| Health Popups | Floating damage and healing numbers (Week 7) |

## In class

1. Give the player 1, then 3, then 10 health and play the same section each time.
2. Set Invulnerable Time to `0` and stand on spikes.

## Where it comes up

- [Ex 05 — Combat](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat.md) and [Ex 05 — Turn-Based](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat%20%28Turn-Based%29.md).
- [Ex 06 — UI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md): the HUD and damage numbers.
- [Hazards and Checkpoints](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Hazards%20and%20Checkpoints.md).
