# Multihead

Multi-head, multi-screen, multi-display or multi-monitor represent setups with multiple display devices attached to a single computer. This article provides a general description for several multi-head setup methods, and provides some configuration examples.

## Historical background
X Window System (X, X11) is the underlying graphical user interface (GUI) for most Unix/Linux computers that provide one. It was developed in 1984 at MIT. After about 35 years of development, tweaks, new features and ideas, it is generally acknowledged to be a bit of a beast. During the time of early development, the common configuration was a single running X that provided individual views to Xterminals on a time-sharing system. Today, X typically provides a single screen on a desktop or laptop.

In short, there are many ways to configure GUIs using X. When using modern versions, sometimes you can even get away with limited or no configuration. In the last few years, the boast is that X is self-configuring. Certainly, a good rule of thumb is that less configuration is better - that is, only configure what the defaults got wrong.

## RandR
RandR (Rotate and Resize) is an X Window System extension, which allows clients to dynamically change (e.g. resize, rotate, reflect) screens. In most cases, it can fully replace the old Xinerama setup. See an explanation why RandR is better than Xinerama.

RandR can be configured for the current session via the xrandr tool, arandr or persistently via an xorg.conf file.

## Configuration using xrandr
You may arrange your screens either relatively to each other (using the , , ,  options), or by absolute coordinates (using the  option; note that in this case you usually need to know resolutions of your monitors). See  for details. Some frequently used settings are described below.

## VGA1 left of HDMI1 at their preferred resolutions
 $ xrandr --output VGA1 --auto --output HDMI1 --auto --right-of VGA1

 places the previous screen () to the right of the specified screen ().

## VGA1 right of HDMI1 at fixed resolutions
 $ xrandr --output VGA1 --mode 1024x768 --pos 1920x0 --output HDMI1 --mode 1920x1080 --pos 0x0

or

 $ xrandr --output VGA1 --mode 1024x768 --output HDMI1 --mode 1920x1080 --left-of VGA1

 places the previous screen () to the left of the specified screen ().

## Combine screens into virtual display
Since randr version 1.5, it has been possible to combine monitors into one virtual display. This is an updated version of what was possible with Xinerama and works with open source drivers and does not require an Xorg restart. Some desktop environments do not support this feature yet. Openbox has been tested and works with this feature.

Get monitor list by doing

 0: +*DisplayPort-4 1920/518x1200/324+1920+0  DisplayPort-4
 1: +DisplayPort-3 1920/518x1200/324+0+0  DisplayPort-3
 2: +HDMI-A-0 1920/518x1200/324+3840+0  HDMI-A-0

Create virtual display .  determines the size of the virtual display, setting this to auto will automatically create the correct size of the display array. Monitor order in this command does not matter and the monitors need to be rearranged correctly after or before this command is executed.

For a more detailed explanation see this page.

## Configuration using xorg.conf
This is similar to using xrandr, separate  section is needed for each screen. As an , the same value as reported by  is used (i.e.  is used instead of ).

## Example: dualhead configuration using relative coordinates
## Example: dualhead configuration using relative coordinates with custom resolutions
The ID for each monitor can be found by running the  command and should be defined as  inside the  section.

See Xrandr#Adding undetected resolutions.

## Example: dualhead configuration using absolute coordinates
There are no negative coordinates, the setup's leftmost and highest possibly targeted point is at 0,0

## Dynamic display configuration
The following options allow you to automatically detect when a new display is connected and then change the layout based on that. This can be useful for laptop users who frequently work in multiple different environments that require different setups.

*  allows you to save your current xrandr configuration as profiles based on what display hardware is connected.
*  or  is a shell script to quickly manage 2-monitors display using xrandr.

## Separate screens
This is the original way of configuring multiple monitors with X, and it has been around for decades.  Each physical monitor is assigned as an X screen, and while you can move the mouse between them, they are more or less independent.

Normally the X display has a single identifier such as , set in the  environment variable; but in this configuration, each screen has a different  value.  The first screen is , the second is  and so on.

With this configuration, it is not possible to move windows between screens, apart from a few special programs like GIMP and Emacs, which have multi-screen support.  For most programs, you must change the  environment variable when launching to have the program appear on another screen:

 # Launch a terminal on the second screen
 $ DISPLAY=:0.1 urxvt &

Alternatively, if you have a terminal on each screen, launching programs will inherit the  value and appear on the same screen they were launched on.  But, moving an application between screens involves closing it and reopening it again on the other screen.

Working this way does have certain advantages. For example, windows popping up on one screen will not steal the focus away from you if you are working on another screen - each screen is quite independent.

## TwinView
TwinView is NVIDIA's extension which makes two monitors attached to a video card appear as a single screen.  TwinView provides Xinerama extensions so that applications are aware there are two monitors connected, and thus it is incompatible with Xinerama.  However, if you only have two monitors and they are both connected to the same NVIDIA card, there is little difference between TwinView and Xinerama (although in this situation TwinView may offer slightly better performance.)

If you wish to attach more than two monitors or monitors attached to other video cards, you will need to use Xinerama instead of TwinView. Likewise, as of April 2012, both monitors must be in the same orientation - you cannot have one in landscape and the other in portrait mode.

In the past, TwinView was the only way to get OpenGL acceleration with NVIDIA cards while being able to drag windows between screens.  However modern versions of the NVIDIA closed-source driver are able to provide OpenGL acceleration even when using Xinerama.

See NVIDIA#TwinView for an example configuration.

## Xinerama
Xinerama is the old way of doing genuine multihead X. Xinerama combines all monitors into a single screen () making it possible to drag windows between screens.

Xinerama is configured via custom X configuration files. There is also a GUI tool named WideGuy to make toggling Xinerama easier. Note that to use WideGuy you still need an Xorg configuration with a ServerLayout section.

Here are some X configuration examples:

This is a ServerLayout section which controls where each monitor sits relative to the others.

Each Screen in the above section is defined in a separate file, such as this one:

You will need to create a  section for each monitor, i.e. a dual head video card will have two Device sections.  The following example shows how to configure two video cards each providing two outputs, for a total of four monitors.
