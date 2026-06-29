This article will explain how to use [Git](https://wiki.gentoo.org/wiki/Git "Git") to synchronize the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository").

** Warning**\
There are two different types of ::gentoo repository available via git. The \'sync\' / metadata repositories, and the raw ones. The raw ones lack metadata, GLSAs, and news. This article uses the correct repositories.

** Important**\
GitHub does not support IPv6^[\[1\]](#cite_note-1)^ syncing. IPv6-only users should use [`https://anongit.gentoo.org/git/repo/sync/gentoo.git`](https://anongit.gentoo.org/git/repo/sync/gentoo.git) instead, or investigate a NAT64 option after confirming the steps in the rest of the article.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Setup]](#Setup)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [emerge \--sync failed]](#emerge_--sync_failed)
-   [[4] [Local Mirrors]](#Local_Mirrors)
-   [[5] [References]](#References)

## [Prerequisites]

[[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] both need to be installed. By default [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] is installed with the [[[git]](https://packages.gentoo.org/useflags/git)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]. USE flag.

`root `[`#`]`emerge --ask app-eselect/eselect-repository`

To reduce the risk of issues, it\'s recommended to sync the Gentoo repository before starting this process, and ensure that the system is using the latest [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)").

## [Setup]

Disable and remove the old Gentoo ebuild repository:

`root `[`#`]`eselect repository remove -f gentoo`

    Removing /var/db/repos/gentoo ...
    Updating repos.conf ...
    1 repositories removed

If the obsolete variable [PORTDIR](https://wiki.gentoo.org/wiki/PORTDIR "PORTDIR") is defined in [make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") (which may be the case on older Gentoo installations), remove that definition as well.

** Note**\
If the system is old enough to have `PORTDIR` set to [/usr/portage/], this is an excellent opportunity to migrate it to use [more modern paths](https://wiki.gentoo.org/wiki//usr/portage "/usr/portage"). Take note of the current profile by running [eselect profile show], then delete the definition of `PORTDIR` and any other variables in [make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") which reference paths under [/usr/portage/]. The rest of these instructions assume that this has been done if necessary.

Configure a new repository:

** Important**\
Out of courtesy to the community run efforts at [codeberg](https://wiki.gentoo.org/index.php?title=Codeberg&action=edit&redlink=1 "Codeberg (page does not exist)"), users should being using [Github](https://wiki.gentoo.org/index.php?title=Github.com&action=edit&redlink=1 "Github.com (page does not exist)") to sync, or in cases where users can only use IPv6, using Gentoo\'s anongit. This is mostly due to bandwidth concerns.

`root `[`#`]`eselect repository add gentoo git `[`https://github.com/gentoo-mirror/gentoo`](https://github.com/gentoo-mirror/gentoo)

    Adding gentoo to /etc/portage/repos.conf/eselect-repo.conf ...
    Repository gentoo added

** Tip**\
You can view more git-related(`sync-git*`) options through `man 5 portage`.

** Verification**\
Verify the [repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf") content, including in particular the `location` entry in the `gentoo` section:

`user `[`$`]`portageq repos_config /`

    [DEFAULT]
    auto-sync = yes
    main-repo = gentoo
    strict-misc-digests = true
    sync-allow-hardlinks = true
    sync-openpgp-key-refresh = true
    sync-rcu = false

    [gentoo]
    auto-sync = yes
    location = /var/db/repos/gentoo
    masters =
    priority = -1000
    strict-misc-digests = true
    sync-allow-hardlinks = true
    sync-openpgp-key-path = /usr/share/openpgp-keys/gentoo-release.asc
    sync-openpgp-key-refresh = true
    sync-openpgp-key-refresh-retry-count = 40
    sync-openpgp-key-refresh-retry-delay-exp-base = 2
    sync-openpgp-key-refresh-retry-delay-max = 60
    sync-openpgp-key-refresh-retry-delay-mult = 4
    sync-openpgp-key-refresh-retry-overall-timeout = 1200
    sync-openpgp-keyserver = hkps://keys.gentoo.org
    sync-rcu = false
    sync-type = git
    sync-uri = https://github.com/gentoo-mirror/gentoo.git

\
Sync the repository with the new Git configuration:

`root `[`#`]`emaint sync -r gentoo`

Run again to test.

## [Troubleshooting]

### [emerge \--sync failed]

If you run emerge \--sync or eix-sync after switching to the git repo and it fails, this could be because the old rsync repo is still populated with rsync data. This can be confirmed with this sync error:

`root `[`#`]`emerge --sync`

    Syncing repository 'gentoo' into '/var/db/repos/gentoo'...
    /usr/bin/git clone --depth 1 https://github.com/gentoo-mirror/gentoo .
    fatal: destination path '.' already exists and is not an empty directory.
    !!! git clone error in /var/db/repos/gentoo
    fatal: not a git repository (or any of the parent directories): .git

To solve this issue, back up the directory [/var/db/repos/gentoo] using the following command:

`root `[`#`]`mv /var/db/repos/gentoo /var/db/repos/gentoo.rsync-backup`

After the backup has been finished re-sync the gentoo repository using *one* of the following commands:

-   :::: cmd-box


    `root `[`#`]`emaint sync -r gentoo`


    ::::

-   :::: cmd-box


    `root `[`#`]`emerge --sync`


    ::::

-   :::: cmd-box


    `root `[`#`]`eix-sync`


    ::::

## [Local Mirrors]

As a matter of courtesy, it is considered best practice that if you have multiple Gentoo hosts, you should set up a local portage mirror to reduce the number of external syncs that you have to perform. Syncing all of your internal hosts to an external mirror wastes bandwidth at both ends, and increases load on the public mirrors.

Please refer to [Local_Mirror](https://wiki.gentoo.org/wiki/Local_Mirror "Local Mirror") for instructions for setting up a local Portage mirror.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/orgs/community/discussions/10539](https://github.com/orgs/community/discussions/10539)]]