# Virtual reality

Virtual reality is the process of simulating an environment for a user, using a variety of peripherals, head mounted displays or CAVEs, and trackers. Instead of showing you a static viewpoint from a screen, it renders your viewpoint relative to where you are standing, on a head-attached or projected surface, to give an effect identical to your own eyes.

A number of peripherals have been released or are about to be released recently which have brought affordable, extremely immersive virtual reality to everyone. Most of these peripherals have full or partial Linux support, and many have AUR packages.

## Hardware compatibility
The following is a non-exhaustive list of currently supported VR/XR devices, and what software supports them.

## PCVR HMDs
{| class="wikitable"
! Device
! SteamVR
! Monado
|-
! Valve Index
|
|
|-
! HTC Vive/Vive Pro
|
|
|-
! HTC Vive Pro Eye
|  (eye tracking WIP)
|  (eye tracking WIP)
|-
! HTC Vive Pro 2
|  (custom driver and patches needed)
|  (AMD GPUs only, 2 kernel patches required: 1 2)
|-
! Bigscreen Beyond
|  (AMD GPUs only, kernel patch required)
|  (AMD GPUs only, kernel patch required)
|-
! Pimax HMDs
|  (planned)
|  (might work with kernel patch)
|-
! WMR
|  (common HMDs, Monado SteamVR plugin)
|  (6DoF controllers experimental)
|-
! Oculus Rift CV1
|  (OpenHMD recommended)
|  (OpenHMD recommended)
|-
! Oculus Rift S
|  (Monado SteamVR plugin)
|  (6DoF controllers experimental)
|-
|}

In addition, there's an experimental PC-PC stream client for WiVRn that might work with the above HMDs that are supported by Monado.

## Standalone HMDs
Entries marked with "Yes" but without store links can be sideloaded from their corresponding project websites.
{| class="wikitable"
! Device
! WiVRn
! SteamVR through ALVR
! SteamVR through Steam Link
|-
! Meta Quest 2/3/3S/Pro
|  (Meta Quest Store)
|  (Meta Quest Store)
|  (Meta Quest Store)
|-
! Meta Quest 1
|
|  (Sidequest)
|
|-
! Pico 4/4 Ultra
|
|
|  (Pico Store)
|-
! Pico Neo 3
|
|
|  (Pico Store)
|-
! HTC Vive Focus 3
|
|
|  (Viveport)
|-
! HTC Vive XR Elite
|
|
|  (Viveport)
|-
! Lynx R1
|
|
|
|-
! Apple Vision Pro
|
|  (Apple App Store)
|
|-
! Samsung Galaxy XR
|
|  (partially working)
|
|}

## Tracking devices
{| class="wikitable"
! Device
! SteamVR
! Monado
! WiVRn
|-
! Vive/Tundra trackers
|  (native or spacecal)
|  (native or motoc)
|  (motoc)
|-
! SlimeVR trackers
|
|
|
|-
! Project Babble
|  (oscavmgr)
|  (oscavmgr)
|  (oscavmgr)
|-
! Eyetrack VR
|  (oscavmgr)
|  (oscavmgr)
|  (oscavmgr)
|-
! Mercury hand tracking
|
|  (survive driver only)
|
|-
! Lucid VR gloves
|
|  (survive driver only)
|
|-
! Kinect based FBT
|
|  (experimental)
|
|-
! Standable FBT
|
|
|
|}

## Supported runtimes and toolkits
## OpenXR
OpenXR is an open, royalty-free standard for access to virtual reality and augmented reality platforms and devices. It is maintained by the Khronos Group and adopted by most of the industry. Most runtimes support OpenXR.

## Monado
Monado is an open source OpenXR runtime developed by Collabora. It is under heavy development and aims to provide a common runtime supporting most headsets. Current progress can be found here: https://monado.freedesktop.org/

Install using .

## Envision
Envision is a graphical app that acts as an orchestrator to get a full Monado setup up and running with a few clicks. Envision attempts to construct a working runtime with both a native OpenXR and an OpenVR API, provided by XRizer or OpenComposite, for client applications to utilize.

## WiVRn
WiVRn is a runtime based on Monado, capable of streaming to standalone headsets. It currently supports most available Android based HMDs, and also has experimental support for PC to PC streaming.

