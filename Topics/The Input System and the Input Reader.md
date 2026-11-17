---
title: "The Input System and the Input Reader"
course: GAME 1303
week: 4
type: topic
status: draft
tags:
  - game1303
  - topic
---

# The Input System and the Input Reader

**Week 4 · [[Lecture] Week 4](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2004%20-%20Lecture.md)**

> [!abstract] In one sentence
> Unity's Input System describes controls as actions bound to many devices, and the course's Input Reader lets every script ask for an action without caring which device produced it.

## What this topic is for

Students should understand why their character works on keyboard and gamepad without any extra setup, and where to look if they want to change a control.

## Key ideas

- **Actions, not keys.** An action is something the player does: Move, Jump, Attack, Pause. Each action has **bindings** to keys, buttons and sticks. Move is bound to WASD, the arrow keys and the left stick at once.
- **Action maps.** Actions are grouped. **Player** holds gameplay actions; **UI** holds menu navigation.
- **The project's actions.** The course project's actions file is `Assets/_Course/Core/Input/InputSystem_Actions`. Open it to see every action and binding.
- **The Input Reader.** Course scripts never read a key. They ask the `InputReader` asset:
  - **values** that can be read any time, such as `Move`, `JumpHeld`;
  - **events** that fire at a moment, such as `JumpPressed`, `PausePressed`.
- **Switching controls off.** The Input Reader can switch the player's controls off and back on, for pause menus, cutscenes and end screens. Pause keeps working so the game can be un-paused. Controls switch back on whenever a scene loads.

## In class

1. Open the actions file and follow Move and Jump to their bindings.
2. Plug in a gamepad and play Ex 03 with no changes.
3. Show a controller's **Input** field filling itself in when the component is added.

## Common problems

| What happens | Why |
|---|---|
| Nothing responds | The Game view doesn't have focus. Click in it |
| "Input is empty" in the Console | The controller's Input field needs the `InputReader` asset |
| A student changed a binding and an update undid it | The actions file is in `_Course`. Changing controls is a custom-script conversation |

## Where it comes up

- [Ex 03 — Player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex03%20-%20Player.md), Part 4.
- [Ex 05 — Turn-Based](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat%20%28Turn-Based%29.md): Attack and Interact as menu choices.
- [Ex 06 — UI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md): Pause.

## Further resources

- Input System manual (version 1.18), [Actions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.18/manual/Actions.html).
