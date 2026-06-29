# NVIDIA/Troubleshooting

## Failure to start
## System will not boot after driver was installed
If after installing the NVIDIA driver your system becomes stuck before reaching the display manager, try to disable kernel mode setting.

## Xorg fails to load or Red Screen of Death
If you get a red screen and use GRUB, disable the GRUB framebuffer by editing  and uncomment . For more information see GRUB/Tips and tricks#Disable framebuffer.

## Black screen at X startup / Machine poweroff at X shutdown
If you have installed an update of NVIDIA and your screen stays black after launching Xorg, or if shutting down Xorg causes a machine poweroff, try the below workarounds:

* Prepend  to your xinitrc
* Use the  kernel parameter.
* You can also try to add the  module directly to your mkinitcpio.conf.

## Screen(s) found, but none have a usable configuration
Sometimes NVIDIA and X have trouble finding the active screen. If your graphics card has multiple outputs try plugging your monitor into the other ones. On a laptop it may be because your graphics card has VGA/TV out. Xorg.0.log will provide more info.

Another thing to try is adding an invalid  to  to force Xorg throw an error and show you how to correct it. See the documentation for more information about the ConnectedMonitor setting.

After re-run X see Xorg.0.log to get valid CRT-x,DFP-x,TV-x values.

 could be helpful.

## X fails with "Failing initialization of X screen"
If  says X server fails to initialize screen

 (EE) NVIDIA(G0): GPU screens are not yet supported by the NVIDIA driver
 (EE) NVIDIA(G0): Failing initialization of X screen

and nvidia-smi says

The solution is at first reinstall latest , and then copy  to , and then edit  and add the line . Restart the computer. The problem will be fixed.

## Xorg fails during boot, but otherwise starts fine
On very fast booting systems, systemd may attempt to start the display manager before the NVIDIA driver has fully initialized. You will see a message like the following in your logs only when Xorg runs during boot.

In this case you will need to establish an ordering dependency from the display manager to the DRI device. First create device units for DRI devices by creating a new udev rules file.

Then create dependencies from the display manager to the device(s).

If you have additional cards needed for the desktop then list them in Wants and After seperated by spaces.

## Black screen on systems with integrated GPU
If you have a system with an integrated GPU (e.g. Intel HD 4000, VIA VX820 Chrome 9 or AMD Cezanne) and have installed the  or earlier package, you may experience a black screen on boot, when changing virtual terminal, or when exiting an X session. This may be caused by a conflict between the graphics modules. This is solved by blacklisting the relevant GPU modules. Create the file  and prevent the relevant modules from loading on boot:

## X fails with "no screens found" when using Multiple GPUs
In situations where you might have multiple GPUs on a system and X fails to start with:

 [ 76.633] (EE) No devices detected.
 [ 76.633] Fatal server error:
 [ 76.633] no screens found

then you need to add your discrete card's BusID to your X configuration. This can happen on systems with an Intel CPU and an integrated GPU or if you have more than one NVIDIA card connected. Find your BusID:

Then you fix it by adding it to the card's Device section in your X configuration. In my case:

In the example above  is stripped to be written as , however some conversions can be more complicated.  output is in hex format, but in configuration files the BusID's are in decimal format! This means that in cases where the BusID is greater than 9 you will need to convert it to decimal!

ie:  from lspci becomes .

## Modprobe Error: "Could not insert 'nvidia': No such device" on linux >=4.8
With linux 4.8, one can get the following errors when trying to use the discrete card:

This problem is caused by bad commits pertaining to PCIe power management in the Linux Kernel (as documented in this NVIDIA DevTalk thread).

The workaround is to add  to your kernel parameters. Note that this disables PCIe power management for all devices.

