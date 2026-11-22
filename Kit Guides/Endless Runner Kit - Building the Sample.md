---
title: "Endless Runner Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.15.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - instructor
---

# Endless Runner Kit — Building the Sample

**For the instructor.** These steps build the kit's sample game once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Endless Runner Kit**, not this page.

Everything goes in `Assets/_Course/Kits/EndlessRunner/Sample/`, with folders `Data`, `Prefabs`, `Chunks` and `Scenes`. The art is Kenney's Pixel Platformer, already in the project at `Assets/_Course/Art/Kenney/kenney_pixel-platformer` (one tile is one unit). Tile names below match the Platformer Kit's guide.

> [!tip] The quick way
> **Collin Game → Kit Samples → Build Endless Runner Sample** builds everything on this page in a few seconds and opens the menu scene; press **Play**. It replaces the kit's `Sample` folder. It makes its own Spikes and One-Way Platform, so it doesn't need the Platformer sample. Steps have a thin trigger on their front that ends the run, like a crate. It sets the tiled sprites' images to Mesh Type Full Rect. Then work through **Test** to check it. Building by hand, step by step, is still the way to learn the kit, and checks this guide.

## Before you start

1. Pull the template project. It should be version 0.15.0 or later, with no red errors in the Console.
2. Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data

In `Sample/Data`:

| Asset | Type |
|---|---|
| `Distance`, `BestDistance`, `Coins` | Int Variable, Initial Value `0` |
| `PlayerDied` | Void Event Channel |

## Part 2 — The runner and pickups

**`Runner`**: the sprite `Characters/tile_0000`, Order in Layer `10`, tag `Player`, with:

| Component | Settings |
|---|---|
| Box Collider 2D | Size `0.7, 1`, Offset `0, -0.1` |
| Runner Controller 2D | Style **Jump**; Start Speed `6`; Max Speed `14`; Speed Gain Per Second `0.1`; Start Delay `1`; Distance `Distance`; Jump Height `3.2`; Can Slide ticked; Slide Height `0.5` |
| Health | Max Health `1`, Invulnerable Time `0`, Raise On Died `PlayerDied` |
| Coin Magnet 2D | Radius `4`, Always On unticked |
| Sprite Flipbook | Frames `Characters/tile_0000`, `Characters/tile_0001`; Frames Per Second `10` |

**`Coin`**: `tile_0151`, Order `3`, Circle Collider 2D trigger (Radius `0.3`), **Collectible** (Add To `Coins`), Sprite Flipbook (`tile_0151`, `tile_0152`, 6 fps).

**`Magnet`**: a gem tile such as `tile_0067`, tinted blue, Circle Collider 2D trigger, **Magnet Power-Up 2D** (Duration `8`).

## Part 3 — Chunks

Build each chunk in a scratch scene as in **Making a chunk** in the student guide: an empty with **Track Chunk** at `0, 0, 0`, ground with its top at `y = 0`, then saved to `Sample/Chunks`.

Ground for every chunk: a child `Ground` sprite using `tile_0022` with **Draw Mode Tiled**, Width as listed, Height `3`, positioned so its top is at `y = 0` and its left edge at the given X. Give it a **Box Collider 2D** with **Auto Tiling** ticked.

| Chunk | Length | Min · Max difficulty | Ground (left X, width) | Contents |
|---|---|---|---|---|
| `Chunk Start` | `30` | — | `0`, `30` | Nothing. Used as First Chunk |
| `Chunk Flat` | `20` | `0` · `1` | `0`, `20` | 5 coins in a row at `y = 0.5` |
| `Chunk Gap` | `20` | `0` · `0.7` | `0`, `9` and `12`, `8` | A 3-wide gap; 3 coins in an arc over it |
| `Chunk Crates` | `20` | `0` · `1` | `0`, `20` | Two crates (`tile_0026`, Box Collider 2D, Damage On Touch) at X `8` and `15` |
| `Chunk Steps` | `20` | `0.3` · `1` | `0`, `20` | Raised blocks (`tile_0000`, solid) one and two high, coins on top |
| `Chunk Low Bar` | `20` | `0.3` · `1` | `0`, `20` | A bar of `tile_0028` at `y = 1.2`, 3 wide, with Damage On Touch: slide under it |
| `Chunk Double Gap` | `24` | `0.3` · `1` | `0`, `7`; `10`, `5`; `18`, `6` | Two 3-wide gaps |
| `Chunk Spikes` | `20` | `0.6` · `1` | `0`, `20` | Three Spikes (from the Platformer sample) spread out; a Magnet at X `10`, `y = 3` |
| `Chunk Platforms` | `24` | `0.6` · `1` | `0`, `6` and `20`, `4` | One-way platforms (from the Platformer sample) across the gap at heights `1` and `2` |
| `Chunk Gauntlet` | `24` | `0.8` · `1` | `0`, `24` | Crate, Spikes, Low Bar, Crate, close together |

