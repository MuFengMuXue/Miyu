# GRUB/EFI examples

It is well known that different motherboard manufactures implement UEFI differently. The purpose of this page is to show hardware-specific methods known to work when installing/restoring GRUB in EFI mode.

## Acer
## Aspire V3-571G (Possibly other Aspire One laptops as well)
Some variations of this laptop have a only partial EFI compatibility due to originally shipping with Windows 7 only. Later revisions of this laptop shipped with more complete UEFI compatibility. Due to this the earlier revisions can only boot GRUB if it is placed where the Windows boot loader binary is expected (). However the binary can only be booted manually from the boot menu (on key F12), likely because it is missing Microsoft signatures. A solution to this problem is to upgrade to the newer version of the system firmware, however the process is not straight forward as earlier revisions of the machine are locked out of upgrading for some reason.

The following steps can be taken to bypass the restriction and upgrade to a later revision firmware:

* Acquire an incompatible 2.x version of the BIOS firmware for the same model machine from Acer Acer CDN direct linkArchive.org mirror.
* Extract the archive to obtain the flasher executable (eg. Q5WV1221.exe).
* Open this executable in a hex editor of your choice (a good simple one is ).
* In the hex editor search for the block flag string .
* Change the ASCII string so that it becomes  (That's changing the last byte from hex 31 to 30).
* Save the modified binary.
* Obtain a copy of FreeDOS, flash it to a boot media and put your modified binary on the boot media as well (more on that here Flashing BIOS from Linux#FreeDOS)
* Run your modified binary from within FreeDOS and follow the instructions on screen. Upon completion you should have your firmware upgrade to the officially unsupported 2.x version.
* You can now install GRUB normally as described here GRUB#UEFI systems.

More info:

* https://www.bios-mods.com/forum/Thread-Upgrade-Bios-To-UEFI-Insyde?pid=159051#pid159051
* https://catchtito.blogspot.com/2013/05/how-to-update-to-2x-bios-from-1x-bios.html

## Apple Macs
Use bless command from within macOS to set  as the default boot option. You can also boot from the macOS install disc and launch a Terminal there if you only have Linux installed. In the Terminal, create a directory and mount the EFI system partition:

 # cd /Volumes
 # mkdir efi
 # mount -t msdos /dev/disk0s1 /Volumes/efi

Then run bless on  and on the EFI system partition to set them as the default boot options.

 # bless --folder=/Volumes/efi --file=/Volumes/efi/EFI/GRUB/grubx64.efi --setBoot
 # bless --mount=/Volumes/efi --file=/Volumes/efi/EFI/GRUB/grubx64.efi --setBoot

## ASUS
## Z68 Family and U47 Family
 # cp esp/EFI/GRUB/grubx64.efi esp/shellx64.efi

After this launch the UEFI Shell from the UEFI setup/menu (in ASUS UEFI BIOS, switch to advanced mode, press Exit in the top right corner and choose "Launch EFI shell from filesystem device"). The GRUB menu will show up and you can boot into your system. Afterwards you can use efibootmgr to setup a menu entry, for example if you have the EFI system partition on :

 # efibootmgr --create --disk /dev/sda --part 1 --write-signature --loader /EFI/GRUB/grubx64.efi --label "GRUB" --verbose

If your motherboard has no such option (or even if it does), you can use UEFI shell to create a UEFI boot option for the Arch partition temporarily.

Once you boot into the UEFI shell, add a UEFI boot menu entry:

 Shell> bcfg boot add 0 FS0:\EFI\GRUB\grubx64.efi "GRUB"

where  is the mapping corresponding to the EFI system partition and  is the file from the  from the  command above.

This will temporarily add a UEFI boot option for the next boot to get into Arch. Once in Arch,  and confirm that  creates no errors (no errors meaning you successfully booted in UEFI mode). Then GRUB installation can be performed again and should successfully permanently add a boot entry in the UEFI menu.

## ux32vd
There is a caveat. If the machine was booted from MBR then  (or efibootmgr) will fail to create the UEFI boot entry with the following error:

 EFI variables are not supported on this system

You first need to boot the machine with EFI and then create the boot entry. This can be done the way described for Z68 Family: by copying  into  and selecting "Launch EFI shell from filesystem device".
After successful boot it is possible to create a boot entry using grub-install or efibootmgr.

## P8Z77 Family
Install GRUB and copy the modified UEFI Shell binary to ESP.

The EFI system partition should contain just two files:

 /Shell.efi
 /EFI/GRUB/grubx64.efi

* Reboot and enter the BIOS (the  key will do this).
* Using the arrow keys, move to the exit menu and drop down to the EFI shell.
* Add an entry for Arch to the menu. Below is an example, see the Unified Extensible Firmware Interface#Launching UEFI Shell article for more.

Within UEFI shell

 Shell> bcfg boot dump -v
 Shell> bcfg boot add 1 FS0:\EFI\GRUB\grubx64.efi "GRUB"
 Shell> exit

* Reboot the machine and enter the BIOS.
* Navigate to the Boot section and adjust the boot order to with the "GRUB" being the one on the SSD.
* Boot to this entry and enjoy.

## M5A97
Finish the standard Arch install procedures, making sure that you partition your boot hard disk as GPT.

Install GRUB and copy the modified UEFI Shell binary to ESP.

The reason that we need this shell application is that the  command will fail silently during .

After this launch the UEFI Shell from the UEFI setup/menu (in ASUS UEFI BIOS, switch to advanced mode, press Exit in the top right corner and choose "Launch EFI shell from filesystem device"). The UEFI shell will show up. From here we need to add our GRUB entry to the NVRAM.

 Shell> bcfg boot add 3 FS0:\EFI\GRUB\grubx64.efi "GRUB"

where  is the mapping corresponding to the EFI system partition and  is the zero based boot entry index.

To list the current boot entries you can run:

 Shell> bcfg boot dump -v

## Asrock
## Z97M Pro4
This is a similar procedure to Asus Z68 Family. This was tested on a Z97M Pro4 BIOS P1.90.

 # cp esp/EFI/GRUB/grubx64.efi esp/shellx64.efi

After this launch the UEFI Shell from the UEFI setup/menu (in ASROCK UEFI BIOS, goto Exit tab and choose "Launch EFI Shell From Filesystem Device"). The GRUB menu will show up and you can boot into your system. Afterwards you can use efibootmgr to setup a menu entry, for example if you have the EFI system partition on :

 # efibootmgr --create --disk /dev/sda --part 1 --write-signature --loader /EFI/GRUB/grubx64.efi --label "GRUB" --unicode

## Dell
## PowerEdge T30
The Dell UEFI implementation needs the UEFI firmware workaround to load grub. Otherwise it will drop into a "no OS found" screen.

## Latitude E7450
In addition to the UEFI firmware workaround (without which GRUB is not launched), the Dell Latitude seems to require to have the EFI system partition mounted on . When ESP is mounted on , GRUB fails to find the configuration files and launches the rescue console.

## MSI
These MSI motherboards seem to want the EFI program to exist in a different location from where GRUB installs it.  Do one of the following after following the instructions for installing GRUB:

## B250M PRO-VH
 # mkdir esp/EFI/BOOT
 # cp esp/EFI/grub/grubx64.efi esp/EFI/BOOT/shellx64.efi

## B150 PC MATE / B250 PC MATE / H110I PRO / Z370 GAMING PLUS / MPG B760I EDGE WIFI
Install GRUB to the default/fallback boot path.

## HP
## EliteBook 840 G1 & Probook 6570b
See HP EliteBook 840 G1#UEFI Setup for details.

## Intel
## S5400 Family
This board can run in BIOS or in EFI mode. BIOS mode requires an MBR partitioned hard drive, EFI - a GPT hard drive. Please note that this board operates on the Intel EFI v1.10 specification, and is IA32 (32-bit) only. The normal procedure for UEFI installation can be followed, with the exception of the following changes.

* Instead of using the  target,  has to be used
* The  command is not available for pre-UEFI (v2.0) firmware. A  file can be used on the root of the EFI system partition containing the path to the boot loader. For example:  has to be placed in the  file on the root of the EFI system partition.
* The  file has to be placed in the same directory as the grub EFI binary, otherwise GRUB will not find it and enter the interactive shell.

## Lenovo
## K450 IdeaCentre
The EFI system partition requires the file  to be present in order to boot, otherwise you will receive "Error 1962: No operating system found. Boot sequence will automatically repeat."

Install GRUB to the default/fallback boot path.

This is a workaround for what is likely a bug in the UEFI implementation.

## M92p ThinkCentre
This system whitelists UEFI boot entries. It will boot from a entry called "Red Hat Enterprise Linux" or "Windows Boot Manager"(Jan. 2021). So specify the  appropriately:

 # grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id="Red Hat Enterprise Linux" --recheck --debug

or

 # grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id="Windows Boot Manager" --recheck --debug

It is also possible to edit your EFI config with efibootmgr.
First, list your boot entries:

 # efibootmgr

Delete old entry for Windows Boot Manager:

 # efibootmgr -Bb 0000

Now create a new boot entry which points to your desired boot loader on your hard drive. Be aware: -p defines on which partition your EFI system partition lies.

 # efibootmgr -c -d /dev/sda -p 1 -L "Windows Boot Manager" -l "\EFI\boot\grubx64.efi"

This will set up your EFI to boot the entry "Windows Boot Manager" and load the grub boot loader.

## X270 Thinkpad
Install GRUB to the default/fallback boot path.
