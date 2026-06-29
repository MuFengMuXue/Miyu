# Microsoft Surface Book 2

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| Camera || ||
|-
| Card reader || ||
|-
| Bluetooth || ||
|}

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on Microsoft Surface Book 2 devices.

## Installation
The information in Boot loaders applies here.  and systemd-boot work well.

## UEFI setup and disabling Secure Boot
Disabling Secure Boot is not necessary, but makes things easier.

Follow the manufacturer's directions for accessing UEFI setup:

# Shut down your Surface and wait about 10 seconds to be sure it is off.
# Press and hold the volume-up button on your Surface, and, at the same time, press and release the power button.
# When you see the Surface logo, release the volume-up button. The UEFI menu will appear within a few seconds.

## Boot from USB
Booting from USB is possible by reordering boot devices in the UEFI setup or by holding the volume down button while booting.

The "Enable Boot from USB devices" UEFI option needs to be enabled in order to boot to the installer.

## Graphics
## Drivers
The standard  driver works with the Surface Book devices.

The NVIDIA 1050 and 1060 cards in the Surface Book 2 Performance Base are recognized by the kernel and supported by .

Without the kernel (linux-surface), there was a bug which causes it to be effectively useless because when a load is put on the NVIDIA graphics hardware, it immediately and severely throttles down to around 139MHz. The reason, as reported by nvidia-smi, is software thermal throttling. The cause is that, apparently, the fan cannot be controlled automatically, nor through nvidia-smi or nvidia-settings, even when the  option is set to 8.

## Console fonts
Because of the screen's resolution, the console font is barely readable - refer to Linux console#Fonts on how to change them.

Using  with 32pt looks good on Surface Book 2 on the vconsole (add  to  after installing).

## Touchscreen
Only works in a Window Manager or Desktop Environment that has full support for it. It is recognized as a mouse click otherwise.

## Audio
Surface Book 2 devices exhibit a hissing noise at times. See Advanced Linux Sound Architecture#Disabling auto mute on startup for the fix.

Built-in speaker quality can be improved with the HDAJackRetask utility available in the  package. In HDAJackRetask, override the 0x14 pin to 'Internal speaker (LFE)' and the 0x1e pin to 'Internal Speaker', then select 'Apply now' to test your settings.

## Wi-Fi
Requires the installation of the  package for the wireless network interface to be recognized by the kernel.

Since September 2018, Surface Book 2 Wi-Fi may power off during use. When this happens, it is not visible with lspci and rebooting is a way to get it back on. However, this behavior can be prevented (temporarily) by installing  and running the following command as root:

 # iw dev wlp1s0 set power_save off

To permanently fix the issue with NetworkManager, add this to your NetworkManager config. (Such as )

 wifi.powersave = 2
 [device
 wifi.scan-rand-mac-address=false

## Keyboard base
Removal is a few seconds slower in Linux than in Windows, may cause touchscreen to stop working until reboot and may cause issues with dedicated graphics (if equipped). Installing  reduces this time significantly.

## Camera
Front and rear cameras both function, but should be considered experimental at this time.

Install  and  to use the cameras in applications that support libcamera. The qcam utility available in  can be used to easily test camera functionality.

Both cameras work in  after installing  and enabling media.webrtc.camera.allow-pipewire in the browser.

## Accelerometer
Install the  package and enable .

To check that that iio-sensor-proxy is working, run

 $ monitor-sensor --accel

then rotate your device. The rotation should appear in your terminal window.

Compatible desktop environments, such as KDE Plasma, can automatically rotate the display once the service is enabled and the display rotation is enabled through the desktop environment's settings.
