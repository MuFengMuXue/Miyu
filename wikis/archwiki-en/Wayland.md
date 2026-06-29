# Wayland

Wayland is a display server protocol. It has been widely established as the successor of the X Window System [https://blogs.gnome.org/alatiera/2025/06/08/the-x11-session-removal/ [https://pagure.io/fesco/issue/3408. You can find a comparison between Wayland and Xorg on Wikipedia.

Display servers using the Wayland protocol are called compositors because they also act as compositing window managers. Below you can find a list of Wayland compositors.

For compatibility with native X11 applications to run them seamlessly, Xwayland can be used, which provides an X Server in Wayland.

## Requirements
Wayland is just the protocol, unlike Xorg it does not have a common "display server" to install. To use it, you only need a compatible display driver (this section) and a compositor (next section) or desktop environment (e.g. GNOME or Plasma) that implements the Wayland protocol. Most Wayland compositors only work on systems using Kernel mode setting.

For the GPU driver and Wayland compositor to be compatible they must support the same buffer API. There are two main APIs: GBM and EGLStreams.

{| class="wikitable"
! Buffer API !! GPU driver support !! Wayland compositor support
|-
| GBM || All except NVIDIA For other Java programs, you need you bring your own Wakefield build, e.g. . To use it, point  to  and run your program with the  option.

## Tips and tricks
## Automation
* ydotool () - Generic command-line automation tool (not limited to wayland). Enable/start the  user unit. See , .
* wtype () - xdotool type for wayland. See .
* keyboard - Python library that works on Windows and Linux with experimental OS X support.  Also see the mouse library.
* wlrctl  () - A command line utility for miscellaneous wlroots extensions (supports the foreign-toplevel-management, virtual-keyboard, virtual-pointer)

## Remap keyboard or mouse keys
See Input remap utilities.

## Screencast
See Screen capture#Screencasting and Screen capture#Screencast Wayland windows with X11 applications.

## Persist clipboard after app close
Due to Wayland's design philosophy, clipboard data is stored in the memory of the source client. When the client closes, the clipboard data is lost. You can solve this using , which runs in the background to reads the clipboard data and stores it in its own memory, separate from the source client.

## Autostart wayland compositor as systemd service
If you do not want to use a display manager or a shell, you can autostart your Wayland compositor with a systemd service. Adjust the  line with the compositor you want to use. Here is an example for KDE Plasma:

## Use another renderer for wlroots based compositor
You can use another wlroots renderer such as Vulkan by specifying the  environment variable for wlroots based compositor. The list of available ones is on the wlroots documentation.

## Specifying the primary graphics cards on wlroot based compositor
If your device has Hybrid graphics , then you can use  environment variable to specifies primary graphics cards according to the wlroots documentation

Example:

 WLR_DRM_DEVICES='/dev/dri/card1:/dev/dri/card2:/dev/dri/card0'

## Remote display
*  and  (used by sway) offers a VNC backend via  since version 0.10. RDP backend has been removed *  has now remote desktop enabled at compile time, see [https://wiki.gnome.org/Projects/Mutter/RemoteDesktop and  for details.
*  offers a VNC server for .  can be used to set up another device as an extra monitor.
* There was a merge of FreeRDP into Weston in 2013, enabled via a compile flag. The  package has it enabled since version 6.0.0.
*  is a transparent proxy for Wayland applications, with a wrapper command to run over SSH
** Here is an example for launching a remote KDE kcalc under Plasma:
::

## Troubleshooting
First, make sure that your current session is running under Wayland instead of X11 (many compositors support both).
This can be done by examining the  environment variable (it should begin with ), and/or checking that  is .

For (possibly) application-related issues, consider also checking whether the application is running under XWayland.

## Useful tools
*  from : displays information about the current compositor.
* : for debugging Wayland events on a Wayland window, analagous to the X11 tool xev.
* : Wayland output power management for compositors that support the wlr output power management protocol.
* : Manages outputs of Wayland compositors that support the wlr output management protocol.

## Color correction
See Backlight#Color correction.

## GNOME: Slow motion, graphical glitches, and crashes
Gnome-shell users may experience display issues when they switch to Wayland from X. One of the root cause might be the  set by yourself for Xorg-based gnome-shell. Just try to remove it from  or other rc files to see if everything goes back to normal.

## Input grabbing in games, remote desktop and virtual machine windows
In contrast to Xorg, Wayland does not allow exclusive input device grabbing, also known as active or explicit grab (e.g. keyboard, mouse), instead, it depends on the Wayland compositor to pass keyboard shortcuts and confine the pointer device to the application window.

This change in input grabbing breaks current applications' behavior, meaning:

* Hotkey combinations and modifiers will be caught by the compositor and will not be sent to remote desktop and virtual machine windows.
* The mouse pointer will not be restricted to the application's window which might cause a parallax effect where the location of the mouse pointer inside the window of the virtual machine or remote desktop is displaced from the host's mouse pointer.

Wayland solves this by adding protocol extensions for Wayland and Xwayland. Support for these extensions is needed to be added to the Wayland compositors. In the case of native Wayland clients, the used widget toolkits (e.g GTK, Qt) needs to support these extensions or the applications themselves if no widget toolkit is being used. In the case of Xorg applications, no changes in the applications or widget toolkits are needed as the Xwayland support is enough.

These extensions are already included in , and supported by .

The related extensions are:

* Xwayland keyboard grabbing protocol
* Compositor shortcuts inhibit protocol
* Relative pointer protocol
* Pointer constraints protocol

Supporting Wayland compositors:

* Mutter, GNOME's compositor since release 3.28
* wlroots supports relative-pointer and pointer-constraints
* Kwin
** KDE#X11 shortcuts conflict on Wayland
** Keyboard shortcuts inhibit

Supporting widget toolkits:

* GTK since release 3.22.18.

## GTK themes not working
See https://github.com/swaywm/sway/wiki/GTK-3-settings-on-Wayland.

## Avoid loading NVIDIA modules
Add  as environment variable before launching a Wayland compositor like sway.

## Magnifying/surface scaling
Screen magnifying is not solved yet, a pull request was merged mid-2022 providing the protocol wp-surface-scale.

## Wayland lag/stuttering since kernel 6.11.2 (AMD)
Until this issue is patched in future kernel releases, a workaround is to add  to the cmdline.

See: https://community.frame.work/t/wayland-lag-stuttering-since-kernel-6-11-2/59422

## Games / applications suspended when changing a virtual desktop
When changing workspace or using , games (and possibly other graphical applications) are suspended, put in some weird state, and they (partially) stop. This includes VRR applications and applications with VSync turned on but is not limited to them only. Symptoms include things like audio dropping (partially) out, game not progressing, ping times rising high or network dropping out, but only if the game window is not in focus. This may only affect applications with VSync on.

It is possible some games can work around this issue by changing to a window, but some do not. This is extremely annoying in more complex games which require heavy usage of web browsing, documentation and 3rd party tools or if the gameplay is interrupted for some reason.

Possible workaround include setting environment variables  and/or , but setting these will break any VSync or VRR implementations.
