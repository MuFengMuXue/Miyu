# Nouveau

This article covers the reverse-engineered open-source Nouveau driver for NVIDIA graphics cards. For information about the upstream drivers, see NVIDIA.

Find your card's code name (a more detailed list is available on Wikipedia), and compare it with the feature matrix for supported features.

## Installation
Install the  package, which provides the DRI driver for 3D acceleration.

* For 32-bit application support, also install the  package from the multilib repository.
* For the DDX driver (which provides 2D acceleration in Xorg), install the  package.

See also Hardware video acceleration.

## Using the Mesa NVK Vulkan Driver
NVK is an open-source Vulkan driver based on Nouveau for Kepler and newer NVIDIA cards.

Using NVK requires Kernel version 6.7 or newer and  version 24.1 or newer.

Before enabling NVK you must uninstall any of the following packages (and/or their  and DKMS variants):

* , ,
* ,
*

If you are using a hybrid laptop or a dual GPU system ensure you do not have Nouveau blacklisted by a GPU manager in .

Then install  (and if it is required, ).

Add  as a kernel parameter if required. It is enabled by default on Ada Lovelace and newer cards. See note in the documentation.

Finally reboot your system.

To verify everything is working  from  can be used. It should report the NVIDIA GPU in your system as using the NVK driver.

## Loading
The Nouveau kernel module should load automatically on system boot. If it does not happen, then:

* Make sure you do not have  or  as a kernel parameter, since Nouveau requires kernel mode-setting.
* Also, check that you do not have Nouveau disabled using any modprobe blacklisting technique within  or .
* If everything above still fails to load nouveau, check dmesg for an opcode error. Add  to your kernel parameters to prevent module unloading.* Check if  or any file in  exists and is referencing the  driver. It is probably a good idea to rename the file.

## Early KMS
Kernel mode setting (KMS) is supported by the  driver and is enabled early since mkinitcpio v32, as the  hook is included by default. For other setups, see Kernel mode setting#Early KMS start for instructions on how to enable KMS as soon as possible at the boot process.

## Tips and tricks
## Keep NVIDIA driver installed
If you want to keep the proprietary NVIDIA driver installed (and are not using OpenGL), but want to use the Nouveau driver, follow the steps below:

Comment out nouveau blacklisting in  or , modifying it as follows:

 #blacklist nouveau

