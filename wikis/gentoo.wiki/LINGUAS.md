This page contains [[changes](https://wiki.gentoo.org/index.php?title=Localization/Guide&oldid=1400316&diff=1441142#LINGUAS)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Localization/Guide/de "Lokalisierungs-Leitfaden (96% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Localization/Guide/es "Localización/Guía (72% translated)")
-   [français](https://wiki.gentoo.org/wiki/Localization/Guide/fr "Guide de localisation (50% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Localization/Guide/it "Localizzazione/Guida (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Localization/Guide/hu "Nyelvterület beállítása / Útmutató (100% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Localization/Guide/pt-br "Localização/Guia (6% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/Localization/Guide/cs "Lokalizace/HOWTO (39% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Localization/Guide/ru "Руководство по локализации (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Localization/Guide/zh-cn "本地化/指南 (84% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Localization/Guide/ja "地域化/ガイド (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Localization/Guide/ko "Localization/Guide/ko (55% translated)")

## Contents

-   [[1] [Time zone]](#Time_zone)
-   [[2] [Locale system]](#Locale_system)
    -   [[2.1] [What are locales?]](#What_are_locales.3F)
    -   [[2.2] [Environment variables for locales]](#Environment_variables_for_locales)
    -   [[2.3] [Generating specific locales]](#Generating_specific_locales)
    -   [[2.4] [Setting a locale]](#Setting_a_locale)
        -   [[2.4.1] [OpenRC]](#OpenRC)
        -   [[2.4.2] [systemd]](#systemd)
-   [[3] [Keyboard layout for the console]](#Keyboard_layout_for_the_console)
    -   [[3.1] [OpenRC]](#OpenRC_2)
    -   [[3.2] [systemd]](#systemd_2)
-   [[4] [Keyboard layout for the X server]](#Keyboard_layout_for_the_X_server)
    -   [[4.1] [OpenRC]](#OpenRC_3)
    -   [[4.2] [systemd]](#systemd_3)
-   [[5] [Native Language Support]](#Native_Language_Support)
-   [[6] [LINGUAS]](#LINGUAS)
-   [[7] [L10N]](#L10N)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)
-   [[10] [References]](#References)

## [Time zone]

In order to keep the system time properly according to the present location, the timezone needs to be set. Instructions how to do this for [OpenRC based systems](https://wiki.gentoo.org/wiki/System_time#OpenRC "System time") and [systemd based systems](https://wiki.gentoo.org/wiki/System_time#systemd "System time") can be found in the [system time](https://wiki.gentoo.org/wiki/System_time "System time") article.

## [Locale system]

### [][What are locales?]

A locale is a set of information that most programs use for determining country and language specific settings. The locales and their data are part of the system library and can be found under the [/usr/share/i18n/locales/] directory on most systems. A locale name is generally named `ab_CD` where `ab` is the two (or three) letter language code (as specified in [ISO-639](https://en.wikipedia.org/wiki/ISO_639 "wikipedia:ISO 639")) and `CD` is the two letter country code (as specified in [ISO-3166](https://en.wikipedia.org/wiki/ISO_3166 "wikipedia:ISO 3166")). Variants like `@euro` or `@latin` are often appended to locale names, e.g. `de_DE@euro` or `nan_TW@latin`. Please explore [Wikipedia](https://en.wikipedia.org/wiki/Locale_(computer_software) "wikipedia:Locale (computer software)") to read more about locales and related articles.

### [Environment variables for locales]

The variables controlling different aspects of locale settings are given in the table below. All of them take one name of a locale in `ab_CD` format given above.

  -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Variable name              Explanation
  `LANG`          Defines all locale settings at once, while allowing further individual customization via the LC\_\* settings below.
  `LC_COLLATE`    Define alphabetical ordering of strings. This affects e.g. output of sorted directory listings.
  `LC_CTYPE`      Define the character-handling properties for the system. This determines which characters are seen as alphabetic, numeric, and so on. This also determines the character set used, if applicable.
  `LC_MESSAGES`   Programs\' localizations stored in [/usr/share/locale/] for applications that use a message-based localization scheme (the majority of GNU programs).
  `LC_MONETARY`   Defines currency units and formatting of currency-type numeric values.
  `LC_NUMERIC`    Defines formatting of numeric values which aren\'t monetary. Affects things such as thousand separator and decimal separator.
  `LC_TIME`       Defines formatting of dates and times.
  `LC_PAPER`      Defines default paper size.
  `LC_ALL`        Overrides all other settings.
  -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

** Note**\
Some programs are written in such a way that they expect traditional English ordering of the alphabet, while some locales, most notably the Estonian one, use a different ordering. Therefore it\'s recommended to explicitly set `LC_COLLATE` to C when dealing with system-wide settings.

** Warning**\
Using `LC_ALL` is strongly discouraged as it automatically overrides all other `LC_*` variables (`LANG` is not affected). This means that changes made by other means will be hidden until `LC_ALL` is set to a null string. It is probably best not to set it in a startup file.

Most typically, users only set the `LANG` variable globally.

### [Generating specific locales]

Most users will probably only use one or maybe two locales on their system. How additional locales can be specified is explained in the [/etc/locale.gen] file.

[CODE] **Adding locales to /etc/locale.gen**

    en_GB # Defaults to UTF-8 if not further specified
    en_GB ISO-8859-1
    de_DE ISO-8859-1
    de_DE@euro ISO-8859-15

** Note**\
Use an `@euro` value from [/usr/share/i18n/SUPPORTED] as the locale when using the Euro currency symbol (€) on non UTF-8 based locales.

** Note**\
As of version 3.10, the [/etc/locale.gen] config file grammar has been simplified. For instance, \"en_US.UTF-8 UTF-8\" may instead be written as \"en_US UTF-8\", or even \"en_US\". Both the short and long forms are valid.

The next step is to run [locale-gen]. It will generate all the locales specified in the [/etc/locale.gen] file and write them to the locale-archive ([/usr/lib/locale/locale-archive]).

`root `[`#`]`locale-gen`

     * Generating 4 locales (this might take a while) with 1 jobs
     *  (1/4) Generating en_GB.ISO-8859-1 ...                       [ ok ]
     *  (2/4) Generating en_GB.UTF-8 ...                            [ ok ]
     *  (3/4) Generating de_DE.ISO-8859-1 ...                       [ ok ]
     *  (4/4) Generating de_DE.ISO-8859-15@euro ...                 [ ok ]
     * Generation complete

Verify that the selected locales are available by running [locale -a].

`user `[`$`]`locale -a`

    C
    POSIX
    de_DE
    de_DE.iso88591
    de_DE.iso885915@euro
    de_DE@euro
    deutsch
    en_GB
    en_GB.iso88591
    en_GB.utf8
    german

The [/usr/lib/locale/locale-archive] file can be shown by [localedef].

`user `[`$`]`localedef --list-archive`

Its raw content can be displayed using the [strings] command.

`user `[`$`]`strings /usr/lib/locale/locale-archive | less`

### [Setting a locale]

#### [OpenRC]

When using OpenRC locale settings are stored in environment variables. These are typically set in [/etc/env.d/02locale] (for system-wide settings) and [\~/.bashrc] (for user-specific settings). More details can be found in the [UTF-8](https://wiki.gentoo.org/wiki/UTF-8#Setting_the_locale "UTF-8") article. The system wide settings ([/etc/env.d/02locale]) can be managed through [eselect locale]. For instance, to set the `LANG` variable to the `C` value:

`root `[`#`]`eselect locale list`

    Available targets for the LANG variable:
      [1]   C
      [2]   POSIX
      [3]   en_US
      [4]   en_US.iso885915
      [5]   en_US.utf8
      [ ]   (free form)

`root `[`#`]`eselect locale set 1`

Of course, editing the file manually is possible as well to diversify the locale variables.

The command above lists the suffix in lower case without any hyphens, glibc understands both forms of the suffix, many other programs don\'t. The most common example of which is X. So it is best to always use UTF-8 in preference to utf8.

[FILE] **`/etc/env.d/02locale`Setting the default system locale in /etc/env.d/02locale**

    LANG="de_DE.UTF-8"
    LC_COLLATE="C.UTF-8"

In some cases users may notice glitchy non-English representation in some applications like Krusader ([https://bugs.kde.org/show_bug.cgi?id=371582](https://bugs.kde.org/show_bug.cgi?id=371582)). Removing or commenting the `LC_ALL=""` line from [/etc/env.d/02locale] should fix the problem.

It\'s also possible, and pretty common especially in a more traditional UNIX environment, to leave the global settings unchanged, i.e. in the `C` locale. Users can still specify their preferred locale in their own shell configuration file:

[FILE] **`~/.bashrc`Setting the user locale**

    export LANG="de_DE.UTF-8"
    export LC_COLLATE="C.UTF-8"

[FILE] **`~/.profile`Setting the user locale for X applications**

    export LANG="de_DE.UTF-8"
    export LC_COLLATE="C.UTF-8"

Another way of configuring system is to leave it in the default `C` locale, but enable UTF-8 character representation at the same time. This option is achieved using the following settings in [/etc/env.d/02locale]:

[CODE] **Using traditional C locale while specifying UTF-8**

    LC_CTYPE=de_DE.UTF-8

Using the above snippet, users will be able to see localized file names properly, while not being forced to completely use the selected language.

Once the right locale is set up, be sure to update the environment variables to make the system aware of the change.

For a system-wide default locale:

`root `[`#`]`env-update && source /etc/profile`

For a user-specific locale:

`user `[`$`]`source ~/.bashrc`

After this, kill the X server by pressing [Ctrl]+[Alt]+[Backspace], log out, then log in as a user.

Now, verify that the changes have taken effect:

`user `[`$`]`locale`

The values of locale environment variables that have been explicitly set e.g. in an export statement (if using bash) are listed without double quotes. Those whose value has been inherited from other locale environment variables have their values in double quotes.

#### [systemd]

With systemd set the locale with the [localectl] command. Check the list of available locales with:

`root `[`#`]`localectl list-locales`

Then set the desired locale:

`root `[`#`]`localectl set-locale LANG=de_DE.utf8`

Finally check if the result is good:

`root `[`#`]`localectl | grep "System Locale"`

       System Locale: LANG=de_DE.utf8

## [Keyboard layout for the console]

### [OpenRC]

The keyboard layout used by the console is set in [/etc/conf.d/keymaps] by the `keymap` variable. Valid values can be found in [/usr/share/keymaps/YOUR_ARCH/]. [i386] has further subdivisions into layout ([qwerty/], [azerty/], etc.). Some languages have multiple options - experiment with the various options to decide which one fits your needs best.

[FILE] **`/etc/conf.d/keymaps`Setting the console keymap**

    keymap="de"
    #keymap="de-latin1"
    #keymap="de-latin1-nodeadkeys"

### [systemd]

With systemd the keymap layout used for the console can be set using the [localectl] command. First check the available keymap layouts:

`root `[`#`]`localectl list-keymaps`

Then set the requested console keymap layout:

`root `[`#`]`localectl set-keymap it`

Finally check if the console keymap layout was set correctly:

`root `[`#`]`localectl | grep "VC Keymap"`

           VC Keymap: it

## [Keyboard layout for the X server]

### [OpenRC]

The keyboard layout to be used by the X server is specified in [/etc/X11/xorg.conf.d/30-keyboard.conf] by the `XkbLayout` option. For details visit the [Xorg guide](https://wiki.gentoo.org/wiki/Xorg/Guide#Configuring_the_keyboard "Xorg/Guide") and the article about [Keyboard layout switching](https://wiki.gentoo.org/wiki/Keyboard_layout_switching#X11 "Keyboard layout switching").

### [systemd]

With systemd the keymap layout for the X11 server can be set using the [localectl] command. First check the available X11 keymap layouts:

`root `[`#`]`localectl list-x11-keymap-layouts`

Then set the requested X11 keymap layout:

`root `[`#`]`localectl set-x11-keymap it`

Finally check if the X11 keymap layout was set correctly:

`root `[`#`]`localectl | grep "X11 Layout"`

          X11 Layout: it

## [Native Language Support]

For message based localization to work in programs that support it and have the `nls` [USE flag](https://packages.gentoo.org/useflags/nls), compile the programs with this flag set. Message strings are installed in [/usr/share/locale/\<locale\>/LC_MESSAGES/\.mo] files. Most of the programs using the *Native Language Support (NLS)* also need the gettext library to extract and use localized messages. Of course, Portage will automatically install it when needed.

After enabling the `nls` USE flag some packages might need to be re-emerged:

`root `[`#`]`emerge --ask --changed-use --deep --with-bdeps=y @world`

## [LINGUAS]

** Warning**\
LINGUAS causes packages to implicitly skip locales. When using it, the package manager cannot determine which locales were omitted. Do not use LINGUAS if you intend to redistribute binary packages.

There is also an additional `LINGUAS` variable that is used by some gettext-based build systems to control which localization files are built and installed. The variable takes in *space*-separated list of language codes, and a suggested place to set it is [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")]:

`root `[`#`]`nano -w /etc/portage/package.use/00-localization`

    ## (Add in the LINGUAS variable. For instance, for German, Finnish and English:)
    */* LINGUAS: de fi en

Note that there is a large difference between `LINGUAS` being unset and being set to an empty value: Unset `LINGUAS` means to install all available languages. By contrast, with `LINGUAS=""`, most ebuilds would install only the packages\' default language but none of the `LC_MESSAGES` files.

** Note**\
Incorrect setting of LINGUAS may lead to incomplete translation of some applications, such as KDE Plasma and its apps. Try to remove LINGUAS and rebuild related packages if you encounter this problem.

## [L10N]

A `USE_EXPAND` variable called `L10N` decides which extra localization support will be installed. This is commonly used for downloads of additional language packs by packages. Similar to `LINGUAS`, the variable takes a space separated list of language tags, and it can be set in [/etc/portage/] global USE file:

`root `[`#`]`nano -w /etc/portage/package.use/localization`

    ## (Add in the L10N variable. For instance, for German and Brazilian Portuguese:)
    */* L10N: de pt-BR

To set it per-package, edit [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")] and prefix the requested language packs with \"l10n\_\", as shown in the next example:

[FILE] **`/etc/portage/package.use`**

    app-text/aspell l10n_de l10n_pt-BR

Note that while the common two letter language codes (like `de` or `fr`) are identical in `LINGUAS` and `L10N`, more complex entries have a different syntax because `L10N` uses [IETF language tags](https://www.w3.org/International/articles/language-tags/) (aka BCP 47). For example, `pt_BR` and `sr@latin` in `LINGUAS` become `pt-BR` and `sr-Latn` in `L10N`, respectively.

A list of `L10N` values that can be used is provided as [/var/db/repos/gentoo/profiles/desc/l10n.desc]:

`user `[`$`]`grep -i portuguese /var/db/repos/gentoo/profiles/desc/l10n.desc`

    pt - Portuguese
    pt-BR - Portuguese (Brazil)
    pt-PT - Portuguese (Portugal)

After setting the `L10N` `USE_EXPAND` variable it may be necessary to re-emerge some packages:

`root `[`#`]`emerge --ask --changed-use --deep --with-bdeps=y @world`

## [See also]

-   [Configuring locales](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Configure_locales "Handbook:AMD64/Installation/Base") (Gentoo Handbook)
-   [Musl#Locales](https://wiki.gentoo.org/wiki/Musl#Locales "Musl")
-   [Keyboard layout](https://wiki.gentoo.org/wiki/Evdev#Keyboard_layout "Evdev") inside the Evdev article
-   [X resources](https://wiki.gentoo.org/wiki/X_resources "X resources")
-   [Localization/Guide/The Euro symbol](https://wiki.gentoo.org/wiki/Localization/Guide/The_Euro_symbol "Localization/Guide/The Euro symbol") --- how to display the Euro symbol (€) for the console and in X.

## [External resources]

-   [Locales and Internationalization](https://www.gnu.org/software/libc/manual/html_node/Locales.html) (gnu.org)
-   [L10N USE_EXPAND variable replacing LINGUAS](https://gentoo.org/support/news-items/2016-06-23-l10n-use_expand.html)
-   [Michał Górny: How LINGUAS are thrice wrong!](https://blogs.gentoo.org/mgorny/2016/05/16/how-linguas-are-thrice-wrong/)
-   [\[gentoo-dev\] \[RFC\] How to deal with LINGUAS mess?](https://archives.gentoo.org/gentoo-dev/message/a08ea09c2c8e534fd9bc1146703c66ff)
-   [\[gentoo-dev\] \[RFC\] Masterplan for solving LINGUAS problems](https://archives.gentoo.org/gentoo-dev/message/41e09d1ddc8b30abb9f9d21d205b7b82)

## [References]

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Alexander Holler, Steven Lucy, Benny Chuang, Lars Weiler, Tobias Scherbaum, Flammie Pirinen, , [Francisco Blas Izquierdo Riera (klondike)](https://wiki.gentoo.org/wiki/User:Klondike "User:Klondike") **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*