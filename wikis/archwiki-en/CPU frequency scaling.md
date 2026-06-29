# CPU frequency scaling

CPU performance scaling enables the operating system to scale the CPU frequency up or down in order to save power or improve performance. Scaling can be done automatically in response to system load, adjust itself in response to ACPI events, or be manually changed by user space programs.

The Linux kernel offers CPU performance scaling via the CPUFreq subsystem, which defines two layers of abstraction:

* Scaling governors implement the algorithms to compute the desired CPU frequency, potentially based off of the system's needs.
* Scaling drivers interact with the CPU directly, enacting the desired frequencies that the current governor is requesting.

A default scaling driver and governor are selected automatically, but userspace tools like cpupower, acpid, Laptop Mode Tools, or GUI tools provided for your desktop environment, may still be used for advanced configuration.

## Userspace tools
## i7z
 is an i7 (and now i3, i5, i7, i9) CPU reporting tool for Linux. It can be launched from a Terminal with the command  or as GUI with .

## turbostat
 can display the frequency, power consumption, idle status and other statistics of the modern Intel and AMD CPUs.

## cpupower
 is a set of userspace utilities designed to assist with CPU frequency scaling. The package is not required to use scaling, but is highly recommended because it provides useful command-line utilities and a systemd service to change the governor at boot.

The configuration file for cpupower is located in . This configuration file is read by a bash script in  which is activated by systemd with . You may want to enable  to start at boot.

## thermald
 is a Linux daemon used to prevent the overheating of Intel CPUs. This daemon proactively controls thermal parameters using P-states, T-states, and the Intel power clamp driver. thermald can also be used for older Intel CPUs. If the latest drivers are not available, then the daemon will revert to x86 model specific registers and the Linux "cpufreq subsystem" to control system cooling.

By default, it monitors CPU temperature using available CPU digital temperature sensors and maintains CPU temperature under control, before hardware takes aggressive correction action. If there is a skin temperature sensor in thermal sysfs, then it tries to keep skin temperature under 45C.

On Tiger Lake laptops (e.g. Dell Latitude 3420), this daemon has been reported as unlocking more performance than what would be otherwise available.

The associated systemd unit is , which should be started and enabled. See  for more information.

## power-profiles-daemon
The powerprofilesctl command-line tool from  handles power profiles (e.g. balanced, power-saver, performance) through the  service. GNOME and KDE also provide graphical interfaces for profile switching; see the following:

* GNOME#Power modes
* KDE#Power management

See the project's README for more information on usage, use cases, and comparisons with similar projects.

Start/enable the  service. Note that when powerprofilesctl is launched, it also attempts to start the service (see the unit status of ).

## tuned
 is a daemon for monitoring and adaptive tuning of system devices. It can configure GPU power modes, PCIe power management, set sysctl settings, adjust kernel scheduling and more; a daemon that also configures out aspects of power management in the system.

As of release 2.23.0, the project ships with , a compatibility layer for programs written for , such as the following:

* GNOME#Power modes
* KDE#Power management

For reasons why tuned should be used instead of power-profiles-daemon, see Fedora's proposal to replace it with tuned. For opposite arguments, see Start/enable the  daemon service. For power-profiles-daemon compatibility, also start/enable the  service. To control tuned from the command line, use  to view and set profiles.

