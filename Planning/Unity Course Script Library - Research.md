---
title: Unity Course Script Library — Research & Planning
created: 2026-11-02
status: planning
course: GAME 1303
unity: 6000.5+
tags:
  - unity
  - gamedev
  - teaching
  - script-library
  - planning
---

# Unity Course Script Library — Research & Planning

> [!abstract] Goal
> A shared set of basic scripts covering most game types, for use in college game courses. Targets **Unity 6000.5+** and uses the **Input System**, **UI Toolkit**, **ScriptableObjects**, **Cinemachine**, **TextMeshPro**, **Timeline** and **Tilemaps**. This note covers research and planning only. No code yet.

---

## 1. Architecture: three layers

1. **Core** is used by every game: input, game state, save, audio, UI shell, events.
2. **Dimension modules** hold movement, camera, physics and presentation building blocks: 2D, 3D, 2.5D, VR, AR, Narrative.
3. **Genre kits** are thin layers that combine Core and a dimension module into a playable starting point, such as a platformer or a twin-stick shooter.

Shared gameplay systems live in a **Common Gameplay** layer that sits between Core and the genre kits. Examples are inventory, grid, turn manager and stat modifiers. Genre kits never duplicate these.

- Each layer is its own **assembly definition** and namespace, for example `CollinGame.Core`, `CollinGame.TwoD` and `CollinGame.Genres.Platformer`.
- Students import only what their game needs, so nothing pulls in XR packages by accident.
- Cross-type genres such as roguelike, tower defense and tactics are **genre kits that can sit on any dimension module**.

---

## 2. Unity 6.5 notes that affect the plan

> [!warning] Use URP for everything
> The Built-In Render Pipeline is officially deprecated as of Unity 6.5. 2D lights and shadows also require URP.

- **Version strategy.** 6.5 is a *Supported* release that builds on 6.3 LTS and progresses toward **6.7 LTS**. Lock one version per semester, and plan to move to 6.7 LTS when it ships.
- **2D physics.** `LowLevelPhysics2D` was renamed to **PhysicsCore2D** and moved to the `Unity.U2D.Physics` namespace. Student-facing scripts stay on standard `Rigidbody2D`, because PhysicsCore2D is still changing and is aimed at large-scale simulation.
- **2D additions in 6.5:** custom 2D lights and shadows, a 2D Profiler module, and a sprite blend shape API.
- **TextMeshPro.** Still maintained: 6.5 added new TMP callbacks for custom asset loading. TMP is now part of the uGUI package.
- **Graph Toolkit.** Became part of the Editor core in 6.4. 6.5 added creating and editing graphs programmatically. Only relevant if we ever build a custom dialogue or quest graph editor.

---

## 3. Genre map by type

### 2D
- Platformer, precision platformer
- Metroidvania
- Top-down action/adventure (Zelda-like)
- Twin-stick or top-down shooter
- Shmup (vertical or horizontal scrolling)
- Endless runner
- Roguelike or roguelite (dungeon crawler)
- Puzzle: grid/Sokoban, match-3, physics puzzle
- Tower defense
- Turn-based tactics
- Card game or deckbuilder
- Idle/clicker
- Farming or life sim
- Point-and-click adventure
- Arcade classics (Pong, Breakout, Asteroids), which make good first assignments
- Fighting (1v1)

### 3D
- FPS
- Third-person action/adventure
- 3D platformer
- Racing (arcade or kart)
- Survival/crafting
- Horror, stealth
- Walking sim/exploration
- RPG (action or open-world-lite)
- RTS or city builder
- Physics sandbox
- Sports

### 2.5D
- Side-scroller with 3D art (constrained to a plane)
- Isometric ARPG (Diablo-like)
- Isometric tactics
- Sprites in a 3D world ("HD-2D", Paper Mario style)
- Fixed-camera adventure

### VR
- Interaction sandbox
- Wave shooter
- Escape room/puzzle
- Rhythm
- Exploration/locomotion
- Simulation/training

