**Resources**

[[]][GitHub](https://github.com/vaeth/eix/)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/eix)

**eix** is a set of utilities for searching and diffing local [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") using a binary cache. The cache allows relatively fast queries, and should be generated after each [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") sync.

[eix] is both more efficient and more flexible than the [emerge \--search] command. [eix] comes with colorized output which helps users easily find the needed package information.

For more information on [eix], read its [man page](https://wiki.gentoo.org/wiki/Man_page "Man page"): [man eix].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Environment variables]](#Environment_variables)
    -   [[2.3] [Managing the cache]](#Managing_the_cache)
        -   [[2.3.1] [Updating the cache manually]](#Updating_the_cache_manually)
        -   [[2.3.2] [Updating the cache with each sync]](#Updating_the_cache_with_each_sync)
            -   [[2.3.2.1] [Method 1: Using Portage\'s postsync hook]](#Method_1:_Using_Portage.27s_postsync_hook)
            -   [[2.3.2.2] [Method 2: Using eix-sync]](#Method_2:_Using_eix-sync)
    -   [[2.4] [Adding remote repositories to the cache]](#Adding_remote_repositories_to_the_cache)
    -   [[2.5] [Using tmpfs cache]](#Using_tmpfs_cache)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Searching for packages]](#Searching_for_packages)
        -   [[3.1.1] [Simple search]](#Simple_search)
        -   [[3.1.2] [Searching for installed packages]](#Searching_for_installed_packages)
        -   [[3.1.3] [Searching in package descriptions]](#Searching_in_package_descriptions)
        -   [[3.1.4] [Searching in package categories]](#Searching_in_package_categories)
        -   [[3.1.5] [Searching in only the main (::gentoo) repository]](#Searching_in_only_the_main_.28::gentoo.29_repository)
        -   [[3.1.6] [Searching for installed packages in a specific package repository]](#Searching_for_installed_packages_in_a_specific_package_repository)
        -   [[3.1.7] [Searching by license]](#Searching_by_license)
        -   [[3.1.8] [Excluding results]](#Excluding_results)
        -   [[3.1.9] [Searching for installed obsolete packages]](#Searching_for_installed_obsolete_packages)
    -   [[3.2] [Format strings]](#Format_strings)
        -   [[3.2.1] [Category/name-version and license]](#Category.2Fname-version_and_license)
        -   [[3.2.2] [Conditional blocks]](#Conditional_blocks)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Show changes since last sync]](#Show_changes_since_last_sync)
    -   [[4.2] [Have Eix and Emerge use the same color palette]](#Have_Eix_and_Emerge_use_the_same_color_palette)
    -   [[4.3] [Tmux and Screen users should disable status line updates]](#Tmux_and_Screen_users_should_disable_status_line_updates)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/eix](https://packages.gentoo.org/packages/app-portage/eix) [[]] [Search and query ebuilds]

  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)     Build with upstream\'s CXXFLAGS/LDFLAGS for debugging support; not recommended for normal use.
  [`doc`](https://packages.gentoo.org/useflags/doc)         Create description of the eix cache file additionally in html format
  [`nls`](https://packages.gentoo.org/useflags/nls)         Add Native Language Support (using gettext - GNU locale utilities)
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)   Compile in support for portage\'s sqlite backend; to actually use it you need additional configuration of portage and eix
  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-portage/eix]](https://packages.gentoo.org/packages/app-portage/eix)[]]:

`root `[`#`]`emerge --ask app-portage/eix`

## [Configuration]

### [Files]

-   [/etc/eix-sync.conf] - Stores commands and configurations for [eix-sync]
-   [/etc/eixrc] - [eix]\'s global configuration file.
-   [\~/.eixrc] - [eix]\'s per-user configuration file.

### [Environment variables]

-   `EIXRC` - If this variable can set a new location for [eix]\'s global configuration file (see above).
-   `EIX_SYNC_OPTS`, `EIX_SYNC_CONF`, `EIX_REMOTE_OPTS`, `EIX_LAYMAN_OPTS`, `EIX_TEST_OBSOLETE_OPTS` - Security relevant variables. See the man page for more details.

### [Managing the cache]

#### [Updating the cache manually]

After the installation has finished, it is important to update the cache to index all packages on the system. Running the following command will update the local [eix] cache:

`root `[`#`]`eix-update`

** Tip**\
[eix-update] can utilize the metadata cache generated by [emerge \--regen] for a speedup and better accuracy. To enable this, set the `OVERLAY_CACHE_METHOD` variable to `assign` in the [/etc/eixrc/01-cache] file.\
\

[FILE] **`/etc/eixrc/01-cache`Setting OVERLAY_CACHE_METHOD**

    OVERLAY_CACHE_METHOD="assign"

#### [Updating the cache with each sync]

After each update of the Portage tree, the cache needs to be updated.

The following two alternative methods are used to automatically update the cache with each sync.

** Note**\
Method 1 is preferred, as it is able to work in combination with all possible [emaint sync] commands (see [Portage plug-in sync system specification](https://wiki.gentoo.org/wiki/Project:Portage/Sync "Project:Portage/Sync")).

##### [][Method 1: Using Portage\'s postsync hook]

After all repository syncs, all executable scripts in the directory [/etc/portage/postsync.d/] are called. First, create the directory:

`root `[`#`]`mkdir --parents /etc/portage/postsync.d`

Then create the following script:

[FILE] **`/etc/portage/postsync.d/eix`**

    #!/usr/bin/env bash
    if [[ -e /var/cache/eix/portage.eix ]]; then
        rsync -ca /var/cache/eix/portage.eix /var/cache/eix/previous.eix;
    fi
    eix-update
    if [[ -e /var/cache/eix/previous.eix ]]; then
        eix-diff;
    fi

Finally, make the file executable:

`root `[`#`]`chmod +x /etc/portage/postsync.d/eix`

** Note**\
From `0.36.7-r2` (available 2024-12-04), eix will install a symlink that hooks [eix-postsync] into portage\'s postsync via [/etc/portage/postsync.d]. If you need to execute [eix-diff] after syncing, then the script should only include the [eix-diff] part; otherwise, there may be an issue where [eix-diff] has no output because the diff is empty after implicitly running [eix-update] twice.

[FILE] **`/etc/portage/postsync.d/99-eix-diff`Show sync diff status**

    #!/usr/bin/env bash
    if [[ -e /var/cache/eix/previous.eix ]]; then
        eix-diff;
    fi

If additional ebuild repositories are used, [eix-update] can become quite slow, as many of them do not provide pregenerated caches. To speed up the process of [eix-update], Portage can be hooked to regenerate the cache for each repository, after each sync.

An example for this is provided in the [/usr/share/portage/config/repo.postsync.d/example] file. This example can be copied to [/etc/portage/repo.postsync.d/egencache] and made executable. Note the `--jobs` argument to [egencache] - setting this to the output of [nproc] (as shown below) causes it to use all available system cores. If less impact on system resources is desired, this can be reduced to a smaller number.

[FILE] **`/etc/portage/repo.postsync.d/egencache`**

    #!/bin/sh

    # The repository name.
    repository_name=$
    # The URI to which the repository was synced.
    sync_uri=$
    # The path to the repository.
    repository_path=$

    # Portage assumes that a hook succeeded if it exits with 0 code. If no
    # explicit exit is done, the exit code is the exit code of last spawned
    # command. Since our script is a bit more complex, we want to control
    # the exit code explicitly.
    ret=0

    if [ -n "$" ]; then
            # Repository name was provided, so we're in a post-repository hook.
            echo "* In post-repository hook for $"
            echo "** synced from remote repository $"
            echo "** synced into $"

            # Gentoo comes with pregenerated cache but the other repositories
            # usually don't. Generate them to improve performance.
            if [ ! -d "$/metadata/md5-cache" ]; then
                    if ! egencache --update --repo="$" --jobs=$(nproc)
                    then
                            echo "!!! egencache failed!"
                            ret=1
                    fi
            fi
    fi

    # Return explicit status.
    exit "$"

##### [Method 2: Using eix-sync]

Alternatively, [eix-sync] can be used from [eix] itself:

`root `[`#`]`eix-sync`

The above command is a shorthand way to running these commands sequentially:

`root `[`#`]`emerge --sync `

`root `[`#`]`cp -a /var/cache/eix/portage.eix /var/cache/eix/previous.eix `

`root `[`#`]`eix-update `

`root `[`#`]`eix-diff `

If layman is used to manage [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"), then it is recommended to configure [eix] to synchronize layman-managed repositories too:

[FILE] **`/etc/eix-sync.conf`**

    # Sync all ebuild repositories with layman -S
    *

In standard configuration, [emerge \--sync] [calls](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository") [emaint sync \--auto] that updates other repositories as well. Finally, to speed up the [eix-update] step, [eix-sync] can run [emerge \--regen] after syncing ebuild repositories:

[FILE] **`/etc/eix-sync.conf`**

    # Regenerate ebuild repository metadata
    @emerge --regen || true

### [Adding remote repositories to the cache]

To be able to search for packages in remote repositories/overlays not yet installed, fetch caches of them (by default from [http://gpo.zugaina.org/eix_cache/eix-cache.tbz2](http://gpo.zugaina.org/eix_cache/eix-cache.tbz2)) and store them locally:

** Important**\
This **must** be run as root for the first invocation, otherwise the files it downloads will have incorrect ownership.

`root `[`#`]`eix-remote update`

To do this automatically on each [eix-sync], add the following:

[FILE] **`/etc/eix-sync.conf`**

    @StatusInfo "Downloading remote1"
    @eix-remote fetch1

It will then be possible to search all overlays using the `-R` option to **eix**:

`user `[`$`]`eix -R`

    * dev-scheme/termite
         Available versions:  (~)0.15-r1
         Homepage:            https://code.google.com/p/termite/
         Description:         Erlang-style concurrency for Gambit Scheme

    * x11-terms/termite
         Available versions:  (~)6[1] (~)7[1] (~)7[3] (~)8[1] (~)8[3] (~)9[1] (~)9[3] (~)10[1] (~)10[3] (~)11[1] (~)11[3] (~)12[1] (~)13[1] (~)13[2] **9999[1] **9999[2] **9999[3] (~)9999[4] (~)9999[5]
         Homepage:            https://github.com/thestinger/termite
         Description:         A keyboard-centric VTE-based terminal

    [1] "eroen" layman/eroen
    [2] "gig" layman/gig
    [3] "nightmare" layman/nightmare
    [4] "SoniFrog" layman/SoniFrog
    [5] "zjpxshade" layman/zjpxshade

    Found 2 matches

### [Using tmpfs cache]

This breaks [eix] because [/var/cache/eix] is missing when [/var/cache] is mounted:

`root `[`#`]`grep /var/cache /etc/fstab`

    none /var/cache tmpfs size=512m 0 0

The simple solution is to move the [eix] cache files away from the default location:

`root `[`#`]`cat >> /etc/eixrc/00-eixrc << EOF`

    EIX_CACHEFILE=%/var/cache/eix/portage.eix
    EIX_PREVIOUS=%/var/cache/eix/previous.eix
    EIX_REMOTE1=%/var/cache/eix/eix-remote.eix
    EIX_REMOTE2=%/var/cache/eix/eix-remote2.eix
    EIX_REMOTEARCHIVE1=%/var/cache/eix/eix-remote.tar.bz2
    EIX_REMOTEARCHIVE2=%/var/cache/eix/eix-remote2.tar.bz2
    EOF

Check all new set variables:

`root `[`#`]`eix --dump | grep "EIX_CACHEFILE\|EIX_PREVIOUS\|EIX_REMOTE1\|EIX_REMOTE2\|EIX_REMOTEARCHIVE1\|EIX_REMOTEARCHIVE2"`

    EIX_CACHEFILE="%/var/cache/eix/portage.eix"
    # EIX_CACHEFILE="%/var/cache/eix/portage.eix"
    EIX_PREVIOUS="%/var/cache/eix/previous.eix"
    # EIX_PREVIOUS="%/var/cache/eix/previous.eix"
    EIX_REMOTE1="%/var/cache/eix/eix-remote.eix"
    # EIX_REMOTE1="%/var/cache/eix/eix-remote.eix"
    EIX_REMOTE2="%/var/cache/eix/eix-remote2.eix"
    # EIX_REMOTE2="%/var/cache/eix/eix-remote2.eix"
    EIX_REMOTEARCHIVE1="%/var/cache/eix/eix-remote.tar.bz2"
    # EIX_REMOTEARCHIVE1="%/var/cache/eix/eix-remote.tar.bz2"
    EIX_REMOTEARCHIVE2="%/var/cache/eix/eix-remote2.tar.bz2"
    # EIX_REMOTEARCHIVE2="%/var/cache/eix/eix-remote2.tar.bz2"

One side effect is needing to run [eix-update] after each reboot which will take a few seconds. To do so, add a [.start] script to the [/etc/local.d/] ([Local.d](https://wiki.gentoo.org/wiki/Local.d "Local.d")) directory:

[FILE] **`/etc/local.d/90_eix-update.start`**

    #!/bin/sh
    /usr/bin/logger -s "/etc/local.d/90_eix-update.start: executed"
    /usr/bin/eix-update

This will also write into the [/var/log/syslog] log file that it was executed.

Do not forget to make the file executable:

`root `[`#`]`chmod +x /etc/local.d/90_eix-update.start`

For systemd:

[FILE] **`/etc/systemd/system/eix-update.timer`**

    [Unit]
    Description=update the eix database 15min after boot

    [Timer]
    OnBootSec=15min
    OnUnitActiveSec=1d

    [Install]
    WantedBy=timers.target

And the service file:

[FILE] **`/etc/systemd/system/eix-update.service`**

    [Unit]
    Description=update the eix database 15min after boot and every day if system is running

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/eix-update
    User=portage
    Group=systemd-journal

Afterwards enable timer:

`root `[`#`]`systemctl enable eix-update.timer`

## [Usage]

### [Searching for packages]

#### [Simple search]

To find package names containing *kernel* keyword:

`user `[`$`]`eix kernel`

    * app-admin/eclean-kernel
         Available versions:  (~)0.3 }
         Homepage:            https://bitbucket.org/mgorny/eclean-kernel/
         Description:         Remove outdated built kernels

    * app-doc/linux-kernel-in-a-nutshell
         Available versions:  1
         Homepage:            http://www.kroah.com/lkn/
         Description:         Linux Kernel in a Nutshell: A Desktop Quick Reference

    * games-misc/fortune-mod-kernelcookies
         Available versions:  9 }
         Homepage:            http://www.schwarzvogel.de/software-misc.shtml
         Description:         A collection of funny lines from the Linux kernel

    * net-fs/openafs-kernel
         Available versions:  1.4.14 (~)1.4.14.1 (~)1.6.0 (~)1.6.1_pre1 (~)1.6.1 }
         Homepage:            http://www.openafs.org/
         Description:         The OpenAFS distributed file system kernel module

    * sec-policy/selinux-kerneloops
         Available versions:  [M]2.20120215 [M](~)2.20120215-r1
         Homepage:            http://www.gentoo.org/proj/en/hardened/selinux/
         Description:         SELinux policy for kerneloops

    * sys-cluster/drbd-kernel
         Available versions:  8.0.16 (~)8.3.6 (~)8.3.8.1 }
         Homepage:            http://www.drbd.org
         Description:         mirror/replicate block-devices across a network-connection

    * sys-cluster/gfs-kernel
         Available versions:  2.03.09 }
         Homepage:            http://sources.redhat.com/cluster/wiki/
         Description:         GFS kernel module

    [I] sys-kernel/genkernel
         Available versions:  3.4.16 (~)3.4.16.1 3.4.20 (~)3.4.21.2 (~)3.4.22.1 (~)3.4.23.1 (~)3.4.24 3.4.24_p1 (~)3.4.25.1 (~)3.4.26 (~)3.4.27 (~)3.4.28 (~)3.4.29 (~)3.4.32 (~)3.4.33.1 (~)3.4.34 (~)3.4.35 (~)3.4.36 **9999 }
         Installed versions:  3.4.36(01:30:10 AM 07/01/2012)(crypt -cryptsetup -ibm -selinux)
         Homepage:            http://www.gentoo.org
         Description:         Gentoo automatic kernel building scripts

    Found 8 matches.

** Note**\
The displayed versions are colorized and have the following meanings:

[stable]\
[unstable or testing and unkeyworded]\
[unkeyworded or masked]

[![Eix-search.png](/images/thumb/5/5c/Eix-search.png/300px-Eix-search.png)](https://wiki.gentoo.org/wiki/File:Eix-search.png)

[](https://wiki.gentoo.org/wiki/File:Eix-search.png "Enlarge")

#### [Searching for installed packages]

Search for installed packages using the `-I` option:

`user `[`$`]`eix -I kernel`

    [I] sys-kernel/genkernel
         Available versions:  3.4.16 (~)3.4.16.1 3.4.20 (~)3.4.21.2 (~)3.4.22.1 (~)3.4.23.1 (~)3.4.24 3.4.24_p1 (~)3.4.25.1 (~)3.4.26 (~)3.4.27 (~)3.4.28 (~)3.4.29 (~)3.4.32 (~)3.4.33.1 (~)3.4.34 (~)3.4.35 (~)3.4.36 **9999 }
         Installed versions:  3.4.36(01:30:10 AM 07/01/2012)(crypt -cryptsetup -ibm -selinux)
         Homepage:            http://www.gentoo.org
         Description:         Gentoo automatic kernel building scripts

#### [Searching in package descriptions]

To search in package descriptions use the `-S` option. It is possible to print out results in a compact list using `-c`:

`user `[`$`]`eix -S -c corba`

    [N] dev-ada/polyorb (~2.1.0): A CORBA implementation for Ada
    [I] dev-libs/libIDL (0.8.14@07/10/11): CORBA tree builder
    [N] gnome-base/libbonobo (2.24.3): GNOME CORBA framework
    [I] gnome-base/orbit (2.14.19-r1(2)@07/10/11): ORBit2 is a high-performance CORBA ORB
    [N] net-misc/mico (~2.3.13-r5): A freely available and fully compliant implementation of the CORBA standard
    [N] net-misc/omniORB (4.1.4-r1): A robust, high-performance CORBA 2 ORB

#### [Searching in package categories]

Search for certain category using the `-C` option and print out the results in a compact list (`-c`):

`user `[`$`]`eix -C -c app-officeext`

    [N] app-officeext/barcode (1.3.5.0): Extension for reading barcodes
    [N] app-officeext/ct2n (1.4.0): Extension for converting text to numbers
    [N] app-officeext/dmaths (3.4.2.2): Mathematics Formula Editor Extension
    [N] app-officeext/languagetool (1.7): Style and Grammar Checker for libreoffice
    [N] app-officeext/ooo2gd (3.0.0): Extension for export to Google docs, zoho and WebDAV
    [N] app-officeext/sun-templates (~1.0.0): Collection of sun templates for various countries.
    [N] app-officeext/texmaths (0.35): LaTeX Equation Editor for LibreOffice

#### [][Searching in only the main (::gentoo) repository]

The main Gentoo repository has an eix overlay index of 0 (zero), and so can be specified by the `--only-in-overlay` option.

`user `[`$`]`eix -C games-board --only-in-overlay 0`

    [N] games-board/ace (~1.4-r2): DJ Delorie's Ace of Penguins solitaire games
    [N] games-board/atakks (~1.0-r2): Clone of Ataxx
    [N] games-board/awale (~1.6): Free Awale - The game of all Africa
    [N] games-board/biloba (~0.9.3-r2): a board game, up to 4 players, with AI and network
    [N] games-board/blokish (~0.9.4-r3): Open source clone of the four-player board game Blokus
    [N] games-board/cgoban (~1.9.14-r2): A Go-frontend
    ...

#### [Searching for installed packages in a specific package repository]

The [eix-update] command will regenerate the binary cache from the local repositories and list the index numbers in square brackets before each overlay name. The output will look similar to the following:

`user `[`$`]`eix -C games-board --only-in-overlay 0`

    Reading Portage settings...
    Building database (/var/cache/eix/portage.eix)...
    [0] "gentoo" /var/db/repos/gentoo/ (cache: metadata-md5-or-flat)
         Reading category 184|184 (100) Finished
    [1] "another-brave-overlay" /var/db/repos/another-brave-overlay (cache: parse|ebuild*3.0.24#metadata-md5#metadata-flat#assign)
         Reading category 184|184 (100) Finished
    [2] "guru" /var/db/repos/guru (cache: parse|ebuild*3.0.24#metadata-md5#metadata-flat#assign)
         Reading category 184|184 (100) Finished
    [3] "hyproverlay" /var/db/repos/hyproverlay (cache: parse|ebuild*3.0.24#metadata-md5#metadata-flat#assign)
         Reading category 184|184 (100) Finished
    [4] "steam-overlay" /var/db/repos/steam-overlay (cache: parse|ebuild*3.0.24#metadata-md5#metadata-flat#assign)
         Reading category 184|184 (100) Finished
    Applying masks...
    Calculating hash tables...
    Writing database file /var/cache/eix/portage.eix...

The overlay *name* or the *index number* can be used with the `--only-in-overlay` option to search specific package repositories for installed packages.

For example, to use eix to search the guru repository from the repository cache listing above, the index number of 2 can be used with the `--only-in-overlay` option:

`user `[`$`]`eix --installed --only-in-overlay 2`

A package name and the overlay name can also be specified. To search for an installed package using the overlay name:

`user `[`$`]`eix mangohud --installed --only-in-overlay guru`

#### [Searching by license]

Search for packages that are licensed under a specific license or subset of licenses using the `-L` option. For example\'s sake let the license be an End-User License Agreement (a type of proprietary license), or EULA and let\'s limit the results to the games-rpg category (as without a category limitation the results would be too long to fit comfortably in this article):

`user `[`$`]`eix -Cc games-rpg -L "EULA"`

    [N] games-rpg/arx-fatalis-data ((~)1.21-r3): Arx Fatalis data files
    [N] games-rpg/nwn (1.69-r1): role-playing game set in a huge medieval fantasy world of Dungeons and Dragons
    [N] games-rpg/nwn-data (1.29-r5): Neverwinter Nights Data Files
    [N] games-rpg/runescape-launcher (2.2.4): Official RuneScape NXT client launcher

#### [Excluding results]

To exclude results that, for example, have EULA in their license field using the `--not` option:

`user `[`$`]`eix --not -L "EULA"`

(output not shown as it is too long).

#### [Searching for installed obsolete packages]

Search for obsolete packages on the system using the [eix-test-obsolete] command (It will in fact search for packages not installed but mentioned in the config files.):

`user `[`$`]`eix-test-obsolete`

    No non-matching entries in /etc/portage/package.keywords.
    Non-matching entries in /etc/portage/package.accept_keywords:

    net-wireless/iwl5000-code ~amd64
    app-text/xpdf ~amd64
    --

    No non-matching entries in /etc/portage/package.mask.
    No non-matching entries in /etc/portage/package.unmask.
    No non-matching or empty entries in /etc/portage/package.use.
    No non-matching or empty entries in /etc/portage/package.env.
    No non-matching or empty entries in /etc/portage/package.license.
    No non-matching or empty entries in /etc/portage/package.cflags.
    The names of all installed packages are in the database.

    Redundant in /etc/portage/package.keywords:

    ... considered as REDUNDANT_IF_WEAKER
    [I] www-client/firefox-bin (14.0.1@02/08/12): Firefox Web Browser
    [I] www-client/opera-next (12.50.1546@17/08/12): A fast and secure web browser and Internet suite
    [N] www-client/seamonkey-bin (2.11): Mozilla Application Suite - web browser, email, HTML editor, IRC
    Found 3 matches.

    ... considered as REDUNDANT_IF_NO_CHANGE
    [I] app-laptop/laptop-mode-tools (1.60-r1@18/01/12): Linux kernel laptop_mode user-space utilities
    [I] media-sound/ncmpc (0.20@02/04/12): A ncurses client for the Music Player Daemon (MPD)
    [I] media-sound/ncmpcpp (0.5.10@02/04/12): An ncurses mpd client, ncmpc clone with some new features, written in C++
    [N] media-sound/pms ((~)0.42): Practical Music Search: an open source ncurses client for mpd, written in C++
    [I] www-client/opera (12.01.1532@02/08/12): A fast and secure web browser and Internet suite
    [N] www-client/seamonkey-bin (2.11): Mozilla Application Suite - web browser, email, HTML editor, IRC
    [I] www-plugins/adobe-flash (11.2.202.238@18/08/12): Adobe Flash Player
    [I] x11-misc/dclock (2.2.2_p4@02/04/12): Digital clock for the X window system.
    [I] x11-misc/xosview (1.9.3@29/04/12): X11 operating system viewer
    [I] x11-wm/fvwm (2.6.5[2]@12/05/12): An extremely powerful ICCCM-compliant multiple virtual desktop window manager
    [1] "mpd" /var/lib/layman/mpd
    [2] "testing" /usr/local/portage

    Found 10 matches.

    Not installed but in /etc/portage/package.keywords:
    [N] media-sound/pms ((~)0.42): Practical Music Search: an open source ncurses client for mpd, written in C++
    [N] www-client/seamonkey-bin (2.11): Mozilla Application Suite - web browser, email, HTML editor, IRC
    [N] x11-libs/libaosd ((~)0.2.7): An advanced on screen display (OSD) library
    [N] x11-plugins/wmtime ((~)1.0_beta2_p10): applet which displays the date and time in a dockable tile
    Found 5 matches.

    No  redundant  entries in /etc/portage/package.mask
    No uninstalled entries in /etc/portage/package.mask
    No  redundant  entries in /etc/portage/package.unmask
    No uninstalled entries in /etc/portage/package.unmask
    Skipping check:  redundant  entries in /etc/portage/package.use
    Skipping check: uninstalled entries in /etc/portage/package.use
    Skipping check:  redundant  entries in /etc/portage/package.env
    Skipping check: uninstalled entries in /etc/portage/package.env
    No  redundant  entries in /etc/portage/package.license
    No uninstalled entries in /etc/portage/package.license
    Skipping check:  redundant  entries in /etc/portage/package.cflags
    Skipping check: uninstalled entries in /etc/portage/package.cflags

    Installed packages with a version not in the database (or masked):
    [D] sys-fs/udev (171-r6@26/05/12 -> ??): Linux dynamic and persistent device naming support (aka userspace devfs)
    [D] x11-misc/xmobar (0.13@21/03/12 -> ~0.14): A Minimalistic Text Based Status Bar
    Found 2 matches.

### [Format strings]

This is probably the most powerful aspect of [eix], but the documentation is hard to understand. [eix] has a mini-language for specifying more precise queries and output formats than are possible using only the basic options. The format string is specified as the option argument to the `--format` option. There are basically two major concepts, properties and variables:

-   **Properties:** Each package has a set of associated properties that can either be printed or used as part of a predicate in a conditional block.
-   **Variables:** A variable can be any environment variable set in the environment of eix, or any of the variables printed from the output of [eix \--dump].

#### [][Category/name-version and license]

When creating distributed media [eix] can be used to output a versioned package list along with the associated license information:

`user `[`$`]`NAMEVERSION="<category>/<name>-<version>" eix -I --format 'Package: <installedversions:NAMEVERSION> | License: <licenses>\n'`

#### [Conditional blocks]

Conditional blocks take can 3 forms, each with an optional RHS, each of which can be optionally negated:

[CODE] **If-then string comparison**

    TCODE

[CODE] **If-then predicate**

    TCODE

[CODE] **If-then-else string comparison**

    TCODEFCODE

[CODE] **If-then-else predicate**

    TCODEFCODE

[CODE] **Assignment**



[CODE] **Assign 1 or empty string**



## [Tips]

### [Show changes since last sync]

It is possible to show a diff of the changes since the last sync:

`root `[`#`]`cp -a /var/cache/eix/portage.eix /var/cache/eix/previous.eix `

`root `[`#`]`eix-update `

`root `[`#`]`eix-diff `

### [Have Eix and Emerge use the same color palette]

On some terminal emulators, the color palette will render Eix and Emerge with different color output. To get it back together, add this to the end of the Eix configuration:

[FILE] **`/etc/eixrc/00-eixrc`**

    COLOR_INST_VERSION="white,1;blue|33,1;%|black;green|30,1;%"

    BG0=none;
    BG1=none;
    BG2=none;
    BG3=none;

    COLORSCHEME0=0;
    COLORSCHEME1=0;
    COLORSCHEME2=0;
    COLORSCHEME3=0;

### [Tmux and Screen users should disable status line updates]

When using [tmux] with automatic window renaming enabled (that is `set -g automatic-rename on` has been ran in the [tmux] configuration file) or [screen], status line updates should be disabled. Otherwise, every time [eix-update] is ran the title of the window will be renamed to something like \"eix-update: Finished\*\".

To disable status line updates, run the following command:

`root `[`#`]`echo "NOSTATUSLINE=true" >> /etc/eixrc/00-eixrc`

## [See also]

-   [Equery](https://wiki.gentoo.org/wiki/Equery "Equery") --- a tool to make several common [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") operations simpler.
-   [packages.gentoo.org](https://wiki.gentoo.org/wiki/Packages.gentoo.org "Packages.gentoo.org") --- [https://packages.gentoo.org](https://packages.gentoo.org) (*p.g.o*) is a publicly-accessible website that provides information about all the packages available in the current [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository")
-   [Search for packages using the emerge command](https://wiki.gentoo.org/wiki/Emerge#Search_for_packages "Emerge") from [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")
-   [Useful Portage tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

## [External resources]

-   [app-portage/eix \... usage, examples, etc](https://forums.gentoo.org/viewtopic-t-1040038.html) - A forum post with many examples
-   [https://wiki.calculate-linux.org/eix](https://wiki.calculate-linux.org/eix) - A more detailed guide to using eix