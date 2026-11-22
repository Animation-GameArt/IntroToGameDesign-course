---
title: "Minimap Add-On"
course: GAME 1303
status: draft
course_version: 0.28.0
unity: 6000.3.10f1
tags:
  - game1303
  - guide
  - 3d
  - add-on
---

# Minimap Add-On

A top-down map in the corner of the screen, for any 3D game where the player finds their way around: a stealth game, an adventure, a maze, a racing track. Seeing the level from above helps players plan. In a stealth game they can see where the guards are, which way they face, and which way their vision cones point.

- **M** shows or hides the map.
- Holding **Tab** shows a big map in the middle of the screen, showing more of the level.
- Colored **markers** show what matters: the player as an arrow, enemies, keys, the exit.

It's an add-on: no kit needs it, and you can add it to a finished game in about ten minutes. This page adds it to the Stealth Kit's sample, **Night Shift**, as the example.

## What's in it

In `Assets/_Course/ThreeD/Minimap`:

| File | What it does |
|---|---|
| `Minimap3D` | Makes a second camera that looks straight down on the player and draws into a picture; shows the picture in the corner; M and Tab |
| `MinimapMarker3D` | Shows an object on the map as a colored dot, square or arrow |
| `Minimap.uxml`, `Minimap.uss` | The map's frame on screen: its size, place and border |

## How it works

The map is a second camera, made by Minimap 3D when the scene starts. It's high above the player, looking straight down, **orthographic** (no perspective, so the map is to scale), and it draws into a picture instead of onto the screen. A UI Document shows the picture.

The markers float a few units above their objects, on a layer called **Minimap**. The map camera draws that layer; the game's main camera is set not to, so the markers only appear on the map.

## Setting it up

### 1. The Minimap layer

**Edit → Project Settings → Tags and Layers**. Under **Layers**, type `Minimap` in the first empty User Layer.

Without it, the map still works, but the markers also float over the objects in the game view, and the Console says so.

### 2. The map

1. On the scene's systems object (in Night Shift, `Stealth Systems`), add a child: **Create Empty**, named `Minimap`.
2. Add a **UI Document**: Panel Settings `CoursePanelSettings`, Source Asset `Minimap` (from `ThreeD/Minimap`), **Sort Order** `1`. That's above the HUD (`0`) and below the pause menu (`10`), so the pause menu covers the map.
3. Add **Minimap 3D** (**Add Component → Collin Game → 3D → Minimap 3D**):

| Setting | Night Shift | What it does |
|---|---|---|
| Target | (empty) | What the map centres on. Empty: the object tagged Player |
| View Size | `12` | How much the small map shows: units from its centre to its top edge |
| Big View Size | `16` | How much the big map shows. Night Shift is 30 × 20, so `16` shows nearly all of it |
| Height | `40` | How high the map camera is. Above the tallest wall or tree |
| Turn With Target | unticked | Unticked: north is always up. Ticked: the map turns so up is the way the player faces |
| Show Layers | Everything | What the map draws (markers are always drawn) |
| Renderer Index | `1` | The Universal (3D) Renderer, as the main camera uses |
| Toggle Key, Big Map Key | `M`, `Tab` | |

If the systems object is a prefab, apply the changes to the prefab (**Overrides → Apply All**), or make the change in the prefab itself.

### 3. Markers

Add **Minimap Marker 3D** (**Add Component → Collin Game → 3D → Minimap Marker 3D**) to each thing worth seeing on the map. Edit the prefabs, so every copy gets one.

| Object | Shape | Color | Size | Order |
|---|---|---|---|---|
| `Player` | Arrow | `4FC3F7` (light blue) | `1.8` | `10` |
| `Guard` | Arrow | `E05050` (red) | `1.8` | `5` |
| `Key` | Dot | `FFD23F` (gold) | `1.2` | `1` |
| `Exit Zone` (in the scene) | Square | `6BD66B` (green) | `2` | `0` |

**Height Above** (default `4`) is how far above the object its marker floats. Keep it above the object's top, and above walls the object stands beside, or they hide it on the map. Night Shift's walls are 3 high, so the default works.

An **Arrow** turns with its object, so the map shows which way the player and guards face. A key's marker goes when the key is picked up, because the key is destroyed.

## Test

- [ ] The map shows in the top-right corner, with the player's arrow in the middle, pointing the way they face.
- [ ] The map moves with the player; north stays up (with Turn With Target unticked).
- [ ] Walls, furniture, guards and their vision cones show from above. The cones turn orange and red on the map too.
- [ ] Guards' red arrows, the gold keys and the green exit show; a key's dot goes when it's picked up.
- [ ] The markers don't show in the game view.
- [ ] **M** hides and shows the map.
- [ ] Holding **Tab** shows the big map, showing nearly the whole building; letting go puts it back in the corner.
- [ ] Esc pauses: the pause menu covers the map, and M and Tab do nothing while paused.
- [ ] No warnings in the Console.

## Making it your own

**Where it is, and its size.** Change `.minimap-frame` in `Minimap.uss`: `top` and `right` (or `bottom` and `left`) for its place, `width` and `height` for its size. `.minimap-frame--big` is the big map. For a round map, set `border-radius` to half the width.

**Turning with the player.** Tick **Turn With Target** for a map where up is always the way the player faces, as in many racing and open-world games. Untick it (north up) for planning, as in stealth and strategy.

**Indoors, with ceilings.** The map camera sees roofs and ceilings first. Put them on their own layer (add one called `Ceiling`), and untick that layer in **Show Layers**: the map then shows into the rooms. (The Scene view's see-through walls, in **See-Through Walls in the Scene View**, help when you're placing things.)

**A map you have to find.** Untick **Visible At Start**, and call **Minimap3D → Show** from a pickup's **On Collected**: the map works once the player finds it.

**Markers that change.** **Minimap Marker 3D → SetColor** changes a marker's color while playing. For example, a door's square could go from red to green when it unlocks.

**Hiding things from the map.** The map draws every layer in Show Layers. Put things you don't want on it (a secret room, say) on their own layer and untick it.

**A different renderer.** In a project whose URP asset lists the renderers in a different order, set **Renderer Index** to the Universal Renderer's number in the asset's **Renderer List**. Night Shift's Main Camera uses the same one.

## If something goes wrong

| What you see | Fix |
|---|---|
| No map at all | The UI Document's Source Asset is `Minimap`, its Panel Settings are set, and Minimap 3D is on the same object (or its **Document** field is set). Check the Console |
| The map is black, or shows only the background color | **Height** is above everything; **Renderer Index** is the Universal Renderer; **Show Layers** isn't Nothing |
| The map doesn't follow the player | The player is tagged **Player**, or drag it into **Target** |
| Markers float over things in the game view | Add the `Minimap` layer (step 1) |
| A marker is hidden on the map | Raise its **Height Above** over the walls around it |
| The map covers the HUD | Move it in `Minimap.uss`, or move the HUD element |
