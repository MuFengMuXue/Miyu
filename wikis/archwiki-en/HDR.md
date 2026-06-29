# HDR

High-dynamic range (HDR) is supported by Wayland's Color management and HDR protocol, and some compositors have implemented it. X.org has no plans to support HDR.

## Requirements
* HDR-capable display
** While many displays advertise HDR support, many may provide a suboptimal experience if they lack any form of local dimming. More information is available at RTINGS: Local Dimming on TVs.
* HDR-capable GPU and driver
** AMDGPU and NVIDIA are both supported
** Intel graphics has experimental HDR support with Gen 9 and newer
*** The implementation is reportedly incomplete.
* Supported compositor
* Supported application
* Vulkan WSI with HDR support

## Vulkan HDR WSI
 and  extensions are required for HDR support when using the Vulkan API.

*  25.1 and later includes these extensions by default.
*  595.58.03 and later also includes these extensions by default.
** NVIDIA users on drivers before 595.58.03 must install  and set  in each game or application that will be used with HDR. Enabling this globally is not recommended.

## Compositor configuration
## KDE Plasma
See KDE#HDR.

## Hyprland
Hyprland >= 0.55 will automatically switch to HDR mode in its default configuration, when the monitor and fullscreen content support it. To use HDR on the desktop you must set  and  in your monitor configuration like so:

{{bc|
hl.monitor({
    -- ...
    bitdepth  10,
    cm  "hdr",
})
}}

Additional settings can be found on the Hyprland wiki: monitor color management, render variables.

## GNOME
Ensure  is >= 48.0.

Enable HDR in GNOME's display settings. The HDR toggle is per-monitor and is located next to the resolution and refresh rate setting.

## Gamescope with Steam session
Valve's Steam compositor gamescope offers experimental HDR support. Following these steps will allow you to try out Valve's Steam client running through the HDR capable gamescope.

* Install  and
* You may create the optional config file  with the following content:
** Update the resolution values above to the correct ones. You can list your displays by running .
** You may need to set the Display  if it does not pick the right one by default.

You can now start  from your login manager or a terminal using one of the following steps:

## Via a login manager
Log out and select the Steam Big Picture in your login manager and log in.

## Via the command line
# Go to a new TTY by pressing
# Log in and run  to start the standalone steam session in HDR.
#* If networking does not work you can fix it by installing and enabling NetworkManager.

## Configure Steam
# In the general settings, under Display, you should now see HDR settings. Enable HDR and Experimental HDR Support.
# Select an HDR compatible game and click on the cog next to it.
# Set Compatibility to Force Proton 8.0 or Proton Experimental.
# Set Game Resolution to match your monitor otherwise it will launch at Steam Deck native resolution.
# Click Play to start the game.  Check the in-game settings to see if the HDR setting is available and enable it.
# To switch back to your normal session, select Power and Switch to desktop mode from the Steam menu.

## COSMIC
The COSMIC developers have promised HDR support in the initial stable release.

## sway
Add  and  to the outputs's config in your sway config file, and start sway with  environment variable set.

Setup a binding to toggle hdr or toggle manually i.e.: .

## Application configuration
## Wine/Proton
HDR through Wine or Steam Proton requires DXVK (2.1+) or VKD3D-Proton (2.8+), depending on DirectX version used by the game.

## Without Gamescope
To use HDR without gamescope run a build of Wine which includes the Wayland driver.

* proton-ge-custom: install  and set  and  * [https://github.com/Frogging-Family/wine-tkg-git wine-tkg: install wine-tkg, set , and unset .
* proton-cachyos or wine-cachyos: install your choice of , , or  and set  and  ==== With Gamescope ====

Gamescope with proper HDR requires scRGB and  protocol support or [https://gitlab.freedesktop.org/wayland/wayland-protocols/-/merge_requests/14 frog-color-management-v1 protocol support in your compositor.

Because of this gamescope will not work with the  layer. Ensure  is not .

You have many options for using gamescope depending on your desired configuration:

* Launch Steam with HDR enabled. All games will then have HDR enabled, but Steam and all games will be launched inside a gamescope window.
 $ gamescope --hdr-enabled --steam -- env DXVK_HDR=1 steam
* Enable HDR for a single game in Steam. Set the following Launch options:
 DXVK_HDR=1 gamescope -f --hdr-enabled -- %command%
* To launch a non-Steam game within gamescope:
 $ DXVK_HDR=1 gamescope -f --hdr-enabled -- executable

## RetroArch
HDR in RetroArch is supported from version 1.10.0 with Vulkan video driver. First, select video driver Vulkan. Then, enable HDR in RetroArch video settings via Settings tab > Video > HDR > Enable HDR.

 $ retroarch

## Native SDL
To run native games that use SDL with HDR set .

For example for Quake II RTX:
 $ SDL_VIDEODRIVER=wayland quake2rtx

## mpv
For best image quality mpv maintainers recommend using the  video output driver, which is the default.  supports HDR with , which is selected by default on Wayland.

 $ mpv "path/to/video"

Other ways of enabling [https://github.com/mpv-player/mpv/discussions/16105#discussioncomment-12619072 Wayland HDR support include using the  video output and the  GPU context.

 $ mpv --vo=dmabuf-wayland "path/to/video"

* From the tty terminal, one could do ( is selected by default)
 $ mpv "path/to/video"

## Firefox
 introduces working experimental HDR in 138.0 under the hidden preference . You can enable it at .

Stable HDR is still in progress [https://bugzilla.mozilla.org/show_bug.cgi?id=1642854.

## Chromium
 has work-in-progress HDR support Support has been merged as of version 141.0.7370.0.

## Troubleshooting
## HDR video samples
Kodi wiki [https://kodi.wiki/view/Samples#4K_(UltraHD)_&_HDR_Formats maintains the list of fair use HDR video samples. These can be used to test the HDR output using video players that support HDR such as #mpv.

## Broken screen sharing with HDR10
Pipewire attempts to stream what it sees as BGRA, which WebRTC cannot interpret, due to its current lack of capacity to interpret it. As such, a "ParamId:EnumFormat: 0:0 Invalid argument" exception is thrown and the WebRTC socket crashes for that application == See also ==

* [https://www.youtube.com/watch?t=21171&v=yTO8QRIfOjA X.Org Developers' Conference 2022 | Harry Wentland: "Is HDR Harder?"
* wlroots/wlroots | HDR10 support
* Xaver Hugl's blog | An update on HDR and color management in KWin
