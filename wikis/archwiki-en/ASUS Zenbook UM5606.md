# ASUS Zenbook UM5606

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || PS/2 ||
|-
| Touchscreen & stylus || PS/2 ||
|-
| Keyboard || PS/2 ||
|-
| GPU ||  ||
|-
| NPU ||  ||
|-
| Webcam ||  ||
|-
| ALS || ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wireless ||  ||
|-
| Thunderbolt ||  ||
|-
| TPM ||  ||
|-
| Fans || ||
|}

This page is for the ASUS Zenbook S 16 (UM5606/UM5606WA), although this may help for other 2024 ASUS laptops with the Ryzen 9 AI chips (HX 365/370) such as the ASUS Vivobook S 16 (M5606) and the ProArt P16 (H7606/H7606WV).

## Installation
When booting into the Arch Linux ISO, press  to edit the chosen boot option and add the  kernel parameter to prevent freezing during installation. A similar setting may or may not be needed after installation, see #Power management.

## Accessibility
The UEFI may be difficult to navigate using screen readers, and it may be difficult to see the boot menu edit options when inputting the temporary kernel parameter. If necessary, you should proceed with the assistance of a sighted person.

## Firmware
fwupd shows the CPU/GPU, TPM, SMU, UEFI firmware, NVMe, System firmware (which can have an attestation added), and the webcam. Most of them show as updatable, but no OTA updates have been released as of the time of writing.

There is an important UEFI update that has been posted on ASUS's website -- to apply it, download the "BIOS for ASUS EZ Flash Utility" (not "for Windows") file, extract the contents to a FAT32 formatted USB drive, reboot and go into the firmware setup, and then go into the "EZ Flash" menu. The update can be found here: checks the ASUS website for BIOS updates, and this can be set up with a systemd user service/timer to act as a crude method to automatically check for BIOS updates.

## Power management
Linux ≥6.14rc1 is needed to alleviate most power management problems, including high power usage during suspend and random freezing/hanging.

