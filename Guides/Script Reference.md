---
title: "Script Reference"
course: GAME 1303
type: guide
status: draft
course_version: 0.15.0
unity: 6000.3.10f1
tags:
  - game1303
  - guide
  - scripts
---

# Script Reference

Every course script in the course project, as of version **0.15.0**: where it lives, what it does, how to set it up, and which scripts it works with. Check your version in `Assets/_Course/VERSION.txt`.

## Finding the scripts

| To add a… | Use |
|---|---|
| Component (on a GameObject) | **Add Component → Collin Game →** *group* → *name* |
| Asset (a variable, an event, the Input Reader) | Right-click in the Project window → **Create → Collin Game →** *group* → *name* |
| Editor tool | The **Collin Game** menu at the top of the Editor |

Every script explains its settings: hover over a field in the Inspector to see its tooltip. When something is set up wrong, the script writes a plain-language message to the Console that names the object and the fix.

> [!warning] Don't edit course files
> Everything in `Assets/_Course` is replaced when the course is updated. To change a script, prefab or screen, copy it into `Assets/_Game` and change the copy. For prefabs, make a **Prefab Variant**.

## Directory map

| Folder | Assembly | Contents |
|---|---|---|
| `_Course/Core/GameFlow` | `CollinGame.Core` | Starting the game, loading scenes, fades |
| `_Course/Core/Events` | `CollinGame.Core` | Event channels and listeners |
| `_Course/Core/Variables` | `CollinGame.Core` | Variable assets, and components that show, reset and watch them |
| `_Course/Core/Input` | `CollinGame.Core` | The Input Reader and the project's input actions |
| `_Course/Core/Gameplay` | `CollinGame.Core` | Health, damage, pickups, checkpoints, zones, spawning |
| `_Course/Core/TurnBased` | `CollinGame.Core` | Turn order, turn takers and their actions |
| `_Course/Core/UI` | `CollinGame.Core` | UI Toolkit screens, their style sheet, the shared `CoursePanelSettings`, and the components that run them |
| `_Course/Core/Audio` | `CollinGame.Core` | Sound effects, music and volume |
| `_Course/Core/Effects` | `CollinGame.Core` | Camera shake, hit stop, cutscenes |
| `_Course/Core/Saving` | `CollinGame.Core` | Saving variables and high scores |
| `_Course/Core/Editor` | `CollinGame.Core.Editor` | Inspector helpers and the art importer. Editor only |
| `_Course/TwoD/Movement` | `CollinGame.TwoD` | 2D character controllers and moving objects |
| `_Course/TwoD/AI` | `CollinGame.TwoD` | 2D enemies |
| `_Course/TwoD/Visuals` | `CollinGame.TwoD` | Simple sprite animation |
| `_Course/ThreeD/Movement` | `CollinGame.ThreeD` | 3D and 2.5D player controllers |
| `_Course/Kits/Platformer/Scripts` | `CollinGame.Kits.Platformer` | Platformer kit scripts |
| `_Course/Kits/Platformer/UI` | — | Platformer kit screens |
| `_Course/Kits/PhysicsPuzzle/Scripts` | `CollinGame.Kits.PhysicsPuzzle` | Physics puzzle kit scripts |
| `_Course/Kits/PhysicsPuzzle/UI` | — | Physics puzzle kit HUD |
| `_Course/Kits/TopDownAdventure/Scripts` | `CollinGame.Kits.TopDownAdventure` | Top-down adventure kit scripts |
| `_Course/Kits/TopDownAdventure/UI` | — | Top-down adventure kit HUD |
| `_Course/Kits/TurnBasedBattle/Scripts` | `CollinGame.Kits.TurnBasedBattle` | Turn-based battle kit scripts |
| `_Course/Kits/TurnBasedBattle/UI` | — | Battle screen |
| `_Course/Kits/ArcadeClassic/Scripts` | `CollinGame.Kits.ArcadeClassic` | Arcade classic kit scripts |
| `_Course/Kits/ArcadeClassic/UI` | — | Arcade and Pong HUDs |
| `_Course/Kits/TopDownShooter/Scripts` | `CollinGame.Kits.TopDownShooter` | Top-down shooter kit scripts |
| `_Course/Kits/TopDownShooter/UI` | — | Shooter HUD |
| `_Course/Kits/EndlessRunner/Scripts` | `CollinGame.Kits.EndlessRunner` | Endless runner kit scripts |
| `_Course/Kits/EndlessRunner/UI` | — | Runner HUD |
| `_Course/Art/Kenney` | — | Kenney art packs (CC0). Its README links to every pack the kits use |
| `_Course/Credits` | — | The course's credits text |

Each folder's scripts can use the folders above it in this order: Core, then TwoD, then Kits. Core never depends on a kit, so adding or removing a kit can't break the exercises.

## How the pieces fit together

Most course scripts never talk to each other directly. They share **assets** instead.

| Pattern | Example | Why |
|---|---|---|
| A component **changes a variable**; others **show or watch** it | A Collectible adds to `Score`; a UI Variable Binder shows it; an Int Variable Condition reacts when it reaches 10 | The coin doesn't need to know the HUD exists |
| A component **raises an event**; others **listen** | A Trigger Zone raises `LevelCompleted`; a Void Event Listener shows the win screen | The goal doesn't need to know what happens when it's reached |
| A component **asks the Input Reader** | The Platformer Controller reads `Move` and listens for `JumpPressed` | Works on keyboard and gamepad; controls can be switched off in one place |
| Components on the **same GameObject** cooperate | Health and Respawner on the player: when health runs out, the Respawner refills it | No wiring needed |

The main families:

| Family | Scripts |
|---|---|
| Starting and changing scenes | Bootstrapper → Scene Loader + Screen Fader; Scene Changer |
| Sharing data | Variables, Variable Label, UI Variable Binder, Variable Resetter, Int Variable Condition |
| Sharing moments | Event Channels, Event Listeners, Trigger Zone, Checkpoint, Health, Collectible |
| Player | Input Reader → Platformer or Top Down Controller 2D; Health; Respawner |
| Hurting and healing | Damage On Touch, Kill Zone, Stompable Enemy 2D → Health ← Collectible (Heal) |
| Dying and coming back | Health → Respawner ← Checkpoint, Kill Zone |
| Spawning | Spawner → a prefab with Health, Lifetime or Damage On Touch (Remove Self After Hit) |
| Turns | Turn Manager → Turn Taker ← Turn Actions → Health |
| Screens | UI Document + UI Screen + UI Button Events + UI Variable Binder; Pause Controller; UI Credits; UI Settings |
| Sound | Sound Effect assets (played from any event); Music Player → Audio Service |
| Feedback | Camera Shake, Hit Stop, Health Popups |
| Saving | Variable Saver, High Score |

---

## Game flow

### Bootstrapper

`Core/GameFlow/Bootstrapper.cs` · runs by itself; never added to anything

Before the first scene loads, creates an object named **[Course Services]** that holds a Scene Loader, a Screen Fader and the Audio Service, and keeps it alive across scene changes. That's why you can press Play from any scene. While playing, you can find it under **DontDestroyOnLoad** in the Hierarchy.

Optional: if a prefab named `CourseServices` exists in a `Resources` folder, it's used in place of an empty object, so its settings can be changed.

**Works with:** Scene Loader, Screen Fader, Audio Service. **Used in:** [Ex 01](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex01%20-%20Bootstrap.md).

### Scene Loader

`Core/GameFlow/SceneLoader.cs` · created by the Bootstrapper

Loads scenes with a fade out and a fade in. There is always exactly one. It refuses to load a scene that isn't in the Scene List (**File → Build Profiles → Scene List**) and says so in the Console. Loading a scene also un-pauses the game.

| Setting | Default | |
|---|---|---|
| Fade Duration | `0.35` | Seconds for each fade. `0` switches with no fade |

From a script: `SceneLoader.Instance.LoadScene("Level2")`, `ReloadScene()`, `LoadNextScene()`, `QuitGame()`.

### Screen Fader

`Core/GameFlow/ScreenFader.cs` · created with the Scene Loader

The full-screen color the Scene Loader fades through. Setting: **Color** (black).

### Scene Changer

`Core/GameFlow/SceneChanger.cs` · **Add Component → Collin Game → Core → Scene Changer**

Changes scene with no code. Type a scene name, then start the change in one of three ways.

| Setting | Default | |
|---|---|---|
| Scene Name | — | Exactly as the file is named, without `.unity` |
| Load After Seconds | `0` | Load by itself after this many seconds. `0` is off |
| Load On Action | — | Load when the player uses an input action, such as **Player/Jump** |

