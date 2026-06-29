# Lenovo ThinkPad Edge E455

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Ethernet || ||
|-
| Wi-Fi || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Card reader || ||
|-
| Backlit keyboard || ||
|-
| Fingerprint scanner || ||
|-
| Bluetooth || ||
|-
| Webcam || ||
|}

## Wi-Fi
The current driver for RTL8723BE PCIe Wireless Network Adapter can drop signals due to a power saving bug. See Network configuration/Wireless#rtl8723ae/rtl8723be.

Also wireless n is unstable so it is recommended to set your router for wireless g modulation.

## Hybrid graphics
Out of the box, the integrated card is used while the radeon driver dynamically powers off the discrete card. For use of discrete card, see PRIME.

## Backlight
Due to this system having a muxless hybrid configuration, the backlight controller cannot be detected by the system but its brightness can be changed by using the  subsystem. See Acpid, to configure brightness functionality.

## ClickPad
The clickpad that is used is from Alps. Specifically, it uses Alps protocol 8 which has initial support in kernel 4.1. While basic functionality works with kernels less than 4.1, there may be issues that occur with use in kernel less than 4.1.

There are two input drivers you can use for touchpad support: synaptics or libinput

Using the synaptics driver,for more advance features such as Vertical Edge Scrolling, see Touchpad Synaptics. An interesting quirk that occurs is that in order to be able to use Vertical, or Horizontal, Edge Scrolling you have to enable Two Finger
Scrolling. Setting only the Edge Scrolling option in xorg does not enable it.

For the libinput driver please see libinput.

Issue (using the Synaptics Driver):

After a certain amount of time used, the clickpad interrupts cease to be processed.

Work-Around (Non-Permanent):

Reload the "psmouse" kernel module when functionality ceases. Eventually it will cease up again requiring another reload.

 # modprobe -r psmouse
 # modprobe psmouse

Fix

In order to fix these problems, use the libinput driver instead of synaptics.

## Function keys
 and  keys can be swapped in BIOS.

The  key lock can be switched with .

The function keys that map into the  buttons, are partially working. The Wi-Fi key works out of the box but the sound keys and brightness keys need to be mapped in order to be functional. See Acpid, to configure hotkey functionality.
