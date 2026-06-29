# AMDGPU

AMDGPU is the open source graphics driver for AMD Radeon graphics cards since the Graphics Core Next family.

## Selecting the right driver
Identify your hardware and find the right driver by reading Graphics processing unit#Installation. This driver supports Southern Islands (GCN 1, released in 2012) cards and later. AMD has no plans to support pre-GCN GPUs.

Owners of unsupported GPUs may use the open source ATI driver.

## Installation
Install the  package, which provides both the DRI driver for 3D acceleration and VA-API/VDPAU drivers for accelerated video decoding.

* For 32-bit application support, also install the  package from the multilib repository.
* For 2D acceleration under Xorg, you may optionally install the  package, which provides the AMD-specific DDX driver. Most Xorg systems using the  kernel driver will work correctly with the generic modesetting DDX built into . However,  could be required for features such as  or to resolve hardware-specific issues on some AMD hardware, like Southern Islands. Read the Note at Intel graphics#Installation.
* For Vulkan support install  ( for 32-bit applications).

## Experimental
It may be worthwhile for some users to use the upstream experimental build of mesa.

Install the  package, which provides the DRI driver for 3D acceleration.

* For 32-bit application support, also install the  package from the mesa-git repository or the AUR.
* For the DDX driver (which provides 2D acceleration in Xorg), install the  package.
* For Vulkan support using the mesa-git repository, install the vulkan-radeon-git package. Optionally install the lib32-vulkan-radeon-git package for 32-bit application support. This should not be required if building  from the AUR.

## Enable Southern Islands (SI) and Sea Islands (CIK) support
Officially supported kernels enable AMDGPU support for cards of the Southern Islands (GCN 1, released in 2012) and Sea Islands (GCN 2, released in 2013). The  kernel driver needs to be loaded before the radeon one. You can check which kernel driver is loaded by running . It should be like this:

If the  driver is not in use, follow instructions in the next section.

## Load amdgpu driver
The module parameters of both  and  modules are  and .

They need to be set as kernel parameters or in a modprobe configuration file, and depend on the cards GCN version.

You can use both parameters if you are unsure which kernel card you have.

## Set module parameters in kernel command line
Set one of the following kernel parameters:

* Southern Islands (SI):
* Sea Islands (CIK):

Furthermore, if you are using an AMD A10 APU with an integrated Sea Island (GCN 1.1) card, you may have to disable Radeon Dynamic Power Management to get a proper boot. This is a feature that dynamically re-clocks the graphics core in order to keep the APU cooler and quieter, however this feature may put you in an infinite restart loop. To disable it, following the instructions above, add  to the boot options.

## Specify the correct module order
Make sure  has been set as first module in the Mkinitcpio#MODULES array, e.g. .

## Set kernel module parameters
For Southern Islands (SI) use the  kernel module parameter, for Sea Islands (CIK) use :

Make sure  is in the  array in  and regenerate the initramfs.

## Compile kernel which supports amdgpu driver
When building or compiling a kernel,  and/or  should be set in the config.

## ACO compiler
The ACO compiler is an open source shader compiler created and developed by Valve Corporation to directly compete with the LLVM compiler, as well as Windows 10. It offers lesser compilation time and also performs better while gaming than LLVM.

