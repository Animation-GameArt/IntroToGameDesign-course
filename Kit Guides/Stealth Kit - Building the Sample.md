---
title: "Stealth Kit — Building the Sample"
course: GAME 1303
status: draft
audience: instructor
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - 3d
  - instructor
---

# Stealth Kit — Building the Sample

**For the instructor.** These steps build the kit's sample level once, in the template project. Building it tests every kit script, and the result is what students import. Students read **Stealth Kit**, not this page.

Everything goes in `Assets/_Course/Kits/Stealth/Sample/`, with folders `Data`, `Materials`, `Prefabs` and `Scenes`. The level is built from Unity's basic shapes.

> [!tip] The quick way
> **Collin Game → Kit Samples → Build Stealth Sample** builds everything on this page in a few seconds and opens the menu scene; press **Play**. It replaces the kit's `Sample` folder. It builds its own player, bakes the NavMesh into `Sample/Scenes`, and uses the kit's `Audio/Heartbeat.wav` for Alert Audio. Then work through **Test** to check it. Building by hand, step by step, is still the way to learn the kit, and checks this guide.

## Before you start

1. Pull the template project. It should be version 0.22.0 or later, with no red errors in the Console.
2. Check **AI Navigation** is in **Window → Package Manager → In Project** (version 2.0.16; it's in the course project's manifest).
3. The 3D Platformer sample's orbit camera (Part 4 of its guide) is reused here; build that first, or follow its Part 4 again.
4. Every UI Document uses `CoursePanelSettings`.

## Part 1 — Data and materials

In `Sample/Data`: `Keys` (Int Variable, `0`), `Battery` (Float Variable, `100`), `Message` (String Variable, empty), and Void Event Channels `ExitOpened`, `Escaped`, `Caught`.

In `Sample/Materials` (shader **Universal Render Pipeline/Lit** unless noted): `Floor` (`4A4F5C`), `Wall` (`8A8F9C`), `Furniture` (`6B5640`), `Locker` (`5C7A8C`), `Key` (`FFD23F`, Emission ticked), `Guard` (`C04848`). And `Vision`: shader **Universal Render Pipeline/Unlit**, Surface Type **Transparent**, Render Face **Both**, color white at 30% alpha.

## Part 2 — The building

1. A new scene from **Basic (Built-in)**, saved as `Sample/Scenes/NightShift_Level`. Main Camera → Renderer: **Universal Renderer**.
2. **Lighting:** set the Directional Light's Intensity to `0.15` and its color to a dark blue (`4060A0`). In **Window → Rendering → Lighting → Environment**, set Environment Lighting Intensity to `0.3`. Add a few dim **Point Lights** (Intensity `2`, Range `6`, warm color) in some rooms, and leave others dark.
3. An empty `Level`. Inside it, a floor Cube `30 × 0.2 × 20` (`Floor`), and walls `0.3` thick and `3` high (`Wall`) making five rooms around a corridor, with door gaps 2 units wide:
   - **Lobby** (start), **Office** (desks), **Storage** (shelves and lockers), **Break Room**, **Security** (the exit is here).
4. Furniture (`Furniture`): desks (`2 × 1 × 1`) in the Office, shelves (`3 × 2.5 × 0.6`) in Storage that block sight lines. Give every wall and piece of furniture its collider.
5. **Add Component → NavMesh Surface** on `Level`, and click **Bake**. A blue overlay should cover the floor, but not the furniture.

## Part 3 — The player

1. Reuse the 3D Platformer sample's `Player` (or build it the same way), at the Lobby's far end.
2. **Player Controller 3D**: Facing **Face Movement**, Walk Speed `4`, Sprint Speed `6.5`, Can Crouch ticked, Crouch Speed `1.8`, Crouch Height `1`, Can Jump unticked.
3. **Stealth Target 3D**: Look Point empty.
4. A child **Spot Light** `Flashlight` at `0, 1.4, 0.3`, pointing forward: Range `15`, Spot Angle `45`, Intensity `8`. Add **Flashlight 3D**: Battery Seconds `120`, Battery Percent `Battery`, Flicker Below `20`, On At Start unticked.
5. No Health or Respawner: being caught ends the game.
6. The orbit camera as in the 3D Platformer sample, with Radius `5`, and **Cursor Lock 3D**.

## Part 4 — Guards

`Guard` prefab, in `Sample/Prefabs`: a Capsule (`Guard`), with a child Cube for a visor at head height so you can see which way it looks.

1. **NavMesh Agent**: Radius `0.4`, Height `2`, Angular Speed `360`, Acceleration `12`, Stopping Distance `0.3`.
2. **Guard 3D**: Patrol Speed `2`, Wait At Point `1.5`; View Distance `11`, View Angle `90`, Eye Height `1.6`, Time To Spot `1`, Flashlight Sight Bonus `1.5`; Hearing Range `10`; Investigate Speed `3`, Look Around Time `4`, Chase Speed `4.5`, Lose Track After `3`, Calm Down Rate `0.15`, Catch Distance `1.2`; Raise On Caught `Caught`.
3. A child `Vision Cone` at `0, 0.05, 0`: **Mesh Filter**, **Mesh Renderer** (material `Vision`), **Vision Cone 3D** (Rays `24`).

