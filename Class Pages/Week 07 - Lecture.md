---
title: "[Lecture] Week 7"
course: GAME 1303
week: 7
status: draft
tags:
  - game1303
  - lecture-page
---

# Week 7 — Ex 06: UI · Ten-pager due

**Exercise:** Ex 06 — UI. A main menu, a pause screen, a HUD and damage popups, completing the sandbox game.

**Also due:** the final ten-pager, in Canvas by 11:59 PM the night before class. It's the plan each student builds from, starting next week.

## Lecture topics, expanded

**UI Toolkit.** UI Toolkit builds screens the way web pages are built. A **UXML** file describes the structure: this button, inside this panel. A **USS** file describes the style: colors, sizes, spacing. A **UI Document** component puts the screen into a scene. Build a small menu live from a student's layout sketch, so the class sees a drawing become a screen. One style sheet shared by every screen is what makes a game's interface look like one design.

**Binding a HUD to variables.** The score variable from Week 3 and the health from Week 6 already announce when they change. The HUD listens to those same assets, so it never needs to ask and never falls out of date. Show the alternative, a HUD that checks every frame and reaches into the player object, and how it breaks when the player is respawned. The HUD doesn't know the player exists. It only knows the values.

**Four kinds of UI.** **Screen UI** sits on top of the game: menus and the HUD. **Diegetic** UI exists in the world, such as a computer terminal. **Spatial** UI is placed in the world but isn't part of it, such as a name floating over a character. **Meta** UI is an effect on the screen itself, such as a red flash when hurt. UI Toolkit handles screens and in-world panels, and TextMeshPro handles small world-space text such as damage numbers. Have students sort their own layout sketches into the four kinds.

**Menus, pause and usability.** Walk the screen flow every game needs: title, play, pause, win or lose, and back. Pausing is a game state, and the rest of the game reacts to it: time stops and player controls switch off. Then the basics of usable UI: text large enough to read, enough contrast, and menus that work with a gamepad as well as a mouse. Ask what the player needs to see at every moment, and remove anything else from the HUD.

## Connecting it forward

The sandbox game is complete after today: scenes, events, a player, a level, opponents and UI, all built from the scripts students will use in their own games. Next week those scripts stay the same and the subject changes. Each student imports the kit for their genre and starts their own project, with the ten-pager as the plan and the production backlog as the first week's work.