Some benchmarks can be seen on GitHub and Phoronix [https://www.phoronix.com/scan.php?page=article&item=radv-aco-gcn10&num=1.

Since  version 20.2 ACO is the default shader compiler.

## Loading
The  kernel module is supposed to load automatically on system boot.

If it does not:

* Make sure to #Enable Southern Islands (SI) and Sea Islands (CIK) support when needed.
* Make sure you have the latest  package installed. This driver requires the latest firmware for each model to successfully boot.
* Make sure you do not have  or  as a kernel parameter, since  requires KMS.
* Check that you have not disabled  by using any kernel module blacklisting.

It is possible it loads, but late, after the X server requires it. In this case see Kernel mode setting#Early KMS start.

## Xorg configuration
Xorg will automatically load the driver and it will use your monitor's EDID to set the native resolution. Configuration is only required for tuning the driver.

If you want manual configuration, create , and add the following:

Using this section, you can enable features and tweak the driver settings, see  first before setting driver options.

## Tear free rendering
TearFree controls tearing prevention using the hardware page flipping mechanism. By default, TearFree will be on for rotated outputs, outputs with RandR transforms applied, and for RandR 1.4 slave outputs, and off for everything else. Or you can configure it to be always on or always off with  or  respectively.

 Option "TearFree" "true"

You can also enable TearFree temporarily with xrandr:

 $ xrandr --output output --set TearFree on

Where  should look like  or  and can be acquired by running .

## DRI level
DRI sets  the maximum level of DRI to enable. Valid values are 2 for DRI2 or 3 for DRI3. The default is 3 for DRI3 if the Xorg version is >=  1.18.3, otherwise DRI2 is used:

 Option "DRI" "3"

## Variable refresh rate
See Variable refresh rate.

## 10-bit color
Newer AMD cards support 10bpc color, but the default is 24-bit color and 30-bit color must be explicitly enabled. Enabling it can reduce visible banding/artifacts in gradients, if the applications support this too. To check if your monitor supports it search for "EDID" in your Xorg log file (e.g.  or ):

 [   336.695] (II) AMDGPU(0): EDID for output DisplayPort-0
 [   336.695] (II) AMDGPU(0): EDID for output DisplayPort-1
 [   336.695] (II) AMDGPU(0): Manufacturer: DEL  Model: a0ec  Serial#: 123456789
 [   336.695] (II) AMDGPU(0): Year: 2018  Week: 23
 [   336.695] (II) AMDGPU(0): EDID Version: 1.4
 [   336.695] (II) AMDGPU(0): Digital Display Input
 [   336.695] (II) AMDGPU(0): 10 bits per channel

To check whether it is currently enabled search for "Depth"):

 [   336.618] (**) AMDGPU(0): Depth 30, (--) framebuffer bpp 32
 [   336.618] (II) AMDGPU(0): Pixel depth = 30 bits stored in 4 bytes (32 bpp pixmaps)

With the default configuration it will instead say the depth is 24, with 24 bits stored in 4 bytes.

To check whether 10-bit works, exit Xorg if you have it running and run  which will display a black and white grid, then press  and  to exit X, and run . If this works fine, then 10-bit is working.

To launch in 10-bit via , use . To permanently enable it, create or add to:

## Reduce output latency
If you want to minimize latency you can disable page flipping and tear free:

See Gaming#Reducing DRI latency to further reduce latency.

## Features
## Video acceleration
See Hardware video acceleration#AMD/ATI.

## Monitoring
Monitoring your GPU is often used to check the temperature and also the P-states of your GPU. See Graphics processing unit#Monitoring for a list of CLI and GUI tools.

If you want to manually monitor individual elements, for example to use them within scripts, all the information is available in . For additional elements and details see The Linux Kernel - GPU Power/Thermal Controls and Monitoring.

For the commands below,  may need replaced with another value (E.g., ) depending on the number of GPUs in the system.

To check your GPU's P-states, execute:

 $ cat /sys/class/drm/card0/device/pp_od_clk_voltage

To monitor your GPU, execute:

 # watch -n 0.5 cat /sys/kernel/debug/dri/0/amdgpu_pm_info

To check your GPU utilization (%), execute:

 $ cat /sys/class/drm/card0/device/gpu_busy_percent

To check your GPU frequency, execute:

 $ cat /sys/class/drm/card0/device/pp_dpm_sclk

To check your GPU temperature (millidegrees Celsius), execute:

 $ cat /sys/class/drm/card0/device/hwmon/hwmon*/temp1_input

To check your VRAM frequency, execute:

 $ cat /sys/class/drm/card0/device/pp_dpm_mclk

