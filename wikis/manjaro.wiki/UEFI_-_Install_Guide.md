Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide/de "UEFI - Installationsanleitung (8% translated)") • ‎[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide/tr "UEFI - Kurulum Kılavuzu (1% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide/fr "UEFI - Guide d'installation (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide/ru "UEFI - Руководство по установке (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide/fa "یو‌ئی‌اِف‌آی - راهنمای نصب (42% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide/zh-cn "UEFI - 安装指南 (60% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Target computer]](#Target_computer)
-   [[3] [The steps]](#The_steps)
    -   [[3.1] [Common]](#Common)
        -   [[3.1.1] [Graphical Installer]](#Graphical_Installer)
        -   [[3.1.2] [CLI installer]](#CLI_installer)
            -   [[3.1.2.1] [Disk preparation]](#Disk_preparation)
            -   [[3.1.2.2] [Setting filesystem mount points]](#Setting_filesystem_mount_points)
            -   [[3.1.2.3] [Installation]](#Installation)
-   [[4] [Switching from BIOS to UEFI]](#Switching_from_BIOS_to_UEFI)
-   [[5] [Dual booting with Windows]](#Dual_booting_with_Windows)
    -   [[5.1] [Instructions]](#Instructions)
        -   [[5.1.1] [Manual install]](#Manual_install)
        -   [[5.1.2] [An alternative: chainloading via GRUB]](#An_alternative:_chainloading_via_GRUB)
-   [[6] [Extras]](#Extras)
    -   [[6.1] [Using Rufus on Windows to create installation media]](#Using_Rufus_on_Windows_to_create_installation_media)
-   [[7] [Feedback]](#Feedback)
-   [[8] [External Links]](#External_Links)

# [Introduction]

    UEFI is the commonly agreed on name for both the EFI & UEFI
    standards which merged. It does not include the old EFI v1,
    or Apple's own non-standard version of EFI.

# [Target computer]

The following guide aims to install Manjaro on a machine with UEFI enabled, Secure boot disabled, and using GUID Partition Table (GPT) disk(s).

For multi-boot, the EFI system partition which is already present (or will be created), can usually be shared amongst multiple Linux installs.

# [The steps]

## [Common]

-   1\. Download your preferred Manjaro version: XFCE, Gnome, KDE, Budgie, Cinnamon, I3, Sway or Mate.

<!-- -->

-   2\. Burn the .iso to USB or DVD. See [Burn an ISO File](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Burn_an_ISO_File "Special:MyLanguage/Burn an ISO File") for more details.

<!-- -->

-   3\. Check your BIOS, UEFI must be ON and Secure boot OFF.

<!-- -->

-   4\. Boot with your USB or DVD & use the rEFInd - Main Menu\... to choose which GPU drivers you want to have installed, the open-source or proprietary:

<!-- -->

    * Boot with open source drivers -
      This chooses the open-source - free GPU drivers.
    * Boot with proprietary drivers -
      This option chooses the proprietary GPU drivers
      from Nvidia or ATI.

### [Graphical Installer]

**tip**

------------------------------------------------------------------------

Since Manjaro-0.8.9, UEFI support is also provided in the Graphical Installer, so one can simply try the Graphical installer and skip the instructions given below for the CLI installer.

To use the Graphical Installer select the **Install Manjaro** option from the Manjaro Welcome screen or from the desktop.

For the ESP (EFI system partition) which will store the EFI Grub binary, a 512mb partition of type fat32 can be created in the partitioning step, and mounted to */boot/efi*

If you are dual booting then an EFI partition from a previous install can also be used.

### [CLI installer]

-   5-b. Open terminal & enter:

[user \$ ][ sudo setup [COPY TO CLIPBOARD]]

\

-   6\. Now, we are in the CLI Installer.

<!-- -->

-   7\. *Choose 1.* Set date and time - an easy intuitive configuration.

#### [Disk preparation]

**tip**

------------------------------------------------------------------------

If your hard disk is already partitioned the way you want, then this step can be skipped.

    * When you click 2. Partition Hard Drives,
      you get a dialog saying "Do you want to use GUID
      Partition Table (GPT)", choose Yes.
    * Partition your disk(s) as you want (Instructions on
      manually partitioning are beyond the scope of this
      guide, some deatils are available here).
    * Important Step: Create a 50~250MB EFI Partition,
      mine is 100MB (code: ef00)

#### [Setting filesystem mount points]

    * After the partitioning is done, go to 4. Set Filesystem
      Mountpoints.
    * Important Step: Format the EFI Partition you
      created as VFAT and mount on /boot/efi

\

**note**

------------------------------------------------------------------------

If you are re-using your EFI partition (that was created by Windows previously (or any other OS), then there is no need to format. Formatting will wipe the previous bootloader. Only mounting the EFI partition as **/boot/efi** is required in that case.

#### [Installation]

-   9\. *Choose 3.* Install system and wait\...

<!-- -->

-   10\. Now, go to *4. Configure System* and configure it the way you like (username, password, mirrorlist, system-name, \...).

<!-- -->

-   11\. When you are done, go to *5. Install bootloader.* Choose EFI_x86_64 \> GRUB (2) UEFI x86_64, *DON\'T select BIOS GRUB.*

<!-- -->

-   11.1 It will ask to format the EFI Partition you created earlier as FAT32, yes can be chosen.

**note**

------------------------------------------------------------------------

Formatting not required if reusing previous EFI partition.

-   12\. If it gives a error in the final stages saying \"efivars kernel module was not properly loaded\", don\'t worry, the system will work fine!

<!-- -->

-   13\. If the installer asks you about copying grub/efi files to another folder in order to maintain compatibility in some systems, choose Yes.

<!-- -->

-   14\. *Click 6.* Quit

<!-- -->

-   15\. Shutdown, remove the DVD or USB, and boot. Your system should appear now!

# [Switching from BIOS to UEFI]

1\) You need to create an *ESP (EFI System Partition)*.

It is a FAT32 partition which has the .efi files for booting, which you can create using gparted or gdisk. (Size at least 200-300 MiB.) Ensure the flags \`boot\` and \`esp\` are set on this partition.

You should also install/check whether following packages are present:

    1. efibootmgr
    2. dosfstools
    3. grub

[(How to install packages)](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Pacman_Overview "Special:MyLanguage/Pacman Overview")

\
2) Create the */boot/efi* directory

[user \$ ][ sudo mkdir /boot/efi [COPY TO CLIPBOARD]]

\

\
3.) Mount the EFI partition as */boot/efi*

    sudo mount /dev/sdXY /boot/efi

X = Alphabet of the drive = a,b,c \... Y = Partition number of the EFI partition = 1,2,3,4\...

Example - */dev/sda4*

\
4.) Install Grub according to UEFI

[user \$ ][ sudo grub-install \--target=x86_64-efi \--efi-directory=/boot/efi \--bootloader-id=manjaro \--recheck [COPY TO CLIPBOARD]]

\

5.) Update Grub configuration file.

[user \$ ][ sudo update-grub [COPY TO CLIPBOARD]]

\

\

**note**

------------------------------------------------------------------------

If you get an error like:

    path '/boot/grub' is not readable by Grub on boot. Installation is impossible. Aborting

Then you will need to [chroot](https://wiki.archlinux.org/index.php/Change_Root) as described [here](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Restore_the_GRUB_Bootloader#Identify_and_Prepare_the_Installed_Partition.28s.29 "Special:MyLanguage/Restore the GRUB Bootloader"), and then perform Step 5 again.

\

**note**

------------------------------------------------------------------------

If you get the following error:

    EFI variables are not supported on this system.

then you could load the **efivarfs** module :

[user \$ ][ sudo modprobe efivarfs [COPY TO CLIPBOARD]]

\

**See also**

[Restore the GRUB Bootloader](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Restore_the_GRUB_Bootloader "Special:MyLanguage/Restore the GRUB Bootloader")

[Related Forum topic](https://forum.manjaro.org/t/using-livecd-v17-0-1-as-grub-to-boot-os-with-broken-bootloader/24916)

# [Dual booting with Windows]

**tip**

------------------------------------------------------------------------

Some manufactures EFI implementations cause GRUB not to be showed in the Boot Menu, or even if its there it can\'t be made default.

\
**In such cases *[rEFInd](http://www.rodsbooks.com/refind/index.html)*** can be used.

\
[![Refind.png](/images/4/4a/Refind.png)](//wiki.manjaro.org/index.php?title=File:Refind.png)

\
There are two ways to install rEFInd:

1.Install rEFInd from its [website](https://www.rodsbooks.com/refind/installing.html) (detailed) or **install using pacman***(preferred)*:

[user \$ ][ sudo pacman -S refind [COPY TO CLIPBOARD]]

\

Files will be present in /usr/share/refind .

2.Or using the instructions on the [rEFInd website](http://www.rodsbooks.com/refind/installing.html)

## [Instructions]

The **refind-install** command can be used to automatically install rEFInd (the EFI partition may need to be mounted for this to work). See the [Arch wiki](https://wiki.archlinux.org/index.php/REFInd#Installation) for more details.

### [Manual install]

Inside the refind folder (**/usr/share/refind**), copy the files and folders to `/boot/efi/EFI/Boot/`.

\

**note**

------------------------------------------------------------------------

My ESP (EFI System Partition) is mounted at **/boot/efi**.

You need to copy these files to the Boot folder on your EFI partition, and the Boot folder itself will be present inside the EFI folder on the EFI Partition, so take note of it.

You can check which partition is your ESP using Gparted; find which partition is formatted as fat32 and has size around 200MiB-1GiB.

Can mount it as /boot/efi by

[user \$ ][ sudo mount /dev/sdXN /boot/efi [COPY TO CLIPBOARD]]

\

X=a,b,c\... N=1,2,3\... These depend on which partition your ESP is present which can be obtained via Gparted as mentioned earlier.

Now inside the /boot/efi/EFI/Boot/ folder, there should already be a file present:

    bootx64.efi

You can ***rename*** it as *windows.bootx64.efi* Then you can rename *refind_x64.efi* to *bootx64.efi*

The bootx64.efi files boot by default, hence rEFInd should now boot by default, and detect grubx64.efi(linux-manjaro) and efibootmgfw.efi (windows) automatically.

\

**note**

------------------------------------------------------------------------

A folder Manjaro (name could be some other also) containing the file *grubx64.efi* should also be present in **/boot/efi/EFI/** folder, which should contain the *grubx64.efi* file which will be used by rEFInd to boot Grub.

So it could be like:

    /boot/efi/EFI/Manjaro/grubx64.efi

rEFInd would use this file for booting Manjaro.

If you do not have this file or folder, try:

[user \$ ][ sudo grub-install \--target=x86_64-efi \--efi-directory=/boot/efi \--bootloader-id=Manjaro \--recheck [COPY TO CLIPBOARD]]

\

to create **/boot/efi/EFI/Manjaro/grubx64.efi**

\
See also- [http://www.rodsbooks.com/refind/installing.html#naming](http://www.rodsbooks.com/refind/installing.html#naming)

### [An alternative: chainloading via GRUB]

An entry can be added to

/etc/grub.d/40_custom

    menuentry 'Windows8 (UEFI)' )/EFI/Microsoft/Boot/bootmgfw.efi
    boot
    }

In this case (hd0,4) or /dev/sda4 is the EFI System partition where the Windows bootloader is present.

After adding the above entry, running **sudo update-grub** updates the GRUB configuration file so that an entry named **Windows8 (UEFI)** is added to the GRUB boot menu.

[Related Forum topic](https://forum.manjaro.org/t/detecting-efi-files-and-booting-them-from-grub/38083)

The chainloading will fail on some hardware (Lenovo Ideapad 110) with the \"invalid signature\" message - the Refind method will still work.

# [Extras]

## [Using Rufus on Windows to create installation media]

[Rufus](http://rufus.akeo.ie/) users can use the following settings:

    * Click on the DVD icon and load your .iso
    * In the menu left of the DVD icon, select DD Image
    * Device: "choose your USB" (Attention: choose correctly,
      the device selected here will be formatted!!!)
    * Partition scheme: GPT partition scheme for UEFI computer
    * File system: FAT32
    * Cluster size: "Don't modify"
    * Volume label: "Don't modify"
    * Click Start, and you are done (takes 2~5 min to complete).

# [Feedback]

Questions, suggestions, critics? Please post [here](https://forum.manjaro.org/)

# [External Links]

Youtube video: [https://www.youtube.com/watch?v=36tDZIXn3-k](https://www.youtube.com/watch?v=36tDZIXn3-k)