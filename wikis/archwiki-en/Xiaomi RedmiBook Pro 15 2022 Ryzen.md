# Xiaomi RedmiBook Pro 15 2022 Ryzen

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard || ||
|-
| GPU (AMD) ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Audio ||  ||
|-
| SD-card reader ||  ||
|-
| Fingerprint reader ||  ||
|}

This laptop has two variants, one with dedicated NVIDIA graphics and one without.

## Installation
See #Firmware.

## Accessibility
The appearance of the UEFI is pretty simple and not very colorful, so it might work well with OCR software.

## Firmware
This UEFI setup interface has very limited options available. You can disable/enable Secure Boot, set/unset password, change the size of shared VRAM, change boot order, or change the date/time. But that is about what all you can do in it. Pressing  during booting to select the boot device.

fwupd does not support this device yet.

## Secure Boot
Enter the UEFI menu by pressing  during booting and disable the password and Secure Boot.

* Security > Set password
* Security > Disable Secure Boot
* Reset the password by setting the password again but letting the New Password fields blank.

## Microphone detection problem
This laptop has a SenaryTech SN6140 Audio chip. When  an external microphone is plugged in the 3.5mm port, it may not be detected.

This only happens when the resistance of the microphone of the headset (with a 4-segment TRRS plug) is lower than usual. For example, the microphone of my Anker Soundcore Q35 headset has a resistance of about 1000Ω, while the microphone my other two headsets have a resistance of about 2000Ω.
This is probably a bug in detecting whether an OMTP/CTIA headset is plugged in or just an headphone with no microphone is plugged in. Because the resistance of the speaker in the earcup is usually much lower than that of the microphone, the audio chip might be measuring the resistance to tell them apart, and mistakes a microphone with lower resistance as a speaker.

With that in mind, you may pick one from the following ways to solve or to workaround the problem. (Or just use another microphone)

## Change the resistance
You can increase the resistance of the microphone to get it detected easily. You can add a resistor of a suitable value in series to the microphone, which requires some electronics work.

## Reconfigure the audio chip with   command
With this method, you can plug in your headset in a normal way and no electronics work is required.
However, I do not know what those commands actually do to the audio chip. Please only use them if you feel confident and adventurous.

Install the  package.

First, check and save the original value of the (potential) micbias output current comparator threshold. Here  is my device path.  is the get-verb corresponding to the  set-verb.  is an unused parameter.

 # hda-verb /dev/snd/hwC1D0 0x1c 0xb20 0
 nid = 0x1c, verb = 0xb20, param = 0x0
 value = 0x10

Here  is the unmodified value of the threshold register. Now, let's change it to some other value:

 # hda-verb /dev/snd/hwC1D0 0x1c 0x320 0x08

This sets the threshold register to . This should lower the threshold by about 500Ω on my system. Your result may differ. Other useful values include , ,  and . You may try different values. They seem to set different thresholds but I absolutely don't know why and how it works.

Your microphone should work with one of those values. This value seems to be persistent across reboots, and even useful when rebooting to a dual-boot Windows. After using the microphone, if you feel uncomfortable leaving that modified value, you can write back the original value:

 # hda-verb /dev/snd/hwC1D0 0x1c 0x320 0x10

Substitute  to your save value if differ.

## Plug in a two-step way
When you insert the plug of the headset, you can do it slowly and watch the audio input device list (for example in the KDE audio settings dialog). If you stop at a certain point, you may see a microphone appears in the list. Then you can resume the inserting and the microphone will keep working. This  method has no potential harm of unknown commands, but requires unusual usage every time you plug in a microphone.

## Fingerprint reader
The fingerprint reader requires a proprietary driver from an unknown third-party. The author explains that "The driver is developed with an internal async framework, which is not well-prepared to be open-sourced. So only the binary is released for the time being."