To check your VRAM usage (bytes), execute:

 $ cat /sys/class/drm/card0/device/mem_info_vram_used

To check your VRAM size (bytes), execute:

 $ cat /sys/class/drm/card0/device/mem_info_vram_total

## Overclocking
Since Linux 4.17, once you have enabled the features at boot below, it is possible to adjust clocks and voltages of the graphics card via .

## Boot parameter
It is required to unlock access to adjust clocks and voltages in sysfs by appending the Kernel parameter .

Not all bits are defined, and new features may be added over time. Setting all 32 bits may enable unstable features that cause problems such as screen flicker or broken resume from suspend. It should be sufficient to set the PP_OVERDRIVE_MASK bit, 0x4000, in combination with the default ppfeaturemask. To compute a reasonable parameter for your system, execute:

 $ printf 'amdgpu.ppfeaturemask=0x%x\n' "$(($(cat /sys/module/amdgpu/parameters/ppfeaturemask) | 0x4000))"

## Manual
For in-depth information on all possible options, read the kernel documentation for amdgpu thermal control.

To enable manual overclocking, select the  performance level as described in #Performance levels.

To set the GPU clock for the maximum P-state 7 on e.g. a Polaris GPU to 1209MHz and 900mV voltage, run:

 # echo "s 7 1209 900" > /sys/class/drm/card0/device/pp_od_clk_voltage

The same procedure can be applied to the VRAM, e.g. maximum P-state 2 on Polaris 5xx series cards:

 # echo "m 2 1850 850" > /sys/class/drm/card0/device/pp_od_clk_voltage

To apply, run:

 # echo "c" > /sys/class/drm/card0/device/pp_od_clk_voltage

To check if it worked out, read out clocks and voltage under 3D load:

 # watch -n 0.5 cat /sys/kernel/debug/dri/0/amdgpu_pm_info

You can reset to the default values using:

 # echo "r" > /sys/class/drm/card0/device/pp_od_clk_voltage

It is also possible to forbid the driver from switching to certain P-states, e.g. to workaround problems with deep powersaving P-states, such as flickering artifacts or stutter. To force the highest VRAM P-state on a card, while still allowing the GPU itself to run with lower clocks, first find the highest possible P-state, then set it:

 # echo "manual" > /sys/class/drm/card0/device/power_dpm_force_performance_level
 # echo "3" >  /sys/class/drm/card0/device/pp_dpm_mclk

Allow only the three highest GPU P-states:

 # echo "5 6 7" > /sys/class/drm/card0/device/pp_dpm_sclk

To set the allowed maximum power consumption of the GPU to e.g. 50 Watts, run:

 # echo 50000000 > /sys/class/drm/card0/device/hwmon/hwmon0/power1_cap

## Assisted
If you are not inclined to fully manually overclock your GPU, there are some overclocking tools that are offered by the community to assist you to overclock and monitor your AMD GPU.

## CLI tools
*
*

## GUI tools
*
*
*
*

## Startup on boot
One way is to use systemd units, if you want your settings to apply automatically upon boot, consider looking at this Reddit thread to configure and apply your settings on boot.

Another way is to use udev rules for some of the values, for example, to set a low performance level to save energy:

{{hc|/etc/udev/rules.d/30-amdgpu-low-power.rules|2=
ACTION=="add", SUBSYSTEM=="drm", DRIVERS=="amdgpu", ATTR{device/power_dpm_force_performance_level}="low"
}}

## Performance levels
AMDGPU offers several performance levels,  the file power_dpm_force_performance_level is used for this, it is possible to select between these levels:

