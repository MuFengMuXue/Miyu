## On Linux

The game should work just fine out of the box with GE-Proton.

### Bakkesmod

Psyonix is adding EAC in April the 28th, 2026. This means bakkesmod will stop working for online matches. It will only work on offline/local matches.

To use bakkesmod, follow these instructions:

1) Download Rocket League normally on Heroic and run it once
2) Download Bakkesmod installer from [the official website](https://bakkesmod.com/download.php)
3) Close the game, and run the installer in the same wine prefix as the rocket league, without creating a desktop shortcut or anything. Go to the game's settings in Heroic > Wine tab > click the "Run EXE in Prefix" button > select the installer
4) Create a `run_with_bakkesmod.bat` text file inside the game installation directory with the following content:
```
@echo off

set RL_PATH=%cd%\Binaries\Win64

echo Launching BakkesMod...
C:
cd "C:\Program Files\BakkesMod"
start BakkesMod.exe
echo BakkesMod started, starting Rocket League: %RL_PATH%
Z:
cd %RL_PATH%
Launcher.exe -noeac %*
```

Make sure this is a plain text file, that it is NOT a rich text file.

5) In Heroic launcher, go to Rocket League's settings > Advanced tab > and set the `.bat` file as the alternative EXE
6) Run the game through Heroic
7) Disable safe mode in Bakkesmod. It might complain about a dll, you can ignore that, and when it asks to inject say yes
8) To add plugins, locate the Bakkesmod folder in the same wine prefix as before and drag them like you'd do on windows. You can use the 3-dots menu > Browse Wine Prefix button to open the prefix folder

## On MacOS

Psyonix announced they will add EAC to the game in April the 28th, 2026.

### This means the game will completely stop working on MacOS since that date, there's no way to get it to work as there's no way to bypass EAC

The game provides a `No Easy Anti Cheat` launch option that disables online matches. It removes EAC but can only be used for local/offline matches. Bakkesmod should work in this mode.

Mac users will have ONLY these alternatives:
- if you have an Intel mac, you can install windows/linux on it or use a streaming service like GeForce Now
- if you have an Apple Silicon mac, in this case the only option is a streaming service (you cannot install Windows in these machines and Asahi Linux -the only linux distro that works on some M chips- is not compatible with EAC either)

<details>
  <summary>Old content, does not apply anymore since EAC is added</summary>
If you are on an Apple Silicon (M chip), the best way to run the game for free is using the Game Porting Toolkit (3.0 at the moment of writing this). If you are on an Intel chip, you can use Wine-Crossover or Wine-Staging to play it for free but there's a known issue with DXVK on Mac that will not render the name plates explained below.

If you own the commercial Crossover, you can use it with any chip and it will work fine.

### Missing name plates

This is a known issue with DXVK when using Wine-Crossover and Wine-Staging. There's not solution when using those compatibility layer, the alternatives are: the commercial Crossover if you are on an Intel chip, or either the commercial Crossover, the Game Porting Toolkit, or WineStaging (with DXMT) if you are on an Apple Silicon (M chip).

### Microphone not working

Quote from Gcenx:

> Upstream wine and the foss packages including game-porting-toolkit don’t have the required hack to gain access to the system Mic
>
> CrossOver-25 and later are able to required Mic access

So the only solution to get the microphone working is using the paid Crossover.

### Bakkesmod

#### With the paid Crossover

https://www.youtube.com/watch?v=7Y0aC72Em88

#### With Wine-Staging + DXMT

It looks like bakkesmod works now with Wine-Staging with DXMT (only available on M chips).

Steps are similar to linux steps but a tiny bit different:

1) Download Rocket League normally on Heroic and run it once
2) Download Bakkesmod installer from [the official website](https://bakkesmod.com/download.php)
3) Close the game, and run the installer in the same wine prefix as the rocket league, without creating a desktop shortcut or anything. Go to the game's settings in Heroic > Wine tab > click the "Run EXE in Prefix" button > select the installer
4) Create a `run_with_bakkesmod.bat` text file inside the game installation directory with the following content:

```
@echo off

set RL_PATH=%cd%\Binaries\Win64

echo Launching BakkesMod...
C:
cd "C:\Program Files\BakkesMod"
start BakkesMod.exe
echo BakkesMod started, starting Rocket League: %RL_PATH%
Z:
cd %RL_PATH%
Launcher.exe -noeac %*
```

Make sure this is a plain text file, that it is NOT a rich text file.

5) In Heroic launcher, go to Rocket League's settings > Advanced tab > and set the `.bat` file as the alternative EXE
6) Run the game through Heroic
7) Disable safe mode in Bakkesmod. It might complain about a dll, you can ignore that, and when it asks to inject say yes
8) To add plugins, locate the Bakkesmod folder in the same wine prefix as before and drag them like you'd do on windows. You can use the 3-dots menu > Browse Wine Prefix button to open the prefix folder

#### With Game-Porting-Toolkit

There are no reports of it working, if you get it working please share steps on Discord. Some known possible issues:
- GPTK reports windows 7, so the windows 7 executable of bakkesmod would be needed https://bakkesmod.com/windows7.php
- GPTK3.0 fails to install the Visual C++ Runtime, GPTK3.0beta5 might be needed (even with GPTK3.0beta5, the injector fails to inject the mod complaining about vcrun possibly missing)

### Can't ALT-TAB out of the game

You can try changing the video mode to either borderless or windowed. Seems to not be an issue with the paid Crossover.

### Stuck in Press Any Key screen when game opens

This usually means the game is waiting for the user to accept the EULA terms.

A browser windows should pop-up outside of the game for the user to read and accept the terms.

If this window does not show up, try some of these possible soliutions:
- A user reported that configuring Whisky make the browser window pop-up (whisky is not recommended as it's abandoned, but can be used just to accept the terms and then change back to GPTK/Wine-Staging/Crossover)
- Change the default web browser of the OS: either install a new browser if you currently have Safari as the default, or reconfigure Safari as the default if you have an alternative browser set
- The last option would be to run the game in another machine with linux/windows and accept the terms there

### Anticheat

Psyonix announced they will add EAC to the game in April 2026. **This means the game will completely stop working on MacOS for online matches, there's no way to get it to work as there's no way to bypass EAC.**

Mac users will have ONLY these alternatives:
- if you have an Intel mac, you can install windows on it or use a streaming service like GeForce Now
- if you have an Apple Silicon mac, you cannot install windows, in this case the only option is a streaming service
