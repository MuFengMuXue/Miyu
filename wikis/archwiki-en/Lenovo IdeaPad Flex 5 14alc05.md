# Lenovo IdeaPad Flex 5 14alc05

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Webcam ||  ||
|-
| Fingerprint sensor
|

|
|-
| Pen input || ||
|-
| Accelerometer ||  ||
|-
| SD-card reader ||  ||
|}

The IdeaPad Flex 5 14alc05 is a 14-inch AMD Lucienne (Ryzen 5000)-based convertible from Lenovo.

## Firmware
fwupd does not officially support this device but it can still be used to apply UEFI firmware updates.=== Updating bios ===

## Pre update
* Install the ,  and  packages.
* Download bios update exe file.[https://pcsupport.lenovo.com/in/en/products/laptops-and-netbooks/flex-series/flex-5-15alc05/downloads/driver-list/component?name=BIOS%2FUEFI

## Procedure
Run the following commands:
* Extract the bios  file:
 $ innoextract file.exe
* Get the GUID number of your system firmware for the next step. You should get something that looks like example below:

{{hc|# fwupdate -l|
system-firmware type, {e20bafd3-9914-4f4f-9537-3129e090eb3c} version 22315982 can be updated to any version above 22315981
device-firmware type, {e3be8073-66a6-4bf6-966a-c0d58b486c40} version 1 can be updated to any version above 0
device-firmware type, {c85ba1bc-54a7-4aab-9337-eed4746bf09f} version 0 can be updated to any version above 4294967295
}}
* Schedule the update for the next system reboot, using extracted  file:
 # fwupdate -a e20bafd3-9914-4f4f-9537-3129e090eb3c /path/to/file.cap

*Verify that the update is pending:
 # fwupdate -i

* Reboot if there are no errors and if update is pending.

* When the update completes it will boot into the boot menu. At this point it is safe to interact with the device again.

## Manually with EDK2 CapsuleApp
* Install
* Build MdeModulePkg

* Copy the extracted  file, the UEFI Shell at  and the built  to your efi root. (probably )
* Reboot into the UEFI Shell.

* Go into the efi root.

* Check for the files with ls.
* Run

* When the update completes it will boot into the boot menu. At this point it is safe to interact with the device again.

## Post update
* Disable secure boot in the settings to be able to boot into Linux.
* If your boot loader is not detected, boot into a usb with Arch and use  to reinstall your boot loader or use  to create a boot entry.

## Secure Boot
The BIOS accepts custom Secure Boot keys. To enroll them, you have to use  from .
Follow the guide under Secure Boot#Using KeyTool.

## Wireless
The Ideapad Flex 5 14alc05 may come with either Wi-Fi 5 (802.11ac 2x2) or Wi-Fi 6 (802.11ax 2x2), both equipped with Bluetooth 5.0 and connected via M.2 slot (see the PSREF for device specifications). However, Lenovo sources these cards from multiple companies. Depending on the hardware layout, this device may have either an Intel or a Realtek Wi-Fi card. Intel Wi-Fi cards should work out of the box, reliably and with full performance. Realtek on the other hand does not support Linux, and so Wi-Fi will not work out of the box.

If the card is a Realtek 8852AE or similar, a driver is available as .

## Touchpad/Touchscreen
Sometimes the touchpad and touchscreen will not work after booting due to missing module dependencies,  is unavailable when the modules for the touchpad/touchscreen get loaded.

To use the touchpad/touchscreen reliably after booting, create the following file:

## Fingerprint sensor
Depending on your specific model, you may have a  (Goodix) or a  (Synaptics). The process will differ depending on your reader, so first use lsusb to determine which one you have.

## Goodix
Follow this guide.

## Synaptics
For installation, the Windows driver will be downloaded and extracted. To do so, you need to install the  package beforehand. You also need  and .

In your chosen directory, run

 $ git clone https://github.com/Popax21/synaTudor/
 $ cd synaTudor
 $ arch-meson build
 $ cd build
 $ ninja
 # ninja install

For the module to work, you need to have the  fork installed instead of libfprint. You can now follow the steps in fprint or use your DE to configure your sensor!

## Accelerometer
While there used to be problems (See https://bbs.archlinux.org/viewtopic.php?pid=1933133#p1933133 and https://bugzilla.kernel.org/show_bug.cgi?id=212615), installing  seems to enable rotation support in compatible desktop environments.

## Power management
(see Lenovo IdeaPad 5 14are05#Power management, similar methods)

## System Performance Mode
There are 3 performance modes available: Intelligent Cooling, Extreme Performance and Battery Saving. To set them, you need to call the corresponding ACPI methods.

First install  ( for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

Set it to Battery Saving mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0013B001' > /proc/acpi/call

Set it to Extreme Performance mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0012B001' > /proc/acpi/call

Set it to Intelligent Cooling mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x000FB001' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.PFMM' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for Battery Saving,  for Extreme Performance and  for Intelligent Cooling.

## Battery Conservation
Similarly to #System Performance Mode, make sure you have set up .

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x03' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x05' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.SMBM' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

There is also an alternative way to control the conservation mode of the battery.

## Rapid Charge
Make sure you have set up .

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call

To verify your setting:
 # echo '\_SB.PCI0.LPC0.EC0.QKCM' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

Note however, that this is untested!

## Hidden BIOS menu
See https://forums.lenovo.com/topic/findpost/1092/5018261/5262868. You can turn on S3 sleep support.

## Suspend
See Power management/Suspend and hibernate#Changing suspend method for the general context in which this workaround applies.

* Get acpidump and iasl, provided by the  package.
* Dump all your ACPI files into a directory:

 $ mkdir ~/acpi/
 $ cd ~/acpi/
 # acpidump -b

* Decompile the DSDT table

 $ iasl -e *.dat -d dsdt.dat

* Patch the decompiled DSDT table (dsdt.dsl), using this patch:

 $ patch -p1  acpi_override

* Copy created cpio file to boot:

 # cp acpi_override /boot

* Reboot

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || Toggles Fn lock3
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || +
|-
|  ||  ||  ||
|-
|  ||  ||  || +
|-
|  ||  ||  || +
|-
|  ||  ||  || ++
|-
|  ||  ||  ||
|-
|  ||  ||  || Lenovo Vantage4
|-
|  ||  ||  || Screenshot4
|-
|  ||  ||  || Keyboard Backlight Brightness
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# The key has a status indicator LED in it similar to
# The Lenovo function keys driver provides special functionality for this key on Windows (See https://pcsupport.lenovo.com/de/en/products/laptops-and-netbooks/flex-series/flex-5-14alc05/82hu/82hu002yus/r9137p7f/downloads/driver-list/component?name=Mouse,%20Pen%20and%20Keyboard, under "Lenovo Fn and Function Keys for Windows 10 (64-bit)")
