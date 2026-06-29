# ASUS Vivobook X513EAN

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on the ASUS Vivobook X513EA laptop. This information may be more widely applicable to ASUS Vivobooks, or may be specific to EU or even UK models of this laptop.

## Installation
To install Arch Linux, you can follow the official Installation guide. Since the X513EA uses UEFI and GPT, make sure to also read the UEFI, GPT and Arch boot process#Boot loader pages.

## Boot from USB medium
Hold  while powering on to get into the boot menu.

## Screen backlight
To allow for  and  to lower and raise screen brightness respectively, set the kernel parameters  and  (the space is required).

You can also control the brightness of the screen backlight through the  file in  by writing a value to it.

This requires root, or using  to set the ownership of  to your user (which is subsequently reset to root on reboot).

You can retrieve the maximum from :

 # cat /sys/class/backlight/acpi_video0/max_brightness

To set it to a particular value:

 # echo X > /sys/class/backlight/acpi_video0/brightness

## Keyboard backlight
By writing a value to , it can similarly be changed.

This also requires root or changing ownership of the file, making the firmware level  shortcut far preferable.

## Solid state drive
This machine comes with one or more NVME SSD. Make sure to read Solid state drive.

## Graphics
Install the  package to fix screen tearing. See Intel graphics and Xorg

## Touchpad
See libinput

When using libinput, the touchpad can be configured in . Similar configurations can be defined for Xorg. For instance:

## Disabling the touchpad
The touchpad on this laptop is large and easily brushed while typing, so it is recommended to enable disable-while-typing, as described above.

This laptop also 'flexes' considerably when picked up by the side or corner, as well as when leaned on while typing. This can often activate a mouse button, so it is recommended to set an easily activated shortcut to disable the touchpad. Many window managers and desktop environments can achieve this

## Power management
It is possible to limit the battery maximum charge on this laptop. This is recommended because lithium-ion cells degrade faster when constantly fully charged, and will enjoy a longer life if maintained at a lower charge.

See Laptop/ASUS#Battery charge threshold.

To configure some other power saving options and tools, see Power saving.

 is NOT recommended on this laptop as most of its core features, such as fan curve speeds and setting the keyboard LEDs, are not enabled.

## Function keys
See Keyboard shortcuts or use a desktop shell with built-in shortcut support to enable the functionality of these keys, except for the screen backlight keys.

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Toggles Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  || Toggles up through four keyboard brightness settings
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Deactivated
|-
|  ||  ||  || Deactivated
|-
|  ||  ||  || Deactivated
|-
|  ||  ||  ||  (Pg Up)
|-
|  ||  ||  ||  (Pg Dn)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}
# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# Handled by firmware
