---
title: "[Lecture] Week 5"
course: GAME 1303
week: 5
status: draft
tags:
  - game1303
  - lecture-page
---

# Week 5 — Ex 04: Level · Screen layout due

**Exercise:** Ex 04 — Level. A level wider than the screen, a following camera with bounds, hazards and checkpoints.

**Also due:** the screen layouts, in Canvas by 11:59 PM: sketches of the title screen, HUD, pause menu and win or lose screen. The ten-pager draft is due next week; read the assignment together from the page's Next week section.

## Lecture topics, expanded

**Level design: teach, test, twist.** A good level introduces one idea at a time. First a **teach beat**: the player meets the idea somewhere safe, such as a gap with a floor under it. Then a **test beat**: the same idea with something at stake. Later a **twist** combines it with another idea. Pacing is the rhythm of tense and calm stretches between them. Sketch a level on the board as a line of beats before placing a single tile. Pickups do quiet work here too: a trail of coins shows the player where to go.

**Hazards and checkpoints.** A hazard gives a mistake a cost. A checkpoint decides how big that cost is. Placed after every hard section, checkpoints keep a difficult level from being a punishing one. Placed too far apart, they make the player replay the easy parts to retry the hard one. Show both in the course project, and tie them back to the event channels from Week 3: "the player died" and "checkpoint reached" are events that the level, the camera and later the HUD can all react to.

**Tilemaps.** A Tilemap paints a level onto a grid from a palette of tiles. Cover the palette, painting and erasing, and separate Tilemaps for ground, background and hazards. Add a Tilemap Collider so the ground is solid, and show Rule Tiles choosing the right edge and corner pieces automatically. Because the character's jump height is in units and the grid is in units, students can design gaps and ledges by counting tiles.

**Cameras with Cinemachine.** Once the level is wider than the screen, the camera becomes part of the design. A Cinemachine camera follows the player with a **dead zone**, so small movements don't shake the view, and stays inside **bounds**, so it never shows past the level's edge. What the camera shows decides what's fair: a hazard the player couldn't see coming isn't a challenge.

## Connecting it forward

The level from today is where next week's enemy patrols and where its spawner sits. Checkpoints become respawn points once the player has health to lose. On paper, the screen layouts submitted tonight go straight onto page 6 of the ten-pager, and the level sketch from lab goes onto page 5.