You may also need to comment out other configuration files that prioritize the proprietary driver, e.g. [https://man.archlinux.org/man/systemd-modules-load.service.8.en systemd-modules-load's  and udev's . Check what files the driver has installed with the following command:

 $ pacman -Ql nvidia-utils | grep conf

Then, ensure that you have disabled -prefixed services that might call  to load the module on boot. For example:

 $ systemctl status nvidia-persistenced.service

And if you are using Xorg, tell Xorg to load nouveau instead of NVIDIA:

Reboot to make effects. And check that it loaded fine by looking at kernel messages:

 # dmesg

## Installing the latest development packages
To get the latest Nouveau improvements

*
*
*
*
*
*

## Dual head
Multiple monitors can be setup with RandR, see Multihead#RandR.

## Setting console resolution
You can pass the resolution to nouveau with the  kernel line option (see KMS).

## Power management
The lack of proper power management in the nouveau driver is one of the most important causes of performance issues, since most cards will remain in their lower power state with lower clocks during their use. Experimental support for GPU reclocking is available for some cards (see the Nouveau PowerManagement page) and since kernel 4.5 can be controlled through a debugfs interface located at .

For example, to check the available power states and the current setting for the first card in your system, run:

 # cat /sys/kernel/debug/dri/0/pstate

It is also possible to manually set/force a certain power state by writing to said interface:

 # echo pstate > /sys/kernel/debug/dri/0/pstate

## Fan control
If it is implemented for your card, you can configure fan control via .

 $ find /sys -name pwm1_enable
 /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/hwmon/hwmon1/pwm1_enable
 $ readlink /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/driver
 ../../../../bus/pci/drivers/nouveau

 can be set to 0, 1 or 2 meaning NONE, MANUAL and AUTO fan control. If set to manual fan control, you can set  manually, for example to 40 for 40%.

You can also set it by an udev rule:

{{hc|/etc/udev/rules.d/50-nouveau-hwmon.rules|2=
ACTION=="add", SUBSYSTEM=="hwmon", DRIVERS=="nouveau", ATTR{pwm1_enable}="2"
}}

Sources:

* https://floppym.blogspot.de/2013/07/fan-control-with-nouveau.html
* https://web.archive.org/web/20141031191559/https://kalgan.cc/blog/posts/Controlling_nVidia_cards_fans_with_nouveau_in_Debian/

## Optimus
You have two solutions to use Optimus on a laptop (aka hybrid graphics, when you have two GPUs on your laptop): bumblebee and PRIME

## Vertical synchronization
Xorg compositors are prone to show issues with Nouveau. Unlike most of them, Picom offers lots of options to tweak for a smoother and tearing free result. A configuration which is expected to deliver a good result would be the following:

 $ picom -b --unredir-if-possible --backend xr_glx_hybrid --vsync --use-damage --glx-no-stencil

## Troubleshooting
Add  and  to your kernel parameters to turn on video debugging:

Create verbose Xorg log:

 $ startx -- -logverbose 9 -verbose 9

View loaded video module parameters and values:

 $ modinfo -p video

## Disable MSI
If you are still having problems loading the module or starting the X server, append  to your Kernel parameters.

Source: https://bugs.freedesktop.org/show_bug.cgi?id=78441

## Phantom output issue
It is possible for the nouveau driver to detect "phantom" outputs.  For example, both VGA-1 and LVDS-1 are shown as connected but only LVDS-1 is present.

This causes display problems and/or prevent suspending on lid closure.

## Kernel parameters
The problem can be overcome by disabling the phantom output (VGA-1 in the examples given) with Kernel parameters:

 video=VGA-1:d

Where  = disable.

The nouveau kernel module also has an option to disable TV-out detection tv_disable=1

## Xorg configuration
The phantom output can be disabled in Xorg by adding the following to :

 Section "Monitor"
 Identifier "VGA-1"
 Option "Ignore" "1"
 EndSection

Source: https://web.archive.org/web/20170118202740/http://gentoo-en.vfose.ru/wiki/Nouveau#Phantom_and_unpopulated_output_connector_issues

## Xrandr
Xrandr can disable the output:

 $ xrandr --output VGA-1 --off

This can be added to the xinit configuration.

## Random lockups with kernel error messages
Specific NVIDIA chips with Nouveau may give random system lockups and more commonly throw many kernel messages, seen with dmesg.  Try adding the  kernel parameter. See Fedora:Common kernel problems#Systems with nVidia adapters using the nouveau driver lock up randomly for more information.

Note that using  kernel parameter might cause [https://bugs.kde.org/show_bug.cgi?id=485429 ~%100 CPU usage on Wayland when there is no iGPU or disabled iGPU by factory. You can switch to X11 session or prefer adding  environment variable for wayland to disable OpenGL hardware acceleration completely.

As an alternative, you can also use the  environment variable to disable OpenGL acceleration in Qt applications.

## Pointer to flat panel table invalid
NVIDIA graphics cards with recent chipsets can cause startup issues - this includes X11 being unable to start and lspci freezing indefinitelyThis can break live distributions/installation media. This can be detected either by running lspci, or checking the systemd journal for the error:

 nouveau E[     DRMPointer to flat panel table invalid

The system may start if the Nouveau driver is disabled by passing the following kernel parameters:

 modprobe.blacklist=nouveau

The Nouveau driver can then be loaded using

 # modprobe nouveau

The system should then function correctly.
If you have another NVIDIA graphics card, or just want to be safe, you can disable the offending card using:

 # echo 1 > /sys/bus/pci/devices/card-device-id/remove