## cpupower-gui
 is a graphical utility designed to assist with CPU frequency scaling. The GUI is based on GTK and is meant to provide the same options as cpupower. cpupower-gui can enable or disable cores and change the maximum/minimum CPU frequency and governor for each core. The application handles privilege granting through polkit and allows any logged-in user in the  user group to change the frequency and governor. See [https://github.com/vagnum08/cpupower-gui?tab=readme-ov-file#systemd-units cpupower-gui systemd units for more information on  and .

## gnome-shell-extension-cpupower
 is a GNOME shell extension that can alter minimum/maximum CPU frequencies and enable/disable frequency boosting.

## auto-cpufreq
 is an automatic CPU speed and power optimizer for Linux based on active monitoring of laptop's battery state, CPU usage, CPU temperature and system load.

## nvidia-powerd
The nvidia-powerd daemon provides support for NVIDIA's Dynamic Boost technology on supported laptop platforms. It acts as a system-wide power controller that dynamically redistributes power between the GPU and CPU based on workload demands, while maintaining the system's total thermal budget. Start/enable the  service, which is provided by the  package.

## Scaling drivers
Scaling drivers implement controls over frequency scaling by interfacing with the CPU hardware. The driver is the hardware interface that communicates with the governor which dictates policy for generic frequency control.

However  and  (active mode) implement their own internal control logic, sometimes bypassing traditional governors.

The ACPI 2.0 standard introduced power-performance states ("P-states")), but can also have additional features (such as Hardware-based P-States, which allow the CPU to govern frequency autonomously).[https://docs.kernel.org/admin-guide/pm/cpufreq.html#cpu-performance-scaling-in-linux

{| class="wikitable"
!  !! Description
|-
|   || Utilizes ACPI power-performance states (P-States). This driver also supports the Intel Enhanced SpeedStep (previously supported by the deprecated  module). For AMD Ryzen, it only provides 3 frequency states.
|-
|  || This driver has three modes corresponding to different degrees of autonomy from the CPU hardware: active, passive, and guided. Kernel 6.5 changed defaults to AMD P-State active (EPP) mode for supported Ryzen systems with CPPC support. However not all systems enable it automatically and server platforms may still default to . See #amd_pstate for details.
|-
|  || EPP-based variant of the  driver used in active mode.
|-
|  || Based on ACPI's newer CPPC system (see #Collaborative processor performance control). Common default on AArch64 systems. Works on modern x86 too, but the  and  drivers implement additional hardware-specific features.
|-
|  || Reported  when  is in "passive mode"|-
|  || Modern frequency scaling driver for Intel processors (Sandy Bridge and newer). It is used automatically for these processors instead of the other drivers below. This driver takes priority over other drivers and is built-in as opposed to being a module. By default,  will select "Active Mode" if the processor supports hardware-managed P-States (HWP), called Speed Shift Technology (SST) by Intel (Skylake processors and newer). If the processor doesn't support HWP (or if using the  parameter) then  will select "Passive Mode" and the reported  string will be "". If you encounter a problem while using this driver, you can revert to  scaling driver by adding  to your Kernel parameters. See the [https://docs.kernel.org/admin-guide/pm/intel_pstate.html  documentation for more details.
|-
|  || CPUFreq driver for Intel Pentium 4/Xeon/Celeron processors which lowers the CPU temperature by skipping clocks. (You probably want to use  instead, an internal helper library used by legacy Intel SpeedStep drivers.)
|-
|  || This driver supports Processor Clocking Control interface by Hewlett-Packard and Microsoft Corporation which is useful on some ProLiant servers.
|-
|  || CPUFreq driver for K8/K10 Athlon 64/Opteron/Phenom processors. Since Linux 3.7, 'acpi_cpufreq' will automatically be used for more modern AMD CPUs.
|-
|  || CPUFreq driver for Intel SpeedStep-enabled processors (mostly Atoms and older Pentiums)
|}

To see a full list of available modules, run:

 $ ls /usr/lib/modules/$(uname -r)/kernel/drivers/cpufreq/

To view drivers built-in to the current kernel, query its config:
 $ zgrep -E 'CONFIG_X86_(INTEL_PSTATE|AMD_PSTATE|ACPI_CPUFREQ|PCC_CPUFREQ|POWERNOW_K8|P4_CLOCKMOD)=/proc/config.gz

Load the appropriate module (see Kernel modules for details). Once the appropriate cpufreq driver is loaded, detailed information about the CPU(s) can be displayed by running

 $ cpupower frequency-info

## Setting maximum and minimum frequencies
In some cases, it may be necessary to manually set maximum and minimum frequencies.

To set the maximum clock frequency ( is a clock frequency with units: GHz, MHz):

 # cpupower frequency-set -u clock_freq

To set the minimum clock frequency:

 # cpupower frequency-set -d clock_freq

To set the CPU to run at a specified frequency:

 # cpupower frequency-set -f clock_freq

Alternatively, you can set the frequency manually:

 # echo value | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq

The available values can be found in  or similar. [https://web.archive.org/web/20201029114421/https://software.intel.com/sites/default/files/comment/1716807/how-to-change-frequency-on-linux-pub.txt

## Configuring frequency boosting
Some processors support raising their frequency above the normal maximum for a short burst of time, under appropriate thermal conditions. On Intel processors, this is called Turbo Boost, and on AMD processors this is called Turbo-Core.

## Setting via sysfs (intel_pstate)
intel_pstate has a driver-specific interface for prohibiting the processor from entering turbo P-States:

 # echo 1 > /sys/devices/system/cpu/intel_pstate/no_turbo

## Setting via sysfs (other scaling drivers)
For scaling drivers other than , if the driver supports boosting, the  attribute will be present, and can be used to disable/enable boosting.

To disable boosting, run:
 # echo 0 > /sys/devices/system/cpu/cpufreq/boost
To enable boosting, run:
 # echo 1 > /sys/devices/system/cpu/cpufreq/boost

## Setting via x86_energy_perf_policy
On Intel processors,  can also be used to configure Turbo Boost:

 # x86_energy_perf_policy --turbo-enable 0

## amd_pstate
 has three operation modes: CPPC autonomous (active) mode, CPPC non-autonomous (passive) mode and CPPC guided autonomous (guided) mode. Officially supported kernels are built with  which means the default for them is the active mode. This can be changed with the kernel parameter ,  or . To revert to the  driver, set  instead.

; Active mode
: The  mode is implemented by  (Energy Performance Preference) driver. In this mode, the  driver provides a hint to the hardware when software wants to bias the CPPC firmware towards performance (0x0) or power efficiency (0xff).
; Passive mode
: The  mode is implemented by the  driver. In this mode, the driver defines a desired performance based on the current workload, and specifically how much performance degradation can be tolerated without affecting quality of life.
; Guided mode
: The  mode is implemented by the  driver. In this mode, the  driver requests minimum and maximum performance level and the platform autonomously selects a performance level in this range and appropriate to the current workload.

## Scaling governors
Scaling governors are power schemes determining the desired frequency for the CPU. Some request a constant frequency, others implement algorithms to dynamically adjust according to the system load. The governors included in the kernel are:

{| class="wikitable"
! Governor !! Description
|-
| performance  || Run the CPU at the maximum frequency, obtained from .
|-
| powersave    || Run the CPU at the minimum frequency, obtained from .
|-
| userspace    || Run the CPU at user specified frequencies, configurable via .
|-
| ondemand     || Scales the frequency dynamically according to current load. Jumps to the highest frequency and then possibly back off as the idle time increases.
|-
| conservative || Scales the frequency dynamically according to current load. Scales the frequency more gradually than ondemand.
|-
| schedutil    || Scheduler-driven CPU frequency selection [https://lore.kernel.org/lkml/1614814.usHvZ58O6A@vostro.rjw.lan/.
|}

Depending on the scaling driver, one of these governors will be loaded by default:

*  since Linux 4.9.5
* the internal  governor for Intel and AMD CPUs using the  and  driver respectively (see the note above, it is equivalent to ).

To activate a particular governor, run:

 # cpupower frequency-set -g governor

Alternatively, you can activate a governor on every available CPU manually:

 # echo governor | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

## Tuning the ondemand governor
See the kernel documentation for details.

## Switching threshold
To set the threshold for stepping up to another frequency:

 # echo -n percent > /sys/devices/system/cpu/cpufreq/governor/up_threshold

To set the threshold for stepping down to another frequency:

 # echo -n percent > /sys/devices/system/cpu/cpufreq/governor/down_threshold

## Sampling rate
The sampling rate determines how frequently the governor checks to tune the CPU.  is a tunable that multiplies the sampling rate when the CPU is at its highest clock frequency, thereby delaying load evaluation and improving performance. Allowed values for  are 1 to 100000.  This tunable has no effect on behavior at lower CPU frequencies/loads.

To read the value (default = 1), run:

 $ cat /sys/devices/system/cpu/cpufreq/ondemand/sampling_down_factor

To set the value, run:

 # echo -n value > /sys/devices/system/cpu/cpufreq/ondemand/sampling_down_factor

## Make changes permanent
Since Linux 5.9, it is possible to set the  kernel option.To set the desired scaling parameters at boot, configure the cpupower utility and enable its systemd service. Alternatively, systemd-tmpfiles or udev rules can be used.

## Autonomous frequency scaling
Both Intel and AMD define a way to have the CPU decide its own speed based on (1) a performance range from the system and (2) a performance/power hint specifying the preference. The fully-autonomous mode is activated when:

*  is set to "active"—requires CPPC support in both the CPU and BIOS,
*  is set to "active" and hardware P-state (HWP) is available (i.e. Sandy Bridge and newer)—works out-of-the-box.

The most important feature of active governing is that only two governors appear available,  and . They do not work at all like their normal counterpart, however: these levels are translated into an Energy Performance Preference hint for the CPU's internal governor. As a result, they both provide dynamic scaling, similar to the  or  generic governors respectively, differing mostly in latency. The  algorithm [https://www.phoronix.com/scan.php?page=news_item&px=MTM3NDQ should give better power saving functionality than the old ondemand governor for Intel HWP.

## Intel active, non-HWP
The intel-pstate driver has, confusingly, an "active" mode that works without the CPU's active decision. This mode turns on when kernel cmdline forces an "active" mode but HWP is unavailable or disabled. It will still only provide  and , but the driver itself does the governing in a way similar to  and  (i.e. it stays at the maximum P-state). There is no real benefit to this mode compared to passive intel-pstate.

## Setting the EPP
It is possible to select in-between hints with the sysfs interfaces available. The interface is identical between AMD and Intel, where the files  describe the current preference and  providing a list of available preferences. One can also pass a number between 0 (favor performance) and 255 (favor power). A fallback implementation is provided for Intel CPUs without EPP, translating strings to EPB levels (described in next section) but failing on numbers.

 supports configuration of EPP hints via the  switch on Intel CPUs only. It works via direct access of machine-specific registers (MSRs) which differ between Intel and AMD. The program can also restrict the range of HWP frequencies using a range of frequency multipliers.

To enable hardware P-States with :

 # x86_energy_perf_policy -H 1
 # x86_energy_perf_policy -U 1

## Collaborative processor performance control
The power consumption of modern CPUs is no longer simply dependent on the frequency or voltage setting, as there are modules that can be switched on as needed. Collaborative processor performance control (CPPC) is the P-state replacement provided by ACPI 5.0. Instead of defining a table of static frequency levels, the processor provides many abstract performance levels and the operating system selects from these levels. There are two advantages:

* There is no longer a limit of 16 P-state entries; a typical CPU provides hundreds of levels to choose from.
* The CPU can provide a higher frequency (e.g. boost) for a performance level when certain parts (e.g. vector FPU) is not used.

On the other hand, the flexible frequency breaks frequency-invariant utilization tracking, which is important for fast frequency changes by . A number of vendor-specific methods have been used to make the frequency static under CPPC, with most successes coming from arm64.

 is the generic CPPC scaling driver.  also uses ACPI CPPC to manage the CPU frequency when the Zen 3 MSR is unavailable – this method, also called "shared memory", has higher latency than MSR.

## Intel performance and energy bias hint
The Intel performance and energy bias hint (EPB) is an interface provided by Intel CPUs to allow for user space to specify the desired power-performance tradeoff, on a scale of 0 (highest performance) to 15 (highest energy savings). The EPB register is another layer of performance management functioning independently from frequency scaling. It influences how aggressive P-state and C-state selection will be, and informs internal model-specific decision making that affects energy consumption.

Common values and their aliases, as recognized by sysfs and  are:

{| class="wikitable"
! EPB value
! String
|-
| 0
| performance
|-
| 4
| balance-performance
|-
| 6
| normal, default
|-
| 8
| balance-power
|-
| 15
| power
|}

## Setting via sysfs
The EPB can be set using a sysfs attribute:

 # echo epb | tee /sys/devices/system/cpu/cpu*/power/energy_perf_bias

## Setting via x86_energy_perf_policy
With :

 # x86_energy_perf_policy --epb epb

## Setting via cpupower
With :

 # cpupower set -b epb_value

## Interaction with ACPI events
Users may configure scaling governors to switch automatically based on different ACPI events such as connecting the AC adapter or closing a laptop lid. A quick example is given below; however, it may be worth reading full article on acpid.

Events are defined in . If the  package is installed, the file should already exist and be executable. For example, to change the scaling governor from  to  when the AC adapter is disconnected and change it back if reconnected:

## Troubleshooting
## BIOS frequency limitation
Some CPU and BIOS configurations are unable to reach their maximum frequency or scale to higher frequencies at all. This is most likely caused by BIOS events telling the OS to limit the frequency resulting in  set to a lower value.

Before blaming the BIOS implementation, verify you have not manually set the CPU frequency limits, thermal management preferences, or other relevant options in the BIOS Setup Utility.

On some devices (e.g. IBM/Lenovo Thinkpads), usage with a failing battery (or it removed) coupled with an undersized AC adapter may trigger a BIOS-enforced CPU frequency limit. See ThinkWiki.

You can tell the kernel to ignore the limitations: set the  kernel parameter. For trying this temporarily, change the value in  from  to .

Some systems use a different mechanism to limit the CPU frequency when running without battery or an unofficial power adapter. On Intel CPUs, you can manipulate the BD PROCHOT bit in Intel CPUs as explained in Lenovo ThinkPad T480#CPU stuck at minimum frequency and Dell XPS 15 (9560)#General slowness & stuttering. These steps may also apply to other devices, like Intel-based MacBooks running at the minimum CPU frequency without a battery.
