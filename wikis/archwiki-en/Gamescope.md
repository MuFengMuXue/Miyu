# Gamescope

Gamescope is a microcompositor from Valve that is used on the Steam Deck. Its goal is to provide an isolated compositor that is tailored towards gaming and supports many gaming-centric features such as:

* Spoofing resolutions.
* Upscaling using AMD FidelityFX™ Super Resolution or NVIDIA Image Scaling.
* Limiting framerates.

As a microcompositor it is designed to run as a nested session on top of your existing desktop environment though it is also possible to use it as an embedded compositor as well.

## Installation
Gamescope can be installed with the  package. Additionally there is also  which includes extra patches not present in the mainline build.

## Requirements
* AMD: Mesa 20.3 or above
* Intel: Mesa 21.2 or above
* NVIDIA: proprietary drivers 515.43.04 or above, and the  kernel parameter

## Usage
Gamescope offers many options, far too many to cover here. For a full list use the  command from a terminal.

## From a display manager
See Steam#Big Picture Mode from a display manager.

## From a desktop session
The following command will run supertuxkart using Gamescope and force a 1920x1080 resolution at 60 FPS

 $ gamescope -W 1920 -H 1080 -r 60 -- supertuxkart

## From Steam
You can run games from Steam using Gamescope by adding the following to the games launch options

 gamescope -- %command%

 gamescope -W 1920 -H 1080 -r 60 -- %command%

## From Wine
To run programs using Gamescope through Wine, simply append wine followed by the executable.

 $ gamescope -W 1920 -H 1080 -r 60 -- wine supertuxkart.exe

Almost all the popular Wine managers such as Lutris, Bottles, and PlayOnLinux have support for Gamescope. Using them is as simple as installing the desired Gamescope package and checking the Use Gamescope (or similar) option.

## From Flatpak
You can also use Gamescope from Flatpak versions of Wine managers and Steam in the same way as you would from a package install. It does however require that you first install Gamescope from Flathub with the following command:

 $ flatpak install flathub org.freedesktop.Platform.VulkanLayer.gamescope

## Upscaling
The  and  flags can be used to upscale games using AMD FidelityFX™ Super Resolution 1.0 (FSR) or NVIDIA Image Scaling v1.0.3 (NIS) respectively. You can also use  for integer upscaling or  for stretch scaling.

To upscale a 720p game to 1440p using FSR:

 $ gamescope -h 720 -H 1440 -F fsr -- supertuxkart

To run a game at 1080p internal resolution but display it at 4K using NIS:

 $ gamescope -w 1920 -h 1080 -W 3840 -H 2160 -F nis -- supertuxkart

Games with low resolutions typically use linear filtering on fullscreen by default and sometimes get stretched. This is specially noticeable in classic JRPG. To have a pixelated look and keep aspect ratio:

 $ gamescope -F nearest -S fit -- tecnoballz

Filters can be changed while the game is running:

*  toggle nearest filtering.
*  toggle FSR upscaling.
*  toggle NIS upscaling.
*  increase FSR sharpness by 1.
*  decrease FSR sharpness by 1.

## HDR support
Gamescope is a requirement for HDR10 support when playing games, to make use of this feature you must launch your Gamescope session using the  flag.

## Wayland support
Gamescope does not support Wayland clients by default. To enable support for Wayland clients, add the  flag to Gamescope's parameters.

## SDR Gamut Wideness
Since SteamOS 3.5.5, Valve has changed the default color rendering for the Steam Deck LCD. The effect is achieved through Gamescope by changing the "wideness" of the gamut for SDR content, which can result in a warmer and more vibrant color appearance depending on the adjustment.

In a Steam game's launch options, simply add  followed by a value that's equal or between 0-1:

 gamescope --sdr-gamut-wideness 1 -- %command%

## Mangoapp
Using traditional MangoHud with gamescope is not supported. Instead the gamescope argument  should be used. This allows MangoHud to run on top of gamescope instead of the underlying application. Certain MangoHud configurations, such as displaying FSR or HDR status, require the use of mangoapp with gamescope in order to work.

## Variable Refresh
If your monitor supports it, enable variable refresh rate by passing the  flag.

## Tips and tricks
## Recording the gamescope output
Gamescope exposes a video node in PipeWire for recording. You can record this with GStreamer.

 $ gst-launch-1.0 --eos-on-shutdown pipewiresrc do-timestamp=true target-object=gamescope ! vaapih264enc ! h264parse ! mux. pulsesrc do-timestamp=true device="Recording_$(pactl get-default-sink).monitor" ! opusenc ! mux. matroskamux name=mux ! filesink location=recording.mkv

