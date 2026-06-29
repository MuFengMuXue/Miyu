[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Duplicity&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://duplicity.gitlab.io/)

[[]][GitLab](https://gitlab.com/duplicity/duplicity)

[[]][Package information](https://packages.gentoo.org/packages/app-backup/duplicity)

[[]][Official documentation](https://duplicity.us/docs.html)

Duplicity is backup software written in Python with native [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") integration and support for many different storage backends. It is designed around the ubiquitous [Tar](https://wiki.gentoo.org/wiki/Tar "Tar"), [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG"), and the same algorithm as [Rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") via [[[net-libs/librsync]](https://packages.gentoo.org/packages/net-libs/librsync)[]].

It supports both whole backups as well as incremental diffs, using librsync to generate small deltas. It doesn\'t have a complex file format for its metadata, instead using [tar] and [rdiff].

Wrappers like [[[app-backup/duply]](https://packages.gentoo.org/packages/app-backup/duply)[]] or [[[app-backup/deja-dup]](https://packages.gentoo.org/packages/app-backup/deja-dup)[]] are also available.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Backing up / to Backblaze with parity]](#Backing_up_.2F_to_Backblaze_with_parity)
    -   [[3.2] [Backing up /home to Backblaze]](#Backing_up_.2Fhome_to_Backblaze)

## [Installation]

### [USE flags]

### [USE flags for] [app-backup/duplicity](https://packages.gentoo.org/packages/app-backup/duplicity) [[]] [Secure backup system using GnuPG to encrypt data]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`s3`](https://packages.gentoo.org/useflags/s3)         Support for backing up to the Amazon S3 system
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-20 22:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-backup/duplicity`

## [Configuration]

[duplicity] has limited configuration file support, but it\'s not necessary either, as the CLI is simple and can be handled with just a small script. There *is* a *\--config-dir* argument but the format it accepts isn\'t well-documented and use of this feature isn\'t common at all.

It recognizes the following environment variables:

-   *BACKEND_PASSWORD* (previously *FTP_PASSWORD*)
-   *PASSPHRASE* (used for encrypting backups with gpg)
-   *SIGN_PASSPHRASE* (ditto, but for unlocking the gpg signing key)
-   Others depending on the storage backend

## [Usage]

The [man page](https://duplicity.us/stable/CHANGELOG.html) is extensive and recommended reading. Below, some basic examples are covered.

### [][Backing up / to Backblaze with parity]

duplicity can optionally chain *par2* to add parity for a proportion of the backed up data to add some resilience in the event of corruption on the storage side. Install [[[app-arch/par2cmdline]](https://packages.gentoo.org/packages/app-arch/par2cmdline)[]] and prefix the destination with \'par2+\' for this.

[FILE] **`~/bin/backup-home`**

    #!/bin/bash

    # Duplicity uses these: specifying passwords via environment variables
    # is better than exposing them by passing as command-line arguments.
    export PASSPHRASE="..."
    export BACKEND_PASSWORD="..."

    # Configuration for the script itself
    DUPLICITY_KEYID=""
    DUPLICITY_BUCKET=""

    DUPLICITY_ARGS=(
            # Optional verbosity (controllable)
            -v info

            --concurrency $(nproc)

            # Run an incremental backup on each invocation unless
            # it has been a month since the last full backup: in which case,
            # start a new incremental chain with a full backup.
            --full-if-older-than 1M

            #
            # https://duplicity.nongnu.org/vers7/duplicity.1.html#toc9
            #
            --exclude ~/.cache
            --exclude ~/.ccache
            --exclude ~/.debug

            --exclude /var/cache/binpkgs
            --exclude /var/cache/distfiles
            --exclude /var/tmp

            --exclude /tmp
            --exclude /sys
            --exclude /proc
            --exclude /dev
            --exclude /run

            # Backup / to b2 with par2 parity support added (https://duplicity.nongnu.org/vers7/duplicity.1.html#toc21)
            backup / par2+b2://$@$
    )

    duplicity "$"

### [][Backing up /home to Backblaze]

[FILE] **`~/bin/backup-home`**

    #!/bin/bash

    # Duplicity uses these: specifying passwords via environment variables
    # is better than exposing them by passing as command-line arguments.
    export PASSPHRASE="..."
    export BACKEND_PASSWORD="..."

    # Configuration for the script itself
    DUPLICITY_KEYID=""
    DUPLICITY_BUCKET=""

    DUPLICITY_ARGS=(
            # Optional verbosity (controllable)
            -v info

            --concurrency $(nproc)

            # Run an incremental backup on each invocation unless
            # it has been a month since the last full backup: in which case,
            # start a new incremental chain with a full backup.
            --full-if-older-than 1M

            --exclude ~/.cache

            # Backup homedir (~) to b2
            backup ~ b2://$@$
    )

    duplicity "$"