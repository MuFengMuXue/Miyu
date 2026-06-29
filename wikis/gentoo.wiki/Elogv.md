**Resources**

[[]][GitHub](https://github.com/gentoo/elogv)

[elogv] is a curses-based tool that parses the contents of [elogs](https://wiki.gentoo.org/wiki/Portage_log "Portage log") created by Portage.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

Install [elogv]:

`root `[`#`]`emerge --ask app-portage/elogv`

## [Configuration]

To use [elogv], the Portage elog system needs to be configured in [/etc/portage/make.conf] with the following addition:

[FILE] **[`/etc/portage/make.conf`](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")**

    # Logging
    PORTAGE_ELOG_CLASSES="warn error log"
    PORTAGE_ELOG_SYSTEM="save"

For additional variable definitions see the [/usr/share/portage/config/make.conf.example] file.

** Note**\
If the `PORT_LOGDIR` variable is unset in [/etc/portage/make.conf], logs will be saved to [/var/log/portage/elog] by default.

## [Usage]

### [Invocation]

To use [elogv], type in a console:

`user `[`$`]`elogv --help`

    Elogv is a portage elog viewer based on curses and python,
    you can use these keys to control the behavior of the program:

     - Down arrow or j -> scroll the list of files down by 1 unit
     - Up arrow or k -> opposite of Down arrow
     - PageDown -> scroll the list down by 10 unit
     - PageUp -> opposite of PageDown
     - End -> go to the last file of the list
     - Home -> go to the first file of the list
     - t -> order the list of files by date, most recent on top
     - a -> order the list of files alphabetically, the first time by category,
            the second time (pressing the key again) by package name
     - c -> order the list of files by log class warning level
     - r -> reverse the list of files
     - SpaceBar -> scroll the selected file
     - h or F1 -> show the help screen, press Page Up/Down to scroll up and down,
                  h or F1 again to hide
     - d -> removes selected files, usage is similar to vim "d" command,
            here are same examples:
                da -> removes all files
                de -> removes from selected item to the end of the list
                ds -> remove from selected item to the start of the list
                d1d or dd -> removes selected file only
                d4d -> removes 4 files starting from selected one
     - / -> starts a search prompt, write a string and will be showed the next
            package that contains your string, use ESC to exit
     - q -> quit

## [See also]

-   [Egencache](https://wiki.gentoo.org/wiki/Egencache "Egencache") --- a tool that (re)builds metadata information for the Portage package database.
-   [Portage log](https://wiki.gentoo.org/wiki/Portage_log "Portage log") --- provides information when installing, updating, or removing packages.
-   [Useful Portage tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").