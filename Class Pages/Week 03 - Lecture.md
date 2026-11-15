---
title: "[Lecture] Week 3"
course: GAME 1303
week: 3
status: draft
tags:
  - game1303
  - lecture-page
---

# Week 3 — Pitch Day · Ex 02: Events

**Exercise:** Ex 02 — Events. Coins add to a score variable, a text shows it, and a key raises an event that opens a door.

**Also due:** the pitch, posted to the Canvas Discussion by 11:59 PM the night before class and presented live. Approval, with any conditions, comes out of today.

## Lecture topics, expanded

**Pitch Day.** Each student presents from their Discussion post. Keep feedback to two things: is the core loop clear, and does the scope fit eight weeks in a supported genre. Approve, approve with conditions, or ask for a revision, and say which out loud so the student knows where they stand. The custom scripts and tutorials for each game are prepared from these pitches over the next two weeks, so a clear pitch has a practical payoff.

**GameObjects, components and prefabs.** A GameObject is an empty container. Everything it does comes from the components on it: a Sprite Renderer to be seen, a collider to be touched, a Rigidbody to move under physics. Build the ball from Ex 02 live, one component at a time, and show what each adds. A **prefab** is a GameObject saved as a reusable template. This is composition, and it's how nearly everything in the course is built.

**The script lifecycle and the Console.** Unity calls a script's methods at set moments: `Awake` and `Start` once at the beginning, `Update` every frame, `FixedUpdate` on the physics clock. Students don't write much code yet, but they need to read errors. Show a real one: read the first line, find the object and script it names, and double-click to jump to it. The course scripts write plain-language messages for common mistakes, which Ex 01's experiments already showed.

**ScriptableObjects: variables and event channels.** A ScriptableObject is data saved as an asset in the Project window, outside any scene. The course uses two kinds. A **variable** holds one shared value, such as the score. An **event channel** announces a moment, such as "key collected." The coin adds to the score without knowing a text exists. The key raises its event without knowing there's a door. Contrast this with objects that hold direct references to each other, which break as soon as one is removed or renamed.

## Connecting it forward

Every later exercise leans on today's two assets. The score variable from Ex 02 is the same one the HUD shows in Ex 06, and event channels carry the player's death, the level's end and the pause state. The collectible written today is collected by a rolling ball; next week the same collectible, unchanged, is collected by a player character.
