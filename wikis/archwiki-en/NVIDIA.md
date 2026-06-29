# NVIDIA

This article covers the official NVIDIA graphics card drivers. For the community open-source driver, see Nouveau. If you have a laptop with hybrid graphics, see also NVIDIA Optimus.

## Installation
First, find the family of your card (e.g. NV110, NVC0, etc.) on nouveau wiki's code names page corresponding to its model/official name obtained with:

 $ lspci -k -d ::03xx

Then, install the appropriate driver for your card:

{| class="wikitable"
! GPU family
! Driver
! Status
|-
| Blackwell (GBXXX) and newer
|  for    for    for any kernel(s)
| Recommended by upstream Current, supported1
|-
| Turing (NV160/TUXXX)  through  Ada Lovelace (NV190/ADXXX)
| colspan="2" | Supported both by:
*  with no RTD3 Power Management on Turing2,  possible crashes on Ampere-equiped laptops2
*
|-
| Maxwell (NV110/GMXXX) through  Volta (NV140/GV100)
|
| Legacy, supported
|-
| Kepler (NVE0/GKXXX)
|
| rowspan="4" | Legacy, unsupported3,4
|-
| Fermi (NVC0/GF1XX)
|
|-
| Tesla (NV50/G80-90-GT2XX)
|
|-
| Curie (NV40/G70) and older
| No longer packaged
|}

# If these packages do not work (usually due to new hardware releases)  may have a newer version that offers support.
# NVIDIA's GSP firmware is known to cause issues, from suboptimal power management of Turing GPUs to complete failure on some laptops containing Ampere GPUs. If affected, use the proprietary driver (e.g. ) with the module parameter  instead.
# May not function correctly on Linux 5.18 (or later) on systems with Intel CPUs 11th Gen and newer due an incompatibility with Indirect Branch Tracking. You can disable it by setting the  kernel parameter from the boot loader. Be aware, this security feature is responsible for mitigating a class of exploit techniques.
# NVIDIA no longer actively supports these cards and their drivers may not officially support the current Xorg version. It might be easier to use the nouveau driver; however, NVIDIA's legacy drivers are still available and might provide better 3D performance/stability.

:

For 32-bit application support, also install the corresponding lib32 package from the multilib repository (e.g. ).

The  package contains a file which blacklists the  module once you reboot. Optionally, you can also remove  from the  array in  and regenerate the initramfs. This will prevent the initramfs from containing the  module making sure the kernel cannot load it during early boot.

## Custom kernel
Ensure your kernel has , and if using  then this is needed in the PKGBUILD (since kernel 5.16):

 install -Dt "$builddir/tools/bpf/resolve_btfids" tools/bpf/resolve_btfids/resolve_btfids

If your kernel is compiled with  enabled, you may need to prevent the new NVIDIA GPU driver Nova from loading.  adds it to the blacklist by default. You can check this by running systemd-analyze. If you have installed a different version of the driver, you may need to blacklist the  and  modules manually.

## DRM kernel mode setting
Kernel mode setting is required to make Wayland compositors function properly. KMS is also required for native Wayland rendering on NVIDIA dedicated GPUs for dual-GPU setups. NVIDIA does not support automatic KMS late loading without enabling DRM (Direct Rendering Manager). Starting from  560.35.03-5, DRM is enabled by default.

To verify that DRM is actually enabled, execute the following:

 # cat /sys/module/nvidia_drm/parameters/modeset

Which should now return , and not .

For drivers older than version 560, manually set the  kernel module parameter for the  module.

Officially supported kernels enable , while NVIDIA driver requires  or  when its own fbdev is disabled (or unavailable, with driver versions older than 545): see BBS#307164 for a possible workaround if you experience issues.

## Early loading
For basic functionality, just adding the kernel parameter should suffice. If you want to ensure it is loaded as early as possible, or you are noticing startup issues (such as the  kernel module being loaded after the display manager), you can add , ,  and  to the initramfs. See Kernel module#Early module loading to learn how to configure your initramfs generator.

