**Resources**

[[]][Home](http://surf.suckless.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Surf_(web_browser) "wikipedia:Surf (web browser)")

surf is a simple web browser based on WebKit/GTK. It is able to display websites and follow links. It supports the XEmbed protocol which makes it possible to embed it in another application. Furthermore, one can point surf to another URI by setting its XProperties.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Patches and additional features]](#Patches_and_additional_features)
    -   [[2.2] [Tabbed browsing]](#Tabbed_browsing)

## [Installation]

### [USE flags]

### [USE flags for] [www-client/surf](https://packages.gentoo.org/packages/www-client/surf) [[]] [A simple web browser based on WebKit/GTK+]

  ------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)   Without a saved config.h, this package depends on net-misc/curl and x11-terms/st for a default download mechanism
  [`tabbed`](https://packages.gentoo.org/useflags/tabbed)             Install surf-open.sh script for running surf in x11-misc/tabbed
  ------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2023-11-30 11:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Preferably, you\'ll want to enable [`savedconfig`](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") USE flag and save your customized configuration file to [/etc/portage/savedconfig/www-client/surf-2.0] for later editing pleasure.

`root `[`#`]`euse --enable savedconfig`

### [Emerge]

Install [[[www-client/surf]](https://packages.gentoo.org/packages/www-client/surf)[]]:

`root `[`#`]`emerge --ask www-client/surf`

## [Configuration]

As stated previously, the main surf configuration file is the [/etc/portage/savedconfig/www-client/surf-2.0] file and after each change, surf needs to be recompiled for any changes to take effect.

### [Patches and additional features]

There are many user-created [patches](http://surf.suckless.org/patches/) available from the official site that greatly extend the functionality of surf.

### [Tabbed browsing]

The [[[x11-misc/tabbed]](https://packages.gentoo.org/packages/x11-misc/tabbed)[]] program can be used with surf for a simple tabbed browsing experience.

A basic set-up:

`user `[`$`]`tabbed surf -e`

To achieve a similar behavior to Firefox or Chromium where upon closing the last tab, the browser exits, use:

`user `[`$`]`tabbed -c surf -e`