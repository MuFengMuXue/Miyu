# Installing Visual C Runtime

This page explains different ways to solve the `"The following components are required to run this program: Microsoft Visual C++ Runtime"` error message.

The solution is to install the C++ Runtime, and there are multiple ways of doing it depending on the platform and tools used.

## Linux

### Using Winetricks

This is the simplest option for most users. Winetricks is automatically downloaded and the steps to install the Visual C++ Runtime are:

- Open the game's settings in Heroic
- Make sure you are in the Wine tab
- Scroll down and click the `winetricks` button, a new dialog should show up
- In the text field, type `vcrun2022`. After a moment a list should show up with an `Install` button
- Click the `Install` button and wait until it's done

> Note that, in general, installing the latest `vcrun` covers most use cases since it includes older ones. If, for any reason, you need to install an older version, just type `vcrun` instead and install the one you want.

### Manual installation

Sometimes, the installation using winetricks fails. In those cases, the Visual C++ Runtime can be installed manually:

- Open https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170 in the browser
- Download both the `x86` and `x64` installers listed under `Latest Microsoft Visual C++ Redistributable Version`
- Open the game's settings in Heroic
- Make sure you are in the Wine tab
- Scroll down and click the `Run EXE in Prefix` button, a file picker should show up
- Select one of the installer and complete the process
- Repeat for the other installer

## Mac

### With Crossover (the paid version, not the free Wine-Crossover)

When using Crossover, winetricks cannot be used. In this case you'll have to use Crossover's UI:

- Open Crossover
- Select the corresponding Bottle on the left sidebar
- Click the `Install application into bottle` button in the right sidebar
- Search for Visual C++ and install the package (Visual C++ 2015-2022 at the time of writing this)

### With Whisky


### With wine-crossover / wine-staging / wineskin / gptk (or other wine)

For these tools, the same options that are available for Linux can be used: with winetricks or with the `Run EXE in Prefix` option.

Note that, to use the `winetricks` options, you have to make sure you have the correct dependencies of winetricks installed, check https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Using-Heroic-on-a-Mac-computer#winetricks-setup

Once you have the winetricks dependencies installed, follow these steps to install `vcrun2022` https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Installing-Visual-C---Runtime#using-winetricks

IMPORTANT: Installing the Visual C++ Runtime with the GPTK3.0 is broken, use version 3.0-1 or newer.

## Windows

In general, Heroic prompts to install the latest C++ Runtime at boot if it detects it's not installed, but, if needed, the files can be downloaded and installed manually:

- Open https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170 in the browser
- Download both the `x86` and `x64` installers listed under `Latest Microsoft Visual C++ Redistributable Version`
- Install both
