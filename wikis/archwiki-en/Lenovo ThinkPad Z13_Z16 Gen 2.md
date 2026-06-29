# Lenovo ThinkPad Z13/Z16 Gen 2

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Haptic Touchpad ||  ||
|-
| TrackPoint || ||
|-
| TouchScreen ||  ||
|-
| Stylus ||  ||
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
| Bluetooth ||  ||
|-
| Fingerprint reader ||  ||
|-
| USB4 || ||
|-
| TPM || ||
|}

## Accessibility
The BIOS only offers GUI operation, and can be navigated to some degree via the keyboard.

## Haptic Touchpad
The device uses a I2C HID Sensel haptic touchpad, with configurable force requirements and haptic feedback.

## Sensitivity and Haptic intensity
The haptic intensity can be set using  at runtime. Configuration options can be listed as follows after installing the package:

 # hid-feature list /dev/hidraw0

To set maximum haptics:

  # hid-feature set /dev/hidraw0 -f b0000 100

Configuration for click sensitivity has not yet been identified,

The device reverts to default settings after reboot, which feels like a high sensitivity requiring only light press and a medium or low haptic intensity.

## Webcam
Works out of the box. However, web applications have a tendency to pick the IR camera first, which will fail and require changing the camera selection.

## GPU
The integrated GPU is seeing very active support from AMD. The iGPU is shared with certain Framework models, with AMD actively engaging with their forums.

The dedicated GPU is an older RDNA2 chip. All displays connect to the iGPU.

## GPU Resets
The GPU currently has a tendency to reset under certain applications, Chrome and Electron in particular. Handling this gracefully requires a display server that correctly handles GPU resets.

In case of Sway, this currently requires running the master branch through .

## Display brightness (OLED)
The brightness for the OLED panel uses the amdgpu's "aux" controls. The brightness slowly animates to the selected value. The scale appears very non-linear, with 30% under Linux more or less matching 75% under Windows.

Whenever the display is re-enabled (e.g., due to closing the lid), it does so at a default brightness value despite the kernel still reporting the previously set value.

## USB4/Thunderbolt
When connected to a Thunderbolt 3 dock during boot, USB has a tendency to stop working after boot completes, despite USB being functional for example in the cryptsetup prompts earlier.

Disconnecting the cable and plugging it back in fixes it as a workaround.

## Function keys
 is placed to the left of , which differs from the normal ThinkPad placement where  is on the left. The buttons are the same size, and can be swapped in the firmware as usual.

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables Fn lock
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
|  ||  ||  || 3
|-
|  ||  ||  || Toggle Webcam
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Cycle keyboard backlight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || 3
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
|}

# The key is visible via  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
