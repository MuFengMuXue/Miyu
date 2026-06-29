## Contents

-   [[1] [RFC-3339 date format and its friends]](#RFC-3339_date_format_and_its_friends)
-   [[2] [System wide RFC-3339 date]](#System_wide_RFC-3339_date)
    -   [[2.1] [.profile]](#.profile)
    -   [[2.2] [zsh]](#zsh)
    -   [[2.3] [xfce panel clock]](#xfce_panel_clock)

### [RFC-3339 date format and its friends]

The [RFC-3339 standard](https://www.rfc-editor.org/rfc/rfc3339) is available for free in the public and widely used for software. The [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601) is very similar, but requires the \'T\' between the day and the hours. RFC-3339 allows to use a space or the \'T\' respectively.

\

+----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Example                    | Allowed in Standard   | date command                                                                                                                                                                                    |
+----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2023-08-13                 | RFC-3339, ISO_8601    | :::: cmd-box                                                                                                                                                                                    |
|                            |                       |                                                                                                                                                                                            |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       | `user `[`$`]`date --rfc-3339='date'`    |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       |                                                                                                                                                                                           |
|                            |                       | ::::                                                                                                                                                                                            |
+----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2023-08-13T16:07:54+02:00  | RFC-3339, ISO_8601    | :::: cmd-box                                                                                                                                                                                    |
|                            |                       |                                                                                                                                                                                            |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       | `user `[`$`]`date --iso-8601='seconds'` |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       |                                                                                                                                                                                           |
|                            |                       | ::::                                                                                                                                                                                            |
+----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2023-08-13 16:08:44+02:00  | RFC-3339              | :::: cmd-box                                                                                                                                                                                    |
|                            |                       |                                                                                                                                                                                            |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       | `user `[`$`]`date --rfc-3339='seconds'` |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       |                                                                                                                                                                                           |
|                            |                       | ::::                                                                                                                                                                                            |
+----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2023-08-13 16:08:44 +02:00 | RFC-3339              | :::: cmd-box                                                                                                                                                                                    |
|                            |                       |                                                                                                                                                                                            |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       | `user `[`$`]`date "+%F %T %:z"`         |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       |                                                                                                                                                                                           |
|                            |                       | ::::                                                                                                                                                                                            |
+----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2023-08-13 16:08:44        | \-                    | :::: cmd-box                                                                                                                                                                                    |
|                            |                       |                                                                                                                                                                                            |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       | `user `[`$`]`date "+%F %T"`             |
|                            |                       |                                                                                                                                                                                                 |
|                            |                       |                                                                                                                                                                                           |
|                            |                       | ::::                                                                                                                                                                                            |
+----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\

-   [stackoverflow: What\'s the difference between ISO 8601 and RFC 3339 Date Formats?](https://stackoverflow.com/questions/522251/whats-the-difference-between-iso-8601-and-rfc-3339-date-formats)
-   comparison between RFC 3339 and ISO 8601 [https://ijmacd.github.io/rfc3339-iso8601/](https://ijmacd.github.io/rfc3339-iso8601/)

## [System wide RFC-3339 date]

Several configuration files need adjustments to achieve a system wide RFC-3339 date representation. Here we focus on the representation with space instead of \'T\'.

### [.profile]

[FILE] **`~/.profile`.profile**

    # Localization
    TIME_STYLE=long-iso #for ISO Date in ls"

### [zsh]

[FILE] **`~/.zshrc`.zshrc**

    # Localization
    TIME_STYLE=long-iso #for ISO Date in ls"

\

### [xfce panel clock]

[FILE] **`.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml`xfce panel clock with T**




[FILE] **`.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml`xfce panel clock with space**