## Troubleshooting
## Cursor doesn't behave properly
If the cursor is not captured by the application, for example by limiting your camera movement or by not properly disappearing out of menu, use the  option. Some proton/wine games require this workaround.

## Switching to fullscreen causes low performance
This is a known bug when using Gamescope's fullscreen hotkey , if you encounter this issue it can be worked around by using the fullscreen flag  when launching the game.

## Setting Gamescopes priority
Another known cause of low performance and/or stuttering is not having Gamescope's priority set correctly. You can tell this is the case if you see an error like this in the terminal while Gamescope is running:

The following command will fix this:

 # setcap 'CAP_SYS_NICE=eip' $(which gamescope)

## Window does not appear in Flatpak on NVIDIA
This is because Flatpak Gamescope fails to access the NVIDIA DRM's GBM backend.
It can be solved by simply setting an environment variable with the following command:

 $ flatpak override --env=GBM_BACKENDS_PATH=/usr/lib/x86_64-linux-gnu/GL/nvidia-XXX-YY-ZZ/extra/gbm packageid

where  is the Flatpak package identifier of Gamescope or the app you want to use Gamescope with, such as Bottles.
Replace  with the currently installed NVIDIA driver version; inside Flatpak, it can be queried with this command:

 $ flatpak run --command=ls packageid /usr/lib/x86_64-linux-gnu/GL

where  is any Flatpak package identifier; do note that the directory only exists inside Flatpak.

## Image corruption on Intel graphics
If gamescope outputs corrupted image colors on Intel graphics disabling lossless color compression can be a work-around at the cost of increased memory bandwidth utilization. To disable it pass  environment variable.

## VRR stutters when HDR is enabled
If VRR and HDR work independently, but the framerate is unstable when they're both enabled, then you may be hitting issues with long HDR compositing times. See https://github.com/ValveSoftware/gamescope/issues/1006. This only applies to using Gamescope in embedded mode, and not when using gamescope within an existing wayland or X session.

When using AMD graphics this can be fixed by using experimental AMD color management, which uses hardware planes to composite the final image. This requires one of two setups:

## Steam Deck kernel
* The Steam Deck Linux kernel , , or a kernel built with the [https://gitlab.com/evlaV/linux-integration/-/commit/90e3a855c922d0b8c4b18c886c5cf73223d69475.patch Steam Deck color management patch
*

## Linux kernel with experimental AMD color management enabled
Linux 6.8 or newer compiled with  including , eg

## High polling rate mice cause stuttering
Moving a high polling rate mouse (observed with 4000Hz) in the game window might cause stuttering or temporary freezes Setting a lower polling rate like 1000Hz should work around this issue.

## Swapchain Errors
A common cause of swapchain errors is improperly attempting to use mangohud instead of mangoapp. See the Mangoapp section of #Usage, above.

## Launching gamescope from Steam, stuttering after ~24 minutes (Gamescope Lag Bomb)
If after launching gamescope from Steam you experience heavy stuttering setting in around ~24 minutes, then you can fix this by either enabling the Steam Overlay  option on your Steam Client, or by overwriting the environment variable  with an empty value. For example:
 $ LD_PRELOAD="" gamescope -- %command%

This, however, will disable the Steam Overlay and any additional Steam features; game recording being one of them. Depending on the game, you may be able to restore Steam functionality by bypassing  running on gamescope, and passing it instead as an env directly to the desired command. For example:
 $ env -u LD_PRELOAD gamescope -- env LD_PRELOAD="$LD_PRELOAD" %command%

The above seems to work well for games that do not contain a secondary launcher (Rockstar, EA, etc.)

See [https://github.com/ValveSoftware/gamescope/issues/163 ValveSoftware/gamescope#163.

## Games crash on launch if Gamescope is launched non-fullscreen.
Several reports have indicated that some games on certain systems will crash if Gamescope is not launched in fullscreen, and the current workaround is to add  to the launch options. This will, however, lead to issues where the camera can pan in games rotationally indefinitely due to a failure to capture the mouse cursor correctly (see 4.1). Thus,  is recommended to be used in conjunction with this fix.

## Rapidly cycling framebuffer on OpenGL/32-bit games with NVidia.
See ValveSoftware/gamescope#495 for a report regarding the details. Causes are unconfirmed, and no fixes have been listed yet.
