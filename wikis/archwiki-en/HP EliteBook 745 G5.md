# HP EliteBook 745 G5

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| AMD graphics || ||
|-
| VGA || ||
|-
| HDMI || ||
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
| Pointing stick || ||
|-
| Camera || ||
|-
| Fingerprint reader || ||
|-
| Smart card Reader || ||
|-
| 4G modem || ||
|-
| Dock || ||
|-
|}

## Firmware
The last firmware is mandatory to modify the BIOS parameters. At the moment of writing this entry: 01.09.01 Rev.A.
In upgraded BIOS, disable the secure boot to be able to load any boot loader.

From Windows, it is easy to force the UEFI priority: https://www.rodsbooks.com/refind/installing.html#windows

Be careful with rEFInd: https://www.reddit.com/r/archlinux/comments/cgkhop/help_refind_boot_manager_hangs_seconds_after/

In this specific case, avoid option scanfor internal.

## Kernel options
System freezes randomly when the proper parameters are not loaded https://www.reddit.com/r/linuxhardware/comments/afktfv/linux_freezes_and_amd_2500u_chipset/

Recommended kernel parameters:

 idle=nomwait amdgpu.gpu_recovery=1 amd_iommu=pt audit_enabled=0

## AMD graphics
Use AMDGPU.
To avoid any problem, make sure  has been set as the first module in the mkinitcpio#MODULES array, e.g. . Take care as the original EFI system partition could have not enough space for amdgpu and radeon modules.

## SmartCard reader
Works perfectly with  & . Read Smartcards for more info.

## Function keys
Usual function keys work out of the box. Keyboard Backlight controls work out of the system, so it is perfectly working in Linux.
However, rare keys as telephone or calendar are not assigned to anything.
You can remap using udev.
For example, the call key can be remapped as an insert key by creating  that contains this:

## Audio
If you have trouble to get audio properly working (e.g. no audio input or no audio output after adjusting volume) and you see errors in the journal:

 pulseaudio2299: Failed to create sink input: sink is suspended.

Comment out the following line like this:
