**Resources**

[[]][Home](https://community.kde.org/Baloo)

[[]][Package information](https://packages.gentoo.org/packages/kde-frameworks/baloo)

[[]][Bugs (upstream)](https://bugs.kde.org/)

[[]][GitWeb](https://invent.kde.org/frameworks/baloo)

**Baloo** is a file-indexing and search framework provided as part of the [KDE](https://wiki.gentoo.org/wiki/KDE "KDE")/Plasma software suite.

Baloo includes a [daemon](https://wiki.gentoo.org/wiki/Category:Daemons "Category:Daemons") for file indexing, a search framework (that powers for example the [Dolphin](https://wiki.gentoo.org/wiki/Dolphin "Dolphin") file manager\'s search functionality), and a [commnd-line](https://wiki.gentoo.org/wiki/Shell "Shell") utility (described below).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [systemd]](#systemd)
        -   [[2.2.2] [XDG autostart]](#XDG_autostart)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Check index size]](#Check_index_size)
    -   [[3.3] [Purge index]](#Purge_index)
    -   [[3.4] [Check indexing status]](#Check_indexing_status)
    -   [[3.5] [Disable indexing]](#Disable_indexing)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Baloo is using 100% of one CPU core]](#Baloo_is_using_100.25_of_one_CPU_core)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Installation]

The [[[kde-frameworks/baloo]](https://packages.gentoo.org/packages/kde-frameworks/baloo)[]] package won\'t usually be [emerged](https://wiki.gentoo.org/wiki/Emerge "Emerge") manually, but pulled in by installing a piece of software that depends on it.

### [USE flags]

### [USE flags for] [kde-frameworks/baloo](https://packages.gentoo.org/packages/kde-frameworks/baloo) [[]] [Framework for searching and managing metadata]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 20:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Configuration]

In KDE/Plasma, some basic Baloo settings can be managed through a [GUI](https://wiki.gentoo.org/wiki/Category:GUI_software "Category:GUI software") by opening the *Application Launcher*, clicking on the *System* category, then opening the *System Settings* tool. Scroll down the list of settings to select the *Search* entry.

This dialogue contains an option to enable or disable Baloo indexing for the current user\'s KDE/plasma sessions.

### [Files]

-   [\~/.config/baloofilerc] - User-specific configuration file. See [upstream documentation](https://community.kde.org/Baloo/Configuration) for details.
-   [/etc/xdg/autostart/baloo_file.desktop] - XDG autostart file to allow the Baloo daemon to automatically run upon user login (for supported [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment")). If this behavior is not desired, this file may be modified by the system administrator to change this behavior system-wide as required, for example by removing the auto start line for certain desktop environments.

### [Services]

#### [systemd]

On systemd systems, the Baloo utility can be controlled as [user service](https://wiki.gentoo.org/wiki/Systemd#User_services "Systemd") and configured to automatically run in the background.

To disable the Baloo systemd user service:

`user `[`$`]`systemctl --user disable --now kde-baloo.service`

#### [XDG autostart]

When [[[kde-frameworks/baloo]](https://packages.gentoo.org/packages/kde-frameworks/baloo)[]] is installed, it will place a [baloo_file.desktop] [.desktop file](https://wiki.gentoo.org/wiki/.desktop_files ".desktop files") in [/etc/xdg/autostart]. This will allow some [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") to start baloo during desktop session startup.

For information on how to enable or disable the autostarting of services provided by through the XDG autostart mechanism, refer to the appropriate desktop environment documentation.^[\[1\]](#cite_note-1)^

## [Usage]

### [Invocation]

Baloo includes a userspace utility to manage its functionality:

`user `[`$`]`balooctl6 --help`

    Usage: balooctl6 [options] command status enable disable purge suspend resume check index clear config monitor indexSize failed

    Options:
      -f, --format <format>  Output format <multiline|json|simple>.
                             The default format is "multiline".
                             Only applies to "balooctl status <file>"
      -v, --version          Displays version information.
      -h, --help             Displays help on commandline options.
      --help-all             Displays help including Qt specific options.

    Arguments:
      command                The command to execute
      status                 Print the status of the indexer
      enable                 Enable the file indexer
      disable                Disable the file indexer
      purge                  Remove the index database
      suspend                Suspend the file indexer
      resume                 Resume the file indexer
      check                  Check for any unindexed files and index them
      index                  Index the specified files
      clear                  Forget the specified files
      config                 Modify the Baloo configuration
      monitor                Monitor the file indexer
      indexSize              Display the disk space used by index
      failed                 Display files which could not be indexed

To avoid any possible confusion, note that this command used to be named [balooctl] but in Gentoo since plasma 6 the command is [balooctl6].^[\[2\]](#cite_note-2)^

### [Check index size]

Disk space consumed by index can be displayed using:

`user `[`$`]`balooctl6 indexSize`

    File Size: 6.27 GiB
    Used:      3.66 GiB

               PostingDB:     978.16 MiB    26.124 %
              PositionDB:       1.46 GiB    39.929 %
                DocTerms:     875.02 MiB    23.369 %
        DocFilenameTerms:     116.66 MiB     3.116 %
           DocXattrTerms:            0 B     0.000 %
                  IdTree:      31.55 MiB     0.843 %
              IdFileName:     133.30 MiB     3.560 %
                 DocTime:      81.82 MiB     2.185 %
                 DocData:      27.00 MiB     0.721 %
       ContentIndexingDB:            0 B     0.000 %
             FailedIdsDB:       4.00 KiB     0.000 %
                 MTimeDB:       5.71 MiB     0.153 %

### [Purge index]

To free up disk space consumed by the index, issue:

`user `[`$`]`balooctl6 purge`

    Stopping the File Indexer .... - done
    Deleted the index database
    Restarting the File Indexer

### [Check indexing status]

`user `[`$`]`balooctl6 status`

    ...
    Baloo File Indexer is running
    Indexer state: Indexing file content
    ...

### [Disable indexing]

`user `[`$`]`balooctl6 disable`

## [Troubleshooting]

### [][Baloo is using 100% of one CPU core]

When Baloo is running it will use 100% of one CPU core. To disable indexing (which will impact the ability to search for files) see the [disable section](#Disable_indexing) above.

## [See also]

-   [Plasma](https://wiki.gentoo.org/wiki/Plasma "Plasma") --- a free software community, producing a wide range of applications including the popular Plasma desktop environment.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://specifications.freedesktop.org/autostart-spec/latest/](https://specifications.freedesktop.org/autostart-spec/latest/)]]
2.  [[[↑](#cite_ref-2)] [[https://community.kde.org/Baloo#Plasma_6_versions](https://community.kde.org/Baloo#Plasma_6_versions)]]