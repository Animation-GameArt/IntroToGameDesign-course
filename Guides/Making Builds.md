---
title: "Making Builds"
course: GAME 1303
status: draft
unity: 6000.3.10f1
tags:
  - game1303
  - guide
---

# Making Builds

How to turn your project into a game people can play without Unity: a **Web** build that runs in a browser, and **Windows** and **macOS** builds they download. Come back to this page at every milestone.

You make your first build in **Exercise 08**. Every milestone from First Playable on is a link to your itch.io page with a build on it.

| Build | Who can play it | Best for |
|---|---|---|
| **Web** | Anyone with a browser, straight from your itch.io page | Every milestone. It's the easiest for classmates and playtesters |
| **Windows** | People on Windows who download it | Games that run slowly in a browser, or need full-screen performance |
| **macOS** | People on Macs who download it | The same, for Mac players |

Make a Web build for every milestone. Add a Windows or macOS build if your game needs it, or for Gold.

## Before any build

1. **No red errors in the Console.** A project with errors can't be built.
2. Open **File → Build Profiles → Open Scene List**. Every scene in your game is there, **your menu scene is first**, and the rest are in play order. Untick or remove exercise and kit sample scenes.
3. Click **Player Settings** (bottom of the Build Profiles window). Set **Company Name** to your name and **Product Name** to your game's title. Set a **Default Icon** if you have one.
4. Play the game once in the Editor from the menu scene, start to finish.

## Build, or Build And Run?

The Build Profiles window has two buttons:

| Button | What it does | Use it when |
|---|---|---|
| **Build** | Makes the build in a folder you choose, and stops | You'll upload it, or zip it to send |
| **Build And Run** | Makes the build, then starts it so you can play it at once | You want to check the build right away. Use it most of the time |

For a **Web** build, use **Build And Run** to test it. A Web build can't be opened by double-clicking its `index.html`: browsers block it. Build And Run starts a small local web server so it plays properly. On itch.io it works either way.

**Where to save builds.** Make a `Builds` folder next to your `Assets` folder, **not inside it**, with a folder per platform: `Builds/Web`, `Builds/Windows`, `Builds/macOS`. Choose the right one each time. Unity replaces what's in the folder, so a new build overwrites the old one. The course project's `.gitignore` already leaves `Builds` out of Git.

## Web build

1. **File → Build Profiles**. Under **Platforms**, select **Web**.
   - If it says the module isn't installed: in **Unity Hub → Installs**, click the ⚙ next to Unity 6000.3.10f1 → **Add modules** → **Web Build Support**. Restart Unity.
2. Click **Switch Platform** and wait. The first switch takes a few minutes.
3. **Player Settings → Publishing Settings**: tick **Decompression Fallback**. (Without it, itch.io can show a blank page.)
4. Click **Build And Run**, and choose `Builds/Web`. When it finishes, the game opens in your browser. Play it start to finish.

### Upload a Web build to itch.io

1. Open `Builds/Web`, select **everything inside it** (`index.html` and the folders next to it), and compress it into a ZIP. `index.html` must be at the top of the ZIP, not inside another folder.
2. On your itch.io page (**Edit game**):
   - **Kind of project:** HTML.
   - **Uploads:** upload the ZIP, and tick **This file will be played in the browser**. Delete the previous build's upload, so only the newest is played.
   - **Embed options:** viewport `960` × `540`; tick **Fullscreen button**.
3. **Save**, then **View page**, and play it there.

### Things that work differently in a browser

- **Quit does nothing.** A browser tab can't close itself. The course's Settings screen hides Full Screen in Web builds; hide your Quit button too, or leave it, knowing it won't do anything.
- **The mouse pointer can only be locked after a click.** In a 3D game with **Cursor Lock 3D**, the player clicks the game once to start mouse look.
- **Saving** uses the browser's storage. It's kept per browser, and lost if the player clears their browsing data.
- **Performance.** Web builds are slower than desktop builds. If your game stutters in the browser but not in the Editor, see **The Profiler** topic, or add a Windows build.

## Windows build

You can make a Windows build from a Windows computer without installing anything extra. From a Mac, add **Windows Build Support (Mono)** in **Unity Hub → Installs → Add modules**.

1. **File → Build Profiles**. Under **Platforms**, select **Windows**. Click **Switch Platform**.
2. Leave **Architecture** on **Intel 64-bit**.
3. **Player Settings → Resolution and Presentation**: **Fullscreen Mode** **Fullscreen Window** is a good default (the Settings screen lets players change it). Tick **Resizable Window**.
4. Click **Build And Run**, and choose `Builds/Windows`. The game starts when it's built.