* auto: dynamically select the optimal power profile for current conditions in the driver.
* low: clocks are forced to the lowest power state.
* high: clocks are forced to the highest power state.
* manual: user can manually adjust which power states are enabled for each clock domain (used for setting #Power profiles)
* profile_standard, profile_min_sclk, profile_min_mclk, profile_peak: clock and power gating are disabled and the clocks are set for different profiling cases. This mode is recommended for profiling specific work loads

To set the AMDGPU device to use a low performance level, the following command can be executed:

 # echo "low" > /sys/class/drm/card0/device/power_dpm_force_performance_level

## Power profiles
AMDGPU offers several optimizations via power profiles, one of the most commonly used is the compute mode for OpenCL intensive applications. Available power profiles can be listed with:

To use a specific power profile you should first enable manual control over them with:

 # echo "manual" > /sys/class/drm/card0/device/power_dpm_force_performance_level

Then to select a power profile by writing the NUM field associated with it, e.g. to enable COMPUTE run:

 # echo "5" > /sys/class/drm/card0/device/pp_power_profile_mode

The exact values and limits of power profiles is managed through the powerplay table system. Use  to modify the table for supported models (Polaris to Navi2x; Navi3x and Navi4x are bugged on kernel side).

## Enable GPU display scaling
To avoid the usage of the scaler which is built in the display, and use the GPU own scaler instead, when not using the native resolution of the monitor, execute:

 $ xrandr --output output --set "scaling mode" scaling_mode

Possible values for  are: , , , .

* To show the available outputs and settings, execute:
* To set  for just every available output, execute:

## Virtual display on headless setups
AMDGPU offers GPU accelerated virtual monitors for headless setups without the use of a dummy plug. This is useful for RDP and game streaming software such as .

Choose the AMD GPU to use:

Add the  kernel module parameter for the  module, where  is the PCI address of the GPU and  is the number of crtc (virtual monitors) to expose. Using this parameter also disables physical outputs. Multiple GPUs can also be used by separating PCI address with a semicolon (;) as shown below:

 amdgpu.virtual_display=1234:56:78.9,x;9876:54:32.1,y

## User queues
The AMDGPU driver supports user queues, which allow job submission directly to the GPU hardware without going through the kernel driver’s command submission ioctl.
Enabling this can reduce latency and improve efficiency by bypassing some kernel driver overhead.

To enable user queues, set the following environment variable:

 export AMD_USERQ=1

To verify it is active, check the  parameter:

 $ cat /sys/module/amdgpu/parameters/user_queue

It should return . If it returns  or , the hardware or driver version is likely incompatible.

## Dedicated transfer-only Queue using SDMA
The code merged for Mesa 26.0 has the RADV dedicated transfer queue support working on GFX9 (Vega) and newer GPUs. Enabling this feature currently requires the  environment variable to be set. The DXVK Direct3D-on-Vulkan layer is among the software able to benefit from the Vulkan transfer queues support although there are no performance/benchmark numbers noted in [https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/25594 the merge request for quantifying the benefit of the new functionality.

## Troubleshooting
## Module parameters
The amdgpu module stashes several config parameters () in masks that are only documented in the kernel sources.

## Xorg or applications will not start
* "(EE) AMDGPU(0): DRI2SwapBuffers: drawable has no back or front?" error after opening glxgears, can open Xorg server but OpenGL applications crash.
* "(EE) AMDGPU(0): Given depth (32) is not supported by amdgpu driver" error, Xorg will not start.

Setting the screen's depth under Xorg to 16 or 32 will cause problems/crash. To avoid that, you should use a standard screen depth of 24 by adding this to your "screen" section:

## Screen artifacts and frequency problem
Dynamic power management may cause screen artifacts to appear when displaying to monitors at higher frequencies (anything above 60Hz) due to issues in the way GPU clock speeds are managed[https://bugs.freedesktop.org/show_bug.cgi?id=96868A workaround [https://bugs.freedesktop.org/show_bug.cgi?id=96868#c13 is to set the  or  performance level as described in #Performance levels.

Changing the kernel version can also help eliminate this issue. For example, it appears to be fixed in 6.12.9.

## Artifacts in Chromium
If you see artifacts in Chromium, forcing the vulkan-based backend might help. Go to  and enable  and .

## R9 390 series poor performance and/or instability
If you experience issues with a AMD R9 390 series graphics card, set  as kernel parameters to force the use of amdgpu driver instead of radeon.

If it still does not work, disabling DPM might help, add  to the kernel parameters.

## Freezes with "[drm IP block:gmc_v8_0 is hung!" kernel error
If you experience freezes and kernel crashes during a GPU intensive task with the kernel error " IP block:gmc_v8_0 is hung!" [https://gitlab.freedesktop.org/drm/amd/issues/226, a workaround is to set  as kernel parameters to force the GPUVM page tables update to be done using the CPU. Downsides are listed here === Screen flickering white/gray ===

When you change resolution or connect to an external monitor, if the screen flickers or stays white, add  as a kernel parameter.

## System freeze or crash when gaming on Vega cards
Dynamic power management may cause a complete system freeze whilst gaming due to issues in the way GPU clock speeds are managed. [https://gitlab.freedesktop.org/drm/amd/-/issues/716 A workaround is to set the  performance level as described in #Performance levels.

## WebRenderer (Firefox) corruption
Artifacts and other anomalies may present themselves (e.g. inability to select extension options) when WebRenderer is force enabled by the user. Workaround is to fall back to OpenGL compositing.

## Double-speed or "chipmunk" audio, or no audio when a 4K@60Hz device is connected
This is sometimes caused by a communication issue between an AMDGPU device and a 4K display connected over HDMI. A possible workaround is to enable HDR or "Ultra HD Deep Color" via the display's built-in settings. On many Android based TVs, this means setting this to "Standard" instead of "Optimal".

## Issues with power management / dynamic re-activation of a discrete amdgpu graphics card
If you encounter issues where the kernel driver is loaded, but the discrete graphics card still is not available for games or becomes disabled during use (similar to you can workaround the issue by setting the kernel parameter , which prevents the dGPU from being powered down dynamically at runtime.

## Frozen or unresponsive display (flip_done timed out)
A bug in the amdgpu driver may stop the display from updating [https://gitlab.freedesktop.org/drm/amd/-/issues/4141. It is suggested to append the  or  kernel parameter as a workaround.

## kfd fails to initialize
kfd can fail to initialize depending on the GPU's architecture. gfx803 (GCN 4) requires PCIe atomics support, while gfx9xx (Vega) and later devices does not require PCIe atomics. kfd does not support GCN 3 or older devices.

If you are not planning to use ROCm, these errors can be safely ignored.

## "Core Name not supported in kfd"
In the system journal or the kernel message keyring a critical level error message may appear relating to kfd:

(Replace BONAIRE with the name of the core that's in your GPU, such as TOPAZ, HAWAII, etc. You can find the core name by looking up your GPU or by using a GPU diagnostic utility such as )

This means that your GPU is not supported in kfd and will not work with ROCm.==== "PCI rejects atomics" ====

On GCN 4 GPUs, your CPU must support PCIe atomics and the slot that the GPU is in supports at least PCIe 3.0.[https://github.com/ROCm/ROCm/issues/2224#issuecomment-2299689450 If these requirements are not met, you will encounter this message:
{{hc|# dmesg  grep kfd|
kfd kfd: amdgpu: skipped device 1002:67e3, PCI rejects atomics 730
 kernel:  dump_stack_lvl+0x47/0x60
 kernel:  warn_alloc+0x165/0x1e0
 kernel:  __alloc_pages_slowpath.constprop.0+0xd7d/0xde0
 kernel:  __alloc_pages+0x32d/0x350
 kernel:  ttm_pool_alloc+0x19f/0x600 0bd92a9d9dccc3a4f19554535860aaeda76eb4f4

As a workaround, a userspace service can ensure to allocate enough RAM for the VRAM to be buffered by swapping out enough RAM before the system is suspended.

## Wrong GPU clocks causing multiple issues
There is a bug in the amdgpu module, due to which the video core frequencies can be higher than those declared by the manufacturer, which can cause system instability during the game, when exiting sleep, when rebooting.

The problem has been noticed on RDNA 3 GPUs (7XXX Models) [https://wiki.gentoo.org/wiki/AMDGPU#Frequent_and_Sporadic_Crashes In dmesg you can see logs like theese:

 amdgpu: [gfxhub page fault (src_id:0 ring:40 vmid:6 pasid:32830)
 amdgpu:  in process GameThread pid 100056 thread vkd3d_queue pid 100468)
 amdgpu:   in page starting at address 0x0000000218a36000 from client 10
 amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00641051
 amdgpu:          Faulty UTCL2 client ID: TCP (0x8)
 amdgpu:          MORE_FAULTS: 0x1
 amdgpu:          WALKER_ERROR: 0x0
 amdgpu:          PERMISSION_FAULTS: 0x5
 amdgpu:          MAPPING_ERROR: 0x0
 amdgpu:          RW: 0x1

If you have similar problems, check the maximum frequency of the video core in the system with what is stated by the manufacturer. To decrease maximum frequency, refer to #Overclocking.

## AMD dedicated GPU HDMI freezing issue on Wayland
As an example, the ASUS G14 2022 laptop which as has AMD CPU and dedicated AMD GPU. The most successful approach requires to use armor crate on Windows to enforce dGPU Ultimate power options. It's switching GPU order and laptop internal power policies. Since that change HDMI should be working but user is going to experience separate rendering for integrated GPU (which SDDM and Wayland somehow pick by default) and dedicated GPU. User can obviously add  it this case before launching any application but its not convenient. Extending configuration to presented one allows flawless experience in expense of shorter battery life when running on battery.

Additionally kernel command line should be extended with

 amdgpu.runpm=0 amdgpu.modeset=1

## Colors appear washed out and dim on laptops
Power-saving applications such as  and  have started to enable a feature known as Panel Power Savings (PPS).

PPS is a featured supported on Laptops in which the laptop's GPU is instructed to have a lower color accuracy in the name of saving power. This, however, leads to washed out colors whenever selecting more aggressive power-saving modes on the aforementioned power-profiles-daemon and tuned. Therefore, there is interest in disabling this feature entirely.

It can be done by setting the following kernel parameter to zero:

 amdgpu.abmlevel=0

## System freezes or reboots when idle
Issues with some PowerPlay features, such as GFXOFF can cause frequent, unrecoverable driver crashesThey coincide with idle GPU usage on a multi-monitor setup, and especially waking up from sleep mode.

A well-known solution is appending a kernel parameter (as described in #Boot parameter) that disables PP_GFXOFF_MASK, for example  - this particular one leaves all other (implemented and unimplemented) PowerPlay features enabled.

Alternative solutions rely on disabling more features than just GFXOFF:
* Disable [https://www.reddit.com/r/linux4noobs/comments/1ahb8pf/comment/koppio6/ PP_GFXOFF_MASK and PP_STUTTER_MODE with ,
* Disable PP_GFXOFF_MASK, PP_STUTTER_MODE and PP_OVERDRIVE_MASK with ,
* Disable PP_GFXOFF_MASK, PP_GFX_DCS_MASK and PP_OVERDRIVE_MASK with ,
* Disable every feature with  (or ). This can be used if the cause of driver crashes is unknown.

You can create your own feature mask from  followed by an 8-character mask calculated with a hexadecimal bitwise calculator (example included). Start the mask with  (all bits enabled) XOR the feature to mask. You can keep "XORing" more features to the result. You can skip zeroes before the first non-zero character: for example, 0x8000 is equivalent to 0x00008000.

Make sure the parameter does not get removed during kernel updates.

## HDMI 4K capped at 120hz
Due to licensing issues the  driver cannot support HDMI 2.1. You must use DisplayPort. If your display does not support DisplayPort, some users have reported success with converter devices that take DisplayPort input and output HDMI 2.1 signals.
