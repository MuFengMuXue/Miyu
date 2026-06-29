## Chapter 22. PCI-Express Runtime D3 (RTD3) Power Management

## Introduction

NVIDIA GPUs have many power-saving mechanisms. Some of them will reduce clocks and voltages to different parts of the chip, and in some cases turn off clocks or power to parts of the chip entirely, without affecting functionality or while continuing to function, just at a slower speed.

However, the lowest power states for NVIDIA GPUs require turning power off to the entire chip, often through ACPI calls. Obviously, this impacts functionality. Nothing can run on the GPU while it is powered off. Care has to be taken to only enter this state when there are no workloads running on the GPU and any attempts to start work or any memory mapped I/O (MMIO) access must be preceded with a sequence to first turn the GPU back on and restore any necessary state.

The NVIDIA GPU may have one, two or four PCI functions:

- Function 0: VGA controller / 3D controller

- Function 1: Audio device

- Function 2: USB xHCI Host controller

- Function 3: USB Type-C UCSI controller

Out of the four PCI functions, the NVIDIA driver directly manages the VGA controller / 3D Controller PCI function. Other PCI functions are managed by the device drivers provided with the Linux kernel. The NVIDIA driver is capable of handling entry into and exit from these low power states, for the PCI function 0. The remaining PCI functions are also powered down along with function 0 when entering these low power states. As a result, the device drivers for the other three functions also need to be taken into account to:

- prevent entering the lowest-power state when the device is in use,
- trigger exiting the lowest-power state when the device is needed,
- save and restore any hardware state around power-off events.

The NVIDIA Linux driver includes support for dynamically managing power to the NVIDIA GPU. It depends on the runtime power management framework within the Linux kernel to arbitrate power needs of various PCI functions. In order to have maximum power saving from this feature, two conditions must be met:

1\. Runtime power management for all the PCI functions of the GPU should be enabled.

2\. The device drivers for all the PCI functions should support runtime power management.

If these conditions are satisfied and if all the PCI functions are idle, then The NVIDIA GPU will go to the lowest power state resulting into maximum power savings.

## Supported Configurations

This feature is available only when the following conditions are satisfied:

- This feature is supported on notebooks and desktops.

- This feature requires system hardware as well as ACPI support (ACPI "\_PR0" and "\_PR3" methods are needed to control PCIe power). The necessary hardware and ACPI support was first added in Intel Coffeelake chipset series. Hence, this feature is supported from Intel Coffeelake chipset series.

- This feature requires a Turing or newer GPU.

- This feature is supported with Linux kernel versions 4.18 and newer. With older kernel versions, it may not work as intended.

- This feature is supported when Linux kernel defines CONFIG_PM (CONFIG_PM=y). Typically, if the system supports S3 (suspend-to-RAM), then CONFIG_PM would be defined.

## System Settings

1.  Enable runtime power management for each PCI function.

    For Ampere or later notebooks with supported configurations, runtime D3 power management is enabled by default for the GPU's PCI function 0 (VGA controller / 3D controller).

    For pre-Ampere notebooks and all desktop SKUs, runtime D3 power management can be enabled for each PCI function using the following command.

    **echo auto \> /sys/bus/pci/devices/\<Domain\>:\<Bus\>:\<Device\>.\<Function\>/power/control**

    For example:

    **echo auto \> /sys/bus/pci/devices/0000\\01\\00.0/power/control**

## Driver Settings

This feature is enabled by default on supported Ampere or newer notebook computers. In all other configurations, it is disabled by default.

It can be enabled or disabled via the `NVreg_DynamicPowerManagement` nvidia.ko kernel module parameter.`Option "NVreg_DynamicPowerManagement=0x00"`
This setting will disable runtime D3 power management features. With this setting, the NVIDIA driver will only use the GPU's built-in power management so it always is powered on. Actual power usage will vary with the GPU's workload.

`Option "NVreg_DynamicPowerManagement=0x01"`
This setting is called coarse-grained power control. With this setting, the NVIDIA GPU driver will allow the GPU to go into its lowest power state when no applications are running that use the nvidia driver stack. Whenever an application requiring NVIDIA GPU access is started, the GPU is put into an active state. When the application exits, the GPU is put into a low power state.

`Option "NVreg_DynamicPowerManagement=0x02"`
This setting is called fine-grained power control. With this setting, the NVIDIA GPU driver will allow the GPU to go into its lowest power state when no applications are running that use the nvidia driver stack. Whenever an application requiring NVIDIA GPU access is started, the GPU is put into an active state. When the application exits, the GPU is put into a low power state.