Its methods can be chosen from any button or event response: **Load**, **ReloadScene**, **LoadNextScene** (the next scene in the Scene List), **QuitGame** (stops Play mode in the Editor).

**How to use it:**

1. Create an empty GameObject and add a Scene Changer.
2. Type the **Scene Name**, and add that scene to the Scene List.
3. Choose how it starts: a timer, an input action, or a button's On Click (**SceneChanger → Load**).

**Works with:** UI Button Events, Void Event Listener, Variable Resetter. **Used in:** [Ex 01](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex01%20-%20Bootstrap.md), [Ex 04](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md), [Ex 06](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md).

---

## Variables

Variable assets hold one shared value outside any scene. They go back to their **Initial Value** each time the game starts, and **keep** their value when scenes change. During Play, the Inspector shows each variable's **Current Value**.

| Asset | Create menu | Holds | Extra methods |
|---|---|---|---|
| Int Variable | Create → Collin Game → Variables → Int Variable | A whole number: score, coins, lives | **Add (int)**; use a negative number to subtract |
| Float Variable | … → Float Variable | A decimal: time, speed | **Add (float)** |
| Bool Variable | … → Bool Variable | True or false: paused, has the key | **Toggle** |
| String Variable | … → String Variable | Text: a message, a name | |

All variables have **Description** (a note for yourself), **Initial Value** and **Log Changes** (writes each change to the Console).

**Used in:** [Ex 02](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md) onward. **Background:** [ScriptableObjects: Variables and Events](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/ScriptableObjects%20-%20Variables%20and%20Events.md).

### Variable Label

`Core/Variables/VariableLabel.cs` · **Add Component → Collin Game → Core → Variable Label**

Shows a variable in a **TextMeshPro** text in the world, and keeps it up to date. Add it to the same GameObject as the text.

| Setting | Default | |
|---|---|---|
| Variable | — | Any variable asset |
| Label | this object's text | The text to write into |
| Format | `{0}` | `{0}` is replaced by the value, so `Score: {0}` shows "Score: 3" |

For screen UI, use **UI Variable Binder** instead. **Used in:** [Ex 02](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md), [Ex 05 (turn-based)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat%20%28Turn-Based%29.md).

### Variable Resetter

`Core/Variables/VariableResetter.cs` · **Add Component → Collin Game → Core → Variable Resetter**

Sets variables back to their Initial Value: when the scene starts, or when **ResetAll** is called from a button or event. Leave a variable out of its list if it should carry between scenes.

| Setting | Default | |
|---|---|---|
| Variables | — | The variables to reset |
| Reset When Scene Starts | ticked | Untick to reset only when ResetAll is called |

**Used in:** [Ex 02](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md), [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md) (lives and coins).

### Int Variable Condition

`Core/Variables/IntVariableCondition.cs` · **Add Component → Collin Game → Core → Int Variable Condition**

Watches a number and reacts when it reaches a value: game over at 0 lives, a door opening at 10 coins.

| Setting | Default | |
|---|---|---|
| Variable | — | The Int Variable to watch |
| Comparison | At Least | **Equal To**, **At Least** or **At Most** |
| Value | `1` | The value to compare with |
| Only Once | ticked | Untick to react every time the condition becomes true again |
| Raise Event | — | Optional event channel |
| On Became True | — | Things to do |

**Works with:** any Int Variable, Void Event Channel. **Used in:** [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md) (game over).

---

## Events

An event channel is an asset that one object **raises** and any number of objects **listen** to.

| Asset | Create menu | Carries |
|---|---|---|
| Void Event Channel | Create → Collin Game → Events → Void Event Channel | Nothing: "this happened" |
| Int, Float, Bool, String, GameObject Event Channel | … → *type* Event Channel | A value of that type |

Every channel has **Description** and **Log When Raised**. During Play, a Void Event Channel's Inspector has a **Raise** button for testing.

**Raised by:** Collectible (Raise Event), Trigger Zone, Checkpoint, Health (Raise On Died), Respawner, Int Variable Condition, Turn Manager, or a script calling `Raise()`.

### Event Listeners

`Core/Events/` · **Add Component → Collin Game → Events →** *type* **Event Listener**

Runs a **Response** when its **Channel** is raised. Typed listeners pass the value along. A listener only listens while its GameObject is active.

**How to use one:**

1. Add a **Void Event Listener** to the object that should react.
2. Drag the event channel asset into **Channel**.
3. Under **Response**, click **+**, drag in the object to act on, and choose a method, such as **GameObject → SetActive** or **UIScreen → Show**.

**Used in:** [Ex 02](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md) (the door), [Ex 04](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md), [Ex 06](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md) (the win screen).

---

## Input

### Input Reader

`Core/Input/InputReader.cs` and the asset `Core/Input/InputReader` · already in the project

The one place course scripts get player input. It reads the project's input actions (`Core/Input/InputSystem_Actions`) and offers them as values and events. Leave its **Actions** field empty to use the project's actions.

| Values (read any time) | Events (at a moment) |
|---|---|
| Move, Look | JumpPressed, JumpReleased |
| JumpHeld, AttackHeld, InteractHeld, CrouchHeld, SprintHeld | AttackPressed/Released, InteractPressed/Released |
| | CrouchPressed/Released, SprintPressed/Released |
| | PreviousPressed, NextPressed, PausePressed |

**DisablePlayerInput** and **EnablePlayerInput** switch the player's controls off and on, for pauses, cutscenes and end screens. Pause keeps working while they're off, and controls switch back on whenever a scene loads.

| Action | Keyboard and mouse | Gamepad |
|---|---|---|
| Move | WASD, arrow keys | Left stick |
| Jump | Space | Bottom face button |
| Attack | Enter, left mouse button | Left face button |
| Interact | E | Top face button |
| Pause | Esc | Start |

**Used by:** both 2D controllers, Turn Actions, Pause Controller, Scene Changer (Load On Action). Components that need it fill in their **Input** field themselves when added. **Background:** [The Input System and the Input Reader](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/The%20Input%20System%20and%20the%20Input%20Reader.md).

---

## 2D movement

### Platformer Controller 2D

`TwoD/Movement/PlatformerController2D.cs` · **Add Component → Collin Game → 2D → Platformer Controller 2D**

A side-view character that runs and jumps. Adds and sets up its own Rigidbody 2D. Needs a 2D collider; a Capsule Collider 2D works well. It rides moving platforms, passes up through one-way platforms, and can be launched by springs and stomps.

| Group | Setting | Default |
|---|---|---|
| Input | Input | `InputReader` |
| Running | Max Speed · Acceleration · Deceleration · Air Control | `7` · `60` · `70` · `0.6` |
| Jumping | Jump Height (units) · Extra Air Jumps · Short Hop Speed Kept · Coyote Time · Jump Buffer Time | `3` · `0` · `0.5` · `0.1` · `0.1` |
| Gravity | Gravity Scale · Fall Gravity Multiplier · Max Fall Speed | `3` · `1.5` · `20` |
| Ground check | Ground Layers · Ground Check Distance | Everything · `0.08` |
| Looks | Sprite To Flip | first sprite found |
| Events | On Jump · On Land | |

Selecting the character shows its ground check as a box: green on the ground, red in the air.

**Works with:** Input Reader, Health, Respawner, Platformer Sprite Animator, Bounce Pad 2D, Stompable Enemy 2D, Waypoint Mover 2D. **Used in:** [Ex 03](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex03%20-%20Player.md) onward. **Background:** [Game Feel](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Game%20Feel.md), [Forgiving Controls](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Forgiving%20Controls.md).

### Top Down Controller 2D

`TwoD/Movement/TopDownController2D.cs` · **Add Component → Collin Game → 2D → Top Down Controller 2D**

A character seen from above that moves in any direction. Adds its own Rigidbody 2D with gravity off.

| Setting | Default | |
|---|---|---|
| Input | `InputReader` | |
| Max Speed · Acceleration · Deceleration | `6` · `50` · `60` | |
| Facing | Flip Sprite | **None**, **Flip Sprite**, or **Rotate To Movement** |
| Sprite To Flip | first sprite found | |

**Used in:** [Ex 03](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex03%20-%20Player.md), Part 6.

### Waypoint Mover 2D

`TwoD/Movement/WaypointMover2D.cs` · **Add Component → Collin Game → 2D → Waypoint Mover 2D**

Moves an object along a path, over and over: moving platforms, flying enemies, saw blades. Sets its own Rigidbody 2D to Kinematic.

