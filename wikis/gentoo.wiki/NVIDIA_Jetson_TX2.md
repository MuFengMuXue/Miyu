This article briefly describes the process of imaging a NVIDIA Jetson TX2 with Gentoo aarch64 from an amd64 host. These instructions may be be adapted to suit other NVIDIA Jetson devices with some common-sense modifications; TX2-specific configuration will be called out where possible.

The primary approach documented is the use of external storage to avoid modification of the existing Linux4Tegra software image such that the device can be restored to an out-of-the-box configuration by removing external storage which (as a happy side effect) also ensures that the device can be recovered using the Linux4Tegra image.

It is possible to install Gentoo directly to the eMMC if external storage is unavailable, however this may impact on the longevity of the flash memory.

Upstream documentation on the device is available [here](https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3273/index.html).

## Contents

-   [[1] [Booting the TX2]](#Booting_the_TX2)
    -   [[1.1] [Boot Sequence and Sysboot Configuration Files]](#Boot_Sequence_and_Sysboot_Configuration_Files)
    -   [[1.2] [Changing the Boot Order]](#Changing_the_Boot_Order)
-   [[2] [Optional Prerequisites]](#Optional_Prerequisites)
    -   [[2.1] [Update the onboard L4T image]](#Update_the_onboard_L4T_image)
    -   [[2.2] [Configure QEMU user and binfmt]](#Configure_QEMU_user_and_binfmt)
-   [[3] [Preparing an Image]](#Preparing_an_Image)
-   [[4] [Flashing the Image]](#Flashing_the_Image)
-   [[5] [Custom Kernels]](#Custom_Kernels)
    -   [[5.1] [Sources]](#Sources)

## [Booting the TX2]

The Jetson TX2, like other NVIDIA Tegra devices, uses the [Das U-Boot](https://wiki.gentoo.org/wiki/Das_U-Boot "Das U-Boot") bootloader to load Linux from a rootfs on a bootable device.

### [Boot Sequence and Sysboot Configuration Files]

U-Boot includes a default boot sequence - It scans bootable devices for /boot/extlinux/extlinux.conf in the following order:

-   External SD card
-   Internal eMMC
-   USB device or NVMe device (Jetson TX2 series only)
-   NFS network via DHCP/PXE

Where extlinux.conf is a standard [extlinux](https://wiki.gentoo.org/wiki/Syslinux "Syslinux") text-format sysboot configuration file that contains the:

-   kernel image filename
-   initramfs image filename (optional)
-   device tree blob filename (optional)
-   kernel command line.

Once an extlinux.conf has been identified, U-Boot performs the following steps:

1.  Uses the sysboot command to read the boot configuration from extlinux.conf
2.  Loads the specified kernel Image file (+ initramfs and device tree blob if configured)
3.  Boots the kernel

The images and extboot configuration may be replaced or updated from a running system; it is not required to flash a new system image to update the kernel.

### [Changing the Boot Order]

It may be desirable to boot off a device that is enumerated after the eMMC in the default boot order. There are several mechanisms for achieving this:

-   Use the extlinux configuration, kernel, and associated boot files on an SD card or the eMMC to boot a rootfs on another device
-   Use the Boot Menu (available **only** via UART; the recovery console is inactive) temporarily
-   Compile and provide U-Boot using the NVIDIA sources.

## [Optional Prerequisites]

#### [Update the onboard L4T image]

If it is desirable to use the L4T kernel, modules, and initramfs these items should be updated first. NVIDIA provide a docker image containing the SDK Manager which can be used to flash the device; An NVIDIA Developer Zone login is required to proceed. Further documentation is available [here](https://docs.nvidia.com/sdk-manager/docker-containers/index.html).

It is recommended to place the device in recovery mode before running the container.

1\. [Source the appropriate docker image](https://developer.nvidia.com/drive/sdk-manager) (18.04) from NVIDIA and load it into docker with an appropriate tag.

`user `[`$`]`docker load -i sdkmanager-1.9.1.10844-Ubuntu_18.04_docker.tar.gz`

`user `[`$`]`docker tag sdkmanager-1.9.1.10844-Ubuntu_18.04_docker.tar.gz sdkmanager:latest`

2\. Run the container.

`user `[`$`]`docker run -rm -it --privileged -v /dev/bus/usb:/dev/bus/usb/ -v /dev:/dev -v /media/$USER:/media/nvidia:slave --rm sdkmanager:latest --cli install --logintype devzone --product Jetson --version 4.6.3 --targetos Linux --host --target JETSON_TX2_TARGETS --flash all --additionalsdk 'DeepStream 6.0.1' --license accept --staylogin true --datacollection disable --exitonfinish`

3\. Follow the prompts to login to the NVIDIA Developer Zone and continue until the device has been flashed.

#### [Configure QEMU user and binfmt]

1\. Configure and install QEMU to enable chrooting into an aarch64 rootfs.

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu QEMU_SOFTMMU_TARGETS: aarch64 x86_64
    app-emulation/qemu QEMU_USER_TARGETS: aarch64

`root `[`#`]`echo app-emulation/qemu static-user >> /etc/portage/package.use/qemu `

`root `[`#`]`echo ':aarch64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7\x00:\xff\xff\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-aarch64:' > /proc/sys/fs/binfmt_misc/register `

`root `[`#`]`echo ':aarch64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7\x00:\xff\xff\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-aarch64:' > /etc/binfmt.d/qemu-aarch64-static.conf `

`root `[`#`]`systemctl restart systemd-binfmt `

`root `[`#`]`emerge --ask app-emulation/qemu`

`root `[`#`]`gpasswd -a larry kvm `

`root `[`#`]`quickpkg app-emulation/qemu `

2\. Setup an appropriate crossdev toolchain:

`root `[`#`]`emerge --ask sys-devel/crossdev`

`root `[`#`]`mkdir -p /var/db/repos/crossdev/ `

`root `[`#`]`echo 'crossdev' > /var/db/repos/crossdev/profiles/repo_name `

`root `[`#`]`echo 'masters = gentoo' > /var/db/repos/crossdev/metadata/layout.conf `

`root `[`#`]`echo 'thin-manifests = true >> /var/db/repos/crossdev/metadata/layout.conf `

`root `[`#`]`chown -R portage:portage /var/db/repos/crossdev `

[FILE] **`/etc/portage/repos.conf/crossdev.conf`**

    [crossdev]
    location = /var/db/repos/crossdev
    priority = 10
    masters = gentoo
    auto-sync = no

`root `[`#`]`crossdev --stable -t aarch64-linux-gnueabi `

## [Preparing an Image]

1\. Create a development space for associated files

`user `[`$`]`mkdir -p ~/development/jetson_tx2/rootfs`

`user `[`$`]`cd ~/development/jetson_tx2`

`user `[`$`]`chown root:root rootfs`

2\. Download and extract the latest arm64 stage3 tarball and portage snapshot.

`user `[`$`]`wget `[`https://gentoo.osuosl.org/releases/arm64/autobuilds/current-stage3-arm64-systemd/stage3-arm64-systemd-*.tar.xz`](https://gentoo.osuosl.org/releases/arm64/autobuilds/current-stage3-arm64-systemd/stage3-arm64-systemd-*.tar.xz)

`user `[`$`]`wget `[`http://distfiles.gentoo.org/snapshots/portage-latest.tar.xz`](http://distfiles.gentoo.org/snapshots/portage-latest.tar.xz)

`root `[`#`]`cd rootfs`

`root `[`#`]`tar xpvf ../stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner`

`root `[`#`]`cd /var/db/repos`

`root `[`#`]`tar xpvf ../../../../portage-latest --xattrs-include='*.*' --numeric-owner`

`root `[`#`]`mv portage gentoo`

3\. Set a root password

`root `[`#`]`cd ../../../`

`root `[`#`]`ROOTPASS=$(openssl passwd -6 -salt xyz «your_password_here»)`

`root `[`#`]`sed -i -e "s,^root:[^:]\+:,root:$:," etc/shadow`

4\. Create a non-root user

`root `[`#`]`ROOTFS_USERNAME=larry`

`root `[`#`]`USERPASS=$(openssl passwd -6 -salt xyz «your_password_here»)`

`root `[`#`]`mkdir -p home/$ && cp -R etc/skel/* home/$/`

`root `[`#`]`chown -R $:$ home/$`

`root `[`#`]`chmod -R go=u,go-w home/$ && chmod go= home/$`

`root `[`#`]`echo "$:x:1000:1000::/home/$:/bin/bash" >> etc/passwd`

`root `[`#`]`echo "$:x:1000:" >> etc/group`

`root `[`#`]`for group in wheel audio video users;`

`root `[`#`]`do sed -i "/^$:/ s/$/ $/" etc/group; done`

5\. Customise the system image; Emerge QEMU into the target and chroot. Proceed with a typical Stage 3 configuration oustide of Kernel and Bootloader

`root `[`#`]`ROOT=$PWD/ emerge --usepkgonly --oneshot --nodeps qemu `

`root `[`#`]`mount --bind /proc proc `

`root `[`#`]`mount --bind /sys sys `

`root `[`#`]`mount --bind /dev dev `

`root `[`#`]`mount --bind /dev/pts dev/pts `

`root `[`#`]`chroot . /bin/bash --login `

6\. Apply the Tegra firmware to the rootfs.

** Note**\
Until bug 703278 is resolved, FEATURES=\"-pid-sandbox\" must be set or all emerges in the chroot (if using QEMU) will fail.

`root `[`#`]`emerge --ask sys-firmware/jetson-tx2-firmware x11-drivers/jetson-tx2-drivers`

7\. On the build host, install mkstage4 and use it to create a stage4 for installation on the device

`root `[`#`]`emerge --ask app-backup/mkstage4-0.4`

## [Flashing the Image]

1.  Connect appropriate external storage
2.  Boot the Jetson TX2 into a working Linux
3.  rsync the stage4 image onto the TX2
4.  Partition external storage and unpack the image
5.  Partition the SD card as ext4 and copy the boot files to it

`root `[`#`]`gparted /dev/mmcblk1`

`root `[`#`]`mkdir /mnt/sdcard`

`root `[`#`]`mount /dev/mmcblk1p1 /mnt/sdcard`

`root `[`#`]`mkdir /mnt/sdcard/boot`

`root `[`#`]`cp -R /boot/* /mnt/sdcard/boot/`

`root `[`#`]`# Update kernel command line to point to appropriate device`

`root `[`#`]`vim /mnt/sdcard/boot/extlinux/extlinux.conf`

When the device is next booted the SD card extlinux config, kernel, and supporting files will be used to boot the device off external storage.

## [Custom Kernels]

While this article uses the existing kernel and initramfs to boot Gentoo, it is possible to compile a custom kernel.

### [Sources]

-   The Mainline kernel has some support for Jetson devices
-   NVIDIA provide kernel source tarballs with each L4T release
-   The [tegra-mainline-linux](https://github.com/sarnold/tegra-mainline-linux) sources are relatively up-to-date and should support all hardware but will \*not\* work with NVIDIA drivers and libraries.
-   The [LADI](https://github.com/LADI/linux) sources are reported to work with NVIDIA drivers and libraries.

<!-- -->

-