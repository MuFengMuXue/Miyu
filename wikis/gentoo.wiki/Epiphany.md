**Resources**

[[]][Home](https://wiki.gnome.org/Apps/Web/)

[[]][GitLab](https://gitlab.gnome.org/GNOME/epiphany)

**Epiphany**, sometimes called simply **web**, is a simple, fast Webkit-based web browser built for [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") and [Pantheon](https://wiki.gentoo.org/wiki/Pantheon "Pantheon"). It\'s main goal is to create a web browser that is [free](https://en.wikipedia.org/wiki/Free_software), open source, aesthetically pleasing and clean. It comes with a built-in adblocker and [Intelligent Tracking Prevention](https://webkit.org/tracking-prevention/) by default.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Flatpak]](#Flatpak)

## [Installation]

### [USE flags]

### [USE flags for] [www-client/epiphany](https://packages.gentoo.org/packages/www-client/epiphany) [[]] [GNOME webbrowser based on Webkit]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 00:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask www-client/epiphany`

### [Flatpak]

Epiphany also offers a flatpak version. It is the recommended way of installing epiphany by the developers.

Install Flatpak:

`root `[`#`]`emerge --ask sys-apps/flatpak`

Install epiphany from flathub.

`root `[`#`]`flatpak install flathub org.gnome.Epiphany`

Run through the command line:

`user `[`$`]`flatpak run org.gnome.Epiphany`

See [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak") for more information.