| Setting | Default | |
|---|---|---|
| Stops | `(4, 0)` | Positions measured from where the object starts |
| Path Mode | Back And Forth | Or **Loop** |
| Speed | `2` | Units per second |
| Wait At Stops | `0.5` | Seconds |

Selecting the object draws its path. A character with the Platformer Controller 2D is carried along when standing on it.

**Used in:** [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md) (Moving Platform, Flyer).

---

## 3D movement

3D scripts sit beside the 2D ones and use the same Core scripts, so Health, Respawner, Checkpoint, Collectible, Kill Zone and the UI all work with 3D colliders. A 3D scene's Main Camera uses the **Universal Renderer** (**Rendering → Renderer**); 2D scenes keep the 2D Renderer.

### Tank Controller 3D

`ThreeD/Movement/TankController3D.cs` · **Add Component → Collin Game → 3D → Tank Controller 3D**

A player controlled relative to themselves: left and right turn, forward and back move the way the player faces, Jump jumps. Uses a **Character Controller**, added and sized for you (Height `2`, Radius `0.4`, Center `0, 1, 0`). Put it on the root of the player, with the pivot at the feet. Pair it with a Cinemachine Camera that follows from behind.

| Setting | Default | |
|---|---|---|
| Input | `InputReader` (filled in for you) | |
| Turn Speed · Air Turning | `180` · `0.75` | Degrees per second; share of turning kept in the air |
| Forward Speed · Backward Speed | `6` · `3` | Units per second |
| Acceleration · Deceleration · Air Control | `30` · `40` · `0.5` | |
| Jump Height · Extra Air Jumps | `2` · `0` | `1` gives a double jump |
| Short Hop Speed Kept | `0.5` | Letting go of Jump early cuts the jump |
| Coyote Time · Jump Buffer Time | `0.1` · `0.1` | |
| Gravity · Fall Gravity Multiplier · Max Fall Speed | `25` · `1.5` · `30` | |
| On Jump · On Landed | — | |

Read by other scripts: **IsGrounded**, **ForwardSpeed**, **Velocity**, **MoveInput**. Method: **Bounce** (height), for bounce pads. A Respawner can move the player; the controller notices and keeps up.

**Used in:** [2.5D Tutorial 1 — Third-Person Controller](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Tutorials/2.5D%20Tutorial%201%20-%20Third-Person%20Controller.md).

### Rail Runner 3D

`ThreeD/Movement/RailRunner3D.cs` · **Add Component → Collin Game → 3D → Rail Runner 3D**

Keeps the player on a **Spline Container** (the rail): they run along it, step sideways within its width, and jump, but can't fall off. At the start, and after a Respawner moves them, the player snaps to the nearest point on the rail. Select the player to see the rail's edges. Uses a Character Controller so trigger colliders (pickups, hazards, checkpoints) still work; solid colliders are ignored.

| Setting | Default | |
|---|---|---|
| Input · Rail | `InputReader` · the scene's first Spline Container | Both filled in for you |
| Controls | Forward And Back | **Forward And Back** (camera behind), **Left And Right** (camera at the side, a 2.5D side-scroller), **Auto Run** (endless runner) |
| Swap Left And Right | unticked | Left And Right only, for a camera on the other side |
| Run Speed · Backward Speed | `7` · `4` | |
| Acceleration · Deceleration | `30` · `40` | |
| Rail Width · Side Speed | `1` · `4` | Width `0` keeps the player on the line |
| Height Above Rail | `0` | Raise it if the player sinks into the path's mesh |
| Face Run Direction · Turn Speed | unticked · `720` | Tick it to turn around when running back |
| Rail Facing Target | — | A child kept facing along the rail. Use it as the camera's Tracking Target for a side view |
| Jump Height · Extra Air Jumps · Short Hop Speed Kept · Jump Buffer Time | `2` · `0` · `0.5` · `0.1` | |
| Gravity · Fall Gravity Multiplier | `25` · `1.5` | |
| On Jump · On Landed · On Reached End · On Reached Start | — | The end events only run on a rail that doesn't loop |

Read by other scripts: **Progress** (0 to 1 along the rail), **RunSpeed**, **SideOffset**, **IsGrounded**, **Rail**. Methods: **SnapToNearest**, **Bounce**.

**Used in:** [2.5D Tutorial 2 — Rail Runner](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Tutorials/2.5D%20Tutorial%202%20-%20Rail%20Runner.md).

---

## 2D enemies and visuals

### Patrol Enemy 2D

`TwoD/AI/PatrolEnemy2D.cs` · **Add Component → Collin Game → 2D → Patrol Enemy 2D**

A side-view enemy with two states. **Patrol:** walks and turns at walls and ledges. **Chase:** walks toward the player while within Chase Range, without walking off ledges. Adds its own Rigidbody 2D. It doesn't hurt anything by itself: add **Damage On Touch** or **Stompable Enemy 2D**.

| Setting | Default | |
|---|---|---|
| Patrol Speed · Start Moving Right | `2` · ticked | |
| Turn At Ledges · Turn At Walls | ticked · ticked | |
| Max Distance From Start | `0` | `0` is no limit |
| Chase Tag · Chase Range · Chase Speed | `Player` · `0` · `3.5` | Range `0` never chases |
| Solid Layers | Everything | |
| Sprite To Flip | first sprite found | |

Selecting the enemy shows its chase range as a circle. **Used in:** [Ex 05](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat.md). **Background:** [State Machines and Enemy AI](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/State%20Machines%20and%20Enemy%20AI.md).

### Sprite Flipbook

`TwoD/Visuals/SpriteFlipbook.cs` · **Add Component → Collin Game → 2D → Sprite Flipbook**

Plays a few sprites in a loop: a spinning coin, a waving flag. No Animator needed. Settings: **Frames**, **Frames Per Second** (`6`), **Target** (this object's sprite), **Random Start** (ticked, so copies don't move in step).

---

## Gameplay

All gameplay components work in 2D and 3D. Those that react to touch need a collider, and at least one of the two touching objects needs a Rigidbody. Most have a **tag** setting that defaults to `Player`; leave it empty to react to anything.

### Collectible

`Core/Gameplay/Collectible.cs` · **Add Component → Collin Game → Core → Collectible**

Something that can be picked up. Needs a collider with **Is Trigger** ticked.

| Setting | Default | |
|---|---|---|
| Collector Tag | `Player` | |
| Add To · Amount | — · `1` | An Int Variable to add to |
| Heal | `0` | Health given to the collector |
| Raise Event | — | An event channel |
| On Collected | — | Things to do |
| Destroy When Collected | ticked | Untick to hide it instead |

**Used in:** [Ex 02](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex02%20-%20Events.md) onward. Coins, keys, hearts and gems are all Collectibles with different settings.

### Health

`Core/Gameplay/Health.cs` · **Add Component → Collin Game → Core → Health**

Health that can be lost and regained. Starts full each time the object appears. Announces damage, healing and death, so nothing needs to check it.

| Setting | Default | |
|---|---|---|
| Max Health | `3` | |
| Invulnerable Time | `1` | Seconds after a hit when no damage is taken. Use `0` for turn-based |
| When Health Runs Out | Nothing | **Nothing** (use with a Respawner), **Deactivate** (a Spawner can reuse it), **Destroy** |
| Health Variable | — | Kept equal to current health, for the HUD |
| Raise On Died | — | An event channel |
| On Damaged · On Healed · On Died | — | Things to do |

Other components call **TakeDamage**, **Heal** and **Kill**.

**Works with:** Respawner, Damage On Touch, Kill Zone, Stompable Enemy 2D, Collectible (Heal), Health Popups, Turn Actions, Turn Taker. **Background:** [Health and Damage](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Health%20and%20Damage.md).

### Respawner

`Core/Gameplay/Respawner.cs` · **Add Component → Collin Game → Core → Respawner**

Sends an object back to its respawn point, stops it, and refills its Health. The respawn point starts where the object begins the scene, and moves when it touches a Checkpoint.

| Setting | Default | |
|---|---|---|
| Respawn When Health Runs Out | ticked | Needs a Health on the same object |
| Raise On Respawn · On Respawn | — | |

**Works with:** Health, Checkpoint, Kill Zone. **Used in:** [Ex 04](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md).

### Checkpoint

`Core/Gameplay/Checkpoint.cs` · **Add Component → Collin Game → Core → Checkpoint**

When an object with a Respawner touches it, the respawn point moves here. Needs a trigger collider.

| Setting | Default | |
|---|---|---|
| Activator Tag | `Player` | |
| Respawn Point | this object | An exact place to reappear |
| Indicator · Active Color | — · green | A sprite that changes color when reached |
| Raise On Activated · On Activated | — | |

