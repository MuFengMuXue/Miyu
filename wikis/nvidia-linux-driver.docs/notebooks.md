## Chapter 16. Configuring a Notebook

### Installation and configuration

Installation and configuration of the NVIDIA Linux Driver Set on a notebook is the same as for any desktop environment, with a few additions, as described below.

### Power Management

All notebook NVIDIA GPUs support power management, both S3 (also known as "Standby" or "Suspend to RAM") and S4 (also known as "Hibernate", "Suspend to Disk" or "SWSUSP"). Power management is system-specific and is dependent upon all the components in the system; some systems may be more problematic than other systems.

Most recent notebook NVIDIA GPUs also support PowerMizer, which monitors application work load to adjust system parameters to deliver the optimal balance of performance and battery life. However, PowerMizer is only enabled by default on some notebooks. Please see the known issues below for more details.

### Hotkey Switching of Display Devices

Most laptops generate keyboard events when the display change hotkey is pressed. On some laptops, these are simply normal keyboard keys. On others, they generate ACPI events that may be translated into keyboard events by other system components.

The NVIDIA driver does not handle ACPI display change hotkeys itself. Instead, it is expected for desktop environments to listen for these key-press events and respond by reconfiguring the display devices as necessary.

### Docking Events

All notebook NVIDIA GPUs support docking, however support may be limited by the OS or system. There are three types of notebook docking (hot, warm, and cold), which refer to the state of the system when the docking event occurs. hot refers to a powered on system with a live desktop, warm refers to a system that has entered a suspended power management state, and cold refers to a system that has been powered off. Only warm and cold docking are supported by the NVIDIA driver.

### Known Notebook Issues

There are a few known issues associated with notebooks:

- In many cases, suspending and/or resuming will fail. As mentioned above, this functionality is very system-specific. There are still many cases that are problematic. Here are some tips that may help:

  - In some cases, hibernation can have bad interactions with the PCI Express bus clocks, which can lead to system hangs when entering hibernation. This issue is still being investigated, but a known workaround is to leave an OpenGL application running when hibernating.

  - On notebooks with relatively little system memory, repetitive hibernation attempts may fail due to insufficient free memory. This problem can be avoided by running \`echo 0 \> /sys/power/image_size\`, which reduces the image size to be stored during hibernation.

  - Some distributions use a tool called vbetool to save and restore VGA adapter state. This tool is incompatible with NVIDIA GPUs' Video BIOSes and is likely to lead to problems restoring the GPU and its state. Disabling calls to this tool in your distribution's init scripts may improve power management reliability.

- On some notebooks, PowerMizer is not enabled by default. This issue is being investigated, and there is no known workaround.

- When available, the NVIDIA driver installs a backlight handler that allows access to the driver's backlight controller through /sys/class/backlight/nvidia_0. This option can be disabled by passing the

``` screen
  NVreg_EnableBacklightHandler=0

```

  parameter to the nvidia kernel module.
