---
title: "[Lecture] Week 4"
course: GAME 1303
week: 4
status: draft
tags:
  - game1303
  - lecture-page
---

# Week 4 — Ex 03: Player · One-sheet due

**Exercise:** Ex 03 — Player. A controllable character, a small level, a game-feel tuning pass and a top-down variant.

**Also due:** the one-sheet, in Canvas by 11:59 PM. One page: logline, story summary, core loop, unique selling points, comparable games and a key image. Screen layouts are introduced today and due next week.

## Lecture topics, expanded

**The Input System and the Input Reader.** Unity's Input System works in **actions**, such as Move and Jump, and each action has **bindings** to keys, buttons and sticks. Open the project's actions asset and show that Move is bound to WASD, the arrow keys and the left stick all at once. The course scripts never read a key directly. They ask the **Input Reader** asset, which offers values such as `Move` and events such as `JumpPressed`. That's why the same controller works on keyboard and gamepad, and why controls can be turned off in one place during a cutscene.

**Game feel.** Game feel is what the controls feel like in the hands. Show the handful of numbers behind it on the Platformer Controller: top speed, acceleration and deceleration, air control, jump height, gravity and fall speed. Change one at a time, live, and have students name the result: icy, heavy, floaty, sharp. Jump height is set in units, so level design and movement can be planned together: a three-unit jump clears a two-unit wall.

**Coyote time, jump buffering and short hops.** Players press buttons slightly early and slightly late. **Coyote time** lets a jump still work for a moment after walking off a ledge. **Jump buffering** remembers a press made just before landing. **Short hops** make a tap lower than a held press. Turn each off in front of the class and have a student play. The game doesn't get harder in an interesting way; it just feels unfair. These settings are invisible when they work, which is the point.

**One-sheets and screen layouts.** The one-sheet is written for a busy reader deciding whether to approve the game: one page, no filler. Walk the template once. Then introduce screen layouts, due next week: rough sketches of the title screen, the HUD, the pause menu and the win or lose screen. Ask what the player must be able to see at every moment, and where it goes. In Week 7 these sketches become real screens in UI Toolkit.

## Connecting it forward

The level built today is deliberately small and fits on one screen. Next week it grows past the screen edge, which is what makes a following camera, hazards and checkpoints necessary. The tuned jump height matters there too: every gap and ledge in Ex 04 is measured against it. The one-sheet handed in tonight is expanded section by section into the ten-pager over the next three weeks.
