# ASUS Zenbook UM425

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Bluetooth || ||
|}

## Configuration
## Secure Boot (option)
In order to boot any Linux operating system, navigate to BIOS (hold F2 during power-on), then hit  or click on Advanced Menu, then the Security tab and set Secure Boot to .

If the aforementioned Secure Boot option is a menu rather than an on-or-off option, click on Secure Boot, Key Management, then Reset to Setup Mode and confirm in the dialog.

## Video
See AMD and Hardware video acceleration.

## Audio
See PulseAudio.

## Touchpad
See Libinput.

The NumPad is working with asus-touchpad-numpad-driver implementation from GitHub. Be sure to install  and  before starting systemd's service, otherwise this script will not work.

## Keyboard
Some people encounter issues on cold boot where the keyboard is unresponsive.

Adding  to the kernel parameters seems to resolve the problem, this can be done by either rebooting, using a USB keyboard, or using chroot.

See https://lore.kernel.org/lkml/20211112180022.10850-1-tiwai@suse.de/T/ (this commit only seems to mention the UA version but this was tested on UX425QA).

## Battery charge threshold
Battery charge threshold is working. Laptop's battery stops charging at certain percentage when value in  is set to either , , or . But  may report the wrong charging status and percentage when the battery threshold is set below ; You may see the status listed as  even when the battery is fully charged to the limit, and the percentage may be one point short of the limit. For example when charging to , the battery's charge may say . See https://gitlab.freedesktop.org/upower/upower/-/issues/142

In order to automatically change the value at boot, user can create the systemd service: refer to Laptop/ASUS#Battery charge threshold

## Tips and tricks
See ASUS Zenbook UX430/UX530#Tips and tricks (with the exception of battery life, which is 20 hours for this model).
