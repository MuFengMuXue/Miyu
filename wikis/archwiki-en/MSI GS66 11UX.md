# MSI GS66 11UX

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| Display || ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Thunderbolt ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|}

MSI has released refreshed GS66 laptops with 11th Intel processors and NVIDIA Ampere graphics. Exact models are 11UH, 11UG and 11UE. Note that these models should not be confused with 10UX models as they are reported to work out of the box with Linux.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Installation
## UEFI configuration
* Pressing  during startup will open the UEFI.
* Pressing  during startup will open a boot menu.

This laptop also has advanced UEFI settings if desired.

Before installing Arch Linux, several steps need to be done in the UEFI:

* Secure Boot must be disabled in Security > Secure Boot.
* VMD controller must be enabled in Advanced > VMD controller.

## Audio
Arch Linux will not detect audio hardware unless you install Sound Open Firmware.

The audio device exhibits clipping issues under Linux, whereby audio may be lost at the start or end of playback. During continuous playback, the device behaves as expected.

This occurs using ALSA directly, meaning it is independent of software mixers like PulseAudio or PipeWire, and also occurs in legacy mode, using driver , and with power management disabled. It is unknown what is required to make the device operate optimally under Linux.

Alternatively, you can workaround this issue by constantly playing inaudible (25000hz) tone through your speakers in the background all the time:

 $ sox -n -r 96000 -c 2 -t wav - synth sine 25000 | pw-play -

## Graphics
When an external display is connected, especially high framerate (e.g. 240Hz) via HDMI or DisplayPort, it reports its true refresh rate, but only the cursor seems to use the reported refresh rate, while the rest stays at ~120Hz. Other issues include artifacts and glitches.

To fix this, switch to dedicated NVIDIA GPU (using Mux switch, via UEFI or via Windows) as a workaround. See also upstream issue.

## Tips and tricks
## Keyboard RGB control
Install  and see the project's README#usage. Using the  argument works fine with GS66 11UX models that have an US keyboard. This has not been tested with all other keyboards, but it does not work with Spanish keyboards.

## Disable fan when idle
Laptop fan never powers off, even when system is completely idle. This can be fixed by installing  package, configuring EC register to be available with write support and issuing this command on boot:

 # isw -s 0x72 0

## MSI Center replacement (MControlCenter)
This device has quite some features, controllable via software, such as fan speed control, fan turbo mode, battery charge thresholds as well as power modes. All of these can be controlled via MControlCenter () application. For more information, see Fan speed control.

## Mux switch
By default, this device operates in Hybrid graphics which works completely fine, but one of the key features of this device is mux switch. In short, it allows physically wiring NVIDIA GPU to the display, which eliminates the need for the integrated graphics processor and resulting in improved performance.

MSI only provides Windows application (UWP or ZIP) to switch between Hybrid graphics (Intel + NVIDIA) and discrete graphics (NVIDIA) mode. Basically it sets some sort of a flag (presumably in EC register) and reboots. During the reboot, it seem to temporarily boot into the UEFI, change the graphics mode and reboot back to Windows. Some reverse engineering to achieve the same functionality has been done on a similar model (see the GitHub issue and the GitHub project), but there was no success for this specific model.

While there is an option in the UEFI to change such graphics, it is greyed out. Fortunately, UEFI version E16V4IMS.107 (mirror) is the most up-to-date version that does not have such option greyed out and allows to change graphics. Note that you will need to activate advanced options, allow UEFI downgrading and flash this UEFI file as a regular UEFI update.

## CPU undervolting
CPU undervolting is done via  as described in Undervolting CPU. However, it will not work until overclocking support is enabled in the UEFI advanced settings. Once enabled, saved and rebooted, you can undervolt CPU within Linux. Note that re-connecting battery will reset overclocking support and it needs to be enabled within the UEFI again.
