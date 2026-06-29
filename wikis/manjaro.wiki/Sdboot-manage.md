Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Systemd-boot/de "Systemd-boot (62% translated)") • ‎[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Systemd-boot/tr "Systemd-boot (15% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Systemd-boot/ru "Systemd-boot (100% translated)")

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Customizing entries]](#Customizing_entries)
    -   [[1.2] [Setting up Plymouth splash screen]](#Setting_up_Plymouth_splash_screen)
    -   [[1.3] [Further configuration]](#Further_configuration)
-   [[2] [See Also]](#See_Also)

\
systemd-boot is an alternative to other bootloaders such as GRUB.

## [Configuration]

### [Customizing entries]

The entries in the bootloader are automatically generated using sdboot-manage. The generated entries can be customized by editing `/etc/sdboot-manage.conf`.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **/etc/sdboot-manage.conf**                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::  |
| /etc/sdboot-manage.conf                                                                                                                                                                                                                                                                                           |
| :::                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| :::                                                       |
|     # config file for sdboot-manage                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
|     # kernel options to be appended to the "options" line                                                                                                                                                                                                                                                         |
|     #LINUX_OPTIONS=""                                                                                                                                                                                                                                                                                             |
|     #LINUX_FALLBACK_OPTIONS=""                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                   |
|     # when LINUX_USE_DEVICE_FOR_RESUME is set to "yes", the specified device will be used for hibernation                                                                                                                                                                                                         |
|     #LINUX_USE_DEVICE_FOR_RESUME=/dev/sda4                                                                                                                                                                                                                                                                        |
|     #LINUX_USE_DEVICE_FOR_RESUME=UUID=device_uuid                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                   |
|     # when LINUX_USE_SWAP_FOR_RESUME is set to "yes", the first detected available swap device will be used for hibernation                                                                                                                                                                                       |
|     # i.e. the "resume=UUID=swap_device" parameter would be appended to the kernel command line                                                                                                                                                                                                                   |
|     #LINUX_USE_SWAP_FOR_RESUME="no"                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
|     # the DEFAULT_ENTRY option determines if and how the default entry in loader.conf should be managed                                                                                                                                                                                                           |
|     #   "latest"    The most recent Manjaro kernel will be used(the one with the highest version number)                                                                                                                                                                                                          |
|     #   "oldest"    The oldest Manjaro kernel will be used(the one with the lowest version number)                                                                                                                                                                                                                |
|     #   "manual"    Don't modify the default setting                                                                                                                                                                                                                                                              |
|     #DEFAULT_ENTRY="latest"                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                   |
|     # ENTRY_ROOT is a template that describes the beginning of the name for system-boot entries                                                                                                                                                                                                                   |
|     # The ENTRY_ROOT will be followed by the kernel version number                                                                                                                                                                                                                                                |
|     # For example, if ENTRY_ROOT="manjaro" and you are using kernel 4.19 your entry will be named "manjaro4.19.conf"                                                                                                                                                                                              |
|     #ENTRY_ROOT="manjarolinux"                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                   |
|     # ENTRY_TITLE is a template that describes the beginning of the title of (i.e. the text displayed in the loader screen for) systemd-boot entries                                                                                                                                                              |
|     # For example, if ENTRY_TITLE="Manjaro" and you are using kernel 4.19, the title of your entry will be "Manjaro Linux 4.19"                                                                                                                                                                                   |
|     #ENTRY_TITLE="Manjaro Linux"                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                   |
|     # when ENTRY_APPEND_KVER is set to "yes", the kernel version number will be appended to both the filename and the title of systemd-boot entries                                                                                                                                                               |
|     #ENTRY_APPEND_KVER="yes"                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                   |
|     # Use this pattern to match kernels which should be considered native OS kernels                                                                                                                                                                                                                              |
|     #KERNEL_PATTERN="vmlinuz-[0-9]*-*" \                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
|     # setting REMOVE_EXISTING to "yes" will remove all your existing systemd-boot entries before building new entries                                                                                                                                                                                             |
|     #REMOVE_EXISTING="yes"                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
|     # unless OVERWRITE_EXISTING is set to "yes" existing entries for currently installed kernels will not be touched                                                                                                                                                                                              |
|     # this setting has no meaning if REMOVE_EXISTING is set to "yes"                                                                                                                                                                                                                                              |
|     #OVERWRITE_EXISTING="no"                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                   |
|     # when REMOVE_OBSOLETE is set to "yes" entries for kernels no longer available on the system will be removed                                                                                                                                                                                                  |
|     #REMOVE_OBSOLETE="yes"                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
|     # if PRESERVE_FOREIGN is set to "yes", do not delete entries starting with $ENTRY_ROOT                                                                                                                                                                                                                        |
|     #PRESERVE_FOREIGN="no"                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
|     # setting NO_AUTOUPDATE to "yes" will stop the updates to systemd-boot when systemd is updated - not recommended unless you are seperately updating systemd-boot                                                                                                                                              |
|     #NO_AUTOUPDATE="no"                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                   |
|     # setting NO_AUTOGEN to "yes" will stop the automatic creation of entries when kernels are installed or updated                                                                                                                                                                                               |
|     #NO_AUTOGEN="no"                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
|     # add discard option to cryptdevice parameters                                                                                                                                                                                                                                                                |
|     #DISCARD="no"                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                   |
|     # add discard option to boot parameters for filesystems (rootflags=discard) for continuous TRIM                                                                                                                                                                                                               |
|     # see: https://wiki.archlinux.org/index.php/Solid_state_drive#Continuous_TRIM                                                                                                                                                                                                                                 |
|     #CDISCARD="no"                                                                                                                                                                                                                                                                                                |
| :::                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

After changing this file, the existing entries need to be regenerated.

[user \$ ][ sudo sdboot-manage gen [COPY TO CLIPBOARD]]

\

### [Setting up Plymouth splash screen]

After installing Plymouth the kernel bootline needs to be adjusted. This can be done by editing `/etc/sdboot-manage.conf` as follows:

Find the line

    #LINUX_OPTIONS=""

and replace it with

    LINUX_OPTIONS="quiet splash loglevel=3 rd.udev.log_priority=3 vt.global_cursor_default=0"

### [Further configuration]

For further configuration such as custom entries, refer to [ArchWiki](https://wiki.archlinux.org/title/Systemd-boot).

# [See Also]

[systemd-boot on ArchWiki](https://wiki.archlinux.org/title/systemd-boot) For a more complete article about systemd-boot.

[dalto.8/systemd-boot-manager on GitLab](https://gitlab.com/dalto.8/systemd-boot-manager/-/tree/master) For the automatic generators source code.

[man systemd-boot.7](https://man.archlinux.org/man/systemd-boot.7) The man-page for systemd-boot.