**Background:** [Hazards and Checkpoints](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Hazards%20and%20Checkpoints.md).

### Kill Zone

`Core/Gameplay/KillZone.cs` · **Add Component → Collin Game → Core → Kill Zone**

Anything that touches it is out at once: pits, lava. Takes all Health, or, with no Health, respawns the object. Works as a trigger or as a solid. Setting: **Target Tag** (`Player`).

### Damage On Touch

`Core/Gameplay/DamageOnTouch.cs` · **Add Component → Collin Game → Core → Damage On Touch**

Hurts anything with Health that touches it: spikes, enemies, rocks. Works as a trigger or as a solid.

| Setting | Default | |
|---|---|---|
| Target Tag | `Player` | |
| Damage | `1` | |
| Repeat Every | `0.5` | Hurt again while still touching. `0` hurts only on first touch |
| Remove Self After Hit | unticked | For rocks and projectiles |
| On Hit | — | |

### Trigger Zone

`Core/Gameplay/TriggerZone.cs` · **Add Component → Collin Game → Core → Trigger Zone**

An area that reacts when something enters or leaves: a goal, a trap, a door that opens as you approach. Needs a trigger collider.

| Setting | Default | |
|---|---|---|
| Trigger Tag | `Player` | |
| Only Once | unticked | |
| Raise On Enter · On Enter | — | |
| Raise On Exit · On Exit | — | |

**Used in:** [Ex 04](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex04%20-%20Level.md) (the goal).

### Spawner

`Core/Gameplay/Spawner.cs` · **Add Component → Collin Game → Core → Spawner**

Creates copies of a prefab over time, and reuses copies that have been switched off (pooling).

| Setting | Default | |
|---|---|---|
| Prefab | — | From the Project window, not the Hierarchy |
| Spawn Points | this object | Picked at random |
| Start Automatically · Start Delay · Interval | ticked · `1` · `2` | |
| Max At Once · Total To Spawn | `5` · `0` | `0` is no limit |
| On Spawned · On Finished | — | |

Methods: **StartSpawning**, **StopSpawning**, **SpawnOne**.

**Works with:** prefabs that switch themselves off: Health (Deactivate), Lifetime, Damage On Touch (Remove Self After Hit). **Used in:** [Ex 05](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat.md). **Background:** [Spawners and Pooling](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Spawners%20and%20Pooling.md).

### Lifetime

`Core/Gameplay/Lifetime.cs` · **Add Component → Collin Game → Core → Lifetime**

Removes an object after a number of seconds. Settings: **Seconds** (`5`), **When Time Is Up** (**Deactivate**, so a Spawner can reuse it, or **Destroy**).

---

## Turn-based

Background: [Turn-Based Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Turn-Based%20Systems.md). Used in: [Ex 05 (turn-based)](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex05%20-%20Combat%20%28Turn-Based%29.md).

### Turn Manager

`Core/TurnBased/TurnManager.cs` · **Add Component → Collin Game → Turn Based → Turn Manager**

Runs a battle: keeps the turn order, starts each turn, counts rounds, and decides when it's won (no opponents can act) or lost (nobody on the player's side can act).

| Setting | Default | |
|---|---|---|
| Turn Order | — | Turn Takers, in order |
| Start Automatically · Pause Between Turns | ticked · `0.6` | |
| Status Text · Round Variable | — | A String and an Int Variable to show |
| Raise On Player Won · Raise On Player Lost | — | Event channels |
| On Battle Started · On Player Won · On Player Lost | — | |

### Turn Taker

`Core/TurnBased/TurnTaker.cs` · **Add Component → Collin Game → Turn Based → Turn Taker**

Marks a participant. Skipped once its Health runs out. Settings: **Display Name**, **Player Side**, **On Turn Started**, **On Turn Ended**.

### Turn Actions

`Core/TurnBased/TurnActions.cs` · **Add Component → Collin Game → Turn Based → Turn Actions**

Attack or heal; each uses up the turn. **Player** control waits for Attack (Enter) or Interact (E). **Computer** control waits, heals if its health is low and a heal is left, and attacks otherwise.

| Setting | Default | |
|---|---|---|
| Controlled By · Input | Player · `InputReader` | |
| Attack Target · Attack Damage | — · `2` | The opponent's Health |
| Heal Amount · Heals Available | `3` · `2` | |
| Think Time · Heal When Health At Or Below | `1` · `2` | Computer only |
| Message Text | — | A String Variable describing the last action |
| On Attack · On Heal | — | |

---

## UI

### Screens

UXML files in `Core/UI`, styled by `CourseTheme.uss`. Put one in a scene with **GameObject → UI Toolkit → UI Document**, then set its **Source Asset**. Its **Panel Settings** should be `CoursePanelSettings` (filled in for you), so every screen scales the same way. Components find elements by **name**, so copies in `_Game` must keep these names.

| Screen | Element names |
|---|---|
| `HUD` | `health-label`, `score-label` |
| `MainMenu` | `title-label`, `subtitle-label`, `play-button`, `settings-button`, `credits-button`, `quit-button` |
| `PauseMenu` | `resume-button`, `settings-button`, `restart-button`, `menu-button` |
| `EndScreen` | `score-label`, `play-again-button`, `menu-button` |
| `GameOver` | `score-label`, `try-again-button`, `menu-button` |
| `Credits` | `credits-label`, `back-button` |
| `Settings` | `music-slider`, `effects-slider`, `fullscreen-toggle`, `back-button` |

To change a screen's look, copy the UXML into `Assets/_Game` and edit it in **UI Builder** (double-click it).

### UI Screen

`Core/UI/UIScreen.cs` · **Add Component → Collin Game → UI → UI Screen**

Shows and hides a whole UI Document. Methods: **Show**, **Hide**, **Toggle**.

| Setting | Default | |
|---|---|---|
| Hidden At Start | unticked | Tick for pause, win and credits screens |
| Select When Shown | — | The button to select first, so a gamepad can use the menu |

### UI Button Events

`Core/UI/UIButtonEvents.cs` · **Add Component → Collin Game → UI → UI Button Events**

Connects buttons to the scene with no code. For each button, type its **Button Name** and set **On Click**.

### UI Variable Binder

`Core/UI/UIVariableBinder.cs` · **Add Component → Collin Game → UI → UI Variable Binder**

Shows variables in a UI Document's labels and keeps them current. For each binding: **Label Name**, **Variable**, **Format** (`{0}` is the value).

### Pause Controller

`Core/UI/PauseController.cs` · **Add Component → Collin Game → UI → Pause Controller**

Pauses and un-pauses on the Pause action: stops time, switches off the player's controls, and shows the pause screen. Put it on the pause menu's UI Document; its fields fill themselves in.

| Setting | | |
|---|---|---|
| Input · Pause Screen | `InputReader` · this UI Screen | |
| Paused Variable | — | A Bool Variable kept equal to "paused" |
| On Paused · On Resumed | — | |

Methods: **Pause**, **Resume**, **TogglePause**. It doesn't pause during a cutscene.

### UI Settings

`Core/UI/UISettings.cs` · **Add Component → Collin Game → UI → UI Settings**

Runs the `Settings` screen: music volume, sound effects volume, and full screen (hidden in Web builds). Changes apply at once and are saved on the player's computer. Optional **Preview Sound**: a Sound Effect played when the effects slider moves.

**Used in:** [Ex 08](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex08%20-%20Save%20%26%20Build.md).

### UI Credits

`Core/UI/UICredits.cs` · **Add Component → Collin Game → UI → UI Credits**

Fills the Credits screen from text files. List **Credit Files** in order: the student's `Assets/_Game/Credits` first, then `Assets/_Course/Credits/Course Credits`.

### Health Popups

`Core/UI/HealthPopups.cs` · **Add Component → Collin Game → UI → Health Popups**

Floating "-1" and "+1" above an object when its Health changes. Add it next to a Health. Settings: **Damage Color**, **Heal Color**, **Font Size** (`5`), **Offset** (`0, 1.2, 0`). Uses **Floating Text**, which scripts can also call directly: `FloatingText.Spawn("Hello", position, Color.white)`.

**Used in:** [Ex 06](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex06%20-%20UI.md).

---

## Platformer kit

Imported with the Platformer Kit package. See [Platformer Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Platformer%20Kit.md).

### Stompable Enemy 2D

`Kits/Platformer/Scripts/StompableEnemy2D.cs` · **Add Component → Collin Game → Platformer Kit → Stompable Enemy 2D**

