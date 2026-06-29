This page contains [[changes](https://wiki.gentoo.org/index.php?title=Portage_log&oldid=1402703&diff=1439956)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Portage_log/de "Portage Log (28% translated)")
-   [English]
-   [français](https://wiki.gentoo.org/wiki/Portage_log/fr "Journaux de portage (93% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Portage_log/hu "Portage napló (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Portage_log/ru "Portage log (19% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Portage_log/ja "Portage ログ (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Portage_log/ko "Portage log/ko (10% translated)")

The **[Portage](https://wiki.gentoo.org/wiki/Portage "Portage") log** provides information when installing, updating, or removing packages.

When using [emerge] for building a package, it is not uncommon to notice messages coming from [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") itself. Since they may contain important information from Gentoo developers it is a good idea to read them, but often this is not immediately possible because they rapidly scroll out of the screen. This can be easily solved by enabling a Portage [feature](https://wiki.gentoo.org/wiki/FEATURES "FEATURES") called elog, whose purpose is to save messages to disk for later review. But other logging capabilities exist as well\...

## Contents

-   [[1] [Portage elog subsystem]](#Portage_elog_subsystem)
    -   [[1.1] [Setup]](#Setup)
    -   [[1.2] [Configuring for file-based storage]](#Configuring_for_file-based_storage)
        -   [[1.2.1] [Script to lookup logs]](#Script_to_lookup_logs)
    -   [[1.3] [Configuring for e-mail]](#Configuring_for_e-mail)
    -   [[1.4] [Related software]](#Related_software)
-   [[2] [Build logs]](#Build_logs)
    -   [[2.1] [Always save build logs]](#Always_save_build_logs)
    -   [[2.2] [Cleaning up]](#Cleaning_up)
-   [[3] [Other Portage log files]](#Other_Portage_log_files)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [[] Portage elog subsystem]

The Portage elog subsystem keeps track of specific, ebuild-provided log messages that developers have put in the [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") to attract attention of the system administrator or root user. Often, these messages contain important or interesting information related to the build of said package.

### [[] Setup]

Select which kind of information should be logged through the `PORTAGE_ELOG_CLASSES` variable. Possible values are `info`, `warn`, `error`, `log`, and `qa`:

[FILE] **[`/etc/portage/make.conf`](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")**

    PORTAGE_ELOG_CLASSES="log warn error"

### [[] Configuring for file-based storage]

Portage can handle the elog events in a number of ways, including:

-   `echo`: display messages again when `emerge` exits.
-   `save`: save one log file per package.
-   `custom`: pass messages to `PORTAGE_ELOG_COMMAND`.
-   `syslog`: send messages to syslog.
-   `mail`: send messages using `PORTAGE_ELOG_MAILURI`.
-   `save_summary`: save all messages to one summary log.
-   `mail_summary`: send all messages in one mail when `emerge` exits.

In order to save the elog events to disk, enable the `save` module in the `PORTAGE_ELOG_SYSTEM` variable:

[FILE] **`/etc/portage/make.conf`**

    # Warning: just 'save' won't show messages on emerging! Add 'echo' to save *AND* show.
    #PORTAGE_ELOG_SYSTEM="save"

    # Show messages after emerging *and* save
    PORTAGE_ELOG_SYSTEM="echo save"

The messages will be saved in [/var/log/portage/elog] or in [\$/elog] if said variable is set.

In order to create per-category elog files, enable the `split-elog` Portage feature. It will force Portage to create category-based subdirectories of the [/var/log/portage/elog] location.

Additionally, to create per-category build logs, enable the `split-log` Portage feature. It will force Portage to create category-based subdirectories of the [/var/log/portage/build] location.

#### [[] Script to lookup logs]

When the logs are split up, it\'s a bit annoying to look through them one by one. Here\'s an example script to print them using the date:

[FILE] **`print-elog-messages.sh`**

    #!/bin/bash

    # This script is assuming that portage is configured to log in
    # /var/log/portage/elog and that it's configured to split the logged files.
    #
    # If you want specific dates, run the script like so:
    # GET_DATES="20230101 20230102" ./print_elog_messages.sh
    #
    # If you want all files to be printed, run the script like so:
    # GET_ALL="true" ./print_elog_messages.sh
    #
    # If the script filename is different, adjust accordingly!

    # Check if running as root and stop if it is.
    current_user=$(whoami)
    [ -z "$current_user" ] && echo "whoami returns an empty string" && exit 1
    [ "$current_user" == "root" ] && echo "Don't run as root, there's no need!" && exit 1

    # Set periods to check. These strings are interpreted by the "date" tool.
    declare -a days=("today" "yesterday")

    # Change the array to the custom dates if they're declared.
    [ -n "$GET_DATES" ] && declare -a days=("$GET_DATES")

    # If we're printing everything, there's no reason to loop multiple times and
    # it would make sense to change the period to "all".
    [ "$GET_ALL" == "true" ] && declare -a days=("all")

    # Go through the periods set in the array "days" and format to find filenames
    # containing YYYYmmdd, for example 20221215, since that's the format that's
    # part of the filenames by default. After this, run the command cat with the
    # found filenames as arguments, which adds the file contents
    # to the terminal output. Remove the -n argument from cat if you don't want
    # it to print the line numbers as well.
    for val in $; do
        echo "          ===== $val ====="
        find /var/log/portage/elog -name \
            "*$([ "$GET_ALL" == "true" ] || date --date=$val +%Y%m%d)*" \
            -type f -print -exec cat -n '' \;
    done

### [[] Configuring for e-mail]

To mail logs to a recipient, enable the `mail` module. The mail option requires some additional variables to be set. Read [/usr/share/portage/config/make.conf.example] for more information.

Below, an example setup is shown which is hopefully self-explanatory:

[FILE] **`/etc/portage/make.conf`**

    # This will _only_ email; you may want to do "mail save" or similar instead.
    PORTAGE_ELOG_SYSTEM="mail"
    # First the mail-to address, then the SMTP server
    PORTAGE_ELOG_MAILURI="log-intake@example.com mail.example.com"
    PORTAGE_ELOG_MAILFROM="portage@$(hostname).example.com"
    PORTAGE_ELOG_MAILSUBJECT="\$ is \$ on \$"

Another example with nullmailer or sendmail:

[FILE] **`/etc/portage/make.conf`**

    # This will _only_ email; you may want to do "mail save" or similar instead.
    PORTAGE_ELOG_SYSTEM="mail"
    # First the mail-to address, then the SMTP server
    PORTAGE_ELOG_MAILURI="users@host /usr/sbin/sendmail"
    PORTAGE_ELOG_MAILFROM="portage@$(hostname).example.com"
    PORTAGE_ELOG_MAILSUBJECT="\$ is \$ on \$"

When configuring PORTAGE_ELOG_MAILURI, be aware that the port number behaves differently when STARTTLS is required.

[FILE] **`/usr/lib/python3.13/site-packages/portage/mail.py`**

    # Syntax for PORTAGE_ELOG_MAILURI (if defined):
    # address [[user:passwd@]mailserver[:port]]
    # where address:    recipient address
    #       user:       username for smtp auth (defaults to none)
    #       passwd:     password for smtp auth (defaults to none)
    #       mailserver: smtp server that should be used to deliver the mail (defaults to localhost)
    #                                   alternatively this can also be the absolute path to a sendmail binary if you don't want to use smtp
    #       port:       port to use on the given smtp server (defaults to 25, values > 100000 indicate that starttls should be used on (port-100000))

For example, if your mail server expects STARTTLS on port 587, you must specify 100587 in PORTAGE_ELOG_MAILURI. This triggers STARTTLS and internally maps the port to 587 with STARTTLS enabled.

### [[] Related software]

The following is a list of elog related software packages:

-   [[[app-portage/elogv]](https://packages.gentoo.org/packages/app-portage/elogv)[]] - Curses based utility to parse the contents of elogs.
-   [[[app-portage/elogviewer]](https://packages.gentoo.org/packages/app-portage/elogviewer)[]] - Python based elog viewer.

## [[] Build logs]

Package build logs can be saved to disk or mailed to a remote recipient, by setting variables in [[make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")]. This allows system administrators to review builds later.

By default, when [emerge] is running, Portage temporarily saves the build log of a package to [/var/tmp/portage/\<category\>/\/temp/build.log]. The build directory will be deleted when [emerge] finishes successfully, so successful build logs will be lost. If a build fails however, the logs will be retained, so the [build.log] will still be available for [attaching to support tickets](https://wiki.gentoo.org/wiki/Attach_the_logs_to_the_bug_ticket "Attach the logs to the bug ticket").

*n.b.* The [build.log] may be followed by an extra extension if `compress-build-logs` is set in `FEATURES`. The default `PORTAGE_TMPDIR` is [/var/tmp], adjust path accordingly if it is set to something different in [make.conf].

### [[] Always save build logs]

To enable saving build logs, edit [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] and set `PORTAGE_LOGDIR` to a location where the log files should be stored:

[FILE] **`/etc/portage/make.conf`**

    PORTAGE_LOGDIR="/var/log/portage"

It is customary to choose [/var/log/portage] as the location for log files, because it is where the elog subsystem\'s [elog] directory would be if `PORTAGE_LOGDIR` has been previously empty or unset.

A number of `FEATURES` settings may be set in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] which influence how Portage handles build logs:

-   With `binpkg-logs` set, even binary package deployments will have their logs saved.
-   When `clean-logs` is set, regular log file clean operations are executed. The command that is executed is defined by `PORTAGE_LOGDIR_CLEAN` and defaults to a retention of the files of 7 days.
-   With `split-elog` set, elog notices are stored in category-named subdirectories of `$/elog`
-   WIth `split-log` set, build logs are stored in category-named subdirectories of `$/build`

Until Portage version 2.3.53, `PORTAGE_LOGDIR` variable used to be named `PORT_LOGDIR`. This old name is now deprecated.

### [[] Cleaning up]

When `clean-logs` is enabled in the `FEATURES` variable of [/etc/portage/make.conf], Portage will execute the command defined by `PORTAGE_LOGDIR_CLEAN` after every build or unmerge operation. By default, the following command is used:

[FILE] **`/usr/share/portage/config/make.globals`**

    PORTAGE_LOGDIR_CLEAN="find \"\$\" -type f ! -name \"summary.log*\" -mtime +7 -delete"

When defining a custom command, do not forget to *escape* the `PORTAGE_LOGDIR` variable (or immediately hard code the right location).

Until Portage version 2.3.53, `PORTAGE_LOGDIR_CLEAN` variable used to be named `PORT_LOGDIR_CLEAN`. This old name is now deprecated.

## [[] Other Portage log files]

Portage also can have log files in [/var/log/emerge.log], and [/var/log/emerge-fetch.log].

## [[] See also]

-   [Elogv](https://wiki.gentoo.org/wiki/Elogv "Elogv") --- a curses-based tool that parses the contents of [elogs] created by Portage.

## [[] External resources]

-   [Sven Vermeulen](https://wiki.gentoo.org/wiki/User:SwifT "User:SwifT"). [\"Underestimated or underused: Portage (e)logging \"](http://blog.siphos.be/2013/09/underestimated-or-underused-portage-elogging/), September 25th, 2013. Retrieved on May 30th, 2019.