# Lenovo IdeaPad Gaming 3

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (AMD) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|}

## Installation
Before installing, disable Secure Boot in the UEFI Setup. You can access the UEFI Setup by pressing  at the Splash screen. The boot menu can also be accessed by pressing .

## Accessibility
The UEFI firmware settings can be entered by pressing  repeatedly during boot.

## Navigation
The interface can be fully navigated and controlled with a keyboard and mouse. Up and down arrow keys let the user choose categories, settings items within each category and values for settings. Left and right arrow keys let the user leave and enter a category, settings item or value picker. The enter key can also be used to enter a category or enter and leave an item's value picker. Settings can be saved and the system restarted by pressing .

## Secure Boot
In order to boot an Arch installation medium, Secure Boot must be disabled in the UEFI settings. Once disabled, press  on the next boot to enter the boot device menu and select your Arch installation medium.

## Firmware
This laptop is not supported by fwupd. You need a Windows installation in order to update UEFI.

## Power management
Install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

## System Performance Mode
There are 3 modes available: Intelligent Cooling, Extreme Performance and Battery Saving. To switch between them, press  on the IdeaPad's internal keyboard.

Using ACPI calls directly (tested on 15ACH6):

Set it to Intelligent Cooling mode:

 # echo '\_SB_.GZFD.WMAA 0 0x2C 2' > /proc/acpi/call

Set it to Extreme Performance mode:

 # echo '\_SB_.GZFD.WMAA 0 0x2C 3' > /proc/acpi/call

Set it to Battery Saving mode:

 # echo '\_SB_.GZFD.WMAA 0 0x2C 1' > /proc/acpi/call

To view the currently activated System Performance Mode in 15ARH05 or 15ACH6 and its family series:

 # echo '\_SB.PCI0.LPC0.EC0.SPMO' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

In some 15ACH6 and 15ARH7 and its family series :

 # echo '\_SB.PCI0.LPC0.EC0.GZ44' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

As a result you get the value for the bit SPMO / GZ44 (either ,  or ).
The value of the bit corresponds to the following System Performance Modes:

{| class="wikitable"
! SPMO / GZ44 !! Mode
|-
| 0x0 || Intelligent Cooling
|-
| 0x1 || Extreme Performance
|-
| 0x2 || Battery Saving
|}

A simple OSD for KDE is available via ; edit  for customization.
Enable/start the  user unit manually.

## Rapid Charge
Turn on Rapid Charge:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call

Turn off Rapid Charge:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call

Get the status of Rapid Charge:

 # echo '\_SB.PCI0.LPC0.EC0.QCHO' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

For some 15ACH6:

 # echo '\_SB.PCI0.LPC0.EC0.FCGM' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

## Battery Conservation
Similarly to the #Rapid Charge, make sure you have set up .

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x03' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x05' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.BTSM' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

There is also an alternative way to control the Conservation Mode of the battery:

First make sure the  kernel module is loaded with the  command.

If it is, run the following command as root to enable Battery Conservation Mode:

 # echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

A 0 will in turn disable the feature.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?
! Marked?
! Effect
|-
|  ||  ||  || Toggle Fn lock
|-
|  ||  ||  || Mute audio
|-
|  ||  ||  || Volume down
|-
|  ||  ||  || Volume up
|-
|  ||  ||  || Mute microphone
|-
|  ||  || 1 || Screen brightness down
|-
|  ||  || 1 || Screen brightness up
|-
|  ||  ||  || Show screen projecting menu (same as )
|-
|  ||  ||  || Turn on airplane mode
|-
|  ||  ||  || Turn touchpad on/off
|-
|  ||  ||  || LeftCtrl+LeftAlt+Tab
|-
|  ||  ||  || Calculator
|-
|  || 2 ||  || Toggle keyboard backlight (off/low/bright)
|-
|  ||  ||  || Switch between performance modes, see #System Performance Mode
|-
|  ||  ||  || (Media) Play/Pause
|-
|  ||  ||  || (Media) Stop
|-
|  ||  ||  || (Media) Previous
|-
|  ||  ||  || (Media) Next
|-
|}
# If the backlight controls does not work on the AMD/NVIDIA variant by default, add the following kernel parameter: .
# If the keyboard backlight appears but cannot be controlled (i.e. it is shown by mistake), mask  and the following udev rule disables it:

## Advanced UEFI/BIOS
To access the advanced UEFI/BIOS setup utility, do the following:
# Power off completely
# Press the power button
# Repeatedly press  to enter UEFI/BIOS
# Press the following key sequence 3 times, one key at a time:, ,
# Press  and  to save and exit
# Repeatedly press  to enter UEFI/BIOS, this should now have the advanced options visible
