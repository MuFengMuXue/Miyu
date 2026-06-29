# Lenovo Yoga Pro 7 14AHP9

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  || *
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

For a general overview of laptop-related articles and recommendations, see Laptop.

## Accessibility
The UEFI offers one mode of operation, GUI.

The GUI can be navigated to some degree via the keyboard.  and  arrow keys to move the selection and  to activate.

## Firmware
fwupd does not support this device yet and likely is not going to.

Lenovo support page for this model only provides .exe installer for UEFI updates. There is no option in the UEFI itself to select a binary blob from USB stick.

CPPC is enabled in UEFI in the latest BIOS update, otherwise the kernel falls back to the legacy  driver for CPU frequency scaling. This is resolved in Linux 6.12. Battery charge threshold is supported.

## Updating UEFI
[https://www.reddit.com/r/Lenovo/comments/1i7qyr1/psa_how_to_update_bios_on_lenovo_yoga_pro_7_gen_9/ A workaround is to install the UEFI from Windows PE. A common choice is Hiren's Boot CD. Boot into the live environment, download the update file and install it.

## Secure boot
The firmware only allows restoring Microsoft vendor keys, and does not have any options to install any custom keys. To install keys you can use tools such as . No Option ROMs appear to be present as per testing with:

See Secure Boot for more details.

## Issues
## Headphones
There is an issue with using headphones through the 3.5mm jack when using PipeWire. When headphones are connected, little to no sound may be audible. To resolve this, adjust the  volume to 100% using  when the headphones are plugged in. After that, the regular volume control in PipeWire will function as expected.

The  volume must be adjusted every time headphones are connected.

## Laptop Built-in Speakers
Another issue with sound on Lenovo Yoga Pro models (specifically on  and  and ) is sound card pin mixup. It manifests as follows: changing volume does not seem to have any effect, but when setting it to 0% volume does actually turn off. To fix volume control you need to create  with row below and reboot:

The quirk is know in linux kernel, e.g. see the constant   in kernel realtek patches

Supposedly its been fixed with kernel patch but I needed the manual modprobe option.

## Panel Self Refresh issues
PSR can cause flickering and random freezes/crashes, see AMDGPU#Frozen_or_unresponsive_display_(flip_done_timed_out) for details.

 is part of
 from
drivers/gpu/drm/amd/include/amd_shared.h.

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
|  ||  ||  || No symbol
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables/disables keyboard backlight
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
