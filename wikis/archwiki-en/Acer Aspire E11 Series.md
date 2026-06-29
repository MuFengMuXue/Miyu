# Acer Aspire E11 Series

{| class="wikitable archwiki-table-laptop"
| Device || Working
|-
| Intel graphics ||
|-
| Network ||
|-
| Broadcom wireless ||
|-
| Atheros Wireless ||
|-
| ALSA ||
|-
| Touchpad ||
|-
| Webcam ||
|-
| Card Reader ||
|-
| Power management ||
|}
Aspire E11 Series

## Installation
Prior to installation, download and install the latest firmware update from Acer under Windows. Older versions of the firmware can only boot from the (black) USB 2.0 port.

To recover the Windows key at a later stage, run:

 $ hexdump -C /sys/firmware/acpi/tables/MSDM

Note that this key is tied to the particular laptop model and unusable elsewhere. See also === Create a recovery drive ===

A recovery drive can made with the preinstalled Acer eRecovery Management application. This requires a USB-attached flash drive or hard disk with at least 16 GB free space available, and presence of the  directory. All present data on the target drive will be lost.

Choose the option Create Factory Default Backup, select the partition Windows is installed on, and click start. Remove the drive afterwards - booting from the device will now start the recovery software. See [https://web.archive.org/web/20141201061449/http://acer--uk.custhelp.com/app/answers/detail/a_id/14303/~/create-a-recovery-usb-flash-drive-with-acer-erecovery-management-5.x for more information.

## Booting
The Acer E3-111 does not have an optical drive.

Both UEFI and Legacy (BIOS) boot are supported. To switch modes, press  at the boot splash screen to enter the EFI setup, then select the Boot tab. Alternatively, access the EFI setup by rebooting in Windows.

Disable Secure Boot, then follow the installation guide. An Ethernet connection is recommended, as the needed wireless drivers are not included in the installation medium.

## Configuration
## Wireless
To use the Broadcom BCM43142 chipset is, install , and load the module:

 # modprobe wl

The system will now recognize the interface as . See Broadcom wireless and Wireless for details.

## Touchpad
The E11 series include a Precision Touchpad, which supports a variety of touch gestures. To enable the touchpad, append the  kernel parameter. See Touchpad Synaptics for configuration details.

## Power management
You may need to use the linux-lts kernel for full support.

## Suspend and hibernate
Suspend and hibernate should work after following Power management/Suspend and hibernate.

## Troubleshooting
## GPU
See Intel graphics#AccelMethod.

## Start up and shutdown freeze
If you have an issue where the computer freezes during start up and shutdown, requiring multiple reboots, try adding the following to

 blacklist dw_dmac
 blacklist dw_dmac_core

See also [https://bugzilla.redhat.com/show_bug.cgi?id=1213216
