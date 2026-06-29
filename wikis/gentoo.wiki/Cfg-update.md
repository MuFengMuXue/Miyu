**Resources**

[[]][Home](https://github.com/rich0/cfg-update)

**Article status**

[[]]This article has some todo items:\

-   Finish usage

[cfg-update] is a utility used on Gentoo to manage configuration file updates. It allows system administrators to review then accept or reject upstream configuration changes, which frequently happens when packages are updated. It is has an integrated backup system which does not require an external version control system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/cfg-update](https://packages.gentoo.org/packages/app-portage/cfg-update) [[]] [Easy to use GUI & CLI alternative for etc-update]

  ----------------------------------------------- ---------------------
  [`X`](https://packages.gentoo.org/useflags/X)   Add support for X11
  ----------------------------------------------- ---------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-08-02 17:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-portage/cfg-update`

## [Configuration]

Configuration is done through [/etc/cfg-update.conf]. The most common option users need to change is the `MERGE_TOOL` option to the preferred merge tool of the system. Supported tools include meld, xxdiff, kdiff3, gvimdiff, tkdiff, vimdiff, sdiff and imediff.

## [Usage]

### [Invocation]

[cfg-update] must be run as the root user. The first time it runs, it creates a portage hook to update its index and will remind of running the update command.

`user `[`$`]`cfg-update --help`

    USAGE     cfg-update [runmode] [options]              (version 1.8.2-r1)

    RUNMODES
      -l, --list
              List updates (._cfg0000_* files) including modification state
              Examples: cfg-update -l         : list updates on localhost
                        cfg-update -l -h1 -l  : list updates on remote host 1
                        cfg-update -l -h0-100 : list localhost + remote host 1-100

      -u, --update
              Update the protected configuration files
              Examples: cfg-update -u         : update localhost
                        cfg-update -up        : update pretend-only
                        cfg-update -ua        : update automatic-only
                        cfg-update -um        : update manual-only
                        cfg-update -u -h1     : update remote host 1
                        cfg-update -u -h0-100 : update localhost + remote host 1-100

      -b, --backups
              List backup files, with numbers for use with the -r option
              The backups are stored in /var/lib/cfg-update/backups
              Examples: cfg-update -b         : list all backups localhost
                        cfg-update -b -h1     : list all backups remote host 1

      -r [x], --restore [x]
              Restore a backup by using a number [x] from the -b output
              Examples: cfg-update -r10       : restore backup 10 on localhost
                        cfg-update -r10 -h1   : restore backup 10 on remote host 1

      --mount
              Mounts the remote hosts specified in /etc/cfg-update.hosts

      --check
              Checks the remote hosts for problems and shows their status

      --unmount
              Unmounts the remote hosts specified in /etc/cfg-update.hosts

    OPTIONS
      -a, --automatic-only
              Skips all manual updates (for use with cronjobs)

      -m, --manual-only
              Skips all automatic updates

      -h [x|x-y], --host [x|x-y]
              Includes sshfs mounted remote hosts (combine with -u, -l, -b, -r)
              With this option you can perform updates on multiple remote machines
              from a single location. Listing updates, updating, listing backups
              and restoring backups on remote machines are all possible.
              For configuration info see: /etc/cfg-update.hosts

      -t [tool], --tool [tool]
              Set mergetool, overrides the default setting in /etc/cfg-update.conf
              GUI tools: xxdiff, kdiff3, meld, tkdiff, gtkdiff, gvimdiff
              CLI tools: vimdiff, sdiff, imediff2

      -p, --pretend
              Pretend, simulate the update session without changing anything

      -v, --verbose
              Verbose output, shows all file operations and unhides STDERR messages

      -d, --debug
              Debugging mode, unhides STDERR messages and shows subroutine tags

    SPECIAL OPTIONS
      -i, --index (--paludis)
              Creates or updates the checksum-index if neccesary.
              The index is neccesary for determining which files can be updated
              automatically. The index needs to be updated before installing new
              packages. A hook will be created in /etc/portage/bashrc so you don't
              have to do this manually. When Paludis is installed, cfg-update will
              add a hook to /usr/share/paludis/hooks/install_all_pre/cfg-update.bash
              The Portage hook will execute: cfg-update --index
              The Paludis hook will execute: cfg-update --index --paludis

      -s, --show-protected-dirs
              Shows directories protected by the CONFIG_PROTECT system variable
              cfg-update searches for updates in the CONFIG_PROTECT directories

      --optimize-backups
              Backups can be used for automatic 3-way merging. This option creates
              extra backups to maximize the chances of future automatic updates

    SETTINGS (from /etc/cfg-update.conf)
      Stage1  >>  Automatic replacing     - enabled
      Stage2  >>  Automatic 3-way merging - enabled
      Stage3  >>  Manual 3-way merging    - disabled (not supported by imediff2)
      Stage4  >>  Manual 2-way merging    - enabled
      Stage5  >>  Manual replacing        - enabled

    USAGE INFORMATION
      Start (as root) with "cfg-update -l" to list all the ._cfg0000_* files,
      followed by "cfg-update -u" to update the current config files one by one.
      You can also use the --pretend mode with "cfg-update -u -p" to see how
      cfg-update will handle the files without actually updating them.
      Take a look in the manpage for more usage examples...

    MERGETOOL INFORMATION
      /usr/bin/imediff2  (manual 3-way merging is not supported)
      In imediff2 you select the lines that you want to keep.
      When done, try saving the merged result as *.merge
      or save the merged result over the current config file.
      When you exit imediff2, cfg-update will finish the update...

    For more info, type "man cfg-update"
    or visit http://people.zeelandnet.nl/xentric

To update system files:

`root `[`#`]`cfg-update -u`

    cfg-update -u
    Searching for updates...

    << Stage1 >> 1 files in queue for automatic replacing, starting...

    (1/1)  /etc/wgetrc  *Unmodified File
      This file has not been changed and does not contain custom settings.
      Replacing it with /etc/._cfg0000_wgetrc
    Update complete...

    << Stage2 >> 0 files in queue for automatic 3-way merging, skipping...

    << Stage3 >> imediff2 does not support 3-way merging, skipping...

    << Stage4 >> 0 files in queue for manual 2-way merging, skipping...

    << Stage5 >> 0 files in queue for manual updating, skipping...

    All files have been updated...

## [See also]

-   [dispatch-conf (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Tools#dispatch-conf "Handbook:AMD64/Portage/Tools")
-   [Dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf") --- a utility included with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), used to safely and conveniently manage configuration files after package updates.