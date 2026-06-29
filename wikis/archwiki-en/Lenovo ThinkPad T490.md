# Lenovo ThinkPad T490

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Webcam ||  ||
|-
| Bluetooth || ||
|-
| Mobile broadband || ||
|-
| Fingerprint reader ||  ||
|-
| MicroSD reader || ||
|}

## Function keys
Most Function keys should work out of the box, but if it does not, bind mentioned keys to below commands:

*  button: .
*  button: .
*  button: .
*  button: .

## Touchpad
Touchpad is problematic. By default, if you hold the thumb over the button area, the pointer will not move. Once the system is installed, the problem disappears when using KDE, while GNOME still exhibits the issue. In GNOME, use the following to fix the problem:

 $ xinput set-prop 'SynPS/2 Synaptics TouchPad' 'libinput Click Method Enabled' 1 0

Even after doing this, the mouse pointer still jumps around when clicking the button sometimes.

 v245 contains broken hwdb entry that sets invalid aspect ratio for the touchpad making it behave strangely.

## Fingerprint Sensor
The fingerprint sensor works with some recent firmware and software updates (2019-12-15). Driver development info: Use fwupd to install the latest firmware for "Synaptics Prometheus Fingerprint Reader". The update might have to be done manually as the released firmware is in testing; or you could [https://github.com/fwupd/fwupd/wiki/LVFS-Testing-remote enable the testing remote in fwupd to allow automated upgrade. The relevant firmwares are Prometheus Fingerprint Reader and Prometheus Fingerprint Reader Configuration.

fprint has more details on how to setup the fingerprint for PAM authentication for example.

## Known Issues
## Extremely high battery usage because of dedicated GPU
In short, because of a device-specific quirk in how Lenovo handles ACPI calls, you need the following kernel command line parameter to successfully power off your dedicated GPU: .

If your laptop is equipped with a NVIDIA dedicated GPU (such as the GeForce MX250), you will likely encounter very high battery usage because the GPU will not turn off.

You can check the "power state" of the dedicated GPU with the following, where you need to change  with the PCI Bus ID of your GPU you get from .

 $ cat /sys/bus/pci/devices/0000:3c:00.0/power_state

or

 $ cat /sys/bus/pci/devices/0000:3c:00.0/firmware_node/power_state

Power state 'D0' means your GPU is consuming a lot of power right now. Power states 'D3hot' and 'D3cold' are the low-power modes where the GPU is basically turned off, but still recognized by the kernel.

Use  to disable the GPU altogether:

* Install NVIDIA,  and  (optionally, install  or  to enable the card on-demand).
* Make sure to have the following inside file , where the ID after "PCI:" (60 in the example above) will be the output you get from , converted from hex to decimal (e.g., from  to ):
* Load the bbswitch module at boot by running
* Important: Add  to the kernel command line parameters. This article has a short explaination why, and reboot. This step is required because of a Lenovo bug in how they handle ACPI calls, which bbswitch relies on to power on/off your GPU.
* You can now turn on/off the dedicated GPU by running the following

Check the power status of the GPU by running

If you want to boot with your GPU disabled, run:

 # echo options bbswitch load_state=0 unload_state=1 > /etc/modprobe.d/bbswitch.conf

And blacklist any nvidia/nouveau driver that tries to load at boot, by editing :

 blacklist nouveau
 blacklist nvidia-drm
 blacklist nvidia-modeset
 blacklist nvidia-uvm
 blacklist nvidia

If you did everything correctly, you should experience a significant drop in battery usage on idle (e.g., from 7W to 3.5W on idle), almost doubling your battery life.

## CPU throttling issue
With the BIOS Version 1.52 (this problem is known to occur on 1.52, it might still happen on other versions too), the CPU tends to throttle down to 400 MHz earlier than it should. In particular, this can be seen when using Bumblebee.

After installing BIOS Version 1.54, this problem is fixed.

## Speaker noise issue
The speaker on the Lenovo Thinkpad T490 may have a high static hissing noise, which does not change if you lower the volume, but stops if you mute the speaker or use the headphone jack.
This problem cannot be fixed completely as of now. Updating to the most current BIOS version will make the speaker silent while it is not playing anything without you having to mute it all the time. But as soon as the user is playing sound, the noise will be back, clearly audible in the background.

Check the Lenovo Support Website for the newest BIOS Version.

## Slow wakeup after suspend
After suspend the laptop takes a few second until it becomes responsive. Disallowing the access to the WWAN device in the BIOS solves this issue.

## 2101: Detection error on HDD0 (Main HDD)
If you get this error after a reboot using "LENSE30256GMSP34MEAT3TA" NVMe SSD, try adding  to your kernel parameters.

You can see some exceptions for some SSDs but not for this model since kernel v5.16 core.c?h=v5.16#n2474

## ACPI
The default  script has a check for the device that looks like this:

 ac_adapter)
         case "$2" in
             AC|ACAD|ADP0)

This will not work, since the T490 device is called  which is not matched by the above check. The instructions in acpid does mention a pattern that does work and it is recommended to use this instead.

## Also See
* Lenovo Forums: A throttling fix is being investigated by Lenovo.
* Unix & Linux Stack Exchange: kernel - clarifying nvme apst problems for linux
