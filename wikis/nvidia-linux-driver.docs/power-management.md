## Chapter 21. Configuring Power Management Support

## Background

The NVIDIA Linux driver includes support for the suspend (suspend-to-RAM) and hibernate (suspend-to-disk) system power management operations, such as ACPI S3 and S4 on the x86_64 platform. When the system suspends or hibernates, the NVIDIA kernel drivers prepare in-use GPUs for the sleep cycle, saving state required to return these GPUs to normal operation when the system is later resumed. The NVIDIA Linux driver also supports S0ix-based s2idle system suspend (suspend-to-idle), if both the platform and the NVIDIA GPU support it.

The GPU state saved by the NVIDIA kernel drivers includes allocations made in video memory. However, these allocations are collectively large, and typically cannot be evicted. Since the amount of system memory available to drivers at suspend time is often insufficient to accommodate large portions of video memory, the NVIDIA kernel drivers are designed to act conservatively, and normally only save essential video memory allocations.

The resulting loss of video memory contents is partially compensated for by the user-space NVIDIA drivers, and by some applications, but can lead to failures such as rendering corruption and application crashes upon exit from power management cycles.

To better support power management with these types of applications, the NVIDIA Linux driver provides a custom power management interface intended for integration with system management tools like **systemd**. This interface is still considered experimental. It is not used by default, but can be taken advantage of by configuring the system as described in this chapter.

## Overview

The NVIDIA Linux driver supports the suspend and hibernate power management operations via two different mechanisms. In this section, each is summarized briefly with its capabilities and requirements:

`Kernel driver callback`
When this mechanism is used, the NVIDIA kernel driver receives callbacks from the Linux kernel to suspend, hibernate, and to resume each GPU for which a Linux PCI driver was registered. This is the default mechanism: it is enabled and used without explicit configuration.

While this mechanism has no special requirements, yields good results with many workloads, and has been supported by the NVIDIA kernel driver in similar form for years, it suffers from a few limitations. Notably, it can only preserve a relatively small amount of video memory reliably, and it cannot support power management when advanced CUDA features are being used.

`/proc/driver/nvidia/suspend`
Instead of callbacks from the Linux kernel, this mechanism, when used, relies on a system management tool, such as **systemd**, to issue suspend, hibernate, and resume commands to the NVIDIA kernel driver via the `/proc/driver/nvidia/suspend` interface. It is still considered experimental, and requires explicit configuration to use.

If configured correctly, this mechanism is designed to remove the limitations of the kernel driver callback mechanism. It supports power management with advanced CUDA features (such as UVM), and it is capable of saving and restoring all video memory allocations.

## Preserve all video memory allocations

To save potentially large portions of video memory, the NVIDIA driver supports the following two methods:

`Save allocations in an unnamed temporary file`
The NVIDIA driver uses an unnamed temporary file to save potentially large portions of video memory. By default, this file is created in `/tmp` during system suspend. This location can be changed with the `NVreg_TemporaryFilePath` nvidia.ko kernel module parameter, e.g.`NVreg_TemporaryFilePath=/run`. The destination file system needs to support unnamed temporary files, and it needs to be large enough to accommodate all the utilized video memory copies for the duration of the power management cycle.

When determining a suitable size for the video memory backing store, it is recommended to start with the overall amount of video memory supported by the GPUs installed in the system. For example: `nvidia-smi -q -d MEMORY |grep 'FB Memory Usage' -A1`. Each `Total` line returned by this command reflects one GPU's video memory capacity, in MiB. The sum of these numbers, plus 5% of margin, is a conservative starting point for the size of the video memory backing store.

Please note that file systems such as `/tmp` and `/run` are often of the type `tmpfs`, and potentially relatively small. Most commonly, the size of the type of the file system used is controlled by **systemd**. For more information, see https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems. To achieve the best performance, file system types other than `tmpfs` are recommended at this time.

Additionally, to unlock the full functionality of the interface, the NVIDIA Linux kernel module `nvidia.ko` needs to be loaded with the `NVreg_PreserveVideoMemoryAllocations=1` module parameter. This changes the default video memory save/restore strategy to save and restore all video memory allocations. Also, the `/proc/driver/nvidia/suspend` power management mechanism (with a system management tool, such as **systemd**) is required for using this interface.`S0ix-based power management`
If both the platform and the NVIDIA GPU support S0ix-based power management, then the NVIDIA Linux driver will put the GPU video memory in self refresh mode during **s2idle** system suspend. S0ix-based suspend will consume more power than legacy S3 system suspend, but it will enter and exit suspend/resume more quickly. Also, the suspend/resume latency will be constant irrespective of GPU video memory usage.

