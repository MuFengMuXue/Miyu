# Ryzen

Ryzen is a brand of microprocessors  manufactured by Advanced Micro Devices (AMD). This article covers system configuration and troubleshooting information for different generations of the CPU.

## Enable microcode support
Install the  package to enable microcode updates and enable it with the help of the Microcode page. These updates provide bug fixes that can be critical to the stability of your system. It is highly recommended to use it despite it being proprietary.

## Tweaking Ryzen
## Voltage, power and temperature monitoring
 should be able to monitor temperatures out of the box. However, for more detailed information such as power consumption and voltage,  is needed. For GUI based monitoring tools, use  or  for Zen 3 CPUs.

## Power management, undervolting and overclocking
*
*
*
*

## AMD 3D V-Cache scheduling (multi-CCD CPUs)
On CPUs with asymmetric CCDs (e.g. 7950X3D, 9950X3D), one CCD has 3D V-Cache (larger L3,
better for gaming) and one has higher clock speeds. The  driver
(kernel 6.13+) exposes a scheduling bias via sysfs.

First, set CPPC Dynamic Preferred Cores to  in the UEFI (on MSI boards:
).
Without this, the sysfs override has no effect.

The recommended setup is to leave the system in  mode (default), so the
OS and background tasks prefer the faster non-X3D CCD, and pin games explicitly to the
X3D cores:

 # echo frequency > /sys/bus/platform/drivers/amd_x3d_vcache/AMDI0101:00/amd_x3d_mode

To identify which cores are the X3D cores, read the prefcore rankings, in
mode the X3D cores will have the lowest rankings:

 $ grep -r '' /sys/devices/system/cpu/cpu*/cpufreq/amd_pstate_prefcore_ranking

On the 9950X3D these are cpu0–7 and cpu16–23. For native Linux games pin them via
the Steam launch option:

 taskset -c 0-7,16-23 %command%

For Proton/Wine games,  does not propagate into the Steam Proton
container (pressure-vessel). Use  instead:

 WINE_CPU_TOPOLOGY=16:0,1,2,3,4,5,6,7,16,17,18,19,20,21,22,23 %command%

The format is .

## Compiling a kernel
See Gentoo:Ryzen#Kernel on enabling Ryzen support. The officially supported kernels have the required configuration by default.

## Troubleshooting
## Random reboots
See Gentoo:Ryzen#Random_reboots_with_mce_events if you are experiencing random reboots.

With Ryzen 5000 series, particularly the higher-end models of 5950X and 5900X there seem to be some slight instability issues under Linux, related possibly to the 5.11+ kernel, as shown by this kernel bug. After investigating and reading reports on the Internet, It seems that out of the box, Windows seems to run the CPUs at higher voltage and lower peak frequencies, compared to the stock linux kernel, which depending on your draw from the silicon lottery could cause a host of random application crashes or hardware errors that lead to reboots. You will recognise those by dmesg logs that look like:

 kernel: mce: Error: Machine check events logged
 kernel: mce: Error: CPU 22: Machine Check: 0 Bank 1: bc800800060c0859
 kernel: mce: Error: TSC 0 ADDR 7ea8f5b00 MISC d012000000000000 IPID 100b000000000
 kernel: mce: Error: PROCESSOR 2:a20f10 TIME 1636645367 SOCKET 0 APIC d microcode a201016

The CPU ID and the Processor number may vary. To solve this problem you need to supply higher voltage to your CPU so that it is stable when running at peak frequencies. The easiest way to achieve this is to use the AMD curve optimiser which is accessible via your motherboard's UEFI. Access it and put a positive offset of 4 points, which will increase the voltage your CPU is getting at higher loads. It will limit overclocking potential due to higher heat dissipation requirements, but it will run stable. For more details check this forum post. When I did this for my 5950X, my processor stabilised and the frequency and voltage ranges were more similar to those observed under windows.

## System halts
Within similar context of #Random reboots, systems might halt under heavy or specific low loads, even after applying the fixes. Reset button or forced shutdowns don't work, peripherals powers off, video output might stop, and unplugging is the only way out of this state.

Reducing frequencies to within non-overclocked standards and increasing voltages of CPU or RAM helps, but might not fix the issue. A potential fix is to update the UEFI (also misnamed "BIOS updates"), and then apply the PBO+4 curve for more stability on higher frequencies. Per silicon lottery, some CPUs might need +6 or higher offsets.

## Screen-tearing (APU)
If you are using Xorg and are experiencing screen-tearing, see AMDGPU#Tear free rendering.

## Soft lock freezing
This bug is well known and is being discussed on bugzilla and launchpad. While the solution is not the same in all cases, this one helped some users. Add the output of this command  as a kernel parameter where the command  just prints your CPU's threads. For this option to be applied, you need a compiled kernel with option  (like ).

A different cause for the freezes is the power saving management indicated by c-states. The maximum power saving state c6 can cause problems. Adding the kernel parameter  helped in some cases but other users reported that the option is not applied and the c6 state is still entered. For them, disabling C6 states through a helper script relying on  helped. Before using it,  needs to be run in order to activate that kernel module.

Some laptops with Ryzen CPUs such as the HP Envy x360 15-bq100na may experience CPU soft locks which result in a frozen system. These can be avoided with the kernel parameter  added.

In some cases, kernel parameter  fixes the issue.

In some other cases, the issue is simply bad hardware, and warranty claiming the CPU for a new one may just solve your issues.

## Freeze on shutdown, reboot and suspend
This issue is strongly linked to the C6 CPU idle state, which can cause instability on Linux, particularly when used with power supplies or motherboards that do not handle ultra-low current draw well.

To mitigate this, enter the UEFI setup:

* Locate the setting called  (or similar).
* Change it from  to .
* This disables deeper idle states (such as C6), allowing only C1 and C2. While this slightly increases power consumption, it significantly improves system stability.

If your motherboard does not offer this setting, or if issues persist, alternative workarounds include:

* Fully disabling C-states in UEFI (if available, though not always recommended).
* Adding the following kernel parameter to limit CPU idle state:

Disabling deep C-states may raise idle power consumption by approximately 5–10 W, but typically resolves issues with suspend, reboot, and shutdown on affected systems.
