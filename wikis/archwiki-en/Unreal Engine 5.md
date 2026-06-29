# Unreal Engine 5

Unreal Engine 5 is the latest version of the videogame engine created by Epic Games.

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
You can compile manually from a downloaded GitHub release or install from AUR. By default the engine will be compiled on all physical cores.

## Manually
You can get the most recent releases on GitHub as ZIPs.

Setup:

 $ ./Setup.sh

Generate project files:

 $ ./GenerateProjectFiles.sh

Then compile:

 $ make -j1

This will compile the Unreal Engine and the Unreal Editor.

 $ ./Engine/Build/BatchFiles/Linux/Build.sh UnrealEditor Linux Development -Progress

## From the AUR
Unreal Engine 5 is available in the AUR as the  package. You might have to fix permissions for UE5 to precompile shaders on first launch:

 # chmod -R a+rwX /opt/unreal-engine/Engine

In the case of version 5.4, the installed size is ~190 GiB, it needs 340+ GiB to build with the final package being ~45 GiB when compressed. This PKGBUILD downloads ~20 GiB of source files plus ~5 GiB of dependencies.

For a smaller download you can use .zip releases as a source for PKGBUILD. Note that this link will not work unless you first follow the steps outlined above.

## From the Epic Games Store
Pre-compiled binaries are also available via Epic's Game Store. These .zip files contain precompiled binaries without any need for the setup steps as mentioned above.

That being said, you will still need the pre-requisite dependencies to run the extracted binary(see the aur for reference). After downloading, you should be able to simply extract the files wherever you please and launch the editor using the binary located in the extracted path:

 $ Linux_Unreal_Engine_5.x.x/Engine/Binaries/Linux/UnrealEditor

The zip for Linux_Unreal_Engine_5.5.4 is 25.2GB in size and after extraction is around ~43GB in size.

## Compilation time
The compilation will take 4-5 hours for the average high end consumer cpu (i9/Ryzen9). This could be somewhat accelerated by forcing to use all cores instead of just the physical ones which is how it compiles by default. This number does not include the time to compile shaders after first launch.

(Ryzen 9 6900HX compilation time for UE5.4.2 was about 5 hours using all (8) physical cores after downloading the depenedencies. Packaging, unpackaging and compiling shaders afterwards took another hour thus making the total install time after downloading the dependencies ~6 hours.)

## Troubleshooting
## Compilation problems
If the compilation fails you should try building the Editor using the Debug profile$ make UE5Editor-Linux-Debug

However, this might have some performance impact.

Another approach would be to use different clang version (e.g. 3.8 or 4.0)

## Runtime problems
If the editor does not start from the menu, or something does not work right, start it in a console and check the output for errors.

 $ /opt/unreal-engine/Engine/Binaries/Linux/UnrealEditor

## C++ code project problems
After creating a code project, the new project opens in a text editor instead of in Unreal Editor as it should.  After re-launching the editor, the new project shows up and can be opened, but on the first run, it takes a half-hour or so to compile, and since this happens in the background (no GUI) it might not seem to be doing anything.  The CPU usage should show that it is still compiling, and you may want to launch the editor from a console to see progress.

If while trying to open the project in UE for the first time, you get a message about editor modules being out of date, you need to build the  target in your IDE. Do not abort this build, or you will brick the Unreal Editor and will need to reinstall . Afterward, it will open and ask you to rebuild the project class, after which you can actually start working on your new project.

Note that completing both of these rebuilds can very well take over an hour, depending on your system specs.

## Engine modules are out of date, and cannot be compiled while the engine is running. Please build through your IDE
First, in your source folder in your project, check that {nameofproject}.Target.cs and {nameofproject}Editor.Target.cs has "DefaultBuildSettings = BuildSettingsVersion.V2;" in the section base(Target) { ... }
If it does not work, check the file Engine/Source/Developer/DesktopPlatform/Private/DesktopPlatformBase.cpp in your Unreal Engine source code, look for the line `Arguments += " -Progress -NoEngineChanges -NoHotReloadFromIDE";` and remove the two last options : `Arguments += " -Progress";`

* Re-compile Unreal Engine
* Launch your project and accept the rebuild

## Disable Tooltips
UE4's mouse-over tooltips might be rendered very slow. They can be disabled by adding to:

## Random freeze under KDE
Disable index file content in the KDE file search options.

## Slow rendered tooltips in KDE
Epic suggests allowing compositing for the Unreal Editor, which is stopped by default. Source: https://michaeljcole.github.io/wiki.unrealengine.com/Linux_Known_Issues/#KDE

## Blank window in Blueprint with multi-monitor configuration
To fix the big blank window go to Edit Preferences > User interface > Enable Window Animation and activate the checkbox

## Issues with Wayland in a Window Manager
Unreal Engine has lots of issues with its wayland support. It is recommended to use the x11 version by setting these environment variables.

 unset QT_SCALE_FACTOR
 unset QT_AUTO_SCREEN_SCALE_FACTOR
 unset GDK_SCALE
 unset GDK_DPI_SCALE

 export SDL_VIDEODRIVER=x11

Alternatively, edit the Exec= line in the desktop entry:

## SDL: wayland not available
When trying to force the editor to run on Wayland using the SDL_VIDEODRIVER=wayland environment variable, the editor will give this error to some users. The cause of this problem is unknown, as such no reliable solution exists for this problem. Setting SDL_DYNAMIC_API=/usr/lib/libSDL2.so will actually allow you to run the editor on wayland but it will crash the moment you hover your mouse over certain UI elements.

## Flickering shadows, stuttering, random crashes
There seem to be major issues with frame buffer synchronization with Vulkan on NVIDIA drivers. The simplest fix for this is to run in `one-thread mode without parallel rendering. It's not ideal, but it provides a significantly more stable experience and fixes a variety of issues in the editor.

If you're experiencing issues, try launching your project like so:

 $ /Path/To/Unreal/Engine/Binaries/Linux/UnrealEditor "/Path/To/YourProject/YourProject.uproject" -NoParallelRendering -onethread

## FAB plugin does not load
The FAB plugin, as well as other Unreal Engine components that rely on web services via CEF (Chromium Embedded Framework), may fail to load or work only partially on some systems.

This issue is related to name resolution via glibc NSS when using systemd-resolved. In particular, configurations that include the resolve NSS module with conditional return rules (such as [!UNAVAIL=return) may cause DNS resolution failures inside CEF-based applications. As a result, CEF is unable to resolve Epic Games service endpoints, causing the FAB plugin to malfunction or remain blank.

This problem is most likely to affect Unreal Engine 5.6 and later versions, which ship with newer CEF builds (CEF 128 and newer).

A workaround is to simplify the hosts line in /etc/nsswitch.conf to use a more traditional and deterministic resolution order:

For example:

After applying the change, restart Unreal Editor.

## Additional Content
## Starter Content
The StarterContent project is installed to , you can browse to it from the launcher.

## Marketplace Apps
The launcher with the Unreal Marketplace is not available for Linux yetso apps like the ContentExamples project cannot be installed from Linux[https://answers.unrealengine.com/questions/301869/download-content-from-marketplace-on-linux.html.

The marketplace apps can be downloaded using the launcher on Windows (or Mac), they are stored in . ProgramData is hidden by default.

There are several options to download Marketplace content natively:
* use  and the Epic Games Store installer, with disabled sandbox you can add content directly into your projects
* use Epic Asset Manager from flathub or  which lets you download the assets to the vault
* there is an implementation of UE4 Marketplace Downloader written in JS.