## System does not return from suspend
What you see in the log:

 kernel: nvidia-modeset: ERROR: GPU:0: Failed detecting connected display devices
 kernel: nvidia-modeset: ERROR: GPU:0: Failed detecting connected display devices
 kernel: nvidia-modeset: WARNING: GPU:0: Failure processing EDID for display device DELL U2412M (DP-0).
 kernel: nvidia-modeset: WARNING: GPU:0: Unable to read EDID for display device DELL U2412M (DP-0)
 kernel: nvidia-modeset: ERROR: GPU:0: Failure reading maximum pixel clock value for display device DELL U2412M (DP-0).

A possible solution based on Run this command to get the  string:

 # strings /sys/firmware/acpi/tables/DSDT | grep -i 'windows ' | sort | tail -1

Add the  kernel parameter to your boot loader configuration.

Another possible cause to the issue could be the use of the  package, as described here:
* https://bbs.archlinux.org/viewtopic.php?pid=2047692
* https://github.com/NVIDIA/open-gpu-kernel-modules/issues/450
* https://github.com/NVIDIA/open-gpu-kernel-modules/issues/223
* https://github.com/NVIDIA/open-gpu-kernel-modules/issues/94

## Black screen returning from suspend
If experiencing black screen issues and logs containing:

 archlinux kernel: NVRM: GPU at PCI:0000:08:00: GPU-926ecdb0-adb1-6ee9-2fad-52e7214c5011
 archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='', name=, Graphi>
 archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='', name=, Graphi>
 archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='', name=, Graphi>
 archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='', name=, Graphi>
 archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='', name=, Graphi>

You need to enable the NVIDIA suspend, hibernate and sleep services as explained in NVIDIA/Tips and tricks#Preserve video memory after suspend.

## One or more monitors not working in multi-monitor setup in Xorg
If one or more of your monitors is not outputting anything in Xorg and is showing up as "Disabled" in the  control panel, then your current Xorg configuration may be incompatible.
The proprietary NVIDIA driver should not require a X configuration to simply function. See NVIDIA#Xorg configuration.

Simply move or rename the  file and any configuration files in  pertaining to the NVIDIA driver. Only files ending in  will be read by Xorg.
 $ mv /etc/X11/xorg.conf /etc/X11/xorg.conf.old

After disabling the old NVIDIA Xorg configuration you may want to use  to generate a new NVIDIA Xorg configuration suited to your hardware. This shouldn't however be necessary to get the driver to work.
 $ nvidia-xconfig

## Crashes and hangs
## Crashing in general
* Try disabling the GSP firmware.
* Try disabling  in xorg.conf.
* If Xorg outputs an error about  or , or crashes with a "Signal 11" while using nvidia-96xx drivers, add  to your kernel parameters.
* If the NVIDIA compiler complains about different versions of GCC between the current one and the one used for compiling the kernel, add in :
 export IGNORE_CC_MISMATCH=1
* If fullscreen applications are freezing or crashing, try enabling  and  options in your desktop environment's settings.