In the level:

- `Guard A` patrols the corridor and the Office: four points, a loop, passing the Office desks.
- `Guard B` patrols Storage and the Break Room: four points, with a long wait in the Break Room doorway.

Patrol points are empty objects in a `Routes` group, not children of the guards.

## Part 5 — Hiding, keys and the exit

- **Lockers** (three, in Storage and the corridor): an open-fronted box the player can step into, made of thin Cubes (`Locker`) for the back, the two sides and the top, about `1.2` wide, `2.4` high and `1` deep inside. Inside it, an empty with a trigger Box Collider filling the space, and **Hiding Spot 3D** (Needs Crouch unticked). Hidden players can't be seen, so place lockers where a guard walks close by, for tension.
- **Desks** (in the Office): a trigger under each desk with **Hiding Spot 3D**, Needs Crouch ticked.
- **Keys**: `Key 1` in the Office (between the desks), `Key 2` in Storage (behind the shelves), `Key 3` in the Break Room (on the table). Each a small Cube or Cylinder (`Key`), trigger collider, **Collectible**: Add To `Keys`, Amount `1`; **Spin 3D**.
- **Battery**: one in Storage. A small Cube with **Collectible** (Add To empty); On Collected → `Flashlight` → **Flashlight3D → AddBattery** `50`.
- **Exit**: in Security, a door Cube `Exit Door` closing a gap, and behind it a trigger `Exit Zone` with **Trigger Zone**: Raise On Enter `Escaped`.
- **`Exit Logic`**: an **Int Variable Condition**: Variable `Keys`, At Least `3`, Raise Event `ExitOpened`. A **Void Event Listener** on `ExitOpened`: `Exit Door` → **GameObject.SetActive** (unticked), and `Message` → **StringVariable.SetValue** `The exit is open. Get to Security!`.

## Part 6 — Stealth Systems

An empty `Stealth Systems`, made into a prefab:

**`HUD`** — UI Document `StealthHUD` (from `Kits/Stealth/UI`), with **UI Stealth HUD** (Battery Percent `Battery`), and a **UI Variable Binder**: `objective-label` → `Keys` → `Keys: {0} / 3`; `message-label` → `Message` → `{0}`.

**`Alert Audio`** — an Audio Source with a looping heartbeat (from Kenney's sound packs, or any short low thump), Loop and Play On Awake ticked, Spatial Blend `0`; **Alert Audio**: Calm Volume `0`, Alert Volume `0.8`, Chase Pitch `1.25`.

**`Reset`** — a **Variable Resetter** with `Keys`, `Battery` and `Message`.

**`Pause Menu`**, **`Settings`**, **`Scene Changer`**, **`To Menu`** — as in the Platformer Kit sample.

**`Escaped`** — UI Document `EndScreen`, hidden, shown on `Escaped`; title *You Escaped*; also calls **CursorLock3D → Unlock**.

**`Caught`** — UI Document `GameOver`, hidden, shown on `Caught`; Try Again → **ReloadScene**; also calls **CursorLock3D → Unlock**.

## Part 7 — Menu

`NightShift_Menu`, like the Platformer sample's menu, with Play loading `NightShift_Level`. Scene List: `NightShift_Menu`, `NightShift_Level`.

## Part 8 — Test

- [ ] Guards walk their routes and pause at each point; their vision cones sweep the floor and stop at walls.
- [ ] Standing in a cone fills the alert meter, faster up close; the HUD says *Suspicious*, and the cone turns orange.
- [ ] Ducking out of sight before the meter fills: the guard comes to look, looks around, and goes back to its route.
- [ ] A full meter: *Spotted!*, the cone turns red, the guard runs at the player, and the heartbeat speeds up.
- [ ] Getting caught shows the caught screen with the pointer back.
- [ ] Sprinting near a guard (even behind it) makes it come to look; walking past at the same distance doesn't; crouching right behind it doesn't.
- [ ] Inside a locker, a guard can look straight at the player and see nothing; under a desk only while crouching.
- [ ] Losing a chase by breaking line of sight and hiding: the guard searches, then gives up.
- [ ] The flashlight toggles with a left click, drains the battery bar, flickers below 20%, and goes out when empty; the battery pickup refills it.
- [ ] With the flashlight on, guards spot the player from farther away.
- [ ] Collecting three keys opens the exit and shows the message; reaching it shows the escaped screen.
- [ ] Esc pauses the guards and brings the pointer back.
- [ ] **Balance:** play twice carefully and once carelessly. A careful player should usually escape; a careless one should usually be caught.

Note anything that fails, with the Console message.

## Part 9 — Commit

Commit and push the `Sample` folder with its `.meta` files.

## Later — Exporting the kit

Export `Assets/_Course/Kits/Stealth` with **Assets → Export Package**, unticking Core and 3D scripts that Unity adds as dependencies. Students' projects get AI Navigation from the course project's manifest.
