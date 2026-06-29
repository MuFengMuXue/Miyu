# Lenovo IdeaPad 5 15are05

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Video ||  ||
|-
| Webcam (Acer) ||  ||
|-
| Webcam (Chicony) ||  ||
|-
| Bluetooth (Intel) ||  ||
|-
| Bluetooth (Realtek) ||  ||
|-
| SD card reader ||  ||
|-
| Audio ||  ||
|-
| Wireless (Intel) ||  ||
|-
| Wireless (Realtek) ||  ||
|-
| Fingerprint reader ||  ||
|}

## Installation
Before installing, disable Secure Boot in the BIOS. You can access the BIOS by pressing  at the Splash screen. The boot menu can also be accessed by pressing .

## Wireless
This laptop is available with either Intel AX200 or Realtek RTL8822CE, both work well on modern kernel. Realtek has pretty bad performance when using Bluetooth A2DP together with 2.4 GHz Wi-Fi network. Use either 5 GHz wireless network or external Bluetooth adapter for better speed when using Bluetooth audio devices.

## Microphone
See Laptop/Lenovo#IdeaPad "Pink Sardine" internal microphone not working.

## Power management
Battery Conservation Mode is a feature that limits battery charging to 55-60% of its capacity to improve battery life, being most useful when the laptop tends to run on external power much of the time. It can be controlled with . With   it is possible to control both Battery Conservation and System performance modes.

## Kernel method
Set the  kernel parameter.

To use without reboot:

 # rmmod ideapad_laptop
 # modprobe ideapad_laptop allow_v4_dytc=1

Restart . Now power-profiles-daemon can do everything below.

Apply this across reboots by setting it permanently.

## System Performance Mode
There are 3 modes available: Intelligent Cooling, Extreme Performance and Battery Saving. To toggle it, you need to call some ACPI methods.

First install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

Set it to Intelligent Cooling mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x000FB001' > /proc/acpi/call

Set it to Extreme Performance mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0012B001' > /proc/acpi/call

Set it to Battery Saving mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0013B001' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.SPMO' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

As a result you get the value for the bit SPMO (either ,  or ).

 # echo '\_SB.PCI0.LPC0.EC0.FCMO' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

As a result you get the value for the bit FCMO (either ,  or ). To interpret the results the following table can be used:

{| class="wikitable"
! SPMO !! FCMO !! Mode
|-
| 0x0 || 0x0 || Intelligent Cooling
|-
| 0x1 || 0x1 || Extreme Performance
|-
| 0x2 || 0x2 || Battery Saving
|}

## Rapid Charge
Make sure you have set up .

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.QCHO' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

Also see the note

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

There is also an alternative way to control the conservation mode of the battery.

## Note
It is worth noting that the Lenovo Vantage software for Windows when turning on Battery Conservation mode also turns off #Rapid Charge (if it was on). The same is also valid for the #Rapid Charge: turning it on will bring the battery conservation mode down. The aforementioned acpi call #Battery Conservation will not do this for you, but #Rapid Charge will. So it is possible to get the state where both battery conservation and rapid charge modes are active if you activate #Battery Conservation after #Rapid Charge. You generally do not want this, as Rapid Charging puts more strain on the battery than regular charging, defeating the purpose of Battery Conservation Mode.

## Function Keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Toggles Fn lock
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
|  ||  ||  || Inputs 3
|-
|  ||  ||  ||
|-
|  ||  ||  || Inputs 4
|-
|  ||  ||  || Inputs 5
|-
|  ||  ||  || Inputs 6
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
|  ||  ||  || Inputs
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function
# Default shortcut for opening "project" (as in projector) menu on Windows
# Default shortcut for opening "Windows Settings" on Windows
# Default shortcut for "Lock Screen" on Windows
# Default shortcut for "Task View" on Windows
# Default shortcut for capturing screenshots on Windows