The ProArt P16 (H7606) may have high power usage during suspend, as observed with [https://pypi.org/project/amd-debug-tools/ AMD Debug Tools. This can be improved with udev rules to set power management to auto:

{{hc|/etc/udev/rules.d/50-asus-usb-power.rules|2=
# Enable autosuspend for all USB devices, including ASUS ITE device
ACTION=="add", SUBSYSTEM=="usb", ATTR{power/control}="auto"

# Specific rule for ASUS ITE Device if needed
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="0b05", ATTR{idProduct}=="19b6", ATTR{power/control}="auto"
}}

You can also set  to prevent wakeup from the lid switch

## Panel Self Refresh
Random freezing/hanging may persist despite upgrading to a 6.14 release candidate kernel due to a known issue with PSR2-SU on Strix Point APUs. PSR2-SU should be disabled by default in future kernels, it can be disabled in the meantime by setting , which will disable PSR2-SU but keep legacy PSR enabled. PSR status can be confirmed using  which should not return a non-negative value (note that compositor options and misbehaving applications may also interfere with PSR). If you continue to encounter issues, set  as in the installation, which will entirely disable PSR.  may also need to be set if you encounter issues with external monitors.

If you are using KDE, you need to edit the  user unit and add this to the configuration:

## Fan control
The firmware supports four fan profiles: standard, quiet, high-performance, and full-performance. Out of the box, it's set to standard, but this can be changed with .

## Wake from suspend
## Screen Freeze Issues
There is currently known a problem when waking up from suspend (s2idle) that the screen will freeze for about 10 seconds. This problem is currently caused by the  kernel module failing to properly re-initialize the MT7925 wireless card after resuming. This has been fixed in Linux ≥6.14-rc1.

However, as a temporary workaround for older kernel, you can unbind the device from the driver before suspending and later rebind it after resuming. This can be achieved using the following two systemd service units:

## Bluetooth issues after resume
Even with Linux ≥ 6.14 where the Wi-Fi freeze is fixed, the Bluetooth component of the MT7925 (which typically connects via the USB bus internally) may fail to initialize after resuming from suspend (s2idle). Symptoms include  showing "No default controller available" and  reporting  timeouts or  (device descriptor read/64).

## Power management workaround
This is often caused by the USB autosuspend feature being too aggressive for the MediaTek controller during the wake-up transition. You can disable autosuspend specifically for the Bluetooth module via a udev rule.

First, identify your Bluetooth device ID (usually under IMC Networks or MediaTek):

  $ lsusb | grep -i blue
  Bus 003 Device 002: ID 13d3:3602 IMC Networks Wireless_Device

Create a udev rule to keep the device powered on during suspend:

{{hc|/etc/udev/rules.d/80-mt7925-bt.rules|2=
# Disable autosuspend for MT7925 Bluetooth to fix resume timeouts
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="13d3", ATTR{idProduct}=="3602", ATTR{power/control}="on"
}}

Replace  and  with your actual vendor and product IDs.

## Hardware reset
If the Bluetooth module has already entered a deadlocked state (showing repeated  in logs), a simple reboot might not be enough due to residual power. A "cold boot" is required: power off the laptop, disconnect the power adapter, and hold the power button for 20-30 seconds to perform a full hardware reset.

## Reduce idle power at 2880x1800@120 Hz (MCLK/FCLK stuck high)
The UM5606 laptop's internal eDP panel (model ) has two default modes 2880x1800@60 Hz and 2880x1800@120 Hz, with the former one encoded in the Detailed Timing Descriptor (DTD) of the base EDID block and the latter one in the displayID extension block. While the 2880x1800@120 Hz mode offers a smoother experience, it uses a very small vertical blanking (vblank) interval, which may cause the AMDGPU display driver to keep GPU memory clock (MCLK) and fabric clock (FCLK) at a higher DPM state even at idle/light load, significantly increasing power consumption. This issue contributes one of the most damaging factors to battery life when using the laptop on battery at 120 Hz. With the issue solved and other power management improvements in place (e.g. Power-saver profile, Panel self-refresh), idle/light-load power consumption at 120 Hz can be reduced to around 6-8 Watts, presenting a very competitive battery life.

Concretely, the symptoms are:

* With mode 2880x1800@120 Hz, the MCLK stays at around 800 MHz at idle as can be observed using , even though the Strix Point APU's lowest MCLK state is 400 MHz.
* With mode 2880x1800@60 Hz, the MCLK drops to 400 MHz at idle as expected.
* The issue persists across Wayland and X11 sessions.

This issue matches exactly what is described in this gist about small vblank intervals preventing MCLK/FCLK from down-scaling. Thus, a workaround is to use a custom modeline or a custom EDID that increases vertical blanking while staying within the panel's advertised maximum pixel clock of 660 MHz.

The EDID info of the panel can be checked using  with  (from package ):

 # get-edid | edid-decode

In summary, the stock 2880x1800@120 Hz mode has the following timing:

* Horizontal: Hfront=32, Hsync=8, Hback=60, Hwidth=2880, Hpol=Neg; => hblank=100
* Vertical: Vfront=8, Vsync=8, Vback=8, Vheight=1800, Vpol=Neg; => vblank=24 (very tight vblank)
* Pixel clock: 652.264 MHz => 120 Hz refresh rate

A known good timing is as follows, with vblank increased to 40:

* Horizontal: Hfront=32, Hsync=8, Hback=60, Hwidth=2880, Hpol=Neg; => hblank=100 (same as stock)
* Vertical: Vfront=8, Vsync=8, Vback=24, Vheight=1800, Vpol=Neg; => vblank=40
* Pixel clock: 657.984 MHz => 120 Hz refresh rate (within panel limit)

The following two subsections describe how to implement this timing in X11 and Wayland sessions respectively.

## Workaround for X11 sessions
For X11 sessions, it is possible to simply use a custom modeline with  to increase vblank for solving the MCLK/FCLK scaling issue. Thus, for Wayland session users, the X11 session can also be leveraged to conduct a quick test and verification.

Add the custom modeline:

 $ xrandr --newmode "2880x1800_120_vb40" 657.984 2880 2912 2920 2980  1800 1808 1816 1840 -hsync -vsync

Associate the new mode with the eDP output (replace with the actual output name, but it should be "eDP" anyway):

 $ xrandr --addmode eDP "2880x1800_120_vb40"

Set the eDP output to use the new mode:

 $ xrandr --output eDP --mode "2880x1800_120_vb40"

## Workaround for Wayland sessions
For Wayland sessions it can be hard to set a custom modeline. So instead, a custom EDID binary can be created and loaded via the kernel command line. While the previous gist suggest using  for custom EDID creation, the  tool is in fact insufficient for this case as the 120 Hz mode is stored in the displayID extension block, which  cannot edit.

Create a custom EDID binary:

*One method is using CRU (Custom Resolution Utility) on Windows:
** Edit the internal panel's preferred timing to use hblank=100 and vblank=40 at 120 Hz.
** Export the modified EDID as a binary  file.
*If you are comfortable downloading a pre-made EDID binary, you can download it from here.

Install the custom EDID binary into the firmware search path:

Add the kernel parameter (adjust connector name if needed):

 drm.edid_firmware=eDP-1:edid/edid_mclk_fix.bin

You can confirm the connector name using . Say the output is , then the connector name is .

Ensure the EDID blob is available at boot (initramfs):

* mkinitcpio:

:Then regenerate the initramfs.
* dracut:

:Then regenerate the initramfs.

Reboot and verify the absence of EDID load errors:

 # dmesg | grep -iE 'edid|edid_firmware|Requesting EDID firmware|failed'

Verify MCLK can downclock at idle at 120 Hz using .

## Audio
Linux ≥6.13 is needed to get audio fully working without sounding tinny.

## Wireless
Wireless may be unstable. If you're experiencing issues, switch from  to iwd, then create this file and reload units:

## NPU
Currently Linux ≥6.19rc1, the private branch of the XRT NPU drivers, and the private branch of RyzenAI-SW are needed to get the NPU properly working for Onnx model inference. Functionality is currently being tested.

## ALS
The Ambient Light Sensor (ALS) works out of the box on GNOME, and on wlroots/smithay compositors with  and this configuration:

{{hc|~/.config/wluma/config.toml|2=
path = "/sys/bus/iio/devices"
thresholds = { 0 = "night", 2 = "dark", 5 = "dim", 8 = "normal", 13 = "bright", 15 = "outdoors" }

output.backlight
name = "eDP-1"
path = "/sys/class/backlight/amdgpu_bl1"
capturer = "none"
}}

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Enables Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  || Adjusts keyboard backlight
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
|  ||  ||  || Unknown (scancode 240)
|-
|  ||  ||  ||
|-
|}

# The key is visible to , , , and similar tools
# The physical key has a symbol on it, which describes its function
# The key isn't visible to keycode viewer tools, but it sends a signal that D-Bus picks up on, and GNOME sees it (and shows the OSD popup). The signal looks like this:
::Where the  can be a value between 0 and 3, denoting which of the four brightness levels the keyboard backlight has been set to (0 = off, 1 = low, 2 = medium, 3 = high).
