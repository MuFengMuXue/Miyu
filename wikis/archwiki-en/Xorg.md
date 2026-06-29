# Xorg

X.Org Server — commonly referred to as simply X — is the X.Org Foundation implementation of the X Window System (X11) display server, and it is the most popular display server among Linux users. Its ubiquity has led to making it an ever-present requisite for GUI applications, resulting in massive adoption from most distributions.

For the alternative and successor, see Wayland.

## Installation
Xorg can be installed with the  package.

Additionally, some packages from the  group are necessary for certain configuration tasks. They are pointed out in the relevant sections.

Finally, an  group is also available, which includes Xorg server packages, packages from the  group and fonts.

## Drivers
See Graphics processing unit#Installation to identify your hardware and choose the driver for it.

Hardware-specific Device Dependent X (DDX) drivers are considered legacy: there is a generic  DDX driver in , which uses kernel mode setting and works well on modern hardware. The modesetting DDX driver uses Glamorfor 2D acceleration, which requires OpenGL.

If you want to install another DDX driver, note that Xorg searches for installed DDX drivers automatically:

* If it cannot find the specific driver installed for the hardware (listed in Graphics processing unit#Installation), it first searches for fbdev (), which does not include any 2D or 3D acceleration.
* If that is not found, it searches for vesa (), the generic driver, which handles a large number of chipsets but does not include any 2D or 3D acceleration.
* If vesa is not found, Xorg will fall back to  DDX driver.

## Running
The  command is usually not run directly. Instead, the X server is started with either a display manager or xinit.

## Configuration
Xorg uses a configuration file called  and files ending in the suffix  for its initial setup: the complete list of the folders where these files are searched can be found in , together with a detailed explanation of all the available options.

## Using .conf files
The  directory stores host-specific configuration. You are free to add configuration files there, but they must have a  suffix: the files are read in ASCII order, and by convention their names start with  (two digits and a hyphen, so that for example 10 is read before 20). These files are parsed by the X server upon startup and are treated like part of the traditional  configuration file. Note that on conflicting configuration, the file read last will be processed. For this reason, the most generic configuration files should be ordered first by name. The configuration entries in the  file are processed at the end.

For option examples to set, see Fedora:Input device configuration#xorg.conf.d.

## Using xorg.conf
Xorg can also be configured via  or . You can also generate a skeleton for  with:

 # Xorg :0 -configure

This should create a  file in  that you can copy over to .

Alternatively, your proprietary video card drivers may come with a tool to automatically configure Xorg: see the article of your video driver, NVIDIA, for more details.

## Input devices
For input devices the X server defaults to the libinput driver (), but  and related drivers are available as alternative.[https://archlinux.org/news/xorg-server-1191-is-now-in-extra/

Udev, which is provided as a systemd dependency, will detect hardware and both drivers will act as hotplugging input driver for almost all devices, as defined in the default configuration files  and  in the  directory.

After starting X server, the log file will show which driver hotplugged for the individual devices (note the most recent log file name may vary):
 $ grep -e "Using input driver " Xorg.0.log

If both do not support a particular device, install the needed driver from the  group. The same applies, if you want to use another driver.

To influence hotplugging, see #Configuration.

For specific instructions, see also the libinput article, the following pages below, or Fedora:Input device configuration for more examples.

## Input identification
See Keyboard input#Identifying keycodes in Xorg.

## Mouse acceleration
See Mouse acceleration.

## Extra mouse buttons
See Mouse buttons.

## Touchpad
See  libinput or Synaptics.

## Touchscreen
See Touchscreen.

## Keyboard settings
See Keyboard configuration in Xorg.

## Monitor settings
## Manual configuration
For a headless configuration, the  driver is necessary; install it and create a configuration file, such as the following:

## Multiple monitors
See main article Multihead for general information.

## More than one graphics card
You must define the correct driver to use and put the bus ID of your graphic cards (in decimal notation).

To get your bus IDs (in hexadecimal):

The bus IDs here are  and .

## Display size and DPI
By default, Xorg always sets DPI to 96 since 2009-01-30. A change was made with version 21.1 to provide proper DPI auto-detection, but reverted.

The DPI of the X server can be set with the  command line option.

Having the correct DPI is helpful where fine detail is required (like font rendering). Previously, manufacturers tried to create a standard for 96 DPI (a 10.3" diagonal monitor would be 800x600, a 13.2" monitor 1024x768). These days, screen DPIs vary and may not be equal horizontally and vertically. For example, a 19" widescreen LCD at 1440x900 may have a DPI of 89x87.

To see if your display size and DPI are correct:

 $ xdpyinfo | grep -B2 resolution

Check that the dimensions match your display size.

If you have specifications on the physical size of the screen, they can be entered in the Xorg configuration file so that the proper DPI is calculated (adjust identifier to your xrandr output):

If you only want to enter the specification of your monitor without creating a full xorg.conf, create a new configuration file. For example ():

If you do not have specifications for physical screen width and height (most specifications these days only list by diagonal size), you can use the monitor's native resolution (or aspect ratio) and diagonal length to calculate the horizontal and vertical physical dimensions. Using the Pythagorean theorem on a 13.3" diagonal length screen with a 1280x800 native resolution (or 16:10 aspect ratio):

 $ echo 'scale=5;sqrt(1280^2+800^2)' | bc  # 1509.43698

This will give the pixel diagonal length, and with this value you can discover the physical horizontal and vertical lengths (and convert them to millimeters):

 $ echo 'scale=5;(13.3/1509)*1280*25.4' | bc  # 286.43072
 $ echo 'scale=5;(13.3/1509)*800*25.4'  | bc  # 179.01920

## Setting DPI manually
For RandR compliant drivers (for example the open source ATI driver), you can set it by:

 $ xrandr --dpi 144

To make it permanent, see Autostarting#On Xorg startup.

## Proprietary NVIDIA driver
You can manually set the DPI by adding the option under the  or  section:
 Option              "DPI" "96 x 96"

## Manual DPI Setting Caveat
GTK very often overrides the server's DPI via the optional X resource . To find out whether this is happening to you, check with:

 $ xrdb -query | grep dpi

With GTK library versions since 3.16, when this variable is not otherwise explicitly set, GTK sets it to 96. To have GTK apps obey the server DPI you may need to explicitly set  to the same value as the server. The  resource is the method by which some desktop environments optionally force DPI to a particular value in personal settings. Among these are KDE and TDE.

## Display Power Management
DPMS is a technology that allows power saving behaviour of monitors when the computer is not in use. This will allow you to have your monitors automatically go into standby after a predefined period of time.

## Composite
The Composite extension for X causes an entire sub-tree of the window hierarchy to be rendered to an off-screen buffer. Applications can then take the contents of that buffer and do whatever they like. The off-screen buffer can be automatically merged into the parent window, or merged by external programs called compositing managers. For more information, see Wikipedia:Compositing window manager.

Some window managers (e.g. Compiz, Enlightenment, KWin, , , , , Xfwm) do compositing on their own. For other window managers, a standalone composite manager can be used.

## List of composite managers
*
*
*
*
*

## Tips and tricks
## Automation
This section lists utilities for automating keyboard / mouse input and window operations (like moving, resizing or raising).

{| class="wikitable"
! Tool !! Package !! Manual !! Keysyminput !! Windowoperations !! Note
|-
! xautomation
|  ||  ||  ||  || Also contains screen scraping tools. Cannot simulate  and more.
|-
! xdo
|  ||  ||  ||  || Small X utility to perform elementary actions on windows.
|-
! xdotool
|  ||  ||  ||  || Very buggy and not in active development, e.g: has broken CLI parsing.|-
! xvkbd
|  ||  ||  ||  || Virtual keyboard for Xorg, also has the  option for sending characters.
|-
! AutoKey
|   || [https://github.com/autokey/autokey#documentation documentation ||  ||  || Higher-level, powerful macro and scripting utility, with both Qt and Gtk front-ends.
|}

See also Clipboard#Tools and an overview of X automation tools.

## Nested X session
To run a nested session of another desktop environment:

 $ /usr/bin/Xnest :1 -geometry 1024x768+0+0 -ac -name Windowmaker & wmaker -display :1

This will launch a Window Maker session in a 1024 by 768 window within your current X session.

This needs the package  to be installed.

A more modern way of doing a nested X session is with Xephyr.

## Starting an application without a window manager
See xinit#Starting applications without a window manager.

## Starting GUI programs remotely
See main article: OpenSSH#X11 forwarding.

## On-demand disabling and enabling of input sources
With the help of xinput you can temporarily disable or enable input sources. This might be useful, for example, on systems that have more than one mouse, such as the ThinkPads and you would rather use just one to avoid unwanted mouse clicks.

Install the  package.

Find the name or ID of the device you want to disable:

 $ xinput

For example in a Lenovo ThinkPad T500, the output looks like this:

Disable the device with , where device is the device ID or name of the device you want to disable. In this example we will disable the Synaptics Touchpad, with the ID 10:

 $ xinput --disable 10

To re-enable the device, just issue the opposite command:

 $ xinput --enable 10

Alternatively using the device name, the command to disable the touchpad would be:

 $ xinput --disable "SynPS/2 Synaptics TouchPad"

## Persistently disable input source
You can disable a particular input source using a configuration snippet:

 is an arbitrary name, and  is the name of the input driver, e.g. .  is what is actually used to match the proper device. For alternate methods of targeting the correct device, such as libinput's , consult your input driver's documentation. Though this example uses libinput, this is a driver-agnostic method which simply prevents the device from being propagated to the driver.

## Killing application with hotkey
Run script on hotkey:

 #!/bin/sh
 windowFocus=$(xdotool getwindowfocus)
 pid=$(xprop -id "$windowFocus" | grep PID)
 kill -9 "$pid"

Dependencies: ,

See also #Killing an application visually.

## Block TTY access
To block tty access when in an X add the following to xorg.conf:

This can be used to help restrict command line access on a system accessible to non-trusted users.

## Prevent a user from killing X
To prevent a user from killing X when it is running add the following to xorg.conf:

## Killing an application visually
When an application is misbehaving or stuck, instead of using  or  from a terminal and having to find the process ID or name,  allows to click on said application to close its connection to the X server. Many existing applications do indeed abort when their connection to the X server is closed, but some can choose to continue.

## Rootless Xorg
Xorg may run with standard user privileges instead of root (so-called "rootless" Xorg). This is a significant security improvement over running as root. Note that some popular display managers do not support rootless Xorg (e.g. LightDM or XDM).

You can verify which user Xorg is running as with .

See also , , Systemd/User#Xorg as a systemd user service, Fedora:Changes/XorgWithoutRootRights and .

## Using xinitrc
To configure rootless Xorg using xinitrc:

* Run startx as a subprocess of the login shell; run  directly and do not use .
* Ensure that Xorg uses virtual terminal for which permissions were set, i.e. passed by logind in  via .xserverrc.
* If using certain proprietary display drivers, kernel mode setting auto-detection will fail. In such cases, you must set  in .

Note that executing  directly without  leaves the shell open in the case of a xorg crash. Since some lock screens are executed inside xorg, this can lead to full access to the executing user.

## Using GDM
GDM will run Xorg without root privileges by default when kernel mode setting is used.

## Session log redirection
When Xorg is run in rootless mode, Xorg logs are saved to . However, the stdout and stderr output from the Xorg session is not redirected to this log. To re-enable redirection, start Xorg with the  flag and redirect the stdout and stderr output to a file:

 startx -- -keeptty >~/.xorg.log 2>&1

Alternatively, copy  to , and append . See === Xorg as Root ===

As explained above, there are circumstances in which rootless Xorg is defaulted to. If this is the case for your configuration, and you have a need to run Xorg as root, you can configure  to require root:

## Wayback
Wayback is an X11 compatibility layer which allows for running full X11 desktop environments (and window managers) using Wayland components. It's available from the AUR as  package.

## 12to11
12to11 allows you to seamlessly run Wayland-only applications under X11. It's available from the AUR as . Run with the EGL renderer for best performance:

 $ RENDERER=egl 12to11

## Troubleshooting
## General
If a problem occurs, view the log stored in either  or, for the rootless X default since v1.16, in . GDM users should check the systemd journal. [https://bbs.archlinux.org/viewtopic.php?id=184639

The logfiles are of the form  with  being the display number. For a single user machine with default configuration the applicable log is frequently , but otherwise it may vary. To make sure to pick the right file it may help to look at the timestamp of the X server session start and from which console it was started. For example:

* In the logfile then be on the lookout for any lines beginning with , which represent errors, and also , which are warnings that could indicate other issues.
* If there is an empty  file in your , either delete or edit it in order for X to start properly. If you do not do this X will show a blank screen with what appears to be no errors in your . Simply deleting it will get it running with a default X environment.
* If the screen goes black, you may still attempt to switch to a different virtual console (e.g. ), and blindly log in as root. You can do this by typing  (press  after typing it) and entering the root password (again, press  after typing it).

: You may also attempt to kill the X server with:
:
: If this does not work, reboot blindly with:
:

* Check specific pages in Input devices if you have issues with keyboard, mouse, touchpad etc.
* Search for common problems in AMDGPU, Intel and NVIDIA articles.

## Black screen, No protocol specified, Resource temporarily unavailable for all or some users
X creates configuration and temporary files in current user's home directory. Make sure there is free disk space available on the partition your home directory resides in. Unfortunately, X server does not provide any more obvious information about lack of disk space in this case.

## DRI with Matrox cards stopped working
If you use a Matrox card and DRI stopped working after upgrading to Xorg, try adding the line:

 Option "OldDmaInit" "On"

to the  section that references the video card in .

## Frame-buffer mode problems
X fails to start with the following log messages:

To correct, uninstall the  package.

## Program requests "font '(null)'"
Error message: .

Some programs only work with bitmap fonts. Two major packages with bitmap fonts are available,  and . You do not need both; one should be enough. To find out which one would be better in your case, try  from , like this:

 $ xdpyinfo | grep resolution

and use what is closer to the shown value.

## Recovery: disabling Xorg before GUI login
If Xorg is set to boot up automatically and for some reason you need to prevent it from starting up before the login/display manager appears (if the system is wrongly configured and Xorg does not recognize your mouse or keyboard input, for instance), you can accomplish this task with two methods.

* Change default target to . See systemd#Change default target to boot into.
* If you have not only a faulty system that makes Xorg unusable, but you have also set the GRUB menu wait time to zero, or cannot otherwise use GRUB to prevent Xorg from booting, you can use the Arch Linux live CD. Follow the installation guide about how to mount and chroot into the installed Arch Linux. Alternatively try to switch into another tty with  + function key (usually from  to  depending on which is not used by X), login as root and follow steps below.

Depending on setup, you will need to do one or more of these steps:

* Disable the display manager.
* Disable the automatic start of X.
* Rename the  or comment out the  line in it.

## X clients started with "su" fail
If you are getting , try adding the line:

 session        optional        pam_xauth.so

to  and .  will then properly set environment variables and handle  keys.

## X failed to start: Keyboard initialization failed
If the filesystem (specifically ) is full,  will fail. The log file will contain:

Make some free space on the relevant filesystem and X will start.

## A green screen whenever trying to watch a video
Your color depth is set wrong. It may need to be 24 instead of 16, for example.

## SocketCreateListener error
If X terminates with error message , you may need to delete socket files in . This may happen if you have previously run Xorg as root (e.g. to generate an ).

## Invalid MIT-MAGIC-COOKIE-1 key when trying to run a program as root
That error means that only the current user has access to the X server. The solution is to give access to root:

 $ xhost +si:localuser:root

That line can also be used to give access to X to a different user than root.
