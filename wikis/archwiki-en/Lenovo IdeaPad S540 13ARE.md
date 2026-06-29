# Lenovo IdeaPad S540 13ARE

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Touchpad || ||
|-
| Audio ||  ||
|-
|}

The Lenovo Ideapad S540-13ARE is a laptop introduced in Mid-2020. It features a 13" QHD screen, AMD Ryzen 4000 processors (Renoir), and integrated AMD Vega graphics. It uses the name Xiaoxin Pro 13 2020 in some markets.

## CPU
It is strongly recommended to enable proprietary microcode updates, see Ryzen and Microcode for details.

## GPU related freezes
Some Vega-graphics powered devices, including this one, are suffering from a series of critical random crashes of the AMDGPU kernel driver, which may lead to a sudden freeze of the whole system.

You can refer to  from Arch bug tracker,  this bug report on the freedesktop gitlab and this bug report for the kernel side for further information.

It works *almost* fine for kernel 5.7.12 and newer, expect some infrequent regression though.

## System Performance Mode
There are 3 modes available: Intelligent Cooling, Extreme Performance and Battery Saving. To toggle it, you need to call some ACPI methods.

Install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

Set it to Intelligent Cooling mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x000FB001' > /proc/acpi/call

Set it to Extreme Performance mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0012B001' > /proc/acpi/call

Set it to Battery Saving mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0013B001' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.FCMO' > /proc/acpi/call
 # cat /proc/acpi/call | cut -d '' -f1

where  stands for Intelligent Cooling,  stands for Extreme Performance and  stands for Battery Saving.

## Rapid Charge
Make sure you have set up .

Turn on:

 #echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.QCHO' > /proc/acpi/call
 # cat /proc/acpi/call | cut -d '' -f1

where  stands for off and  stands for on.

## USB-C port failure
Sometimes after hibernate or reboot, you might find that the USB-C port cannot function normally. Charging, video output, data transmission all failed.

This is a common issue for Lenovo Xiaoxin laptop, see https://club.lenovo.com.cn/thread-5850476-1-1.html (written in Chinese).

To fix this problem:

# remove all the devices plugged to a USB ports or the 3.5mm headphone jack.
# Then power off your laptop, make sure that the machine is not being charged .
# Press , hold it for a while to enable battery shipping mode.
# Now the computer should not be able to boot without AC power.
# Finally, connect the laptop to AC power and start it.

The USB-C port should now function normally, or you should ask for technical support from Lenovo.
