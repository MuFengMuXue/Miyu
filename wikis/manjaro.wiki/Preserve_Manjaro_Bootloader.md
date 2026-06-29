This page contains [[changes](//wiki.manjaro.org/index.php?title=Preserve_Manjaro_Bootloader&oldid=42288&diff=52117)] which are not marked for translation.

Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Preserve_Manjaro_Bootloader/tr "Manjaro Bootloader'ı Koru (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Preserve_Manjaro_Bootloader/ru "Сохранение загрузчика Manjaro (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Bios-legacy systems]](#Bios-legacy_systems)
-   [[3] [UEFI systems]](#UEFI_systems)
-   [[4] [A fallback alternative]](#A_fallback_alternative)

# [Introduction]

This is not to get back or to restore your Manjaro bootloader. To restore your Manjaro bootloader, see [this](https://wiki.manjaro.org/index.php?title=Restore_the_GRUB_Bootloader).

This is to prevent your working Manjaro bootloader being overridden by other OS bootloaders. This can happen when the other OS updates its grub (not update-grub). And due to Manjaro\'s implementation of intel-ucode, other OS bootloader cannot boot Manjaro OS, hence this tutorial.

# [Bios-legacy systems]

Boot up all other linux OS and at their terminals, do

[user \$ ][ sudo grub-install \--force /dev/sdxy [COPY TO CLIPBOARD]]

\

where /dev/sdxy is the other OS partition. Note some OS\'s need command \'grub2-install\'.

When installing a new linux OS, at their installer, always select \"installing bootloader to partition\". We can also choose not to install bootloader, but selecting \'to partition\' (Manjaro calls this \'to system\') is good enough and is preferable to have a bootloader installed at every OS.

If you choose to uninstall Manjaro later on, remember to make the other OS bootloader as default before uninstalling.

# [UEFI systems]

At any linux OS terminal, see output of

[user \$ ][ efibootmgr [COPY TO CLIPBOARD]]

\

It will give an output like this:

\

[\$] [efibootmgr]\

     BootCurrent: 0001
     Timeout: 1 seconds
     BootOrder: 0001,0002,0004,0005,0008
     Boot0001* manjaro
     Boot0002* ubuntu
     Boot0004* UEFI: WDC WD10PURX
     Boot0005* Hard Drive
     Boot0008* Systemd Boot Manager

\
Make sure Manjaro bootorder is at the beginning as above: \"BootOrder: 0001,0002,0004,0005,0008\" If it is not, reorder such that it is, like this:

[user \$ ][ sudo efibootmgr -o 0001,0002,0004,0005,0008 [COPY TO CLIPBOARD]]

\

Whenever we install another OS, it will be at the top of that bootorder; and we will need to reorder such that Manjaro is again at the top. And we can do that at that install livecd media itself. If we forget, we can do it after installation at any OS. For UEFI, we can still select Manjaro to boot at boot-setup (one of F8 \~ F12).

That alone should be sufficient for most UEFI systems. However in some situations (and reported in some topics here), it is not (possibly due to firmware issues). The above steps do not ensure that Manjaro bootorder will be booted up. In these cases, one extra command is required.

[user \$ ][ sudo cp /boot/grub/x86_64-efi/core.efi /boot/efi/EFI/boot/bootx64.efi [COPY TO CLIPBOARD]]

\

Or, if done at livecd (or another OS) and mounted / partition to /mnt and /boot/efi partition to /mnt/boot/efi

[user \$ ][ sudo cp /mnt/boot/grub/x86_64-efi/core.efi /mnt/boot/efi/EFI/boot/bootx64.efi [COPY TO CLIPBOARD]]

\

Copying /boot/efi/EFI/Manjaro/grubx64.efi instead of /boot/grub/x86_64-efi/core.efi can also accomplish the same thing because /boot/efi/EFI/Manjaro/grubx64.efi is itself a copy of /boot/grub/x86_64-efi/core.efi

So doing this is also an alternative.

[user \$ ][ sudo cp /boot/efi/EFI/Manjaro/grubx64.efi /boot/efi/EFI/boot/bootx64.efi [COPY TO CLIPBOARD]]

\

Doing this extra command where the extra command is not needed does not seem to harm the system.

# [A fallback alternative]

(Both bios-legacy and uefi)

We can despite our efforts, still use the other OS grub to boot Manjaro, and might come in useful, particularly if the above methods seems daunting. Or if we are stuck not being able to get to Manjaro bootloader.

At the other OS grub 2 system, create a custom.cfg file

[user \$ ][ sudo touch /boot/grub/custom.cfg [COPY TO CLIPBOARD]]

\

Some OS\'s like Suse, Fedora, Mageia uses directory in /boot/grub2 not /boot/grub, so do so accordingly. Then add the following in the newly created custom.cfg. No need to update-grub or change /etc/default/grub and will stand (persist) grub-installs or update-grubs. And of course persists to any new Manjaro kernel. Note this entry/entries will not be shown in their grub.cfg.

/boot/grub/custom.cfg

    menuentry "Manjaro - configfile "

btrfs will need additional tweaks (rootflag=subvolume=@)