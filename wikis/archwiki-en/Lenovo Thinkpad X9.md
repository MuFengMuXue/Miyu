# Lenovo Thinkpad X9

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| ForcePad ||  ||
|-
| TouchScreen || ||
|-
| Stylus || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| IR camera ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| NPU ||  ||
|-
| Bluetooth ||  ||
|-
| Fingerprint reader ||  ||
|-
| Ambient light sensor ||  ||
|-
| Thunderbolt 4 ||  ||
|-
| TPM || ||
|}

## ForcePad
For 14" Sensel touchpad, you can adjust haptic feedback using :

 # hid-feature set /dev/hidraw1 -f b0000

and click force with:

 # hid-feature set /dev/hidraw1 -f d0000

The device reverts to default settings after reboot. We can make it permanent through udev rules:

{{hc|etc/udev/rules.d/99-sensel.rules|2=
SUBSYSTEM=="hidraw", ACTION=="add", ENV{ID_VENDOR_FROM_DATABASE}=="Cirtech (UK) Ltd", RUN+="/usr/bin/hid-feature set /dev/%k -f b0000 50", RUN+="/usr/bin/hid-feature set /dev/%k -f d0000 1"
}}

## TouchScreen
Same as #ForcePad.

## Stylus
Same as #ForcePad.

## Audio
This laptop requires Sound Open Firmware in order to make the sound card working.

## Power Management
There are typically battery charging adjustments available for ThinkPad laptops.

See Power management/Suspend and hibernate#Changing suspend method.

## Ambient Light Sensor
This model needs  for the ambient light sensors.

## Webcam
Certain models feature a MIPI camera (Sony IMX471 sensor) connected to the Intel IPU7 interface. Unlike standard USB webcams, this requires a complex driver stack and is not yet supported out-of-the-box.

## Kernel Support
The camera sensor driver is yet to be upstreamed, but for now can be installed using DKMS () with at least Linux kernel 6.19.

After install, you can verify the module is loaded with

## User Space
The proprietary Intel HAL is currently difficult to setup on Arch. An alternative is using libcamera's SoftISP, which processes the raw sensor data on the GPU or CPU.

There is a caveat that picture quality is currently worse than the proprietary stack.

# Install
# Install  to bridge the camera to PipeWire.

You can check if your camera is working with .

## WirePlumber Configuration
WirePlumber may not monitor libcamera devices by default. Create the following configuration file to force it.

{{hc|~/.config/wireplumber/wireplumber.conf.d/10-libcamera.conf|
wireplumber.profiles  {
  main  {
    monitor.libcamera  required
  }
}
}}

Restart the relevant services:

## IR Camera
Same as Webcam. The driver for the IR camera sensor (HM1092) is not available yet.

## Firmware
Can be updated via fwupd or the official bootable ISO updater provided by Lenovo.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  || 3 ||  || Enables Fn lock
|-
|  || 3 ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  || 4 Mutes microphone
|-
|  ||  ||  || 5
|-
|  ||  ||  || 5
|-
|  ||  ||  || 4
|-
|  ||  ||  || Toggles ACPI platform profile
|-
|  || 3 ||  || SW_CAMERA_LENS_COVER4 Toggles integrated camera
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  ||  ||  ||
|-
|  ||  ||  || +
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || switch to performance profile
|-
|  ||  ||  || switch to balanced profile
|-
|  ||  ||  || switch to low power profile
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || +
|}

# The key is visible via  and similar tools
# The physical key has a symbol on it, which describes its function
# An LED indicates the state of this switch
# This event is handled by "ThinkPad Extra Buttons"
# This event is handled by "Video Bus"

 and  can be swapped in the BIOS menu. The keycaps are the same size, so they could theoretically also be swapped to match the BIOS setting.

As of BIOS version N4DET32W (1.15 on the X9-14), the "Fool proof FN Ctrl" feature is enabled by default and ,  and some other act as  etc…

## Fingerprint sensor
Fingerprint sensor is located on the power button, reported as "Synaptics Sensors".

The fingerprint reader works out of the box using . See Fprint.
