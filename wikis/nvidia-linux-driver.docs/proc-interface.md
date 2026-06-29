## Chapter 20. Using the `/proc` File System Interface

The NVIDIA `/proc` file system interface can be used to obtain run-time information about the NVIDIA kernel driver and about the NVIDIA GPUs present in the system. It can also be used to control some aspects of the NVIDIA driver's operation.

This information is contained in several files in `/proc/driver/nvidia`:`/proc/driver/nvidia/version`
Lists the installed driver revision and the version of the GNU C compiler used to build the Linux kernel module.

`/proc/driver/nvidia/warnings`
The NVIDIA graphics driver tries to detect potential problems with the host system's kernel and warns about them using the kernel's `printk()` mechanism, typically logged by the system to `/var/log/messages`.

Important NVIDIA warning messages are also logged to dedicated text files in this `/proc` directory.`/proc/driver/nvidia/gpus/PCI-BUS-ID/information`
Provide information about each of the installed NVIDIA GPUs (model name, IRQ, BIOS version, etc.). Note that some of the information is only available when the GPUs have been initialized. See [“What is the format of a PCI Bus ID?”](faq.html#busid) for information on how to determine PCI-BUS-ID.

`/proc/driver/nvidia/gpus/PCI-BUS-ID/power`
Provide information about the runtime D3 (RTD3) Power Management status of each of the installed NVIDIA GPUs. Note that some of the information is only available when the GPUs have been initialized. Please see [Chapter 22, *PCI-Express Runtime D3 (RTD3) Power Management*](dynamicpowermanagement.html "Chapter 22. PCI-Express Runtime D3 (RTD3) Power Management") for the detailed description of this `/proc` interface. See [“What is the format of a PCI Bus ID?”](faq.html#busid) for information on how to determine the PCI-BUS-ID.`/proc/driver/nvidia/suspend`
Notify the NVIDIA kernel drivers of system power management events, such as suspend and hibernate. Please see [Chapter 21, *Configuring Power Management Support*](powermanagement.html "Chapter 21. Configuring Power Management Support") for a detailed description of this `/proc` interface.