Check every gap at Max Speed `14`: a full jump covers about 9 units.

## Part 4 — Runner Systems

An empty `Runner Systems` at `0, 0, 0`, made into a prefab, with these children:

**`Track`** — at `-10, 0, 0`, with **Track Spawner 2D**: First Chunk `Chunk Start`, Chunks: the other nine, Build Ahead `40`, Remove Behind `20`.

**`Pit`** — at `0, -8, 0`, a Box Collider 2D trigger, Size `100000, 2`, **Kill Zone**. It's that long so no run can outrun it. (Don't make it a child of the runner: a child's collider becomes part of the runner's own body.)

**`Background`** — three sprites from `Tiles/Backgrounds`, each with Draw Mode **Tiled**, Width three times the sprite, and **Parallax 2D**: far layer Distance `0.9`, Order in Layer `-30`; middle `0.7`, `-20`; near `0.4`, `-10`.

**`HUD`** — UI Document `RunnerHUD` (from `Kits/EndlessRunner/UI`), with a **UI Variable Binder**: `distance-label` → `Distance` → `{0} m`; `best-label` → `BestDistance` → `Best: {0} m`; `coins-label` → `Coins` → `Coins: {0}`.

**`Best`** — **High Score**: Score `Distance`, Best `BestDistance`, Save Name `Runner`.

**`Reset`** — a **Variable Resetter** with `Distance` and `Coins`.

**`Pause Menu`**, **`Settings`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Game Over`** — UI Document `GameOver`, hidden, shown by a **Void Event Listener** on `PlayerDied`; `score-label` → `Distance` → `{0} m`; Try Again → **ReloadScene**; Menu → To Menu **Load**.

## Part 5 — The game scene (`Runner_Game`)

1. `Runner` at `0, 1, 0`.
2. Select `Runner` and choose **GameObject → Cinemachine → Targeted Cameras → 2D Camera**. Lens Orthographic Size `6`. On its **Position Composer**, set **Screen Position X** to `-0.25`, so the runner sits left of centre and the player sees what's coming. Set Damping Y to `1`.
3. Main Camera background: a sky color.
4. `Runner Systems`.

## Part 6 — Menu

`Runner_Menu`: like the Platformer sample's menu, with Play loading `Runner_Game`, and a label bound to `BestDistance` (`Best: {0} m`). Add a **High Score** (Score `Distance`, Best `BestDistance`, Save Name `Runner`) so the best is loaded on the menu.

## Part 7 — Scene List

`Runner_Menu`, `Runner_Game`.

## Part 8 — Test

- [ ] After a second, the runner starts running and speeds up.
- [ ] Tap Jump for a short hop; hold for a full jump.
- [ ] Holding down slides under the Low Bar.
- [ ] Gaps, crates and spikes end the run; falling into a gap ends it too.
- [ ] Chunks join without gaps or steps, and new chunks keep coming.
- [ ] After about 30 seconds, medium chunks appear; after about a minute, hard ones.
- [ ] Coins add to the HUD; the Magnet pulls in coins for 8 seconds.
- [ ] Distance counts up; after a run, Best shows the longest, also after restarting Unity.
- [ ] Background layers move at different speeds and never show an edge.
- [ ] Game Over shows the distance; Try Again starts a fresh run.
- [ ] Esc pauses.

Note anything that fails, with the Console message.

## Part 9 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/EndlessRunner` with **Assets → Export Package**. It uses prefabs and art from the Platformer Kit (Spikes, One-Way Platform, the Pixel Platformer pack): tick them in the export, or copy what's needed into this kit's `Sample` folder first.
