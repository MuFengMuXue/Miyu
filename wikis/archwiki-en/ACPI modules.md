# ACPI modules

From uefi.org:

:The Advanced Configuration and Power Interface (ACPI) specification was developed to establish industry common interfaces enabling robust operating system (OS) directed motherboard device configuration and power management of both devices and entire systems. ACPI is the key element in OS-directed configuration and Power Management (OSPM).

ACPI modules are kernel modules for different ACPI parts. They enable special ACPI functions or add information to  or . These information can be parsed by acpid for events or other monitoring applications.

## Which modules are available?
This is a small list and summary of ACPI kernel modules:

* ac (power connector status)
* asus-laptop (useful on ASUS/medion laptops)
* battery (battery status)
* bay (bay status)
* button (catch button events, like LID or POWER BUTTON)
* container (container status)
* dock (docking station status)
* fan (fan status)
* i2c_ec (EC SMBus driver)
* thinkpad_acpi (useful on Lenovo ThinkPad laptops)
* processor (processor status)
* sbs (smart battery status)
* thermal (status of thermal sensors)
* toshiba_acpi (useful for Toshiba laptops)
* video (status of video devices)

A complete list for your running kernel can be obtained with the following command:

## How to select the correct ones
You have to try yourself which module works for your machine using , then check if the module is supported on your hardware by using dmesg. It may help to add a grep text search to narrow your results:

You can load the module at boot to make the change permanent for the working ones.

## Getting information
To read out battery information, you can simply install the package  and run .

Using  to store ACPI information has been discouraged and deprecated since Linux 2.6.24. The same data is available in  now, and interested parties can (should) subscribe to ACPI events from the kernel via netlink. For example, for battery:
 /sys/class/power_supply/BAT0/

## Troubleshooting
## DSDT fix
If problems with power management persist despite having loaded the proper modules, a Linux-unfriendly DSDT might be the cause.

## ACPI fix for notebooks
Sometimes you see "ACPI: EC: input buffer is not empty, aborting transaction". This is a problem with ACPI, more specifically an incompatibility of the BIOS. There may be four ways to solve this issue:

* If available, flash BIOS.
* Use  as kernel parameter, however this will kill all ACPI functionality like battery charging and power saving.
* In some cases disabling DPMS has been reported to solve the issue However, screen brightness may no longer be fully controllable:
* Build a custom kernel with patches of [https://bugs.launchpad.net/ubuntu/+source/linux/+bug/578506 bugs.launchpad.net.

## Boot-looping
Some notebooks or motherboard may have boot issues, such as powering off during the transition from boot loader to OS due to bad ACPI firmware implementation. The following steps provide several kernel parameters, to be tested in order:

# Set . If you are able to successfully boot:
## Dump the ACPI table and check for strings similar to "Windows XXXX". Find the most recent ones:
## Set .
# Boot looping issues may be due to unstable C-States:
## Disable ACPI C-State driver by using
## If you are using Intel processors, set  to limit C-State to C1E. Higher C-State may work, your mileage may vary.
## Disable MWAIT instruction and fallback to ACPI C-State driver with . Verify your changes by using cpupower:
