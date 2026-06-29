**Resources**

[[]][Home](https://qingyun.huawei.com/desktops/qingyun-w515/)

[[]][Support Page](https://bsupport.huawei.com/cn/product/qingyun-w515/)

[[]][Specification](https://qingyun.huawei.com/desktops/qingyun-w515/specs/)

[[]][User Manual](https://consumer-tkbdownload.huawei.com/ctkbfm/servlet/download/downloadServlet/H4sIAAAAAAAAAD2QzUrDQBSFX0VmpZDKnZlMM-Oq-RuQgBasupTJTNIGalrSRLHiWhe2IAq-gm-g9Hna-BomJbj8uIdzP84jqhZJMXqYJ-gEYWQhM7vPO6QNptk0OVO3Le5W6-3Ppn5fbzdv1wyzg9-Pr_rlu3593q0-e4dDlY-rKys6v7gBZi0nPZ0fHc9N2pUMVTlpSlhstObGwTHHtkiJIk7KjGaglQCCSZOOs-WpaaKRO9i3YMY5xZQOMADYTUAXiSqzWT7KWi_cB2FTsKE9W2iRjXNVVkVr7EPoc-IHYciEK5nHPcdh4Mq-pIK4XshDEBKHpA-E0oBzW3AvkDLwpO0I3xPNrzs1zczl_0RlUSV7w26iyEVPfzi8gVpDAQAA.pdf)

HUAWEI QingYun W515 is a desktop computer featuring a [Kirin 990](https://www.hisilicon.com/en/products/kirin/kirin-flagship-chips/kirin-990) mobile phone SoC.

This product is not meant for the consumer market but government usage, which makes it niche and expensive to get (as brand new).

Despite in the form factor of a desktop computer, this device is designed more like an oversized SBC rather than an ARM SystemReady compliant desktop computer/server.

[Standard Build Unit](https://www.linuxfromscratch.org/~bdubbs/about.html) time: \~1 min 30 s (2.44-r4, `USE=nls plugins zstd`)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Prototypes]](#Prototypes)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Firmware]](#Firmware)
        -   [[3.1.1] [Boot Sequence]](#Boot_Sequence)
        -   [[3.1.2] [Optional: Upgrading the Bootloader]](#Optional:_Upgrading_the_Bootloader)
            -   [[3.1.2.1] [Upgrading the First Stage Bootloader]](#Upgrading_the_First_Stage_Bootloader)
            -   [[3.1.2.2] [Upgrading the Second Stage Bootloader (UEFI)]](#Upgrading_the_Second_Stage_Bootloader_.28UEFI.29)
    -   [[3.2] [Partitioning]](#Partitioning)
    -   [[3.3] [Kernel]](#Kernel)
        -   [[3.3.1] [Using Binary NeoKylin Kernel]](#Using_Binary_NeoKylin_Kernel)
        -   [[3.3.2] [Alternative: Configure and Compile NeoKylin Kernel from Source]](#Alternative:_Configure_and_Compile_NeoKylin_Kernel_from_Source)
            -   [[3.3.2.1] [Kernel Configuration]](#Kernel_Configuration)
    -   [[3.4] [Bootloader]](#Bootloader)
    -   [[3.5] [Emerge]](#Emerge)
        -   [[3.5.1] [GPU]](#GPU)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Vendor Specific Routines]](#Vendor_Specific_Routines)
        -   [[4.1.1] [WLAN]](#WLAN)
        -   [[4.1.2] [Bluetooth]](#Bluetooth)
    -   [[4.2] [Audio]](#Audio)

## [Hardware]

### [Standard]

  ------------------ ------------------------------------------------------------- ---------- -------------------------------- --------------------- ------------------ -------------------------------------------
  Device             Make/model                                                    Status     Vendor ID / Product ID           Kernel driver(s)      Kernel version     Notes
  CPU                HiSilicon Kirin 990                                           Works      \-                               \-                    4.19.71-46-kr990
  NAND               SKHynix HN8T15BZGKX016                                        Works      \-                               ufshcd                4.19.71-46-kr990
  SATA Controller    ASMedia Technology Inc. ASM1064 Serial ATA Controller         Works      1b21:1064:2116:2116 / 01-06-01   ahci                  4.19.71-46-kr990
  SSD                Dell-EMC/Micron MTFDDAK480TDS                                 Works      \-                               ahci,sd               4.19.71-46-kr990
  DVD-RW             LiteOn DU-8AESH                                               Works      \-                               ahci,sr               4.19.71-46-kr990
  USB Controller     Renesas Electronics Corp. uPD720202 USB 3.0 Host Controller   Works      1912:0015 / 0c-03-30             \-                    4.19.71-46-kr990
  Internal USB hub   Genesys Logic, Inc. Hub                                       Works      05e3:0610 / 09-00-00             \-                    4.19.71-46-kr990
  Internal USB hub   VIA Labs, Inc. VL820 Hub                                      Works      2109:0820 / 09-00-00             \-                    4.19.71-46-kr990
  LAN                Realtek RTL8153 Gigabit Ethernet Adapter                      Works      0bda:8153 / ff-ff-00             r8152_n               4.19.71-46-kr990   Onboard, but on USB Bus
  WLAN               HiSilicon Hi1103CPC                                           Works      ?                                plat_1105,wifi_1105   4.19.71-46-kr990
  Bluetooth          HiSilicon Hi1103CPC                                           Works      ?                                plat_1105             4.19.71-46-kr990
  Audio              HiSilicon Hi6405                                              Works      ?                                \-                    4.19.71-46-kr990
  GPU                Mali-G76                                                      Limited    ?                                \-                    4.19.71-46-kr990   Cannot get EGL & WayLand HW Accel working
  UEFI               Byosoft UEFI v1.00.71                                         Limited    \-                               \-                    4.19.71-46-kr990   Cannot properly register efivars
  ------------------ ------------------------------------------------------------- ---------- -------------------------------- --------------------- ------------------ -------------------------------------------

### [Accessories]

  ---------- -------------------------------------------- -------- ----------- ------------------ ------------------ ------------------------------------
  Device     Make/model                                   Status   Bus ID      Kernel driver(s)   Kernel version     Notes
  Keyboard   Holtek Semiconductor, Inc. Gaming Keyboard   Works    04d9:0024   usbhid             4.19.71-46-kr990   Random branded mechanical keyboard
  Keyboard   SayoDevice 2x6F RGB                          Works    8089:0008   usbhid             4.19.71-46-kr990   4x6 programmable keypad
  Mouse      Dell MS116 Optical Mouse                     Works    413c:301a   usbhid             4.19.71-46-kr990
  ---------- -------------------------------------------- -------- ----------- ------------------ ------------------ ------------------------------------

## [Prototypes]

There are prototype units being sold on second-hand markets. They could be identified by such identities:

-   The front bezel is golden (which is the same as a W510), rather than pure black
-   Sticker on the side with product name `XXXXXXXX`
-   BIOS and EC version \< 1.00

The hardware of prototype and retail units are mostly identical. Most of the content in this document also applies to prototypes (unless explicitly pointed out), but they could run into strange issues that retail units won\'t have.

## [Installation]

### [Firmware]

The UEFI environment vaguely follows UEFI 2.7 standard. DeviceTree is passed from the UEFI environment. ACPI is not used.

#### [Boot Sequence]

The boot sequence of this device is closer to an SBC rather than ARM SystemReady compliant desktop computers/servers.

1.  The first stage BootROM loads the payload from the UFS storage module, which is the UEFI environment as second stage bootloader.
    -   The detailed process is similar to an Android phone that cannot find the OS, then boots into Recovery mode which is actually the UEFI ?
2.  The second stage bootloader loads UEFI executables (GRUB etc.) as third stage bootloader
3.  The third stage bootloader loads Linux.

** Important**\
The second stage bootloader is prone to damage caused by improper disk operations, resulting in devices no longer able to boot, and very hard to recover considering there are literally no off-the-shelf devices that could read/write these UFS storage modules. Hence it\'s highly recommended to install Gentoo in extra SATA disks rather than replacing the OS in the UFS storage module.

-   Accessories (cable and mounting tray) for SATA disks are optional and may not come with each device. In this case:
    -   If there is a DVD-ROM, it could be replaced with a laptop optical drive to 2.5 inch SATA disk tray converter.
    -   If there isn\'t a DVD-ROM, a mini 8-pin to SATA power cable and a disk mounting tray is required. This could be acquired either from HUAWEI customer support or third party.

** Tip**\
Technically speaking, the second stage bootloader could be trimmed out and boots Linux directly from first stage bootloader, similar to how [postmarketOS](https://postmarketos.org/) boots. This is very risky and should only be taken out by expert users.

#### [Optional: Upgrading the Bootloader]

** Warning**\
Do not upgrade the bootloader of a prototype. This could result in device no longer able to boot.

** Important**\
Do not upgrade the firmware if the device is still required to run a certain version of NeoKylin/Uniontech UOS, which is a common requirement in governments due to licensing issues, etc., as doing so would easily break their compatibility and cause them to no longer be able to boot.

** Important**\
Upgrading the bootloader should be done under NeoKylin or Uniontech UOS. The upgrade package/script may work under other distros if all userland dependencies are met, but only those two distros are officially tested.

\
Upgrading the Bootloader, both first stage and second stage (officially referenced as [HiSilicon Firmware] and [BIOS]) may improve the stability of the device.

** Note**\
[KVM](https://linux-kvm.org/page/Main_Page) features may have issues with first stage bootloader version lower or equal than [2.1.203.27] .

Upgrade files could be downloaded from [Support Page](https://bsupport.huawei.com/cn/product/qingyun-w515/).

##### [Upgrading the First Stage Bootloader]

A command in NeoKylin/Uniontech UOS could be used to check the current first stage bootloader version:

`user `[`$`]`hwfirmware -v`

     current hisi Version: 2.1.203.51

** Warning**\
Do not rollback the firmware below version [2.1.202.13] if the device comes with 16GB of RAM. This would result in device no longer able to boot.

If the first stage version of the firmware is below [2.1.203.27], upgrade to this version first. Otherwise, the newer firmware version may not install due to changed validation algorithms.

Upgrade files are installed the same way as a Debian binary package file. On NeoKylin or Uniontech UOS, this could be done by just double-clicking on the file. On other Linux distros this could be done by command:

`root `[`#`]`apt install path/to/package.deb`

After the installation of the package, a popup will show up on the bottom right of the desktop. Click the blue start button and the device will reboot and start upgrading.

** Important**\
Do not disconnect or shut off the monitor, as the popup indicated. Despite doing so may not cause actual trouble, better safe than sorry.

-   NeoKylin/Uniontech UOS may not be able to boot after a first stage bootloader upgrade; This is an expected behavior as each version of NeoKylin and Uniontech UOS is specifically adapted to each version of first stage bootloader. A reinstall of these OS with the corresponding version is required.

##### [][Upgrading the Second Stage Bootloader (UEFI)]

Upgrade files are executable files. Run the following command to install:

`root `[`#`]`chmod 777 path/to/executable.sh && path/to/executable.sh 1`

Upgrade applies once the script has successfully finished.

### [Partitioning]

This unit doesn\'t need a \"hard disk\" by common means to function. Instead, it has a 256/512GB UFS protocol NAND storage module underneath the CPU fan, which functions both as firmware and storage device.

** Warning**\
Partitioning the UFS storage module should be taken with extra care. Improper partitioning/reformatting could damage the first/second stage bootloader and cause the device no longer able to boot.

The UFS storage module is emulated into 3 logical devices:

`root `[`#`]`fdisk -l`

    Disk /dev/sda: 4 MiB, 4194304 bytes, 1024 sectors
    Disk model: HN8T15BZGKX016
    Units: sectors of 1 * 4096 = 4096 bytes
    Sector size (logical/physical): 4096 bytes / 4096 bytes
    I/O size (minimum/optimal): 524288 bytes / 524288 bytes

    Disk /dev/sdb: 4 MiB, 4194304 bytes, 1024 sectors
    Disk model: HN8T15BZGKX016
    Units: sectors of 1 * 4096 = 4096 bytes
    Sector size (logical/physical): 4096 bytes / 4096 bytes
    I/O size (minimum/optimal): 524288 bytes / 524288 bytes

    GPT PMBR size mismatch (327680 != 327679) will be corrected by write.
    Disk /dev/sdc: 1.26 GiB, 1342177280 bytes, 327680 sectors
    Disk model: HN8T15BZGKX016
    Units: sectors of 1 * 4096 = 4096 bytes
    Sector size (logical/physical): 4096 bytes / 4096 bytes
    I/O size (minimum/optimal): 524288 bytes / 524288 bytes
    Disklabel type: gpt
    Disk identifier: F9F221FF-A8D4-5F0E-9746-594869AEC34E

    Device      Start    End Sectors  Size Type
    /dev/sdc1     128    255     128  512K Linux filesystem
    /dev/sdc2     256    383     128  512K Linux filesystem
    (...)
    /dev/sdc32 271360 271871     512    2M Linux filesystem

    Disk /dev/sdd: 237.1 GiB, 254577475584 bytes, 62152704 sectors
    Disk model: HN8T15BZGKX016
    Units: sectors of 1 * 4096 = 4096 bytes
    Sector size (logical/physical): 4096 bytes / 4096 bytes
    I/O size (minimum/optimal): 524288 bytes / 524288 bytes
    Disklabel type: gpt
    Disk identifier: 1B7CF424-F98E-4EFB-A37A-0CE833407518

-   `/dev/sda` and `/dev/sdb` are the first stage bootloader that **should not be modified in any ways.**
-   `/dev/sdc` is the second stage bootloader that **should not be modified in any ways.**
-   `/dev/sdd` is the safe part to modify. The OS should be installed here.

Procedures of partitioning SATA disks are trivial.

### [Kernel]

This device seems cannot boot mainline Linux kernel. The kernel of NeoKylin is used here as an alternative.

Till the last edit of this article, NeoKylin only provides kernel 4.19 for this device and it seems to be based on the kernel for Android.

** Important**\
If it\'s a prototype, always use the kernel bundled in the OS preinstalled rather than acquiring a new one, and back it up to a safe place; it could be the only one that would boot.

#### [Using Binary NeoKylin Kernel]

A NeoKylin binary kernel could be acquired from either the LiveCD or full installation of NeoKylin.

Assuming Gentoo rootfs has been mounted to `/mnt/gentoo`.

Copying the kernel and modules from NeoKylin to Gentoo:

`root `[`#`]`cp /boot/vmlinuz-4.19.71-46-kr990 /mnt/gentoo/boot/vmlinuz-4.19.71-46-kr990`

`root `[`#`]`cp -r /lib/modules/4.19.71-46-kr990 /mnt/gentoo/lib/modules/4.19.71-46-kr990`

Then reference to [Handbook:AMD64/Installation/Base#Chrooting](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Chrooting "Handbook:AMD64/Installation/Base") to chroot into the Gentoo rootfs.

Regenerate initramfs:

** Note**\
The following command use [dracut] and [grub] for example. If preferring other ways of generating initramfs and/or bootloaders, check out the corresponding articles.

`root `[`#`]`dracut --kver 4.19.71-46-kr990 && grub-mkconfig -o /boot/grub/grub.cfg`

#### [Alternative: Configure and Compile NeoKylin Kernel from Source]

NeoKylin kernel source code could either be acquired from [apt] in a full installation of NeoKylin, or downloaded directly from NeoKylin apt repository.

To get the kernel source code in NeoKylin:

`root `[`#`]`apt install linux-source`

** Note**\
An `apt search linux-source` may reveal more version options but currently only 4.19.71 is the valid option and will be brought in by installing `linux-source` package. Other versions are either missing HiSilicon platform-specific options & drivers, or just dummy packages that install nothing but an empty folder.

Assuming the Gentoo rootfs has been mounted, extracting the tarball into the corresponding location:

`root `[`#`]`tar -xf /usr/src/linux-source-4.19.71.tar.bz2 -C /mnt/gentoo/usr/src --verbose`

Copying the default configuration file into the corresponding location. This file is the one being used to compile the kernel in NeoKylin:

`root `[`#`]`cp /boot/config-4.19.71-46-kr990 /mnt/gentoo/usr/src/linux-source-4.19.71/.config`

Reference to [Handbook:AMD64/Installation/Base#Chrooting](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Chrooting "Handbook:AMD64/Installation/Base") to chroot into the Gentoo rootfs.

Compiling the kernel requires GCC 9.5.0. On ARM64, this package has to be unmasked first:

[FILE] **`/etc/portage/package.unmask`Unmasking GCC 9.5.0**

    =sys-devel/gcc-9.5.0

Then emerging GCC 9.5.0:

`root `[`#`]`emerge --ask sys-devel/gcc:9.5.0`

Enabling GCC 9.5.0:

`root `[`#`]`eselect gcc set aarch64-unknown-linux-gnu-9.5.0`

** Note**\
Do not forget to switch GCC version back after compiling the kernel so compilation of other packages won\'t be interfered. For more information about switching between GCC version, reference to [Eselect#Gcc](https://wiki.gentoo.org/wiki/Eselect#Gcc "Eselect").

** Tip**\
The kernel doesn\'t have to be compiled with [LLVM/Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") as menuconfig/nconfig indicated.

Finally, reference to [Handbook:AMD64/Installation/Kernel](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel "Handbook:AMD64/Installation/Kernel") to compile and install the kernel.

##### [Kernel Configuration]

Most of the configurations required are already set in the default configuration, besides some debloating.

[KERNEL] **Disable NeoKylin Specific Security Mechanisms**

    Security options  --->
        [ ] Kylin security enhanced plug-ins
        [ ] Enable Box protect
        [ ] uos elfverify support

    Kernel Features  --->
        [ ] No protection for Meltdown and Spectre

Make sure all the framebuffer supports are disabled except `Simple framebuffer support` has been enabled (including `EFI-based Framebuffer Support`), otherwise the system will boot without any display:

[KERNEL] **Framebuffer Supports**

    Device Drivers  --->
        Graphics support  --->
            Frame buffer Devices  --->
                [*] Simple framebuffer support

** Note**\
Not recommended to enable more platform-specific features than actually needed, which are basically fully covered by the initial configuration. Many of them aren\'t (properly) implemented and could cause compilation errors or other issues that are hard to diagnose.

### [Bootloader]

Due to UEFI environment oddities, [GRUB] may have trouble installing :

`root `[`#`]`grub-install --efi-directory=/boot/efi`

    Installing for arm64-efi platform.
    Could not prepare Boot variable: Invalid argument
    grub-install: error: efibootmgr failed to register the boot entry: Input/output error.

This is due to [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") unable to write boot entries. Adding `--no-nvram` would solve the issue:

`root `[`#`]`grub-install --efi-directory=/boot/efi --no-nvram`

** Tip**\
No need to worry if [efibootmgr] shows lots of invalid boot entries after trying to install [GRUB] for many times. Those are dummy entries and will be cleared after a reboot.

As the UEFI is so shabby that it doesn\'t support multiple hard disk boot entries, even multiple boot entries in the same hard disk, users that would like to boot from both the UFS storage module and SATA disks would have to :

-   Put [GRUB] in the EFI partition of the UFS storage module and adding the Gentoo Linux boot entry to it.
-   Put [GRUB] in the EFI partition of the UFS storage module and adding another [GRUB] executable in the EFI partition in the SATA disk to chainload it, which would then boot Gentoo.
-   Boot from another boot manager in the CD-ROM or USB drive then either loads Gentoo in the SATA disk directly, or chainloads the [GRUB] in the SATA disk which would then boot Gentoo.

** Note**\
Obviously the UFS storage module couldn\'t be removed to make space for an EFI boot entry, as the system won\'t even have UEFI environment to begin with.

### [Emerge]

#### [GPU]

** Warning**\
Do not replace the \"discrete GPU\", which is just a signal breakout board for the integrated GPU with other GPU or PCIE devices. This could result in hardware damage.

As the 4.19 kernel doesn\'t support Panfrost DRI, the graphics can only work in software rendering mode.

[VIDEO_CARDS] extended use flag does not need to be set. The procedures of setting up X11-based window managers/desktop environments are trivial. Wayland-based window managers/desktop environments cannot function properly.

** Important**\
It\'s possible to enable hardware acceleration by using closed-source userland drivers: bringing libmali.so.\* in and replacing Mesa related libraries with the ones from NeoKylin/Uniontech UOS, but as the driver being old and missing features (`gbm_bo_get_fd_for_plane`, `gbm_bo_map`, and possibly more), compilation of many window managers/desktop environments including [KDE](https://wiki.gentoo.org/wiki/KDE "KDE"), [Niri](https://wiki.gentoo.org/wiki/Niri "Niri"), and [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") will fail.

## [Configuration]

### [Vendor Specific Routines]

Some components require vendor-specific binaries and scripts to function. A full installation of NeoKylin could provide these components.

Assuming the Gentoo rootfs has been mounted to `/mnt/gentoo`, execute the following command to copy them into place:

`root `[`#`]`cp -r /vendor /mnt/gentoo`

** Tip**\
Users familiar with Android partition scheme may consider the `/vendor` is in a partition/image file and try to find how it\'s mounted - it\'s just a plain directory in this case.

#### [WLAN]

Execute the initialization script `1103start.sh` for the wireless adapter to start functioning. This script will load the corresponding kernel modules.

`root `[`#`]`/vendor/1103start.sh`

** Tip**\
This could be set as a [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")/[OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") service to automatically execute on boot. A reference setup could be found as `110x.service` in NeoKylin.

Mainline version of [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") and [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") have trouble with this wireless adapter that would cause themselves and programs relying on them getting stuck for minutes, if not indefinitely until forcefully stopped after changing/disconnecting from APs. Problem seems resides in power management.

Instead, use [iwd](https://wiki.gentoo.org/wiki/Iwd "Iwd") in standalone mode.

[dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd") might have to be introduced to provide DHCP for the WLAN adapter:

`root `[`#`]`emerge --ask net-misc/dhcpcd`

Then setting up the correspond USE flags:

[FILE] **`/etc/portage/package.use/iwd`**

    net-wireless/iwd standalone

[FILE] **`/etc/portage/package.use/networkmanager`**

    net-misc/networkmanager -wifi -wext dhcpcd

Reinstall these packages:

`root `[`#`]`emerge -atv --deep --newuse net-misc/networkmanager net-wireless/iwd`

Reconfiguring services:

** Note**\
This part uses systemd configuration as example.

`root `[`#`]`systemctl daemon-reload && systemctl restart NetworkManager && systemctl enable --now iwd`

Then use [iwd] to manage wireless connections.

** Tip**\
[[[net-wireless/iwgtk]](https://packages.gentoo.org/packages/net-wireless/iwgtk)[]] could be a handy tool for graphical interfaces.

#### [Bluetooth]

Bluetooth is also provided by HiSilicon Hi1103CPC and has to be initialized using `1103start.sh` first.

After kernel modules are loaded by `1103start.sh`, it has to be further initialized by a customized version of [hciattach]. This could be acquired from a full installation of NeoKylin/Uniontech UOS:

`user `[`$`]`cp /usr/bin/hciattach /mnt/gentoo/vendor/hciattach`

Then initialize the bluetooth adapter:

`root `[`#`]`/vendor/hciattach -n /dev/hwbt hisi`

Finally, reference to [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") to set up userland tools.

** Tip**\
This could be set as a systemd/OpenRC service to automatically execute on boot. A reference setup could be found as `hciattach.service` in NeoKylin.

** Note**\
Mainline version of [hciattach], which could be acquired by installing [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]] with `deprecated` USE flag, doesn\'t know how to properly operate this Bluetooth adapter.

### [Audio]

** Important**\
The author doesn\'t fully understand the principles behind; it may become a \"works on my machine\" suggestion that has to be carefully treated with.

PulseAudio has to have `daemon` use flag enabled:

[FILE] **`/etc/portage/package.use/pulseaudio`**

    media-sound/pulseaudio daemon

(Re)installing PulseAudio:

`root `[`#`]`emerge --ask media-sound/pulseaudio`

Then copy these files from NeoKylin to Gentoo:

`root `[`#`]`cd /etc/pulse && cp -f client.conf daemon.conf default.pa pow-exponent.ini system.pa /mnt/gentoo/etc/pulse`

Finally, enabling the PulseAudio service reference to [PulseAudio#Running](https://wiki.gentoo.org/wiki/PulseAudio#Running "PulseAudio").

** Important**\
The Hi6405 seems doesn\'t like to work with [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire"). Using it could cause severe sound crackling/glitching on all outputs, even after referenced to [PipeWire#Crackling_and_stuttering](https://wiki.gentoo.org/wiki/PipeWire#Crackling_and_stuttering "PipeWire").