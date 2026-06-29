# Lenovo Yoga 14s 2021

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU || ||
|-
| Wi-Fi || ||
|-
| Bluetooth || ||
|-
| Screen || ||
|-
| Audio || ||
|-
| Webcam (optical) || ||
|-
| Webcam (infrared) || ||
|-
| Ambient light sensor || ||
|}

This page is for the Lenovo Yoga 14s 2021 (ITL / IHU) laptop with Intel Core i5-1135G7 / i5-11300H processor, delivered starting from 2020-11-01 (China).
It may be branded with different model names in other regions.

Most things will work out-of-the-box, if you just follow the normal set-up method. However, there are some issues you may want to solve before or during installation.

## Installation
If your Wi-Fi interface is missing, simply power-off and re-boot your device.

## Screen
Users may experience far more laggy animations in Plasma Wayland sessions than in X11 ones. This situation is known to be greatly relieved if this extra kernel parameter is added:

 i915.enable_guc=3

This workaround is only tested on an i5-11300H processor. One should test if it works on i5-1135G7 too.

## Wi-Fi
The Wi-Fi interface is missing sometimes after rebooting from Windows, but  can still discover it.

It is known that after powering-off and booting again, this will be corrected.

## Audio
This laptop requires Sound Open Firmware in order for the soundcard to work.

## Webcam (Infrared)
This laptop comes with infrared camera and light, to support Windows Hello. The infrared webcam can be detected on Linux automatically, but the light does not work by default.

To make them work, install and configure .

See more instruction on Howdy, a program that imitates Windows Hello on Linux.
