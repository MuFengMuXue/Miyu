# MSI GE63VR

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU (Intel) || ||
|-
| GPU (nvidia) || ||
|-
| Webcam || ||
|-
| Bluetooth || ||
|-
| SD-Card slot || ||
|-
| Audio || ||
|-
| Wireless || ||
|}
Not to be confused with MSI GS63VR

## Installation
You have to disable Fast Boot in the BIOS to install Arch. If you run into CPU lockup errors, also disable C-States.

## Audio
By default, ALSA reports Headphone and Speaker channels separately. However, on this laptop, the Speaker channel actually controls both the speakers and the plugged-in headphones, while the Headphone channel does not control anything. This is a problem because PulseAudio automatically sets the Speaker channel to zero when headphones are plugged in, which causes all outputs to be muted in this case.

The proposed fix is to disable the auto-mute feature (https://bbs.archlinux.org/viewtopic.php?id=237456). Edit the file  and replace the section

 Speaker
 switch = off
 volume = off

with

 Speaker
 switch = off
 volume = merge

Note : This change may get overwritten when PulseAudio is updated.

## Video
The system will hang if you try to start the X server while the NVidia GPU is turned off via bbswitch. To fix it, add  to your kernel parameters. Beware of the quotes  : for instance, if you use rEFInd as your boot loader, you will have to escape the quotes as  since rEFInd already uses quotes in its configuration file.

After applying this fix, power switching in optimus-manager should work with the following minimal config (as of version 1.3.1):

 switching=bbswitch
 pci_power_control=no

To use the HDMI or DisplayPort port the Nvidia GPU must be powered on. You need to either run your whole X session on the Nvidia GPU, or run it on the Intel GPU and have the Nvidia card act as a display sink

## RGB keyboard backlighting
On Windows, RGB keyboard backlighting can be configured with the SteelSeries Engine software, which is not available on Linux. As an alternative, the tool  provides partial control, specifically for MSI laptops with per-key RGB.
Tools designed for models with region-based RGB, such as [https://github.com/Gibtnix/MSIKLM MSIKLM, will not work.

Since the RGB settings are stored into the keyboard itself, another option for dual-boot owners is to configure the keyboard once in Windows, and then reboot into Linux.

## ACPI
A continuous stream of errors similar to the following will appear in kernel messages :

  AER: PCIe Bus Error: severity=Corrected, type=Data Link Layer, (Receiver ID)
  AER:   device error status/mask=00000040/00002000
  AER:    [ 6 BadTLP

You can fix them with the kernel parameter .

When the  workaround mentioned above is enabled, the following errors will occasionally appear as well. They seem harmless though.

 ACPI Error: No handler for Region (00000000e51c2f4b) [SystemCMOS (20180313/evregion-132)
 ACPI Error: Region SystemCMOS (ID=5) has no handler (20180313/exfldio-265)
 ACPI Error: Method parse/execution failed \_SB.PCI0.LPCB.EC._Q9A, AE_NOT_EXIST (20180313/psparse-516)

## Thermals
This laptop is compatible with the tool . You can use it to read sensor information in real-time :

## Suspend/Hibernate
Resuming from sleep can cause graphical glitches if the desktop session was running off the Nvidia GPU. On the other hand, if the Nvidia GPU was turned off via bbswitch, resuming wakes it up and causes it to start consuming power again.
