**Resources**

[[]][Package information](https://packages.gentoo.org/packages/dev-build/steve)

**steve** is a jobserver implementation for Gentoo. Its author [mgorny](https://wiki.gentoo.org/wiki/User:MGorny "User:MGorny") has written up its design. ^[\[1\]](#cite_note-1)^

[GNU make](https://wiki.gentoo.org/wiki/Make "Make") and other supporting clients support requesting tokens from a [jobserver](https://www.gnu.org/software/make/manual/html_node/POSIX-Jobserver.html) for coordination of parallelism across different make (and friends) instances. It is supported by [make], [ninja], GCC\'s [LTO](https://wiki.gentoo.org/wiki/LTO "LTO") support, and [Rust](https://wiki.gentoo.org/wiki/Rust "Rust")\'s Cargo.

This allows capping the total number of parallel jobs across different [emerge] jobs or calls.

** Warning**\
Testing of steve and jobserver use is welcome but please be advised that a lot of the integration isn\'t yet stable, as its rollout and various related fixes are still in development and very new.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel Configuration]](#Kernel_Configuration)
    -   [[1.2] [Build steve]](#Build_steve)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [steve daemon]](#steve_daemon)
        -   [[2.1.1] [systemd]](#systemd)
    -   [[2.2] [stevie]](#stevie)
    -   [[2.3] [Starting Steve]](#Starting_Steve)
        -   [[2.3.1] [systemd]](#systemd_2)
        -   [[2.3.2] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Packages]](#Packages)
    -   [[3.2] [Portage]](#Portage)
    -   [[3.3] [Permissions]](#Permissions)
    -   [[3.4] [Tips & tricks]](#Tips_.26_tricks)
        -   [[3.4.1] [Customizing use per-package]](#Customizing_use_per-package)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [Kernel Configuration]

`CONFIG_CUSE` is required in the kernel to be able to have the /dev/steve character device.

Rebuild/install/reboot the kernel in the normal way if any configuration changes are required.

[KERNEL] **Enable Character device in Userspace support**

    File systems --->
      FUSE (Filesystem in Userspace) support --->
        <*>  Character device in Userspace support Search for <code>CONFIG_CUSE</code> to find this item.

### [Build steve]

`root `[`#`]`emerge --ask dev-build/steve`

steve itself has an extensive README in [/usr/share/doc/steve\*].

## [Configuration]

Clients are configured via `MAKEFLAGS="--jobserver-auth=fifo:/dev/steve"`.

Note that while the the *\--jobserver-auth* flag is GNU Make-specific, non-GNU Make clients usually only check `MAKEFLAGS` and not `GNUMAKEFLAGS`.

### [steve daemon]

[steve] itself can be configured via the systemd unit ([systemctl edit steve]) or OpenRC init script ([/etc/conf.d/steve]).

It defaults to handing out a maximum of `$(nproc)` tokens which can be adjusted via *\--jobs=N*. It supports other limiting factors like load average (*\--load-average=N*) and free memory (*\--min-memory-avail=N*) too.

#### [systemd]

When editing steve\'s startup options with [systemctl edit], make sure to clear the old value of `ExecStart` first.

For example, to enable debugging output:

[FILE] **`N/A`**

    ### Editing /etc/systemd/system/steve.service.d/override.conf
    ### Anything between here and the comment below will become the contents of the drop-in file

    [Service]
    ExecStart=
    ExecStart=/usr/bin/steve --verbose --debug

    ### Edits below this comment will be discarded

    ### /etc/systemd/system/steve.service
    # [Service]
    # Type=exec
    # ExecStart=/usr/bin/steve
    # User=steve
    # Group=steve
    #
    # [Install]
    # WantedBy=multi-user.target

### [stevie]

The steve daemon can be configured at runtime via the [stevie] client.

[stevie -t] is very useful to see how many tokens are left for the job server to allocate.

`user `[`$`]`stevie --get-tokens`

    31

This could be used this to dynamically reduce the number of jobs before starting a particularly heavy package via [/etc/portage/bashrc] hooks.

### [Starting Steve]

Enable and start steve via the init system:

#### [systemd]

`root `[`#`]`systemctl enable --now steve`

#### [OpenRC]

`root `[`#`]`rc-update add steve default`

`root `[`#`]`/etc/init.d/steve start`

steve itself has an extensive README in [/usr/share/doc/steve\*].

## [Usage]

### [Packages]

For the jobserver to be used by packages, the package manager must be told how to communicate this to build systems: Example [/etc/portage/make.conf] snippet:

[FILE] **`/etc/portage/make.conf`**

    # Replace 32 by the value of $(nproc)
    MAKEOPTS="-j32 -l32"
    NINJAOPTS="-l32"
    MAKEFLAGS="-l32 --jobserver-auth=fifo:/dev/steve"

It is important that *-jN* is **not** passed to make or other clients, as they interpret this as a directive to not use the jobserver. Portage will defer to `MAKEFLAGS` if both `MAKEOPTS` and `MAKEFLAGS` are set.

On the other hand, `MAKEOPTS` should still be set because some packages using less popular build systems (not involving [make] or [ninja]) will extract *-jN* from it to use an appropriate level of parallelism.

Unfortunately, `GNUMAKEFLAGS` cannot be used to resolve this problem because clients like [ninja] only inspect `MAKEFLAGS`.

### [Portage]

Portage (\>=3.0.74) supports claiming a jobserver token per job in [emerge \--jobs]. This is important because of the \'implicit slot\' problem. See [[[bug #966879]](https://bugs.gentoo.org/show_bug.cgi?id=966879)[]].

This is controlled by `FEATURES="jobserver-token"`:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="$ jobserver-token"

### [Permissions]

Access to [steve]\'s jobserver at [/dev/steve] is controlled by the *jobserver* group from [[[acct-group/jobserver]](https://packages.gentoo.org/packages/acct-group/jobserver)[]]. The *portage* group is a member of *jobserver* by default.

Users who wish to access the jobserver for builds run manually as their user will need to add their user to the group.

\

### [][Tips & tricks]

#### [Customizing use per-package]

Users often wish for \'large\' packages to be treated specially in some way: emerged first, last, or serially (e.g. [[[bug #460712]](https://bugs.gentoo.org/show_bug.cgi?id=460712)[]]). Achieving that is challenging because there is no single definition of a *large* package, nor do all users want the same behavior for them.

One solution to this can be found by combining *stevie* (a client for querying and configuring steve at runtime) and [/etc/portage/env]. This is especially useful as Portage will request a job from the jobserver (see above) if configured to do so for its own phase execution, not just build systems themselves.

For example, to limit parallel jobs when [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]] is being built:

[FILE] **`/etc/portage/env/www-client/chromium`**

    pre_src_compile()

    post_src_compile()
    }

A similar thing could be done with stevie\'s *\--set-min-memory-avail* to adjust the amount of memory assumed per job. One may wish to try add a *death hook* to restore the old value if the build fails too.

Another option could be to limit parallelism whenever *check-reqs.eclass* is inherited in an ebuild:

[FILE] **`/etc/portage/bashrc`**

    pre_src_compile()  ; then
            # Before starting to compile a large package, backup the old
            # number of allowed total jobs.
            _STEVE_BACKUP_JOBS=$(stevie --get-jobs)
            # Lower the number to 5.
            stevie --set-jobs 5
        fi
    }

    post_src_compile()  ; then
            # Reset to the old value once the large package has been compiled.
            stevie --set-jobs $
        fi
    }

## [See also]

-   [Guildmaster](https://wiki.gentoo.org/wiki/Guildmaster "Guildmaster") --- a simple jobserver implementation
-   [Make](https://wiki.gentoo.org/wiki/Make "Make") --- a [tool to *build*](https://wiki.gentoo.org/wiki/Build_automation#Available_software "Build automation") software from source code (which usually includes compiling)

## [References]

1.  [[[↑](#cite_ref-1)] [[One jobserver to rule them all](https://blogs.gentoo.org/mgorny/2025/11/30/one-jobserver-to-rule-them-all/)]]