# Open Broadcaster Software

Open Broadcaster Software (OBS) is an open-source cross-platform video recording and live-streaming application. It provides an easy to pick up and extensible workflow with customizable scenes, volume mixers, transitions, filters and more.

## Installation
Install one of the following packages:

*  — latest OBS release.
** Additionally, to have support for a browser source, install the  package (preferably as a dependency).
*  — builds all the features except Twitch, Restream and YouTube integrations. The browser source plugin is built with patched CEF.
*  — additionally applies some unmerged PRs or backported fixes.

## Configuration
For easy configuration, Tools > Auto-Configuration Wizard can quickly set up base settings for both recording and live-streaming. The wizard auto-selects bitrate, resolution and encoder based on your hardware (and network connection if streaming was set up).

## Hardware video acceleration
Hardware-accelerated encoding and decoding is best for performance, CPU/GPU usage and quality. The encoder can be changed in Settings > Output > Streaming > Encoder (may have to first set Settings > Output > Output Mode to Advanced). See Hardware video acceleration if a hardware encoder is not detected.

## Recording output
By default, OBS will output recordings in the user's home path with spaces in the video filename and the same encoder selected for streaming. The output path, filesize, file format, filename style and more can be changed in Settings > Output > Recording.

## Hotkeys
By default, OBS assigns no hotkeys. All hotkey pairs highlighted in red upon selection can use the same keybind for toggling the pair's function.

Hotkeys may not work in Wayland by default; see #Wayland for troubleshooting.

## Virtual camera output
Starting from version 26.1, OBS supports virtual camera output on Linux. To use it, install v4l2loopback, then the Start Virtual Camera button will appear in OBS. If the  kernel module is not loaded yet, OBS will automatically try to load it and ask for administrative privileges to do so (using ).

## Tips and tricks
## Capturing via Vulkan/OpenGL
The obs-vkcapture plugin adds the capability to capture Vulkan or OpenGL programs by hooking into those APIs directly, rather than using generic Xorg or Wayland window capture APIs. To use it, install , as well as  if capturing 32-bit applications. Follow the instructions in the GitHub repository to setup a Game Capture using the plugin.

## Encoding using GStreamer
obs-gstreamer is a project which provides:

* An encoder plugin for using GStreamer for encoding.
* Plugins for using a GStreamer pipeline as a source, video filter, or audio filter. This is an advanced capability intended for users familiar with GStreamer usage.

To use obs-gstreamer for encoding, install  (or  to get the standalone plugins) and change OBS' encoder to VAAPI H.26x/VPx/AV1 on . If OBS gives an error regarding encoders you might need to install the  package.

## Manual plugins installation
You can manually install plugins to the  directory. An example folder structure is:

 ~/.config/obs-studio/plugins/plugin_name/bin/64bit/plugin_name.so
 ~/.config/obs-studio/plugins/plugin_name/data/locale/en-US.ini

## Record rectangular area
On KDE Plasma, it is possible to select a rectangular area for the recording using the helper script obs-rectangle-area-selector.

## Troubleshooting
## Wayland
Since OBS is a Qt application, see Wayland#Qt to make it work under Wayland. OBS has upgraded from Qt 5 to Qt 6 since version 28, so installation of  is required for the newer versions. See PipeWire#WebRTC screen sharing to enable Wayland screen capture.

## Global shortcuts
While Wayland applications can set up global shortcuts through the XDG desktop portal, OBS currently has no support for itmeaning that the global shortcuts set in OBS only work when OBS is in focus.

## Shortcuts via XDG desktop portal
The [https://github.com/leia-uwu/obs-wayland-hotkeys obs-wayland-hotkeys plugin can be used to provide XDG desktop portal functionality. Install the  package, and OBS should prompt to register global shortcuts the next time it is launched.

## Shortcuts via OBS WebSocket
OBS can be controlled through its WebSocket interface, which can be enabled in OBS by going to Tools > WebSocket Server Settings and selecting Enable WebSocket server.

The WebSocket password and port can be found in WebSocket Server Settings > Show Connect Info.

WebSocket clients:

*
*
*

Then depending on your environment bind WebSocket client commands to keyboard shortcuts — e.g. in KDE Plasma go to System Settings > Shortcuts to set a custom shortcut.

## QuickSync returns "Error creating a MFX session"
This error can occur if the right Intel QuickSync drivers are not installed.

 @ 0x6111a37c1040 Error creating a MFX session: -9.
 Device creation failed: -1313558101.

To use QuickSync, install  for Iron Lake (Gen5) to Ice Lake (Gen10)  GPUs, or  for Tiger Lake (Gen11) and newer GPUs.

For more information, refer to FFmpeg#Intel QuickSync (QSV).

## Plugin load error: frontend-tools
If the following message appears when starting OBS:

 Plugin Load Error

  The following OBS plugins failed to load:

  frontend-tools

  Please update or remove these plugins.

Install the  optional dependency (preferably with the install reason as a dependency) and restart OBS.
