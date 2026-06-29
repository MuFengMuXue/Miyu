# Kernel mode setting

Kernel Mode Setting (KMS) is a method for setting display resolution and depth in the kernel space rather than user space.

The Linux kernel's implementation of KMS enables native resolution in the framebuffer and allows for instant console (tty) switching.  KMS also enables newer technologies (such as DRI2) which will help reduce artifacts and increase 3D performance, even kernel space power-saving.

## Background
Previously, setting up the video card was the job of the X server. Because of this, it was not easily possible to have fancy graphics in virtual consoles. Also, each time a switch from X to a virtual console was made (), the server had to give control over the video card to the kernel, which was slow and caused flickering. The same "painful" process happened when the control was given back to the X server ( when X runs in VT7).

With Kernel Mode Setting (KMS), the kernel is now able to set the mode of the video card. This makes fancy graphics during bootup, virtual console and X fast switching possible, among other things.

## Configuration
At first, note that for any method you use, you should always disable:

* Any  options in your boot loader as these will conflict with the native resolution enabled by KMS.
* Any  lines that enable a framebuffer that conflicts with the driver.

## Late KMS start
Intel, Nouveau, ATI and AMDGPU drivers already enable KMS automatically for all chipsets, so you do not need to do anything.

The proprietary NVIDIA driver supports KMS (since 364.12), which has to be manually enabled.

## Early KMS start
KMS is typically initialized after the initramfs stage. However, it is possible to enable KMS already during the initramfs stage. Add the required module for the video driver to the initramfs configuration file:

