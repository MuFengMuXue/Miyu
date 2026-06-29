\
This article describes the setup of an [ACPI](https://wiki.gentoo.org/wiki/ACPI "ACPI") based docking stations and media bays.

## [Installation]

Activate the following kernel options for dock support:

[KERNEL] **Enabling ACPI dock support**

    Power management and ACPI options  --->
        [*] ACPI (Advanced Configuration and Power Interface) Support  --->
            [*] ACPI Support
                [*]   Dock

** Note**\
Remember to recompile the kernel and to reboot the machine when enabling build-in kernel support. Without this step the new kernel will not be loaded into memory.

## [Usage]

After the driver is loaded, for each docking station or media bay a directory [/sys/devices/platform/dock.0], [/sys/devices/platform/dock.1], etc. will be created. The files and their information can be used in scripts to adjust power management, monitors (screens), or any dock related settings.