An enemy that's defeated by landing on it. From above, the enemy is hurt and the player bounces. From any other side, the player is hurt. Needs a **solid** collider. Use it instead of Damage On Touch. Without Health, one stomp removes it.

| Setting | Default | |
|---|---|---|
| Player Tag | `Player` | |
| Stomp Damage · Bounce Height | `1` · `2` | |
| Add To · Amount | — · `1` | Points for a stomp |
| On Stomped | — | |
| Touch Damage · Repeat Every | `1` · `0.5` | |

### Bounce Pad 2D

`Kits/Platformer/Scripts/BouncePad2D.cs` · **Add Component → Collin Game → Platformer Kit → Bounce Pad 2D**

A spring. Needs a trigger collider over its top. Settings: **Target Tag**, **Bounce Height** (`6`), **Sprite To Change**, **Fired Sprite**, **Fired Time** (`0.2`), **On Bounce**.

### Platformer Sprite Animator

`Kits/Platformer/Scripts/PlatformerSpriteAnimator.cs` · **Add Component → Collin Game → Platformer Kit → Platformer Sprite Animator**

Changes the character's sprite: **Idle** when standing, **Walk** frames when moving, **In Air** when jumping or falling. Needs the Platformer Controller 2D on the same object. **Walk Frames Per Second**: `8`.

### Kit screens

| Screen | Element names |
|---|---|
| `PlatformerHUD` | `health-label`, `lives-label`, `coins-label` |
| `PlatformerMenu` | `title-label`, `subtitle-label`, `play-button`, `settings-button`, `credits-button`, `quit-button` |
| `LevelComplete` | `coins-label`, `next-button`, `menu-button` |

---

## Audio

Background: [Sound and Music](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Sound%20and%20Music.md). Used in: [Ex 07](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex07%20-%20Juice%20%26%20Audio.md).

### Sound Effect

`Core/Audio/SoundEffect.cs` · **Create → Collin Game → Audio → Sound Effect**

An asset holding one or more clips. Play it from **any event**: click **+**, drag the Sound Effect asset (from the Project window) into the object field, and choose **SoundEffect → Play**.

| Setting | Default | |
|---|---|---|
| Clips | — | With several, a different one plays each time |
| Volume | `1` | The player's effects volume is applied on top |
| Pitch Variation | `0.05` | Random change each time, so repeats don't grate |
| Minimum Gap | `0.05` | Seconds; stops the same sound stacking up |

### Music Player

`Core/Audio/MusicPlayer.cs` · **Add Component → Collin Game → Audio → Music Player**

Plays looping music in a scene. Same music in the next scene carries on; different music crossfades. Settings: **Music**, **Volume** (`0.7`), **Fade Time** (`1`), **Play On Start** (ticked). Methods: **Play**, **PlayClip (AudioClip)**, **Stop**.

### Audio Service

`Core/Audio/AudioService.cs` · created by the Bootstrapper

