Other languages:

[English] • ‎[français](//wiki.manjaro.org/index.php?title=Plymouth/fr "Plymouth (96% translated)") • ‎[Ελληνικά](//wiki.manjaro.org/index.php?title=Plymouth/el "Plymouth/el (12% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Plymouth/ru "Plymouth (100% translated)")

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Removal]](#Removal)
-   [[4] [See Also]](#See_Also)

Plymouth is an application that runs very early in the boot process (even before the root filesystem is mounted) that provides a graphical boot animation while the boot process happens in the background.

\

## [Installation]

Plymouth is available from the Manjaro repositories. However, some steps need to be followed to set it up properly.

The steps from [https://wiki.archlinux.org/index.php/Plymouth#Installation](https://wiki.archlinux.org/index.php/Plymouth#Installation) apply, except the last step.

When rebuilding the initrd image, the \"linux\" preset does not exist. Use the one that corresponds to you kernel version:

    sudo mkinitcpio -p linux<version>

If you do not know what value to use, look in the `/etc/mkinitcpio.d` directory. It contains all available presets (files with the .preset extension). For example:

[user \$ ][ sudo mkinitcpio -p linux419 [COPY TO CLIPBOARD]]

\

Note that in order to enable Plymouth on boot you must edit `/etc/default/grub` and add the word \"*splash*\" to the list of arguments for the following line, as shown:

    GRUB_CMDLINE_LINUX_DEFAULT="quiet"

    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"

Make sure not to remove anything else that may already be there.

## [Configuration]

See [https://wiki.archlinux.org/index.php/Plymouth#Configuration](https://wiki.archlinux.org/index.php/Plymouth#Configuration)

## [Removal]

4 or 5 steps are needed to remove Plymouth. They are:

-   Remove plymouth hook from */etc/mkinitcpio.conf* (For disk encryption users should encrypt)

<!-- -->

-   Regenerate the initramfs for your kernel with **sudo mkinitcpio -p linux\<version\>**

<!-- -->

-   Remove the word splash & quiet from the Grub command line options via editing */etc/default/grub*

<!-- -->

-   Update Grub config file with

    :::
    [user \$ ][ sudo grub-mkconfig -o /boot/grub/grub.cfg [COPY TO CLIPBOARD]]
    :::

\

-   ~~Configure display manager~~:
    -   ~~[For Xfce](https://classicforum.manjaro.org/index.php?topic=14213.msg128429#msg128429)~~ (broken link)
    -   ~~[For KDE, replacing kdm with sddm for most newer installs, and systemctl can generally be successful without sudo](https://classicforum.manjaro.org/index.php?topic=14213.msg139844#msg139844)~~.(broken link)

<!-- -->

-   After that the plymouth package and its themes can be removed. For example:

[user \$ ][ sudo pacman -Rsn plymouth plymouth-theme-manjaro [COPY TO CLIPBOARD]]

\

## [See Also]

-   [https://wiki.archlinux.org/index.php/Plymouth](https://wiki.archlinux.org/index.php/Plymouth)