The build is a folder of files: `YourGame.exe`, a `YourGame_Data` folder, `UnityPlayer.dll` and a few more. **All of them are needed.** Sending only the `.exe` doesn't work.

### Upload a Windows build to itch.io

1. Compress the **whole contents** of `Builds/Windows` into a ZIP named like `YourGame-Windows.zip`.
2. On your itch.io page (**Edit game**) → **Uploads**: upload the ZIP, and tick **Windows** under the platforms. Don't tick "played in the browser".
3. If the page also has a Web build, keep **Kind of project** on **HTML**: players can play in the browser or download.
4. Download it from the page and run it, to check.

Windows may show **"Windows protected your PC"** the first time, because the game isn't signed. Click **More info → Run anyway**. Tell your playtesters to expect it.

## macOS build

You can make a macOS build from a Mac without installing anything extra. From Windows, add **Mac Build Support (Mono)** in **Unity Hub → Installs → Add modules**.

1. **File → Build Profiles**. Under **Platforms**, select **macOS**. Click **Switch Platform**.
2. **Architecture:** **Intel 64-bit + Apple silicon**, so it runs on every Mac.
3. The same **Resolution and Presentation** settings as Windows.
4. Click **Build And Run**, and choose `Builds/macOS`. The build is one `YourGame.app`.

### Upload a macOS build to itch.io

1. Right-click `YourGame.app` → **Compress** to make a ZIP. (Built on Windows? Zip the `.app` folder the same way.)
2. On itch.io → **Uploads**: upload the ZIP and tick **macOS**.

macOS blocks games from unknown developers the first time. The player double-clicks it, clicks **Done** on the warning, then opens **System Settings → Privacy & Security**, scrolls down, and clicks **Open Anyway** next to the game's name. Tell your playtesters to expect it. A Mac build made on Windows may not open at all; build on a Mac if you can, or offer the Web build.

## Development builds

**Development Build** (in Build Profiles) makes a build that shows errors on screen and can be connected to the Profiler. It's useful for chasing a bug that only happens in the build. **Untick it for every milestone build**: it's slower and shows a "Development Build" label.

## Before you submit a milestone

- [ ] The build starts at your menu.
- [ ] You played it start to finish **in the build**, not the Editor.
- [ ] On itch.io, the newest build is the one that plays (old uploads deleted).
- [ ] You opened the page while logged out, or in a private window, to see it as a player would. For a private draft, use the page's **secret URL** (Edit game → **Visibility & access**).

## If something goes wrong

| What you see | What to do |
|---|---|
| Build fails | Read the **first** red error in the Console, fix it, and build again. A project with errors can't be built |
| "Module not installed" | Add the platform's Build Support in **Unity Hub → Installs → Add modules**, and restart Unity |
| Starts on the wrong scene | Drag your menu scene to the top of the Scene List |
| A level is missing | Add its scene to the Scene List |
| Next Level goes to the wrong scene | The Scene List's order is the level order |
| Text is tiny or cut off | Check the UI at the build's size in the Game view (the resolution menu at its top); every UI Document uses `CoursePanelSettings` |
| Web: blank page on itch.io | Tick **Decompression Fallback**, build again, and upload again |
| Web: "can't find index.html" | The ZIP has an extra folder level. Zip the files inside `Builds/Web`, not the folder |
| Web: double-clicking `index.html` shows an error | Expected. Use **Build And Run**, or upload it |
| Windows: "missing UnityPlayer.dll" | The whole build folder wasn't shared. Zip everything in `Builds/Windows` |
| Windows: "Windows protected your PC" | **More info → Run anyway** |
| macOS: "can't be opened" | **System Settings → Privacy & Security → Open Anyway** |
| Something works in the Editor but not the build | Note exactly what. Make a **Development Build** to see its errors on screen |

## Related

- [Ex 08 — Save & Build](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Exercises/Ex08%20-%20Save%20%26%20Build.md): your first Web build and itch.io page
- [Making a Build](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Making%20a%20Build.md) and [Publishing on itch.io](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Publishing%20on%20itch.io.md)
- [Final Build Checks](https://github.com/Animation-GameArt/IntroToGameDesign-course/blob/main/Topics/Final%20Build%20Checks.md): before Gold
- Unity Manual: [Create and manage build profiles](https://docs.unity3d.com/Manual/create-build-profile.html), [Web](https://docs.unity3d.com/Manual/webgl.html)
