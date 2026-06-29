[![](/images/thumb/7/7f/Gentoo_running_in_a_BQ_Aquaris_X_Pro.jpg/300px-Gentoo_running_in_a_BQ_Aquaris_X_Pro.jpg)](https://wiki.gentoo.org/wiki/File:Gentoo_running_in_a_BQ_Aquaris_X_Pro.jpg)

[](https://wiki.gentoo.org/wiki/File:Gentoo_running_in_a_BQ_Aquaris_X_Pro.jpg "Enlarge")

Gentoo running in a BQ Aquaris X Pro (Bardockpro)

BQ Aquaris X Pro (bardockpro) is a 2017 mid-range device by Spanish manufacturer BQ. it has a glass back. It differs from the non-pro version in the camera, so instructions are pretty much the same for both devices.

## Contents

-   [[1] [Previous setup]](#Previous_setup)
-   [[2] [Installing Bootloader]](#Installing_Bootloader)
    -   [[2.1] [Build LK2ND]](#Build_LK2ND)
    -   [[2.2] [Flash]](#Flash)
        -   [[2.2.1] [Backup the entire phone (Optional, but very recommended)]](#Backup_the_entire_phone_.28Optional.2C_but_very_recommended.29)
        -   [[2.2.2] [Flash the bootloader]](#Flash_the_bootloader)
-   [[3] [Partitioning]](#Partitioning)
-   [[4] [Notes on installing Gentoo]](#Notes_on_installing_Gentoo)
    -   [[4.1] [Modify FEATURES to disable some sandboxing capabilities which break qemu]](#Modify_FEATURES_to_disable_some_sandboxing_capabilities_which_break_qemu)
    -   [[4.2] [Additional advice while following the handbook]](#Additional_advice_while_following_the_handbook)
-   [[5] [Configuring bootloader]](#Configuring_bootloader)
-   [[6] [Compiling the kernel]](#Compiling_the_kernel)
-   [[7] [Install firmware]](#Install_firmware)
-   [[8] [Compiling various services needed for the modem to work]](#Compiling_various_services_needed_for_the_modem_to_work)
    -   [[8.1] [qrtr]](#qrtr)
        -   [[8.1.1] [Install the repository]](#Install_the_repository)
    -   [[8.2] [Alsa]](#Alsa)
    -   [[8.3] [Q6voiced]](#Q6voiced)
        -   [[8.3.1] [Installing]](#Installing)
        -   [[8.3.2] [For Systemd]](#For_Systemd)
        -   [[8.3.3] [For Openrc]](#For_Openrc)
    -   [[8.4] [tqftpserv]](#tqftpserv)
        -   [[8.4.1] [Install the project]](#Install_the_project)
        -   [[8.4.2] [Enable the service in Systemd]](#Enable_the_service_in_Systemd)
        -   [[8.4.3] [Create, and enable the service in Openrc]](#Create.2C_and_enable_the_service_in_Openrc)
    -   [[8.5] [rmtfs]](#rmtfs)
        -   [[8.5.1] [Install the project]](#Install_the_project_2)
        -   [[8.5.2] [Create the Systemd service]](#Create_the_Systemd_service)
        -   [[8.5.3] [Create the Openrc service]](#Create_the_Openrc_service)
    -   [[8.6] [Udev rules]](#Udev_rules)
    -   [[8.7] [Quirks]](#Quirks)
-   [[9] [Install a mobile environment]](#Install_a_mobile_environment)
-   [[10] [Running dracut]](#Running_dracut)
-   [[11] [Copying the kernel, and initramfs to the correct location]](#Copying_the_kernel.2C_and_initramfs_to_the_correct_location)
-   [[12] [Flashing the image]](#Flashing_the_image)
-   [[13] [End of installation]](#End_of_installation)
-   [[14] [Rsync updating the phone]](#Rsync_updating_the_phone)
-   [[15] [Missing pieces]](#Missing_pieces)
-   [[16] [Troubleshooting]](#Troubleshooting)
    -   [[16.1] [The phone\'s touchscreen becomes unresponsive after suspend]](#The_phone.27s_touchscreen_becomes_unresponsive_after_suspend)
    -   [[16.2] [Modem disconnects randomly]](#Modem_disconnects_randomly)
    -   [[16.3] [Suspend messes up modem, touch and other things]](#Suspend_messes_up_modem.2C_touch_and_other_things)
    -   [[16.4] [There are too few key shortcut options in the terminal in Phosh for the user\'s needs]](#There_are_too_few_key_shortcut_options_in_the_terminal_in_Phosh_for_the_user.27s_needs)

## [Previous setup]

The following tools should be installed, and configured in the computer which is going to be used to install Gentoo in the device:

-   [Edl from bkerler](https://github.com/bkerler/edl) This tool is needed to extract firmware partitions.
-   [Android SDK](https://developer.android.com/studio) Download from the link a file that looks like commandlinetools-linux-13114758_latest.zip, uncompress in a directory like \$HOME/Android/Sdk.
-   Platform tools installed with Android SDK Manager.
-   Crossdev arm-none-eabi environment.
-   Crossdev aarch64-pc-linux-gnu environment.
-   Qemu with aarch64, and static-user support.

Additionally the following physical hardware is needed:

-   A BQ Aquaris X Pro
-   A usb-c cable fresh enough to carry data. (Worn out cables may not be able to carry data in a consistent way)
-   A Linux computer with root access, and a modern enough Kernel.

Add the following to the user\'s .bashrc.

[FILE] **`$HOME/.bashrc`Android Sdk Config**

    export ANDROID_SDK_ROOT="$HOME/Android/Sdk"

** Warning**\
Remove any Google account, pin code, pattern, fingerprint authentication or password before following this guide, ensure to connect to mobile data at least once with the sim card that is going to be used in Android and that 4g, 3g, 2g mode is chosen in Android if that\'s not done mobile data may not work, and unlock the phone\'s bootloader. Restoring the original Android may be more difficult in the future if this is not done.

## [Installing Bootloader]

### [Build LK2ND]

`user `[`$`]` git clone https://github.com/bq-msm8953-mainline/lk2nd $HOME/bq-lk2nd `

`user `[`$`]` cd $HOME/bq-lk2nd `

`user `[`$`]` make TOOLCHAIN_PREFIX=arm-none-eabi- lk2nd-msm8953 `

### [Flash]

Unplug from power cable the device, and shut it completely down pressing [Power] until the screen completely turns off (It is not possible to shut it down while it is receiving power, it would reboot)

Plug the usb-c cable data to the computer, and press [Volume Up]+[Volume Down] (Do not press [Power]) in the BQ Aquaris X Pro while doing this plug the cable to the phone.

** Note**\
The phone is now in an special recovery mode that allows to do any backup needed. Please consider reading the documentation in [EDL source code, it is possible to exit EDL at any moment pressing [Power] while plugging and unplugging the power cable in most devices including this one](https://github.com/bkerler/edl).

#### [][Backup the entire phone (Optional, but very recommended)]

** Warning**\
It is recomended to remove any google account or security passcode or pattern before doing this to have the ability in the future to restore the image.

`user `[`$`]`edl rl bq-backup`

#### [Flash the bootloader]

`user `[`$`]` edl w boot $HOME/bq-lk2nd/build-lk2nd-msm8953/lk2nd.img`

## [Partitioning]

The partition touched are the following:

-   boot (LK2ND Bootloader)
-   system (/boot)
-   userdata (/)

The bootloader is already handled so now it is time to focus on /boot, and /.

Retrieve a copy of both partitions.

** Note**\
This is slow go grab a coffee.

`user `[`$`]`edl r userdata bq-userdata.img && edl r system bq-system.img`

These .img files are going to be used as the base images for partitioning so do not rely on them as backups since this process will remove their contents.

`root `[`#`]`mkfs.ext2 bq-system.img`

`root `[`#`]`mkfs.ext4 bq-userdata.img`

Now mount these images like this, and follow the normal procedure to install gentoo.

`root `[`#`]`mount bq-userdata.img /mnt/gentoo`

`root `[`#`]`mkdir /mnt/gentoo/boot`

`root `[`#`]`mount bq-system.img /mnt/gentoo/boot`

## [Notes on installing Gentoo]

Once uncompressed the correct tarball (An appropriate aarch64 one), and before chrooting, do the following:

** Note**\
Start the chroot as explained here: [Embedded_Handbook/General/Compiling_with_QEMU_user_chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_QEMU_user_chroot "Embedded Handbook/General/Compiling with QEMU user chroot") --- how to use [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") to chroot into a system that targets a different architecture (e.g. **[aarch64]**) than the one being used (e.g. **[amd64]**)..

### [Modify FEATURES to disable some sandboxing capabilities which break qemu]

[FILE] **`/mnt/gentoo/etc/portage/make.conf`**

    FEATURES="-pid-sandbox -network-sandbox"

Now the system is actually ready to follow the steps needed to enter in the chroot environment (Follow [Handbook:AMD64](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") --- A handbook dedicated to installing and configuring Gentoo on the **[amd64]** architecture., an effort to centralize documentation into a coherent handbook.)

### [Additional advice while following the handbook]

Ignore everything related to partitioning, bootloader, firmware or kernel in the handbook since it is going to be device specific.

** Note**\
The correct value for VIDEO_CARDS in the make.conf is freedreno.

To look up the correct uuids for /etc/fstab use this commands.

`root `[`#`]`blkid bq-system.img # /boot`

`root `[`#`]`blkid bq-userdata.img # /`

Use noauto as option for /boot in fstab since it takes a lot to mount, and it can slow down the system\'s boot, also ext2 partitions can easily become corrupt if not correctly unmounted so the less time it is mounted the better.

** Warning**\
Ext2 support is about to be dropped in the kernel, and lk2nd only supports as an alternative to craft a special kernel image + initramfs + cmdline no documentation online could be found to create

Flashing the system each time a minor configuration error is made, and the system is not usable it is very slow so during the installation ensure to create a user, enable sshd, add a password to the user, append the ssh id to the users authorized_keys, and give it access to root to that user. (Check everything possible to work)

Ensure to transfer the wifi password to a file in the system for easy first time wifi setup since typing it in a touchscreen is not pleasant.

## [Configuring bootloader]

Inside the chroot:

`root `[`#`]`mkdir /boot/extlinux`

[FILE] **`/boot/extlinux/extlinux.conf`**

    default Gentoo

    label Gentoo
        linux /vmlinuz
        fdt /msm8953-bq-bardockpro.dtb
        initrd /initrd
        append root=UUID=<The bq-userdata.img uuid without any quotes>

## [Compiling the kernel]

This should be done outside of the chroot:

`user `[`$`]`git clone https://github.com/bq-msm8953-mainline/linux msm8953-linux`

`user `[`$`]`cd msm8953-linux`

Download the Postmarketos Kernel sources for this soc.

`user `[`$`]`curl -o .config -L https://gitlab.postmarketos.org/postmarketOS/pmaports/-/raw/master/device/community/linux-postmarketos-qcom-msm8953/config-postmarketos-qcom-msm8953.aarch64?ref_type=heads&inline=false`

Run olddefconfig:

`user `[`$`]`ARCH=arm64 CROSS_COMPILE=aarch64-pc-linux-gnu- make -j$(nproc) olddefconfig`

Join it with the bq config:

`user `[`$`]`ARCH=arm64 CROSS_COMPILE=aarch64-pc-linux-gnu- make -j$(nproc) olddefconfig bq-common.config`

Create a script for fast compiling:

[FILE] **`install_kernel.sh`**

    ARCH=arm64 CROSS_COMPILE=aarch64-pc-linux-gnu- INSTALL_MOD_PATH=/mnt/gentoo INSTALL_PATH=/mnt/gentooboot make -j$(nproc)
    sudo ARCH=arm64 CROSS_COMPILE=aarch64-pc-linux-gnu- INSTALL_MOD_PATH=/mnt/gentoo INSTALL_PATH=/mnt/gentoo/boot make install -j$(nproc)
    sudo ARCH=arm64 CROSS_COMPILE=aarch64-pc-linux-gnu- INSTALL_MOD_PATH=/mnt/gentoo INSTALL_PATH=/mnt/gentoo/boot make modules_install -j$(nproc)
    sudo cp -v $HOME/msm8953-linux/arch/arm64/boot/dts/qcom/msm8953-bq-bardockpro.dtb /mnt/gentoo/boot/

** Warning**\
The dtb is different for the non-pro version

Start compiling:

`user `[`$`]`bash install_kernel.sh`

This will install the kernel in the mounted partitions.

## [Install firmware]

** Note**\
dmesg is a great source of information to find what firmware is missing in the phone\'s Gentoo

Anything related to venus currently causes the phone to kernel panic, so avoid it.

These instructions are being written from experience installing in the device but not while installing it so it will point in general lines what firmwares will the device need, and where to get it but it may not be enough precise yet.

These are the links related to firmware by priority.

-   [msm-firmware-loader may be a handy read while finding what firmware the device needs, but it cannot use it directly since it would bring venus files from its partitions, and become the phone\'s Gentoo unbootable](https://gitlab.postmarketos.org/postmarketOS/msm-firmware-loader/-/blob/master/msm-firmware-loader.sh)

It is possible to retrieve the original firmware that msm-firmware-loader would seek mounting the backups done already with EDL, it is also possible to do the backup now of those partitions, for example:

`root `[`#`]`edl r modem modem.img`

`root `[`#`]`mkdir /mnt/modem`

`root `[`#`]`mount modem.img /mnt/modem`

-   [This repository contains some firmware that may be handy, and cannot be found in the partitions like a\\d\_zap.\*](https://github.com/bq-msm8953-mainline/firmware-bq-bardockpro)
-   [In the official linux-firmware repository missing firmware files can be found](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/qcom)

Some firmware may be signed, and not be transferable from other phones with the same soc that do not share model to bardockpro.

While copying a .mbn file always create a symlink from the same file name but with the extension .mdt.

This is what a working but not cleaned up device looks like: (It can be seen that it has venus firmwares they are not in a location where the kernel finds it, they are not needed like many things in this setup)

While installing please contribute to this wiki page firmware findings.

[FILE] **`/lib/firmware`**

    /lib/firmware/
    /lib/firmware/a225_pm4.fw
    /lib/firmware/modem.b06
    /lib/firmware/a420_pfp.fw
    /lib/firmware/qcom
    /lib/firmware/qcom/a225_pm4.fw
    /lib/firmware/qcom/a420_pfp.fw
    /lib/firmware/qcom/a530_pm4.fw
    /lib/firmware/qcom/qrb4210
    /lib/firmware/qcom/qrb4210/modemuw.jsn
    /lib/firmware/qcom/qrb4210/adspr.jsn
    /lib/firmware/qcom/qrb4210/a610_zap.mbn
    /lib/firmware/qcom/qrb4210/adspua.jsn
    /lib/firmware/qcom/qrb4210/cdspr.jsn
    /lib/firmware/qcom/qrb4210/adsp.mbn
    /lib/firmware/qcom/qrb4210/adsps.jsn
    /lib/firmware/qcom/qrb4210/cdsp.mbn
    /lib/firmware/qcom/qrb4210/modem.mbn
    /lib/firmware/qcom/qrb4210/modemr.jsn
    /lib/firmware/qcom/venus-5.2
    /lib/firmware/qcom/venus-5.2/venus.mdt
    /lib/firmware/qcom/venus-5.2/venus.b01
    /lib/firmware/qcom/venus-5.2/venus.b00
    /lib/firmware/qcom/venus-5.2/venus.b02
    /lib/firmware/qcom/venus-5.2/venus.b04
    /lib/firmware/qcom/venus-5.2/venus.mbn
    /lib/firmware/qcom/venus-5.2/venus.b03
    /lib/firmware/qcom/sa8775p
    /lib/firmware/qcom/sa8775p/qupv3fw.elf
    /lib/firmware/qcom/sa8775p/adspr.jsn
    /lib/firmware/qcom/sa8775p/adspua.jsn
    /lib/firmware/qcom/sa8775p/cdsp0.mbn
    /lib/firmware/qcom/sa8775p/cdsp1.mbn
    /lib/firmware/qcom/sa8775p/gpdsp1.mbn
    /lib/firmware/qcom/sa8775p/cdspr.jsn
    /lib/firmware/qcom/sa8775p/adsp.mbn
    /lib/firmware/qcom/sa8775p/gpdsp1r.jsn
    /lib/firmware/qcom/sa8775p/gpdspr.jsn
    /lib/firmware/qcom/sa8775p/a663_zap.mbn
    /lib/firmware/qcom/sa8775p/gpdsp0.mbn
    /lib/firmware/qcom/a623_gmu.bin
    /lib/firmware/qcom/qdu100
    /lib/firmware/qcom/qdu100/xbl_s.melf
    /lib/firmware/qcom/gen70500_sqe.fw
    /lib/firmware/qcom/sm8550
    /lib/firmware/qcom/sm8550/SM8550-QRD-tplg.bin
    /lib/firmware/qcom/sm8550/SM8550-HDK-tplg.bin
    /lib/firmware/qcom/a702_sqe.fw
    /lib/firmware/qcom/a330_pfp.fw
    /lib/firmware/qcom/gen71500_sqe.fw
    /lib/firmware/qcom/sdm845
    /lib/firmware/qcom/sdm845/Thundercomm
    /lib/firmware/qcom/sdm845/Thundercomm/db845c
    /lib/firmware/qcom/sdm845/Thundercomm/db845c/slpi.mbn
    /lib/firmware/qcom/sdm845/Thundercomm/db845c/slpir.jsn
    /lib/firmware/qcom/sdm845/Thundercomm/db845c/slpius.jsn
    /lib/firmware/qcom/sdm845/modemuw.jsn
    /lib/firmware/qcom/sdm845/mba.mbn
    /lib/firmware/qcom/sdm845/adspr.jsn
    /lib/firmware/qcom/sdm845/modem_nm.mbn
    /lib/firmware/qcom/sdm845/adspua.jsn
    /lib/firmware/qcom/sdm845/cdspr.jsn
    /lib/firmware/qcom/sdm845/a630_zap.mbn
    /lib/firmware/qcom/sdm845/adsp.mbn
    /lib/firmware/qcom/sdm845/cdsp.mbn
    /lib/firmware/qcom/a225_pfp.fw
    /lib/firmware/qcom/qcs8300
    /lib/firmware/qcom/qcs8300/qupv3fw.elf
    /lib/firmware/qcom/qcs8300/adspr.jsn
    /lib/firmware/qcom/qcs8300/adspua.jsn
    /lib/firmware/qcom/qcs8300/cdsp0.mbn
    /lib/firmware/qcom/qcs8300/cdspr.jsn
    /lib/firmware/qcom/qcs8300/adsp.mbn
    /lib/firmware/qcom/qcs8300/a623_zap.mbn
    /lib/firmware/qcom/qcs8300/gpdsp0.mbn
    /lib/firmware/qcom/qcs615
    /lib/firmware/qcom/qcs615/a612_zap.mbn
    /lib/firmware/qcom/gen71500_gmu.bin
    /lib/firmware/qcom/a660_gmu.bin
    /lib/firmware/qcom/a420_pm4.fw
    /lib/firmware/qcom/a330_pm4.fw
    /lib/firmware/qcom/a530_gpmu.fw2
    /lib/firmware/qcom/sm8250
    /lib/firmware/qcom/sm8250/Thundercomm
    /lib/firmware/qcom/sm8250/Thundercomm/RB5
    /lib/firmware/qcom/sm8250/Thundercomm/RB5/slpi.mbn
    /lib/firmware/qcom/sm8250/Thundercomm/RB5/slpir.jsn
    /lib/firmware/qcom/sm8250/Thundercomm/RB5/slpius.jsn
    /lib/firmware/qcom/sm8250/a650_zap.mbn
    /lib/firmware/qcom/sm8250/adspr.jsn
    /lib/firmware/qcom/sm8250/adspua.jsn
    /lib/firmware/qcom/sm8250/cdspr.jsn
    /lib/firmware/qcom/sm8250/adsp.mbn
    /lib/firmware/qcom/sm8250/cdsp.mbn
    /lib/firmware/qcom/NOTICE.txt
    /lib/firmware/qcom/aic100
    /lib/firmware/qcom/aic100/fw1.bin
    /lib/firmware/qcom/aic100/fw5.bin
    /lib/firmware/qcom/aic100/fw10.bin
    /lib/firmware/qcom/aic100/fw9.bin
    /lib/firmware/qcom/aic100/sbl.bin
    /lib/firmware/qcom/aic100/fw2.bin
    /lib/firmware/qcom/apq8016
    /lib/firmware/qcom/apq8016/mba.mbn
    /lib/firmware/qcom/apq8016/WCNSS_qcom_wlan_nv_sbc.bin
    /lib/firmware/qcom/apq8016/modem.mbn
    /lib/firmware/qcom/apq8016/wcnss.mbn
    /lib/firmware/qcom/qcm6490
    /lib/firmware/qcom/qcm6490/qupv3fw.elf
    /lib/firmware/qcom/qcm6490/adspr.jsn
    /lib/firmware/qcom/qcm6490/a660_zap.mbn
    /lib/firmware/qcom/qcm6490/adspua.jsn
    /lib/firmware/qcom/qcm6490/battmgr.jsn
    /lib/firmware/qcom/qcm6490/ipa_fws.mbn
    /lib/firmware/qcom/qcm6490/cdspr.jsn
    /lib/firmware/qcom/qcm6490/adsp.mbn
    /lib/firmware/qcom/qcm6490/adsps.jsn
    /lib/firmware/qcom/qcm6490/cdsp.mbn
    /lib/firmware/qcom/apq8096
    /lib/firmware/qcom/apq8096/a530_zap.mbn
    /lib/firmware/qcom/apq8096/mba.mbn
    /lib/firmware/qcom/apq8096/adspr.jsn
    /lib/firmware/qcom/apq8096/adspua.jsn
    /lib/firmware/qcom/apq8096/adsp.mbn
    /lib/firmware/qcom/apq8096/modem.mbn
    /lib/firmware/qcom/apq8096/modemr.jsn
    /lib/firmware/qcom/a530v2_seq.fw2
    /lib/firmware/qcom/venus-4.2
    /lib/firmware/qcom/venus-4.2/venus.mdt
    /lib/firmware/qcom/venus-4.2/venus.b01
    /lib/firmware/qcom/venus-4.2/venus.b00
    /lib/firmware/qcom/venus-4.2/venus.b02
    /lib/firmware/qcom/venus-4.2/venus.b04
    /lib/firmware/qcom/venus-4.2/venus.mbn
    /lib/firmware/qcom/venus-4.2/venus.b03
    /lib/firmware/qcom/vpu-2.0
    /lib/firmware/qcom/vpu-2.0/venus.mdt
    /lib/firmware/qcom/vpu-2.0/venus.b01
    /lib/firmware/qcom/vpu-2.0/venus.b00
    /lib/firmware/qcom/vpu-2.0/venus.b02
    /lib/firmware/qcom/vpu-2.0/venus.b04
    /lib/firmware/qcom/vpu-2.0/venus.mbn
    /lib/firmware/qcom/vpu-2.0/venus.b03
    /lib/firmware/qcom/qcm2290
    /lib/firmware/qcom/qcm2290/modemuw.jsn
    /lib/firmware/qcom/qcm2290/adspr.jsn
    /lib/firmware/qcom/qcm2290/a702_zap.mbn
    /lib/firmware/qcom/qcm2290/adspua.jsn
    /lib/firmware/qcom/qcm2290/adsp.mbn
    /lib/firmware/qcom/qcm2290/adsps.jsn
    /lib/firmware/qcom/qcm2290/modem.mbn
    /lib/firmware/qcom/qcm2290/modemr.jsn
    /lib/firmware/qcom/sc8280xp
    /lib/firmware/qcom/sc8280xp/LENOVO
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qcvss8280.mbn
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/adspr.jsn
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qcslpi8280.mbn
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/adspua.jsn
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/battmgr.jsn
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qcdxkmsuc8280.mbn
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/cdspr.jsn
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qccdsp8280.mbn
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/audioreach-tplg.bin
    /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qcadsp8280.mbn
    /lib/firmware/qcom/venus-5.4
    /lib/firmware/qcom/venus-5.4/venus.mdt
    /lib/firmware/qcom/venus-5.4/venus.b01
    /lib/firmware/qcom/venus-5.4/venus.b00
    /lib/firmware/qcom/venus-5.4/venus.b02
    /lib/firmware/qcom/venus-5.4/venus.b04
    /lib/firmware/qcom/venus-5.4/venus.mbn
    /lib/firmware/qcom/venus-5.4/venus_s2.mbn
    /lib/firmware/qcom/venus-5.4/venus.b03
    /lib/firmware/qcom/a530v3_seq.fw2
    /lib/firmware/qcom/a660_sqe.fw
    /lib/firmware/qcom/a650_gmu.bin
    /lib/firmware/qcom/leia_pfp_470.fw
    /lib/firmware/qcom/venus-1.8
    /lib/firmware/qcom/venus-1.8/venus.mdt
    /lib/firmware/qcom/venus-1.8/venus.b01
    /lib/firmware/qcom/venus-1.8/venus.b00
    /lib/firmware/qcom/venus-1.8/venus.b02
    /lib/firmware/qcom/venus-1.8/venus.b04
    /lib/firmware/qcom/venus-1.8/venus.mbn
    /lib/firmware/qcom/venus-1.8/venus.b03
    /lib/firmware/qcom/vpu
    /lib/firmware/qcom/vpu/vpu30_p4_s6.mbn
    /lib/firmware/qcom/vpu/vpu30_p4.mbn
    /lib/firmware/qcom/vpu/vpu30_p4_s6_16mb.mbn
    /lib/firmware/qcom/vpu/vpu20_p1.mbn
    /lib/firmware/qcom/vpu/vpu20_p4.mbn
    /lib/firmware/qcom/vpu/vpu20_p1_gen2.mbn
    /lib/firmware/qcom/yamato_pfp.fw
    /lib/firmware/qcom/sm8650
    /lib/firmware/qcom/sm8650/SM8650-QRD-tplg.bin
    /lib/firmware/qcom/sm8650/SM8650-MTP-tplg.bin
    /lib/firmware/qcom/gen70500_gmu.bin
    /lib/firmware/qcom/x1e80100
    /lib/firmware/qcom/x1e80100/adspr.jsn
    /lib/firmware/qcom/x1e80100/adspua.jsn
    /lib/firmware/qcom/x1e80100/battmgr.jsn
    /lib/firmware/qcom/x1e80100/adsp.mbn
    /lib/firmware/qcom/x1e80100/adsps.jsn
    /lib/firmware/qcom/x1e80100/gen70500_zap.mbn
    /lib/firmware/qcom/x1e80100/adsp_dtb.mbn
    /lib/firmware/qcom/x1e80100/LENOVO
    /lib/firmware/qcom/x1e80100/LENOVO/21N1
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/adsp_dtbs.elf
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/qcadsp8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/cdsp_dtbs.elf
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/adspr.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/qcvss8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/qccdsp8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/adspua.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/battmgr.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/cdspr.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/qcdxkmsuc8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/X1E80100-LENOVO-Thinkpad-T14s-tplg.bin
    /lib/firmware/qcom/x1e80100/LENOVO/21N1/adsps.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/adsp_dtbs.elf
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/qcadsp8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/qcav1e8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/adspr.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/qcvss8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/X1E80100-LENOVO-Yoga-Slim7x-tplg.bin
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/qccdsp8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/adspua.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/battmgr.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/cdspr.jsn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/qcdxkmsuc8380.mbn
    /lib/firmware/qcom/x1e80100/LENOVO/83ED/adsps.jsn
    /lib/firmware/qcom/a300_pm4.fw
    /lib/firmware/qcom/leia_pm4_470.fw
    /lib/firmware/qcom/a630_gmu.bin
    /lib/firmware/qcom/venus-6.0
    /lib/firmware/qcom/venus-6.0/venus.mbn
    /lib/firmware/qcom/yamato_pm4.fw
    /lib/firmware/qcom/x1p42100
    /lib/firmware/qcom/x1p42100/gen71500_zap.mbn
    /lib/firmware/qcom/a300_pfp.fw
    /lib/firmware/qcom/a663_gmu.bin
    /lib/firmware/qcom/a530v3_gpmu.fw2
    /lib/firmware/qcom/a650_sqe.fw
    /lib/firmware/qcom/a630_sqe.fw
    /lib/firmware/qcom/venus-3.0
    /lib/firmware/qcom/venus-3.0/venus.mdt
    /lib/firmware/qcom/venus-3.0/venus.b01
    /lib/firmware/qcom/venus-3.0/venus.b00
    /lib/firmware/qcom/venus-3.0/venus.b02
    /lib/firmware/qcom/venus-3.0/venus.b04
    /lib/firmware/qcom/venus-3.0/venus.mbn
    /lib/firmware/qcom/venus-3.0/venus.b03
    /lib/firmware/qcom/venus-4.4
    /lib/firmware/qcom/venus-4.4/venus.mdt
    /lib/firmware/qcom/venus-4.4/venus.b01
    /lib/firmware/qcom/venus-4.4/venus.b00
    /lib/firmware/qcom/venus-4.4/venus.b02
    /lib/firmware/qcom/venus-4.4/venus.b04
    /lib/firmware/qcom/venus-4.4/venus.mbn
    /lib/firmware/qcom/venus-4.4/venus.b03
    /lib/firmware/qcom/venus-x
    /lib/firmware/qcom/venus-x/venus.mdt
    /lib/firmware/qcom/venus-x/venus.b01
    /lib/firmware/qcom/venus-x/venus.b00
    /lib/firmware/qcom/venus-x/venus.b02
    /lib/firmware/qcom/venus-x/venus.b04
    /lib/firmware/qcom/venus-x/venus.b03
    /lib/firmware/qcom/vpu-1.0
    /lib/firmware/qcom/vpu-1.0/venus.mdt
    /lib/firmware/qcom/vpu-1.0/venus.b01
    /lib/firmware/qcom/vpu-1.0/venus.b00
    /lib/firmware/qcom/vpu-1.0/venus.b02
    /lib/firmware/qcom/vpu-1.0/venus.b04
    /lib/firmware/qcom/vpu-1.0/venus.mbn
    /lib/firmware/qcom/vpu-1.0/venus.b03
    /lib/firmware/qcom/a530_pfp.fw
    /lib/firmware/qcom/a540_gpmu.fw2
    /lib/firmware/a506_zap.mdt
    /lib/firmware/a530_pm4.fw
    /lib/firmware/regulatory.db.p7s
    /lib/firmware/modem.mdt
    /lib/firmware/modem_pr
    /lib/firmware/modem_pr/mcfg
    /lib/firmware/modem_pr/mcfg/configs
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/commerci/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/commerci/volte/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/commerci/subsidiz
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/commerci/subsidiz/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/commerci/openmkt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/commerci/openmkt/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/lab
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/lab/test
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cu/lab/test/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/commerci/volte_op
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/commerci/volte_op/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/commerci/volte_su
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/commerci/volte_su/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/nsiot_vo
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/nsiot_vo/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/w_irat_c
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/w_irat_c/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/loctech_
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/loctech_/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/tgl_comb
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/tgl_comb/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/eps_only
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/eps_only/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/conf_vol
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/cmcc/lab/conf_vol/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci/volte_op
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci/volte_op/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci/subsidiz
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci/subsidiz/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci/openmkt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci/openmkt/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci/hvolte_o
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/commerci/hvolte_o/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/cta
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/cta/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/test_eps
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/test_eps/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/test_no_
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/test_no_/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/test
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/test/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/conf_vol
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/china/ct/lab/conf_vol/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/3hk
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/3hk/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/3hk/volte/hk
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/3hk/volte/hk/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/ytl
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/ytl/gen_3gpp
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/ytl/gen_3gpp/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/dtac
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/dtac/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/dtac/volte/thailand
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/dtac/volte/thailand/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/trumove
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/trumove/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/trumove/volte/thailand
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/trumove/volte/thailand/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/ais
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/ais/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/ais/volte/thailand
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/ais/volte/thailand/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/smartfre
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/smartfre/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/smartfre/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/singtel
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/singtel/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/singtel/commerci/sg
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/singtel/commerci/sg/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/m1
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/m1/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/m1/volte/singapor
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sea/m1/volte/singapor/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sa
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sa/brazil
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sa/brazil/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/sa/brazil/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/russia
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/russia/beeline
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/russia/beeline/gen_3gpp
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/russia/beeline/gen_3gpp/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/russia/megafon
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/russia/megafon/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/russia/megafon/volte/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/us_cellu
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/us_cellu/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/us_cellu/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/default
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/default/default
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/default/default/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/w_one
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/w_one/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/w_one/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/row
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/row/gen_3gpp
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/row/gen_3gpp/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/multimbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/multimbn/multi_mb
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/multimbn/multi_mb/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/mtn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/mtn/gen_3gpp
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/common/mtn/gen_3gpp/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/reliance
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/reliance/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/reliance/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/dcm
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/dcm/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/dcm/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/kddi
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/kddi/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/kddi/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/sbm
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/sbm/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/apac/sbm/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/sprint
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/sprint/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/sprint/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/tmo
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/tmo/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/tmo/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/verizon
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/verizon/hvolte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/verizon/hvolte/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/verizon/cdmaless
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/verizon/cdmaless/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/att
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/att/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/att/volte/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/att/non_volt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/att/non_volt/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/att/firstnet
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/na/att/firstnet/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/ee
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/ee/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/ee/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci/group_no
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci/group_no/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci/spain
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci/spain/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci/romania
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci/romania/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci/france
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/orange/commerci/france/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt/volte/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt/volte/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt/volte/czech
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt/volte/czech/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt/non_volt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt/non_volt/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/dt/non_volt/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/tim
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/tim/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/tim/volte/italy
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/tim/volte/italy/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/h3g
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/h3g/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/h3g/commerci/italy
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/h3g/commerci/italy/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/h3g/commerci/uk
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/h3g/commerci/uk/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/yoigo
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/yoigo/spain
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/yoigo/spain/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/sfr
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/sfr/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/sfr/volte/fra
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/sfr/volte/fra/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/telefoni
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/telefoni/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/telefoni/volte/de
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/telefoni/volte/de/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/telefoni/non_volt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/telefoni/non_volt/spain
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/telefoni/non_volt/spain/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/safrica
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/safrica/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/turkey
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/turkey/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/netherla
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/netherla/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/cz
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/cz/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/de
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/de/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/spain
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/spain/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/italy
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/italy/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/portugal
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/portugal/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/uk
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/volte/uk/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/non_volt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/non_volt/gen
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/eu/vodafone/non_volt/gen/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/latam
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/latam/amx
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/latam/amx/volte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/latam/amx/volte/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/latam/amx/non_volt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/latam/amx/non_volt/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/lgu
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/lgu/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/lgu/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/skt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/skt/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/skt/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/kt
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/kt/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/kt/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/tta
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/tta/commerci
    /lib/firmware/modem_pr/mcfg/configs/mcfg_sw/generic/korea/tta/commerci/mcfg_sw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la/7+1_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/la/ss/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8/7+1_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8920/wp8/ss/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/default
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/default/default
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/default/default/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/sr_dsds/srlte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/sr_dsds/srlte/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/sr_dsds/normal
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/sr_dsds/normal/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/ss/srlte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/ss/srlte/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/ss/normal
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+1_mode/ss/normal/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/la/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/sr_dsds/srlte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/sr_dsds/srlte/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/sr_dsds/normal
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/sr_dsds/normal/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/ss/srlte
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/ss/srlte/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/ss/normal
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+1_mode/ss/normal/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/qrd8952/wp8/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la/7+1_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/la/ss/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8/7+1_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8953/wp8/ss/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la/7+1_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/la/ss/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8/7+1_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8952/wp8/ss/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la/7+1_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/la/ss/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8/7+1_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8/7+1_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8/7+1_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8/7+5_mode
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8/7+5_mode/sr_dsds
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8/7+5_mode/sr_dsds/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8/ss
    /lib/firmware/modem_pr/mcfg/configs/mcfg_hw/generic/common/msm8940/wp8/ss/mcfg_hw.mbn
    /lib/firmware/modem_pr/mcfg/configs/mbn_ota.txt
    /lib/firmware/goodixfp.mbn
    /lib/firmware/mba.mbn
    /lib/firmware/a530v1_pfp.fw
    /lib/firmware/a702_sqe.fw
    /lib/firmware/a330_pfp.fw
    /lib/firmware/a506_zap.elf
    /lib/firmware/a225_pfp.fw
    /lib/firmware/modem.b07
    /lib/firmware/modem.b02
    /lib/firmware/WCNSS_wlan_dictionary.dat
    /lib/firmware/modem.b08
    /lib/firmware/wcnss.mdt
    /lib/firmware/modem.b10
    /lib/firmware/a420_pm4.fw
    /lib/firmware/a330_pm4.fw
    /lib/firmware/a530_gpmu.fw2
    /lib/firmware/a225p5_pm4.fw
    /lib/firmware/wlan
    /lib/firmware/wlan/prima
    /lib/firmware/wlan/prima/WCNSS_wlan_dictionary.dat
    /lib/firmware/wlan/prima/WCNSS_qcom_wlan_nv.bin
    /lib/firmware/a506_zap.b01
    /lib/firmware/a530v2_seq.fw2
    /lib/firmware/modem.b09
    /lib/firmware/a506_zap.b00
    /lib/firmware/a530v3_seq.fw2
    /lib/firmware/regulatory.db
    /lib/firmware/modem.b16
    /lib/firmware/WCNSS_qcom_wlan_nv.bin
    /lib/firmware/a660_sqe.fw
    /lib/firmware/msadp
    /lib/firmware/modem.b18
    /lib/firmware/adsp.mbn
    /lib/firmware/a506_zap.b02
    /lib/firmware/a300_pm4.fw
    /lib/firmware/qdsp6m.qdb
    /lib/firmware/modem.b04
    /lib/firmware/modem.b13
    /lib/firmware/a530v1_pm4.fw
    /lib/firmware/modem.b11
    /lib/firmware/mba.mdt
    /lib/firmware/prima
    /lib/firmware/prima/WCNSS_wlan_dictionary.dat
    /lib/firmware/prima/WCNSS_qcom_wlan_nv.bin
    /lib/firmware/modem.b05
    /lib/firmware/a300_pfp.fw
    /lib/firmware/a530v3_gpmu.fw2
    /lib/firmware/modem.b19
    /lib/firmware/a650_sqe.fw
    /lib/firmware/a630_sqe.fw
    /lib/firmware/modem.b17
    /lib/firmware/modem.b01
    /lib/firmware/adsp.mdt
    /lib/firmware/modem.b00
    /lib/firmware/wcnss.mbn
    /lib/firmware/a530_pfp.fw
    /lib/firmware/a540_gpmu.fw2
    /lib/firmware/modem.b20
    /lib/firmware/modem.b12

## [Compiling various services needed for the modem to work]

### [qrtr]

[qrtr](https://github.com/linux-msm/qrtr)

It comes with a service qrtr-ns, it is not needed any more since it is done in the kernel side.

#### [Install the repository]

In the chroot clone the repository.

}](https://github.com/linux-msm/qrtr%7D%7D)

Change directory into the repository.

`root `[`#`]`cd qrtr`

Execute the following command to see the supported options:

`root `[`#`]`cat meson_options.txt`

An example configuration of the project to be compiled could look like this for a systemd phone:

`root `[`#`]`meson setup build -Dsystemd-service=disabled -Dqrtr-ns=disabled --prefix=/usr`

Compile the project:

`root `[`#`]`meson compile -C build`

Install it:

`root `[`#`]`meson install -C build`

### [Alsa]

`root `[`#`]`git clone https://github.com/bq-msm8953-mainline/alsa-ucm-conf`

`root `[`#`]`cd alsa-ucm-conf`

`root `[`#`]`cp ucm /usr/share/alsa`

### [Q6voiced]

[q6voiced](https://gitlab.postmarketos.org/postmarketOS/q6voiced/)

Compile it, and install it, the pmaports package has a init service for openrc which it can used

#### [Installing]

Clone the repository.

`root `[`#`]`git clone `[`https://gitlab.postmarketos.org/postmarketOS/q6voiced/`](https://gitlab.postmarketos.org/postmarketOS/q6voiced/)

Change to the directory:

(}

Configure the project:

`root `[`#`]`meson setup build`

Compile:

`root `[`#`]`meson compile -C build`

Install:

`root `[`#`]`meson install -C build`

#### [For Systemd]

[FILE] **`/etc/sytemd/system/q6voiced.service`**

    [Unit]
    Description=Enable q6voice audio when call is performed with oFono

    [Service]
    ExecStart=/usr/local/bin/q6voiced hw:0,4
    Restart=on-failure

    [Install]
    WantedBy=multi-user.target

Enable the service

`root `[`#`]`systemctl enable q6voiced`

#### [For Openrc]

[FILE] **`/etc/init.d/q6voiced`**

    #!/sbin/openrc-run
    supervisor=supervise-daemon

    name="q6voiced"
    description="Enable q6voice audio when call is performed with oFono"

    # Note: q6voice_card/q6voice_device need to be set in /etc/conf.d/q6voiced
    command="/usr/bin/q6voiced"
    command_args="hw:0,4"
    supervise_daemon_args="--user nobody --group audio"

    depend()

Give the correct permissions to the service:

`root `[`#`]`chmod +x /etc/init.d/q6voiced`

Enable the service:

`root `[`#`]`rc-update add q6voiced default`

### [tqftpserv]

[tqftpserv](https://github.com/linux-msm/tqftpserv/)

#### [Install the project]

Clone the repository:

`root `[`#`]`git clone `[`https://github.com/linux-msm/tqftpserv`](https://github.com/linux-msm/tqftpserv)

Change into the directory:

`root `[`#`]`cd tqftpserv`

Configure the project:

`root `[`#`]`meson setup build`

Compile:

`root `[`#`]`meson compile -C build`

Install:

`root `[`#`]`meson install -C build`

#### [Enable the service in Systemd]

`root `[`#`]`systemctl enable tqftpserv`

#### [][Create, and enable the service in Openrc]

[FILE] **`/etc/init.d/tqftpserv`**

    #!/sbin/openrc-run
    supervisor=supervise-daemon
    name="tqftpserv"
    description="Qualcomm Trivial File Transfer Protocol Server"
    command="/usr/bin/tqftpserv"

    depend()

Add execution permission:

`root `[`#`]`chmod +x /etc/init.d/tqftpserv`

Enable the service:

`root `[`#`]`rc-update add tqftpserv default`

### [rmtfs]

[rmtfs](https://github.com/andersson/rmtfs/)

#### [Install the project]

Clone the repository:

`root `[`#`]`git clone `[`https://github.com/andersson/rmtfs/`](https://github.com/andersson/rmtfs/)

Compile the repository:

`root `[`#`]`make rmtfs`

Install the resulting binary:

`root `[`#`]`install -Dm755 rmtfs /usr/sbin/rmtfs`

#### [Create the Systemd service]

Create the file:

[FILE] **`/etc/systemd/system/rmtfs.service`**

    [Unit]
    Description=RMTFS service
    Before=ModemManager.service

    [Service]
    ExecStart=/usr/local/bin/rmtfs -r -P -s
    Restart=always

    [Install]
    WantedBy=multi-user.target

Enable the service:

`root `[`#`]`systemctl enable rmtfs`

#### [Create the Openrc service]

[FILE] **`/etc/init.d/rmtfs`**

    #!/sbin/openrc-run
    supervisor=supervise-daemon

    name="RMTFS"
    description="Qualcomm remote file system service"

    command="/usr/sbin/rmtfs"

    command_args="/usr/local/bin/rmtfs -r -P -s"

    respawn_delay=1

    depend()

Add execution permission to the service:

`root `[`#`]`chmod +x /etc/init.d/rmtfs`

Enable the service:

`root `[`#`]`rc-update add rmtfs default`

### [Udev rules]

Search [pmaports](https://gitlab.postmarketos.org/postmarketOS/pmaports) for udev rules to install into /etc/udev/rules.d, this is how it looks in an example installation:

[FILE] **`/etc/udev/rules.d`Example content of custom udev rules**

    90-device-xiaomi-daisy.rules  90-feedbackd-pm8xxx-vib.rules  90-rmtfs.rules

### [Quirks]

Search [pmaports](https://gitlab.postmarketos.org/postmarketOS/pmaports) for needed bash quirks, only adreno-a506-quirks.sh were found by know.

## [Install a mobile environment]

Check the useflags to support everything the phone needs:

`root `[`#`]`emerge -a eselect-repository`

`root `[`#`]`eselect repository enable guru`

`root `[`#`]`emerge -a gdm phosh NetworkManager modemmanager gnome-terminal --autounmask`

** Note**\
Enable the services NetworkManager ModemManager, and gdm (or display-manager if the phone is using openrc after configuring it to use gdm)

With some luck the images are ready to be flashed now.

## [Running dracut]

`root `[`#`]`emerge -a dracut`

`root `[`#`]`dracut --kver <Everything after vmlinuz- from the file in /boot>`

## [][Copying the kernel, and initramfs to the correct location]

`root `[`#`]`cp /boot/vmlinuz-<version> /boot/vmlinuz`

`root `[`#`]`cp /boot/initramfs-<version> /boot/initrd`

## [Flashing the image]

Ensure the chroot is completely closed, every bash instance is outside of the /mnt/gentoo, and killed any process from:

`root `[`#`]`lsof /mnt/gentoo`

And run the following:

`root `[`#`]`umount -R /mnt/gentoo`

Now run:

** Note**\
This is slow, go grab a coffee

`user `[`$`]`edl w userdata bq-userdata.img`

`user `[`$`]`edl w system bq-system.img`

## [End of installation]

With some luck the phone should boot up with gentoo, and show the gdm init screen, it will be possible to login using the gnome keyboard, and the phone will login into phosh, where it will be possible to join a wifi network, and continue tuning further the phone.

## [Rsync updating the phone]

It is difficult to keep updated the installation using normal means since trying to do heavy compilations in the phone will cause it to auto shutdown, and also the phone will be wanted to be suspended most of the time, the following method can become handy to keep the phone updated while avoding to use portage at all on the phone:

First fetch the rootfs to the computer using this script:

[FILE] **`copy-bardockpro.sh`Copy the rootfs excluding heavy files**

    ssh <The phone ip> sudo mount /boot && sudo rsync -a -e 'sudo -u <computer's user> ssh' --rsync-path="sudo rsync" <The phone ip>:/ gentoo-bq/ --numeric-ids --delete --xattrs -g -o -p -P --exclude=dev/ --exclude=proc/ --exclude=sys/ --exclude=run/ --exclude=home/ --exclude=var/log/ --exclude=tmp/ --exclude=var/cache/ --exclude=var/tmp/ --exclude='*.sw?' --exclude=var/lib/postgresql/ --exclude=swapfile --exclude=var/lib/docker/ --exclude=var/cache --exclude=var/tmp --exclude=root

Then enter in it as chroot, make the necesary updates, and installations.

When finished the following script can be used to send the updates to the phone.

[FILE] **`upload-bardockpro.sh`Upload the rootfs to the phone excluding heavy files**

    ssh <The phone ip> sudo mount /boot && sudo rsync -a -e 'sudo -u <computer's user> ssh' --rsync-path="sudo rsync" gentoo-bq/ <The phone ip>:/ --numeric-ids --delete --xattrs -g -o -p -P --exclude=dev/ --exclude=proc/ --exclude=sys/ --exclude=run/ --exclude=home/ --exclude=var/log/ --exclude=tmp/ --exclude=var/cache/ --exclude=var/tmp/ --exclude='*.sw?' --exclude=var/lib/postgresql/ --exclude=swapfile --exclude=var/lib/docker/ --exclude=var/cache --exclude=var/tmp --exclude=root

** Warning**\
If the upload gets interrupted the phone can be left in an unusable state, and it will be needed to recover using edl, so be careful.

## [Missing pieces]

** Warning**\
Sometimes the phone may lose track of the battery, the touch screen may become unresponsive, and the screen may refuse to power on after suspend. Save any work every time the phone is going to be blocked

Almost everything other venus video encoding, and camera should be working, even calls work pretty well.

## [Troubleshooting]

### [][The phone\'s touchscreen becomes unresponsive after suspend]

A workaround for this bug is to create a script that detects new fails in dmesg and removes the touchscreen kernel module and inserts it again: (The script uses sudo to be able to be used as normal user)

[FILE] **`/usr/local/bin/fix-touch-bq.pl`**

    #!/usr/bin/env perl

    use v5.38.2;

    use strict;
    use warnings;

    my $last_time = 0;
    my $last_line;
    while (1)
                $last_line = $line;
                $last_time = $time;
                $found = 1;
            }
        }
        if ($found)
        sleep 1;
        };
        if ($@)
    }

Then it can be added it to the crontab:

`root `[`#`]`crontab -e`

With this content:

[FILE] **`Crontab Contents`**

    @reboot perl /usr/local/bin/fix-touch-bq.pl

### [Modem disconnects randomly]

It is possible to overcome this failure running this commands:

`root `[`#`]`systemctl restart rmtfs`

`root `[`#`]`sleep 1`

`root `[`#`]`systemctl restart ModemManager`

`root `[`#`]`sleep 1`

`root `[`#`]`systemctl restart NetworkManager`

If the administrator wanted to automate this process they could do it creating a file like this one:

[FILE] **`/usr/local/bin/fix-modem-bq.pl`**

    #!/usr/bin/env perl

    use v5.38.2;

    use strict;
    use warnings;

    my $start_time = time;
    my $last_time_locked = 0;
    while (1)
            if ( `mmcli -m any` =~ /state:[^\n]*locked/ )
            my $ip_a = `ip a`;
            if ( $ip_a !~ /^[^\n]*\@rmnet_ipa[^\n]*UP[^\n]*$/m )
        };
        if ($@)
        sleep 1;
    }

    sub reset_rmtfs( $message )

Later executing:

`root `[`#`]`crontab -e`

And adding this contents to the crontab:

[FILE] **`Crontab Contents`**

    @reboot perl /usr/local/bin/fix-modem-bq.pl

This script will reset all your network again if the phone does not connect to mobile data after unlocking the pin code of the phone in 60 seconds, so it may not be useful for every user depending on the needs.

### [][Suspend messes up modem, touch and other things]

Disable suspend and substitute it with this script:

[FILE] **`/usr/local/bin/nuke-cpus-on-screen-off.pl`**

    #!/usr/bin/env perl

    use v5.38.2;
    use strict;
    use warnings;

    my $last_state = 0;
    while (1) ;
        if ($@)
            $current_state = 0;
        }
        if ( ( !!$last_state ) == ( !!$current_state ) )
        $last_state    = $current_state;
        $current_state = 0 + !!$current_state;
        for my $cpu_number ( 1 .. 7 ) /online";
            open my $fh, '&gt;', "/sys/devices/system/cpu/cpu$/online" or die 'Whatever';
        say $current_state;
            $fh-&gt;print($current_state);
        $fh-&gt;flush;
            close $fh;
        }
        sleep 5;
    }

With this crontab line:

[FILE] **`Crontab Contents`**

    @reboot sudo perl /usr/local/bin/nuke-cpus-on-screen-off.pl

This script will reduce the phone\'s battery waste without suspend to the half, so the phone will have more or less 6 hours of phone battery if it is unused, better battery saving scripts exist on the internet based in stopping processes, if interested in more battery time looking what the internet has to offer would be a good idea.

### [][There are too few key shortcut options in the terminal in Phosh for the user\'s needs]

While using the terminal the user may find itself unable to do certain actions because the terminal shortcut options are too limited for example to use vim, this is solvable using dconf to add new shortcuts like this: (In this case adding [Esc], [Page Up], and [Page Down])

`user `[`$`]`dconf write /sm/puri/phosh/osk/terminal/shortcuts "['Escape', 'Page_Up', 'Page_Down', '<ctrl>', '<alt>', '<ctrl>r', 'Home', 'End', '<ctrl>w', '<alt>b', '<alt>f', '<ctrl>v', '<ctrl>c', '<ctrl><shift>v', '<ctrl><shift>c', 'Menu']"`

The names of the keys are from [gdkkeysyms.h](https://gitlab.gnome.org/GNOME/gtk/-/blob/main/gdk/gdkkeysyms.h) ignoring the leading GDK_KEY\_.

The full documentation about how those accelerators are parsed can be found in [func.accelerator_parse.html from GTK4](https://docs.gtk.org/gtk4/func.accelerator_parse.html). The administrator should be able with this hints to craft it\'s own shortcuts.

The order chosen is respected by Phosh, so the user can tailor it completely to their needs.