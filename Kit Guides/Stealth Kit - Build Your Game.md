---
title: "Stealth Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Stealth Kit — Build Your Game

This guide takes you from your ten-pager to your own finished stealth or horror game, built with the Stealth Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Stealth Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Stealth%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, with the **AI Navigation** package, and you've played the sample from its menu to the end.
- [ ] You've opened `NightShift_Level` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **Stealth or horror:** third person with view cones, or first person in the dark | | Third person, view cones shown |
| **The place:** rooms, and how they connect | | An office building: lobby, office, storage, break room, security |
| **Guards or monster:** how many, their routes, sight and hearing | | Two guards: View Distance `11`, View Angle `90`, Hearing Range `10` |
| **Hiding:** where, and whether it needs crouching | | Lockers; under desks (crouching) |
| **Flashlight:** battery length, and pickups | | 120 seconds; one battery pickup |
| **Objectives:** what the player collects or does | | Three keys |
| **Goal and losing:** how it ends | | Reach the exit; caught once and it's over |
| **Mood:** lighting and sound | | Dim blue light, a heartbeat that rises with alert |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. One building, one or two enemies, three objectives and an exit is a complete stealth or horror game in eight weeks. Light and sound make the mood: leave time for both.

## Stage 1 — First Playable

The goal: one guard on its route, a room or two, one objective and the exit, from the menu to escaping or being caught, in grey boxes.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your data and materials

Create your objective counter (such as `Keys`), `Battery` (Float Variable, `100`), `Message` (String Variable), and Escaped, Caught and exit-opened Void Event Channels in `_Game/Data`.

*Worked example:* [Part 1 — Data and materials](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Stealth%20Kit%20-%20Building%20the%20Sample.md#part-1--data-and-materials).

### 3. Your building, blocked in

1. Create a 3D scene in `_Game/Scenes`; set the camera's **Renderer** to **Universal Renderer**. Make it dark.
2. Block out your first rooms with Cubes: floor, walls with door gaps, furniture that blocks sight.
3. Add a **NavMesh Surface** to the parent of the level and click **Bake**.

*Worked example:* [Part 2 — The building](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Stealth%20Kit%20-%20Building%20the%20Sample.md#part-2--the-building).

### 4. Your player

Build your player (or copy the sample's): **Player Controller 3D** (crouch on, jump off), **Stealth Target 3D**, a Spot Light with **Flashlight 3D**, the camera and **Cursor Lock 3D**. For first person, see the recipe in **Stealth Kit**.

*Worked example:* [Part 3 — The player](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Stealth%20Kit%20-%20Building%20the%20Sample.md#part-3--the-player).

### 5. Your first guard

Make a **Prefab Variant** of the sample's `Guard`, set its sight, hearing and speeds from your table, and give it a route of patrol points. Watch it walk the route before adding anything else.

*Worked example:* [Part 4 — Guards](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Stealth%20Kit%20-%20Building%20the%20Sample.md#part-4--guards).

### 6. Hiding, an objective and the exit

Add a hiding spot, your first objective (a Collectible), the exit door that opens when objectives are done, and the escape trigger.

*Worked example:* [Part 5 — Hiding, keys and the exit](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Stealth%20Kit%20-%20Building%20the%20Sample.md#part-5--hiding-keys-and-the-exit).

### 7. Systems, menu and Scene List

Copy the sample's `Stealth Systems` with your variables, and `NightShift_Menu` into `_Game/Scenes` with Play loading your level. In the Scene List: menu, then your level.

*Worked example:* [Part 6 — Stealth Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Stealth%20Kit%20-%20Building%20the%20Sample.md#part-6--stealth-systems) and [Part 7 — Menu](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Stealth%20Kit%20-%20Building%20the%20Sample.md#part-7--menu).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your guard walks its route, sees you in its view, hears you sprint, searches, chases and catches you.
- [ ] Hiding works, and crouching is quiet.
- [ ] Your first objective opens the exit; reaching it shows the escaped screen, and being caught shows the caught screen.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every room and guard and every feature exists and works. Art and balance can still be rough.

### Your whole building

Block out every room. Give each guard a route that crosses the player's path at moments the player can learn and wait for. Put a hiding place before each tricky stretch.

### All your objectives, and the flashlight

Every objective and battery is placed. Bake the NavMesh again after changing walls.

### Every screen

Menu, pause, escaped and caught and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every room, guard, hiding spot and objective in your table is in.
- [ ] Every objective can be reached by waiting for the right moment, not only by luck.
- [ ] Every guard state can be seen in play: patrol, investigate, chase, give up.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, escaped and caught, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace grey boxes with your art. Keep guards readable in the dark: a light, a visor, a sound. For horror, hide the view cones and the alert meter.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Sound carries this genre. Good places: Guard 3D's **On Suspicious**, **On Chase**, **On Gave Up** and **On Caught**; the flashlight's **On Switched On**; a hiding spot's **On Enter**; and **Alert Audio** for the heartbeat. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch where they get caught and where they're bored. Adjust Time To Spot, View Distance, Hearing Range and guard routes one at a time. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Every guard reaction has a sound, and the mood holds from start to finish.
- [ ] A careful playtester usually escapes; a careless one is usually caught.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| A guard noticing, chasing or giving up | **Guard 3D** → On Suspicious, On Chase, On Gave Up |
| Being caught | **Guard 3D** → On Caught, or the Caught event |
| Hiding | **Hiding Spot 3D** → On Enter, On Exit |
| The flashlight | **Flashlight 3D** → On Switched On, On Switched Off, On Empty |

| To make the kit do something… | Call |
|---|---|
| Refill the battery | **Flashlight 3D → AddBattery** |
| Show a message | **StringVariable → SetValue** on `Message` |
| Show the pointer | **Cursor Lock 3D → Unlock** |
| Read how alert the guards are | **Guard3D.HighestAlert**, **AnyChasing** (from a script) |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
