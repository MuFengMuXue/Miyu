# Nuvision Solo 10 Draw

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Accelerometer || ||
|-
| Audio || ||
|-
| Bluetooth || ||
|-
| Cameras || ||
|-
| Display || ||
|-
| MicroSD reader || ||
|-
| Touchscreen || ||
|-
| Wi-Fi || ||
|}

The Nuvision Solo 10 Draw is a Tablet PC device, equipped with a 10.1 inch touchscreen display that supports 1920 x 1200 pixels. It also has support for N-Trig Pens like the ones for Microsoft Surface.

## System Specifications
*CPU: 	Intel Atom x5-Z8300 1.44GHz with Intel Burst Technology up to 1.84GHz
*GPU: 	Intel HD Graphics (Cherry Trail)
*Display: 	10.1 inches, 1920x1200, IPS LCD
*Dimensions: 	10.25x6.25x0.33in (260.35x158.75x8.38mm), 1.15lbs (0.52kg)
*Camera: 	5MP rear, 2MP front
*Storage:	32GB, expandable with Micro SD
*RAM: 	2GB
*Battery: 	6,800mAh
*Ports: 	Micro-USB, micro-HDMI, 3.5mm headset

## Installation
As of the 11th of February 2019 there is no known way to charge and have other peripherals attached to OTG at the same time for this particular tablet. This means your tablet will run off battery for the entire length of install time.

This device has a UEFI boot loader and BIOS settings menu but no keyboard included. In order to complete setup you will need a USB Hub, a wired USB keyboard, and a Micro-B OTG (On The Go) cable. Once fully set up you should be able to use the tablet without any extra peripherals.

Before starting, have your tablet in a powered off state, plug in your OTG cable, USB hub, your keyboard, and the USB storage device with your install media on.

Power on your tablet and at the moment you see the "Nuvision" boot logo press and hold down the  key on your keyboard until you have reached the BIOS menu. Or alternatively push the power button and hold the volume down button on the side.

In the BIOS menu navigate right to the 'save & exit' section with the arrow keys. Under 'save & exit' navigate down and under 'boot overrides' find your USB device. Press  to select and boot into the storage device.

At this point your tablet should boot into the Arch Linux install environment. You may continue with the standard installation guide.

## On-Screen Keyboard
Depending on your preferred window manager, install  for KDE or  for GNOME, see Tablet PC

## Backlight
Due to a bug the 'i915' graphics driver will fail to get control of the backlight with a similar error message to

 i915 *ERROR* Failed to own the pwm chip

It is possibly the same bug as described here https://bugs.freedesktop.org/show_bug.cgi?id=96571

As a workaround, make sure that graphic module 'i915' is never added to the initramfs or to the 'modules' section of .
This delays the system long enough in finding the correct display driver.

The idea is that 'i915' is loaded too early into the system and 'i915' tries to obtain control over parts of the system that have not fully loaded yet.

As of the 11th of February 2019, this workaround appears to work fine.

## Wireless
Included is a RTL8723BS chipset that supports Wi-Fi and Bluetooth. It appears 2.4GHz is only supported for Wi-Fi.

If you have any issues with connecting to wireless try this workaround. It is a settings change in the BIOS, you want to make sure 'SCC SDIO Support' is set to 'PCI Mode'.

To make that change follow the below guide.

From a powered off state, plug in a wired USB keyboard to a OTG cable and into your tablet.

Power on your tablet and at the moment you see the "Nuvision" boot logo press and hold down the ESC key on your keyboard until you have reached the BIOS menu.

In the BIOS navigate with the arrow keys.

Right to 'Chipset', down to 'South Bridge', down to 'LPSS & SCC Configuration', down to 'SCC SDIO Support' tap enter key and in the popup select 'PCI mode' and enter again.

Tap the ESC key to get back to the top menu and navigate to 'save & exit', then down to 'save changes and exit'.

Wi-Fi should behave much better after this change.

As of the 11th of February 2019, this workaround appears to work fine.

## Charging
A fix has been discussed here: https://bugzilla.kernel.org/show_bug.cgi?id=215882

And a patch was submitted here: https://lore.kernel.org/linux-iio/20220506095040.21008-1-hdegoede@redhat.com/

Until the changes make their way into the kernel. You will want to apply the following commands as root to ensure proper charging support for the Nuvision Solo 10 Draw.

You may want to make sure these commands run at boot, see Autostarting for some ways you can run these commands at boot.

## OTG (On-The-Go)
The drivers and chipset used for this particular tablet do not have automatic switching of OTG modes. It is either in 'device' mode or 'host' mode.
If you leave a OTG cable plugged in before booting up the system properly enables 'host' mode. But otherwise the system will be left in 'device' mode and OTG will not work unless it is switched.

However you can run these commands as root to switch the modes as needed.

Or you can leave the device in 'host' mode by default with a BIOS setting. Going to the BIOS > Chipset > South Bridge > USB Configuration > Default DRD Config   Changing "Default DRD Config" setting to "HostMode"
