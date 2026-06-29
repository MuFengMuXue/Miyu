This page contains [[changes](https://wiki.gentoo.org/index.php?title=St&diff=1285879)] which are not marked for translation.

**Resources**

[[]][Home](http://st.suckless.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/st)

\
**st** is an extremely minimal [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") for the X environment made by the [suckless.org](https://suckless.org/) community. [st] is configured by editing [C](https://en.wikipedia.org/wiki/C_(programming_language) "wikipedia:C (programming language)") source code header files, and recompiling. The suckless website states that the project ***focuses on advanced and experienced computer users***.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Patches and additional features]](#Patches_and_additional_features)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Keyboard]](#Keyboard)
        -   [[3.1.1] [Delete key is not working properly]](#Delete_key_is_not_working_properly)

## [Installation]

### [USE flags]

### [USE flags for] [x11-terms/st](https://packages.gentoo.org/packages/x11-terms/st) [[]] [Simple terminal implementation for X]

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)   Use this to restore your config from /etc/portage/savedconfig \$/\$. Make sure your USE flags allow for appropriate dependencies
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-01 09:47] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Preferably, [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig) USE flag can be enabled and save a customized configuration file to [/etc/portage/savedconfig/x11-terms/st] for later editing pleasure.

`root `[`#`]`euse --enable savedconfig`

### [Emerge]

Install [[[x11-terms/st]](https://packages.gentoo.org/packages/x11-terms/st)[]]:

`root `[`#`]`emerge --ask x11-terms/st`

## [Configuration]

** Important**\
If installed without the [`savedconfig`](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") USE flag, upon recompilation custom settings stored in [/etc/portage/savedconfig/x11-terms/st] will be lost after [dispatch-conf] (depending on chosen option).

As stated previously, the main [st] configuration file is the [[/etc/portage/savedconfig](https://wiki.gentoo.org/wiki//etc/portage/savedconfig "/etc/portage/savedconfig")/x11-terms/st] file and after each change, [st] needs to be recompiled for any changes to take effect.

### [Patches and additional features]

There are many user-created [patches](http://st.suckless.org/patches/) available from the official site that greatly extend the functionality of [st]. See [/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches") on how to apply these patches automatically.

## [Troubleshooting]

### [Keyboard]

#### [Delete key is not working properly]

Add following to the [/etc/inputrc] to make a system-wide change:

[FILE] **`/etc/inputrc`**

    set enable-keypad on

Or to the relative user\'s [\~/.inputrc] file:

[FILE] **`~/.inputrc`**

    $include /etc/inputrc
    set enable-keypad on