To check the platform S0ix state support and required configuration, follow the steps mentioned in [how-achieve-s0ix-states-linux](https://web.archive.org/web/20230614200816/https://01.org/blogs/qwang59/2018/how-achieve-s0ix-states-linux)

To check if the NVIDIA GPU has support for S0ix-based power management, install the NVIDIA driver and run the following command:

`grep 'Video Memory Self Refresh' /proc/driver/nvidia/gpus/<Domain>:<Bus>:<Device>.0/power`

For example:

`grep 'Video Memory Self Refresh' /proc/driver/nvidia/gpus/0000\:01\:00.0/power`

If both the platform and the GPU support S0ix-based power management, then the S0ix support can be enabled in the NVIDIA Linux driver by setting the `nvidia.ko` kernel module parameter `NVreg_EnableS0ixPowerManagement` to "1". With `NVreg_EnableS0ixPowerManagement` set to "1" and system suspend state set to **s2idle**, the NVIDIA Linux driver will calculate the video memory usage at system suspend time.

- During the S0ix suspend, if video memory usage is less than a certain threshold, then the driver will copy video memory contents to system memory and power off the video memory along with the GPU. This will help in saving power.

- During the S0ix suspend, if video memory usage is above a certain threshold, then the video memory will be kept in self-refresh mode while the rest of the GPU is powered down.

By default, this threshold is 256 MB and it can be changed with the `NVreg_S0ixPowerManagementVideoMemoryThreshold` module parameter of `nvidia.ko`.

All the module parameters can be set on the command line when loading the NVIDIA Linux kernel module `nvidia.ko`, or via the distribution's kernel module configuration files (such as those under /etc/modprobe.d).

## **systemd** Configuration

This section is specific to the `/proc/driver/nvidia/suspend` interface. This is required if using the `NVreg_PreserveVideoMemoryAllocations=1` kernel module parameter or advanced CUDA features (such as UVM). The NVIDIA Linux kernel driver requires no configuration if the default power management mechanism is used.

In order to take advantage of the `/proc` interface, a system management tool like **systemd** needs to be configured to access it at appropriate times in the power management sequence. Specifically, the interface needs to be used to suspend or hibernate the NVIDIA kernel drivers just before writing to the Linux kernel's `/sys/power/state` interface to request entry into the desired sleep state. The interface also needs to be used to resume the NVIDIA kernel drivers immediately after the return from a sleep state, as well as immediately after any unsuccessful attempts to suspend or hibernate.

The following example configuration documents integration with the **systemd** system and service manager, which is commonly used in modern GNU/Linux distributions to manage system start-up and various aspects of its operation. For systems not using **systemd**, the configuration files provided serve as a reference.

The **systemd** configuration uses the following files:

`/usr/lib/systemd/system/nvidia-suspend.service`
A **systemd** service description file used to instruct the system manager to write `suspend` to the `/proc/driver/nvidia/suspend` interface immediately before accessing `/sys/power/state` to suspend the system.`/usr/lib/systemd/system/nvidia-suspend-then-hibernate.service`
A **systemd** service description file used to instruct the system manager to write `suspend` to the `/proc/driver/nvidia/suspend` interface immediately before accessing `/sys/power/state` to suspend the system.

The **suspend-then-hibernate** suspend method requires systemd version 248 or higher.

`/usr/lib/systemd/system/nvidia-hibernate.service`
A **systemd** service description file used to instruct the system manager to write `hibernate` to the `/proc/driver/nvidia/suspend` interface immediately before accessing `/sys/power/state` to hibernate the system.`/usr/lib/systemd/system/nvidia-resume.service`
A **systemd** service description file used to instruct the system manager to write `resume` to the `/proc/driver/nvidia/suspend` interface immediately after returning from a system sleep state.`/lib/systemd/system-sleep/nvidia`
A **systemd-sleep** script file used to instruct the system manager to write `resume` to the `/proc/driver/nvidia/suspend` interface immediately after an unsuccessful attempt to suspend or hibernate the system via the `/proc/driver/nvidia/suspend` interface.

For the **suspend-then-hibernate** method of system sleep, this script is responsible for resuming and then hibernating the GPU if the system wakes due to a low battery warning. This feature requires systemd version 248 or newer.

`/usr/bin/nvidia-sleep.sh`
A shell script used by the **systemd** service description files and the **systemd-sleep** file to interact with the `/proc/driver/nvidia/suspend` interface. The script also manages VT switching for the X server, which is currently needed by the NVIDIA X driver to support power management operations.

These files are installed and enabled by nvidia-installer automatically if systemd is detected. Installation of systemd units can be disabled by specifying the **--no-systemd** installer option.

## Exercising power management with **systemd**

This section is specific to the `/proc/driver/nvidia/suspend` interface, when configured as described above. When the default power management mechanism is used instead, or when the `/proc` interface is used without **systemd**, then the use of `systemctl` is not required.

To suspend (suspend-to-RAM) or to hibernate (suspend-to-disk), respectively, use the following commands:

- `sudo systemctl suspend`

- `sudo systemctl hibernate`

For the full list of sleep operations supported by **systemd**, please see the systemd-suspend.service(8) man page.

## Known Issues and Workarounds

- On some systems, where the default suspend mode is `"s2idle"`, the system may not resume properly due to a known timing issue in the kernel. The suspend mode can be verified by reading the contents of the file `/sys/power/mem_sleep`. The following upstream kernel changes have been proposed to fix the issue:

  https://lore.kernel.org/linux-pci/20190927090202.1468-1-drake@endlessm.com/

  https://lore.kernel.org/linux-pci/20190821124519.71594-1-mika.westerberg@linux.intel.com/

  In the interim, the default suspend mode on the affected systems should be set to `"deep"` using the kernel command line parameter `"mem_sleep_default"` -

  **mem_sleep_default=deep**
