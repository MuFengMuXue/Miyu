# DisplayLink

DisplayLink is a technology for connecting displays using USB and Wi-Fi.

DisplayLink devices on Linux still only have experimental support. While some people have had success in using them, it is generally not an easy process and not guaranteed to work. The steps on this page describe the generally most successful methods of using external monitors with DisplayLink.

Also be warned that even over USB 3.0, a DisplayLink monitor may exhibit noticeably more lag than e.g. a DisplayPort monitor, especially when large portions of the screen are being redrawn.

## Installation
## USB 2.0 DL-1x5, DL-1x0 Devices
The kernel DRM driver for DisplayLink is , a rewrite of the original udlfb driver. It allows configuring DisplayLink monitors using xrandr.

This should work without any configuration changes on  4.14.9-1 and later. If you are using an earlier version of that package or have  set in your kernel config, you need to blacklist the old kernel module, , which may attempt to load itself first.

## USB 3.0 DL-6xxx, DL-5xxx, DL-41xx, DL-3xxx Devices
# Install  for the kernel module (after configuring DKMS). As stated on the DKMS page, don't forget to install the appropriate header packages for your kernel (e.g.  for the regular  kernel) or else nothing will happen. If you encounter issues, there is the development version.
# Install the  driver. For Xorg it allows configuring DisplayLink monitors using xrandr in the same manner as the  driver; for Wayland no configuration is necessary.
# Enable .

Furthermore, for Xorg use the "modesetting" driver with AccelMethod "none" and MatchDriver "evdi". To achieve that, create a file with the following content:

A reboot may be required for the setting to be effective. After reboot, see if the Displaylink screens are displaying in your display settings. If not, continue on the next steps, which will attach the DVI-I inputs to your GPU.

## Setting up X Displays
After that, run:

In the above output, we can see that provider 0 is the system's regular graphics provider (Intel), and provider 1 (modesetting) is the DisplayLink provider. To use the DisplayLink device, connect provider 1 to provider 0:

 $ xrandr --setprovideroutputsource 1 0

and xrandr will add a DVI output you can use as normal with xrandr. This is still experimental but supports hotplugging and when works, it is by far the simplest setup. If it works then everything below is unnecessary.

## Configuration
These instructions assume that you already have an up and running X server and are simply adding a monitor to your existing setup.

## Load the framebuffer device
Before your system will recognize your DisplayLink device, the  kernel module must be loaded. To do this, run

 # modprobe udl

If your DisplayLink device is connected, it should show some visual indication of this. Although a green screen is the standard indicator of this, other variations have been spotted and are perfectly normal. Most importantly, the output of dmesg should show something like the following, indicating a new DisplayLink device was found:

Furthermore,  should contain a new  device, likely  if you already had a framebuffer for your primary display.

Instead of loading  manually, you can load the module at boot.

## Configuring X Server
Use  or your desktop environment's display setup graphical interface to configure your USB monitors running either the  or  driver.

## xrandr
Once the driver is loaded, the DisplayLink monitor is listed as an output provider:

In the above example, provider 1 is the DisplayLink device, and provider 0 is the default display. Running  gives a list of available screens:

If the above does not list the DisplayLink screen, then you will need to offload DisplayLink to the main GPU:

 $ xrandr --setprovideroutputsource 1 0

Once the screen is available, refer to xrandr for info on setting it up. For automating the configuration process, see displaylink.sh.

## Enabling DVI output on startup
The DisplayLink provider will not be automatically connected to the main provider in most cases, therefore the DVI output device will not be available. It can be helpful to automatically do this when X starts to facilitate automatic display configuration by the window manager.

Edit your desktop manager's startup configuration and add commands similar to:

 $(xrandr --listproviders | grep -q "modesetting") && xrandr --setprovideroutputsource 1 0

For example, the appropriate startup configuration file for SDDM is .

Avoid placing these commands in  as this breaks the display configuration of some window managers. Instead these commands should be run prior to any display output or setup.

