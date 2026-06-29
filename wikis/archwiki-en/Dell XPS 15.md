# Dell XPS 15

This page is a work in progress! More info coming soon.

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Bluetooth || ||
|-
| Touchpad || ||
|-
| GPU || ||
|-
| Webcam || ||
|}

## Differences between XPS 9550 & Precision 5510
The Precision 5510 is essentially identical to the XPS 9550 variant, with the exception of an Intel Wireless NIC & Quadro 1000M Graphics Chip. Compared to the 9550's Broadcom NIC & 960M graphics chip.

## XPS 15 9560 and "early 2017" revision
There is a dedicated page for version 9560 from 2016 and 2017 (especially troubleshouting video related problems).

## System Setup
## Power Management
For the Sandy Bridge model (L502X): Suspend works; hibernation does not (it gets hung on a flashing cursor in text mode and does not even switch video modes).

If hibernation/resume fails, or does not consistently work, try each of the following:

* Enable early KMS for  and .

* Create the following configuration file (Source):

## Sound
For the XPS 9550 variant, sound works out of the box with the linux kernel. If you try to plug in headphones, you will not hear any output from them. Upon restart, you will receive a Dummy Output as your sound card.

dmesg gives you this output:
 snd_hda_intel 0000:00:1f.3: CORB reset timeout#1, CORBRP = 0
 snd_hda_intel 0000:00:1f.3: no codecs found!

aplay -l should give you this output if Arch can detect your soundcard:
 **** List of PLAYBACK Hardware Devices ****
 card 0: PCH Intel PCH, device 0: ALC3266 Analog Analog
   Subdevices: 0/1
   Subdevice #0: subdevice #0
 card 0: PCH Intel PCH, device 3: HDMI 0 0
   Subdevices: 1/1
   Subdevice #0: subdevice #0
 card 0: PCH Intel PCH, device 7: HDMI 1 1
   Subdevices: 1/1
   Subdevice #0: subdevice #0
 card 0: PCH Intel PCH, device 8: HDMI 2 2
   Subdevices: 1/1
   Subdevice #0: subdevice #0
aplay -l will give you this output if Arch cannot detect your soundcard:
 aplay: device_list:268: no soundcards found...
You may or may not get sound back after a few restarts. This is a bug and has been documented here:

Workarounds:
* Install  and run hdajackretask just toggle the drop down.
* Suspend and resume your computer (thank you spheenik)
* Restart your computer
* Disable sound BIOS, powerboot into Arch, enable sound in BIOS, start Arch with sound back
* Connect external sound card via USB

Regardless, for now, it is recommended that you do not/reduce hot-plugging headphones as it makes ALSA/PulseAudio break/very unstable.

## Microphone
The XPS 15 provides a combo jack for audio input and output.

## No audio input through combo jack
Headsets might only be recognized as headphones. Passing  to the  kernel module solves this issue. This can be done by creating:

## Graphics
By default, both Intel and NVidia cards are active, which can consume a lot of power. Using the Intel-only setup below, you can reduce your battery usage by disabling the Nvidia card. The Intel and Nvidia setup describes how to utilize both cards and save power using Bumblebee. See also Hybrid graphics.

## Intel only
If your model comes with an nVidia card which you do not use then you can try to disable it with an ACPI command. Depending on the model, this can have a small to profound effect on the laptop's temperature and battery life (it can more than double battery life!)

* Install the Intel video driver using the  package.

* To make sure nVidia module will not load into your system:
** Remove nouveau and/or nvidia drivers
** Use acpi_call (compile acpi_call or use one of the AUR packages) to disable the nVidia card

## acpi_call usage
 modprobe acpi_call
 ./usr/share/acpi_call/examples/turn_off_gpu.sh
or:
 sudo /usr/share/linux610-acpi_call/examples/turn_off_gpu.sh

One of the many results will be "works!". Use the value that works in the following call:
 echo '\_SB...._OFF' > /proc/acpi/call

If none worked, you can try one of the other files in the  directory.

For example, the following works on the XPS 15 9550 and L502x model:
 echo '\_SB.PCI0.PEG0.PEGP._OFF' > /proc/acpi/call

You can use this command before and after to see how the battery consumption change (you need to disconnect sector first and the lower the better):

 cat /sys/class/power_supply/BAT0/current_now

To make this permanent, just create a systemd unit file with your working command.

## Intel with Nvidia
The Optimus setup consists of the integrated Intel chip connected to the laptop screen and the Nvidia card runs through this. As such, the Nvidia chip cannot be used without the Intel chip (some other laptops have the option in BIOS to turn Intel off and use just Nvidia, but not this laptop).

See the Bumblebee page set of instructions, particularly the Intel/Nvidia section which has been tested. The main thing to note is that installing both  the Intel and Nvidia packages at once tends to avoid dependency issues.

## Screen
9550 Flickering Screen:

To fix screen flickering issues add  to your boot parameters.

## External Display
Since the Display Port is controlled by the Intel driver, it tends to work quite well and will usually mirror the laptop display without configuration. Getting both the HDMI and DP adapters to display separate requires additional setup.

The Display Port can be accessed with a USB-C to Display Port adaptor, it should be a adaptor that works via "alternate mode" such as the plugable cable (known to work), there are other adaptors that did not work (KiWiBiRD USB 3.1 Type C THUNDERBOLT 3 to DisplayPort 4K Adapter), though why it did not is unknown.

