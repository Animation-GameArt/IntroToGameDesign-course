---
title: "Stealth Kit"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
  - 3d
---

# Stealth Kit

The Stealth Kit is a starting point for 3D stealth and horror games: move carefully, watch what's hunting you, hide or slip past, reach the objective. Examples: Amnesia, Alien: Isolation, Untitled Goose Game, the stealth sections of many games.

The sample, *Night Shift*, is a small office building after hours. Two guards walk their rounds. Find three keys, open the exit, and get out without being caught. You can crouch to move quietly, hide in lockers and under desks, and use a flashlight whose battery runs down.

Read **About 3D games** on the Genre Map first. Fear and tension come from sound, light and pacing as much as from scripts, so leave time for all three.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Guards or monsters that patrol, see, hear, search and chase | Guards that talk to each other or call for help |
| A view cone, blocked by walls; seeing farther when your flashlight is on | Seeing in the dark versus the light (lighting levels) |
| Hearing: sprinting is loud, walking less so, crouching nearly silent | Sounds from thrown objects |
| Hiding spots: lockers, under desks | Hiding bodies, disguises |
| An alert meter and a "Spotted!" warning | Combat, or knocking guards out |
| A flashlight with a battery, and battery pickups | Doors that open and close for guards (a custom script) |
| Third person (with view cones shown) or first person (a horror game) | Several floors with stairs for guards (it works, with care) |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut. The Genre Map's advice stands: one building, one enemy (two at most), three objectives and an exit.

## Install the kit

The kit's guards walk on a **NavMesh**, which needs Unity's **AI Navigation** package. Install it once per project: **Window → Package Manager → Unity Registry → AI Navigation → Install**.

1. Download the Stealth Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/Stealth/Sample/Scenes`, add `NightShift_Menu` and `NightShift_Level`, next to each other, in that order.
4. Open `NightShift_Menu` and press **Play**.

| Action | Keyboard and mouse | Gamepad |
|---|---|---|
| Move | WASD | Left stick |
| Look around | Mouse | Right stick |
| Crouch (hold) | C | Right face button |
| Sprint (loud!) | Left Shift | Left stick press |
| Flashlight | Left click | Left face button |
| Pause | Esc | Start |

## How it works

- **Guard 3D** walks between its patrol points on the NavMesh. It **sees** the player inside its view cone if no wall is in the way, and fills its **alert meter**: fast up close, slowly at the edge of its view. At a third full it comes to investigate; full, it chases. It **hears** the player within its hearing range times how loud they are. Out of sight for long enough, it searches where it last saw them, then goes back to its rounds. Getting close enough while chasing catches the player.
- **Stealth Target 3D**, on the player, tells guards how loud the player is, whether they're hidden, and whether their flashlight is on.
- **Player Controller 3D** (from the course's 3D scripts) gives the player crouching, which is slow but nearly silent.
- **Hiding Spot 3D** is a trigger area. Inside it (crouching, for some), guards can't see or catch the player, though they may still come looking.
- **Flashlight 3D** is a spot light the player switches on and off. It runs down its battery; battery pickups refill it. While it's on, guards see the player from farther away.
- **Vision Cone 3D** draws a guard's view on the floor, colored by its alert. **Alert Audio** fades in a heartbeat as guards grow alert. The **UI Stealth HUD** shows the alert meter and *Unseen*, *Hidden*, *Suspicious* or *Spotted!*
- The keys are Core **Collectibles**. An **Int Variable Condition** opens the exit when all three are found.

## What's in the sample

| Object | What it is | Worth changing |
|---|---|---|
| `Player` | Player Controller 3D (crouch on, jump off), Stealth Target 3D, a Flashlight 3D | **Walk Speed**, **Crouch Speed** |
| `Guard A`, `Guard B` | Guard 3D with a NavMesh Agent and a Vision Cone 3D | **View Distance**, **View Angle**, **Hearing Range**, **Time To Spot** |
| `Lockers`, `Desks` | Hiding Spot 3D (desks need crouching) | |
| `Key 1`–`Key 3`, `Battery` | Collectibles | |
| `Exit` | A door that opens at three keys, and the escape trigger | |
| `Stealth Systems` | HUD, alert audio, pause, caught and escaped screens | |

## Start your own game

1. Draw your building from above on paper: rooms, doors, each guard's route, where the keys are, and where to hide. Make sure every key can be reached by waiting for the right moment, not only by luck.
2. Open `NightShift_Level`, **File → Save As…** into `Assets/_Game/Scenes`, and rebuild the rooms with Cubes.
3. After changing walls or floors, select `Level` and click **Bake** on its **NavMesh Surface**. Guards can only walk where the NavMesh (the blue overlay) is.
4. Move the guards' patrol points to your routes.
5. Press **Play** and sneak through. Then try to get caught on purpose, to see how the guards react.

### Designing stealth

- **Readable guards.** The player should always be able to tell where a guard is looking. View cones, a flashlight beam, footstep sounds, or a sound when they turn.
- **Safe spots between dangers.** A hiding place before each tricky stretch lets players watch and plan.
- **Make getting spotted a second chance, not a loss.** The sample's guards fill their meter over a second, so a player who's seen can still duck away.
- **For horror, take information away.** Hide the view cones and the alert meter; let sound and the flashlight carry the fear.

## Recipes

**A first-person horror game.** On the player, set **Facing** to **Face Camera** and hide the body. Replace the orbit camera with a Cinemachine Camera at the player's head: Position Control **Hard Lock To Target** (target: a `Head` child at `0, 1.6, 0`), Rotation Control **Pan Tilt**, and an Input Axis Controller using `Player/Look`. Make the Flashlight a child of the camera. Untick the Vision Cone 3D renderers, and remove the alert meter from the HUD.

**One monster instead of guards.** One Guard 3D with a long Hearing Range, a short View Distance, and a fast Chase Speed.

**A guard that stands still.** One patrol point, and a wide View Angle; it turns to look around when it hears something.

**Battery pickups.** A Collectible whose **On Collected** calls **Flashlight3D → AddBattery** with `50`.

**No flashlight limit.** Set **Battery Seconds** to `0`.

**A caught sound.** The Guard 3D's **On Caught** plays a Sound Effect; **On Chase** is good for a sting.

## If something goes wrong

| What you see | What to do |
|---|---|
| "Guard … is not close enough to the NavMesh" or guards don't move | Install AI Navigation, add a **NavMesh Surface** to the level, and **Bake**. The guard must start on the blue area |
| Guards walk through walls | Bake the NavMesh again after moving walls |
| Guards see through walls | The walls need colliders, and must be on a layer in **Blocks View** |
| Guards never notice you | The player needs **Stealth Target 3D** and the **Player** tag; check **View Distance** and **View Angle** |
| Hiding doesn't work | The Hiding Spot 3D needs a trigger collider covering the spot; desks need crouching |
| You're caught while hidden | The player's collider is partly outside the hiding spot's trigger: make the trigger bigger |
| The flashlight doesn't light anything | It needs a **Spot Light** on the same object, pointing forward |
| The vision cone is invisible | Its Mesh Renderer needs a transparent, unlit material |
