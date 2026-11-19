---
title: "Physics in Unity"
course: GAME 1303
week: 6
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Physics in Unity

**Week 6 · [[Lecture] Week 6](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2006%20-%20Lecture.md)**

> [!abstract] In one sentence
> Unity's physics simulates bodies, forces, friction, bounce and joints, and a few settings decide whether an object is pushed around, moves on a path, or never moves at all.

## What this topic is for

Students have used physics since Exercise 02 without choosing any of its settings, because the course scripts chose them. This topic opens the box: what each kind of body is for, how forces differ from setting speed, and what materials, joints and layers do. The optional physics part of Exercise 05 lets students try each one. It is also the background for the **Physics Puzzle Kit**.

## Key ideas

- **2D and 3D physics are separate.** A 2D game uses components ending in **2D**: Rigidbody 2D, Box Collider 2D, Hinge Joint 2D. They never interact with the 3D versions.
- **Three kinds of body:**

| Body Type | Moves? | Pushed by collisions? | Use it for | In the course project |
|---|---|---|---|---|
| **Dynamic** | Yes, by physics | Yes | Anything that falls, rolls or gets knocked over | The player, rocks, crates |
| **Kinematic** | Only when a script moves it | No, but it pushes others | Moving platforms, enemies on a path | Waypoint Mover 2D |
| **Static** | Never | No | Ground and walls | Tilemap ground |

- **A collider with no Rigidbody** behaves as static: solid, but never moves.
- **Mass, gravity and drag.** **Mass** decides how hard an object is to push and how hard it hits. **Gravity Scale** multiplies gravity for one object. **Linear Damping** (drag) slows movement, like air or water resistance.
- **Forces and speed.** A script can **set speed** (precise; the course's controllers do this) or **add a force** (natural; objects respond to their mass). An **impulse** is a force applied all at once, like a kick or an explosion.
- **Physics materials.** A **Physics Material 2D** sets **Friction** (how much things slide) and **Bounciness** (how much they bounce). Ice is low friction; a trampoline is high bounciness.
- **Joints connect bodies.**

| Joint | Behaves like |
|---|---|
| Hinge Joint 2D | A door hinge, a seesaw, a pendulum, a rope link |
| Spring Joint 2D | A spring or an elastic band |
| Distance Joint 2D | A rigid rod, or a rope that can't stretch |
| Fixed Joint 2D | Glue: two bodies move as one until it breaks |
| Wheel Joint 2D | A car wheel on a suspension |
| Slider Joint 2D | A piston or a sliding door |

  Every joint has a **Break Force**: pull harder than that and the joint snaps.
- **Effectors** change how things behave on or near a collider. **Platform Effector 2D** makes one-way platforms; **Area Effector 2D** pushes everything inside it, like wind or a conveyor; **Point Effector 2D** pulls things toward a point or pushes them away.
- **Layers and the collision matrix.** Each object has a **Layer**. **Edit → Project Settings → Physics 2D → Layer Collision Matrix** decides which layers can hit which, for example so enemies pass through each other.
- **Rules of thumb.**
  - Move dynamic bodies with physics (velocity or forces), never by changing their Transform position, or they pass through walls.
  - Fast, small objects need **Collision Detection: Continuous** so they don't skip through thin walls.
  - Physics runs on its own clock, in `FixedUpdate`.
  - Bodies that stop moving **sleep** to save time, and wake when touched.

## In class

1. Drop three crates with different **Mass** onto a seesaw made with a Hinge Joint 2D.
2. Give one crate a Physics Material 2D with Friction `0` and push it; then Bounciness `0.9` and drop it.
3. Switch a moving platform from Kinematic to Dynamic and watch it fall.
4. Hang a weight from a Hinge Joint 2D, set **Break Force** low, and hit it.

## Common problems

| What happens | Why |
|---|---|
| An object falls through the floor | One of them has no collider, or the object is moved by its Transform |
| A fast projectile goes through a wall | Set its Rigidbody's **Collision Detection** to **Continuous** |
| A moving platform falls | Its Rigidbody is Dynamic; make it Kinematic |
| A stack wobbles or explodes at the start | Objects overlap. Leave a tiny gap, and let the stack settle before it can break |
| Objects that should pass through each other collide | Put them on layers that don't collide in the Layer Collision Matrix |

## Where it comes up

- [Ex 02](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md): a ball rolling under gravity.
- [Ex 05 — Combat](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat.md), Part 8: the optional physics playground.
- [Physics Puzzle Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit.md): launching, breaking, ropes.
- [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md): one-way platforms (Platform Effector 2D) and moving platforms (kinematic).
- [GameObjects, Components and Prefabs](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/GameObjects%2C%20Components%20and%20Prefabs.md): colliders, triggers and Rigidbodies.

## Further resources

- Unity Manual, 2D physics: start from the **Rigidbody 2D**, **Physics Material 2D**, **Joints 2D** and **Effectors 2D** pages in the Unity 6.3 manual.
