# Lenovo IdeaPad U410

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Keyboard || PS/2 ||
|-
| TouchPad || PS/2 ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
| Audio ||  ||
|-
| Webcam ||  ||
|-
|}

A rather interesting ultrabook from the early 2010s, featuring an HDD + SSD RAID, and a dedicated NVIDIA GT 610M GPU that is better off not being used.

## Installation
You'll have to decide on whether to keep the preconfigured RAID configuration, which uses the main hard drive, or to ditch the RAID config and install on the SSD. The SSD is only 32GB, which can cause issues when installing large packages like desktop environments or games. It may be best to replace the 32GB mSATA drive with a higher-capacity one, replace the 500GB SATA HDD with an SSD, or install on an SD card.

The laptop can also boot from it's internal SD-card slot, so it can be used as another option to install the OS on, or from.

## Accessibility
This laptop features a primarily text-based UEFI-supported BIOS which is easy to OCR.

The easiest way of entering the boot menu is by pressing on the Novo button on the side, which allows you to bypass the trial and error button mashing. After pressing it you can either enter into the BIOS, boot menu, or One Key Recovery which looks for a recovery partition. Another way of getting into the boot menu is by pressing  during POST. Pressing  during POST will take you to the BIOS.

The BIOS is primarily keyboard navigateable and doesn't need a mouse or trackpad

## Graphics
Most units were shipped with an NVIDIA GT 610M dedicated graphics card (GF119M). It is no longer properly supported by the proprietary NVIDIA driver. You have four options:

* Use kernel mode setting (works out of the box)

* Install  (small improvement)

* Install  (does not support Wayland)

Performance will not be great. Expect frequent freezes under moderate loads.

The last option is to ditch the GPU entirely and use the integrated Intel HD 4000 graphics.

## Firmware
fwupd recognizes the device, but only lists the CPU, the drives, and miscellaneous items such as  and

## Function keys
{| class="wikitable"
! Key
! Visible?1
! Marked?2
! Effect
|-
| colspan="4" | Function keys
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Does nothing ( in xev)
|-
|  ||  ||  || Does nothing ( in xev)
|-
|  ||  ||  || Toggles touchpad on and off
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Change external display options ( in xev)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
| colspan="4" | Side keys
|-
|  ||  ||  || Pause
|-
|  ||  ||  || Break
|-
|  ||  ||  || Scroll Lock
|-
|  ||  ||  || Insert
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
