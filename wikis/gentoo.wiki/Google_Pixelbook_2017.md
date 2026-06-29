[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Google_Pixelbook_(2017)&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## Contents

-   [[1] [Summary]](#Summary)
-   [[2] [Hardware specifications]](#Hardware_specifications)
-   [[3] [Booting from USB]](#Booting_from_USB)
    -   [[3.1] [Enable developer mode]](#Enable_developer_mode)
    -   [[3.2] [Enable USB boot]](#Enable_USB_boot)
-   [[4] [Installing Gentoo]](#Installing_Gentoo)
    -   [[4.1] [Partitioning]](#Partitioning)
    -   [[4.2] [RW_LEGACY flashing]](#RW_LEGACY_flashing)
    -   [[4.3] [Genkernel and hardware support (a warning)]](#Genkernel_and_hardware_support_.28a_warning.29)
-   [[5] [Running Gentoo]](#Running_Gentoo)
    -   [[5.1] [Display scaling/DPI]](#Display_scaling.2FDPI)
    -   [[5.2] [Trackpad/touchpad and touchscreen]](#Trackpad.2Ftouchpad_and_touchscreen)
    -   [[5.3] [Audio]](#Audio)
        -   [[5.3.1] [Kernel requirements]](#Kernel_requirements)
        -   [[5.3.2] [Firmware requirements]](#Firmware_requirements)
    -   [[5.4] [Keyboard]](#Keyboard)
        -   [[5.4.1] [Key remapping]](#Key_remapping)
        -   [[5.4.2] [Backlight]](#Backlight)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Factory reset]](#Factory_reset)
    -   [[6.2] [Flashing/blinking keyboard when attempting to boot]](#Flashing.2Fblinking_keyboard_when_attempting_to_boot)

## [Summary]

The [Pixelbook](https://www.google.com/chromebook/device/google-pixelbook/) is a laptop made by Google. Released in October 2017, it was met with a mixed response from the tech crowd, where reviewers often praised the hardware but questioned if it was really worth the \$999 USD MSRP.

Although Google is no longer manufacturing and selling the Pixelbook, used/refurbished ones can be found online for significantly cheaper than their list price. With a 12-inch display in a two-pound frame, a used Pixelbook could be a reasonable choice for those looking for an ultra-portable laptop (and are willing to do a bit of hacking).

Out of the box, it runs ChromeOS, a Linux-based operating system. Although ChromeOS is capable of running Linux (and Android!) applications, the Pixelbook can be convinced to run Gentoo natively.

## [Hardware specifications]

** Important**\
**Note the lack of USB-A ports!** To boot from a typical USB-A flash drive, some sort of USB-C adapter or hub will be necessary.

Not to be confused with the Pixelbook Go (2019), this particular model is usually referred to as the Kaby Lake or EVE model in ChromeOS communities.

-   **CPU**: Intel Core i5-7Y57 or i7-7Y75
    -   **Integrated graphics**: Intel HD 615
-   **RAM**: 8 or 16 GB
-   **Storage**: 128, 256, or 512 GB SSD
-   **Display**: 12.3 inches, 2400 x 1600 (3:2 aspect ratio), touchscreen
    -   The hinge bends a full 360 degrees, enabling the laptop to act as a tent or tablet
-   **Ports**
    -   2 USB-C (one on the left, one on the right \-- either can be used for charging)
    -   1 3.5mm (headphone) jack
-   **Connectivity**
    -   Wi-Fi
    -   Bluetooth
    -   Pixelbook Pen (is compatible with, but not included/sold separately)

## [Booting from USB]

Unfortunately, there are some prerequisite steps to booting from a USB on the Pixelbooks:

1.  (If necessary, such as when using a refurbished Pixelbook) Go through the first-time ChromeOS set up
2.  Enable developer mode
3.  Enable USB boot

### [Enable developer mode]

** Warning**\
Enabling developer mode will \"erase any state stored locally\", essentially performing a factory reset. If you were using ChromeOS, it would be wise to back up the files.

1.  Power off the Pixelbook (hold the Power button until the screen is black).
2.  Enter recovery mode (while holding [Escape]+[Refresh], press the power button).
3.  Enter developer mode with [Ctrl]+[D] and confirm that you want to disable OS verification.
4.  Wait for the device to configure developer mode. **This takes time \-- don\'t be surprised if you\'re waiting upwards of 45 minutes.**
    -   The device will beep a few times \-- twice when the procedure is started, and twice again when the procedure is finished.

### [Enable USB boot]

1.  On the \"Welcome to your Chromebook\" screen, press [Ctrl]+[Alt]+[Refresh] to enter the developer console.
2.  Log in with user \"chronos\" and no password.
3.  Enable USB boot with:

    :::: cmd-box


    `chronos@localhost ~ $``sudo crossystem dev_boot_usb=1 dev_boot_altfw=1`


    ::::
4.  Reboot with:

    :::: cmd-box


    `chronos@localhost ~ $``sudo reboot`


    ::::
5.  On the \"OS verification is OFF\" screen, press [Ctrl]+[L] to boot from USB. You might have to manually specify the \"gentoo\" kernel and screen mode/resolution when prompted by ISOLINUX.
    -   It is possible to use [Ctrl]+[U] and boot via UEFI, but the firmware on the Pixelbook will have to flashed. [See here for more information](https://mrchromebox.tech/#home).

Once booted, the Gentoo LiveCD *should* just work \-- Wi-Fi and display work immediately without any manual hacking or module probing, and the handbook can be followed to completion.

## [Installing Gentoo]

Once inside the Gentoo LiveCD, the [AMD64 Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") can be followed as usual for installing Gentoo, with some things to keep in mind:

### [Partitioning]

The default partition table on the Pixelbook will look similar to this (total size may vary based on hardware):

`root `[`#`]`fdisk -l /dev/nvme0n1`

    Device             Start        End   Sectors   Size Type
    /dev/nvme0n1p1  17092608 1000214527 983121920 468.8G Microsoft basic data
    /dev/nvme0n1p2     20480      53247     32768    16M ChromeOS kernel
    /dev/nvme0n1p3   8704000   17092607   8388608     4G ChromeOS root fs
    /dev/nvme0n1p4     53248      86015     32768    16M ChromeOS kernel
    /dev/nvme0n1p5    315392    8703999   8388608     4G ChromeOS root fs
    /dev/nvme0n1p6     16448      16448         1   512B ChromeOS kernel
    /dev/nvme0n1p7     16449      16449         1   512B ChromeOS root fs
    /dev/nvme0n1p8     86016     118783     32768    16M Microsoft basic data
    /dev/nvme0n1p9     16450      16450         1   512B ChromeOS reserved
    /dev/nvme0n1p10    16451      16451         1   512B ChromeOS reserved
    /dev/nvme0n1p11       64      16447     16384     8M unknown
    /dev/nvme0n1p12   249856     315391     65536    32M EFI System

More information on these partitions can be found in the [ChromiumOS \"Disk Format\" documentation](https://chromium.googlesource.com/chromiumos/docs/+/HEAD/disk_format.md#Drive-contents). Whether or not to keep the ChromeOS partitions is up to the user, but in the worst case scenario, it is possible to recover ChromeOS from a USB drive.

### [RW_LEGACY flashing]

** Important**\
Flashing RW_LEGACY is safe and will not brick your device, but you should still keep in mind that third-party scripts are involved here \-- Gentoo developers have nothing to do with these scripts.

(Technically, one doesn\'t need to do this to *install* Gentoo, but if a bootable system is desired, then this step is required.)

The factory legacy boot firmware for the Pixelbook is incapable of booting from the disk, but this can be fixed, even without any specific hardware/cables. The easiest way to do this is with [MrChromebox\'s Firmware Utility Script](https://mrchromebox.tech/#fwscript): run it from the Gentoo (or any) LiveCD with an active internet connection, and select option 1 \-- \"Install/Update RW_LEGACY Firmware\".

If one is only willing to flash RW_LEGACY and not the full firmware (the latter requires a specific cable to disable write protection), then keep in mind that **only legacy/BIOS boot will be possible** and any steps in the handbook regarding UEFI can be ignored. Also keep in mind that one of the partitions needs to be marked as \"BIOS Boot Partition\" for the GRUB installer to detect said partition.

### [][Genkernel and hardware support (a warning)]

Genkernel, if using the default kernel config, will produce a kernel that is capable of booting and thus can provide a system that *technically* works. However, a lot of the hardware usually taken for granted (e.g. touchpad, speakers) won\'t work. For this reason, it is strongly recommended to manually configure the kernel. Some subsections of \"Running Gentoo\" attempt to document which kernel modules/config options are necessary.

Should one struggle with getting a particular piece of hardware working, one viable (albeit tedious) method is to boot into a LiveUSB with a very generic kernel (i.e. one that supports a lot of hardware out of the box, such as Ubuntu Desktop) and use commands such as lspci, lsusb, lshw, and lsmod to determine which drivers are necessary for said piece of hardware.

## [Running Gentoo]

At this point, one will have a Gentoo installation that technically works but might not be practical or usable. This section attempts to document the issues one could likely encounter:

### [][Display scaling/DPI]

With so many pixels in such a small display, it is likely that the user will find everything far too small to comfortably read. The DPI can be adjusted with Xft.dpi in \~/.Xresources. The default setting is seemingly 96; multiply this number to increase the scaling. For example, a DPI of 96 \* 1.50 = 144 will scale most applications by 150%.

[FILE] **`~/.Xresources`**

    Xft.dpi: 144

Be sure to apply the changes with xrdb once done editing the file:

`user `[`$`]`xrdb ~/.Xresources`

For stubborn applications that don\'t respect this setting, the [Arch Linux Wiki\'s article on high-DPI displays](https://wiki.archlinux.org/title/HiDPI) might be helpful.

### [][Trackpad/touchpad and touchscreen]

The touchpad and touchscreen require CONFIG_I2C_HID_ACPI (and possibly CONFIG_CROS_EC_I2C).

[KERNEL] **I2C_HID_ACPI**

    Device Drivers  --->
        HID support  --->
            I2C HID support  --->
                <M> HID over I2C transport layer ACPI driver

### [Audio]

Audio very likely will not work out of the box. PulseAudio, for example, will not detect the speakers or microphone. To get audio working, one must configure the kernel as seen below *and* copy firmware from a ChromeOS recovery image.

#### [Kernel requirements]

If using Genkernel, the default kernel config already has this enabled. Otherwise, (at least) CONFIG_SND_SOC_INTEL_SKYLAKE is necessary.

[KERNEL] **SND_SOC_INTEL_SKYLAKE**

    Device Drivers  --->
        <M> Sound card support  --->
            <M> Advanced Linux Sound Architecture  --->
                <M> ALSA for SoC audio support  --->
                    [*]   Intel ASoC SST drivers
                        <M> All Skylake/SST Platforms

#### [Firmware requirements]

Download and unzip the latest EVE recovery image from [here](https://chromiumdash.appspot.com/serving-builds?deviceCategory=Chrome%20OS).

`user `[`$`]`curl -LO `[`https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_14989.107.0_eve_recovery_stable-channel_mp-v2.bin.zip`](https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_14989.107.0_eve_recovery_stable-channel_mp-v2.bin.zip)

`user `[`$`]`unzip chromeos_14989.107.0_eve_recovery_stable-channel_mp-v2.bin.zip`

Use kpartx (from [[[sys-fs/multipath-tools]](https://packages.gentoo.org/packages/sys-fs/multipath-tools)[]]) to create a device map with said firmware; this will map a bunch of loop devices.

`root `[`#`]`kpartx -av chromeos_14989.107.0_eve_recovery_stable-channel_mp-v2.bin`

    add map loop0p1 (254:0): 0 17858 linear 7:0 8740864
    add map loop0p2 (254:1): 0 65536 linear 7:0 20480
    add map loop0p3 (254:2): 0 8388608 linear 7:0 352256
    add map loop0p4 (254:3): 0 32768 linear 7:0 86016
    add map loop0p5 (254:4): 0 4096 linear 7:0 348160
    add map loop0p6 (254:5): 0 1 linear 7:0 16448
    add map loop0p7 (254:6): 0 1 linear 7:0 16449
    add map loop0p8 (254:7): 0 32768 linear 7:0 118784
    add map loop0p9 (254:8): 0 1 linear 7:0 16450
    add map loop0p10 (254:9): 0 1 linear 7:0 16451
    add map loop0p11 (254:10): 0 16384 linear 7:0 64
    add map loop0p12 (254:11): 0 65536 linear 7:0 282624

Mount ChromeOS\'s root filesystem (loop0p3).

`root `[`#`]`mount -o ro /dev/mapper/loop0p3 /mnt`

Copy the following firmware files from ChromeOS\'s filesystem to the Gentoo filesystem.

`root `[`#`]`cp /mnt/lib/firmware/9d71-GOOGLE-EVEMAX-0-tplg.bin /lib/firmware/`

`root `[`#`]`cp /mnt/lib/firmware/dsp_lib_dsm_core_spt_release.bin /lib/firmware/`

`root `[`#`]`cp /mnt/lib/firmware/intel/dsp_fw_C75061F3-F2B2-4DCC-8F9F-82ABB4131E66.bin /lib/firmware/intel/`

`root `[`#`]`mkdir -p /opt/google/dsm/ && cp /mnt/opt/google/dsm/dsmparam.bin /opt/google/dsm/`

Set up the ALSA UCM profiles by creating the following directories and copying the contents of the following files.

`root `[`#`]`mkdir -p /usr/share/alsa/ucm2/Intel/kbl-r5514-5663-/`

`root `[`#`]`mkdir -p /usr/share/alsa/ucm2/conf.d/kbl-r5514-5663-/`

Copy HiFi.conf from [HiFi.conf](https://wiki.gentoo.org/wiki/Google_Pixelbook_(2017)/HiFi.conf "Google Pixelbook (2017)/HiFi.conf") to [/usr/share/alsa/ucm2/Intel/kbl-r5514-5663-/HiFi.conf].

Save the configuration in [/usr/share/alsa/ucm2/Intel/kbl-r5514-5663-/kbl-r5514-5663-.conf]:

[FILE] **`/usr/share/alsa/ucm2/Intel/kbl-r5514-5663-/kbl-r5514-5663-.conf`**

    Syntax 3

    SectionUseCase."HiFi"

Symlink [kbl-r5514-5663-.conf]:

`root `[`#`]`cd /usr/share/alsa/ucm2/conf.d/kbl-r5514-5663-/`

`root `[`#`]`ln -sf ../../Intel/kbl-r5514-5663-/kbl-r5514-5663-.conf`

Reboot, and PulseAudio should see four output devices (HDMI 1 and 2, Headphones, Speaker) and two input devices (Headset Microphone and Internal Microphone).

### [Keyboard]

#### [Key remapping]

Coming from other laptops, the keyboard on the Pixelbook might behave a little unexpectedly:

-   The Assistant key (where the Windows/Super key usually sits) likely won\'t do anything at all.
-   The Search key (where Caps Lock usually sits) will likely act like a Super key.
-   The top row of \"icon\" keys between Escape and the Menu key will likely act as F1-10.

Udev can be used to rebind these keys. As an example, the following hwdb file will bind the icon keys to actions rather than function keys, the [Search] key to [Caps Lock], and the [Assistant] key to [Super].

[FILE] **`/etc/udev/hwdb.d/61-eve-keyboard.hwdb`**

    # Copyright 2017 The Chromium OS Authors. All rights reserved.
    # Distributed under the terms of the GNU General Public License v2
    #
    # Special keyboard mapping for Eve project. The keyboard has extra
    # "Assistant" and "Hamburger" keys.
    #
    evdev:atkbd:dmi:bvn*:bvr*:bd*:svnGoogle:pnEve:pvr*
     KEYBOARD_KEY_5d=delete
     KEYBOARD_KEY_d8=leftmeta
     KEYBOARD_KEY_db=capslock
     KEYBOARD_KEY_3b=back
     KEYBOARD_KEY_3c=f5
     KEYBOARD_KEY_3d=f11
     KEYBOARD_KEY_3e=print
     KEYBOARD_KEY_3f=brightnessdown
     KEYBOARD_KEY_40=brightnessup
     KEYBOARD_KEY_41=playpause
     KEYBOARD_KEY_42=mute
     KEYBOARD_KEY_43=volumedown
     KEYBOARD_KEY_44=volumeup

Once this file exists, update the database as described [here](https://wiki.gentoo.org/wiki/Udev#Remapping_keys_and_buttons "Udev") and reboot the PC.

#### [Backlight]

Ensure CONFIG_CROS_KBD_LED_BACKLIGHT is enabled in the kernel.

[KERNEL] **CROS_KBD_LED_BACKLIGHT**

    Device Drivers  --->
        [*] Platform support for Chrome hardware  --->
            <M> Backlight LED support for Chrome OS keyboards

The backlight brightness can then be adjusted by writing a value between 0 and 100 to [/sys/class/leds/chromeos::kbd_backlight/brightness]. Setting up a keyboard combination/shortcut to cycle through some backlight values is an exercise left to the reader, though some inspiration can be found [here](https://copr-dist-git.fedorainfracloud.org/cgit/jmontleon/pixelbook/pixelbook-scripts.git/tree/pixelbook-keyboard-backlight).

## [Troubleshooting]

### [Factory reset]

If you softbrick your Pixelbook or perhaps just want to go back to ChromeOS, [follow the steps here](https://support.google.com/pixelbook/answer/9134768) to perform a recovery.

### [][Flashing/blinking keyboard when attempting to boot]

If purchased used/refurbished, there is a reasonable chance that the battery is fully drained, and the laptop may react strangely to power-on attempts. In case you get an erratically flashing keyboard with no video output, try the following:

1.  Hold the Refresh key, then hold the Power button for 10 seconds (i.e. hold both buttons for a full 10 seconds).
2.  Release both buttons, and if the Pixelbook doesn\'t automatically start, press the Power button.