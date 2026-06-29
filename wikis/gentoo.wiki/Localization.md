This page contains [[changes](https://wiki.gentoo.org/index.php?title=Localization&oldid=1225161&diff=1325572)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Localization/es "Localización (82% translated)")
-   [français](https://wiki.gentoo.org/wiki/Localization/fr "Localisation (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Localization/hu "Nyelvterület-beállítások (lokalizáció) (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Localization/ru "Локализация (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Localization/ja "地域化 (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Internationalization_and_localization "wikipedia:Internationalization and localization")

[[]][Guide](https://wiki.gentoo.org/wiki/Localization/Guide "Localization/Guide")

When dealing with GNU/Linux systems in an international context or for a specific country or region, both localization (abbreviated to *[l10n](https://en.wikipedia.org/wiki/Language_localisation "wikipedia:Language localisation")*) and internationalization (abbreviated to *[i18n](https://en.wikipedia.org/wiki/Internationalization_and_localization "wikipedia:Internationalization and localization")*) play an important part. It allows administrators and users to select the language of choice on the platform, timezone selection, character ordering and more.

In Gentoo Linux, localization is supported in various levels ranging from kernel support up to end user application support.

The handbook explains [locale setup](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Configure_locales "Handbook:AMD64/Installation/Base") during installation.

## Contents

-   [[1] [Localization in GNU/Linux]](#Localization_in_GNU.2FLinux)
    -   [[1.1] [Linux kernel]](#Linux_kernel)
    -   [[1.2] [Core system]](#Core_system)
    -   [[1.3] [Package manager]](#Package_manager)
        -   [[1.3.1] [Portage]](#Portage)
    -   [[1.4] [Graphical environments]](#Graphical_environments)

## [][Localization in GNU/Linux]

Localization plays a part in many layers of a GNU/Linux system.

### [Linux kernel]

In the Linux kernel, localization is enabled through the *Native Language Support* setting as exemplified by the [UTF-8 article](https://wiki.gentoo.org/wiki/UTF-8#Application_support "UTF-8").

### [Core system]

On the core system level (C libraries and affiliated tools), most localization is handled through the [locale system](https://wiki.gentoo.org/wiki/Localization/Guide#Locale_system "Localization/Guide") and [console keyboard layout](https://wiki.gentoo.org/wiki/Localization/Guide#Keyboard_layout_for_the_console "Localization/Guide") which are described well in the [Gentoo Localization Guide](https://wiki.gentoo.org/wiki/Localization/Guide "Localization/Guide") article.

### [Package manager]

#### [Portage]

Portage respects the `USE_EXPAND` variable called `L10N` in [/etc/portage/]:

[FILE] **`/etc/portage/package.use/localization`L10N assignment**

    */* L10N: en en-US

### [Graphical environments]

For the graphical environments, Xorg honors the locale settings, but has its own method for selecting the [keyboard layout for the X server](https://wiki.gentoo.org/wiki/Localization/Guide#Keyboard_layout_for_the_X_server "Localization/Guide"). The desktop environments on top, such as [KDE](https://wiki.gentoo.org/wiki/KDE#Localization "KDE") and [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME"), might have additional steps you have to go through in order to enable the localization and internationalization settings correctly.