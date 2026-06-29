# ASUS Eee PC T101MT

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Keyboard || ||
|-
| Video || ||
|-
| Webcam || ||
|-
| Ethernet || ||
|-
| Card Reader || ||
|-
| Audio || ||
|-
| Wireless || ||
|}

## Function keys
Suspend-, Brightness- and Audiokeys work. Others may need special configuration.

Suspendkey was executing the suspend from KDE and from the acpi Interface. Disabling the KDE event made the Suspend work.

## Power management
## Suspend
Touchscreen is not working afterwards.

It will work after you reload hid_multitouch kernel module:

As a workaround, you can add the following line to the file '/etc/pm/config.d/modules':

This way the kernel module will be explicitly unloaded before suspend.

If you are using twofing you also need to restart it:

This instruction may be useful for solving this problem

## Hibernate
Not Working.

## Brightness
With some Eee PC's, the brightness setting are either too low, or are sometimes a little inconsistent or arbitrary (cycling high/low/completely off).
If you have issues with this, issue this command to fix it and optionally regenerate your boot loader configuration:

 # setpci -s 00:02.0 f4.b=80

The 80 represents the highest brightness level in hexadecimal, which can be replaced with up to FF if desired. 80 is about half, being approximately the same brightness range as Windows or GRUB.

This is not permanent, so it must be autostarted at boot.
