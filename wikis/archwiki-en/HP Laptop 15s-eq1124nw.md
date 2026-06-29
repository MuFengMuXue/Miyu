# HP Laptop 15s-eq1124nw

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Wi-Fi ||  ||
|-
| GPU (AMD) ||  ||
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| SD-card reader ||  ||
|-
| Audio (Onboard + jack) ||  ||
|-
| Audio (HDMI?) ||  ||
|-
| Speakers || ||
|-
| Microphone || ||
|}

The HP 15s-eq1124nw is a laptop featuring a 15.6" FHD IPS display, 16GB of RAM (2x8GB, 2666MHz), 512GB NVMe SSD, and a AMD Ryzen 5 4500U with integrated graphics.

## Installation
The Realtek RTL8822CE network card and integrated AMD GPU graphics card require  to be installed.

## Accessibility
The UEFI setup is a simple, text-based interface, navigated with a keyboard. It does not expose many options apart from the standard time/date settings, and boot configuration.

To show a list of all available menus, press .

To access the UEFI setup, press .

To access the boot menu, press .

## Firmware
fwupd does not support this device.

## Secure Boot
Secure Boot is untested, The device does not come with any Secure Boot keys installed from the factory, but there is an option in the UEFI to install HP factory keys.

## Suspend-to-RAM
See Power management/Suspend and hibernate#Changing suspend method for the general context in which this workaround applies.

The firmware does not expose the necessary ACPI object () to support suspend-to-RAM, but it does have a similarly named object (), which is most likely patched at boot-time to enable this functionality (although there is no UEFI option to configure this). One can manually add support for suspend-to-RAM by doing the following:

First, get the  compiler by installing the  package.

Then compile the following source using :
{{bc|
DefinitionBlock ("ssdt.aml", "SSDT", 1, "HACK  ", "S3      ", 0x00000001)
{
	Scope (\)
	{
		Name (_S3, Package (0x04)
		{
			0x03,
			Zero,
			Zero,
			Zero
		})
	}
}
}}

And finally, tell the kernel to use the new ACPI table.

## Webcam
The webcam supports 720p, but this resolution is only available when not using the YUYV 4:2:2 video format (checked with OBS).

## Function keys
By default, keys - perform their alternative functions, and  is needed to press , but there is a UEFI option to change this behavior. The following table assumes this setting was disabled.

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
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
|  || 3 ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd handles this by default, but does not consume it.

Additionally, Linux logs the following unknown key (what key combination triggers them is yet to be identified):

## Kernel warnings
The kernel reports that the TSC timer is unstable:

The kernel also reports the following ACPI errors:

Despite these errors, the system is stable and operates correctly.
