# Unreal Engine 4

Unreal Engine 4 was the 4th major version of the videogame engine created by Epic Games.

The content of this article was originally written on Unreal Engine wiki and adapted specifically for Arch Linux.

## Prerequisites
See Recommended Hardware.

## Gain access to the source code
The Unreal Engine source code is in a private GitHub repository requiring free registration with the developer (Epic Games) for access.

To gain access, login or register at Epic Games Accounts and provide an accessible GitHub username at the bottom of the Epic Games 'Linked accounts' page. GitHub will then send an email inviting you to join the @EpicGames organization on GitHub, providing access to the private repository.

## Clone
Since the repository is private, you should set up an SSH key so your GitHub account is used to clone the source.

It is faster to clone only the desired branch:

 $ git clone git@github.com:EpicGames/UnrealEngine.git --branch release --single-branch

## Compilation
You can compile manually from a downloaded GitHub release or install from AUR.

## Manually
You can get the most recent releases on GitHub as ZIPs.

Setup:

 $ ./Setup.sh

Generate project files:

 $ ./GenerateProjectFiles.sh

Then compile:

 $ make -j$(nproc)

This will compile the Unreal Engine and the Unreal Editor.

## From the AUR
Unreal Engine 4 is available in the AUR as the  package. You might have to fix permissions for UE4 to precompile shaders on first launch:

 # chmod -R a+rwX /opt/unreal-engine/Engine

For a smaller download you can use .zip releases as a source for PKGBUILD. Note that this link will not work unless you first follow the steps outlined above.

## Compilation time
The compilation can take from 20 minutes up to a few hours depending on your machine.
As an example on a AMD FX-8350 (8 threads) with 16GB DDR3 on an SSD and Clang 3.8.1 takes roughly 40 minutes.
(This does not include shaders compilation)

## Troubleshooting
## Compilation problems
If the compilation fails you should try building the Editor using the Debug profile$ make UE4Editor-Linux-Debug

However, this might have some performance impact.

Another approach would be to use different clang version (e.g. 3.8 or 4.0)

## Runtime problems
If the editor does not start from the menu, or something does not work right, start it in a console and check the output for errors.

 $ /opt/unreal-engine/Engine/Binaries/Linux/UE4Editor

## C++ code project problems
After creating a code project, the new project opens in a text editor instead of in UE4Editor as it should.  After re-launching the editor, the new project shows up and can be opened, but on the first run, it takes a half-hour or so to compile, and since this happens in the background (no GUI) it might not seem to be doing anything.  The CPU usage should show that it is still compiling, and you may want to launch the editor from a console to see progress.

If while trying to open the project in UE for the first time, you get a message about editor modules being out of date, you need to build the  target in your IDE. Do not abort this build, or you will brick UE4 and will need to reinstall . Afterward, it will open and ask you to rebuild the project class, after which you can actually start working on your new project.

Note that completing both of these rebuilds can very well take over an hour, depending on your system specs.

## Engine modules are out of date, and cannot be compiled while the engine is running. Please build through your IDE
First, in your source folder in your project, check that {nameofproject}.Target.cs and {nameofproject}Editor.Target.cs has "DefaultBuildSettings = BuildSettingsVersion.V2;" in the section base(Target) { ... }
If it does not work, check the file Engine/Source/Developer/DesktopPlatform/Private/DesktopPlatformBase.cpp in your Unreal Engine source code, look for the line `Arguments += " -Progress -NoEngineChanges -NoHotReloadFromIDE";` and remove the two last options : `Arguments += " -Progress";`

* Re-compile Unreal Engine
* Launch your project and accept the rebuild

## Disable Tooltips
UE4's mouse-over tooltips might be rendered very slow. They can be disabled by adding to

## Random freeze under KDE
Disable index file content in the KDE file search options.

## Slow rendered tooltips in KDE
Epic suggests allowing compositing for the Unreal Editor, which is stopped by default. Source: https://michaeljcole.github.io/wiki.unrealengine.com/Linux_Known_Issues/#KDE

## Blank window in Blueprint with multi-monitor configuration
To fix the big blank window go to Edit Preferences > User interface > Enable Window Animation and activate the checkbox

## “Unable to launch ./UnrealEngine/Engine/Binaries/Linux/ShaderCompileWorker - make sure you built ShaderCompileWorker.”
Upon launching this error pops up:
 “Unable to launch ./UnrealEngine/Engine/Binaries/Linux/ShaderCompileWorker - make sure you built ShaderCompileWorker.”
If this is the case, you need to build ShaderCompileWorker, as such (assuming you are in UnrealEngine folder, which contains LICENSE.md and README.md):
 ./Engine/Build/BatchFiles/Linux/Build.sh ShaderCompileWorker Linux Development

## Additional Content
## StarterContent
The StarterContent project is installed to , you can browse to it from the launcher.

## Marketplace Apps
The launcher with the Unreal Marketplace is not available for Linux yet[https://forums.unrealengine.com/showthread.php?52166-Unreal-launcher-for-linux, so apps like the ContentExamples project cannot be installed from LinuxThe marketplace apps can be downloaded using the [https://www.unrealengine.com/download launcher on Windows (or Mac), they are stored in .

There are several options to download Marketplace content natively:
* use  and the Epic Games Store installer, with disabled sandbox you can add content directly into your projects
* use Epic Asset Manager from flathub or  which lets you download the assets to the vault
* there is an implementation of UE4 Marketplace Downloader written in JS.
