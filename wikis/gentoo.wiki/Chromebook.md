[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Chromebook&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Chromebook "wikipedia:Chromebook")

This guide details the generic part of installing Gentoo on a Chromebook.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [ARM]](#ARM)
    -   [[1.2] [x86]](#x86)
        -   [[1.2.1] [Installation relying on custom firmware]](#Installation_relying_on_custom_firmware)
            -   [[1.2.1.1] [Disabling hardware write protection]](#Disabling_hardware_write_protection)
            -   [[1.2.1.2] [Enabling Developer Mode]](#Enabling_Developer_Mode)
            -   [[1.2.1.3] [Flashing the custom firmware]](#Flashing_the_custom_firmware)
-   [[2] [Keyboard]](#Keyboard)
    -   [[2.1] [Xorg]](#Xorg)
        -   [[2.1.1] [Layout]](#Layout)
        -   [[2.1.2] [Missing keys]](#Missing_keys)
        -   [[2.1.3] [Extra keys]](#Extra_keys)
        -   [[2.1.4] [Multimedia keys]](#Multimedia_keys)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Sound does not work]](#Sound_does_not_work)
    -   [[3.2] [How to reboot]](#How_to_reboot)
    -   [[3.3] [Stuck at the warning screen]](#Stuck_at_the_warning_screen)
    -   [[3.4] [Unexpected reboot when coming out of suspend to RAM]](#Unexpected_reboot_when_coming_out_of_suspend_to_RAM)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

** Tip**\
Check [Category:Chromebooks](https://wiki.gentoo.org/wiki/Category:Chromebooks "Category:Chromebooks") first, as some pages may contain additional installation methods.

### [ARM]

Check [ASUS Chromebook C201/Installing_Gentoo](https://wiki.gentoo.org/wiki/ASUS_Chromebook_C201/Installing_Gentoo "ASUS Chromebook C201/Installing Gentoo").

### [x86]

There are two main ways to run Gentoo Linux on a Chromebook - relying on stock firmware or relying on custom firmware. By default, all Chromebooks use Chrome OS (stock) firmware, which varies by Chromebook generation and processor architecture. Depending on the stock firmware, a Chromebook may be able to boot another operating system without the need to flash a custom firmware. ^[\[1\]](#cite_note-1)^ The stock firmware should only be used in case if there is a plan to use Chrome OS or if there is no custom firmware for the Chromebook. The reason is that all Chrome OS devices have an **expiration date**. After the expiration date, the stock firmware will not receive **security** updates or **bug** fixes.

#### [Installation relying on custom firmware]

** Warning**\
Flashing custom firmware may result in **damage** to the hardware or **loss of data**.

Flashing requires disabling hardware write protection and enabling developer mode.

##### [Disabling hardware write protection]

** Warning**\
Disabling hardware write protection requires physical interaction with the motherboard (except when using SuzyQable). There have been cases of people unknowingly **damaging** the motherboard. ^[\[2\]](#cite_note-2)^ Therefore, it is very important to find an official manual from the manufacturer that tells how to open the Chromebook.

Depending on the model, there are five possible ways to disable hardware write protection:

-   screw
-   jumper
-   switch
-   [CR50] (battery removal or SuzyQable)
-   [CR50] (SuzyQable)

To find the appropriate method for a certain Chromebook model, [MrChromebox\'s table](https://mrchromebox.tech/#devices) can be used, or in the case of SuzyQable, [another table](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices). It is important to keep in mind that some models have incorrect [CR50] implementation, for them SuzyQable will not work, only battery removal (or soldering). ^[\[3\]](#cite_note-3)^

##### [Enabling Developer Mode]

** Warning**\
Enabling developer mode will **wipe** all existing **data** on the disk.

To enable developer mode, follow instructions provided [here](https://mrchromebox.tech/#devmode).

##### [Flashing the custom firmware]

** Warning**\
There\'s a chance that the Chromebook will turn into a **brick**.

See [MrChromebox\'s Firmware Utility Script](https://wiki.gentoo.org/wiki/MrChromebox%27s_coreboot#Firmware_Utility_Script "MrChromebox's coreboot").

After flashing the UEFI firmware, installing Gentoo is rather straightforward: boot on a liveUSB and follow the [Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") as if installing on a regular machine.

## [Keyboard]

### [Xorg]

#### [Layout]

The layout is supported by Xorg:

[FILE] **`/etc/X11/xorg.conf.d/10-keyboard.conf`**

    Section "InputClass"
      Identifier "Keyboard"
      MatchProduct "AT Translated Set 2 keyboard"
      MatchIsKeyboard "on"
      Option "XkbModel" "chromebook"
    EndSection

The `MatchProduct` section might not fit the hardware, to check the correct name, use:

`user `[`$`]`grep "Using input driver" /var/log/Xorg.0.log`

    (...)
    [617682.560] (II) Using input driver 'libinput' for 'AT Translated Set 2 keyboard'
    (...)

#### [Missing keys]

Since some keys are missing, they are emulated with [Right Alt]:

-   [Right Alt]+[Backspace] = [Delete]
-   [Right Alt]+[Left] = [Home]
-   [Right Alt]+[Right] = [End]
-   [Right Alt]+[Up] = [PgUp]
-   [Right Alt]+[Down] = [PgDn]
-   [Right Alt]+[Search] = [Caps Lock]
-   [Right Alt]+[F1 to F10] = [F1 to F10]

#### [Extra keys]

[Search] is treated as a super key (Super_L)

#### [Multimedia keys]

The multimedia keys should works as expected, except:

-   [fullscreen] (in the F4 spot) will be treated as [F11]
-   [next tab/window] (in the F5 spot) will be treated as [F5]

When used with [Ctrl] or [Alt] or [Shift], these keys will behave as [F1] to [F10].

Example: [Alt]+[Refresh] = [Alt]+[F3]

## [Troubleshooting]

### [Sound does not work]

Check [this article](https://wiki.gentoo.org/wiki/Chromebook/Sound_configuration "Chromebook/Sound configuration").

### [How to reboot]

Since there is typically no [Delete] key, it\'s usually impossible to use [Ctrl]+[Alt]+[Delete]. There is also no [Sys] key, making it impossible to use the Magic Keys.

Fortunately the firmware has a few keyboard shortcuts available:

-   [Power] for several seconds = power off
-   [Refresh]+[Power] = instant reboot

### [Stuck at the warning screen]

Try using [Esc]+[Refresh]+[Power] to force a firmware reset

** Warning**\
Entering or leaving Developer Mode will completely erase the Chromebook\'s disk drive! Proceed with this caution in mind!

If that is not enough, follow the [official procedure](https://support.google.com/chromebook/answer/1080595)

### [Unexpected reboot when coming out of suspend to RAM]

This can be caused by a missing TPM (Trusted Platform Module) driver in the kernel, see in Drivers → Character Devices

## [See also]

-   [MrChromebox\'s coreboot](https://wiki.gentoo.org/wiki/MrChromebox%27s_coreboot "MrChromebox's coreboot") --- a [coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") fork maintained by one of the coreboot leaders

## [External resources]

-   [MrChromebox - Firmwares and firmware flashing tool](https://mrchromebox.tech/)
-   [Chrultrabook - A useful resource for converting your Chromebook to linux](https://docs.chrultrabook.com/)
-   [GalliumOS - Linux distribution for Chromebooks](https://wiki.galliumos.org/Welcome_to_the_GalliumOS_Wiki)
-   [Arch Linux Wiki - Similar page on the Arch Linux Wiki](https://wiki.archlinux.org/index.php/Chrome_OS_devices)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://wiki.galliumos.org/Firmware](https://wiki.galliumos.org/Firmware)]]
2.  [[[↑](#cite_ref-2)] [[https://www.reddit.com/r/chromeos/comments/12mhft4/chromebook_wont_start_after_disconnecting_battery/](https://www.reddit.com/r/chromeos/comments/12mhft4/chromebook_wont_start_after_disconnecting_battery/)]]
3.  [[[↑](#cite_ref-3)] [[https://www.sparkfun.com/products/retired/14746](https://www.sparkfun.com/products/retired/14746)]]