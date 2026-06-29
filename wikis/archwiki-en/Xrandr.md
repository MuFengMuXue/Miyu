# Xrandr

is an official configuration utility to the RandR (Resize and Rotate) X Window System extension. It can be used to set the size, orientation or reflection of the outputs for a screen. For configuring multiple monitors see the Multihead page.

## Installation
Install .

## Graphical front-ends
*
*

## CLI front-ends
*
*

## Testing configuration
When run without any option, xrandr shows the names of different outputs available on the system (, , etc.) and resolutions available on each, with a  after the current one and a  after the preferred one:

You can use xrandr to set different resolution (must be present in the above list) on some output:

 $ xrandr --output HDMI-1 --mode 1920x1080

When multiple refresh rates are present in the list, it may be changed by the  option, either at the same time or independently. For example:

 $ xrandr --output HDMI-1 --mode 1920x1080 --rate 60

The  option will turn the specified output on if it is off and set the preferred (maximum) resolution:

 $ xrandr --output HDMI-1 --auto

It is possible to specify multiple outputs in one command, e.g. to turn off  and turn on  with preferred resolution:

 $ xrandr --output HDMI-1 --off --output HDMI-2 --auto

## Configuration
xrandr is just a simple interface to the RandR extension and has no configuration file. However, there are multiple ways of achieving persistent configuration:

# The RandR extension can be configured via X configuration files, see Multihead#RandR for details. This method provides only static configuration.
# If you need dynamic configuration, you need to execute xrandr commands each time X server starts. See Autostarting#On Xorg startup for details. This method has the disadvantage of occurring fairly late in the startup process, thus it will not alter the resolution of the display manager if you use one.
# Custom scripts calling xrandr can be bound to events (for example when external monitor is plugged in), see udev or acpid for details. The #Scripts section provides you with some example scripts that might be useful for this purpose.

## Scripts
## Toggle external monitor
This script toggles between an external monitor (specified by ) and a default monitor (specified by ), so that only one monitor is active at a time.

The default monitor should be connected when running the script, which is always true for a laptop.

## Manage 2-monitors
 is a POSIX-compliant shell script to quickly manage 2-monitor displays.

It provides well-known modes like computer, duplicate, extend and projector mode as well as selecting and positioning one or two monitors among those plugged in (for more details, see mons).

## Avoid X crash with xrasengan
Use this workaround to turn on connected outputs that may be in suspend mode and hence shown as disconnected, as is often the case of DisplayPort monitors:

 is an xrandr wrapper with this workaround built in.

 $ xrasengan --force -on DisplayPort-0 -off HDMI-0

With the  option, xrasengan will update status of all outputs before HDMI-0 is turned off, avoiding an X crash if they were the only connected/active outputs.

To force reload current settings, xrasengan provides a  option, which uses  and unxrandr from the  package to assemble the command line:

 $ xrasengan --try-reload-active-layout

This can be used in systemd unit or in a keyboard binding to avoid blank screen when resuming DisplayPort monitors from suspend.

## Configuration using arandr
 can graphically arrange your monitors, change resolutions, and save a script to duplicate your setup. By default, if you "Save As" it will be saved in . These files can then be autostarted. Sometimes problems arise from running the arandr script too soon after login, add a  command if needed.

## Troubleshooting
## Screen blinking
For some LCD screens (e.g. Samsung 2343NW, Acer XB280HK and Iiyama ProLite XUB3490WQSU-B1) the command  can be used to calculate standardized modelines with reduced blanking, allowing for higher frequency signals.

For example: an external monitor ProLite XUB3490WQSU-B1 connected to a Dell laptop through a Thunderbolt-HDMI 2.0 adapter, using 59.97Hz refresh rate with a blinking problem:

Calculating the reduced modelines for the desired resolution 3440x1440 gives:

With this information we can use xrandr to create a new mode:

 $ xrandr --newmode "3440x1440R"  319.75  3440 3488 3520 3600  1440 1443 1453 1481 +hsync -vsync

And add it to the set of valid modes for the corresponding output to make it selectable:

 $ xrandr --addmode DP1 3440x1440R

## Adding undetected resolutions
Due to buggy hardware or drivers, your monitor's correct resolutions may not always be detected by xrandr. For example, the EDID data block queried from the monitor may be incorrect. To fix this at a low level, see Kernel mode setting#Forcing modes and EDID. This section will describe how to address this at a higher level by adding the desired resolutions to xrandr. This same procedure can be used to add refresh rates you know are supported, but not enabled by your driver.

First we run  or  to get the Modeline for the resolution we want:

Then we create a new xrandr mode. Note that the Modeline keyword needs to be omitted.

 $ xrandr --newmode "1280x1024_60.00"  109.00  1280 1368 1496 1712  1024 1027 1034 1063 -hsync +vsync

After creating it we need an extra step to add this new mode to our current output (VGA1). We use just the name of the mode, since the parameters have been set previously.

 $ xrandr --addmode VGA1 1280x1024_60.00

Now we change the resolution of the screen to the one we just added:

 $ xrandr --output VGA1 --mode 1280x1024_60.00

Note that these settings only take effect during this session. See Autostarting#On Xorg startup for a way to automatically apply them on startup.