## Bad support of mesh shaders
This bug is present only for new games that depend on them, like Final Fantasy VII Rebirth. This is reflected in the absence of environments when using NVIDIA GPUs even with latest beta drivers. [https://github.com/ValveSoftware/Proton/issues/8408

However, pyroveil allows you to get around the problem with SPIR-V, while waiting for a fix from NVIDIA.

You need to compile and install the tool by following the tutorial on GitHub, then run the game with the  and  environment variables.

## Visual glitches, hangs and errors in OpenGL applications
If you are using a recent CPU (Intel Sandy Bridge (2011) and later or AMD Zen (2017) and later) it has a micro operations cache. Using a micro op cache can lead to problems with NVIDIA's driver in OpenGL due to Cache Aliasing You usually are able to disable the micro op cache in your systems BIOS, but this comes at the cost of performance [https://chipsandcheese.com/2021/07/03/how-zen-2s-op-cache-affects-performance/. Disabling the micro op cache also helps with the most severe graphical glitches in Xwayland applications, although it does not solve the problem fully === Kernel panic when updating and/or rebooting the system ===

This is a known bug that is present in the NVIDIA 550 series drivers. [https://forums.developer.nvidia.com/t/series-550-freezes-laptop/284772 As of yet the cause is unknown however it only appears to affect laptops. See BBS#293400 for more details.

To workaround this issue, switch to  if supported by the hardware, otherwise use  instead.

## GSP firmware
The use of the GSP firmware, enabled by default since version 555 of the NVIDIA driver released in June 2024, is known to cause a range of issues including Vulkan failures and system crashes.

To disable it, use the  module parameter for the  kernel module. This only works with the proprietary NVIDIA driver: see NVIDIA#Installation if switching from the open source driver.

Do not forget to regenerate the initramfs if needed. To have this new kernel module option take effect, reboot.

## Visual issues
## Avoid screen tearing on Xorg
The NVIDIA driver conditionally applies a composition pipeline to prepare the image for display. This not to be confused with a composite manager which takes over window presentation (and can also mitigate screen tearing, via VSync). By default, the composition pipeline is only applied if the current screen transformations require it. The pipeline uses the GPU's specialized display engine if possible, then the more general graphics engine. There are a couple of options to control this:

*  forces usage of the pipeline (further discussed in #Multi-monitor).
*  forces usage of the pipeline, and forces it to all be done with the graphics engine.

Tearing on Xorg can be avoided by setting . To test whether this option will work, run:

 $ nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"

Or click on the Advanced button that is available on the X Server Display Configuration menu option. Select either Force Composition Pipeline or Force Full Composition Pipeline and click on Apply.

In order to make the change permanent, it must be added to the  section of the Xorg configuration file. When making this change,  should be enabled and  should be disabled in the driver configuration as well. See example configuration below:

If you do not have an Xorg configuration file, you can create one for your present hardware using  (see NVIDIA#Automatic configuration) and move it from  to the preferred location .

## Multi-monitor
For multi-monitor setup you will need to specify  for each display. For example:

 $ nvidia-settings --assign CurrentMetaMode="DP-2: nvidia-auto-select +0+0 {ForceCompositionPipeline=On}, DP-4: nvidia-auto-select +3840+0 {ForceCompositionPipeline=On}"

Without doing this, the  command will disable your secondary display.

You can get the current screen names and offsets using :

 $ nvidia-settings --query CurrentMetaMode

The above line is for two 3840x2160 monitors connected to DP-2 and DP-4. You will need to read the correct  by exporting  and append  to each of your displays. Setting  only affects the targeted display.

## Screen corruption after resuming from suspend or hibernation
This also applies if an external monitor does not wake up after suspend or hibernation.

See NVIDIA/Tips and tricks#Preserve video memory after suspend

A corruption after suspend bug when using GDM service was solved as of driver version 515.43.04 === Corrupted screen: "Six screens" Problem ===

For some users, using GeForce GT 100M's, the screen gets corrupted after X starts, divided into 6 sections with a resolution limited to 640x480. The same problem has been reported with Quadro 2000 and hi-res displays.

To solve this problem, enable the Validation Mode  in section :
 Section "Device"
  ...
  Option "ModeValidation" "NoTotalSizeCheck"
  ...
 EndSection

## Invisible text and icons with nvidia-470
An update of GTK4 brought an issue for users relying on the nvidia-470 driver for legacy cards. After the update text and icons randomly disappear and re-appear only after hovering with the mouse over the windows.[https://forums.developer.nvidia.com/t/multiple-apps-do-not-invalidate-repaint-screen-correctly-with-geforce-gt-730-and-v470-driver-on-ubuntu-24-04/291106/2

See the forum for work-arounds.

## Fix graphical corruption in GNOME Shell when resuming from sleep
If you are facing strange fonts and/or having weird graphical glitches in GNOME Shell when resuming from sleep, try setting the following kernel parameter to enable power management:

 nvidia.NVreg_DynamicPowerManagement=0x02

More info: https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/dynamicpowermanagement.html

## System freeze when the display powers off or on resume
If the system freezes or crashes right after the desktop environment turns off the display (DPMS) or when resuming from suspend, and dmesg/journal shows a GSP timeout like:

 NVRM: _kgspLogXid119: ********************************* GSP Timeout **********************************
 NVRM: Xid (PCI:0000:01:00): 119, Timeout after 6s of waiting for RPC response from GPU0 GSP! Expected function 76 (GSP_RM_CONTROL) sequence 1321

the GPU may be dropping to an unstable low clock state during these power transitions.

Workaround: lock a higher minimum GPU/memory clock with nvidia-smi.

Prerequisites:

Enable/start the .

Find supported clock values (use these to pick valid min/max pairs):
 nvidia-smi -q -d SUPPORTED_CLOCKS
 nvidia-smi -q -d CLOCK

Temporary test

Set minimum clocks (example values; adjust to your GPU’s max supported clocks):
 nvidia-smi -lgc 800,2100
 nvidia-smi -lmc 800,10000
 Test DPMS and suspend/resume to see if the issue is resolved.
    To revert:
 nvidia-smi -rgc
 nvidia-smi -rmc

Permanent configuration (systemd)
Create a unit such as :

You can adjust the minimum clock so they are lower than the 800 mentioned earlier to lower idle power consumption; just be aware that setting them to low will cause the issue to occur again.

Then enable/start .

## Performance issues
## Bad performance after installing a new driver version
If FPS have dropped in comparison with older drivers, check if direct rendering is enabled ( is included in ):

 $ glxinfo | grep direct

If the command prints:

 direct rendering: No

A possible solution could be to regress to the previously installed driver version and rebooting afterwards.

## Extreme lag on Xorg
A common issue with Mutter is that animations, video playback and gaming cause extreme desktop lag on Xorg.

See NVIDIA/Tips and tricks#Preserve video memory after suspend.

This should resolve this issue, however if it did not, you are most likely out of luck. One way you can remedy this issue is by adding these options:

turning Sync to VBlank and Allow flipping off within NVIDIA Settings, and configuring NVIDIA Settings to launch on startup using the flag .
This will still result in a laggy desktop behavior, in particular on an eventual second (or third) monitor, but it should be much better.

## CPU spikes with 400 series cards
If you are experiencing intermittent CPU spikes with a 400 series card, it may be caused by PowerMizer constantly changing the GPU's clock frequency. Switching PowerMizer's setting from Adaptive to Performance, add the following to the  section of your Xorg configuration:

  Option "RegistryDwords" "PowerMizerEnable=0x1; PerfLevelSrc=0x3322; PowerMizerDefaultAC=0x1"

## Other issues
## Vulkan error on applications start
On executing an application that require Vulkan acceleration, if you get this error
 Vulkan call failed: -4
try to delete the  or  directory.

## No audio over HDMI
Sometimes NVIDIA HDMI audio devices are not shown when you do

 $ aplay -l

On some new machines, the audio chip on the NVIDIA GPU is disabled at boot. Read more on NVIDIA's website and a forum post.

You need to reload the NVIDIA device with audio enabled. In order to do that make sure that your GPU is on (in case of laptops/Bumblebee) and that you are not running X on it, because it is going to reset:

 # setpci -s 01:00.0 0x488.l=0x2000000:0x2000000
 # rmmod nvidia-drm nvidia-modeset nvidia
 # echo 1 > /sys/bus/pci/devices/0000:01:00.0/remove
 # echo 1 > /sys/bus/pci/devices/0000:00:01.0/rescan
 # modprobe nvidia-drm
 # xinit -- -retro

If you are running your TTY on NVIDIA, put the lines in a script so you do not end up with no screen.

## Backlight is not turning off in some occasions
By default, DPMS should turn off backlight with the timeouts set or by running xset. However, probably due to a bug in the proprietary NVIDIA drivers the result is a blank screen with no powersaving whatsoever. To workaround it, until the bug has been fixed you can use the  as root.

Install the  package.

Turn off your screen on demand and then by pressing a random key backlight turns on again:

 vbetool dpms off && read -n1; vbetool dpms on

Alternatively, xrandr is able to disable and re-enable monitor outputs without requiring root.

 xrandr --output DP-1 --off; read -n1; xrandr --output DP-1 --auto

## HardDPMS
Proprietary driver 415 includes a new feature called HardDPMS. This is reported by some users to solve the issues with suspending monitors connected over DisplayPort.
It is enabled by default since 440.26. If you are using an older driver, the  option can be set in the  or  sections. For example:

 will trigger on screensaver settings like . The following  will set your monitor(s) to suspend after 10 minutes of inactivity:

## xrandr BadMatch
If you are trying to configure a WQHD monitor such as DELL U2515H using xrandr and  gives you the error , it might be because the proprietary NVIDIA driver clips the pixel clock maximum frequency of HDMI output to 225 MHz or lower. To set the monitor to maximum resolution you have to install nouveau drivers. You can force nouveau to use a specific pixel clock frequency by setting  (or ) in your Kernel parameters.

Alternatively, it may be that your monitor's EDID is incorrect. See #Override EDID.

Another reason could be that by default current NVIDIA drivers will only allow modes explicitly reported by EDID, but sometimes refresh rates and/or resolutions are desired which are not reported by the monitor (although the EDID information is correct; it is just that current NVIDIA drivers are too restrictive).

If this happens, you may want to add an option to  to allow non-EDID modes:

This can be set per-output. See README - Appendix B. X Config Options for more information.

## Override EDID
See Kernel mode setting#Forcing modes and EDID, Xrandr#Troubleshooting and  Qnix QX2710#Fixing X11 with Nvidia.

## Overclocking with nvidia-settings GUI not working
Workaround is to use nvidia-settings CLI to query and set certain variables after enabling overclocking (as explained in NVIDIA/Tips and tricks#Enabling overclocking in nvidia-settings, see  for more information).

Example to query all variables:

  nvidia-settings -q all

Example to set PowerMizerMode to prefer performance mode:

  nvidia-settings -a Example to set fan speed to fixed 21%:

 nvidia-settings -a [gpu:0/GPUFanControlState=1 -a Example to set multiple variables at once (overclock GPU by 50MHz, overclock video memory by 50MHz, increase GPU voltage by 100mV):

  nvidia-settings -a GPUGraphicsClockOffsetAllPerformanceLevels=50 -a GPUMemoryTransferRateOffsetAllPerformanceLevels=50 -a GPUOverVoltageOffset=100

## Overclocking not working with Unknown Error
If you are running Xorg as a non-root user and trying to overclock your NVIDIA GPU, you will get an error similar to this one:

To avoid this issue, Xorg has to be run as the root user. See Xorg#Rootless Xorg for details.

## Power draw
Check driver usage:

If power save is configured on the kernel module:

 # rmmod nvidia_drm

## Test software GL
The binary NVIDIA driver will not adhere to the Mesa environment variable  but you can direct libglvnd and EGL to use Mesa by setting the following environment variables:

 __GLX_VENDOR_LIBRARY_NAME=mesa
 __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json

which will result in the Mesa libgl being used for GLX and EGL and result in software GL to see whether a bug is related to the NVIDIA GL library.

## Refresh-rate limited to 120Hz
Newer versions of the driver (after 550xx) [https://bbs.archlinux.org/viewtopic.php?id=302969 seem to waste bandwidth on 8bpc outputs, likely pushing the signal above specification limits and the result is a failure to apply modes with higher refresh rates that otherwise would be within the specification of the output.
Add  to the kernel parameters or set the option via modprobe
Notice that deep color will however be required for HDR monitors.

## Wrong color space on 60hz on Wayland with HDMI
In some cases (like using a HDMI cable with a 1660 Super Graphics Card with 60hz), the driver seems to wrongly assume the color space for the output. This leads to the colors looking darker than normal. Because of there being no easy way to explicitly set the color space on Wayland, as a workaround you can add  to the kernel parameters or set the option via modprobe.
