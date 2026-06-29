[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Khal&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://pimutils.org/)

[[]][GitHub](https://github.com/pimutils/khal)

[[]][Official documentation](https://khal.readthedocs.io/en/latest/)

[[]][Bugs (upstream)](https://github.com/pimutils/khal/issues)

[[]][[#pimutils](ircs://irc.libera.chat/#pimutils)] ([[webchat](https://web.libera.chat/#pimutils)])

khal is a CLI based calendar program that synchronizes with CalDAV utilizing [vdirsyncer](https://wiki.gentoo.org/wiki/Vdirsyncer "Vdirsyncer").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Setting the date and time locale]](#Setting_the_date_and_time_locale)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Displaying a list of events]](#Displaying_a_list_of_events)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/khal](https://packages.gentoo.org/packages/app-misc/khal) [[]] [A CalDAV based calendar]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-15 11:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/khal`

## [Configuration]

A basic khal config file looks like the following:

[FILE] **`~/.config/khal/config`**

    [calendars]

      [[personal]]
        path = ~/.calendars/personal/default
        color = dark green
        priority = 20
        readonly = True

Where the path is the [vdirsyncer](https://wiki.gentoo.org/wiki/Vdirsyncer "Vdirsyncer") storage path for the specified calendar.

### [Setting the date and time locale]

** Note**\
khal uses Python\'s strftime library for date and time formatting, for a full list of values, refer [here](https://docs.python.org/3/library/time.html#time.strftime).

To adjust the date and time locale, use the `[locale]` category like so:

[FILE] **`~/.config/khal/config`**

    ...

    [locale]
    dateformat = "%Y-%m-%d"
    datetimeformat = "%H:%M %Y-%m-%d"
    longdateformat = "%Y-%m-%d"
    timeformat = "%H:%M"

Using this, dates will display as `1970-01-01`, times as `00:00`, and together as `00:00 1970-01-01`. With the UNIX epoch as the example date and time.

## [Usage]

### [Displaying a list of events]

To display a list of events, use the `list` argument:

`user `[`$`]`khal list`

    Today, 1970-01-01
    07:00-15:00 Work
    12:00-13:00 Lunch