# ASUS Zenbook UM3402YA

## Audio
In the default kernel configuration, there is currently no sound output with the internal speakers, due to the Cirrus CS35L41 HD amplifier which cannot be set up properly on boot The ASUS Zenbook UM3402YA series seems to not be the only device where this problem occurs.
This was first caused by a firmware bug, but according to a Cirrus developer, the no-sound-issue seems to be fixed in a BIOS update due to the missing of certain ACPI entries [https://web.archive.org/web/20230122213950/https://github.com/CirrusLogic/linux-firmware/issues/8#issuecomment-1387128605.

There are some unofficial patches available, but these patches got rejected by a kernel developer due to the possibility of harming your device. An updated patches is available for the 6.2 kernel. Also this ssdt patch can be applied by grub (also needs at least 6.2 kernel) possibility of harming your device.

Some further, related threads: [https://github.com/thesofproject/linux/issues/3814, [https://www.linux.org/threads/solved-asus-zenbook-15-ux534f-realtek-hd-audio-problem.27384/, [https://www.linux.org/threads/solved-wifi-adaptator-not-found-mediatek-wi-fi-6-mt7921-wireless-lan-card.37699/page-2#post-143291

## Suspend/resume: one speaker silent
On kernels 6.8+ where audio works at boot, one speaker (typically the right channel) may go silent after suspend/resume. The CS35L41 amplifier firmware fails to reinitialize due to missing ACPI GPIO reset pin, leaving the amp bound but without firmware ( in kernel log).

Symptoms:

* One speaker goes silent after suspend, the other works fine
* ALSA mixer shows balanced levels (issue is at kernel driver level)
* Reboot temporarily fixes it
*  shows  on the affected amp

The workaround is to unload the CS35L41 modules before suspend (while the I2C bus is still clean) and reload them after resume. Create the following system-sleep hook:

Make it executable

No PipeWire restart is needed — the CS35L41 modules have zero direct users even while audio is playing.

## Bluetooth
If you have kept Windows in dual-boot and cannot get Bluetooth working: power-off your laptop, then hold power button for 60 seconds. That will reset UEFI settings, so disable Secure Boot again if needed. After that Bluetooth will be detected and work properly.

## Fingerprint
See fprint, in particular fprint#Enrolling works but verifying does not for tips on how to use the sensor.

## Fan control
See ASUS Zenbook UM3402YAR#Fan control.
