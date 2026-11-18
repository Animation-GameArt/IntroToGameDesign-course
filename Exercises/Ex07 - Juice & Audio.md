---
title: "Exercise 07 — Juice & Audio"
course: GAME 1303
week: 8
status: draft
course_version: 0.10.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 07 — Juice & Audio

**Week 8 · in your own game · submitted at the end of class**

From this week, exercises happen in your own game. In this one you make your game answer the player: sound for the three actions the player does most, background music, a camera shake, and a short freeze on a big hit.

> **Your course project must be version 0.10.0 or later.** Check `Assets/_Course/VERSION.txt`. If it's older, import the latest update package from the Releases page first.

## What you'll learn

- How to bring sounds into your project and credit them
- How a **Sound Effect** asset plays from any event in the Inspector
- How music carries from scene to scene
- How to shake the camera, and how to freeze the game on a hit
- How to choose which moment deserves the biggest reaction

## Part 1 — Get some sounds

1. Download one or two free sound packs. Kenney's audio packs are CC0, so they're free to use for anything. For example, **Impact Sounds**, **Interface Sounds** or **Digital Audio** from [kenney.nl](https://kenney.nl).
2. Find one piece of music that loops, with a license that allows use in a published game. CC0 is simplest.
3. In your project, create `Assets/_Game/Audio`, and drag the sound files and the music in.
4. Open `Assets/_Game/Credits` and add an entry for each pack and for the music: its name, its author, where it came from, and its license.

## Part 2 — Choose your three actions

Write down the three actions the player does most in your game. Use the table to find the event that fires for each.

| Action | Component | Event |
|---|---|---|
| Jump, land | Platformer Controller 2D | **On Jump**, **On Land** |
| Collect | Collectible | **On Collected** |
| Get hurt, heal, die | Health | **On Damaged**, **On Healed**, **On Died** |
| Stomp an enemy | Stompable Enemy 2D | **On Stomped** |
| Spring | Bounce Pad 2D | **On Bounce** |
| Reach a checkpoint | Checkpoint | **On Activated** |
| Something spawns | Spawner | **On Spawned** |
| Attack, heal (turn-based) | Turn Actions | **On Attack**, **On Heal** |
| Enter an area | Trigger Zone | **On Enter** |

## Part 3 — Make Sound Effects

For each of your three actions:

1. In `Assets/_Game/Audio`, right-click and choose **Create → Collin Game → Audio → Sound Effect**. Name it after the action, such as `Jump`.
2. Select it. Under **Clips**, click **+** and drag in one sound. If you have two or three similar sounds, add them all; a different one plays each time.
3. Leave **Pitch Variation** at `0.05` for now.

**Connect it.** For a prefab, such as a coin, open the prefab (or your variant of it) so the change applies to every copy.

1. Select the object that has the event, such as `Player`.
2. Find the event, such as **On Jump**, and click **+**.
3. Drag the **Sound Effect asset** from the Project window into the object field.
4. Open the function dropdown and choose **SoundEffect → Play**.

Press **Play** and do each action. Then change **Pitch Variation** on one sound to `0` and repeat the action ten times. Put it back.

## Part 4 — Music

1. In each scene that should have music, create an empty GameObject named `Music`.
2. Add the **Music Player** component and drag your music into **Music**.
3. Set **Volume** to about `0.5`. Music should sit under the sound effects, not on top of them.

If two scenes use the same music, it carries on across the scene change without restarting. Different music fades over the old one.

## Part 5 — A camera shake

1. Select your **Cinemachine camera**. Click **Add Extension** and choose **Cinemachine Impulse Listener**. Without the listener, nothing shakes.
2. Select `Player`, or whatever gets hurt in your game, and add the **Camera Shake** component. A **Cinemachine Impulse Source** is added with it.
3. On its **Health**, find **On Damaged**, click **+**, drag in the same object, and choose **CameraShake → Shake**.

Press **Play** and take damage. Then try **Strength** at `0.3` and at `3`.

## Part 6 — A hit stop

A hit stop freezes the game for a few hundredths of a second, which makes a hit feel heavy.

1. Add the **Hit Stop** component to `Player`. Keep it on an object that stays in the scene.
2. Choose one big moment, such as **On Stomped** on an enemy, or **On Damaged** on the player, and add **HitStop → Stop**, with `Player` as the object.

Try **Duration** at `0.03`, `0.06` and `0.15`.

## Part 7 — Your design decision

Choose the **one** moment in your game that deserves the biggest reaction: a boss defeated, the level completed, a rare item found. Give it more than anything else: a louder or longer sound, a stronger shake, a longer stop, or all three. Keep everything else smaller, so this moment stands out.

Be ready to say which moment you chose, and why.

## Check-off

Submit in Canvas, by the end of class: a short screen recording (about 30 seconds) or three screenshots of the Inspector, plus two sentences about your design decision.

- [ ] Three common actions each play a sound.
- [ ] Music plays, and it's quieter than the effects.
- [ ] The camera shakes when the player is hurt (or at another moment you chose).
- [ ] One moment has a hit stop.
- [ ] Your credits list every sound and the music.
- [ ] You can name your biggest moment and how it's different from the rest.

## If something goes wrong

| What you see | What to do |
|---|---|
| No sound at all | Check that the **Clips** list isn't empty, and that the Game view's **Mute Audio** button is off |
| **SoundEffect → Play** isn't in the dropdown | You dragged in an object from the Hierarchy. Drag the asset from the **Project** window |
| The camera doesn't shake | The Cinemachine camera needs the **Cinemachine Impulse Listener** extension |
| The game stays frozen | The **Hit Stop** is on an object that was destroyed. Put it on the player |
| Music restarts on every scene | Each scene's Music Player must use the same music file |

## Related topics

- [Feedback and Juice](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Feedback%20and%20Juice.md)
- [Sound and Music](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Sound%20and%20Music.md)
- [Camera Shake and Hit Pause](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Camera%20Shake%20and%20Hit%20Pause.md)
- [Credits and Licenses](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Credits%20and%20Licenses.md)
