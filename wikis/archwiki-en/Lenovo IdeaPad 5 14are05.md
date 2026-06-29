# Lenovo IdeaPad 5 14are05

The IdeaPad 5 14are05 is a 14-inch Lenovo AMD Renoir (Ryzen 4000)-based laptop.

## Hardware Support
## BIOS
BIOS can be accessed by pressing  at the Splash screen. The 15-inch model has BIOS updates that are compatible with DOS, so its BIOS can be flashed without Windows (see Flashing BIOS from Linux#FreeDOS). Unfortunately, the update files for this model require Windows. In theory, Windows can be installed on a USB drive through .

## Microphone
The internal microphone is properly recognized and working for  >=5.8rc3 as long as the  kernel module is loaded.

If the internal microphone is no longer recognized on  >=5.10, you may need to add the following to the kernel parameters:

 snd_rn_pci_acp3x.dmic_acpi_check=1

## Touchpad
The touchpad works almost as expected starting from  5.9-rc1. It is still random whether it will work or not after going out of suspend mode, but in that case it is an easy fix: just add a keyboard shortcut for the touchpad toggle and you should be able to make it work again.

While there is no explicit option to disable the touchpad in the BIOS, some option combinations in the BIOS can make the touchpad inaccessible. Thus, if you are running on  5.9 or newer and you still have issues with this module, try checking your BIOS settings first.

## Display
The brightness works for  >=5.7.6.1, since the patch to fix brightness has been merged. The xbacklight utility provided with  only works with Intel drivers, but you can use its replacement from  to increase and decrease brightness levels. Since the latter requires different permissions for the files in  to control the backlight brightness levels, you should set up a file in  containing:

 SUBSYSTEM=="backlight", ACTION=="add", \
   RUN+="/usr/bin/chgrp video /sys/class/backlight/amdgpu_bl0/brightness", \
   RUN+="/usr/bin/chmod g+w /sys/class/backlight/amdgpu_bl0/brightness"

You would also need to add your users to the  group.

Since backlight improvements in  6.1, you no longer have to add any kernel parameters such as  to the boot loader—in fact, according to Hans de Goede, the former "never was the right thing to do, it just happened to work" and the correct kernel parameter should have been  anyway.

## Suspend
See Power management/Suspend and hibernate#Changing suspend method for the general context in which this workaround applies.

## Enabling S3 sleep
* Turn off OneKeyBattery mode in BIOS setup, if it is enabled, and save the BIOS settings.
* Power down the laptop.
* Type, with the laptop powered off:                              .
If you notice the pattern, it is just going down the column from  to the letter in the last keyboard row, from  to . (You may need to replace some keys accordingly if you got a QWERTZ layout or similar alternative layouts).
* Boot the laptop with  pressed to get into BIOS as usual, you will get into the BIOS but with a few options more unlocked.

You will be able to then find a "S3/Modern Standby Support" setting in one of the newer menus that appear and toggle it to S3 instead of Modern Standby. Do not touch any other setting here unless you know what you are doing.

## ACPI patching
* Get acpidump and iasl, provided by the  package.
* Dump all your ACPI files into a directory:

 $ mkdir ~/acpi/
 $ cd ~/acpi/
 # acpidump -b

* Decompile the DSDT table

 $ iasl -e *.dat -d dsdt.dat

* Patch the decompiled DSDT table (dsdt.dsl). Use this patch for Linux  acpi_override

* Copy created cpio file to boot:

 # cp acpi_override /boot

* Reboot

## Power management
To toggle the System Performance or the Battery Conservation/Rapid Charge mode, you would need to call some ACPI methods.

First install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

You can also use ideapad-perf to control both the System Performance and the Battery Conservation mode through the CLI or with the provided tray applet.

## System Performance Mode
There are 3 modes available: Intelligent Cooling, Extreme Performance and Battery Saving.

Set it to Intelligent Cooling mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x000FB001' > /proc/acpi/call

Set it to Extreme Performance mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0012B001' > /proc/acpi/call

Set it to Battery Saving mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0013B001' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.STMD' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

As a result you get the value for the bit STMD (either  or ).

 # echo '\_SB.PCI0.LPC0.EC0.QTMD' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

As a result you get the value for the bit QTMD (either  or ).
To interpret the results the following table can be used:

{| class="wikitable"
! STMD !! QTMD !! Mode
|-
| 0x0 || 0x0 || Extreme Performance
|-
| 0x0 || 0x1 || Battery Saving
|-
| 0x1 || 0x0 || Intelligent Cooling
|}

## Rapid Charge
The Rapid Charge technology allows you to charge 80% of the battery capacity in around 30 minutes (depending on laptop model and battery). According to Lenovo, their batteries are charged at a higher rate with high current rather than high voltage, which they claim increases battery life.

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.FCGM' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

Also see the note

## Battery Conservation
Battery Conservation Mode is a feature that limits battery charging to 55-60% of its capacity to improve battery life, being most useful when the laptop tends to run on external power much of the time.

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x03' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x05' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.BTSG' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

There is also an alternative way to control the conservation mode of the battery.

## Note
It is worth noting that the Lenovo Vantage software for Windows when turning on Battery Conservation mode also turns off #Rapid Charge (if it was on). The same is also valid for the #Rapid Charge: turning it on will bring the battery conservation mode down. The aforementioned acpi calls (#Rapid Charge and #Battery Conservation) will not do this for you. So it is possible to get the state where both battery conservation and rapid charge modes are active. You generally do not want this, as Rapid Charging puts more strain on the battery than regular charging, defeating the purpose of Battery Conservation Mode. The ideapad-perf script will prevent you from doing this.
