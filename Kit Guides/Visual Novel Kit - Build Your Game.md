---
title: "Visual Novel Kit — Build Your Game"
course: GAME 1303
status: draft
course_version: 0.22.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Visual Novel Kit — Build Your Game

This guide takes you from your ten-pager to your own finished visual novel or dating sim, built with the Visual Novel Kit. You've played the sample; now you build **your** game with the same parts, step by step. Every step uses a decision from your design, not a value from the sample.

Each stage ends with checks for a milestone: **First Playable** (Week 10), **Alpha** (Week 12) and **Beta** (Week 14). Your milestone assignments use these checks.

> [!tip] Stuck on a step?
> Each step names the part of **[Visual Novel Kit — Building the Sample](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Visual%20Novel%20Kit%20-%20Building%20the%20Sample.md)** that does the same thing with the sample's values. It's a worked example: read it to see how, then do it with your own decisions.

## Before you start

- [ ] The kit is installed, and you've played the sample from its menu to the end.
- [ ] You've opened `Story_Game` and clicked through its Hierarchy.
- [ ] Your decisions table (below) is filled in on page 10 of your ten-pager.

## Your decisions

Fill this in on page 10 of your ten-pager. Every step below uses it. An empty row is a decision you haven't made yet: make it before you build that part.

| Decision | Your answer | The sample's answer, for comparison |
|---|---|---|
| **The story:** in one sentence, and how long it is | | A night at a lantern festival; about 10 minutes |
| **Characters:** each one's name, name color, and moods you'll draw | | Ren (orange), Mika (blue), one portrait each |
| **Scenes:** each one's place and what happens | | The square, the stalls, the bridge |
| **Choices that matter:** which choices change what happens later | | Helping Ren find the ticket; who you stand with on the bridge |
| **Variables:** what the story remembers (affection, flags) | | `$ren`, `$mika`, `$helped_ren` |
| **Endings:** how many, and what leads to each | | 3: Ren's, Mika's, alone |
| **Dating sim meters:** shown or hidden | | Shown, out of 6 |
| **Art and sound:** backgrounds, portraits, music | | Plain colors and tiny portraits (placeholders) |
| **Custom scripts:** anything agreed at your pitch that the kit doesn't do | | None |

Keep it small. Three to five scenes, two or three characters and two or three endings is a complete visual novel in eight weeks. Writing and art take most of the time; plan both.

## Stage 1 — First Playable

The goal: your first scene, with your characters, one meaningful choice and at least one ending, from the menu to that ending.

### 1. Set up your folders