## Hardware accelerated video decoding
Accelerated video decoding with VDPAU is supported on GeForce 8 series cards and newer. Accelerated video decoding with NVDEC is supported on Fermi (~400 series) cards and newer. See Hardware video acceleration for details.

## Hardware accelerated video encoding with NVENC
NVENC requires the  module and the creation of related device nodes under .

The latest driver package provides a udev rule which creates device nodes automatically, so no further action is required.

If you are using an old driver (e.g. ), you need to create device nodes. Invoking the  utility automatically creates them. You can create  to run it automatically:

## Wayland configuration
Regarding Xwayland take a look at Wayland#Xwayland.

For further configuration options, take a look at the wiki pages or documentation of the respective compositor.

## Basic support
There are two kernel parameters for the  module to be considered:  and . Both are enabled by default when using the  package. NVIDIA also plans to enable them by default in a future release.

## modeset
Enabling  is necessary for all Wayland configurations to function properly.

For unsupported drivers, where  needs to be enabled manually, see #DRM kernel mode setting, and Wayland#Requirements for more information.

## fbdev
The supported driver versions from NVIDIA provide a framebuffer. For legacy driver versions that are no longer supported, enabling the  kernel module parameter for the  module might be necessary for some Wayland configurations.

It is specifically a hard requirement on Linux 6.11 and later, but it is currently unclear whether this is intended behavior or a bug, see for more details.

To verify that the NVIDIA framebuffer is actually enabled, execute the following:

 # cat /sys/module/nvidia_drm/parameters/fbdev

It will return  if the framebuffer is enabled.

## Suspend support
Wayland suspend can suffer from the defaults more than X does, see /Tips and tricks#Preserve video memory after suspend for details.

If you use GDM, also see GDM#Wayland and the proprietary NVIDIA driver.

