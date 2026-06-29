Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Claws_Mail/es "Claws Mail (94% translated)")
-   [français](https://wiki.gentoo.org/wiki/Claws_Mail/fr "Claws Mail (100% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Claws_Mail/it "Claws Mail (58% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Claws_Mail/hu "Claws Mail (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Claws_Mail/pl "Claws Mail/pl (15% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Claws_Mail/ru "Claws Mail (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Claws_Mail/zh-cn "Claws Mail (36% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Claws_Mail/ja "Claws Mail (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Claws_Mail/ko "Claws Mail/ko (58% translated)")

**Resources**

[[]][Home](http://www.claws-mail.org/)

[[]][Package information](https://packages.gentoo.org/packages/mail-client/claws-mail)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Claws_mail "wikipedia:Claws mail")

[[]][Claws Mail Repository](http://git.claws-mail.org/)

**Claws Mail** is a GUI mail client forked from [Sylpheed](http://sylpheed.sraoss.jp/en/). In [Claws Mail FAQ](http://www.claws-mail.org/faq/index.php/General_Information), it is said: *Claws Mail has many extra features compared to Sylpheed and is more powerful, yet is just as fast, lightweight and stable.*

It is in active development, can be extended by many plugins, and allows importing of mbox-format mailboxes (coming from [Thunderbird](https://wiki.gentoo.org/wiki/Thunderbird "Thunderbird"), for example). Its native mailbox format is [wikipedia:MH Message Handling System](https://en.wikipedia.org/wiki/MH_Message_Handling_System "wikipedia:MH Message Handling System"), although the mbox format can be used with a plugin. Claws Mail cannot write HTML messages (in keeping with the Keep It Simple principle), but can read them using plugins.

For Gentoo Linux it is provided by the [[[mail-client/claws-mail]](https://packages.gentoo.org/packages/mail-client/claws-mail)[]] package for all architectures except **[ia64]**.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Plugins]](#Plugins)
        -   [[1.2.1] [Spam Filtering]](#Spam_Filtering)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration and Usage]](#Configuration_and_Usage)
    -   [[2.1] [Clawsker]](#Clawsker)
    -   [[2.2] [Themes]](#Themes)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [mail-client/claws-mail](https://packages.gentoo.org/packages/mail-client/claws-mail) [[]] [An email client (and news reader) based on GTK+]

  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+gnutls`](https://packages.gentoo.org/useflags/+gnutls)                             Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`+imap`](https://packages.gentoo.org/useflags/+imap)                                 Add support for IMAP (Internet Mail Application Protocol)
  [`+libnotify`](https://packages.gentoo.org/useflags/+libnotify)                       Enable notification on the desktop in connection with USE=notification
  [`+notification`](https://packages.gentoo.org/useflags/+notification)                 Notification for new mail in different ways
  [`+oauth`](https://packages.gentoo.org/useflags/+oauth)                               Enable OAuth2 authentication support
  [`+pgp`](https://packages.gentoo.org/useflags/+pgp)                                   Enable PGP support
  [`archive`](https://packages.gentoo.org/useflags/archive)                             Enable archiving plugin
  [`bogofilter`](https://packages.gentoo.org/useflags/bogofilter)                       Build mail-filter/bogofilter plugin
  [`calendar`](https://packages.gentoo.org/useflags/calendar)                           Add support for calendars (not using mcal!)
  [`clamav`](https://packages.gentoo.org/useflags/clamav)                               Add support for Clam AntiVirus software (usually with a plugin)
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                                   Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)                                 Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                                     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                                   Add LDAP support (Lightweight Directory Access Protocol)
  [`litehtml`](https://packages.gentoo.org/useflags/litehtml)                           Enable dev-libs/gumbo html viewer plugin
  [`networkmanager`](https://packages.gentoo.org/useflags/networkmanager)               Enable net-misc/networkmanager support
  [`nls`](https://packages.gentoo.org/useflags/nls)                                     Add Native Language Support (using gettext - GNU locale utilities)
  [`nntp`](https://packages.gentoo.org/useflags/nntp)                                   Add support for newsgroups (Network News Transfer Protocol)
  [`pdf`](https://packages.gentoo.org/useflags/pdf)                                     Add general support for PDF (Portable Document Format), this replaces the pdflib and cpdflib flags
  [`perl`](https://packages.gentoo.org/useflags/perl)                                   Add optional support/bindings for the Perl language
  [`python`](https://packages.gentoo.org/useflags/python)                               Enable plugin for Python scripting
  [`rss`](https://packages.gentoo.org/useflags/rss)                                     Enable support for RSS feeds
  [`session`](https://packages.gentoo.org/useflags/session)                             Add persistent session support
  [`sieve`](https://packages.gentoo.org/useflags/sieve)                                 Build plugin for sieve filter support
  [`smime`](https://packages.gentoo.org/useflags/smime)                                 Build plugin for S/MIME support
  [`spam-report`](https://packages.gentoo.org/useflags/spam-report)                     Enable plugin for spam reporting to various services
  [`spamassassin`](https://packages.gentoo.org/useflags/spamassassin)                   Build mail-filter/spamassassin plugin
  [`spell`](https://packages.gentoo.org/useflags/spell)                                 Add dictionary support
  [`startup-notification`](https://packages.gentoo.org/useflags/startup-notification)   Enable application startup event feedback mechanism
  [`svg`](https://packages.gentoo.org/useflags/svg)                                     Add support for SVG (Scalable Vector Graphics)
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)                           Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`webkit`](https://packages.gentoo.org/useflags/webkit)                               Add support for the WebKit HTML rendering/layout engine
  [`xface`](https://packages.gentoo.org/useflags/xface)                                 Add xface support used to allow a small image of xface format to be included in an email via the header \'X-Face\'
  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-22 15:05] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Plugins]

Plugins are compiled with Claws Mail when the appropriate USE flags are set --- `bogofilter`, `spamassassin` or `pdf`, for example.

** Note**\
Before version 3.9.1 plugins had to be separately emerged.

#### [Spam Filtering]

-   Simple way: [Bogofilter](http://bogofilter.sourceforge.net/) is a powerful Bayesian filter which doesn\'t need to be configured. It quickly learns from the user\'s spam and ham classifications in Claws Mail. It is the preferred spam filter for desktop computers. Set the `bogofilter` USE flag to compile the plugin with Claws Mail.

<!-- -->

-   Hard way: [Spamassassin](http://spamassassin.apache.org/) is a huge mail filtering system, using Bayesian filtering and external spam-definition resources. It must be extensively configured and its daemon (spamd) must be running for Claws Mail to use it. It is the preferred spam filter for mail servers. Set the `spamassassin` USE flag to compile the plugin with Claws Mail. Some information can be found in the articles [Complete Virtual Mail Server](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/amavisd_spamassassin_clamav "Complete Virtual Mail Server/amavisd spamassassin clamav") and [Mailfiltering Gateway](https://wiki.gentoo.org/wiki/Mailfiltering_Gateway "Mailfiltering Gateway").

### [Emerge]

Create a [/etc/portage/package.use/claws-mail] file to activate the desired USE flags (or add them to the [/etc/portage/package.use] file). To set `bogofilter`, `pgp` and `archive`, for example:

`root `[`#`]`echo 'mail-client/claws-mail bogofilter pgp archive' > /etc/portage/package.use/claws-mail`

Then emerge Claws Mail:

`root `[`#`]`emerge --ask mail-client/claws-mail`

## [Configuration and Usage]

-   Accounts, mail filtering, models, actions, labels, etc. are set in the *Configuration* menu;
-   main configuration is done in *Configuration \> Preferences...*;
-   plugins are (de)activated in *Configuration \> Plugins...* and configured in *Configuration \> Preferences...*;
-   the archive plugin is run from *Tools \> Create Archive...*;
-   the user interface can be modified: lists headers in global or message views, icons, fonts;
-   the address book can import and export several formats.

### [Clawsker]

[[[mail-client/clawsker]](https://packages.gentoo.org/packages/mail-client/clawsker)[]] can be installed to edit many preferences which are not in the GUI:

`root `[`#`]`emerge --ask mail-client/clawsker`

Then launch it when Claws Mail is not running:

`user `[`$`]`clawsker`

The Claws Mail preferences file is [\~/.claws-mail/clawsrc].

### [Themes]

Many icon themes can be installed with [[[x11-themes/claws-mail-themes]](https://packages.gentoo.org/packages/x11-themes/claws-mail-themes)[]]:

`root `[`#`]`emerge --ask x11-themes/claws-mail-themes`

## [External resources]

-   [Claws Mail Features](http://www.claws-mail.org/features.php)
-   [FAQ](http://www.claws-mail.org/faq/index.php/Main_Page)
-   [Plugins](http://www.claws-mail.org/faq/index.php/Plugins)
-   [Versions News](http://claws-mail.org/NEWS)