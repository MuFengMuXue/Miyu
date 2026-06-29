# Lenovo ThinkPad X201 Tablet

## Power management
## Fan control
There are some discussions concerning overheating-related shutdowns when running under full load (video encoding, etc) ([https://bugs.launchpad.net/ubuntu/+source/linux/+bug/751689).

ThinkPad Fan Control contains instructions to install tpfand as a custom replacement for hardware (bios-) fan control.

## Kernel parameters
Add these kernel parameters to make use of power saving mechanisms which are turned off by default because of reported instabilities.

 i915_enable_rc6=1 i915_enable_fbc=1

## Firmware
## Using non-Lenovo Network cards
If you get
  1802: Unauthorized network card is plugged in - Power off and remove the miniPCI network card.
on boot, that means your BIOS does not include that specific card in its whitelist. The only option is either coreboot or a custom BIOS with the whitelist "disabled".

Such a bios can be found at this forum post at mydigitallife.info.

You can either use Windows to flash, or a DOS boot disk with phlash16.exe and the 02C2100.ROM from the forum post's rar like I did. To do it this way, first upgrade the BIOS to the latest version from Lenovo. Then, rename "02C2100.ROM" to "BIOS.WPH", save it to your DOS boot disk and run phlash16.exe.
