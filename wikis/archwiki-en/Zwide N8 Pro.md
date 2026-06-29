# Zwide N8 Pro

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Track point ||  ||
|-
| Keyboard ||  ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|}

## Installation
The default BIOS options are correct. In order to bring the UEFI Boot screen selection, tap the  key for the boot menu, and choose your prepared installation media. After this steps you can install archlinux using installation guide.

## Firmware
No special firmware installation needed. Laptop works well after default installation.

## Screen rotation
By default screen rotated in -90 degrees (specific screen type).

Automatic screen rotation not tested.

You can rotate screen in boot process by add kernel boot params, like this (systemd-boot example):

 /boot/loader/entries/.conf
 ---
 title	Arch Linux (linux)
 linux	/vmlinuz-linux
 initrd	/initramfs-linux.img
 options ... fbcon=rotate:1 <--

and rotate screen in your DE/VM/Compositor, like this (swaywm example):

 ~/.config/sway/config
 ---
 # output * disable
 output DSI-1 enable
 output DSI-1 transform 90 <--

## Sleep
Laptop supported 2 options in UEFI settings. By default S3 sleep mode. Not tested.

## Battery
New laptop may be shipped without battery calibration and battery may be recalibrated manually by charging practices. Battery module shipped with primitive controller, which not support charging limit, cycles and etc.

## USB-C Charging
Charging available with 12v type-c power adapters. Other charging devices with voltage ranges also can charge this laptop.

## External Displays
Laptop supported external displays using mini hdmi port and usb type-c port

## Track point
Track point works well but scrolling supported only with input settings using libinput, like this (swaywm example):
 ~/.config/sway/config
 ---
 # [Inputs
 input "9610:306:SINO_WEALTH_USB_OFN_PADD" {
   dwt disabled
   tap enabled
   natural_scroll enabled
   middle_emulation disabled
   scroll_method on_button_down <--
   scroll_button BTN_RIGHT <--
 }
