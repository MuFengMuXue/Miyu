# Lenovo ThinkPad T14 (AMD) Gen 4

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU || ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|-
| TPM || ||
|-
| NFC || ||
|}

## Firmware
## S3 Sleep
Option to enable S3 sleep is not available in the BIOS. As a result, only  is available.

## Wireless
## Unreliable/High latency
There is an active thread in Lenovo forums regarding this issue. Possible workaround is to disable power saving mode by adding following lines and restarting  service.

There seems to be another issue where after some suspend/wakeup cycles the Wi-Fi card gets into a weird state where it drops almost all outgoing transmissions. This results in authentication timing out and network speeds being unusable. Removing the PCIe device using the sysfs interface and reading it seems to solve this issue:

 # lspci | grep Qualcomm
 02:00.0 Network controller: Qualcomm Technologies, Inc QCNFA765# echo 1 > /sys/bus/pci/devices/0000:02:00.0/remove
 # echo 1 > /sys/bus/pci/rescan

This workaround has been automated with a [https://github.com/Lawstorant/p14s-wifi-reset script that ships a systemd service. Install  and Enable  service. Wi-Fi adapter will be removed and re-added after wakeup from sleep.

## Failure to resume from hibernation
The  driver is experimental and it fails to recover the device after resuming from hibernation. There is an active bug report.
The patch to fix was pending public review but has been reported to be reverted.

See Lenovo ThinkPad T14s (AMD) Gen 3#Network / Wi-Fi for a fix that unloads the  module before sleep and loads it again after resume.

## WAN
You need to FCC Unlock the Fibocom L860R aka "Intel XMM7560 LTE Advanced Pro Modem" before it can be used. To do this, you need to install . However, this tool refuses to unlock Lenovo p14s gen4 because this model is not yet certified/has not yet passed RF testing.

As of 2023-11-24 it shows the following message when trying to FCC unlock the modem:

 DPR_Fcc_unlock_serviceWWAN is not supported in this machine

Fortunately, it is a very simple executable that only checks what is inside  before allowing an FCC unlock. If you want to use your Fibocom L860R you need to create:

Do not forget to make the file executable.

That way  will think that your laptop is a Thinkpad X1 Carbon Gen 10 and it will happily unlock the modem for you to use. Since the file is saved in  ModemManager will FCC unlock your modem automatically every time you initialize a connection to your provider.

## Fan
The fan is relatively loud and triggers from simple web browsing.

* A first solution is thinkfan from Fan speed control, but its not yet perfect as the lowest level maps to too high RPM.
* From the fan-controll page: see gentoo link for an example, and add the proposed experimental=1

## Fingerprint reader
Fingerprint reader works out of the box with fprint. Multiple fingers can be enrolled and any one of those fingers can be used to authorize.

## Infrared camera and emitter
On models with an infrared camera, howdy can be used to enable face unlock. On some models, the IR emitter is not enabled automatically, in that case, follow the workaround from Howdy#IR emitter does not work

## Speakers
Speakers work out of the box. How ever, they won't have the same sound quality as on Windows due to the missing Dolby Atmos Convolver.

To enable Dolby Atmos Convolver install EasyEffects, go to Effects > Add Convolver > Import Impulse

The quality difference is massive, converting the speakers from sounding tinny and cheap to something actually enjoyable.

You can download the "Movie", "Music", and "Dynamic" presets here:

https://stuff.kurz.pw/arch/P14s_G4/Speakers/

They were created on a P14s G4 AMD (identical to T14) with Windows 11.

## Thunderbolt 3 compatibility
Tested with a Lenovo Thunderbolt 3 Dock (40AC) it simply worked out-of-the box (using the USB-C connector right next to the RJ45 port), resulting in new pcie devices appearing on  etc. So yes, this laptop actually has Thunderbolt 3 compatibility. As with the speaker profiles this test was done on an (identically build) P14s.

Depending on BIOS configuration thunderbolt devices might need activation before being usable, e.g. using . For that run  first to retrieve the devices UUID. After that use  to enable the device.

## NFC
Install and start . Detected NFC tags should appear as D-Bus objects. Use the scripts from [https://github.com/linux-nfc/neard/tree/master/test the test directory for reading NFC tags.

## Other issues
## Hang on splash
Remove  from the kernel parameters.

## Mic LED always on
See Lenovo ThinkPad T14 (AMD) Gen 3#Mute Mic LED always on.

## OLED screen not allowing 90Hz
If only 60Hz is allowed in display settings, add  to the kernel parameters. This fixes a regression in Linux 6.13 that populates the screen's EDID info with a manufacturer's preferred settings.

## Display brightness resets
On models with 2.8K OLED pannel, display brightness resets if the screen is blanked and unblanked. This is fixed in  and above.

## Display stays off after lid close
If your display stays off after closing and then opening the lid, there are few things to note:

- the laptop is not crashed, it is just the display that does not turn itself on again

- you need to "re-initialize" the display in some way, e.g. connecting the laptop via the HDMI port to an external display and then disconnecting

- or switching resolution or (even better) just the refresh rate. This is how this solution works.

Install acpid and then edit the following file and add the lines starting with XDG_Session:

/etc/acpi/handler.sh
    button/lid)
        case "$3" in
            close)
                logger 'LID closed'
                ;;
            open)
                logger 'LID opened'
                XDG_SESSION_TYPE=wayland XDG_RUNTIME_DIR=/run/user/1000 kscreen-doctor output.eDP-1.mode.1 output.eDP-1.enable
                XDG_SESSION_TYPE=wayland XDG_RUNTIME_DIR=/run/user/1000 kscreen-doctor output.eDP-1.mode.0 output.eDP-1.enable
                ;;
            *)
                logger "ACPI action undefined: $3"
                ;;
    esac
If you have the 2.8k OLED display this will switch the display to 2880x1800 @ 60Hz and then to 2880x1800 @ 90 Hz every time you open the lid. That way your display gets re-initialized. Note that this solution is only for Wayland. If you are still using X, you will need other environment variables.

## Smartcard reader hang
Sometimes the built in smartcard reader stops responding (). Fix is to power-cycle the card reader by suspend or by toggling power of the internal usb port using .