Additionally, the NVIDIA driver will actively monitor GPU usage while applications using the GPU are running. When the applications have not used the GPU for a short period, the driver will allow the GPU to be powered down. As soon as the application starts using the GPU, the GPU is reactivated.

Furthermore, the NVIDIA GPU driver controls power to the NVIDIA GPU and its video memory separately. While turning off the NVIDIA GPU, the video memory will be kept in a low power self-refresh mode unless the following conditions are met:

- The NVIDIA GPU does not support "Video Memory Self Refresh" mode but supports "Video Memory Off" mode. See [the section called “Procfs Interface For Runtime D3”](dynamicpowermanagement.html#Procfs "Procfs Interface For Runtime D3") for details.

- The system is configured in PRIME render offload mode. See [Chapter 35, *PRIME Render Offload*](primerenderoffload.html "Chapter 35. PRIME Render Offload") for details.

- Less than a certain threshold of video memory is in use. The default threshold value is 200 MB. See [the section called “Video Memory Utilization Threshold”](dynamicpowermanagement.html#VidMemThreshold "Video Memory Utilization Threshold") for details.

- Sufficient system memory is available for saving the video memory contents.

If these conditions are met, the NVIDIA GPU driver will completely turn off the video memory, in addition to the rest of the GPU.

Keeping video memory in a self-refresh mode uses more power than turning off video memory, but allows the GPU to be powered off and reactivated more quickly.

It is important to note that the NVIDIA GPU will remain in an active state if it is driving a display. In this case, the NVIDIA GPU will go to a low power state only when the X configuration option [HardDPMS](xconfigoptions.html#HardDPMS) is enabled and the display is turned off by some means - either automatically due to an OS setting or manually using commands like **xset**.

Similarly, the NVIDIA GPU will remain in an active state if a CUDA application is running.

`Option "NVreg_DynamicPowerManagement=0x03"`
This is the default setting.

For Ampere or later notebooks with supported configurations, this value translates to fine-grained power control. For pre-Ampere notebooks, this value disables runtime D3 power management features. For desktop computers, irrespective of the GPU(s) used, this value disables runtime D3 power management features.

Option `NVreg_DynamicPowerManagement` can be set on the command line while loading the NVIDIA Linux kernel module. For example,

**modprobe nvidia "NVreg_DynamicPowerManagement=0x02"**

## Video Memory Utilization Threshold

The NVIDIA GPU driver uses 200 MB as the default video memory utilization threshold to decide whether the video memory can be turned off or kept in a self-refresh mode. This threshold value can be decreased or increased (up to 1024 MB) using an option `NVreg_DynamicPowerManagementVideoMemoryThreshold`. This option can be set on the command line while loading the NVIDIA Linux kernel module. For example,

**modprobe nvidia "NVreg_DynamicPowerManagementVideoMemoryThreshold=100"**

The video memory utilization threshold value should be a positive integer. It is expressed in Megabytes (1048576 bytes). In the example above, the threshold value will be set to 100 MB. The maximum threshold value can be 1024 MB. Any value greater than 1024 MB will be clamped to 1024 MB.

The use of a higher threshold value will increase the latency during RTD3 entry and exit transitions, so use this option only if the latency increase is not affecting the usability of the system.

This threshold can be set to 0 in order to prevent the video memory from being turned off.

## Procfs Interface For Runtime D3

The following entries in the file `/proc/driver/nvidia/gpus/PCI-BUS-ID/power` provide more details regarding the runtime D3 feature. See [“What is the format of a PCI Bus ID?”](faq.html#busid) for information on how to determine the PCI-BUS-ID.

- "Runtime D3 status" entry gives the current status of this feature.

- "Video Memory" entry gives the power status of the video memory.

- "Video Memory Self Refresh" entry reports whether the NVIDIA GPU hardware supports video memory self refresh mode.

- "Video Memory Off" entry reports whether the NVIDIA GPU hardware supports video memory off mode.

## Known Issues And Workarounds

The first two workarounds in the below section are not required on Linux kernel 5.5 or newer.

1.  The USB xHCI Host controller and USB Type-C UCSI controller drivers present in most Linux distributions do not fully support runtime power management. Full support for runtime power management in these drivers is available in kernel version 5.5. For kernel versions before 5.5, these two PCI functions have to be disabled for this feature to work properly. This can be done using the following command.

    **echo 1 \> /sys/bus/pci/devices/\<Domain\>:\<Bus\>:\<Device\>.2/remove**

    **echo 1 \> /sys/bus/pci/devices/\<Domain\>:\<Bus\>:\<Device\>.3/remove**

    For example:

    **echo 1 \> /sys/bus/pci/devices/0000\\01\\00.2/remove**

    **echo 1 \> /sys/bus/pci/devices/0000\\01\\00.3/remove**

2.  There is a known issue with the audio driver due to which the audio PCI function remains in an active state. This affects Linux kernel versions 4.19 (starting with git commit id `37a3a98ef601f89100e3bb657fb0e190b857028c` ) through 5.4, and is fixed in Linux kernel version 5.5.

    **echo 1 \> /sys/bus/pci/devices/\<Domain\>:\<Bus\>:\<Device\>.1/remove**

    For example:

    **echo 1 \> /sys/bus/pci/devices/0000\\01\\00.1/remove**

    This workaround will result in audio loss when the audio function is being used to play audio over DP/HDMI connection. To recover from audio loss, rescanning the PCI tree will bring back the audio PCI function and audio operation can be recovered. However, after rescanning the PCI tree, all the disabled PCI functions will again become active. To ensure that this feature works again, the workarounds mentioned in this section have to be done again.

3.  When the NVIDIA GPU is driving a console, runtime power management is enabled for the VGA Controller PCI function and nvidia driver is uninstalled, the console will become blank. The workaround for this issue is to disable runtime power management for PCI function 0 before uninstalling the NVIDIA driver using the following command:

    **echo on \> /sys/bus/pci/devices/\<Domain\>:\<Bus\>:\<Device\>.\<Function\>/power/control**

    For example:

    **echo on \> /sys/bus/pci/devices/0000\\01\\00.0/power/control**

4.  On desktops, if a NVIDIA GPU is in RTD3 state and a display is connected to it, it will not be detected. This is because the parent PCI/e port switches off the power to the NVIDIA GPU. The workaround for this issue is to first put the NVIDIA GPU into an active state and then connect the display to it. The NVIDIA GPU can be brought into an active state by running the following command:

    **echo on \> /sys/bus/pci/devices/\<Domain\>:\<Bus\>:\<Device\>.\<Function\>/power/control**

    For example:

    **echo on \> /sys/bus/pci/devices/0000\\01\\00.0/power/control**

    After connecting the display, runtime power management can be enabled again using the following command:

    **echo auto \> /sys/bus/pci/devices/\<Domain\>:\<Bus\>:\<Device\>.\<Function\>/power/control**

    For example:

    **echo auto \> /sys/bus/pci/devices/0000\\01\\00.0/power/control**

5.  On systems where nvidia persistence daemon is running with UVM persistence mode enabled, PCI-Express Runtime D3 (RTD3) Power Management will be disabled. This is because in uvm persistence mode some UVM driver components are kept initialized even when the GPU is not in active use. This prevents the GPU from entering RTD3 low power state.

## Automated Setup

This section describes automated ways to perform the manual steps mentioned above so that this feature works seamlessly after boot.

1.  Create a file named `80-nvidia-pm.rules` in `/lib/udev/rules.d/` directory.

    Add the content given below to `80-nvidia-pm.rules` file. This would enable runtime power management for the VGA Controller / 3D Controller PCI function. It would also remove Audio device PCI function, USB xHCI Host Controller function as well as USB Type-C UCSI Controller PCI function. Note that the first three rules given below are not required from Linux kernel 5.5 and newer.

``` screen
    # Remove NVIDIA USB xHCI Host Controller devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c0330", ATTR{remove}="1"

    # Remove NVIDIA USB Type-C UCSI devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c8000", ATTR{remove}="1"

    # Remove NVIDIA Audio devices, if present
    ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x040300", ATTR{remove}="1"

    # Enable runtime PM for NVIDIA VGA/3D controller devices on driver bind
    ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="auto"
    ACTION=="bind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="auto"

    # Disable runtime PM for NVIDIA VGA/3D controller devices on driver unbind
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030000", TEST=="power/control", ATTR{power/control}="on"
    ACTION=="unbind", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030200", TEST=="power/control", ATTR{power/control}="on"

```

2.  The driver option `NVreg_DynamicPowerManagement` can be set via the distribution's kernel module configuration files, such as those under `/etc/modprobe.d`. For example, the following line can be added to `/etc/modprobe.d/nvidia.conf` to seamlessly enable this feature:

    ```
    options nvidia "NVreg_DynamicPowerManagement=0x02"
    ```

3.  Reboot the system.
