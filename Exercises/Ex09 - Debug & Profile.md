---
title: "Exercise 09 — Debug & Profile"
course: GAME 1303
week: 10
status: draft
course_version: 0.10.0
unity: 6000.3.10f1
tags:
  - game1303
  - exercise
---

# Exercise 09 — Debug & Profile

**Week 10 · in your own game · submitted at the end of class**

In this exercise you start a bug list, find and fix one real bug, take one reading with the Profiler, and sort your bugs into must fix, should fix and won't fix.

## What you'll learn

- How to reproduce a bug and write it down so it can be fixed
- How to use the Console, a log message and a breakpoint
- How to read the Profiler
- How to triage

## Part 1 — Start a bug list

Make a table in a document, a spreadsheet or your task board. Add every bug you already know about.

| # | Steps to make it happen | Expected | What happened | Console message | Priority |
|---|---|---|---|---|---|
| 1 | | | | | |

**Steps** are exact: "Jump onto the moving platform while it turns around," not "platforms are buggy."

## Part 2 — Reproduce one bug

1. Pick one bug from your list.
2. Follow your steps and make it happen.
3. Make it happen a second time. If you can't, add more detail to the steps until you can.

## Part 3 — Find out why

Try these in order. Stop when you understand the bug.

**The Console**

1. Clear the Console, then reproduce the bug.
2. Read the **first** red or yellow message. Click it once to highlight the object it names; double-click it to open the script line.
3. If it's a course message, it says what's wrong and how to fix it.

**The Inspector, during Play**

1. Reproduce the bug while watching the object in the Inspector.
2. Watch the values change. For a variable asset, select it and watch **Current Value**.

**A breakpoint** (for your own scripts)

1. Open your script in your code editor. Click in the margin next to a line to set a breakpoint (a red dot).
2. Attach the editor to Unity: in Visual Studio, **Attach to Unity**; in VS Code, the **Attach to Unity** debug configuration.
3. If Unity asks to switch to **Debug mode**, allow it. The bug icon in the bottom-right of the Editor shows the mode.
4. Press **Play** and reproduce the bug. Unity stops at your line. Hover over names to see their values.
5. Stop debugging and remove the breakpoint when you're done.

## Part 4 — Fix it

1. Change **one** thing.
2. Follow your steps again. The bug shouldn't happen.
3. Try once more to be sure, then mark it fixed on your list.

## Part 5 — A Profiler reading

1. Open **Window → Analysis → Profiler**.
2. Press **Play**, then play the busiest part of your game for about 20 seconds: the most enemies, the most effects.
3. Stop the game. In the Profiler's **CPU Usage** graph, click the tallest spike.
4. In the panel below, look at the top lines. Note the total time for that frame in milliseconds, and the name at the top of the list.
5. Take a screenshot.

About 16 milliseconds a frame is smooth. If your spikes are far above that, look at what the top line names: a spawner with no limit is a common cause. Change one thing and take a second reading.

## Part 6 — Your design decision: triage

Give every bug on your list a priority.

| Priority | Means |
|---|---|
| **Must fix** | Crashes, getting stuck, losing progress, anything that stops play |
| **Should fix** | Noticeable, but the game can be played and finished |
| **Won't fix** | Rare or minor, and the time is better spent elsewhere |

Choose one **won't fix** and write one sentence defending it.

## Check-off

Submit in Canvas, by the end of class:

- [ ] Your bug list, with at least five bugs written as steps.
- [ ] One bug fixed, with a sentence on what caused it and what you changed.
- [ ] Your Profiler screenshot, with the frame time and the top line noted.
- [ ] Every bug triaged, and one "won't fix" defended.

## If something goes wrong

| What you see | What to do |
|---|---|
| The breakpoint is hollow and never stops | The code editor isn't attached, or Unity isn't in Debug mode |
| The Profiler graph is empty | Press Play with the Profiler window open, or click **Record** |
| You can't make the bug happen again | Add detail to the steps: where you were, what you pressed, in what order |

## Related topics

- [Finding and Fixing Bugs](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Finding%20and%20Fixing%20Bugs.md)
- [The Profiler](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/The%20Profiler.md)
- [Bug Triage and Cutting Scope](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Bug%20Triage%20and%20Cutting%20Scope.md)
- [Scripts and the Console](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Scripts%20and%20the%20Console.md)
