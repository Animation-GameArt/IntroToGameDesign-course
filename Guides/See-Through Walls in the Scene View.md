---
title: "See-Through Walls in the Scene View"
course: GAME 1303
status: draft
unity: 6000.3.10f1
tags:
  - game1303
  - guide
  - 3d
---

# See-Through Walls in the Scene View

A trick for building 3D levels: the **Scene view** shows the inside of rooms through their walls, while the **Game view** and your builds draw the walls solid, as players see them. Seeing into every room at once makes it much easier to place furniture, keys and patrol points.

The trick comes from the two renderers in the course's URP settings. The course project already has it set up; this page explains how it works, how to set it up in another project, and how to turn it off.

## How it works

The course's URP asset, `Assets/Settings/UniversalRP`, has two renderers in its **Renderer List**:

| # | Renderer | Draws |
|---|---|---|
| 0 | `Renderer2D` (the **default**) | Sprites, tilemaps and 2D lights |
| 1 | `Universal Renderer` | 3D: meshes, depth, shadows and 3D lights |

- **Every camera** chooses one of these in its **Rendering → Renderer** setting. A 3D scene's Main Camera uses the **Universal Renderer**, so the Game view and builds draw the level properly.
- **The Scene view** has no Renderer setting. It always uses the **default** renderer, the 2D one, which doesn't sort 3D objects by depth the way the 3D renderer does. Walls further back can draw over nearer ones, and you see through them.

So the see-through Scene view is a side effect of the 2D Renderer being the default. It's handy, but Unity doesn't promise it: what shows through can change as you orbit the Scene view, and lighting there looks different from the Game view. Judge how the level really looks in the **Game view**.

## Setting it up

In the course project, this is already done. In another project:

1. **Two renderers.** Select your URP asset (in `Assets/Settings`, or the one in **Project Settings → Graphics**). Under **Rendering → Renderer List**, make sure there's a **2D Renderer** and a **Universal Renderer**. To add one, click **+** and pick the renderer asset (create one with **Assets → Create → Rendering → URP Universal Renderer** or **URP 2D Renderer**).
2. **2D as the default.** In the Renderer List, the default has **Default** after its name. If the Universal Renderer is the default, click the 2D Renderer and choose **Set Default**.
3. **3D cameras use the Universal Renderer.** In every 3D scene, select the Main Camera and set **Rendering → Renderer** to the **Universal Renderer**. A new camera starts on the default (2D), so do this for every new 3D scene. The course's 3D sample builders do it for you.

Check the result: the Game view shows solid, lit walls; the Scene view shows into the rooms.

## Turning it off

To see the level in the Scene view as the Game view shows it (to check lighting, say), make the **Universal Renderer** the default: select the URP asset, click the Universal Renderer in the Renderer List and choose **Set Default**.

**Set the 2D Renderer back to the default when you're done.** 2D scenes' cameras use the default renderer, so while the Universal Renderer is the default, 2D lights and other 2D effects stop working in them.

## If something looks wrong

| What you see | Why | Fix |
|---|---|---|
| The **Game view** shows see-through walls, or 3D lights do nothing | The Main Camera is on the 2D Renderer | Main Camera → Rendering → Renderer → **Universal Renderer** |
| The Scene view shows solid walls | The Universal Renderer is the default | Set the 2D Renderer as the default again |
| 2D lights stopped working in 2D scenes | The Universal Renderer is the default | Set the 2D Renderer as the default again |
| Everything in a 3D scene is pink | Its materials aren't URP materials | Use **Universal Render Pipeline/Lit** materials |
