---
title: "UI Toolkit"
course: GAME 1303
week: 7
type: topic
status: draft
tags:
  - game1303
  - topic
---

# UI Toolkit

**Week 7 · [[Lecture] Week 7](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2007%20-%20Lecture.md)**

> [!abstract] In one sentence
> UI Toolkit builds screens the way web pages are built: a UXML file for structure, a USS file for style, and a UI Document that puts the screen in a scene.

## What this topic is for

Students turn their Week 5 layout sketches into working screens. They should leave able to put a course screen into a scene, change its layout in UI Builder, and say which file controls what.

## Key ideas

| Part | What it is | In the course project |
|---|---|---|
| UXML | The structure: this button inside this panel | `HUD`, `MainMenu`, `PauseMenu`, `EndScreen`, `GameOver`, `Credits` in `_Course/Core/UI` |
| USS | The style: colors, sizes, spacing | `CourseTheme.uss`, shared by every screen |
| UI Document | A component that shows a UXML file in a scene | **GameObject → UI Toolkit → UI Document** |
| Panel Settings | How screens scale to the window | One shared asset for every screen: `CoursePanelSettings` |
| UI Builder | The visual editor for UXML and USS | Double-click a UXML file |

- **Names connect UI to scripts.** Course components find elements by name, such as `score-label` or `play-button`. Rename an element and the connection breaks.
- **One style sheet, one look.** Every screen shares `CourseTheme.uss`, which is why the menus look like one design.
- **Sort Order** decides which UI Document draws on top.
- **Copy before changing.** Students copy a UXML file into `_Game` and edit the copy.

## In class

1. Take a student's layout sketch and rebuild it in UI Builder from the course HUD.
2. Change one rule in a copy of the style sheet and watch every element using it change.

## Common problems

| What happens | Why |
|---|---|
| A screen is blank | Source Asset or Panel Settings is empty |
| A label never updates | Its name was changed in UI Builder |
| A menu is hidden behind the HUD | Its Sort Order is lower |

## Where it comes up

- [Ex 06 — UI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md).
- [Screen Layout](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Assignments/Screen%20Layout.md): the plan for these screens.
- [Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md): every screen's element names.

## Further resources

- Unity Manual, [Introduction to UI Toolkit](https://docs.unity3d.com/Manual/ui-systems/introduction-ui-toolkit.html).
- Unity Manual, [Get started with UI Builder](https://docs.unity3d.com/Manual/UIB-getting-started.html).