If you are not sure about the resolution you will test, you may add a  and a safe resolution command line following, like this:

 $ xrandr --output VGA1 --mode 1280x1024_60.00 && sleep 5 && xrandr --newmode "1024x768-safe" 65.00 1024 1048 1184 1344 768 771 777 806 -HSync -VSync && xrandr --addmode VGA1 1024x768-safe && xrandr --output VGA1 --mode 1024x768-safe

Also, change  to correct output name.

## EDID checksum is invalid
If the previous method results in an  error during boot, see KMS#Forcing modes and EDID and Or  might give you the error . NVIDIA users should read NVIDIA/Troubleshooting#xrandr BadMatch.  could indicate an invalid EDID checksum. To verify that this is the case, run X in verbose mode (e.g. ) and check your Xorg log for messages about a bad EDID.

## Screen resolution reverts back after a blink
If you use GNOME and your monitor does not have an EDID, above #Adding undetected resolutions might not work, with your screen just blinking once, after .

Poke around with , or delete the file completely, and then reboot.

It is better explained in [https://unix.stackexchange.com/questions/184941/gnome-prevents-high-resolution-vga-without-edid-info-over-vga this article.

## Permanently adding undetected resolutions
Once a suitable resolution is found using , the mode can be permanently added by creating an entry in :

Replace  with the right driver, e.g. . When the X server is restarted, you should be able to set the new resolution.

If this does not work for you, try removing the Screen and Device sections and just leaving the Monitor section. === Resolution lower than expected ===

If your video card is recognized but the resolution is lower than you expect, you may try this.

Background: ATI X1550 based video card and two LCD monitors DELL 2408(up to 1920x1200) and Samsung 206BW(up to 1680x1050). Upon first login after installation, the resolution default to 1152x864. xrandr does not list any resolution higher than 1152x864. You may want to try editing /etc/X11/xorg.conf, add a section about virtual screen, logout, login and see if this helps. If not then read on.

Change xorg.conf

About the numbers: DELL on the left and Samsung on the right. So the virtual width is of sum of both LCD width 3600=1920+1680; Height then is figured as the max of them, which is max(1200,1050)=1200. If you put one LCD above the other, use this calculation instead: (max(width1, width2), height1+height2).

## Setting resolution from .xinitrc doesn't work
DDX drivers other than that of the  driver may take time to properly enumerate the modes of attached devices, to where xrandr may not work right away. This seems to be the case for the  driver, with which using xrandr early in the startup sets the incorrect resolution. Possible remedies include:

* Waiting for a couple of seconds before invoking xrandr:
{{hc|~/.xinitrc|
...
{ sleep 2; xrandr xrandr_parameters } &
...
}}
This does the waiting in the background, as to not block the rest of the startup. If this not desirable, e.g. your window manager configuration depends on the display being arranged correctly, you can execute the commands in the foreground:

* Setting the mode in a later part of the desktop startup. Refer to your window manager documentation for details on startup script functionality.
* Switching to the generic modesetting driver. This is most easily done by uninstalling the device specific DDX driver. In the case of , the driver has other deficiencies that may benefit from this; see Intel graphics#Installation for more information.

## Correction of overscan tv resolutions via the underscan property
With a flat panel TV, overscan looks like the picture is "zoomed in" so the edges are cut off.

Check your TV if there is a parameter to change. If not check if the output has support for the underscan property (xrandr --prop), if so apply an  and change border values.
The required  and  values can be different for you, just check it and change it by more or less.

 $ xrandr --output HDMI-0 --set underscan on --set "underscan vborder" 25 --set "underscan hborder" 40

## Correction of overscan tv resolutions via --transform
If underscan is not available another solution is using , which applies a transformation matrix on the output. See the  manual page for the explanation of the transformation.

For example, the transformation scaling horizontal coordinates by , vertical coordinates by  and moving the screen by 35 pixels right and 19 pixels down, is:

 $ xrandr --output HDMI1 --transform 0.80,0,-35,0,1.04,-19,0,0,1

## Disabling phantom monitor
In some cases, a non-existent monitor may be detected by the system. To disable it, find the name of the phantom output, e.g. VGA1, and turn it off with

 $ xrandr --output VGA1 --off

To make this permanent, add the following to an entry in :

## Dynamic interlace pattern artifacts with AOC G2590PX
If you are seeing very prominent [https://pcmonitors.info/reviews/aoc-g2590px/#Interlace_pattern_artifacts interlace pattern artifacts (mesh or grid) when you see movement on the screen with this monitor, it might be happening because of a low refresh rate. Switching to a higher refresh rate (from 60 Hz to 119.98 Hz and perhaps even higher) might help reduce the effect.

Sample xrandr output for this monitor over HDMI:
 HDMI-1 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 544mm x 303mm
    1920x1080     60.00 + 119.98*   99.93    50.00    59.94

As can be seen in the output above, the preferred refresh rate reported by xrandr is 60.00, but the artifacts are very visible with this refresh rate. Switching to 119.98 should help reduce the effect considerably.

 $ xrandr --output HDMI-1 --mode 1920x1080 --rate 119.98
