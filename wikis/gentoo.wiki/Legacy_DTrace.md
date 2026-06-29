[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Legacy_DTrace&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/DTrace "wikipedia:DTrace")

## Contents

-   [[1] [DTrace on Gentoo]](#DTrace_on_Gentoo)
    -   [[1.1] [Overlay repository]](#Overlay_repository)
    -   [[1.2] [Installation]](#Installation)
    -   [[1.3] [Kernel]](#Kernel)
    -   [[1.4] [Test it]](#Test_it)
-   [[2] [References]](#References)

## [DTrace on Gentoo]

### [Overlay repository]

The ebuilds for DTrace are placed (in time of writing) in GitHub repository.

[https://github.com/robertek/dtrace-portage-overlay](https://github.com/robertek/dtrace-portage-overlay)

To activate the repository just add new repository configuration to your Portage config.

[FILE] **`/etc/portage/repos.conf/dtrace`**

    [dtrace]
    location = /var/lib/portage/dtrace
    sync-type = git
    sync-uri = https://github.com/robertek/dtrace-portage-overlay
    auto-sync = yes

Then sync Portage tree.

### [Installation]

DTrace support on Gentoo consists of kernel sources with patches and userspace utilities. It is packed in 3 packages:

-   libctf =\> library for CTF debug info handling, needed for both the kernel and user utilities
-   dtrace-user =\> userspace part, mainly the [dtrace](1) command and libdtrace
-   dtrace-sources =\> kernel 4.14.x sources containing dtrace patches and working initial .config

The default installation can be done installing just the dtrace-user:

`root `[`#`]`emerge --ask dtrace-user`

** Note**\
The dtrace-sources is needed for dtrace-user because of header dependencies. If you plan to manage your local sources in Git or different way you need link [/usr/include/linux/dtrace] -\> [/your/src/path/dtrace-linux-src/include/uapi/linux/dtrace]

### [Kernel]

Build the kernel your way. The main difference to normal building is executing [make ctf] before kernel installation. This will generate CTF debug data for DTrace to work.

Example steps:

`root `[`#`]`cd /usr/src/linux-4.14.28-dtrace `

`root `[`#`]`make oldconfig `

`root `[`#`]`make `

`root `[`#`]`make ctf `

`root `[`#`]`make install `

`root `[`#`]`make modules_install `

** Important**\
Do not expect to be able to create kernel with custom config, it may end with [dwarf2ctf] tool crashing (when I developed these ebuilds I tried my own config for 4.14 without luck). Suggested is using the config provided from dtrace-sources (which is based on Oracle UEK kernel config) and than striping it down or up your way.

### [Test it]

When everything passed correctly you may try some basic DTrace one-liner.

`root `[`#`]` dtrace -n 'proc:::exec-success '`

    dtrace: description 'proc:::exec-success ' matched 1 probe
    CPU     ID                    FUNCTION:NAME
      3   2017  do_execveat_common:exec-success   /usr/bin/konsole
      3   2017  do_execveat_common:exec-success   git --version
      3   2017  do_execveat_common:exec-success   grep --color=auto
      3   2017  do_execveat_common:exec-success   grep --exclude-dir=.cvs
      3   2017  do_execveat_common:exec-success   dircolors -b
      3   2017  do_execveat_common:exec-success   ls --color -d .

[Ctrl]+[c]

## [References]

To start learning DTrace check some informative guides:

-   [https://wiki.freebsd.org/DTrace](https://wiki.freebsd.org/DTrace)
-   [http://dtrace.org/blogs/about/](http://dtrace.org/blogs/about/)