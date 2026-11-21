---
title: "Making a Build"
course: GAME 1303
week: 9
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Making a Build

**Week 9 · [[Lecture] Week 9](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2009%20-%20Lecture.md)**

> [!abstract] In one sentence
> A build packages the game to run without Unity, and the first one is made in Week 9 so its surprises are found early.

## What this topic is for

Every milestone from Week 10 is a build. Students make their first one in Ex 08 and learn the handful of settings that decide whether it works.

## Key ideas

- **Build Profiles** (**File → Build Profiles**) choose the platform and the scenes.
- **The Scene List** decides which scenes are included, and the first one is where the game starts. A scene left off the list is missing from the build.
- **Platforms.** Windows (or macOS) makes a folder with a program in it. **Web** makes a version that runs in a browser, which is the easiest for others to play on itch.io.
- **Errors stop builds.** A project with red errors in the Console can't be built.
- **Builds behave differently.** Things that only worked in the Editor show up now: missing scenes, menus sized for the Editor's window, Editor-only code.
- **Build early, build often.** A build made two days before a deadline leaves time to fix what it reveals.
- **Player Settings** set the game's name, icon and company name, which appear on the build.

## In class

1. Make a Web build of the course sandbox live, start to finish.
2. Leave a scene out of the Scene List and show what happens.

## Common problems

| What happens | Why |
|---|---|
| The build starts on the wrong scene | The first scene in the Scene List is wrong |
| A level is missing | Its scene isn't in the Scene List |
| Text is tiny or cut off | The UI wasn't checked at the build's window size |

## Where it comes up

- [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md): the students' step-by-step guide to Web, Windows and macOS builds, Build versus Build And Run, uploading each to itch.io, and fixes.

- [Ex 08 — Save & Build](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex08%20-%20Save%20%26%20Build.md).
- [First Playable](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Assignments/First%20Playable.md) and every milestone after it.

## Further resources

- Unity Manual, [Create and manage build profiles](https://docs.unity3d.com/Manual/create-build-profile.html).
