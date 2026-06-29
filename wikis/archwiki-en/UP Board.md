# UP Board

The UP Board is an Intel-based System on a chip (SOC) device by Aaeon.  There is a companion device, the UP Core, that uses the same chipset and devices.  Installation of Arch is no different, except that you do not have the GPIO bus to enable.

The UP Squared is a larger and more powerful version of the UP Board. It differs in chipset, CPU, memory type and size; however, it shares the same storage using Intel's eMMC 5.0 specification.

## Installation
The UP Board features a UEFI only setup (no BIOS emulation). The standard UEFI installation process may be followed. systemd-boot works well as a simple boot loader.

## GPIO
The GPIO pins on the UP board are routed through a CPLD that requires a custom driver. This driver has not yet been added to the mainline kernel, so it is required to build a custom kernel or patch it in order to add the functionality. See UP's official wiki page for more information.

## Troubleshooting
## Reboot causing kernel panic
Rebooting the board multiple times without disconnecting power, as what could happen if using as a server, could fail with a kernel panic. This is possibly due to a bug in the  kernel module, as discussed at "UPboard Ubilinux Freezing" forum topic and Bug 106721 in Freedesktop.org bug tracker.

To make rebooting the board more reliable, try adding the following to your kernel parameters:

 reboot=efi,cold

If you are using this board in a headless configuration, a possible workaround is to blacklist the  module, as reported on a message in the "UPboard Ubilinux Freezing" forum discussion.
