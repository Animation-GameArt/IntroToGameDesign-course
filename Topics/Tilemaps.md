---
title: "Tilemaps"
course: GAME 1303
week: 5
type: topic
status: draft
tags:
  - game1303
  - topic
---

# Tilemaps

**Week 5 · [[Lecture] Week 5](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Class%20Pages/Week%2005%20-%20Lecture.md)**

> [!abstract] In one sentence
> A Tilemap paints a level onto a grid from a palette of tiles, which is how most 2D levels in the course are built.

## What this topic is for

Students should be able to make a palette, paint solid ground on one Tilemap and hazards on another, and understand why one tile equals one unit.

## Key ideas

- **The pieces:**

| Piece | What it is |
|---|---|
| Sprite | An image file in the Project window |
| Tile | An asset made from a sprite, which can be painted |
| Tile Palette | A window of tiles to paint with |
| Grid | The object that holds Tilemaps and sets the cell size |
| Tilemap | One painted layer, such as ground or hazards |

- **Tiles are made from files.** A tile can only be made from a sprite in the **Project** window. A sprite object dragged from the Hierarchy goes into the palette but paints nothing, and the brush shows only an outline.
- **Separate layers by purpose.** Ground on one Tilemap with a solid collider. Hazards on another with a trigger collider and a Kill Zone or Damage On Touch. Decoration on a third with no collider.
- **Colliders.** A Tilemap Collider 2D gives every tile a shape. A Composite Collider 2D merges them into one smooth outline, so characters don't catch on seams.
- **One tile, one unit.** The course's art packs import at one tile per unit, so a three-unit jump clears three tiles. Levels can be designed by counting.

## In class

1. Make a palette from one sprite file, live, and point out the dialog that asks where to save the tile. That dialog means it worked.
2. Paint ground, add colliders, and play.
3. Add a hazard layer.

## Common problems

| What happens | Why |
|---|---|
| The brush shows only an outline and paints nothing | The palette holds a scene object, not a tile. Remake it from a sprite file |
| Painting does nothing | Wrong **Active Target**, or the Paint tool isn't selected |
| The player snags on edges | No Composite Collider 2D, or Composite Operation isn't **Merge** |
| Thin lines between tiles | Add a Sprite Atlas with padding |

## Where it comes up

- [Ex 04 — Level](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md), Parts 3 and 4.
- [Platformer Kit sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit%20-%20Building%20the%20Sample.md), Part 4.

## Further resources

- Unity Manual, [Create tile assets](https://docs.unity3d.com/6/Documentation/Manual/tilemaps/tiles-for-tilemaps/create-tile-assets.html).
- Unity Manual, [Tile palette tools](https://docs.unity3d.com/Manual/tile-palette-tools-landing.html).