## Switching between displaylink and NVIDIA/nouveau driver
As of displaylink version 1.3.54-1 it is not possible to use displaylink device and NVIDIA/nouveau driver simultaneously on Optimus based laptops.
Currently to be able to use displaylink device on Intel GPU, you should create a configuration file (see #Troubleshooting below). However, with that configuration file it is not possible to use primusrun. Bumblebee service is running, but it cannot work. Also, the laptop fans are becoming very noisy and the laptop temperature becomes very high. When you want to switch back to activate NVIDIA driver, comment everything in that file and reboot.

To simplify process of switching, you can install  and add an additional menu entry to your boot loader using the kernel parameter , thus activating displaylink workaround.

To check which driver is used for your discrete video card, run  (replace xx:xx.x with your NVIDIA GPU PCI id).

## Troubleshooting
## Not working configuration
These are tested on Xfce using Display settings (included in XFCE4 package) and external tool - . XFCE4 Display settings are likely to crash, so ARandR might help.

When you connect display link device via USB to your computer, the computer should show monitors in Display settings. There are few troubleshooting steps that you should try:

* Check #Setting up X Displays. If you cannot find any external monitors recognized, you should try to make them visible by some of the following commands:  This will make them visible and recognized in Display settings.
* Restart .
* Re-connect the USB cable.
* Check if  driver is loaded and monitors are connected.

## Screen redraw is broken
If you are using  as your kernel driver and the monitor appears to work, but is only updating where you move the mouse or when windows change in certain places, then you probably have the wrong modeline for your screen. Getting a proper modeline for your screen with a command like:

 $ gtf 1366 768 59.9

where  and  are the horizontal and vertical resolutions for your monitor, and  is the refresh rate from its specs. To use this, create a new mode with  like follows:

 $ xrandr --newmode "1368x768_59.90"  85.72  1368 1440 1584 1800  768 769 772 795  -HSync +Vsync

and add it to xrandr:

 $ xrandr --addmode DVI-0 1368x768_59.90

Then tell the monitor to use that mode for the DisplayLink monitor, and this should fix the redraw issues. Check the xrandr page for information on using a different mode.

If this does not solve the problem (or if the correct modeline was already in place because of correct DDC data), it can help to run a compositor.

## Ghosting
If you experience ghosting caused by moving the cursor around, it might happen that your compositor configuration is causing the problem. Changing settings may give you a working setup, such as turning off your compositor on start up can resolve it.

Users have reported that logging out and logging in (to refresh the display manager) corrects the issue temporarily. A longer lasting solution can be implemented into your system by doing the following:

Delaying by 10 seconds seems to work for some users, but a shorter sleep is likely possible to implement. Users report turning off autologin fixes the issue in GNOME.

Additionally, it can possibly be fixed by enabling or disabling Zoom in Accessibility. Users report turning it off fixed it, while others report turning it on sometimes fixed it (with scaling set to 1.0).

## DisplayLink refresh rate is extremely slow with GNOME
If once you set up your DisplayLink your entire desktop becomes slow, try setting a "simpler" background image, such as complete black. Additionally, there have been reports since 2019 that rotated Displaylink screens are inherently laggy, so see if setting the monitor to normal orientation corrects the issue as well.

## All displays are capped to 1 FPS when disabling builtin screen
Applying the patch from https://gitlab.freedesktop.org/xorg/xserver/-/issues/1028#note_504826 to  seems to fix the problem.

## Slow redraw/Unresponsiveness in Google Chrome and Webkit2-based Applications
This is to be associated with bugs in hardware acceleration, which can be tested by running glxgears in the displaylink screen resulting in 1fps. There is currently no complete fix available, but turning off Hardware-Acceleration in affected applications can work as a temporary fix.

This can be done in applications without a hardware-acceleration option by prepending the  environment variable.

## Impossible to activate displaylink's screen
In case you are able to see attached monitor via DisplayLink device in your screen settings, but after you turn it on and apply settings, it becomes deactivated, then try blacklist nouveau module and reboot:

## Suspend problem
Displaylink is not working after suspend. Unplug and then plug again displaylink's usb cable to your computer. Monitor that is connected via DisplayLink will remain black. If you have lock screen, login to the system and then picture will appear at that monitor and you will be able to use displaylink as normal.

## DisplayLink is not working when usb hot plugged
To be able to use DisplayLink monitors, its usb cable should be attached to laptop during boot time. Otherwise it can behave like they are available and mouse can be moved there, but its picture is frozen, even with correct configuration (see workaround 1). If it was not attached at boot time, attach it and reboot.

## DisplayLink driver does not work with Intel GPUs after recent X upgrades
As this support page says, upgrading the X Window Server to a version newer than 1.18.3 will make the system not compatible with DisplayLink by default. This applies to systems using an integrated Intel GPU, or a combination of integrated Intel GPU and a discrete GPU.
Until fixes in X Windows System will be released, there are two workarounds:

## Using the older intel driver as a fallback
Use the "intel" driver for the integrated GPU instead of "modesetting", which is now the default.

Create a file with the following content:

A reboot is required for the setting to be effective.

You may need the  package.

## Temporarily disabling PageFlip for modesetting
For users that prefer to keep using "modesetting" driver, disabling page flipping should also help.
Create a file with the following content or extend the  option to an existing configuration file (e.g. ):

## Displays disconnect at random intervals when using the Dell D6000 docking station
User's have reported that when using the Dell D6000 docking station, their display(s) may disconnect at random intervals during usage. This will require physically reconnecting the dock in order to reinitialise the displays.

This issue appears to be caused by PulseAudio's  module, which automatically suspends sinks/sources on idle.

To disable loading of the  module, comment out the following line in the configuration file in use ( or ):

## Only 1 Display is recognized after boot
In case multiple displays are connected to a DisplayLink Docking station, but only 1 is recognized after bootup, a possible fix is to force evdi to search for multiple displays at boot by adding the  module to  and  to

## DisplayLink and NVIDIA dGPU on X11 (Optimus+DL)
If a laptop using NVIDIA Optimus is in a more permanent setting (using X11), it is nice to permanently set video outputs to use the dGPU.  might produce the following:

Even after installing both  and  packages, the DisplayLink connected displays still might not appear. Manually, we can instruct Xorg to use the  plugin with the video interface given by the  driver.

Identify which DRI device. The easiest way to identify which device is to list all DRI devices by their path:

As you can see, the first  device is .

Add the following to the Xorg config:

Restart the X server to see changes.

The DL displays should appear. Configure using xrandr as necessary.

## USB 2.0 DisplayLink is not working
 is quite finicky. Some USB 2 devices work with it, some do not. As an example, the HP NL571AA,Lenovo LT1421 wide has been tested to work. If your USB 2.0 device is not working with  (for example the EVGA "UV PLUS+16"), you will get the following error in your journal :

## Monitor in vertical orientation cuts off at bottom
A DisplayLink-connected monitor display in vertical orientation could cut off at the bottom in an unusable dead, black area. This may be caused by  loading ahead of the  driver and taking over the DisplayLink connection, leaving  unused. Blacklisting  to let  handle the DisplayLink connection may restore the display to normal.

You can check whether the DisplayLink connection is being configured by  by stopping  and seeing if the DisplayLink monitor stops working. If this causes the screen to go dark and undetected by , the DisplayLink connection is being controlled by  and  is not the issue.

However, if stopping  makes no change in the DisplayLink display and  shows  to be loaded, then it may be that  has loaded ahead of  to handle the DisplayLink connection and a  incompatibility is causing the display issue.

Blacklist  and regenerate the initramfs.

On reboot, check the status of ,  and :

If  is not loaded,  is loaded, and  is active, as in the above output, show detected monitors with  again. If the DisplayLink device appears in the output,  is handling the DisplayLink connection now and the name of the device may have changed. Use this new name, if any, to configure monitor settings and see if the display problem is solved.