### AR
- Tabletop or board game on a detected plane
- Object placement or viewer
- Image-target experiences
- Location/scavenger hunt
- Face filters

### Narrative / dialogue
- Visual novel
- Dating sim
- Interactive fiction
- Detective/mystery
- Dialogue-driven RPG
- Branching cutscene game

---

## 4. Core scripts (every project)

### Architecture (ScriptableObject-driven)
- **Event channels:** `VoidEventChannel`, `IntEventChannel`, `FloatEventChannel`, `GameObjectEventChannel`, plus a generic listener component.
- **Shared variables:** `FloatVariable`, `IntVariable`, `BoolVariable`, with a `Reference` wrapper that accepts either a constant or a variable.
- **Runtime sets:** `RuntimeSet<T>`, e.g. all active enemies.
- **Generic `StateMachine<T>`:** used by the player, AI and game flow.

### Game flow
- `GameManager` / game state SO: Boot, Menu, Playing, Paused, GameOver, Win.
- `SceneLoader` with async loading, a fade transition and a loading screen.
- `Bootstrapper`: a persistent scene for managers, so students can press Play from any scene.

### Input (new Input System)
- `InputReader` SO that wraps one `.inputactions` asset and exposes C# events. Gameplay scripts never touch the Input System directly.
- Action maps: Player, UI, Vehicle, XR.
- Control-scheme detection (keyboard/gamepad) for swapping on-screen prompts.
- Key rebinding plus saving the bindings.

