[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Thunderbird&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.mozilla.org/en-US/thunderbird/)

[[]][Package information](https://packages.gentoo.org/packages/mail-client/thunderbird)

[[]][Binary package - Package information](https://packages.gentoo.org/packages/mail-client/thunderbird-bin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mozilla_Thunderbird "wikipedia:Mozilla Thunderbird")

[[]][[alt.comp.software.thunderbird](news:alt.comp.software.thunderbird) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.comp.software.thunderbird))]

[[]][[#thunderbird](ircs://irc.libera.chat/#thunderbird)] ([[webchat](https://web.libera.chat/#thunderbird)])

**Thunderbird** is Mozilla\'s solution to the e-mail client.

**Earlybird** is the \"unbranded\" version of Thunderbird. It can be enabled when the `bindist` is set.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [XDG integration]](#XDG_integration)
        -   [[2.1.1] [Global search]](#Global_search)
    -   [[2.2] [Writing mails: disable line wrapping (use full width)]](#Writing_mails:_disable_line_wrapping_.28use_full_width.29)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Keyboard shortcuts]](#Keyboard_shortcuts)
    -   [[3.2] [Mail notification sound]](#Mail_notification_sound)
    -   [[3.3] [Instant messaging]](#Instant_messaging)
    -   [[3.4] [Calendar function]](#Calendar_function)
    -   [[3.5] [Filters]](#Filters)
        -   [[3.5.1] [Backing up or moving filter rules]](#Backing_up_or_moving_filter_rules)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [mail-client/thunderbird](https://packages.gentoo.org/packages/mail-client/thunderbird) [[]] [Thunderbird Mail Client]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                               Add support for X11
  [`+clang`](https://packages.gentoo.org/useflags/+clang)                       Use Clang compiler instead of GCC
  [`+system-av1`](https://packages.gentoo.org/useflags/+system-av1)             Use the system-wide media-libs/dav1d and media-libs/libaom library instead of bundled.
  [`+system-harfbuzz`](https://packages.gentoo.org/useflags/+system-harfbuzz)   Use the system-wide media-libs/harfbuzz and media-gfx/graphite2 instead of bundled.
  [`+system-icu`](https://packages.gentoo.org/useflags/+system-icu)             Use the system-wide dev-libs/icu instead of bundled.
  [`+system-jpeg`](https://packages.gentoo.org/useflags/+system-jpeg)           Use the system-wide media-libs/libjpeg-turbo instead of bundled.
  [`+system-libevent`](https://packages.gentoo.org/useflags/+system-libevent)   Use the system-wide dev-libs/libevent instead of bundled.
  [`+system-librnp`](https://packages.gentoo.org/useflags/+system-librnp)       Use system-wide dev-util/librnp instead of bundled one.
  [`+system-libvpx`](https://packages.gentoo.org/useflags/+system-libvpx)       Use the system-wide media-libs/libvpx instead of bundled.
  [`+system-webp`](https://packages.gentoo.org/useflags/+system-webp)           Use the system-wide media-libs/libwebp instead of bundled.
  [`debug`](https://packages.gentoo.org/useflags/debug)                         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`eme-free`](https://packages.gentoo.org/useflags/eme-free)                   Disable EME (DRM plugin) capability at build time
  [`hardened`](https://packages.gentoo.org/useflags/hardened)                   Activate default security enhancements for toolchain (gcc, glibc, binutils)
  [`hwaccel`](https://packages.gentoo.org/useflags/hwaccel)                     Force-enable hardware-accelerated rendering (Mozilla bug 594876)
  [`jack`](https://packages.gentoo.org/useflags/jack)                           Add support for the JACK Audio Connection Kit
  [`libproxy`](https://packages.gentoo.org/useflags/libproxy)                   Enable libproxy support
  [`pgo`](https://packages.gentoo.org/useflags/pgo)                             Add support for profile-guided optimization using gcc-4.5, for faster binaries. This option will double the compile time.
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)               Add sound server support via media-libs/libpulse (may be PulseAudio or Pipewire, or apulse if installed)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sndio`](https://packages.gentoo.org/useflags/sndio)                         Enable support for the media-sound/sndio backend
  [`system-pipewire`](https://packages.gentoo.org/useflags/system-pipewire)     Use system media-video/pipewire for WebRTC and screencast instead of bundled one
  [`system-png`](https://packages.gentoo.org/useflags/system-png)               Use the system-wide media-libs/libpng instead of bundled (requires APNG patches)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                     Enable dev-libs/wayland backend
  [`wifi`](https://packages.gentoo.org/useflags/wifi)                           Enable necko-wifi for NetworkManager integration, and access point MAC address scanning for better precision with opt-in geolocation services
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 15:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask mail-client/thunderbird`

Emerging Thunderbird is a long process, a pre-compiled (binary) version exists for users who want a shorter install time:

`root `[`#`]`emerge --ask mail-client/thunderbird-bin`

Note that behavior of the pre-compiled version may be different in many ways including the choice of default applications for URLs.

## [Configuration]

### [XDG integration]

To ensure Thunderbird is being used by other applications as the [default application](https://wiki.gentoo.org/wiki/Default_applications#Setting_the_default_application_via_mimeapps.list_files "Default applications") for handling `mailto:` links, run:

`user `[`$`]`xdg-mime default thunderbird.desktop x-scheme-handler/mailto`

#### [Global search]

See [forum post: thunderbird not indexation for global search](https://forums.gentoo.org/viewtopic-p-8116898.html#8116898)

### [][Writing mails: disable line wrapping (use full width)]

Go to Tools \> Options \> Advanced \> General and open the **Config Editor**. Search for **mailnews.wraplength** and set it to 0 (maximum length).^[\[1\]](#cite_note-1)^

As with [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") - it is possible to store your settings in **user.js** and use [git](https://wiki.gentoo.org/wiki/Git "Git") for the backup/sync.^[\[2\]](#cite_note-2)^

[FILE] **`~/.thunderbird/xxxxxxxx.default-release/user.js`**

    user_pref('mailnews.wraplength', 0);

## [Usage]

### [Keyboard shortcuts]

Thunderbird has a variety of keyboard shortcuts built-in. A full listing can be viewed on the [Thunderbird support page](https://support.mozilla.org/en-US/kb/keyboard-shortcuts-thunderbird).

### [Mail notification sound]

Mail notification sound needs a sound theme to work, see [[[bug #617566]](https://bugs.gentoo.org/show_bug.cgi?id=617566)[]].

### [Instant messaging]

Thunderbird supports instant messaging and chat using IRC, XMPP, and Twitter. Instructions for configuration can be found on the [instant message and chat support page](https://support.mozilla.org/en-US/kb/instant-messaging-and-chat).

### [Calendar function]

Thunderbird has a build in calendar function called lightning.

### [Filters]

Filter rules can be configured within Thunderbird to short or apply rules to incoming or outgoing messages. For mail accounts which are subscribed to many mailing lists, or which receive a lot of mail from known sending addresses, filter rules enable a tidy inbox. As of 2023-06-26, Thunderbird v102.12.0 has no way to exclusively export filter rule sets from one system to another. See the [Backing up or moving filter rules](#Backing_up_or_moving_filter_rules) section for details on recreating rule sets when using Thunderbird on multiple devices.

Unfortunately, there are [known bugs](https://bugzilla.mozilla.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&field0-0-0=product&field0-0-1=component&field0-0-2=alias&field0-0-3=short_desc&field0-0-4=status_whiteboard&field0-0-5=cf_crash_signature&field1-0-0=product&field1-0-1=component&field1-0-2=alias&field1-0-3=short_desc&field1-0-4=status_whiteboard&field1-0-5=cf_crash_signature&field2-0-0=product&field2-0-1=component&field2-0-2=alias&field2-0-3=short_desc&field2-0-4=status_whiteboard&field2-0-5=cf_crash_signature&type0-0-0=substring&type0-0-1=substring&type0-0-2=substring&type0-0-3=substring&type0-0-4=substring&type0-0-5=substring&type1-0-0=substring&type1-0-1=substring&type1-0-2=substring&type1-0-3=substring&type1-0-4=substring&type1-0-5=substring&type2-0-0=substring&type2-0-1=substring&type2-0-2=substring&type2-0-3=substring&type2-0-4=substring&type2-0-5=substring&value0-0-0=run&value0-0-1=run&value0-0-2=run&value0-0-3=run&value0-0-4=run&value0-0-5=run&value1-0-0=filter&value1-0-1=filter&value1-0-2=filter&value1-0-3=filter&value1-0-4=filter&value1-0-5=filter&value2-0-0=auto&value2-0-1=auto&value2-0-2=auto&value2-0-3=auto&value2-0-4=auto&value2-0-5=auto) regarding filter rules which prevent certain rules from automatically applying as expected. To work around, the user can manually trigger the rule on the appropriate folder as necessary.

#### [[] Backing up or moving filter rules]

Filter rules are stored in a file entitled [msgFilterRules.dat], which is located under the [\~/.thunderbird/\<Profile name\>/] directory on Linux systems. When wishing to backup filter rules or copy them to another Thunderbird client, this file will need located. Follow the below steps:

1.  Locate the profile directory for the relevant mail account. With Thunderbird open:
    -   Open the [Menu Bar] toolbar \> [Tools] \> [Export] \> [Open profile folder] link
    -   Select: [Help] \> [More Troubleshooting Information] \> Under Application Basics located the Profile Directory row, and click [Open Directory].
2.  Either of the above steps should a file browser window showing contents of profile name folder. This should be under the [\~/.thunderbird/\<Profile name\>/] directory as noted above.
3.  Close all running instances of Thunderbird. This ensures all files are written (synced) into the profile directory.
4.  Locate the [msgFilterRules.dat] by drilling into directories until it is discovered, or by opening a shell within the profile directory and running the following command:
    -   :::: cmd-box


        `user `[`$`]`find . -name 'msgFilterRules.dat'`


        ::::
5.  Once discovered, move this file to the backup location and/or into the profile using the same mail account on another device.

## [See also]

-   [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") --- [open source](https://en.wikipedia.org/wiki/Open_source "wikipedia:Open source"), [multiplatform](https://en.wikipedia.org/wiki/Cross-platform_software "wikipedia:Cross-platform software"), [web browser](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications") developed by [Mozilla](https://en.wikipedia.org/wiki/Mozilla "wikipedia:Mozilla").

## [External resources]

-   [Thunderbird tips and tricks](https://support.mozilla.org/en-US/products/thunderbird/tips-and-tricks) (Mozilla).
-   [Thunderbird on Mozilla\'s Forums](http://forums.mozillazine.org/viewforum.php?f=50)
-   [Thunderbird on Mozilla\'s Buglist](https://bugzilla.mozilla.org/buglist.cgi?quicksearch=Thunderbird)

1.  [[[↑](#cite_ref-1)] [[https://superuser.com/a/1243507/204068](https://superuser.com/a/1243507/204068)]]
2.  [[[↑](#cite_ref-2)] [[https://kb.mozillazine.org/User.js_file](https://kb.mozillazine.org/User.js_file)]]