Plays every sound effect and the music, and holds the two volume settings (saved on the player's computer). It's never added by hand. From a script: `AudioService.Instance.MusicVolume`, `EffectsVolume`.

---

## Effects

### Camera Shake

`Core/Effects/CameraShake.cs` · **Add Component → Collin Game → Effects → Camera Shake**

Shakes the camera. Adds a Cinemachine Impulse Source. The Cinemachine camera needs a **Cinemachine Impulse Listener** extension (**Add Extension**), or nothing shakes. Setting: **Strength** (`1`). Methods: **Shake**, **ShakeWithStrength (float)**.

### Hit Stop

`Core/Effects/HitStop.cs` · **Add Component → Collin Game → Effects → Hit Stop**

Freezes the game for a moment on a big hit. Put it on an object that stays in the scene, such as the player. Setting: **Duration** (`0.06` seconds). Methods: **Stop**, **StopFor (float)**. It never un-pauses a paused game.

### Cutscene Player

`Core/Effects/CutscenePlayer.cs` · **Add Component → Collin Game → Effects → Cutscene Player**

Plays the Timeline on the same object's **Playable Director** as a cutscene: the player's controls are off while it plays, the Pause button skips it, and pausing is blocked during it.

| Setting | Default | |
|---|---|---|
| Input | `InputReader` | |
| Play On Start · Can Skip | ticked · ticked | |
| Raise On Finished · On Started · On Finished | — | |

Methods: **Play**, **Skip**. Background: [Cutscenes with Timeline](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Cutscenes%20with%20Timeline.md).

---

## Saving

Background: [Saving Progress](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Saving%20Progress.md). Used in: [Ex 08](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex08%20-%20Save%20%26%20Build.md). Both save on the player's computer, and both work in Web builds.

### Variable Saver

`Core/Saving/VariableSaver.cs` · **Add Component → Collin Game → Saving → Variable Saver**

Saves listed variable assets and loads them again.

| Setting | Default | |
|---|---|---|
| Save Name | `Progress` | Savers with the same name share one save |
| Variables | — | Each must have a different asset name |
| Load When Scene Starts | ticked | |
| Save When Scene Ends | unticked | Also saves when the game closes |

Methods: **Save**, **Load**, **DeleteSave** (for "New Game"). A **Variable Resetter** that resets the same variables when the scene starts will undo the load.

### High Score

`Core/Saving/HighScore.cs` · **Add Component → Collin Game → Saving → High Score**

Watches **Score** and copies it into **Best** whenever it's higher, saving the best. Settings: **Score**, **Best**, **Save Name**, **On New Best**. Method: **ResetBest**.

---

## Physics puzzle kit

Imported with the Physics Puzzle Kit package. See [Physics Puzzle Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Physics%20Puzzle%20Kit.md) and [Physics in Unity](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Physics%20in%20Unity.md).

### Launcher 2D

`Kits/PhysicsPuzzle/Scripts/Launcher2D.cs` · **Add Component → Collin Game → Physics Puzzle Kit → Launcher 2D**

A slingshot. Mouse or touch: press inside the yellow circle, drag back, release. Keyboard or gamepad: hold Attack, aim with Move, release. After each shot it waits for the projectile to come to rest, then raises Shot Finished.

| Setting | Default | |
|---|---|---|
| Input · Grab Radius | `InputReader` · `1.5` | |
| Projectile Prefab · Launch Point | — · this object | The prefab needs a Rigidbody 2D |
| Max Pull · Power | `2.5` · `7` | Launch speed = pull × power |
| Shots Left | — | Optional Int Variable; one used per launch |
| Rest Time · Max Shot Time · Remove Projectile After Shot | `0.75` · `8` · unticked | |
| Dot Sprite · Dot Count · Dot Spacing | — · `15` · `0.06` | Aiming dots; no sprite, no dots |
| Raise On Shot Finished · On Launched · On Shot Finished | — | |

### Breakable 2D

`Kits/PhysicsPuzzle/Scripts/Breakable2D.cs` · **Add Component → Collin Game → Physics Puzzle Kit → Breakable 2D**

Breaks (switches off) when hit faster than **Break Speed** (`6`), or when it falls below **Break Below Y** (`-10`). Hits are ignored for **Settle Time** (`1`) after the scene starts. With a Health component, each hard hit takes 1 health instead. When broken: **Add To** / **Amount** (`100`), **Spawn When Broken**, **Raise On Broken**, **On Broken**. Method: **Break**.

### Puzzle Target 2D

`Kits/PhysicsPuzzle/Scripts/PuzzleTarget2D.cs` · **Add Component → Collin Game → Physics Puzzle Kit → Puzzle Target 2D**

Counts itself into **Targets Left** when the scene starts and out when it's switched off. Use it with a Breakable 2D.

### Puzzle Rules

`Kits/PhysicsPuzzle/Scripts/PuzzleRules.cs` · **Add Component → Collin Game → Physics Puzzle Kit → Puzzle Rules**

Won when no targets are left; lost when the last shot finishes with targets left. Sets Targets Left to 0 and Shots Left to **Starting Shots** (`3`) when the scene starts.

| Setting | |
|---|---|
| Targets Left · Shots Left · Starting Shots · Shot Finished | |
| Win Delay | `1` second |
| Raise On Won · Raise On Lost · On Won · On Lost | |
| Score · Points Per Unused Shot | `500` per unused shot, added on a win |

### Rope 2D

`Kits/PhysicsPuzzle/Scripts/Rope2D.cs` · **Add Component → Collin Game → Physics Puzzle Kit → Rope 2D**

Builds a swinging rope of hinged links from this object down to **Hanging Body** when the scene starts. Every link can be cut. Settings: **Link Count** (`10`), **Link Sprite**, **Link Color**, **Thickness** (`0.12`), **Link Mass** (`0.05`).

### Cuttable 2D and Cutter 2D

**Cuttable 2D** switches off its object's joints when cut (and hides it, with **Hide When Cut**). **Cutter 2D**, one per scene, cuts every Cuttable 2D the mouse or a finger swipes across. Optional **Trail** for a visible swipe. Rope links get Cuttable 2D automatically.

### Kit screens

| Screen | Element names |
|---|---|
| `PuzzleHUD` | `shots-label`, `targets-label`, `score-label` |

---

## Top-down adventure kit

Imported with the Top-Down Adventure Kit package. See [Top-Down Adventure Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Adventure%20Kit.md).

### Melee Attack 2D

`Kits/TopDownAdventure/Scripts/MeleeAttack2D.cs` · **Add Component → Collin Game → Top-Down Adventure Kit → Melee Attack 2D**

A sword swing. When Attack is pressed, everything with Health and the **Target Tag** inside a circle in front of the character takes damage, and is pushed back if it has a Knockback 2D. "In front" is the Top Down Controller 2D's facing direction, or left and right from the sprite.

| Setting | Default | |
|---|---|---|
| Input | `InputReader` (filled on the player) | Leave empty for a character that attacks from a script |
| Reach · Radius | `0.8` · `0.6` | Where the hit circle is, and its size. Shown when selected |
| Target Tag · Damage · Knockback Force · Cooldown | `Enemy` · `1` · `8` · `0.35` | |
| Swing Visual · Swing Visual Time | — · `0.15` | A child sprite pointing right, shown briefly and turned to face the attack |
| On Swing · On Hit | — | On Hit runs only when something was hit |

Method: **Attack**.

### Knockback 2D

`Kits/TopDownAdventure/Scripts/Knockback2D.cs` · **Add Component → Collin Game → Top-Down Adventure Kit → Knockback 2D**

Pushes the character back when hit, and switches off its movement scripts for **Stun Time** (`0.2`). A Melee Attack 2D pushes it away from the attacker; other damage, such as Damage On Touch, pushes it away from what it touched last, with **Force When Touched** (`6`). **Stop While Pushed** defaults to the Top Down Controller 2D or Top Down Chaser 2D on the object. Method: **Push**.

### Top Down Chaser 2D

`Kits/TopDownAdventure/Scripts/TopDownChaser2D.cs` · **Add Component → Collin Game → Top-Down Adventure Kit → Top Down Chaser 2D**

A top-down enemy with three states: **Wander** near home, **Chase** the target, **Return** home. Ranges are drawn when selected.

| Setting | Default | |
|---|---|---|
| Wander Speed · Wander Radius · Rest Time | `1` · `2` · `1` | Wander Speed `0` stands still until it notices the target |
| Chase Tag · Notice Range · Give Up Range · Chase Speed | `Player` · `4` · `7` · `2.5` | |
| Needs Line Of Sight · Sight Blockers | ticked · Everything | Walls (solid, non-moving colliders) block its view |
| Acceleration | `20` | |

### Key Door 2D

`Kits/TopDownAdventure/Scripts/KeyDoor2D.cs` · **Add Component → Collin Game → Top-Down Adventure Kit → Key Door 2D**

A solid door that opens (switches off) when the player touches it with at least **Keys Needed** (`1`) in **Keys**. **Use Up Keys** (ticked) takes them away. Without enough keys, writes **Locked Message** to **Message Text**. Events **On Opened**, **On Locked**. Method: **Open** opens it without keys, for switches.

### Camera Room 2D

`Kits/TopDownAdventure/Scripts/CameraRoom2D.cs` · **Add Component → Collin Game → Top-Down Adventure Kit → Camera Room 2D**

One room of a level: a trigger Box Collider 2D or Polygon Collider 2D. When the player enters, the scene's **Cinemachine Confiner 2D** keeps the camera inside the room. **Room Contents** (optional) is switched on only while the player is in the room, and with **Reset Contents On Return** (ticked) comes back fresh each visit. Events **On Entered**, **On Left**.

### Interactable 2D

`Kits/TopDownAdventure/Scripts/Interactable2D.cs` · **Add Component → Collin Game → Top-Down Adventure Kit → Interactable 2D**

A sign, person, chest or lever. While the player is in its trigger area, Interact shows the next of its **Lines** in **Message Text**, and runs **On Used** the first time. **Only Once** for chests and levers. **Prompt** is shown while the player is close. **On Finished** runs after the last line. Method: **Use**.

### UI Heart Row and UI Message Box

**UI Heart Row** draws **Max Hearts** (`5`) hearts in the element named `hearts`, filled up to **Health** (an Int Variable). Optional **Full Heart** and **Empty Heart** sprites; without them, the hearts are colored squares.

**UI Message Box** shows **Message** (a String Variable) in `message-label`, inside `message-box`, which is hidden while the text is empty. It clears after **Clear After** (`4`) seconds.

### Kit screens

| Screen | Element names |
|---|---|
| `AdventureHUD` | `hearts`, `keys-label`, `coins-label`, `message-box`, `message-label` |

---

## Turn-based battle kit

Imported with the Turn-Based Battle Kit package. Builds on the [Turn Manager](#turn-manager) and [Turn Taker](#turn-taker). See [Turn-Based Battle Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Turn-Based%20Battle%20Kit.md).

### Battle Action

`Kits/TurnBasedBattle/Scripts/BattleAction.cs` · **Create → Collin Game → Turn-Based Battle Kit → Battle Action**

An asset for one action, shared by every fighter that has it.

| Setting | Default | |
|---|---|---|
| Display Name · Description | the asset's name · — | Shown in the battle menu |
| Effect | Damage | **Damage**, **Heal**, **Defend** (half damage until the user's next turn) |
| Target | One Opponent | **One Opponent**, **All Opponents**, **Self**, **One Ally** |
| Power · Accuracy | `3` · `95` | Damage = Power + Attack − Defense, at least 1. Accuracy only affects Damage |
| Uses Per Battle | `0` | `0` is no limit |
| Sound | — | A Sound Effect played when used |

### Battle Actor

`Kits/TurnBasedBattle/Scripts/BattleActor.cs` · **Add Component → Collin Game → Turn-Based Battle Kit → Battle Actor**

A fighter. Needs a **Turn Taker** and a **Health** with **Invulnerable Time `0`**, and must be in the Turn Manager's Turn Order. Player fighters are chosen for in the UI Battle Menu; computer fighters heal when at or below **Heal Below** (`0.35` of max) and otherwise attack.

| Setting | Default | |
|---|---|---|
| Controlled By · Actions | Player · — | Actions in menu order |
| Attack · Defense | `0` · `0` | |
| Think Time · Heal Below | `0.8` · `0.35` | Computer only |
| Lunge Part · Lunge Distance | the sprite · `0.4` | Steps toward the target when acting |
| On Action · On Defend · On Dodged | — | |

Methods: **Perform** (action, target), **ReceiveDamage**, **CanUse**, **UsesLeft**.

### UI Battle Menu, Battle Log and Health Bar 2D

**UI Battle Menu** shows a button per action when a player fighter's turn starts, then a button per target when there is a choice, with a Back button. Buttons have the class `battle-button`.

**Battle Log** keeps the last **Lines To Keep** (`4`) lines of what happened in **Log Text** (a String Variable). Method **Add** adds your own line.

**Health Bar 2D** shrinks a **Fill** sprite from the right as **Health** goes down. **Hide When Full** hides the bar until the first hit.

### Kit screens

| Screen | Element names |
|---|---|
| `BattleUI` | `status-label`, `log-label`, `battle-menu`, `actor-label`, `description-label`, `actions`, `targets` |

---

## Arcade classic kit

Imported with the Arcade Classic Kit package. See [Arcade Classic Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Arcade%20Classic%20Kit.md).

### Paddle 2D

`Kits/ArcadeClassic/Scripts/Paddle2D.cs` · **Add Component → Collin Game → Arcade Classic Kit → Paddle 2D**

A kinematic paddle that slides along one line between **Min Position** and **Max Position** (`-7`, `7`; shown when selected).

| Setting | Default | |
|---|---|---|
| Moves Along · Controlled By | Horizontal · Player | **Vertical** for Pong; **Computer** follows the ball |
| Input · Follow Mouse | `InputReader` · ticked | |
| Speed | `12` | |
| Computer Speed · Computer Dead Zone | `0.6` · `0.3` | Lower speed or a bigger dead zone is easier to beat |

### Ball 2D

`Kits/ArcadeClassic/Scripts/Ball2D.cs` · **Add Component → Collin Game → Arcade Classic Kit → Ball 2D**

Bounces at a steady speed. Where it hits a Paddle 2D sets the angle it leaves at. Waits before each serve; Jump or Attack serves.

| Setting | Default | |
|---|---|---|
| Play Direction | Up And Down | **Side To Side** for Pong |
| Start Speed · Speed Up Per Paddle Hit · Max Speed | `8` · `0.3` · `16` | |
| Max Bounce Angle · Min Angle | `60` · `15` | Min Angle keeps it from going too flat |
| Serve From · Serve Offset | — · `0, 0.5` | Empty waits at the starting point |
| Serve Direction · Random Serve Side | `0.3, 1` · ticked | |
| Input · Auto Serve | `InputReader` · `0` | Auto Serve serves after that many seconds |
| On Serve · On Paddle Hit · On Bounce | — | |

Methods: **Serve**, **ResetBall**.

### Ball Goal 2D, Brick 2D and Counted Object

**Ball Goal 2D** is a trigger past an edge. When the ball enters, **Change Variable** changes by **Amount** (`-1`), and the ball goes back to be served, toward **Next Serve Direction** if set.

**Brick 2D** breaks after **Hits To Break** (`1`) hits by the ball (or by objects tagged **Also Broken By Tag**), changing color by **Color By Hits Left**. When broken: **Add To** / **Amount** (`10`), **Spawn When Broken**, **On Broken**.

**Counted Object** keeps **Count** (an Int Variable) equal to the number of these objects in the scene, including ones created later. Pair it with an Int Variable Condition (Equal To 0). Don't reset that variable with a Variable Resetter.

### Ship Controller 2D, Shooter 2D and Screen Wrap 2D

**Ship Controller 2D**: left and right turn (**Turn Speed** `220`), up thrusts (**Thrust** `9`) up to **Max Speed** (`8`); **Drag** (`0.4`) slows it. **Engine Flame** shows while thrusting. Method **StopAndFaceUp**, for a Respawner's On Respawn.

**Shooter 2D** fires **Projectile Prefab** from **Muzzle** when Attack is pressed. **Aim**: Muzzle Up, Muzzle Right or Move Direction. **Projectile Speed** (`14`), **Shots Per Second** (`5`), **Hold To Fire**, **Max On Screen** (`4`; `0` is no limit), **Add Shooter Velocity**, **On Shoot**. Shots never hit the shooter. Method: **Shoot**.

**Screen Wrap 2D** brings an object back on the opposite edge when it goes past **Margin** (`0.5`). Needs an orthographic camera that doesn't move.

### Drift 2D and Split On Death 2D

**Drift 2D** sends a Rigidbody 2D drifting in a random direction at **Min Speed**–**Max Speed** (`1`–`2.5`), spinning up to **Max Spin** (`60`).

**Split On Death 2D** creates **Pieces** (`2`) of **Piece Prefab** when its Health runs out, spread by **Spread** (`0.3`).

### Kit screens

| Screen | Element names |
|---|---|
| `ArcadeHUD` | `score-label`, `best-label`, `lives-label` |
| `PongHUD` | `left-score`, `right-score` |

---

## Top-down shooter kit

Imported with the Top-Down Shooter Kit package. See [Top-Down Shooter Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Top-Down%20Shooter%20Kit.md).

### Weapon

`Kits/TopDownShooter/Scripts/WeaponData.cs` · **Create → Collin Game → Top-Down Shooter Kit → Weapon**

A weapon as an asset, shared by the player, enemies and power-ups.

| Setting | Default | |
|---|---|---|
| Display Name | the asset's name | Shown in the HUD |
| Projectile Prefab · Projectile Speed · Damage | — · `14` · `1` | The prefab needs a Projectile 2D |
| Shots Per Second | `6` | |
| Projectiles Per Shot · Spread Angle · Inaccuracy | `1` · `30` · `0` | More than one projectile makes a spread |
| Hold To Fire | ticked | Unticked: one shot per press |
| Sound | — | Played on each shot |

### Weapon Shooter 2D

`Kits/TopDownShooter/Scripts/WeaponShooter2D.cs` · **Add Component → Collin Game → Top-Down Shooter Kit → Weapon Shooter 2D**

Fires a Weapon. **Fire When**: **Attack Button** (the player) or **Automatic** (enemies, every **Auto Fire Interval** seconds after **First Shot Delay**, within **Range**). **Direction**: **Aim** (an Aim 2D on the object), **At Target** (the object tagged **Target Tag**) or **Forward** (the object's up). **Muzzle** is where shots start. **Weapon Name** (a String Variable) shows the weapon in the HUD. Methods: **SetWeapon** (for good, or for some seconds before the starting weapon returns), **TryFire**. Event **On Shoot**.

### Projectile 2D

`Kits/TopDownShooter/Scripts/Projectile2D.cs` · **Add Component → Collin Game → Top-Down Shooter Kit → Projectile 2D**

A bullet: flies straight, damages the first object with Health and the **Target Tag** (`Enemy`), and disappears after **Lifetime** (`2`) or on hitting a wall (**Stopped By Walls**). Never hits its shooter. Projectiles are reused rather than destroyed. Optional **Hit Effect**. Needs a trigger collider; the sprite should point up.

### Aim 2D

`Kits/TopDownShooter/Scripts/Aim2D.cs` · **Add Component → Collin Game → Top-Down Shooter Kit → Aim 2D**

Twin-stick aiming. **Aim With**: **Mouse Or Stick** (the pointer once the mouse moves, the right stick when pushed past **Stick Dead Zone**), **Move Direction**, or **Fixed Direction** (for a scrolling shooter's ship). **Turn To Aim** turns a child that points right; **Sprite To Flip** flips to face the aim (set the Top Down Controller 2D's **Facing** to **None**). Read by other scripts: **Direction**.

### Enemy Mover 2D

`Kits/TopDownShooter/Scripts/EnemyMover2D.cs` · **Add Component → Collin Game → Top-Down Shooter Kit → Enemy Mover 2D**

**Pattern**: **Chase**, **Straight** (along **Fly Direction**), **Wave** (along Fly Direction, weaving **Wave Width** at **Waves Per Second**), **Circle** (around the target at **Preferred Distance**), **Keep Away** (holds Preferred Distance). **Speed** (`2.5`), **Target Tag** (`Player`), **Face Movement** (sprite pointing up).

### Wave Spawner 2D

`Kits/TopDownShooter/Scripts/WaveSpawner2D.cs` · **Add Component → Collin Game → Top-Down Shooter Kit → Wave Spawner 2D**

**Waves**, each a list of groups (enemy prefab and count) with **Seconds Between Enemies**. Enemies appear at random **Spawn Points**. The next wave starts **Pause Between Waves** (`2`) after every enemy of the last is gone. **Start Automatically** or call **Begin**; **Loop** for endless waves. **Wave Number** and **Enemies Left** (Int Variables), **Raise When Cleared**, **On Wave Started**, **On Cleared**.

### Power Up 2D and Drop On Death 2D

**Power Up 2D** gives the collector's Weapon Shooter 2D a **Weapon** for **Duration** (`10`; `0` is for good). **Disappear After** removes it if not picked up.

**Drop On Death 2D** leaves one of its **Drops**, chosen at random, with probability **Chance** (`0.25`) when its Health runs out.

### Keep On Screen 2D, Scroll Camera 2D and Wake On Screen 2D

**Keep On Screen 2D** keeps an object inside the main camera's view, **Margin** (`0.5`) from the edge.

**Scroll Camera 2D**, on the Main Camera, moves it along **Direction** at **Speed** (`2`) after **Start Delay**, stopping after **Stop After** (`100`) units and raising **Raise At End**. Methods **PauseScrolling**, **ResumeScrolling**.

**Wake On Screen 2D** keeps an enemy's Enemy Mover 2D and Weapon Shooter 2D off until it comes within **Wake Margin** of the screen, and removes it once it's **Remove Margin** outside again.

### Kit screens

| Screen | Element names |
|---|---|
| `ShooterHUD` | `health-label`, `score-label`, `wave-label`, `weapon-label` |

---

## Endless runner kit

Imported with the Endless Runner Kit package. See [Endless Runner Kit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Endless%20Runner%20Kit.md).

### Runner Controller 2D

`Kits/EndlessRunner/Scripts/RunnerController2D.cs` · **Add Component → Collin Game → Endless Runner Kit → Runner Controller 2D**

Runs right by itself, speeding up from **Start Speed** (`6`) by **Speed Gain Per Second** (`0.1`) to **Max Speed** (`14`), after **Start Delay** (`1`). Writes the distance run to **Distance** (an Int Variable), one point per **Units Per Point**. Stops when the Health on the same object runs out.

| Style | Settings |
|---|---|
| **Jump** | Jump Height `3.2`, Extra Air Jumps `0`, Short Hop Speed Kept `0.5`, Coyote Time `0.1`, Jump Buffer Time `0.15`; Can Slide (hold down), Slide Height `0.5`, Slide Sprite |
| **Jetpack** | Hold Jump: Thrust `45`, Max Rise Speed `8` |
| **Lanes** | Up and down change lane: Lane Heights `-2.5, 0, 2.5`, Start Lane `1`, Lane Change Time `0.12`. No gravity |

Also: Gravity Scale `3.5`, Fall Gravity Multiplier `1.5`, Max Fall Speed `25`, Ground Layers. Events **On Jump**, **On Land**, **On Lane Change**, **On Stopped**. Read by other scripts: **Speed**, **Difficulty** (0 to 1 as the speed ramps), **DistanceRun**, **IsRunning**, **IsGrounded**, **IsSliding**. Methods: **Stop**, **GoToLane**.

### Track Chunk and Track Spawner 2D

**Track Chunk** marks a prefab as one piece of track, starting at its position and **Length** (`20`) units long, allowed between **Min Difficulty** and **Max Difficulty**, picked in proportion to **Weight**. Select it to see its start (green) and end (red).

**Track Spawner 2D** places **First Chunk**, then keeps **Build Ahead** (`40`) units of chunks ahead of the runner, picked at random from **Chunks** by difficulty and weight (**Avoid Repeats**), and removes chunks **Remove Behind** (`20`) units behind it.

### Parallax 2D

`Kits/EndlessRunner/Scripts/Parallax2D.cs` · **Add Component → Collin Game → Endless Runner Kit → Parallax 2D**

A background layer that moves at a share of the camera's speed: **Distance** `0` moves with the world, `1` with the camera. Repeats forever: give the sprite Draw Mode **Tiled** and three times its width. **Vertical** follows the camera up and down too.

### Coin Magnet 2D and Magnet Power-Up 2D

**Coin Magnet 2D**, on the player, pulls Collectibles within **Radius** (`4`) at **Pull Speed** (`18`), while on: **Always On**, or for some seconds after **Activate**. **Active Effect** is shown while it's on.

**Magnet Power-Up 2D** turns the collector's magnet on for **Duration** (`8`).

### Kit screens

| Screen | Element names |
|---|---|
| `RunnerHUD` | `distance-label`, `best-label`, `coins-label` |

---

## Editor tools

| Tool | Where | What it does |
|---|---|---|
| Current Value | Inspector of any variable, during Play | Shows the live value |
| Raise | Inspector of any Void Event Channel, during Play | Raises the event, for testing |
| Reapply Art Import Settings | **Collin Game → Art** menu | Gives the course's art packs their pixel-art settings again |
| Build Platformer Sample | **Collin Game → Kit Samples** menu | Builds the Platformer Kit's sample game: data, prefabs, tiles, two levels, menu and win scenes, and the Scene List. Replaces the kit's `Sample` folder |
| Use Course Panel Settings in Open Scenes | **Collin Game → UI** menu | Sets `CoursePanelSettings` on every UI Document in the open scenes |
| Repair Course Panel Settings | **Collin Game → UI** menu | Creates `CoursePanelSettings` if it's missing, and puts back its settings |
| Course Panel Settings for new UI Documents | Automatic | A new UI Document with no Panel Settings gets `CoursePanelSettings` |

---

## Recipes

| To make… | Use |
|---|---|
| A coin that adds to the score | Trigger collider + **Collectible** (Add To `Score`) |
| A key that opens a door | Key: **Collectible** (Raise Event `KeyCollected`). Door: **Void Event Listener** → **GameObject → SetActive**, unticked |
| A door that opens at 10 coins | **Int Variable Condition** (Coins, At Least, 10) → hide the door |
| Spikes | Trigger collider + **Damage On Touch** |
| A bottomless pit | Large trigger collider below the level + **Kill Zone** |
| A player who dies and comes back | **Health** + **Respawner**, plus **Checkpoint**s in the level |
| Lives | Health's **On Died** → `Lives` **Add (-1)**; **Int Variable Condition** (Lives, At Most, 0) raises `GameOver` |
| A goal that ends the level | Trigger collider + **Trigger Zone** (Raise On Enter `LevelCompleted`) |
| A win screen | UI Document (`EndScreen`) + **UI Screen** (Hidden At Start) + **Void Event Listener** (`LevelCompleted` → **UIScreen → Show**) |
| A HUD | UI Document (`HUD`) + **UI Variable Binder** |
| A pause menu | UI Document (`PauseMenu`) + **UI Screen** + **Pause Controller** + **UI Button Events** |
| Falling rocks | A rock prefab (**Damage On Touch** with Remove Self After Hit, **Lifetime**) + **Spawner** |
| A moving platform | Collider + **Waypoint Mover 2D** |
| An enemy that patrols and hurts | Solid collider + **Patrol Enemy 2D** + **Damage On Touch** or **Stompable Enemy 2D** |
| A turn-based battle | **Turn Manager** + a **Turn Taker**, **Turn Actions** and **Health** on each participant |
| Sound for an action | A **Sound Effect** asset; the action's event → **SoundEffect → Play** |
| Music | A **Music Player** in each scene |
| A shake when hurt | **Camera Shake** on the player, **Impulse Listener** on the camera; Health **On Damaged** → **CameraShake → Shake** |
| A settings screen | UI Document (`Settings`) + **UI Screen** + **UI Settings** + **UI Button Events**; the menu's `settings-button` → **UIScreen → Show** |
| A saved high score | **High Score** (Score, Best) + Best shown with a **UI Variable Binder** |
| An opening cutscene | A Timeline on a **Playable Director** + **Cutscene Player** |
| A slingshot level | **Launcher 2D** + blocks with **Breakable 2D** + targets with **Puzzle Target 2D** + **Puzzle Rules** |
| A rope to cut | **Rope 2D** with a Hanging Body + a **Cutter 2D** in the scene |
| A sword attack | **Melee Attack 2D** on the player; enemies tagged `Enemy` with **Health** and **Knockback 2D** |
| A locked door | Key: **Collectible** (Add To `Keys`). Door: solid collider + **Key Door 2D** |
| A camera that moves room by room | A **Camera Room 2D** per room + a **Cinemachine Confiner 2D** on the Cinemachine Camera |
| A sign or a person to talk to | Trigger collider + **Interactable 2D** + a **UI Message Box** on the HUD |
| A battle with a menu | **Turn Manager** + fighters with **Battle Actor** + `BattleUI` with **UI Battle Menu** |
| Breakout | **Paddle 2D** + **Ball 2D** + bricks with **Brick 2D** and **Counted Object** + a **Ball Goal 2D** below |
| Asteroids | **Ship Controller 2D** + **Shooter 2D** + asteroids with **Drift 2D**, **Split On Death 2D** and **Counted Object**, all with **Screen Wrap 2D** |
| A 3D player with a camera behind | **Tank Controller 3D** + a Cinemachine Camera (Follow, Lock To Target With World Up; Rotation Composer) |
| A path the player can't fall off | A Spline Container + **Rail Runner 3D** |
| Twin-stick shooting | **Aim 2D** + **Weapon Shooter 2D** (Attack Button, Aim) + a Weapon asset with a Projectile 2D prefab |
| Waves of enemies | **Wave Spawner 2D** with spawn points just off screen |
| A scrolling shooter | **Scroll Camera 2D** on the Main Camera, **Keep On Screen 2D** on the player, **Wake On Screen 2D** on each enemy |
| An endless runner | **Runner Controller 2D** + a **Track Spawner 2D** with **Track Chunk** prefabs + a long **Kill Zone** below |
| Background that scrolls slower than the world | **Parallax 2D** on each layer |
| Starting a new game from the menu | **Variable Resetter** in the menu scene, with every variable that carries between levels |

## Common Console messages

| Message says… | Fix |
|---|---|
| "Input is empty" | Drag `InputReader` from `Assets/_Course/Core/Input` into the **Input** field |
| "can't find a scene named…" | Check the spelling, and add the scene to the Scene List |
| "no Channel is set" / "no Variable is set" | Fill in the empty field the message names |
| "there is no button named…" / "no label named…" | Check the name against the UXML element names above |
| "has no Respawner" | Add a **Respawner** to the player |
| "has no 2D collider" | Add a collider to the object named |
| "Prefab is empty" | Drag a prefab from the **Project** window into the Spawner |