### UI (UI Toolkit)
- Main menu, pause, settings, game-over and credits screens: UXML templates plus a shared USS theme.
- `HUDBinder` using runtime data binding to SO variables, so values like health and score update without polling.
- `ScreenManager` to push and pop UI screens.
- World-space TMP popup text (damage numbers, pickups).
- See also [[#7. UI strategy — screen, diegetic & world-space]].

### Systems
- `AudioManager`: music crossfade, pooled SFX, Audio Mixer volume groups, plus `SoundEffectSO` with random pitch and volume.
- `SaveSystem`: JSON to `persistentDataPath`, an `ISaveable` interface, and save slots.
- Settings persistence (volume, resolution, bindings).
- Object pooling built on `UnityEngine.Pool`.
- `Timer` and `Cooldown` utilities.

### Gameplay primitives
- `Health` + `IDamageable` + `DamageInfo`, with `HealthDataSO` for stats.
- `Pickup` / `Collectible` + score/currency SO.
- `IInteractable` + interaction prompt.
- `Spawner` / `WaveDataSO`.
- Cinemachine Impulse camera shake helper.
- `Checkpoint` / respawn.

### Production
- Timeline `SignalReceiver` hooks plus a `CutscenePlayer` that disables input during cutscenes.
- Debug overlay/dev console: god mode, skip level, FPS.
- Optional localization hook (Unity Localization package).

---

## 5. Dimension-module scripts

### 2D
- `PlatformerController2D` (Rigidbody2D) with coyote time, jump buffering, variable jump height and a ground check.
- `TopDownMover2D`.
- `GridMover2D` for tile-locked movement.
- `ParallaxLayer`.
- One-way platforms, moving platforms.
- `SpriteFlash` hit feedback.
- Animator bridge (parameters driven from velocity).
- **Tilemap utilities:** hazard, ice and conveyor tiles via Rule Tiles; destructible tiles; tile-query helpers (what's at this cell?).
- Cinemachine 2D: Position Composer + Confiner2D room setup.
- 2D Light flicker.

### 3D
- `FirstPersonController` (CharacterController).
- `ThirdPersonController` with Cinemachine 3 orbital camera.
- Camera-relative input.
- `NavMeshAgentAI` (AI Navigation package) with patrol, chase and attack states.
- Raycast interactor.
- Physics pickup/throw.
- Footsteps by surface.
- Spline follower (Splines package).
- Door, lever and switch set.

### 2.5D
- Plane-locked 3D controller.
- `Billboard` sprite.
- 8-direction sprite selector based on camera angle.
- Isometric input remap.
- Fixed-camera zones (Cinemachine camera priority switching).

### VR (XR Interaction Toolkit)
- XR Origin rig prefab.
- Locomotion presets: teleport, snap/continuous turn, comfort vignette.
- Grab variants and sockets.
- Haptics helper.
- World-space UI panel (UI Toolkit, see section 7).
- VR-safe fade transitions.
- Hand-presence toggle.

### AR (AR Foundation)
- Plane detection plus tap-to-place.
- Pinch-scale and rotate gestures.
- Anchors.
- Image-tracking spawner.
- Occlusion toggle.
- Session reset UI.

### Narrative
- Bridge from the dialogue plugin to UI Toolkit: dialogue box, choice list, typewriter, speaker name and portrait.
- `CharacterSO` (name, color, portraits by emotion).
- Story flags/variables synced to the save system.
- Dialogue triggers (on interact, on enter).
- Timeline-driven cutscenes triggered from dialogue commands.
- Background/CG and music commands for VN-style games.

---

## 6. Genre-kit scripts

| Genre | Key scripts beyond Core + dimension module |
|---|---|
| Platformer | Hazards/kill zones, collectibles counter, level-end goal, enemy patrol (edge detection), stomp damage |
| Metroidvania | Ability unlock SO + gated doors, room transitions, map/minimap, save rooms |
| Top-down adventure | Melee hitbox, knockback, keys/locked doors, room camera, heart containers |
| Shooter / shmup | `WeaponSO` (rate, spread, projectile), pooled projectiles, enemy movement patterns, power-ups, boss phases |
| Endless runner | Chunk spawner/recycler, difficulty curve SO, distance score |
| Roguelike | Procedural rooms (tilemap generator), loot tables SO, run-vs-meta progression, item modifiers |
| Puzzle (grid) | Grid model separate from view, undo stack, win-condition checker, level SO list |
| Match-3 | Board model, match detection, cascade/refill, combo scoring |
| Tower defense | Path/waypoints, `TowerSO` + targeting modes, wave SO, build placement, currency |
| Turn-based tactics | Turn manager, grid pathfinding (A*), action points, unit stats SO |
| Card game / deckbuilder | `CardSO`, deck/hand/discard piles, effect system (command pattern), turn phases |
| Idle / clicker | Big-number formatting, generators SO, offline earnings, upgrade cost curve |
| Farming / life sim | Day/time cycle, crop growth SO, tile-based soil, inventory, shop |
| Point-and-click | Hotspots, item combine, cursor states, inventory bar |
| FPS | Hitscan + projectile weapons, ammo/reload, recoil via Cinemachine, enemy AI |
| Racing | Vehicle controller (or WheelCollider wrapper), checkpoints/laps, position tracker, AI on splines |
| Survival / crafting | Inventory grid, `RecipeSO`, hunger/stamina stats, gatherable resources |
| Horror / stealth | Vision cone + hearing sensors, flashlight/battery, hide spots, suspicion meter |
| RTS / city builder | Box selection, command queue, grid building placement, resource economy |
| Visual novel | Scene/background manager, character staging, auto/skip/log, save slots with thumbnails |
| VR escape room | Socket-based puzzles, combination locks, timer, hint system |
| AR tabletop | Board anchoring, piece placement on grid, turn manager (shared with tactics) |

---

## 7. UI strategy — screen, diegetic & world-space

> [!tip] Key finding
> Interactive diegetic UI **no longer requires uGUI**. Since Unity 6.2, UI Toolkit supports world-space rendering: set the Panel Settings **Render Mode** from Screen Space to World Space, and a UI Document hosts the UXML in the scene. One UXML/USS skill set then covers both the HUD and in-world screens.

### VR support
- XR Interaction Toolkit supports world-space UI Toolkit from **Unity 6.2 + XRI 3.2.0**.
- A panel needs a **Collider + UI Document** to work with XR ray interactors.
- Adding **XRSimpleInteractable + XRPokeFilter** enables poke with hands or controllers.
- Adding an **XRUIToolkitManager** component to the scene turns on UI Toolkit support for XRI.
- When uGUI and UI Toolkit are used together, turn off `bypassUIToolkitEvents` on the XR UI Input Module.
- Reference: XRI **World Space UI** sample (Package Manager → XR Interaction Toolkit → Samples). It shows UI Toolkit and uGUI side by side.

### TextMeshPro is not the same as "old UI"
TMP has two components:
- **`TextMeshPro`** is a plain 3D mesh. It needs no Canvas and no uGUI.
- **`TextMeshProUGUI`** lives on a uGUI Canvas.

Diegetic text uses the first one. It's still the best tool for many small in-world text objects:
- signs, labels and nameplates
- floating damage numbers
- text needing distance-field material effects like outline, glow or dissolve
- per-character animation

### Which tool to use

| Kind of UI | Example | Tool |
|---|---|---|
| Non-diegetic (screen) | Menus, HUD, pause, dialogue box | UI Toolkit, Screen Space |
| Diegetic, interactive | Computer terminal, in-world shop, wrist menu, VR panels | UI Toolkit, World Space |
| Diegetic or spatial text | Signs, nameplates, damage numbers | TMP 3D (`TextMeshPro`), no Canvas |
| Diegetic on a curved/odd surface | CRT monitor, in-game phone screen | UI Toolkit rendered to a RenderTexture on a mesh |
| Many tiny bars | Health bars over 50 enemies | Sprite or shader quad (cheapest), not a UI panel each |
| Legacy/compatibility | Asset Store plugins that ship uGUI prefabs | uGUI + `TextMeshProUGUI` |

### Current limitations of world-space UI Toolkit
- **Masking:** no arbitrary-shape masking. `overflow: hidden` always clips to a rectangle, so rounded clipping doesn't work yet. Unity says world-space masking is planned.
- **Colliders:** the auto-generated panel collider can conflict with `XRGrabInteractable`. Set **Collider Is Trigger** on the panel, or assign interactable colliders manually.
- **Editor testing:** when testing over Meta Horizon Link in the Editor, input only reaches UI Toolkit while the **Game view has focus**. Warn students about this one.
- **Scroll views in VR:** grab-and-drag scrolling needs 6000.3.8f1, 6000.4.0b9, 6000.5.0a7 or newer. Our 6000.5+ baseline covers it.

### Teaching vocabulary
- **Non-diegetic:** screen HUD, not part of the world.
- **Diegetic:** exists in the world and the character is aware of it (Dead Space health spine, an in-game terminal).
- **Spatial:** placed in the world, but the character isn't aware of it (floating nameplates, waypoint markers).
- **Meta:** screen effects that represent game state (blood vignette, low-health pulse).

### Architecture: one data source, many views
- Gameplay writes to SO variables and event channels.
- Any view can bind to the same data: a screen HUD, a world panel, or a TMP label.
- A student can switch a health readout from a HUD to a diegetic display without touching gameplay code.

### UI scripts to add
- `WorldPanel`: sets up a world-space UI Document, with optional billboarding and distance-based show/hide. Supports mouse/gamepad pointer input outside XR.
- `RenderTexturePanel`: UI Toolkit drawn onto a mesh, for monitors and phones.
- `WorldLabel` / `Nameplate`: TMP 3D text that faces the camera, with optional fade by distance.
- `DamagePopup`: pooled TMP 3D text with a tween.
- `WorldBar`: a sprite/shader health bar for enemies.
- `XRWorldPanel` preset: configured for XRI ray and poke.
- `MetaEffects`: screen-space "meta" UI such as a blood vignette or low-health pulse, using URP full-screen effects.

---

## 8. Plugins & packages

### Narrative (Unity alternatives to Ren'Py)
Ren'Py is a separate Python engine, so it can't be used inside Unity.

| Tool | Cost | Notes |
|---|---|---|
| **Yarn Spinner** ⭐ | Free (MIT) / paid Yarn Spinner+ | Script-based and writer-friendly. Ten years old, used in *Night in the Woods*, *DREDGE* and *A Short Hike*. 3.1 (Dec 2025) added async runner methods and a reworked typewriter; 3.2 shipped March 2026. Yarn Spinner+ adds Text Animator integration. **Leading pick for class.** |
| **Ink** (inkle) | Free | Strong for text-heavy branching interactive fiction. Official Unity integration. |
| **Naninovel** | Paid | Closest to a Ren'Py-style visual novel framework inside Unity. Worth it if VN pitches are common. |
| **Dialogue System for Unity** (Pixel Crushers) | Paid | Visual dialogue database editor. Comprehensive, but heavy for students. |

### First-party Unity packages
- Input System, UI Toolkit, Cinemachine 3, Timeline
- 2D Tilemap Extras, 2D Animation / PSD Importer
- AI Navigation, Behavior (behavior trees), Splines, ProBuilder
- Localization, Addressables
- XR Interaction Toolkit (3.2+), AR Foundation
- Netcode for GameObjects, only if we add a multiplayer kit

### Third-party extras
- **Tweening:** PrimeTween (free, allocation-free) or DOTween
- **Text effects:** Text Animator

---

## 9. Open decisions

- [ ] **Delivery format.**
  - Option A: one UPM package installed from a Git URL, with each genre kit as an importable "Sample". Easy to update every semester. *Current lean.*
  - Option B: separate template projects per genre.
- [ ] **Architecture style.** Strict SO event channels (decoupled, inspector-driven, good for teaching), a few singletons for simplicity (`AudioManager`, `GameManager`), or a hybrid.
- [ ] **Dialogue tool.** Standardize on one, Yarn Spinner or Ink, so the Narrative module isn't built twice.
- [ ] **Unity version lock** per semester; plan the move to 6.7 LTS.
- [ ] **Build order.** Students mostly build 2D, so:
  1. Core
  2. 2D module → Platformer, Top-down and Shooter kits
  3. 2.5D / 3D modules
  4. VR / AR

---

## Sources

- [Unity 6.5 is now available – Unity Discussions](https://discussions.unity.com/t/unity-6-5-is-now-available/1723176)
- [Unity 6.5 Released – GameFromScratch](https://gamefromscratch.com/unity-6-5-released/)
- [New in Unity 6.5 – Unity Docs](https://docs.unity.com/en-us/engine/6000.6/manual/whats-new/unity65.md)
- [Create world space UI with UI Toolkit in Unity 6.2 – Unity](https://unity.com/kr/resources/how-to-create-world-space-ui-toolkit)
- [XRI World Space UI Toolkit support (3.7)](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.7/manual/ui-world-space-ui-toolkit-support.html)
- [XRI World Space UI Toolkit support (3.6)](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.6/manual/ui-world-space-ui-toolkit-support.html)
- [XRI World Space UI Toolkit support (3.5)](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.5/manual/ui-world-space-ui-toolkit-support.html)
- [XRI World Space UI sample](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/samples-world-space-ui.html)
- [Unity Issue Tracker – world-space overflow clipping](https://issuetracker.unity3d.com/issues/ui-toolkits-visualelement-with-overflow-hidden-property-fails-to-clip-its-child-element-when-render-mode-is-set-to-world-space)
- [Yarn Spinner in 2026](https://www.yarnspinner.dev/2026)
- [Yarn Spinner+ for Unity – itch.io](https://yarnspinner.itch.io/yarn-spinner)
- [Yarn Spinner news feed](https://www.yarnspinner.dev/index.xml)
- [Best Unity Dialogue Systems – Generalist Programmer](https://generalistprogrammer.com/tutorials/best-unity-dialogue-systems-complete-asset-comparison)
