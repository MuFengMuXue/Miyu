# Via Technologies

The proprietary VIA drivers (xf86-video-via) are not available since 2008 as they are considered unstable and insecure. The unmaintained xf86-video-unichrome driver is not packaged since 2012 either.

## Installation
To get the OpenChrome driver, install the  package.

The  driver name is .

## Troubleshooting
To enable any of the following options to fix issues, first create a new file  in :

 Section "Device"
     Identifier "My Device Name"
     Driver "openchrome"
 EndSection

## Artifacts
If your X Server shows artifacts and fails to redraw some windows, try disabling the  option:

 Option     "EnableAGPDMA"               "false"

If your machine freeze at startup (GDM) or after login (SLiM), try adding the XAA option . Note that this only applies if you are using the XAA acceleration method (configured by the  option). Since 0.2.906, the default acceleration method is EXA.

 Option "XaaNoImageWriteRect"

If you experience significant CPU usage and low UI framerate, try adding:

 Option "AccelMethod" "XAA"

## Black screen when booting from LiveCD
If you experience a black screen when booting from Live-CD, add  on the kernel command line.

After installing the system you will need to blacklist the  module.

## DPMS problems
If you experience problems with DPMS not turning off laptop's backlight, try adding:

 Option "VBEModes" "true"

to the device section of .

## Hangup on exit
If your computer crashes when closing X, you may try not using the vesa driver for the kernel console. Just delete the vga-related parameters from the kernel command line.
