[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Signal_Desktop&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://signal.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-im/signal-desktop-bin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Signal_(software) "wikipedia:Signal (software)")

[[]][GitHub](https://github.com/WhisperSystems/Signal-Desktop)

**Signal Desktop** is a messaging application geared towards privacy. It is endorsed by Edward Snowden.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Language Selection and Spell Checking]](#Language_Selection_and_Spell_Checking)
    -   [[2.2] [System tray]](#System_tray)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Failed to map segment from shared object]](#Failed_to_map_segment_from_shared_object)
    -   [[3.2] [Unable to add attachments due to File Chooser not opening]](#Unable_to_add_attachments_due_to_File_Chooser_not_opening)
-   [[4] [Removal]](#Removal)

## [Installation]

### [USE flags]

### [USE flags for] [net-im/signal-desktop-bin](https://packages.gentoo.org/packages/net-im/signal-desktop-bin) [[]] [Allows you to send and receive messages of Signal Messenger on your computer]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-12 06:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-im/signal-desktop-bin]](https://packages.gentoo.org/packages/net-im/signal-desktop-bin)[]]:

`root `[`#`]`emerge --ask net-im/signal-desktop-bin`

## [Usage]

### [Language Selection and Spell Checking]

Signal respects the `LANGUAGE` environment variable, which takes a colon-separated list of locale names. All entries will be used for spell checking. Additionally, the first entry defines the UI language, overriding any setting in preferences. The debug log, accessible via View \> Debug Log, lists all supported locales.

The following snippet launches Signal with an English user interface and spell checking in English and German:

`user `[`$`]`LANGUAGE=en_US:de_DE signal-desktop`

### [System tray]

Use one of these commands to open Signal in focus and remain in the system tray, when you close it, or start minimized in the tray:

`user `[`$`]`signal-desktop --use-tray-icon`

`user `[`$`]`signal-desktop --start-in-tray`

## [Troubleshooting]

### [Failed to map segment from shared object]

It is possible to get the following error when starting [signal-desktop] if [/tmp] has been mounted with the `noexec` mount option:

    Uncaught error or unhandled promise rejection: Error: /tmp/.org.chromium.Chromium.xxxxxx: failed to map segment from shared object

To solve the issue remount [/tmp] without the execution restriction:

`root `[`#`]`mount -o remount,exec /tmp`

In order to make the change persist across reboots, it will also be needed to remove the option from [/etc/fstab].

### [Unable to add attachments due to File Chooser not opening]

If selecting the \"Add attachment\" icon (the \'paperclip\' icon) has no effect, and doesn\'t open a File Chooser dialog, ensure that a [xdg-desktop-portal](https://wiki.gentoo.org/wiki/Xdg-desktop-portal "Xdg-desktop-portal") frontend implementing the FileChooser interface is installed (e.g. [[[sys-apps/xdg-desktop-portal-gtk]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gtk)[]]) and that [xdg-desktop-portal] is configured to use it, via [\$XDG_CONFIG_DIR/xdg-desktop-portal/portals.conf]:

[FILE] **`~/$XDG_CONFIG_DIR/xdg-desktop-portal/portals.conf`**

    [preferred]
    default=wlr;gtk;gnome
    org.freedesktop.impl.portal.FileChooser=gtk

## [Removal]

Uninstall Signal Desktop by issuing:

`root `[`#`]`emerge --ask --depclean net-im/signal-desktop-bin`