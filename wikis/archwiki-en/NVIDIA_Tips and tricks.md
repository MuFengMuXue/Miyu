# NVIDIA/Tips and tricks

## Fixing terminal resolution
Since NVIDIA#fbdev is enabled by default, the Linux console should use the native monitor resolution without additional configuration.

If you have disabled  or use an older version of the driver, the resolution may be lower than expected. As a workaround, you can set the resolution in your boot loader configuration.

For GRUB, see GRUB/Tips and tricks#Setting the framebuffer resolution for details. [https://web.archive.org/web/20170405115954/https://www.reddit.com/r/archlinux/comments/4gwukx/nvidia_drivers_and_high_resolution_tty_possible/

For systemd-boot, set  in . See systemd-boot#Loader configuration for details.

For rEFInd, set  in .A small caveat is that this will hide the kernel parameters from being shown during boot.

## Using TV-out
See Wikibooks:NVIDIA/TV-OUT.

## X with a TV (DFP) as the only display
The X server falls back to some "default" screen resolution (usually 640x480) if no monitor is automatically detected. This can be a problem when using a DVI/HDMI/DisplayPort connected TV as the main display, and X is started while the TV is turned off or otherwise disconnected.

To force NVIDIA to use the correct resolution, store a copy of the EDID somewhere in the file system so that X can parse the file instead of reading EDID from the display.

To acquire the EDID, start . It will show some information in tree format, ignore the rest of the settings for now and select the GPU (the corresponding entry should be titled GPU-0 or similar), click the DFP section (again, DFP-0 or similar), click on the Acquire EDID... button and store it somewhere, for example, .

If in the front-end mouse and keyboard are not attached, the EDID can be acquired using only the command line. Run an X server with enough verbosity to print out the EDID block:

 $ startx -- -logverbose 6

After the X server has finished initializing, close it and extract the EDID block from the Xorg log file using nvidia-xconfig:

 $ nvidia-xconfig --extract-edids-from-file ~/.local/share/xorg/Xorg.0.log --extract-edids-output-file ./dfp0.bin

Edit the Xorg configuration by adding to the  section:

The  option forces the driver to recognize the DFP as if it were connected. The  provides EDID data for the device, meaning that it will start up just as if the TV/DFP was connected during the X process.

This way, one can automatically start a display manager at boot time and still have a working and properly configured X screen by the time the TV gets powered on.

