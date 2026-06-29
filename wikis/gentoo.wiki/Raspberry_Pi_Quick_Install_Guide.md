**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only. *Page archived as of **20240630**.*

\
TLDR: **Do not use this article!**

** See also**\
Superseded by [Raspberry_Pi_Install_Guide](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide "Raspberry Pi Install Guide")

Installing Gentoo onto a Raspberry Pi is relatively straight forward and in some ways easier than installing Gentoo on another system because a kernel image is provided by the Raspberry Pi Foundation. This means Gentoo can be installed quickly onto a Raspberry Pi.

This quick install guide presumes the reader will be installing an official Raspberry Pi Foundation 32-bit kernel from a Linux based operating system.

## Contents

-   [[1] [Preparing the SD card]](#Preparing_the_SD_card)
    -   [[1.1] [Create the partitions]](#Create_the_partitions)
    -   [[1.2] [Create the file systems]](#Create_the_file_systems)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Mounting the partitions]](#Mounting_the_partitions)
    -   [[2.2] [Extract stage 3 image]](#Extract_stage_3_image)
    -   [[2.3] [Install Portage]](#Install_Portage)
    -   [[2.4] [Install kernel and modules]](#Install_kernel_and_modules)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Edit fstab]](#Edit_fstab)
    -   [[3.2] [Set boot options]](#Set_boot_options)
    -   [[3.3] [Edit make.conf]](#Edit_make.conf)
    -   [[3.4] [Configure time zone]](#Configure_time_zone)
    -   [[3.5] [Clear root password]](#Clear_root_password)
    -   [[3.6] [Unmount the SD card and boot the Raspberry Pi]](#Unmount_the_SD_card_and_boot_the_Raspberry_Pi)
-   [[4] [Post boot configuration]](#Post_boot_configuration)
    -   [[4.1] [Set root password]](#Set_root_password)
    -   [[4.2] [Enabling networking on boot]](#Enabling_networking_on_boot)
    -   [[4.3] [Select profile]](#Select_profile)
    -   [[4.4] [Configuring inittab and rc.conf]](#Configuring_inittab_and_rc.conf)
    -   [[4.5] [Enable software clock]](#Enable_software_clock)
    -   [[4.6] [Enable the SSH daemon]](#Enable_the_SSH_daemon)
-   [[5] [Overclocking]](#Overclocking)
    -   [[5.1] [Enabling overclocking]](#Enabling_overclocking)
    -   [[5.2] [Optional cpupower]](#Optional_cpupower)
    -   [[5.3] [Force turbo option]](#Force_turbo_option)
    -   [[5.4] [Changing memory split]](#Changing_memory_split)
-   [[6] [Cross building (optional)]](#Cross_building_.28optional.29)
-   [[7] [Hardware random number generator]](#Hardware_random_number_generator)
    -   [[7.1] [Install rng-tools]](#Install_rng-tools)
    -   [[7.2] [Load bcm2708-rng]](#Load_bcm2708-rng)
    -   [[7.3] [Apply settings in /etc/conf.d/rngd]](#Apply_settings_in_.2Fetc.2Fconf.d.2Frngd)
    -   [[7.4] [Check that /dev/random is slow]](#Check_that_.2Fdev.2Frandom_is_slow)
    -   [[7.5] [Restart rngd]](#Restart_rngd)
    -   [[7.6] [Test if it works]](#Test_if_it_works)
    -   [[7.7] [Add rng-tools to boot]](#Add_rng-tools_to_boot)
    -   [[7.8] [Add loading of bcm2708-rng to boot]](#Add_loading_of_bcm2708-rng_to_boot)
-   [[8] [Install video core userland tools and libraries]](#Install_video_core_userland_tools_and_libraries)
-   [[9] [Notes and references]](#Notes_and_references)
-   [[10] [See also]](#See_also)
-   [[11] [External resources]](#External_resources)

## [Preparing the SD card]

The Raspberry Pi boots off a FAT32 [/boot] partition. It will also require root and swap partitions.

### [Create the partitions]

Use the `fdisk` utility to create the partitions:

`root `[`#`]`fdisk -l /dev/mmcblk0`

    Disk /dev/mmcblk0: 7948 MB, 7948206080 bytes
    4 heads, 16 sectors/track, 242560 cylinders
    Units = cylinders of 64 * 512 = 32768 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x000635b7

            Device Boot      Start         End      Blocks   Id  System
    /dev/mmcblk0p1               1        3201      102424    c  W95 FAT32 (LBA)
    /dev/mmcblk0p2            3202        7298      131104   82  Linux swap / Solaris
    /dev/mmcblk0p3            7299      242560     7528384   83  Linux

### [Create the file systems]

`root `[`#`]` mkfs.vfat -F 16 /dev/mmcblk0p1 `

`root `[`#`]` mkswap /dev/mmcblk0p2 `

`root `[`#`]` mkfs.ext4 /dev/mmcblk0p3 `

When using a 4GB SD card:

`root `[`#`]`mkfs.ext4 -N 803200 /dev/mmcblk0p3`

## [Installation]

The installation will be preformed onto the SD card.

### [Mounting the partitions]

`root `[`#`]` mkdir /mnt/gentoo `

`root `[`#`]` mount /dev/mmcblk0p3 /mnt/gentoo `

`root `[`#`]` mkdir /mnt/gentoo/boot/ `

`root `[`#`]` mount /dev/mmcblk0p1 /mnt/gentoo/boot `

### [Extract stage 3 image]

For Raspberry Pi A, A+, B, B+:

`root `[`#`]` cd /tmp/ `

`root `[`#`]` wget http://gentoo.osuosl.org/releases/arm/autobuilds/current-stage3-armv6j_hardfp/stage3-armv6j_hardfp-20160220.tar.bz2 (Change the date for the latest or required stage.) `

`root `[`#`]` tar xfpj stage3-armv6j_hardfp-*.tar.bz2 -C /mnt/gentoo/ `

For Raspberry Pi 2 or Raspberry Pi 3 (in 32 bit mode):

`root `[`#`]` cd /tmp/ `

`root `[`#`]` wget http://gentoo.osuosl.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp/stage3-armv7a_hardfp-20160325.tar.bz2 (Change the date for the latest or required stage.) `

`root `[`#`]` tar xfpj stage3-armv7a_hardfp-*.tar.bz2 -C /mnt/gentoo/ `

### [Install Portage]

`root `[`#`]` wget `[`https://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2`](https://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2)` `

`root `[`#`]` tar xjf portage-latest.tar.bz2 -C /mnt/gentoo/usr `

### [Install kernel and modules]

The Raspberry Pi Foundation maintains a branch of the Linux kernel that will run on the Raspberry Pi, including a compiled version which we use here:

`root `[`#`]` cd /tmp/ `

`root `[`#`]` git clone -b stable --depth 1 https://github.com/raspberrypi/firmware/ `

`root `[`#`]` cd firmware/boot `

`root `[`#`]` cp -r * /mnt/gentoo/boot/ `

`root `[`#`]` cp -r ../modules /mnt/gentoo/lib/ `

## [Configuration]

### [Edit fstab]

Edit the [/etc/fstab] file to match the previously created partition scheme:

`root `[`#`]` nano /mnt/gentoo/etc/fstab `

[FILE] **`/etc/fstab`Example**

    /dev/mmcblk0p1        /boot       auto        noauto,noatime  1 2
    /dev/mmcblk0p3      /       ext4        noatime     0 1
    /dev/mmcblk0p2      none        swap        sw      0 0

### [Set boot options]

Create a file called [cmdline.txt] in [/boot] to pass options to the kernel:

`root `[`#`]` nano /mnt/gentoo/boot/cmdline.txt `

[FILE] **`/boot/cmdline.txt`**

    dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p3 rootfstype=ext4 elevator=deadline rootwait

### [Edit make.conf]

The default [make.conf] includes basic CFLAGS. To change the settings to something more \'optimal\' for the Pi look at the details on the [relevant wiki page](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi").

### [Configure time zone]

View a list of time zones using this command:

`root `[`#`]` ls /mnt/gentoo/usr/share/zoneinfo `

Choose the appropriate time zone. Note that some of the listings in the [zoneinfo] directory are folders that contain more specific time zones. For example, supposing Europe/London is the local time zone:

`root `[`#`]` cp /mnt/gentoo/usr/share/zoneinfo/Europe/London /mnt/gentoo/etc/localtime `

Next set the timezone:

`root `[`#`]` echo "Europe/London" > /mnt/gentoo/etc/timezone `

### [Clear root password]

As chroot was not performed before booting, the root password needs to be unset. Allowing login with a blank password for the root user.

`root `[`#`]` sed -i 's/^root:.*/root::::::::/' /mnt/gentoo/etc/shadow `

### [Unmount the SD card and boot the Raspberry Pi]

Unmount the SD card:

`root `[`#`]` umount /mnt/gentoo/boot `

`root `[`#`]` umount /mnt/gentoo `

Plugin the SD card to the Raspberry Pi, make sure there is a keyboard and monitor plugged in, then connect the power supply. Hopefully Gentoo will boot displaying a login prompt, login as root and no password. During the first boot there could be a few warnings and errors which can be fixed in the next section.

## [Post boot configuration]

### [Set root password]

Immediately set a root password:

`root `[`#`]` passwd `

### [Enabling networking on boot]

Assuming the use of DHCP on the eth0 network interface.

`root `[`#`]` cd /etc/init.d/ `

`root `[`#`]` ln -sv net.lo net.eth0 `

`root `[`#`]` rc-service net.eth0 start `

`root `[`#`]` rc-update add net.eth0 boot `

Please also note that [rc-update] may need to be run, as follows

`root `[`#`]` rc-update --update `

to force an update of the dependency tree. This may be needed in the event of clock skew (in this specific case the eth0 device will not start up after reboot).

### [Select profile]

List the available profiles.

`root `[`#`]` eselect profile list `

Select the desired profile, for example *\[25\] default/linux/arm/13.0/armv6j*:

`root `[`#`]` eselect profile set 25 `

### [Configuring inittab and rc.conf]

Uncomment the linux specific rc.conf rc_sys value, to stop warning in boot up.

`root `[`#`]` nano /etc/rc.conf `

[FILE] **`/etc/rc.conf`**

    rc_sys=""

Comment out the s0 Serial console to stop \"INIT: Id \"s0\" respawning too fast\" messages on the console.

`root `[`#`]` nano /etc/inittab `

[FILE] **`/etc/inittab`**

    # SERIAL CONSOLES
    #s0:12345:respawn:/sbin/agetty 9600 ttyS0 vt100
    #s1:12345:respawn:/sbin/agetty 9600 ttyS1 vt100

### [Enable software clock]

The Raspberry Pi does not have a hardware clock, so the hwclock daemon needs to disabled, then swclock can be enabled to mitigate the issue.

`root `[`#`]` rc-update add swclock boot `

`root `[`#`]` rc-update del hwclock boot`

The date still needs to be set beforehand to install any package, or in the compiling phase there could be warnings about clock skew. Check [system time](https://wiki.gentoo.org/wiki/System_time "System time") using [date] command.

`root `[`#`]` date`

    Thu May 02 04:21:18 UTC 2013

If the date/time displayed is wrong, update it using the [date] MMDDhhmmYYYY syntax (Month, Day, hour, minute and Year). At this stage, the timezone that was set before in the Configure time zone section should be used. For instance, to set the date to May 02th, 04:21 in the year 2013:

`root `[`#`]` date 050204212013`

Now it is possible to set the [system time](https://wiki.gentoo.org/wiki/System_time "System time") using [NTP](https://wiki.gentoo.org/wiki/NTP "NTP") software to setup the system clock on boot.

`root `[`#`]`emerge --ask ntp`

`root `[`#`]` rc-update add ntp-client default `

### [Enable the SSH daemon]

`root `[`#`]` rc-update add sshd default `

`root `[`#`]` /etc/init.d/sshd start `

## [Overclocking]

It is very easy to overclock a Raspberry Pi up to 1000MHz without affecting the warranty [\[1\]](http://www.raspberrypi.org/archives/2008)

[Suggested overclocking values]

\

    #“None” “700MHz ARM, 250MHz core, 400MHz SDRAM, 0 overvolt”
    #“Modest” “800MHz ARM, 300MHz core, 400MHz SDRAM, 0 overvolt”
    #"Medium” “900MHz ARM, 333MHz core, 450MHz SDRAM, 2 overvolt”
    #“High” “950MHz ARM, 450MHz core, 450MHz SDRAM, 6 overvolt”
    #“Turbo” “1000MHz ARM, 500MHz core, 500MHz SDRAM, 6 overvolt”

### [Enabling overclocking]

To enable overclocking select one of the suggest modes from the list above, \"Medium\" is generally a good starting point. Edit the [/boot/config.txt] file, add the appropriate values and reboot the Raspberry Pi for changes to take effect.

`root `[`#`]`mount /boot/ `

`root `[`#`]`nano /boot/config.txt `

[FILE] **`/boot/config.txt`Example with Medium overclocking**

    arm_freq=900
    core_freq=333
    sdram_freq=450
    over_voltage=2

### [Optional cpupower]

To manage the CPU frequency scaling, use the [[[sys-power/cpupower]](https://packages.gentoo.org/packages/sys-power/cpupower)[]].

`root `[`#`]`emerge --ask sys-power/cpupower`

`root `[`#`]`rc-update add cpupower default `

The default scaling governor can be changed in the /etc/conf.d/cpupower file

[FILE] **`/etc/conf.d/cpupower`Example config with on demand scaling**

    START_OPTS="--governor ondemand"
    STOP_OPTS="--governor performance"

Confirm the current scaling and CPU using the cpupower command

`root `[`#`]` cpupower frequency-info `

### [Force turbo option]

** Warning**\
Using `force_turbo` can void your warranty if used with with certain other config values like `over_voltage` with specific values. See [this](https://raspberrypi.stackexchange.com/a/81489) Stack Exchange post for more info.

The `force_turbo` option turns off the dynamic clocks and runs the Raspberry Pi constantly at the highest arm_freq. [\[2\]](https://elinux.org/RPiconfig#force_turbo_mode)

Edit the [/boot/config.txt] file, add `force_turbo=1` then reboot the Raspberry Pi for changes to take effect.

`root `[`#`]`nano /boot/config.txt `

[FILE] **`/boot/config.txt`Example with Medium overclocking and force turbo**

    arm_freq=900
    core_freq=333
    sdram_freq=450
    over_voltage=2
    force_turbo=1

### [Changing memory split]

Not strictly speaking overclocking, but the memory used by the GPU can be changed. To change the memory used by the GPU down to a minimum of 16MB add the gpu_mem value to /boot/config.txt, then reboot the Raspberry Pi for changes to take effect.

[FILE] **`/boot/config.txt`Example with the minimum 16MB of memory for GPU**

    gpu_mem=16

## [][Cross building (optional)]

This is not strictly required, but it is extremely practical given the source driven nature of Gentoo. Building almost anything on the Raspberry Pi takes a very, very long time - especially when there are a lot of dependencies involved.

Fortunately, much of the heavy lifting work can be offloaded to a more powerful system (such as a another gentoo desktop/server) using crossdev and distcc (though this will only work for packages must compile c/c++).

Full details of using distcc and crossdev on the Raspberry Pi are described in [Raspberry Pi Cross building](https://wiki.gentoo.org/wiki/Raspberry_Pi_Cross_building "Raspberry Pi Cross building").

## [Hardware random number generator]

The Arch Wiki tells us that the Raspberry Pi has a hardware random number generator.^[\[1\]](#cite_note-1)^

Hooking it up to [/dev/random] is done via the following steps.

### [Install rng-tools]

`root `[`#`]`emerge -av sys-apps/rng-tools`

### [Load bcm2708-rng]

`root `[`#`]`modprobe bcm2708-rng`

There is a module bcm2835-rng that works with the current tarball.

### [][Apply settings in /etc/conf.d/rngd]

Add the following to /etc/conf.d/rngd

[FILE] **`/etc/conf.d/rngd`**

    RNGD_OPTS="-o /dev/random -r /dev/hwrng"

### [][Check that /dev/random is slow]

To verify that we have done everything correctly, open a new terminal and do:

`user `[`$`]`cat /dev/random`

It will start displaying gibberish (random) but will stop at some point or at least slow down. Now issue [CTRL]+[c] to stop it.

### [Restart rngd]

`root `[`#`]`/etc/init.d/rngd restart`

### [Test if it works]

Again, issue:

`user `[`$`]`cat /dev/random`

in another terminal. Now the random information should be flowing faster than the first time around. Now issue [CTRL]+[c] to stop it.

On an idling Pi (networked via a Wi-Fi USB dongle, a USB keyboard attached, display connected) [/dev/random] spews 4-5 \"chars\" of random information before it blocks. After loading the module and starting rng-tools, it began printing out many lines without blocking.

### [Add rng-tools to boot]

If all is good, add rngd to boot.

`root `[`#`]`rc-update add rngd boot`

### [Add loading of bcm2708-rng to boot]

Add the following to [/etc/modules-load.d/random.conf] so that the module gets loaded at boot

[FILE] **`/etc/modules-load.d/random.conf`**

    bcm2708-rng

## [Install video core userland tools and libraries]

The ARM side libraries for interfacing to Raspberry Pi GPU are included in a package raspberrypi-userland. Which includes the Video Core tools, GLES2, EGL, openmax and openVG libs that support the Raspberry Pi GPU.

`root `[`#`]`emerge --ask raspberrypi-userland`

Then optionally add the following to the shellrc (.bashrc/.zshrc) file to be able to call things like vcgencmd directly.

[FILE] **`~/.bashrc`**

    export PATH=$PATH:/opt/vc/bin

## [Notes and references]

1.  [[[↑](#cite_ref-1)] [[Raspberry Pi Hardware RNG](https://wiki.archlinux.org/index.php/Raspberry_Pi#Hardware_random_number_generator)]]

## [See also]

-   [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi")
-   [Raspberry Pi/Kernel Compilation](https://wiki.gentoo.org/wiki/Raspberry_Pi/Kernel_Compilation "Raspberry Pi/Kernel Compilation")
-   [Raspberry Pi/Cross building](https://wiki.gentoo.org/wiki/Raspberry_Pi/Cross_building "Raspberry Pi/Cross building")
-   [Gentoo Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook") - More information about embedded hardware, cross compiling, and other related topics.

## [External resources]

-   [Raspberry Pi Hub](https://elinux.org/RPi_Hub) at eLinux wiki, with more advanced tutorials to get the most out of the Raspberry Pi