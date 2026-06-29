[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Qutebrowser&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://qutebrowser.org/)

[[]][Package information](https://packages.gentoo.org/packages/www-client/qutebrowser)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Qutebrowser "wikipedia:Qutebrowser")

[[]][GitHub](https://github.com/qutebrowser/qutebrowser)

**qutebrowser** is a web browser with [vim-style key bindings](https://qutebrowser.org/img/cheatsheet-big.png) based off QtWebKit (or QtWebEngine in its latest release). It is lightweight using a minimal GUI and is inspired by software such as [Vimperator](http://www.vimperator.org/vimperator/) and [dwb](https://portix.bitbucket.io/dwb/). It uses [DuckDuckGo](https://duckduckgo.com/) as the default search engine.

qutebrowser was developed by Freya Bruhin, for which she received a CH Open Source award in 2016.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Proprietary Codecs]](#Proprietary_Codecs)
    -   [[2.2] [Video or sound not working well]](#Video_or_sound_not_working_well)
    -   [[2.3] [No sound with Pipewire]](#No_sound_with_Pipewire)
    -   [[2.4] [Kerberos authentication does not work]](#Kerberos_authentication_does_not_work)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [www-client/qutebrowser](https://packages.gentoo.org/packages/www-client/qutebrowser) [[]] [Keyboard-driven, vim-like browser based on Python and Qt]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+adblock`](https://packages.gentoo.org/useflags/+adblock)       Enable Brave\'s ABP-style adblocker library for improved adblocking
  [`pdf`](https://packages.gentoo.org/useflags/pdf)                 Add general support for PDF (Portable Document Format), this replaces the pdflib and cpdflib flags
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`widevine`](https://packages.gentoo.org/useflags/widevine)       Unsupported closed-source DRM capability (required by Netflix VOD)
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-26 05:41] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Turn off the `bindist` flag to enable support for proprietary codecs on WebEngine.

### [Emerge]

`root `[`#`]`emerge --ask www-client/qutebrowser`

## [Troubleshooting]

### [Proprietary Codecs]

To get proprietary codecs to work, turn off the [[[bindist]](https://packages.gentoo.org/useflags/bindist)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") for [[[dev-qt/qtwebengine]](https://packages.gentoo.org/packages/dev-qt/qtwebengine)[]] in [/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use") - see [Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:AMD64/Working/USE").

Once the use flag is properly set in the file, re-emerge qtwebengine. Remember to use the `--oneshot` parameter so as to not add the dependency to the [world file](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)"):

`root `[`#`]`emerge --ask --oneshot dev-qt/qtwebengine`

`root `[`#`]`emerge --ask www-client/qutebrowser`

### [Video or sound not working well]

`root `[`#`]`emerge --ask --verbose media-libs/gst-plugins- media-plugins/gst-plugins-libav`

### [No sound with Pipewire]

To hear sound when Pipewire is used, turn on `pipewire-alsa` for [[[media-video/pipewire]](https://packages.gentoo.org/packages/media-video/pipewire)[]] in [/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use").

[FILE] **`/etc/portage/package.use`Read [this](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:AMD64/Working/USE") for more information**

    media-video/pipewire pipewire-alsa

After the USE flag is set properly, re-emerge Pipewire:

`root `[`#`]`emerge --ask media-video/pipewire`

### [Kerberos authentication does not work]

To let the browser know which domains are allowed to authenticate with Kerberos, make sure you have the following config in place. The example shows allowing it to work when visiting subdomains of `fedoraproject.org` and `work.corp.com`:

[FILE] **`~/.config/qutebrowser/config.py`**

    c.qt.args = [
      "auth-server-allowlist=*.fedoraproject.org,*.work.corp.com",
      "auth-server-whitelist=*.fedoraproject.org,*.work.corp.com",  # this is a deprecated name that might be needed on some older versions
      "disable-auth-negotiate-cname-lookup=true",  # this is currently a no-op, waiting for Chromium to make the setting available
    ]
    config.load_autoconfig()

Sometimes, this is not enough, however. The underlying feature is implemented in a transitive dependency of [[[www-client/qutebrowser]](https://packages.gentoo.org/packages/www-client/qutebrowser)[]] --- [[[dev-qt/qtwebengine]](https://packages.gentoo.org/packages/dev-qt/qtwebengine)[]]. If it\'s not compiled with [[[kerberos]](https://packages.gentoo.org/useflags/kerberos)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] support, the above configuration will not have any effect.

Usually, it\'s not desired to enable the [[[kerberos]](https://packages.gentoo.org/useflags/kerberos)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag just for a single package and most of the time one would want to have it enabled globally. It can be done with a command like:

`user `[`$`]`euse -E kerberos`

    /etc/portage/make.conf was modified, a backup copy has been placed at /etc/portage/make.conf.euse_backup

Alternatively, create the following file by hand:

[FILE] **`/etc/portage/package.use/00kerberos`Read [this](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declare_permanent_USE_flags "Handbook:AMD64/Working/USE") for more information**

    */* kerberos

Finally, once the use flag is properly set in the file, re-emerge [[[dev-qt/qtwebengine]](https://packages.gentoo.org/packages/dev-qt/qtwebengine)[]]. Remember to use the `--oneshot` parameter so as to not add the dependency to the [world file](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)"):

`root `[`#`]`emerge --ask --oneshot dev-qt/qtwebengine`

## [External resources]

-   [Official Installation Documentation](https://qutebrowser.org/doc/install.html#_on_gentoo)
-   [qtwebkit-5.212.0_alpha2.ebuild](https://gist.github.com/annulen/309569fb61e5d64a703c055c1e726f71)