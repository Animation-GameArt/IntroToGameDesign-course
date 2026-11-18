---
title: "Cutscenes with Timeline"
course: GAME 1303
week: 8
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Cutscenes with Timeline

**Week 8 · [[Lecture] Week 8](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2008%20-%20Lecture.md)**

> [!abstract] In one sentence
> Timeline plays a planned sequence of events over time, which is how a small game shows an opening, an ending or a door opening across the room.

## What this topic is for

Not every game needs a cutscene. Students should know what Timeline can do, see one short sequence built, and decide whether their game needs one.

## Key ideas

- **A Timeline** is an asset of tracks laid out over time: move this object, play this animation, start this sound, switch to this camera.
- **A Playable Director** on a GameObject plays the Timeline.
- **Cinemachine tracks** cut and blend between cameras during the sequence.
- **Signals** let a Timeline raise events at a moment, for example to start the level when the opening ends.
- **Player controls switch off** while a cutscene runs, and back on when it ends. The Input Reader handles this.
- **Short and skippable.** A solo game in eight weeks has room for an opening and an ending. Let players skip.

> [!note] Course scripts
> **Cutscene Player**, next to the Playable Director: switches the player's controls off while the Timeline plays, lets the player skip with Pause, and raises an event when it ends. See the [Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md).

## In class

1. Build a five-second sequence: the camera pans to a door, the door opens, the camera returns.
2. Ask which students' games need a cutscene at all.

## Where it comes up

- [Ten-Pager](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Assignments/Ten-Pager.md), page 9: cutscenes and narrative.

## Further resources

- Timeline manual, [About Timeline](https://docs.unity3d.com/Packages/com.unity.timeline@1.8/manual/index.html).
