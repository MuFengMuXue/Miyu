# ASUS Zenbook UX303

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (NVIDIA) ||  ||
|-
| GPU (Intel) ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|}

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on the ASUS Zenbook UX303 Ultrabook.

There is a lot a models but 2 main models, UX303LN with 2 graphics cards (Intel & NVIDIA) and UX303LA with only an Intel graphics card. The previous models UX32LN and UX32LA share a lot hardware with minor differences, e.g. the touchpad (Elantech).

## Touchpad
The touchpad is a FocalTech model exposed through PS/2 at , supported by Touchpad Synaptics and libinput. Check which one by running with

The sensitivity settings may need to be adjusted, because of the large touchpad area. If the touchpad is not responsive, try changing these settings:

If you use Touchpad Synaptics,

If you use libinput,

## Graphics
See Intel and NVIDIA for details. The secondary card is combined with the main graphics in a hybrid NVIDIA Optimus configuration. Bumblebee can be used to take advantage of the NVIDIA card.

## QHD+ PenTile display
Some models include a 3200x1800 (faux-3200x1800 RG/BW PenTile) screen, which displays very tiny characters, and can make them difficult to read due to its incomplete subpixel matrix.

Some environments and GUI toolkits may need adjustment: see HiDPI for possible fixes. Using 192 DPI or 2x scaling works well in most cases.

## Power management
## Suspend/resume
Suspend () works out of the box with expected behavior.

If suspend fails sometimes (kernel crashes when trying to suspend), it might be due to a bios/kernel bug. Try blacklisting the kernel modules  and  meanwhile.

## Battery
Battery has a design capacity of 4429mAh, and is able to provide just over 3 hours of autonomy under normal circumstances (average load of around 0.3 and Wi-Fi enabled, brightness lowered to mid-range) without serious power saving tweaks. Battery stops charging when it reaches near-full capacity on AC and acpi tool will show "discharging at zero rate" message. This behavior can be observed on a brand new battery. ACPI tools are able to correctly detect the battery state:

* On AC power with the battery near full capacity:

* On AC power while the battery is charging:

* On battery power (while the battery is discharging):

Battery life may depend on the type of LCD panel. The above values are shown for the model with QHD display.

There have been suggestions that "discharging at zero rate" while on AC is a battery calibration issue solvable by allowing the battery to fully discharge and then charging it back to full capacity.

It is also recommended to install . On a UX303LB laptop (Broadwell) this increases battery life significantly. See Laptop Mode Tools for more details.

## Audio
If the sound card power-saving capabilities are enabled, you can experiment some annoying click sound right before a sound is played. See Power management#Audio.

## Function keys
All function keys except the backlight and "plane" mode seem to work out of the box. To fix, add  as a kernel parameter and see Backlight.

## USB 3.0
If the USB ports are only working with USB 2.0 devices, disable XHCI Pre-Boot Mode in the UEFI configuration, under Advanced > USB Configuration.
