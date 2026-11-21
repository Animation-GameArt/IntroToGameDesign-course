---
title: "Visual Novel Kit"
course: GAME 1303
status: draft
course_version: 0.20.0
unity: 6000.3.10f1
yarn_spinner: 3.3.2
tags:
  - game1303
  - kit
---

# Visual Novel Kit

The Visual Novel Kit is a starting point for visual novels and dating sims: stories told in lines of dialogue over pictures, where the player's choices change what happens. Examples: Doki Doki Literature Club, Ace Attorney (its story scenes), Monster Prom, Florence.

You write the story in **Yarn Spinner**, a scripting language made for game dialogue. It reads like a screenplay. The kit puts the story on screen: the backgrounds, the characters, the dialogue box, the choices, and, for a dating sim, a meter for how each character feels about the player.

The sample, *Lantern Festival*, is a short story with two characters, Ren and Mika, and three endings. What you say decides who you watch the lanterns with at midnight.

## What the kit covers

| The kit does this | The kit doesn't do this |
|---|---|
| Lines typed out, with the speaker's name in their color | Voice acting (Yarn Spinner can, but the kit doesn't set it up) |
| Choices, including ones locked until a condition is met | Timed choices |
| A background, and up to three characters on stage | Animated characters, or more than three at once |
| Moods: a different portrait per mood | Lip sync |
| Relationship meters for a dating sim | Calendars and schedules (write them in Yarn as choices) |
| Sounds, music, endings and scene changes from the script | A history of past lines, auto-play or skip |
| Using the dialogue in any other game, such as talking to people in a top-down game | Saving in the middle of the story |

If your pitch needs something in the right-hand column, it has to be one of your agreed custom scripts, or it has to be cut. Most of a visual novel's work is the writing and the art; plan for both.

## Install the kit

Yarn Spinner is already in the course project. You don't need to install anything else.

1. Download the Visual Novel Kit package from the course project's **Releases** page.
2. With your project open, double-click the package and click **Import**.
3. Open **File → Build Profiles → Open Scene List**. From `Assets/_Course/Kits/VisualNovel/Sample/Scenes`, add `Story_Menu` and `Story_Game`, next to each other, in that order.
4. Open `Story_Menu` and press **Play**.

Click, tap, or press Space, Enter or E to show the whole line, and again for the next one. Click or tap a choice, or choose with the arrow keys and Enter. **Esc** pauses.

**About the message "This package has no signature."** Unity shows it for Yarn Spinner because it comes from OpenUPM, not from Unity. It's expected, and safe to ignore.

## Writing in Yarn

A Yarn script is a text file (`.yarn`) made of **nodes**. Each node has a title, then its lines between `---` and `===`:

```
title: Start
---
<<background Square>>
It's the night of the Lantern Festival.
<<show Ren left>>
Ren: Oh! Sorry, I almost walked right into you.
-> "No problem."
    <<set $ren = $ren + 1>>
    Ren: You're nice. I like you already.
-> "Watch where you're going."
    Ren: Yikes. Okay.
<<jump Stalls>>
===
```

- **Lines.** `Ren: Hello!` is Ren speaking. A line with no name is narration.
- **Choices.** Lines starting with `->` are choices. The indented lines under each happen only if it's chosen.
- **Variables.** `<<declare $ren = 0>>` creates one; `<<set $ren = $ren + 1>>` changes it. `<<if $ren >= 3>>` … `<<endif>>` checks it.
- **Locked choices.** `-> Ren <<if $ren >= 3>>` is shown greyed out until the condition is true.
- **Jumps.** `<<jump Stalls>>` goes to the node titled `Stalls`.

Yarn Spinner's own documentation (**docs.yarnspinner.dev**) covers the language in full.

### The kit's commands

The **Visual Novel Stage** adds these commands. Names are the ones in its lists.

| Command | What it does |
|---|---|
| `<<background Bridge>>` | Changes the background |
| `<<show Ren>>`, `<<show Ren happy>>`, `<<show Ren left>>`, `<<show Ren happy right>>` | Shows a character, with an optional mood and position (`left`, `center` or `right`) |
| `<<mood Ren sad>>` | Changes the character's portrait |
| `<<hide Ren>>`, `<<hide_all>>` | Takes characters off the stage |
| `<<sound Door>>`, `<<music Theme>>`, `<<stop_music>>` | Plays a sound, plays or stops music |
| `<<raise GoodEnding>>` | Raises a Void Event Channel, such as to show an ending screen |
| `<<scene Credits>>` | Loads a scene |
| `<<wait 2>>` | Waits two seconds (built into Yarn Spinner) |

## How it works