## nvidia-application-profiles-rc.d
Some wayland compositors will consume a large quantity of VRAM by default if the [https://www.nvidia.com/en-us/drivers/details/237587/ GLVidHeapReuseRatio application profile key is not applied against their process name. For example, niri users can free up to ~2.5GiB of idle vram consumption with the following:

{{hc|/etc/nvidia/nvidia-application-profiles-rc.d/50-limit-free-buffer-pool-in-wayland-compositors.json|2=
{
    "rules": [
        {
            "pattern": {
                "feature": "procname",
                "matches": "niri"
            },
            "profile": "Limit free buffer pool on Wayland compositors"
        }
    ],
    "profiles": [
        {
            "name": "Limit free buffer pool on Wayland compositors",
            "settings": [
                {
                    "key": "GLVidHeapReuseRatio",
                    "value": 0
                }
            ]
        }
    ]
}
}}

## Xorg configuration
The proprietary NVIDIA graphics card driver does not need any Xorg server configuration file. You can start X to see if the Xorg server will function correctly without a configuration file. However, it may be required to create a configuration file (prefer  over ) in order to adjust various settings. This configuration can be generated by the NVIDIA Xorg configuration tool, or it can be created manually. If created manually, it can be a minimal configuration (in the sense that it will only pass the basic options to the Xorg server), or it can include a number of settings that can bypass Xorg's auto-discovered or pre-configured options.

## Automatic configuration
The NVIDIA package includes an automatic configuration tool to create an Xorg server configuration file () and can be run by:

 # nvidia-xconfig

This command will auto-detect and create (or edit, if already present) the  configuration according to present hardware.

Double-check your  to make sure your default depth, horizontal sync, vertical refresh, and resolutions are acceptable.

## nvidia-settings
The  tool lets you configure many options using either CLI or GUI. Running  without any options launches the GUI, for CLI options see .

You can run the CLI/GUI as a non-root user and save the settings to  by using the option Save Current Configuration under nvidia-settings Configuration tab.

To load the  for the current user:

 $ nvidia-settings --load-config-only

See Autostarting to start this command on every boot.

## Manual configuration
Several tweaks (which cannot be enabled automatically or with nvidia-settings) can be performed by editing your configuration file. The Xorg server will need to be restarted before any changes are applied.

See NVIDIA Accelerated Linux Graphics Driver README and Installation Guide for additional details and options.

## Minimal configuration
A basic configuration block in  (or deprecated in ) would look like this:

## Disabling the logo on startup
If you are using an old driver (), you may want to disable the NVIDIA logo splash screen that is displayed at X startup. Add the  option under section :

 Option "NoLogo" "1"

## Overriding monitor detection
The  option under section  allows overriding monitor detection when X server starts, which may save a significant amount of time at start up. The available options are:  for analog connections,  for digital monitors and  for televisions.

The following statement forces the NVIDIA driver to bypass startup checks and recognize the monitor as DFP:

 Option "ConnectedMonitor" "DFP"

## Enabling brightness control
Add to kernel parameters:

 nvidia.NVreg_RegistryDwords=EnableBrightnessControl=1

Alternatively, add the following under section :

 Option "RegistryDwords" "EnableBrightnessControl=1"

If brightness control still does not work with this option, try installing .

## Enabling SLI
Taken from the NVIDIA driver's README Appendix B: This option controls the configuration of SLI rendering in supported configurations. A "supported configuration" is a computer equipped with an SLI-Certified Motherboard and 2 or 3 SLI-Certified GeForce GPUs.

Find the first GPU's PCI Bus ID using :

Add the BusID (3 in the previous example) under section :

 BusID "PCI:3:0:0"

Add the desired SLI rendering mode value under section :

 Option "SLI" "AA"

The following table presents the available rendering modes.

{| class="wikitable"
! Value !! Behavior
|-
| 0, no, off, false, Single || Use only a single GPU when rendering.
|-
| 1, yes, on, true, Auto || Enable SLI and allow the driver to automatically select the appropriate rendering mode.
|-
| AFR || Enable SLI and use the alternate frame rendering mode.
|-
| SFR || Enable SLI and use the split frame rendering mode.
|-
| AA || Enable SLI and use SLI antialiasing. Use this in conjunction with full scene antialiasing to improve visual quality.
|}

Alternatively, you can use the nvidia-xconfig utility to insert these changes into  with a single command:

 # nvidia-xconfig --busid=PCI:3:0:0 --sli=AA

To verify that SLI mode is enabled from a shell:

If this configuration does not work, you may need to use the PCI Bus ID provided by ,

and comment out the PrimaryGPU option in your xorg.d configuration,

Using this configuration may also solve any graphical boot issues.

## Multiple monitors
See Multihead for more general information.

## Using nvidia-settings
The nvidia-settings tool can configure multiple monitors.

For CLI configuration, first get the  by running:

{{hc|$ nvidia-settings -q CurrentMetaMode|2=
Attribute 'CurrentMetaMode' (hostnmae:0.0): id=50, switchable=no, source=nv-control :: DPY-1: 2880x1620 @2880x1620 +0+0 {ViewPortIn=2880x1620, ViewPortOut=2880x1620+0+0}
}}

Save everything after the  to the end of the attribute (in this case: {{ic|1=DPY-1: 2880x1620 @2880x1620 +0+0 {ViewPortIn=2880x1620, ViewPortOut=2880x1620+0+0}}}) and use to reconfigure your displays with .

## ConnectedMonitor
If the driver does not properly detect a second monitor, you can force it to do so with ConnectedMonitor.

The duplicated device with  is how you get X to use two monitors on one card without . Note that  will strip out any  options you have added.

## TwinView
You want only one big screen instead of two. Set the  argument to . This option should be used if you desire compositing. TwinView only works on a per-card basis, when all participating monitors are connected to the same card.

 Option "TwinView" "1"

Example configuration:

Device option information.

If you have multiple cards that are SLI capable, it is possible to run more than one monitor attached to separate cards (for example: two cards in SLI with one monitor attached to each). The "MetaModes" option in conjunction with SLI Mosaic mode enables this. Below is a configuration which works for the aforementioned example and runs GNOME flawlessly.

## Vertical sync using TwinView
If you are using TwinView and vertical sync (the Sync to VBlank option in ), you will notice that only one screen is being properly synced, unless you have two identical monitors. Although  does offer an option to change which screen is being synced (the Sync to this display device option), this does not always work. A solution is to add the following environment variables at startup, for example append in :

 export __GL_SYNC_TO_VBLANK=1
 export __GL_SYNC_DISPLAY_DEVICE=DFP-0
 export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-0

You can change  with your preferred screen ( is the DVI port and  is the VGA port). You can find the identifier for your display from  in the X Server XVideoSettings section.

## Gaming using TwinView
In case you want to play full-screen games when using TwinView, you will notice that games recognize the two screens as being one big screen. While this is technically correct (the virtual X screen really is the size of your screens combined), you probably do not want to play on both screens at the same time.

To correct this behavior for SDL 1.2, try:

 export SDL_VIDEO_FULLSCREEN_HEAD=1

For OpenGL, add the appropriate Metamodes to your xorg.conf in section  and restart X:

 Option "Metamodes" "1680x1050,1680x1050; 1280x1024,1280x1024; 1680x1050,NULL; 1280x1024,NULL;"

Another method that may either work alone or in conjunction with those mentioned above is starting games in a separate X server.

## Mosaic mode
Mosaic mode is the only way to use more than 2 monitors across multiple graphics cards with compositing. Your window manager may or may not recognize the distinction between each monitor. Mosaic mode requires a valid SLI configuration. Even if using Base mode without SLI, the GPUs must still be SLI capable/compatible.

## Base Mosaic
Base Mosaic mode works on any set of Geforce 8000 series or higher GPUs. It cannot be enabled from within the nvidia-setting GUI. You must either use the nvidia-xconfig command line program or edit  by hand. Metamodes must be specified. The following is an example for four DFPs in a 2x2 configuration, each running at 1920x1024, with two DFPs connected to two cards:

 # nvidia-xconfig --base-mosaic --metamodes="GPU-0.DFP-0: 1920x1024+0+0, GPU-0.DFP-1: 1920x1024+1920+0, GPU-1.DFP-0: 1920x1024+0+1024, GPU-1.DFP-1: 1920x1024+1920+1024"

## SLI Mosaic
If you have an SLI configuration and each GPU is a Quadro FX 5800, Quadro Fermi or newer, then you can use SLI Mosaic mode. It can be enabled from within the nvidia-settings GUI or from the command line with:

 # nvidia-xconfig --sli=Mosaic --metamodes="GPU-0.DFP-0: 1920x1024+0+0, GPU-0.DFP-1: 1920x1024+1920+0, GPU-1.DFP-0: 1920x1024+0+1024, GPU-1.DFP-1: 1920x1024+1920+1024"

## NVswitch
For systems with NVswitch, like H100x8 on AWS, the following is need.
* install nvidia-fabricmanager
* install matching kernel module needed by the fabric manager

With the fabricmanager, pytorch would report no GPU is found.

To install the fabric manager:
# download the tarball from nvidia. here
# version 555.42.02 works well
# modify the install script in sbin/fm_run_package_installer.sh to fix the installed file path

To get the matching kernel driver:
# git clone the AUR for nvidia-beta-dkms and nvidia-utils-beta
# change the PKGBUILD to use version 555.42.02
# build and install them
# reboot

finally,  and , then pytorch should work.

## Tips and tricks
See NVIDIA/Tips and tricks.

## Troubleshooting
See NVIDIA/Troubleshooting.