Upstream recommends to install ,  or  (for compatibility with Steam games and OpenVR applications), and optionally  for the dashboard. It is also available via Flatpak. You can install the Android client from your devices' store, download the prebuilt Android client from the GitHub releases to sideload, or compile it yourself according to the build documentation.

## OpenVR / SteamVR
OpenVR is an effort by Valve to create an open API for VR development. Unfortunately, while the API is open, the actual default implementation (SteamVR) is not. SteamVR also provides an OpenXR runtime.

## Setting up SteamVR
Install Vulkan and Steam. If using NVIDIA drivers, you may need to set the VK_DRIVER_FILES environment variable. Required dependencies for 32-bit packages are: , , .

From Steam, install SteamVR from the tools menu.

## ALVR
ALVR is a SteamVR driver which allows streaming to standalone headsets like the Meta/Oculus Quest. It is available in the  package.

## Steam Link
Valve's closed-source Steam Link App allows streaming games from a PC running SteamVR to supported headsets without relying on third-party software. It supports both a VR mode for proper VR games and a flat-screen mode for desktop games. If the App finds your PC but fails to connect to SteamVR, you may have to open some ports in your firewall as described here.

## OpenHMD
OpenHMD is currently not maintained, and should be treated as deprecated for all but older HMD's. It aimed to provide a Free and Open Source API and drivers for immersive technology, such as head mounted displays with built in head tracking. The aim was to implement support for as many devices as possible in a portable, cross-platform package.

OpenHMD only supports older devices such as Oculus Rift, HTC Vive, Sony PSVR, Deepoon E2 and others, so it is not needed for newer devices, and should not be considered. Most of the HMD driver efforts are now going towards Monado. There's a fork focusing on Oculus Rift CV1 tracking, and it's still recommended for that specific headset; use Monado otherwise.

## SteamVR support
It is possible to use OpenHMD with SteamVR. To do that, you need to install  and create a symlink that points to the OpenHMD SteamVR driver inside your SteamVR drivers directory, for example:

 $ ln -s /usr/lib/steamvr/openhmd ~/.steam/steam/steamapps/common/SteamVR/drivers/openhmd

## Other software
## vr-video-player
A simple tool to view any X11 window inside your VR headset. vr-video-player supports stereoscopic/180°/360° videos/games. vr-video-player also lets you view regular videos/games/windows inside VR as a flat screen.

Available as .

## xr-video-player
A fork of vr-video-player for OpenXR and wayland that uses pipewire to capture a window or screen/s.

Available as .

## SideQuest
SideQuest can be used to install APK files to your Oculus Quest. It is available as .

See https://sidequestvr.com/setup-howto for installation steps:

# Create an Oculus developer account.
# Turn on Quest in developer mode (e.g., with your phone) and connect your Quest via cable.
# Press Allow USB debugging inside Quest.

See the SideQuest website for more information.

## WayVR
WayVR is a lightweight OpenXR/OpenVR overlay that can mirror and control X11/Wayland desktops. It can also act as a Wayland compositor.

Available as  and .

## Stardust XR
Stardust XR (GitHub) is a modular XR display server. It can act as an overlay (and can run side by side with wlx-overlay-s) or as a standalone application. It can provide a Wayland compositor using , an application launcher with , skyboxes/home environments with  and several other features using other packages. Install the server with ; you can also install  for a premade startup script.

## Troubleshooting
## SteamVR support
## Configuration or startup errors
SteamVR/OpenVR creates a directory  that can get misconfigured over the various versions. Delete that directory and completely uninstall/reinstall SteamVR.

It can also apparently have trouble accessing different HMD's under some configurations. Please refer to the HMD compatibilty chart to see if your headset is compatible.

## Games/Programs
Most XR applications run without major issues through Proton or Proton GE. Proton-GE-RTSP, which provides targeted fixes for VRChat and other social VR platforms, can be installed using  or . If a game has issues running through Proton, please refer to the game's Linux/Wine compatibility information, ProtonDB and documentation for the XR runtimes and compatibility layers in use for possible fixes.

## Other Issues
Because of the nature of VR on Linux it is very common for a wide variety of issues to pop up, and because of the sheer amount of possible issues, it is not possible to write out everything here. Instead, please refer to either the software's respective documentation, the Linux VR Adventures Wiki, or the Linux VR Adventures Discord for help on any possible issue you are facing.