*  for AMDGPU, or  when using the legacy ATI driver.
*  for Intel graphics.
*  for the open-source Nouveau driver.
*  for the out-of-tree NVIDIA drivers. See NVIDIA#DRM kernel mode setting for details.
*  for Matrox graphics.
* Depending on QEMU graphics in use (qemu option  or libvirt **  for  (qemu) and / (libvirt),
**  for ,
**  for ,
**  for  (qemu) and  (libvirt),
**  for .
* Depending on VirtualBox graphics controller:
**  for VMSVGA,
**  for VBoxVGA or VBoxSVGA.

Initramfs configuration instructions are slightly different depending on the initramfs generator you use.

## mkinitcpio
For in-tree modules, either use  in the HOOKS array in  (the default since [https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/merge_requests/126/diffs#57ac3bb5162944ca1d6c5fa29ff4d7cc886e04bb_53_52 mkinitcpio v33) or place the module names in the MODULES array.

For the out-of-tree NVIDIA modules, you must place the module names in the MODULES array as follows:

If you are using the #Forcing modes and EDID method, you should embed the custom file into initramfs as well:

Then regenerate the initramfs.

## Booster
If you use Booster, you can load required modules with this config change:

If you are using the #Forcing modes and EDID method, you should embed the custom file into your booster images as well:

Then regenerate the booster images.

## Dracut
Dracut enables early loading (at the initramfs stage, via ) through its  command or  config entry line. For example:

If you are using the #Forcing modes and EDID method, you should embed the custom file as well:

Then regenerate the dracut images.

## Troubleshooting
## My fonts are too tiny
See Linux console#Fonts for how to change your console font to a large font. The Terminus font () is available in many sizes, such as  which is larger.

Alternatively, disabling modesetting might switch to lower resolution and make fonts appear larger.

## Forcing modes and EDID
If your native resolution is not automatically configured or no display at all is detected, then your monitor might send none or just a skewed EDID file. The kernel will try to catch this case and will set one of the most typical resolutions.

In case you have the EDID file for your monitor, you merely need to explicitly enforce it (see below). However, most often one does not have direct access to a sane file and it is necessary to either extract an existing one and fix it or to generate a new one.

Generating new EDID binaries for various resolutions and configurations is possible during kernel compilation by following the upstream documentation (also see here for a short guide). Other solutions are outlined in details in this article.
Extracting an existing one is in most cases easier, e.g. if your monitor works fine under Windows, you might have luck extracting the EDID from the corresponding driver, or if a similar monitor works which has the same settings, you may use  from the  package. You can also try looking in .

After having prepared your EDID, place it in a directory, e.g. called  under  and copy your binary into it.

To load it at boot, specify the following in the kernel command line:

 drm.edid_firmware=edid/your_edid.bin

In order to apply it only to a specific connector, use:

 drm.edid_firmware=VGA-1:edid/your_edid.bin

If you want to set multiple edid files, use:

 drm.edid_firmware=VGA-1:edid/your_edid.bin,VGA-2:edid/your_other_edid.bin

If you are doing early KMS, you must include the custom EDID file in the initramfs, otherwise you will run into problems.

The value of the  parameter may also be altered after boot by writing to :

 # echo edid/your_edid.bin > /sys/module/drm/parameters/edid_firmware

This will only take effect for newly plugged in displays, already plugged-in screens will continue to use their existing EDID settings. For external displays, replugging them is sufficient to see the effect however.

To load an EDID after boot, you can use debugfs instead of a kernel command line parameter if the kernel is not in lockdown mode.  This is very useful if you swap the monitors on a connector or just for testing.  Once you have an EDID file as above, run:

 # cat correct-edid.bin > /sys/kernel/debug/dri/0/HDMI-A-2/edid_override

And to disable:

 # echo -n reset > /sys/kernel/debug/dri/0/HDMI-A-2/edid_override

If your monitor supports hotplugging, you can also trigger a hotplug to make the monitor use the new EDID you just loaded (e.g. into ), so you don't have to physically replug the monitor nor reboot:

 # echo 1 > /sys/kernel/debug/dri/0/HDMI-A-2/trigger_hotplug

## Forcing modes
From the nouveau wiki:
:A mode can be forced on the kernel command line. Unfortunately, the command line option video is poorly documented in the DRM case. Bits and pieces on how to use it can be found in
:* https://docs.kernel.org/fb/modedb.html
:* https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpu/drm/drm_fb_helper.c

The format is:
 video=::xM][R][-][@][i][m][eDd

* : Specify a video mode at bootup.
* : Specifies the video connection type, such as VGA, DVI, HDMI, etc., see  for available connectors
* : The horizontal resolution in pixels.
* : The vertical resolution in pixels.
* : Enables the use of VESA Coordinated Video Timings (CVT) to calculate the video mode timings instead of looking up the mode from a database
* : Enables reduced blanking calculations for digital displays when using CVT. This reduces the horizontal and vertical blanking intervals to save bandwidth.
* : Specifies the color depth or bits per pixel (e.g., -24 for 24-bit color).
* : Specifies the refresh rate in Hz.
* : Enables interlaced mode.
* : Adds margins to the CVT calculation (1.8% of xres rounded down to 8 pixels and 1.8% of yres)
* : output forced to on
* : digital output forced to on (e.g. DVI-I connector)
* : output forced to off

You can override the modes of several outputs using  several times, for instance, to force  to 1024x768 at 85 Hz and  off:

 video=DVI-I-1:1024x768@85 video=TV-1:d

Options can also be passed after the mode, using commas as separator:

 video=DVI-I-1:720x480,rotate=180

Valid options are:

* , , ,  (integer): Number of pixels in the margins, typically to deal with overscan on TVs
*  (boolean): Perform an axial symmetry on the X axis
*  (boolean): Perform an axial symmetry on the Y axis
*  (integer): Rotate the initial framebuffer by x degrees. Valid values are 0, 90, 180 and 270.
* : Analog TV mode. One of "NTSC", "NTSC-443", "NTSC-J", "PAL", "PAL-M", "PAL-N", or "SECAM".
* , one of "normal", "upside_down", "left_side_up", or "right_side_up". For KMS drivers only, this sets the "panel orientation" property on the kms connector as hint for kms users.

To get the name and current status of connectors, you can use the following shell oneliner:

{{hc|$ for p in /sys/class/drm/*/status; do con=${p%/status}; echo -n "${con#*/card?-}: "; cat $p; done|
DVI-I-1: connected
HDMI-A-1: disconnected
VGA-1: disconnected
}}

## Disabling modesetting
You may want to disable KMS for various reasons. To disable KMS, add  as a kernel parameter. See Kernel parameters for more info.

Along with the  kernel parameter, for an Intel graphics card, you need to add , and for an Nvidia graphics card, you need to add . For Nvidia Optimus dual-graphics system, you need to add all the three kernel parameters (i.e. ).
