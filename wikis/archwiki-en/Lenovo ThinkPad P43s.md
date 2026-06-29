# Lenovo ThinkPad P43s

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Webcam || ||
|-
| Bluetooth || ||
|-
| Mobile broadband || ||
|-
| Fingerprint sensor || ||
|-
| MicroSD reader || ||
|}

## Graphics
This laptop has its external display ports directly wired to the NVIDIA chip. In loose terms this means that the dedicated GPU must be enabled in order for external displays to be used. Luckily, it is possible to do dynamic switching between the integrated and dedicated graphics, but this is only possible by using the Intel DDX driver  as opposed to modesetting.

The laptop can be used in one of two modes: Hybrid Graphics, or Dedicated Graphics only.

In order to use the integrated Intel UHD 630 GPU (as part of Hybrid Graphics) you need to add the  module to your  by adding it as a module in your mkinitcpio. This is done by setting the following on :

Failure to add the above will leave you stuck when trying to load the  and your system will not be able to boot.

It might be possible to make do without the module above by using the  only (this can be done by changing the setting in UEFI).

## Proprietary driver with bumblebee
With this setup the integrated GPU is used by default but some applications can be rendered on the discrete GPU with the  or  launchers. See Bumblebee for detailed instructions. The lack of proper v-sync support means that with this method applications rendered on the discrete GPU exhibit tearing. There is also some overhead introduced as a result of moving data inefficiently between the discrete and integrated GPUs, but the Nvidia GPU performs much better than it does with Nouveau.

To get this working you will need , ,  and .

Then set the following configuration files.

You probably already have one of these so adjust/add as needed - the dummy device at the end is essential:

At this stage, restart your machine. Then you should be able to run applications on the GPU as you normally would with , e.g., . If you want to use the external displays you need to keep your GPU on by running a task on  and then running  (this will stay running and binds the external display ports to virtual outputs that you can use). At this stage you should be able to see and use the external ports.

## Function keys
Most FN keys should work out of the box, but if it does not, bind mentioned keys to below commands:

* F1 button: .
* F2 button: .
* F3 button: .
* F4 button: .

## Touchpad
Touchpad is problematic. By default, if you hold the thumb over the button area, the pointer will not move. Once the system is installed, the problem disappears when using KDE, while GNOME still exhibits the issue. In GNOME, use the following to fix the problem:

 $ xinput set-prop 'SynPS/2 Synaptics TouchPad' 'libinput Click Method Enabled' 1 0

Even after doing this, the mouse pointer still jumps around when clicking the button sometimes.

## Fingerprint sensor
The fingerprint sensor works with some recent firmware and software updates (2019-12-15). Driver development info: Use fwupd to install the latest firmware for "Synaptics Prometheus Fingerprint Reader". The update might have to be done manually as the released firmware is in testing; or you could [https://github.com/fwupd/fwupd/wiki/LVFS-Testing-remote enable the testing remote in fwupd to allow automated upgrade. The relevant firmwares are Prometheus Fingerprint Reader and Prometheus Fingerprint Reader Configuration.

fprint has more details on how to setup the fingerprint for PAM authentication for example.

## Known issues
## CPU throttling issue
With the BIOS Version 1.52 (this problem is known to occur on 1.52, it might still happen on other versions too), the CPU tends to throttle down to 400 MHz earlier than it should. In particular, this can be seen when using Bumblebee.

After installing BIOS Version 1.54, this problem is fixed.

## Speaker noise issue
The speaker on the Lenovo Thinkpad T490 may have a high static hissing noise, which does not change if you lower the volume, but stops if you mute the speaker or use the headphone jack.
This problem cannot be fixed completely as of now. Updating to the most current BIOS version will make the speaker silent while it is not playing anything without you having to mute it all the time. But as soon as the user is playing sound, the noise will be back, clearly audible in the background.

Check the Lenovo Support Website for the newest BIOS Version.

## MicroSD card reader issue
The MicroSD card reader works with the arch kernel 5.3.11-arch1-1. There have been issues with previous kernel versions.

## Bluetooth
Works well with wireless headphones: no issues pairing or connecting with Blueman and PulseAudio.

## Slow wakeup after suspend
After suspend the laptop takes a few second until it becomes responsive. Disallowing the access to the WWAN device in the BIOS solves this issue.

## ACPI
The default  script has a check for the device that looks like this:

This will not work, since the T490 device is called  which is not matched by the above check. The instructions in Acpid does mention a pattern that does work and it is recommended to use this instead.
