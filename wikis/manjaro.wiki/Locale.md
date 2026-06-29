Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Locale/tr "Yerel ayar (14% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Locale/ru "Языковые пакеты (100% translated)")

## Contents

-   [[1] [Locale]](#Locale)
    -   [[1.1] [System]](#System)
    -   [[1.2] [User]](#User)
    -   [[1.3] [Console fonts]](#Console_fonts)
    -   [[1.4] [Troubleshooting]](#Troubleshooting)
    -   [[1.5] [References]](#References)

# [Locale]

The locale is all the settings related to localization, like language, time, currency etc. In Manjaro you can set the desired locale settings with [Manjaro Settings Manager](//wiki.manjaro.org/index.php?title=Manjaro_Settings_Manager "Manjaro Settings Manager") GUI application. Sometimes, because of complicated setups and often after some user mistakes, you might not be able to have the correct settings for each user. Below you will see how you can check and set properly your configuration manually.

In Linux systems all locales are available for installation, they just need to be enabled and generated. The settings are configured initially system-wide, but it is possible to override them for user-session.

## [System]

Check your current system settings (type in terminal)

     locale

Check which are already active

     locale -a

If your locale is not listed, you must edit **/etc/locale.gen** and uncomment yours. In example **LANG=zh_TW.UTF-8**

    # zh_SG.UTF-8 UTF-8
    # zh_TW BIG5
    # zh_TW.EUC-TW EUC-TW
    zh_TW.UTF-8 UTF-8
    # zu_ZA ISO-8859-1

You may want to uncomment all the variations of your country code \"zh_TW\" to use them as fallbacks for some programs they might use them. Then, generate them with this command

    sudo locale-gen

Now you can set the system locale with this

    sudo localectl set-locale LANG=zh_TW.UTF-8

The settings are set in the system file **/etc/locale.conf**. You don\'t need to manually edit this file unless you are having troubles. Here is a sample

     LANG=zh_TW.UTF-8
     LANGUAGE=zh_TW:en_AU
     LC_ADDRESS=en_AU.UTF-8
     LC_IDENTIFICATION=en_AU.UTF-8
     LC_MEASUREMENT=en_AU.UTF-8
     LC_MONETARY=en_AU.UTF-8
     LC_MESSAGES=zh_TW.UTF-8
     LC_NAME=en_AU.UTF-8
     LC_NUMERIC=en_AU.UTF-8
     LC_PAPER=en_AU.UTF-8
     LC_TELEPHONE=en_AU.UTF-8
     LC_TIME=en_AU.UTF-8

## [User]

The system locale can be overriden for a user that wants a different locale language by creating (or editing if it already exists) a file named \`.xprofile\` in the home folder \`/home/USERNAME/.xprofile\`. Edit it with any user specific locale settings as below. This sample illustrates how to set Traditional Chinese as the UI language while keeping Australian English for the formats.

    # Set display language to zh_TW and gcin as default IM
    export LANG=zh_TW.UTF-8
    export LANGUAGE=zh_TW:en_AU
    export LC_MESSAGES=zh_TW.UTF-8
    export LC_CTYPE=zh_TW.UTF-8
    export XMODIFIERS=@im=gcin
    export GTK_IM_MODULE=gcin
    export QT_IM_MODULE=gcin
    export XIM_MODULE=gcin

## [Console fonts]

The file **vconsole.conf** holds information on your keyboard layout and the font displayed in the TTY - the physical console.

Here is a sample setup for danish keyboard and font.

    KEYMAP=dk
    FONT=ter-118n

## [Troubleshooting]

If you have followed the above guide and still have issues, there are possibilities of other files conflicting. Xorg, GDM and Plasma may have overriden your settings. The authoritative Archlinux wiki for locale is an excellent place to look for a solution and of course the Manjaro Forum is always the more welcoming community.

Archlinux wiki is an ultimate source of Linux related information.

Just remember that Arch is not Manjaro so **please ask Manjaro questions in the Manjaro forum**.

## [References]

Arch Linux Wiki - [Locale](https://wiki.archlinux.org/index.php/locale), [Xprofile](https://wiki.archlinux.org/index.php/Xprofile)