## Multihead
The following instructions should help configure the laptop to display separate output on two external monitors. These instructions are similar in nature to the instructions on the Bumblebee page, though recent advancements in virtual displays on Intel reduce the number of steps and packages needed.

* First, follow the instructions in the previous section to install drivers for both Intel and Nvidia with Bumblebee.
* Run  to generate a  file. It may have a different filename, so watch the output and regardless of where it generates it, copy it to . This should generate something like the following (for two external monitors):

* Change the  file to the following settings (these are scattered throughout the conf file):

* Add the following to your  file.

* Run  and check that your displays are working.

The modifications to  automate the configuration of the displays. First,  is launched to run Bumblebee. Then, the  utility (included with  versions 2.99+) creates a few  displays;  was the display mapping to my HDMI port, run  to double check this for yourself. The remaining commands may vary for your configuration, note that  is the laptop screen and  is actually the Display Port.

## WLAN
Remember that  will be needed for using a network manager such as NetworkManager, see Wireless network configuration for more information.

## Bluetooth
Some users may need to run
 hciconfig hci0 reset
to get blueman working

Using power management with TLP might cause a problem. Excluding Bluetooth devices from USB autosuspend by setting:

can resolve the issue.

## BIOS
XPS 9550 with InfinityEdge 4K

The XPS 9550 4K, with its current state, is unstable due to its young age. A majority of the bugs stem from Dell's BIOS.

Listed below are you may encounter with the XPS 9550 4K:

;01.02.00:
* Brightness works with slow fade (XF86MonBrightnessUp / xbacklight -inc:-dec)
* Sleep resume working around 80% of the time
* Resume from sleep restarts the laptop
;01.02.10+:
* Increased speeds (faster boot, applications feel snappier when loading, especially in 01.02.13)
* Black screen upon resume (the computer will operate as if it's on, to get display to work, set brightness to max using keyboard shortcut)
* Brightness flickers/stutters when dimming or increasing the brightness (demonstrated in i3wm)
* Screen flickers on low brightness settings
* Possible poor fan behavior (not confirmed)
* Battery will not charge beyond 60%. The fix is to download and flash [https://downloads.dell.com/FOLDER03906323M/1/XPS_9550_1.2.14.exe 1.2.14 BIOS or later Flashing 01.02.00 will be pointless after, as the issue carries over to this version of BIOS.
;01.02.14:
* Download
* User report that the issue with the battery is fixed
* Still has black screen upon resume issue. To turn screen on, increase brightness to maximum using keyboard. It is not possible to decrease brightness after resume, either maximum or off.
* Increasing the brightness (eg, with xbacklight) by less than 9% does not have any effect. Decreasing by less than 9% always results in a decrease of 9%.
;1.02.16:
* Download
* "Black screen upon resume" issue appears to have been fixed!

Many users have recommend the 01.02.00 BIOS, as it proves to be the most balanced out of all of the updates.

## Webcam
If the camera does not seem to work (black image), try to enable/disable auto-exposure. In reality, the camera tries to record at 0.5 fps and this is why it seems not to work, even if everything seems normal.

## Special Touch Keys
The special touch keys are strangely mapped by default. One changes brightness, one does next track. They seem to be linked to the same key sequences as the Fn+F# keys that do the same job. To fix this, make this new file:

and add this to /etc/rc.local:

Source

## Alternative method
For L502x model the above method can be improved:
# No need to remap Play/Pause, Previous song, Next song keys as they are mapped correctly by default.
# For the first (leftmost) touch key: it's wired in a weird way on the hardware level.  It seems to be wired to both Super_L and x.  Your best bet would be to remap this using your DE or something like xbindkeys.  You may want to double-check with  or  to see exactly what keys it is producing.
Thus the keymap file should be (I prefer standard location):

and add this to /etc/rc.local:

OR make a udev rule (the former remaps keys on boot, this lets udev take care of the remapping):

## Hidden Keyboard Keys
For L502X model: there are additional Fn+ (sequences) that are not marked at all on the keyboard but underlying hardware generates them anyway. Here they are (if you find more add them to the table below):
{| class="wikitable"
|+ Hidden Fn Keys
! Fn+ !! Resulting key (sequence)
|-
| Fn+Esc || Sleep
|-
| Fn+Super_L || Super_R
|-
| Fn+Ins || Pause/Break
|-
| Fn+Del || Ctrl + Pause/Break
|-
| Fn+PrntScr || Alt + PrtSc/SysRq
|}

## Touchpad Gestures
The 1.2.21 BIOS update has caused many users to lose mouse scrolling in Chromium. A bug report has been opened about the issue. A workaround would be to disable Smooth Scrolling in chrome://flags

## libinput
## XPS 9550
Working, using libinput and libinput-gestures.

## Synaptics
If using Synaptics, read Synaptics.

## Notes
* Remember to turn on Wi-Fi and Bluetooth by pressing the F2 button.
* Card reader is finnicky.  Try booting with a card inserted or inserting a card after it is booted and running   Otherwise, card reader will not be detected.  It seems that a certain kernel update results in the workaround not working as well.  More info needed.
