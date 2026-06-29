[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=RHVoice&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home (English)](https://rhvoice.org/)

[[]][Home (Russian)](https://rhvoice.ru/)

[[]][GitHub](https://github.com/RHVoice/RHVoice)

[[]][Official project wiki](https://github.com/RHVoice/RHVoice/wiki)

[[]][Bugs (upstream)](https://github.com/RHVoice/RHVoice/issues)

[[]][[#rhvoice](ircs://irc.libera.chat/#rhvoice)] ([[webchat](https://web.libera.chat/#rhvoice)])

**RHVoice** is a text-to-speech engine with extended language support.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Speech Dispatcher]](#Speech_Dispatcher)
-   [[3] [Usage]](#Usage)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

Enable the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository:

`root `[`#`]`eselect repository enable guru `

`root `[`#`]`emaint sync -r guru `

Install the RHVoice metapackage:

`root `[`#`]`emerge --ask app-accessibility/rhvoice`

It will pull voices for all locales set by the [*L10N* USE_EXPAND](https://wiki.gentoo.org/wiki/Localization#Package_manager "Localization"), skipping nonfree by default.

## [Configuration]

### [Files]

-   [/etc/RHVoice/RHVoice.conf] - Global (system wide) configuration file.

### [Speech Dispatcher]

Uncomment the following line in [/etc/speech-dispatcher/speechd.conf]:

[CODE]

    AddModule "rhvoice"                  "sd_rhvoice"   "rhvoice.conf"

Set RHVoice as the default module (optional):

[CODE]

    DefaultModule rhvoice

Test the new configuration:

`user `[`$`]`killall speech-dispatcher `

`user `[`$`]`spd-say "Hello!" `

## [Usage]

Test if RHVoice works:

`user `[`$`]`echo "Hello!" | RHVoice-test`

## [See also]

-   [eSpeak](https://wiki.gentoo.org/index.php?title=ESpeak&action=edit&redlink=1 "ESpeak (page does not exist)")
-   [Flite](https://wiki.gentoo.org/index.php?title=Flite&action=edit&redlink=1 "Flite (page does not exist)")