In `Assets/_Game`, create `Scenes`, `Prefabs`, `Data` and `Art` (if they don't exist yet). Everything you make goes in `_Game`. Never edit anything in `_Course`: an update to the course project would undo it.

### 2. Your story files

In `_Game/Story`, create a Yarn Script (**Create → Yarn Spinner → Yarn Script**) and a Yarn Project (**Create → Yarn Spinner → Yarn Project**). Write your first scene: a `Start` node, `<<declare>>` your variables, and your first choice. Click the Yarn Project to check for errors.

*Worked example:* [Part 1 — The Yarn Project](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Visual%20Novel%20Kit%20-%20Building%20the%20Sample.md#part-1--the-yarn-project).

### 3. Your data and characters

Create an Int Variable for each meter, and a Void Event Channel for each ending, in `_Game/Data`. Create a **Character** for each character (**Create → Collin Game → Visual Novel Kit → Character**), with the name exactly as in your script, a name color and a portrait.

*Worked example:* [Part 2 — Data](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Visual%20Novel%20Kit%20-%20Building%20the%20Sample.md#part-2--data) and [Part 3 — Characters](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Visual%20Novel%20Kit%20-%20Building%20the%20Sample.md#part-3--characters).

### 4. Your story scene

1. Open `Story_Game`, **File → Save As…** into `_Game/Scenes`.
2. **Dialogue Runner**: your Yarn Project, **Start Node** `Start`.
3. **Visual Novel Stage**: your characters, your backgrounds (a sprite, or a color for now), and your endings in **Events**.
4. **Yarn Variable Link** and **UI Relationship Meters**: your variables (or remove them if you have no meters).
5. Make an ending screen for each ending, shown by its event.

*Worked example:* [Part 4 — Story Systems](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Visual%20Novel%20Kit%20-%20Building%20the%20Sample.md#part-4--story-systems).

### 5. Your menu and Scene List

Copy `Story_Menu` into `_Game/Scenes`, make Play load your story, and change the title. In the Scene List: menu, then your story.

*Worked example:* [Part 5 — Scenes](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Visual%20Novel%20Kit%20-%20Building%20the%20Sample.md#part-5--scenes).

### First Playable checks

- [ ] A build runs outside Unity, starting at your menu (see [Making Builds](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Making%20Builds.md)).
- [ ] Your first scene plays from the menu, with your characters appearing, speaking in their colors, and darkening when silent.
- [ ] At least one choice changes a variable, and something later depends on it.
- [ ] At least one ending can be reached and shows its screen.
- [ ] No Yarn errors, and no Console warnings about missing characters, backgrounds or events.
- [ ] Nothing gets you permanently stuck.

## Stage 2 — Alpha

The goal: every scene and ending and every feature exists and works. Art and balance can still be rough.

### Your whole story

Write the rest of your scenes and every ending. Read it aloud. Check each locked choice can be unlocked, and each ending can be reached.

### Your art in place, even rough

Every character has their moods (`<<mood>>`) and every scene its background, even as rough sketches.

### Every screen

Menu, pause, every ending screen and credits all work. Add your own assets to the credits: create a text file like the course's `Course Credits` in `_Game`, and add it to the **UI Credits** component in your menu.

### Alpha checks

- [ ] Every scene and ending in your table is written and can be reached.
- [ ] Every character and background is in, even if rough.
- [ ] Choices that matter change what happens later, and the meters (if shown) move.
- [ ] Each custom script does its job, or is marked as cut with a reason.
- [ ] Every screen works: menu, pause, every ending screen, credits.
- [ ] You have a written list of placeholders still to replace.

## Stage 3 — Beta

The goal: it looks, sounds and feels finished. No new features.

### Art

Replace placeholders with your backgrounds and portraits. Draw portraits at the same size and framing, so characters line up when they stand together.

### Sound and juice

As in Exercise 07: create **Sound Effect** assets and play them from events. Good places: the presenter's **On Line Started** (a soft blip), `<<sound>>` and `<<music>>` commands in your script, and each ending screen. Add music with a **Music Player**. Add screen shake or particles where a moment should feel big.

### Balance

Playtest with someone who hasn't played it (Exercise 10). Watch where they skim and where they slow down. Cut lines nobody reads; make sure every ending is found by someone. Change one number at a time, and write down what you changed.

### Beta checks

- [ ] Final art and sound are in; any placeholder left is on purpose.
- [ ] Music plays in every scene, and key moments have sounds.
- [ ] Every ending has been reached by a playtester.
- [ ] Your three changes from the playtest are made.
- [ ] The credits list every asset you didn't make, with its license.
- [ ] Volume settings and Quit work.

## Custom scripts

Custom scripts agreed at your pitch go in `Assets/_Game/Scripts`. Connect them to the kit through what it already announces, instead of changing kit scripts:

| To react to… | Listen to |
|---|---|
| Dialogue starting or ending | **UI Dialogue Presenter** → On Dialogue Started, On Dialogue Complete |
| A line starting | **UI Dialogue Presenter** → On Line Started |
| A Yarn variable changing | The linked Int Variable (its Changed event) |
| An ending | Its event, raised by `<<raise>>` |

| To make the kit do something… | Call |
|---|---|
| Start a conversation | **Dialogue Runner → StartDialogue** (a node name) |
| A command of your own | A method in your script, added with **AddCommandHandler** (see Yarn Spinner's docs) |
| Show a screen | **UIScreen → Show** |

Your instructor can help you plan a custom script; the **[Script Reference](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Guides/Script%20Reference.md)** lists everything the kit's scripts can do.
