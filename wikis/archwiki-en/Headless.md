# Headless

A headless computer is one which does not have a connected monitor. This is common for servers or remote systems where you would access the system over the network. This article describes different methods for how to set up a headless server that can provide a GUI desktop over the network.

## Some common tools
These are some of the existing tools available to solve the headless remote desktop problem. Some of these tools are used in the Solutions chapter later on.

## VNC remote desktop client + server
Old but very common remote desktop technology. Common on Linux. This is desktop oriented and usually shows a pixel perfect copy of the server desktop. VNC will usually only send updates over the network to the client if something changes on screen.

## RDP remote desktop client + server
Similar to VNC but more common on Windows. RDP is very similar in use case and technology to VNC but has more functionalty.

## Sunshine server + Moonlight client
A "game streaming"-oriented solution that works well also for remote desktops. This solution will continuously send a video stream from the server to the client. Since video compression is not directly suited for pixel perfect replication it will sometimes show a picture with slight artifacts.
Sunshine is the server software and Moonlight is the client application. Since this solution streams at a very low level from the server it is compatible with both X and Wayland and works most GPUs.  Some drawbacks of this solution is 1) it uses multiple ports and protocols and is therefore more difficult to tunnel over the internet than RDP and VNC and 2) uses more network bandwidth than RDP and VNC.

## Rustdesk, Anydesk
Rustdesk and Anydesk have nonstandard protocols so therefore provide both the client and server software. They are still a bit immature on Wayland.

## Network KVMs
This is a hardware unit connected to the server, both to the display port and a USB port. This will emulate a monitor and keyboard+mouse and present this to the client (usually via a web page). The main drawback is that the picture quality is sometimes not very good and the picture resolution is limited, of course depending on KVM solution. For more enterprise grade servers, the network KVM is usually built into the server (e.g. HP ILO or Dell IDRAC).

## Monitor dummy plug
A dummy plug is a plug that is inserted into the display port or hdmi ports on the server. It acts as a monitor to the GPU. The sole purpose is to trick the GPU into thinking it is connected to a monitor. That is sometimes required before the GPU will display something, like for example a desktop GUI. The benefit is that you can mirror the screen via some remote desktop solution but the drawback is that you can no longer see the output of the monitor so troubleshooting is sometimes tricky. If you want to search the Internet for a plug to purchase, search for "hdmi plug" or "display port plug", possibly also adding "virtual display adapter".

## Virtual display
Virtual displays can be created using the VKMS (Virtual Kernel Mode Setting) or EVDI (Extensible Virtual Display Interface) kernel modules. They emulate DRM devices, allowing Xorg or Wayland to treat them as physical outputs.

## Other tools
See List of applications/Internet Remote desktop.

## Common problems
When trying to set up a remote desktop, some problems are usually encountered. We note them here for information.

## A monitor needs to be connected and turned on
Most remote desktop solutions will mirror whatever is on the monitor over the network to the client. This will however require that a monitor is connected and turned on, otherwise the GPU driver will often refuse to allow the desktop to start. A monitor that is turned on will also consume unnecessary power.

## Resizing desktop to client window does not work
Most remote desktop solutions do not support resizing of the remote desktop to fit the client window. As a fallback, it is often possible to change the resolution of the desktop.

## Keys do not present correctly
Pressing keys on the client keyboard will cause the wrong characters on screen. This is a complex problem and involves both the client and server desktops, as well as the remote desktop software used. Can be solved, but may require some trial and error to find the right combination.

## Slow screen updates
Some solutions are slower than others. It is necessary to try multiple solutions to find a good solution to this problem.

## GPU acceleration not used
Some solutions will fall back to SW driven GUI for the desktop. That may not be a performance problem but may cause problems running some 3D software that require some features that are not emulated in the SW graphics pipeline.

## High CPU usage
Something to watch out for is high CPU usage, both in use and when idling and both on server and client. Game streaming solutions seem to have less focus on low power usage.

## Solutions
This chapter contains solutions for how to build a remote desktop solution to a headless server with the following requirements:

# Fully headless. No monitor or monitor plug required.
# Desktop resize supported. Should resize to size of client window.
# Low CPU usage.
# GPU accelerated.

## Labwc/sway/wayfire with wayvnc
This solution does not mirror the desktop shown on a physical monitor. Instead a fully virtual monitor is used. The requirements above are fulfilled.

# Install labwc on the server. This probably works also for any other desktop based on wlroots. Known to also work are sway or wayfire.
# Install  on the server.
# Use the following example script to start the desktop with labwc:

 #!/bin/bash
 # Example script to start a headless desktop + VNC server
 export WLR_BACKENDS=headless
 export WLR_LIBINPUT_NO_DEVICES=1
 #export WLR_RENDER_DRM_DEVICE=/dev/dri/renderD128 # Only needed for wayfire
 labwc >& labwc.log &
 sleep 5
 export WAYLAND_DISPLAY=wayland-0 # change to wayland-1 for other than labwc
 wayvnc 0.0.0.0 >& wayvnc.log &

Use the TigerVNC client to access the remote desktop. This VNC client supports proper window resizing.

## GNOME
Gnome can be started in headless mode according to this link.

## KDE
For X11, this can be achieved by using TigerVNC both for the client and server. For Wayland, no method has yet been found.

## Custom EDID file
A custom EDID (Extended Display Identification Data) file can be added via a kernel parameter to trick the system that there is a monitor plugged in even though there is not any present nor physically plugged in.This can be used to save money from buying dummy plugs and allow for resolutions that normal dummy plugs would not support (such as 3440x1440). Premade EDID files can be acquired [https://git.linuxtv.org/v4l-utils.git/tree/utils/edid-decode/data here

Once you have downloaded an EDID file that has what you need, you will then have to create a directory for the file. After making the directory, move or copy the EDID file to the directory.

The outputs on your GPU must be identified and a free output must be available, replacing  in the next step with the appropriate output.
{{hc|$ for p in /sys/class/drm/*/status; do con${p%/status}; echo -n "${con#*/card?-}: "; cat $p; done|
DP-1: disconnected
HDMI-A-1: disconnected
VGA-1: disconnected}}

Add the following kernel parameters afterwards

Update your initial image creator's config to include the EDID file. This one is for mkinitcpio's .

Afterwards, regenerate the initramfs

## VKMS
This example shows how to run KDE Wayland and Sunshine, but other options are possible.

Virtual Kernel Mode Setting (VKMS) is a software-only KMS driver that allows for a virtual display output without physical hardware connected.

Load the  kernel module. Enabling the virtual cursor is often necessary for remote desktop applications.

Identify which card corresponds to your physical GPU and which corresponds to VKMS:

KDE compositor can use the KWIN_DRM_DEVICES environment variable to split rendering and output responsibilities.

## EVDI
This method uses evdi to create a virtual connector and  with the  driver to simulate a physical display.

Install  and load the module.

Define a virtual device and monitor. Use  to find GPU's BusID (e.g.,  becomes ).

Start Xorg in the background.

Use  to generate a valid modeline for your desired resolution.

Use the output from the  command to define the new mode. Your output device name, e.g., DVI-I-1-1, may vary; check ).

Start your Desktop Environment and the streaming server.
