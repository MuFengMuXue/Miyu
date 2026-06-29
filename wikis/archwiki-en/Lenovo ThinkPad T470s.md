# Lenovo ThinkPad T470s

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wireless || ||
|-
| Mobile broadband ||  ||
|-
| Audio || ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Smartcard reader ||  ||
|-
| Bluetooth ||  ||
|-
| Fingerprint reader ||  ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo Thinkpad T470s.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Firmware
As of writing, the current BIOS version is 1.54. By visiting the downloads section (for the type HG/HF T470s) an ISO can be downloaded and burned to disk which will perform the update This laptop is unique in that it retains the Thinkpad dock connection as well as provides docking ability over USB-C. We have tested with the [https://www.thinkwiki.org/wiki/ThinkPad_Ultra_Dock Thinkpad Ultra Dock and are able to utilize multiple HiDPI monitors via individual connections (e.g. no display port chaining). There are published firmware updates for the dock that require Windows to install. DisplayPort chaining works via USB-C to DisplayPort adapter.

## Updating the BIOS
## Via a USB key
In order to update the BIOS/UEFI using a USB key, download the "BIOS Update (Bootable CD)" ISO from and follow the instructions on Flashing BIOS from Linux#Bootable optical disk emulation.

## Using fwupd
# Install
# Get the official update utility from [https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t470s/downloads/ds120418-bios-update-utility-bootable-cd-for-windows-10-64-bit-81-64-bit-7-32-bit-64-bit-linux-thinkpad-t470s and follow the instructions from the same page.

## Kernel and hardware support
Hardware video acceleration with Kaby Lake seems to work fine via VA-API.

## Mobile broadband
The mobile broadband card is a Sierra EM7455. It works with Google's Project Fi.

## Configuration
## Fingerprint reader
As of December 2024, the fingerprint reader is still under prototype development, but works just fine.

While  does not yet support the sensor, it can be set up using  and  - install the packages and configure the sensor as described in fprint#Configuration.

Do note that some packages have a hard dependency on  (e.g. ) - for those you will have to edit the PKGBUILDs to remove the dependency and build the packages manually.

## Troubleshooting
## Fan does not spin down after suspend-resume
On  via wayland, suspend-resume results in the fan holding at 100% without ever spinning down. Alternatively if you use xorg this does not seem to happen. This issue has been resolved in BIOS/UEFI version 1.20.

## HDMI audio does not work with PulseAudio
The Intel HD audio module manages both the internal analog audio devices (e.g. speakers, mic, headphone jack) and the HDMI / DisplayPort audio outputs. Which inputs / outputs are used is selectable via the card profile. The profile selection can be changed using the  application in the Configuration tab.

Analog Stereo Duplex is the default, using the internal speakers / headphone jack and the internal microphone. To feed audio out the internal HDMI port while still using the internal microphone for input, select Digital Stereo (HDMI 2) Output + Analog Stereo Input.

PulseAudio will remember this selection and auto switch to/from it based on the status of the HDMI port.
