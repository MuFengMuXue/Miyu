# Lenovo ThinkPad Yoga 260

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Touchscreen ||  ||
|-
| Keyboard || ||
|-
| Video ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Accelerometer ||  ||
|-
| Fingerprint reader ||  ||
|-
| Smart card reader ||  ||
|}

## Installation
To access the boot menu and UEFI, use . Disable Secure Boot from the UEFI.

## Firmware
fwupd does not support this device yet, but it may still detect the laptop as a ThinkPad T460s and try to update its firmware if the installed firmware is very old.

To update the firmware on the device, get the latest bootable CD and follow the steps in Flashing BIOS from Linux#Bootable optical disk emulation.

## TrackPoint
Sometimes the TrackPoint stops working and dmesg reports a stream of garbage when it is touched. Removing and probing the kernel module solves the problem:

 # rmmod psmouse
 # modprobe psmouse

## Video
With default configuration, tearing is apparent when playing videos. See Intel graphics#Tearing.

## Fingerprint reader
Works using https://github.com/3v1n0/libfprint. Bug tracker for fingerprint sensor: https://gitlab.freedesktop.org/libfprint/libfprint/issues/54

## Power management
If the device has unusually high CPU usage in idle then it might be an acpi firmware issue. On Windows this behaviour stops after a regular update. On Linux you can workaround by disabling whatever device is interrupting excessively.

Find the interrupting source:

 $ grep . -r /sys/firmware/acpi/interrupts

This might output something like this:

 ...
 /sys/firmware/acpi/interrupts/gpe34:   30289   enabled   /sys/firmware/acpi/interrupts/gpe34

Now the CPU should idle at 0-2% usage.

Unfortunately you have to do that on every startup. A systemd service can do that automatically for you.

Create :

 Description=Disable acpi interrupts
 [Service
 ExecStart=/usr/bin/bash -c 'echo "disable" > /sys/firmware/acpi/interrupts/gpe34'
 Install
 WantedBy=multi-user.target

Then enable the  systemd unit.