## Headless (no monitor) resolution
In headless mode, resolution falls back to 640x480, which is used by VNC or Steam Link. To start in a higher resolution e.g. 1920x1080, specify a  entry under the  subsection in :
 Section "Screen"
    [...
    SubSection     "Display"
        Depth       24
        Virtual     1920 1080
    EndSubSection
 EndSection

## Check the power source
The NVIDIA X.org driver can also be used to detect the GPU's current source of power. To see the current power source, check the 'GPUPowerSource' read-only parameter (0 - AC, 1 - battery):

## Listening to ACPI events
NVIDIA drivers automatically try to connect to the acpid daemon and listen to ACPI events such as battery power, docking, some hotkeys, etc. If connection fails, X.org will output the following warning:

While completely harmless, you may get rid of this message by disabling the  option in your :

 Section "Device"
   ...
   Driver "nvidia"
   Option "ConnectToAcpid" "0"
   ...
 EndSection

If you are on laptop, it might be a good idea to install and enable the acpid daemon instead.

## Displaying GPU temperature in the shell
There are three methods to query the GPU temperature. nvidia-settings requires that you are using X, nvidia-smi or nvclock do not. Also note that nvclock currently does not work with newer NVIDIA cards such as GeForce 200 series cards as well as embedded GPUs such as the Zotac IONITX's 8800GS.

## nvidia-settings
To display the GPU temp in the shell, use nvidia-settings as follows:

The GPU temps of this board is 49 °C.

In order to get just the temperature for use in utilities such as rrdtool or conky:

## nvidia-smi
Use nvidia-smi which can read temps directly from the GPU without the need to use X at all, e.g. when running Wayland or on a headless server.

To display the GPU temperature in the shell, use nvidia-smi:

Only for temperature:

In order to get just the temperature for use in utilities such as rrdtool or conky:

## nvclock
Install the  package.

There can be significant differences between the temperatures reported by nvclock and nvidia-settings/nv-control. According to this post by the author (thunderbird) of nvclock, the nvclock values should be more accurate.

## Overclocking and cooling
## Enabling overclocking in nvidia-settings
Depending on the driver version, some overclocking features are enabled by default. Some unsupported overclocking features need to be enabled via the Coolbits option in the  section:

 Option "Coolbits" "value"

The Coolbits value is the sum of its component bits in the binary numeral system. The component bits are:

*  (bit 3) - Enables additional overclocking settings on the PowerMizer page in nvidia-settings. Available since version 337.12 for the Fermi architecture and newer. *  (bit 4) - Enables overvoltage using nvidia-settings CLI options. Available since version 346.16 for the Fermi architecture and newer. [https://www.phoronix.com/scan.php?page=news_item&px=MTg0MDI

If you use an unsupported version of the driver, you may also need to use these bits:

*  (bit 0) - Enables overclocking of older (pre-Fermi) cores on the Clock Frequencies page in nvidia-settings. Removed in version 343.13.
*  (bit 1) - When this bit is set, the driver will "attempt to initialize SLI when using GPUs with different amounts of video memory". Removed in version 470.42.01.
*  (bit 2) - Enables manual configuration of GPU fan speed on the Thermal Monitor page in nvidia-settings. Removed in version 470.42.01.

To enable multiple features, add the Coolbits values together. For example, to enable overclocking and overvoltage of Fermi cores, set .

The documentation of Coolbits can be found in  and here.

## Setting static 2D/3D clocks
Use kernel module parameters to enable PowerMizer at its maximum performance level (VSync will not work without this):

## Lowering GPU boost clocks
With Volta (NV140/GVXXX) GPUs and later, clock boost works in a different way, and maximum clocks are set to the highest supported limit at boot. If that is what you want, then no further configuration is necessary.

The drawback is the lower power efficiency. As the clocks go up, increased voltage is needed for stability, resulting in a nonlinear increase in power consumption, heating, and fan noise. Lowering the boost clock limit will thus increase efficiency.

Boost clock limits can be changed using nvidia-smi, running as root:

* List supported clock rates:
* Set GPU boost clock limit to 1695 MHz:
* Set Memory boost clock limit to 5001 MHz:

To optimize for efficiency, use nvidia-smi to check the GPU utilization while running your favorite game. VSync should be on. Lowering the boost clock limit will increase GPU utilization, because a slower GPU will use more time to render each frame. Best efficiency is achieved with the lowest clocks that do not cause the stutter that results when the utilization hits 100%. Then, each frame can be rendered just quickly enough to keep up with the refresh rate.

As an example, using the above settings instead of default on an RTX 3090 Ti, while playing Hitman 3 at 4K@60, reduces power consumption by 30%, temperature from 75 to 63 degrees, and fan speed from 73% to 57%.

## Saving overclocking settings
Typically, clock and voltage offsets inserted in the nvidia-settings interface are not saved, being lost after a reboot.
Fortunately, there are tools that offer an interface for overclocking under the proprietary driver, able to save the user's overclocking
preferences and automatically applying them on boot.
Some of them are:

*  - graphical, applies settings on desktop session start
*  and  - graphical, applies settings on system boot
*  - text based, profiles are configuration files in , applies settings on desktop session start

Otherwise,  and  attributes can be set in the command-line interface of nvidia-settings on startup. For example:

 $ nvidia-settings -a "GPUGraphicsClockOffset$ nvidia-settings -a "GPUMemoryTransferRateOffset[performance_level=offset"

Where  is the number of the highest performance level. If there are multiple GPUs on the machine, the GPU ID should be specified: .

## Custom TDP limit
Modern NVIDIA graphics cards throttle frequency to stay in their TDP and temperature limits. To increase performance it is possible to change the TDP limit, which will result in higher temperatures and higher power consumption.

For example, to set the power limit to 160.30W:
 # nvidia-smi -pl 160.30

To set the power limit on boot (without driver persistence):

Now enable the .

## Set fan speed at login
You can adjust the fan speed on your graphics card with nvidia-settings console interface. First ensure that your Xorg configuration has enabled the bit 2 in the Coolbits option.

Place the following line in your xinitrc file to adjust the fan when you launch Xorg. Replace  with the fan speed percentage you want to set.

 nvidia-settings -a "-a "[fan:0/GPUTargetFanSpeed=n"

You can also configure a second GPU by incrementing the GPU and fan number.

 nvidia-settings -a "-a "[fan:0/GPUTargetFanSpeed=n" \
                 -a "-a  [fan:1/GPUTargetFanSpeed=n" &

If you use a login manager such as GDM or SDDM, you can create a desktop entry file to process this setting. Create  and place this text inside it. Again, change  to the speed percentage you want.

 Entry
 Type=Application
 Exec=nvidia-settings -a "-a "[fan:0/GPUTargetFanSpeed=n"
 X-GNOME-Autostart-enabled=true
 Name=nvidia-fan-speed

To make it possible to adjust the fanspeed of more than one graphics card, run:

 $ nvidia-xconfig --enable-all-gpus
 $ nvidia-xconfig --cool-bits=4

## Simple overclocking script using NVML
The Nvidia Management Library (NVML) provides an API that can manage the GPU's core and memory clock offsets and power limit. To utilise this, you can install  and then use the following Python script with your desired settings. This script needs to be run as root after every restart to re-apply the overclock.

## Undervolting with NVML
The NVML API also allows undervolting a GPU, which reduces power consumption and temperatures with minimal performance loss or even a slight gain. This might be specially desirable for laptop users.

Install , create the following script and make it executable:

{{hc|/usr/local/sbin/nvidia-undervolt.py|2=
#!/bin/env python

from pynvml import *
from ctypes import byref

nvmlInit()

# This sets the GPU to adjust - if this gives you errors or you have multiple GPUs, set to 1 or try other values.
myGPU = nvmlDeviceGetHandleByIndex(0)
##print(f"myGPU value: {myGPU}")

# Get the minimum and maximum power values allowed.
##min_power, max_power = nvmlDeviceGetPowerManagementLimitConstraints(myGPU)
##print(f"Allowed range: {min_power} mW to {max_power} mW")

# The power limit can be set below in mW - 216W becomes 216000, etc.
# This value must be within the minimum and maximum allowed power limits.
# Remove or comment out the line below if you do not want to adjust power limits.
nvmlDeviceSetPowerManagementLimit(myGPU, 000000)

# Define the minimum and maximum clocks allowed.
# The clocks supported by your GPU can be verified with:
# nvidia-smi -q -d SUPPORTED_CLOCKS
nvmlDeviceSetGpuLockedClocks(myGPU,210,2340)

####################################
# ============ P0 State ============
####################################

# ============ Memory ============
# Uncomment and edit this section if desired.
# Note: The memory clock offset should be **multiplied by 2**.
# E.g. a desired offset of 500 means inserting
# a value of 1000 in the clockOffsetMHz line.

##infoMemP0 = c_nvmlClockOffset_t()
##infoMemP0.version = nvmlClockOffset_v1
##infoMemP0.type = NVML_CLOCK_MEM
##infoMemP0.pstate = NVML_PSTATE_0
##infoMemP0.clockOffsetMHz = 2000
### This offset is simply how much faster your memory will run.
### E.g. instead of running at 8000 MHz,
### the memory will run at 8000 + (2000 / 2) = 9000 MHz.

##nvmlDeviceSetClockOffsets(myGPU, byref(infoMemP0))

# ============ Graphics =============
infoGraphicsP0 = c_nvmlClockOffset_t()
infoGraphicsP0.version = nvmlClockOffset_v1
infoGraphicsP0.type = NVML_CLOCK_GRAPHICS
infoGraphicsP0.pstate = NVML_PSTATE_0
infoGraphicsP0.clockOffsetMHz = 270
## What this offset means is: The frequency-voltage
## curve is lifted up by 270 MHz.
## E.g. the voltage value originally assigned to 2070 MHz
## will now be used at 2070 + 270 = 2340 MHz.

nvmlDeviceSetClockOffsets(myGPU, byref(infoGraphicsP0))

nvmlShutdown()
}}

The details of the functions used can be read in Section 5.18 of the NVML API documentation. This Reddit post expĺains why the undervolting is done this way, with a clock offset.

This script only applies the undervolt to the GPU's highest P-state. If you want to configure other P-states aside from P0, check this Reddit post for advice.

Run the script manually as root to apply the settings to your GPU and test your configuration. Do not apply your settings permanently unless you have tested them and made sure no problems occur, i.e. your configuration is stable.

After finding a good setup, you need to re-apply it at every boot. One way to do this is with a systemd service:

Finally, enable the service so your settings are applied every time the system boots up.

## Kernel module parameters
Some options can be set as kernel module parameters, a full list can be obtained by running  or looking at . See Gentoo:NVidia/nvidia-drivers#Kernel module parameters as well.

For example, enabling the following will enable the PAT feature which affects how memory is allocated. PAT was first introduced in Pentium III [https://www.kernel.org/doc/ols/2008/ols2008v2-pages-135-144.pdf and is supported by most newer CPUs (see wikipedia:Page attribute table#Processors). If your system can support this feature, it should improve performance.

On some notebooks, to enable any NVIDIA settings tweaking you must include this option, otherwise it responds with "Setting applications clocks is not supported" etc.

## Preserve video memory after suspend
By default the NVIDIA Linux drivers save and restore only essential video memory allocations on system suspend and resume. Quoting NVIDIA:

:The resulting loss of video memory contents is partially compensated for by the user-space NVIDIA drivers, and by some applications, but can lead to failures such as rendering corruption and application crashes upon exit from power management cycles.

Introduced as an "experimental" interface (originally named  in the 430-590 series drivers), it enables saving all video memory (given enough space on disk or RAM). With 595+ drivers, it has been succeeded by the  kernel module parameter which needs to be set to save and restore all video memory contents.

While NVIDIA does not set these by default, Arch Linux does so for the supported drivers, making preserve work out of the box.

To verify that  is enabled, execute the following:

 # sort /proc/driver/nvidia/params

Which should have a line  , and also , which you can read about below. Drivers prior 595, should have a line  for the same.

In the older 430-590 series drivers, the services , , and  are required and enabled by default, as per upstream requirements.

The aforementioned services are disabled by default on 595+ drivers, as per upstream requirements, as video memory preservation is now handled by kernel suspend notifiers, making the nvidia suspend/hibernate services unnecessary.

See NVIDIA's documentation for more details.

## Dynamic Boost
Dynamic Boost is a system-wide power controller which manages GPU and CPU power, according to the workload on the system. It can particularly improve performance in GPU-bound applications by raising the power limit accordingly.

The main requirement is laptops with Ampere (or newer) GPUs.

See CPU frequency scaling#nvidia-powerd for detailed instructions.

## Driver persistence
NVIDIA has a daemon that can be optionally run at boot. In a standard single-GPU X desktop environment the persistence daemon is not needed and can actually create issues [https://devtalk.nvidia.com/default/topic/1044421/linux/nvidia-persistenced-causing-60-second-reboot-delays. See the Driver Persistence section of the NVIDIA documentation for more details.

To start the persistence daemon at boot, enable the . For manual usage see the upstream documentation.

## Forcing YCbCr with 4:2:0 subsampling
If you are facing limitations of older output standards that can still be mitigated by using YUV 4:2:0, the NVIDIA driver has an undocumented X11 option to enforce that:

 Option "ForceYUV420" "True"

This will allow higher resolutions or refresh rates but will have detrimental impact on the image quality.

## Configure applications to render using GPU
See PRIME#Configure applications to render using GPU.