- The **Dialogue Runner** (from Yarn Spinner) runs the script, starting at its **Start Node**.
- The **UI Dialogue Presenter** shows each line and each set of choices on the kit's `VisualNovel` screen.
- The **Visual Novel Stage** shows the background and characters, and runs the commands above. It also darkens the characters who aren't speaking.
- **Characters** (assets) hold a name, a name color and a portrait per mood.
- For a dating sim, the **Yarn Variable Link** copies Yarn variables, such as `$ren`, into course **Int Variables**. The **UI Relationship Meters** draw them as bars, and anything else in the course scripts can use them too.
- Endings are `<<raise>>` commands, each shown by an ending screen.

## What's in the sample

| Asset | What it is | Worth changing |
|---|---|---|
| `Story/LanternFestival.yarn` | The story | Everything |
| `Ren`, `Mika` | Characters | **Name Color**, **Portraits** |
| `RenAffection`, `MikaAffection` | Int Variables, linked to `$ren` and `$mika` | — |
| `RenEnding`, `MikaEnding`, `AloneEnding` | Void Event Channels, one per ending | — |
| `Story Systems` | The Dialogue Runner, the screen, the stage and the ending screens | **Backgrounds**, **Letters Per Second** |

The sample's art is a placeholder: the portraits are tiny pixel characters and the backgrounds are plain colors. Your game's art is up to you.

## Start your own game

**[Visual Novel Kit — Build Your Game](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Kit%20Guides/Visual%20Novel%20Kit%20-%20Build%20Your%20Game.md)** takes you from the decisions table on page 10 of your ten-pager to your finished game, step by step, with checks for First Playable, Alpha and Beta. The steps below are the short version.

1. Plan your story on paper first: the scenes, the choices, and where they lead. Keep it small: three scenes and two or three endings is plenty for eight weeks.
2. In `Assets/_Game/Story`, create a Yarn script (**Create → Yarn Spinner → Yarn Script**) and a Yarn Project (**Create → Yarn Spinner → Yarn Project**). A Yarn Project includes every Yarn script in its folder and the folders inside it.
3. Create a **Character** for each character (**Create → Collin Game → Visual Novel Kit → Character**), with their name exactly as you write it in the script.
4. Open `Story_Game`, **File → Save As…** into `Assets/_Game/Scenes`, and on `Story Systems`:
   - **Dialogue Runner**: your Yarn Project, and your first node in **Start Node**.
   - **Visual Novel Stage**: your characters, backgrounds, sounds and endings.
5. Press **Play**, and play every path. Then rewrite one scene and play again.

### Writing tips

- **Every choice should matter, or feel like it does.** If both choices lead to the same line, change at least the next line.
- **Show feelings, then numbers.** Players react to Ren's line more than to a meter moving. Use moods.
- **Short lines.** Two lines of text at most per box; split long speeches.
- **Read it aloud.** If it sounds stiff spoken, it reads stiff.

## Recipes

**A dating sim.** Declare a variable per character, change it in choices, link each to an Int Variable with **Yarn Variable Link**, and add **UI Relationship Meters**. Lock the best ending behind a condition, such as `-> Ren <<if $ren >= 5>>`.

**Hide the meters.** Leave UI Relationship Meters off; the variables still work. Many dating sims never show the numbers.

**Characters talking in another game.** Add a Dialogue Runner and the `VisualNovel` screen with only the UI Dialogue Presenter (no stage). In a top-down game, an **Interactable 2D**'s **On Used** can call **DialogueRunner → StartDialogue** with a node name. **Stop Player While Talking** keeps the player still.

**Faster or slower text.** Change **Letters Per Second**; `0` shows each line at once.

**Locked choices hidden instead of greyed.** Untick **Show Unavailable Choices**.

**A blip sound per line.** Play a Sound Effect from the presenter's **On Line Started**.

## If something goes wrong

| What you see | What to do |
|---|---|
| Nothing happens at Play | The Dialogue Runner needs your Yarn Project, and **Auto Start** ticked (or something that calls **StartDialogue**) |
| "No node named …" | The Start Node, or a `<<jump>>`, doesn't match a node's title exactly |
| Lines don't show | Drag the UI Dialogue Presenter into the Dialogue Runner's **Dialogue Presenters** list |
| Yarn errors in the Console | Click the Yarn Project to see them; a missing `===` or a misspelled variable is the usual cause |
| "No character called …" | Add the Character to the stage's **Characters**, with the name exactly as in the script |
| A character doesn't appear | Give the Character at least one portrait |
| A meter doesn't move | The Yarn Variable Link's name needs the `$`, and the variable must be `<<declare>>`d as a number |
| An ending doesn't show | `<<raise Name>>` needs the same Name in the stage's **Events**, and a Void Event Listener that shows the screen |
| The player walks around during dialogue | Tick **Stop Player While Talking** |
