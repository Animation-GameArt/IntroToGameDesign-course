---
title: "Grid Puzzle Kit"
course: GAME 1303
status: draft
course_version: 0.16.0
unity: 6000.3.10f1
tags:
  - game1303
  - kit
---

# Grid Puzzle Kit

The Grid Puzzle Kit is a starting point for puzzles played on a grid, one step at a time. Its sample is a Sokoban game: push every box onto a target. Every move can be undone, and the level can be restarted at any time.

The real work in a puzzle game is designing levels, not writing code. The kit handles the rules, undo, restart and the list of levels, so your time goes into one rule of your own and ten to fifteen levels that teach it.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Movement locked to a grid, one cell per press | Free movement or physics |
| Pushable boxes, solid rocks, items to collect | Pulling, sliding on ice, or falling (a custom rule) |
| Goals for boxes, coloured goals for coloured boxes, exits for the player | Switches and doors that open (a custom rule) |
| Several player pieces moved at once | Turn-based enemies |
| Undo every move, restart, move counter | A solver or hints |
| A list of levels that unlock in order, saved between sessions | Level editors for players |

If your one rule is in the right-hand column, it's your agreed custom script.

## Install the kit

1. Download the Grid Puzzle Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/GridPuzzle/Sample/Scenes`, add `Puzzle_Menu`, `Puzzle_Select`, then `Puzzle_01` to `Puzzle_08`, in that order.
4. Open `Puzzle_Menu` and press **Play**.

| Action | Keyboard | Gamepad |
|---|---|---|
| Move one cell (hold to repeat) | **WASD** or arrow keys | Left stick or D-pad |
| Undo | **Z** or **Backspace** | West button |
| Restart the level | **R** | North button |
| Pause | **Esc** | **Start** |

## What's in the sample

| Prefab or asset | What it is | Settings worth changing |
|---|---|---|
| `Player` | Grid Piece, role Player | **Move Time** (how fast it slides) |
| `Box` | Grid Piece, role Pushable | **Kind** |
| `Red Box`, `Red Target` | A box and a target with Kind `red`: only the red box fills it | **Kind** |
| `Rock` | Grid Piece, role Solid: never moves | |
| `Gem` | Grid Piece, role Item: picked up by walking onto it | |
| `Target` | Grid Goal, filled by any Pushable | **Filled Color** |
| `Exit` | Grid Goal, filled by the Player | |
| `Puzzle Systems` | Board, input, HUD, solved screen, pause | **Max Pushed In A Row**, **Need All Items** on the Grid Board |
| `Puzzle Levels` | The Level List: the eight level scenes, in order | **Unlock All** for testing |

## How the sample fits together

**The board.** Each level has one **Grid Board**. Walls are painted on a Tilemap; any cell with a tile is a wall. Pieces and goals snap to the middle of their cell when the level starts. Nothing uses physics: the board works out every move.

**Moving and pushing.** **Grid Player Input** turns each press into a step. The board checks the next cell: a wall stops the move; a Pushable piece moves along if the cell behind it is free; a Solid piece stops it. With **Max Pushed In A Row** at 1, as in Sokoban, two boxes in a row can't be pushed.

**Undo and restart.** Before every move the board remembers where every piece was. Undo puts them back, one move at a time; Restart puts everything back to the start.

**Solving.** After each move, every **Grid Goal** checks whether a matching piece is on it, and changes colour. When all goals are filled (and every gem is collected, if **Need All Items** is ticked), the level is solved: the board marks it solved in the Level List, and the solved screen appears.

**Levels.** The **Level List** asset holds the level scenes in order. Solving a level unlocks the next. The level select screen shows every level, greys out locked ones, and colours solved ones. Progress is saved between sessions.

## Start your own game

1. **Make a Level List:** in `Assets/_Game`, **Create → Collin Game → Grid Puzzle Kit → Level List**. Give it a Save Name.
2. **Make your first level:** open `Puzzle_01`, **File → Save As…** `Assets/_Game/Scenes/Level_01`.
3. On `Puzzle Systems` → `Board`, set **Level List** to your list.
4. Repaint the walls and move the pieces and goals. Press **Play** and solve it.
5. Add the scene's name to your Level List and to the Scene List.
6. For the next level, Save As again, and redesign.
7. Copy the sample's menu and level select scenes, and set their Puzzle Level Loader's **Level List** to yours.

### Designing levels

- **One idea per level.** Each level should teach or test one thing. Write it down before you build: "boxes in corners can't be moved".
- **Order teaches.** Early levels show the rule safely; later ones combine it with others.
- **Small is hard.** A 6 × 6 room with three boxes can be harder than a big one.
- **Playtest early.** Watch someone else play without helping. Where they get stuck is where the level is teaching, or confusing.
- **Count the moves.** Solve each level yourself and note the moves. If it's under 10, it may be too easy; over 100, too fiddly.

## Recipes

**Push chains.** Set the board's **Max Pushed In A Row** to `3`: the player can push up to three boxes in a line.

**Coloured boxes.** Give a box and a target the same **Kind**, such as `blue`. Only that box fills that target.

**Reach the exit.** A Grid Goal with **Filled By: Player**, and no box targets: the level is solved when the player stands on it.

**Collect everything.** Gems are Items. Tick **Need All Items** on the board: the level is solved when every gem is collected (and any goals filled).

**Two players at once.** Put two `Player` pieces in a level. Both move together, which makes a different kind of puzzle.

**A helper that can't push.** Untick **Can Push** on a second Player piece: it moves with the first player but is blocked by boxes.

**Sounds.** Each Grid Piece has **On Moved**; the board has **On Blocked** (a bump) and **On Undo**; each Goal has **On Filled**.

## If something goes wrong

| What you see | What to do |
|---|---|
| The player doesn't move | The scene needs a **Grid Board** and **Grid Player Input**, and the player's **Role** must be Player |
| The player walks through walls | The Grid Board's **Walls** must be the Tilemap the walls are painted on |
| Pieces sit between cells | They snap when the level starts. Check they're placed inside the right cell, not on a line |
| A box won't move | The cell behind it is a wall, a rock or another box (with Max Pushed In A Row at 1) |
| The level is never solved | Every Grid Goal must be filled. Select each target in Play mode: filled ones change colour. Check Kinds match |
| The level is solved straight away | A box already sits on a target. Move it off |
| The level select is empty | The Puzzle Level Loader needs a **Level List** with scene names |
| The next level doesn't load | The scene must be in the Level List and in the Scene List, spelled the same |
| A solved level is locked again | Progress is saved by the Level List's **Save Name**: keep it the same |
