# HP EliteBook 840 G1

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (AMD) || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Webcam || ||
|-
| Fingerprint reader || ||
|-
| Memory card reader || ||
|-
| Smart card reader || ||
|}

## Configuration
## UEFI Setup
Even if UEFI, Arch Linux and (e.g.) GRUB are correctly configured and with the correct UEFI NVRAM variables set, the system will not boot from the HDD/SSD. The problem is that HP hard coded the paths for the OS boot manager in their UEFI boot manager to  to boot Microsoft Windows, regardless of how the UEFI NVRAM variables are changed. There are two workarounds:

## Using the "Customized Boot" path option (recommended)
The latest HP firmware allows defining a “Customized Boot” path in the UEFI pre-boot graphical environment.
Select the “Customized Boot” option in the UEFI pre-boot graphical environment under “Boot Options” and set the path to your OS boot loader on the ESP (see EFI system partition), e.g.:

Always verify the correct path to the .efi file. Also, adjust the device boot order (also in the UEFI pre-boot graphical environment) to boot this entry first.

## Change the OS boot loader path to match the hard coded path
Change the UEFI application path of the OS boot loader to that hard coded path.
On your EFI system partition; e.g. with  being the EFI system partition mountpoint:

 # mkdir -p esp/EFI/Microsoft/Boot
 # cp esp/EFI/grub/grubx64.efi esp/EFI/Microsoft/Boot/bootmgfw.efi

or

 # mkdir -p esp/EFI/BOOT
 # cp esp/EFI/grub/grubx64.efi esp/EFI/BOOT/BOOTx64.EFI

## Encryption
This notebook supports HDD FDE (SED). The HDD/SSD can be locked by setting a password in the UEFI pre-boot graphical environment under the option "DriveLock" (this requires setting a password for the UEFI pre-boot graphical environment first). If you replace the HDD/SSD, make sure to get a compatible one to make use of this feature.

Otherwise, see Disk encryption for software-based encryption.

## AMD Graphics
In order to get the dedicated AMD graphics card to function properly, install AMDGPU first.
Set the following kernel parameters: .

Now, any application run with  (as described for using PRIME) is using the dedicated GPU.

## Audio
For HDMI Audio you need  in your kernel config (see https://bugzilla.kernel.org/show_bug.cgi?id=61471). In some cases, you will need  in . This will prevent freezes caused by hdmi audio cards conflicting.

## Resume / wake on lid open
This feature needs to be enabled in the UEFI setup: Advanced > Built-in device options > Wake unit from sleep when lid is opened

## Enable the microphone muting key
If your mute mic key () does not work, you actually just need to remap this key manually.

Here is an example of how you can do this by adding a custom mapping file:

Then, you just need to update the hardware database index.
