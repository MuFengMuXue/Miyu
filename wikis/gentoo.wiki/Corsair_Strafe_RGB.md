**Resources**

[[]][Home](http://www.corsair.com/en-us/landing/strafergb)

[[]][GitHub](https://github.com/ccMSC/ckb)

The Corsair Strafe RGB is a mechanical gaming keyboard that is possible of operating cross platforms as a simple USB device. There is ongoing, open source development effort on GitHub (see the link the infobox to the right) to support the advanced features of the keyboard with a system daemon.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Services]](#Services)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [systemd]](#systemd)
-   [[4] [Usage]](#Usage)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [System boots slowly, hangs on USB device]](#System_boots_slowly.2C_hangs_on_USB_device)
    -   [[5.2] [Keyboard stops working after a key press]](#Keyboard_stops_working_after_a_key_press)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Hardware]

The device shows up in [lsusb] with an ID of `1b1c:1b20 Corsair`.

## [Installation]

### [Kernel]

The [ckb] daemon (installed in the step below) requires user level driver support in order to operate properly. Enable this option in the kernel:

[KERNEL] **Enabling `CONFIG_INPUT_UINPUT` support**

    Device Drivers -->
       Input Device Support -->
          Miscellaneous devices -->
             <*> User level driver support

### [Emerge]

A daemon is required in order to send configuration instructions and firmware updates to the keyboard.

`root `[`#`]`emerge --ask app-misc/ckb`

## [Configuration]

### [Services]

In order to configure the keyboard, and display the beautiful color effects, a daemon must be running.

#### [OpenRC]

Set the ckb-daemon to start on system boot:

`root `[`#`]`rc-update add ckb-daemon default`

To start the service now:

`root `[`#`]`service ckb-daemon start`

#### [systemd]

For systemd, ensure the ckb.service file will be loaded on system boot:

`root `[`#`]`systemctl enable ckb.service`

Start the service now via:

`root `[`#`]`systemctl start ckb.service`

## [Usage]

One the daemon is running and the kernel has been configured, start the ckb client program. The icon should now show up in most GUI toolbars. It is also possible to start program from the command-line with:

`user `[`$`]`ckb`

Once the client has been started it will live in the system tray. Be sure to check the \"Start ckb at login\" checkbox which can be found in the [Settings] tab. This will start the client with each system boot.

## [Troubleshooting]

### [][System boots slowly, hangs on USB device]

It is a known issue that the Strafe can cause the system to boot slowly. Generally this is the kernel hanging during USB initialization. Passing `usbhid.quirks=0x1B1C:0x1B20:0x20000408` to the kernel command line is work around for this issue.

For GRUB2, simply:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX="usbhid.quirks=0x1B1C:0x1B20:0x20000408"

Then be sure to regenerate GRUB2\'s configuration file:

`root `[`#`]`grub2-mkconfig -o /boot/grub/grub.cfg`

Other bootloaders can be handled accordingly.

### [Keyboard stops working after a key press]

dmesg output looks like the following:

[CODE]

    [ 2830.878653] usb 2-1.8.5: USB disconnect, device number 14
    [ 2831.175138] usb 2-1.8.5: new full-speed USB device number 15 using ehci-pci
    [ 2831.288348] usb 2-1.8.5: New USB device found, idVendor=1b1c, idProduct=1b20
    [ 2831.288355] usb 2-1.8.5: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [ 2831.288359] usb 2-1.8.5: Product: Corsair STRAFE RGB Gaming Keyboard
    [ 2831.288361] usb 2-1.8.5: Manufacturer: Corsair
    [ 2831.288363] usb 2-1.8.5: SerialNumber: 0C042029AEAA1002550AC6EEF5001945
    [ 2831.289824] input: Corsair Corsair STRAFE RGB Gaming Keyboard as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.8/2-1.8.5/2-1.8.5:1.0/0003:1B1C:1B20.002D/input/input63
    [ 2831.375353] hid-generic 0003:1B1C:1B20.002D: input,hidraw3: USB HID v1.11 Keyboard [Corsair Corsair STRAFE RGB Gaming Keyboard] on usb-0000:00:1d.0-1.8.5/input0
    [ 2841.375974] hid-generic 0003:1B1C:1B20.002E: usb_submit_urb(ctrl) failed: -1
    [ 2841.376004] hid-generic 0003:1B1C:1B20.002E: timeout initializing reports
    [ 2841.376317] input: Corsair Corsair STRAFE RGB Gaming Keyboard as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.8/2-1.8.5/2-1.8.5:1.1/0003:1B1C:1B20.002E/input/input64
    [ 2841.435986] hid-generic 0003:1B1C:1B20.002E: input,hidraw4: USB HID v1.11 Keyboard [Corsair Corsair STRAFE RGB Gaming Keyboard] on usb-0000:00:1d.0-1.8.5/input1
    [ 2851.436532] hid-generic 0003:1B1C:1B20.002F: timeout initializing reports
    [ 2851.436817] hid-generic 0003:1B1C:1B20.002F: hiddev0,hidraw5: USB HID v1.11 Device [Corsair Corsair STRAFE RGB Gaming Keyboard] on usb-0000:00:1d.0-1.8.5/input2
    [ 2861.437042] hid-generic 0003:1B1C:1B20.0030: usb_submit_urb(ctrl) failed: -1
    [ 2861.437058] hid-generic 0003:1B1C:1B20.0030: timeout initializing reports
    [ 2861.437341] hid-generic 0003:1B1C:1B20.0030: hiddev0,hidraw6: USB HID v1.11 Device [Corsair Corsair STRAFE RGB Gaming Keyboard] on usb-0000:00:1d.0-1.8.5/input3
    [ 2861.728138] input: ckb1: Corsair STRAFE RGB Gaming Keyboard as /devices/virtual/input/input65
    [ 2861.728455] input: ckb1: Corsair STRAFE RGB Gaming Keyboard as /devices/virtual/input/input66
    [ 2861.730481] usb 2-1.8.5: usbfs: usb_submit_urb returned -28
    [ 2867.187424] usb 2-1.8.5: usbfs: USBDEVFS_CONTROL failed cmd ckb-daemon rqt 161 rq 1 len 64 ret -110
    [ 2897.348579] usb 2-1.8.5: reset full-speed USB device number 15 using ehci-pci
    [ 2897.674981] usb 2-1.8.5: usbfs: process 16656 (ckb-daemon) did not claim interface 0 before use
    [ 2897.768692] usb 2-1.8.5: reset full-speed USB device number 15 using ehci-pci
    [ 2897.958701] input: Corsair Corsair STRAFE RGB Gaming Keyboard as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.8/2-1.8.5/2-1.8.5:1.0/0003:1B1C:1B20.0031/input/input67
    [ 2898.018915] hid-generic 0003:1B1C:1B20.0031: input,hidraw3: USB HID v1.11 Keyboard [Corsair Corsair STRAFE RGB Gaming Keyboard] on usb-0000:00:1d.0-1.8.5/input0
    [ 2898.158956] usb 2-1.8.5: usbfs: process 16656 (ckb-daemon) did not claim interface 1 before use

The solution is not known yet\...

## [See also]

-   [Razer BlackWidow Chroma](https://wiki.gentoo.org/index.php?title=Razer_BlackWidow_Chroma&action=edit&redlink=1 "Razer BlackWidow Chroma (page does not exist)") - Installation and configuration instructions on Gentoo.

## [External resources]

-   [Corsair\'s official Strafe release video (YouTube)](https://www.youtube.com/watch?v=JYQ2LJzU6GI)