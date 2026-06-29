# Hybrid graphics

Hybrid-graphics is a concept involving two graphics cards on same computer. Laptop manufacturers have developed technologies involving two graphics cards with different abilities and power consumption on a single computer. Hybrid-graphics has been developed to support both high performance and power saving use cases by keeping the Dedicated/Discrete Graphics Processor inactive unless its 3D rendering performance is needed over the Integrated Graphics Processor.

There are a variety of technologies and each manufacturer developed its own solution to this problem. This technology is well supported on Windows but it is still rough around the edges with Linux distributions. This article will try to explain a little about each approach and describe some community solutions to the lack of GNU/Linux systems support by vendors.

## Dynamic switching
Most of the new Hybrid-graphics technologies involve two graphics cards: the dedicated and integrated cards are plugged to a framebuffer and there is no hardware multiplexer. The integrated card is always on and the dedicated card is switched on/off when there is a need in power-save or performance-rendering. In most cases there is no way to use only the dedicated card and all the switching and rendering is controlled by software.
At startup, the Linux kernel starts using a video mode and setting up low-level graphic drivers which will be used by the applications. Most of the Linux distributions then use X.org to create a graphical environment. Finally, a few other softwares are launched, first a login manager and then a window manager, and so on. This hierarchical system has been designed to be used in most of cases on a single graphics card.

## Fully power down discrete GPU
You may want to turn off the high-performance graphics processor to save battery power.

## Using BIOS/UEFI
Some laptop manufacturers provide a toggle in the BIOS or UEFI to fully deactivate the dedicated card.

## Using udev rules
Ensure any display manager config for NVIDIA is removed.

Blacklist the nouveau drivers by creating

Then create

{{hc|/etc/udev/rules.d/00-remove-nvidia.rules|2=
# Remove NVIDIA USB xHCI Host Controller devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c0330", ATTR{power/control}="auto", ATTR{remove}="1"

# Remove NVIDIA USB Type-C UCSI devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c8000", ATTR{power/control}="auto", ATTR{remove}="1"

# Remove NVIDIA Audio devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x040300", ATTR{power/control}="auto", ATTR{remove}="1"

# Remove NVIDIA VGA/3D controller devices
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x030-9*", ATTR{power/control}="auto", ATTR{remove}="1"
}}

Reboot and run  to see if your NVIDIA GPU is still listed.

Check power usage to ensure your GPU is not drawing power, if it does #Using acpi_call may be another option to fully power it down.

## Using bbswitch
With an NVIDIA GPU, this can be more safely done using bbswitch, which consists of a kernel package that automatically issues the correct ACPI calls to disable the discrete GPU when not needed, or automatically at boot.

## Using acpi_call
Otherwise, and for GPUs not supported by bbswitch, the same can be done manually installing the  package.

Once installed load the kernel module:

 # modprobe acpi_call

With the kernel module loaded, execute the script at

The script will go through all the known data buses and attempt to turn them off. You will get an output similar to the following:

See the "works"? This means the script found a bus which your GPU sits on and it has now turned off the chip. To confirm this, your battery time remaining should have increased.

## Turning off the GPU automatically
Currently, the chip will turn back on with the next reboot. To get around this, load the module at boot:

## At boot
To turn off the GPU at boot it is possible to use systemd-tmpfiles.

The configuration above will be loaded at boot by systemd. What it does is write the specific OFF signal to the  file. Obviously, replace the  with the one which works on your system (please note that you need to escape the backslash).

## After X server initialization
On some systems, turning off the discrete GPU before the X server is initialized may hang the system. In such cases, it may be better to disable the GPU after X server initialization, which is possible with some display managers. In LightDM, for instance, the display-setup-script seat configuration parameter could be used to execute a script as root that disables the GPU. If you use SDDM then you can add the line  to either  or  depending if you use Wayland or Xorg, replacing  with the one which works on your system.

## System76
Some System76 laptops (like the Oryx Pro) have their own unique hybrid graphics option.  To make use of it, install , enable , and run .

## Fully power down discrete GPU
First ensure you are using integrated graphics mode by running  and rebooting. Once in integrated mode, to power down the discrete graphics card run . This command is not persistent and will need to be run after each boot.

## Troubleshooting
## The startup time for certain applications is delayed by 30 seconds
When invoked, Vulkan attempts to initialize the Installable Client Driver (ICD) specified in . The package   configures this file to reference the  driver, providing Vulkan with information about the GPU driver's path. However, if the GPU is disabled, initialization of this driver will fail, causing certain applications (e.g., those based on Chromium/Electron) to undergo delayed startup until a 30-second timeout is reached. To prevent Vulkan from attempting to load the driver in the first place and thus mitigate this timeout, you can override the location of the ICD JSON file using the  environment variable. To unset it, use:

 $ export VK_DRIVER_FILES=

## High power draw even after disabling NVIDIA discrete GPU
If after disabling the dedicated GPU bus #Using acpi_call the power draw is still high, check if the nouveau kernel module is loaded with . If it is not then make sure it is installed, that any entries in .conf files that blacklist Nouveau in  are removed and that the Nouveau kernel module is automatically loaded at boot. After rebooting the power draw should be lower.
