# Variable refresh rate

Variable refresh rate (VRR), also referred to as adaptive sync, allows the monitor to adjust its refresh rate to the output signal. This allows for games to eliminate screen tearing with less of the usual downsides of Vsync (such as stuttering). For a comprehensive look at VRR see PC Gaming Wiki.

## Overview
There are multiple implementations of VRR:

* FreeSync is AMD's implementation of VESA's VRR standard, and the phrases are often used interchangeably. FreeSync branded monitors should be compatible with all VESA compatible drivers.
* G-SYNC is NVIDIA's proprietary hardware and software implementation of VRR.
* Intel implements VESA's standard starting with 11th Gen integrated graphics and dedicated GPUs.

For setup purposes, it is necessary to differentiate between "native" G-SYNC monitors that licenses Nvidia's own chip, and G-SYNC Compatible monitors, FreeSync monitors which support a subset of G-SYNC's functionality. Within the category of G-SYNC Compatible monitors, the monitor may or may not be validated by NVIDIA. [https://www.nvidia.com/en-us/geforce/news/g-sync-ces-2019-announcements/ Even if a VRR monitor has not passed NVIDIA's validation (and thus would not be called G-SYNC Compatible in marketing material), you may still be capable of using it with G-SYNC.

{| class="wikitable
|+ VRR compatibility and implementations
|-
! Driver
! VESA
! G-SYNC
|-
! AMDGPU
|
|
|-
! Intel
|
|
|-
! Nouveau
|
|
|-
! NVIDIA
|
|
|}

## Hardware configuration
The monitor must be plugged in via DisplayPort. Some displays which implement (at least part of) the HDMI 2.1 specification also support VRR over HDMI. This is [https://www.phoronix.com/scan.php?page=news_item&px=NVIDIA-440.31-Linux-Release supported by the Nvidia driver and is supported by the AMD driver (pre HDMI 2.1) in Kernel 5.13 and later Some monitors may not support VRR at their maximum refresh rate. For example, a monitor that supports 165Hz may only support VRR when set to use 144Hz or less.

## Xorg configuration
## Enable on AMDGPU
FreeSync is only available if your [https://www.amd.com/en/products/freesync-monitors monitor is compatible with FreeSync, as well as if your GPU is compatible with FreeSync:

:Compatible GPUs include all AMD Radeon™ graphics cards beginning with Radeon™ RX 200 Series, released in 2013, and all newer Radeon consumer graphics products that use GCN 2.0 architecture and later.

## Using an Xorg conf file
Add the line to your AMDGPU .conf file in the  block:

 Option "VariableRefresh" "true"

Verify vrr_capable is set to 1 using xrandr:

xrandr will show the properties for all video output ports; make sure to look at the one that's actually connected to your monitor - the other outputs will report vrr_capable: 0.

## Multi-monitor configuration
Suppose you have a new 144Hz FreeSync capable monitor and want to use it as your primary monitor and connect your old 60Hz monitor as secondary monitor. In that case you may want to enable the AsyncFlipSecondaries option in your AMDGPU .conf file in the  block:

 Option "AsyncFlipSecondaries" "true"

This option is available since xorg-server release 21.1.0 and will allow synchronized page flips up to the highest refresh rate your primary monitor supports. Your secondary monitor(s) may exhibit tearing however.

## Enable on NVIDIA
## Using a Xorg conf file
## Via nvidia-settings
"Native" G-SYNC and validated G-SYNC Compatible monitors should automatically have VRR enabled. To check the state of your monitors, open  and navigate to your GPU (e.g. GPU 0), under which there will be an node for each active monitor (e.g. DP-0, HDMI-0). In each of those monitor frames, the G-SYNC Mode Available indicates the status of G-SYNC support, either: [https://github.com/NVIDIA/nvidia-settings/blob/510/src/libXNVCtrl/NVCtrl.h#L3541-L3551

* G-SYNC, indicating that this is a "native" G-SYNC monitor. Full G-SYNC support is enabled by default.
* G-SYNC Compatible, indicating that this is a validated G-SYNC Compatible monitor. G-SYNC support is enabled by default.
* G-SYNC Unvalidated, indicating that this is an unvalidated G-SYNC Compatible monitor. G-SYNC support is not enabled by default. * None, indicating that this monitor does not seem to support G-SYNC. Note that there are some FreeSync VRR monitors which are not G-SYNC compatible at all. [https://www.howtogeek.com/755346/g-sync-compatible-vs-g-sync-whats-the-difference/

If you have an unvalidated G-SYNC Compatible monitor, you can override NVIDIA's default and enable VRR with it:

* In  go to the X Server Display Configuration page, then under the Advanced button is the option to Allow G-SYNC on monitor not validated as G-SYNC Compatible. Click apply.
* Now, under OpenGL settings, check Allow G-SYNC/G-SYNC Compatible. In the same menu, you can check the show G-SYNC indicator option to display an indicator that G-SYNC is working in the top right corner.

## Wayland configuration
## NVIDIA
VRR Wayland using the proprietary driver requires a Volta GPU architecture or newer.

NVIDIA has shipped VRR Wayland support starting with driver version 525. Until 545, there are forced VSync issues. Past that, there are still remaining issues which are covered by the VRR Wayland thread on NVIDIA forums.

## GNOME
GNOME supports VRR as an experimental feature starting with version 46. Run  to enable the experimental feature, then restart the session by logging out and back in. VRR can then be enabled for each supported monitor in the Display Settings under Refresh Rate. When running on a supported and enabled monitor, GNOME automatically enables VRR for all full screen applications.

## KDE Plasma
Plasma's Wayland session uses the kwin compositor, which should automatically enable VRR for full screen applications === Sway ===

Sway supports variable refresh rate. To enable it for all of your outputs you can add the following to the sway configuration, or apply the setting to on a per output basis:

 output * adaptive_sync on

You can verify that your display supports adaptive sync with swaymsg:

## Hyprland
Hyprland supports variable refresh rate. To enable it, you need to add either  or [https://wiki.hyprland.org/Configuring/Variables/#misc in your misc section of your  :

 misc {
    vrr = 1
 }

Alternatively you can define  as an extra argument for the monitor(s)variable:

 # Example monitor configuration
 monitor=DP-1,2560x1440@240,0x0,1,vrr,1
 monitor=DP-2,2560x1440@165,-1440x-600,1,transform,1,vrr,1

 always enables variable refresh rate, while  only enables it for fullscreen applications.

You can verify that your display supports adaptive sync with hyprctl:

## niri
Niri supports variable refresh rate.
To enable it, you need to add either   or [https://yalter.github.io/niri/Configuration%3A-Outputs.html in your output section of your  :

 output "DP-1" {
    variable-refresh-rate
 }

 always enables variable refresh rate, while  will only enable VRR when a window matches the variable-refresh-rate window ruleThis is helpful to avoid various issues with VRR, since it can be disabled most of the time, and only enabled for specific windows, like games or video players.

You can check whether an output supports VRR:

## Testing
[https://github.com/Nixola/VRRTest VRRTest is a simple testing tool which should work for FreeSync and G-Sync. Install  or, manually install  package, clone repository, then run

 $ love /path/to/cloned/repository

With VRR off, if the application's FPS is less than the monitor's native refresh rate then the bars will stutter a lot since frames are being skipped. With VRR active, the bars will always move smoothly across the screen since the screen's refresh rate will match the application's refresh rate. Even with VRR functional you may experience tearing in which case you can also enable the TearFree option for AMDGPU; with both enabled there should be neither stuttering nor tearing (what is the nvidia equivalent?).

If you are using a Nvidia GPU, you can test G-SYNC compatibility with . This program will allow you to test VRR and Vsync so you can observe resulting effects. See project's Readme for more information.

According to this page: "gl-gsync-demo is made with G-SYNC but that does not matter, it will test AMD adaptive sync just fine". However, it may still not work as expected for FreeSync testing.

## Change VRR range of a FreeSync monitor
Freesync monitors usually have a limited range for VRR that are much lower than their maximum refresh rate, or that does not extend to the minimum refresh it is capable of. It should be possible to underclock or overclock the monitor to change the Freesync range.

## Obtaining the EDID file
External Display Identification Data (EDID) stores driver information about your monitor. By default, this file is sent by your monitor and read on connect.

## NVIDIA
For NVIDIA users, you will need to extract this file using something like  or .

## AMD
For modern AMD GPUs, the kernel should expose a read-only copy of the EDID via the sysfs (i.e. ).

## Editing the EDID File
You can edit this file with .

## Alternative method (AW EDID Editor)
Sometimes, wxedid will refuse to save the file with an error such as:

In that case, AW EDID Editor (Windows, runs under Wine) can be used.

The relevant section will be under EDID Base > Detailed Descriptor > Block Descriptor > Block 2, then under Block Descriptor Type > Display > Range Limits.

## Applying the modified EDID
## X11
Make a Xorg .conf file for your monitor and add a path to the custom EDID file you have edited.
See xrandr to find out the other information about your monitor.

## Wayland
The most reliable way to apply the EDID on Wayland is to add your modified EDID to your initramfs (if using one) and then specifying it as a boot parameter.

Firstly, create the required folder:

 # mkdir /usr/lib/firmware/edid

Now, add your modified EDID inside it. Here we will use  as the filename, but it can be anything:

 # cp modified_edid.bin /usr/lib/firmware/edid/vrr.bin

Then, add the file to the initramfs:

Finally, add the command line parameter using your boot loader configuration. The required parameter is . As example, to override the EDID for port DP-2, using the file located at  the following needs to be added:

 drm.edid_firmware=DP-2:edid/vrr.bin

Regenerate the initramfs and reboot. You should be able to use the extended VRR range now.

## Tips and tricks
You may follow one of the guides of people changing the freesync range on Windows: Process of overclocking on Linux (works only on NVidia GPUs): [https://forum.level1techs.com/t/overclock-your-monitor-with-nvidia-windows-and-linux/109323

## Remove applications from blacklist
Mesa has a list of blacklisted applications to avoid unexpected behavior, you can edit this blacklist here:

 /usr/share/drirc.d/00-mesa-defaults.conf

## Troubleshooting
## Monitor occasionally drops signal with FreeSync enabled
This is most likely due to firmware issues or driver issues causing the refresh rate to fall below the minimum safety marginYou can mitigate it by raising the minimum vertical refresh range.

## Using wxedid
See #Editing the EDID File or refer to [https://forum.level1techs.com/t/how-to-fix-freesync-lfc-screen-blanking-issues-using-wxedid-linux-ubuntu/177867 this tutorial.

## NVIDIA
Alternatively, you can edit the VertRefresh property in your Xorg configuration file (the following example was generated by ):

## Monitor does not show up as VRR capable in Wayland, despite supporting it
For some devices (such as laptop displays), GNOME/Plasma may not recognize VRR capability under Wayland, despite the display supporting it (and advertising support via EDID.

This may be caused by your greeter (such as GDM/SDDM) running on X11, while your desktop session is running on Wayland. To fix this, configure your greeter to use Wayland instead (see: SDDM#Wayland).

## Known issues
* Wayland is supported as of KDE Plasma 5.22 (any compatible GPU) and Sway (no Nvidia) [https://gitlab.freedesktop.org/wayland/wayland/issues/84. GNOME Wayland is supported starting with version 46 as an experimental feature.
* If you want to use G-SYNC and possibly Freesync on X11, only the G-SYNC/Freesync monitor must be connected.
** On X11, multiple monitors in a single X display will break G-SYNC/Freesync, however, this problem does not exist on Wayland.
** A secondary monitor set as copy/duplicate of the primary monitor does not break G-SYNC/Freesync on the primary monitor.
** If on X11, if you want to use multiple monitors and still use G-SYNC/Freesync, you can create a new X display which only covers the G-SYNC/Freesync monitor and run games there.
* Compositors will most likely need to be disabled before the OpenGl/Vulkan program is started (disabling compositors is not relevant or necessary on Wayland https://mastransky.wordpress.com/2021/01/10/firefox-were-finally-getting-hw-acceleration-on-linux/#comment-15517).
* On X11, Mesa blacklists many applications including video players.
* Although tearing is much less noticeable at higher refresh rates, FreeSync monitors often have a limited range for their VRR of 90Hz, which can be much lower than their max refresh rate. See Change VRR Range of a FreeSync Monitor.
