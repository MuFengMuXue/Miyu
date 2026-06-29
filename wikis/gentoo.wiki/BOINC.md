[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=BOINC&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Science "Project:Science")][Project](https://wiki.gentoo.org/wiki/Project:Science "Project:Science")

[[]][Home](https://boinc.berkeley.edu/)

[[]][Official documentation](https://github.com/BOINC/boinc/wiki)

[[]][Package information](https://packages.gentoo.org/packages/sci-misc/boinc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Berkeley_Open_Infrastructure_for_Network_Computing "wikipedia:Berkeley Open Infrastructure for Network Computing")

[[]][GitHub](https://github.com/BOINC/boinc)

[[]][Bugs (upstream)](https://github.com/BOINC/boinc/issues)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/boinc)

**BOINC** *(Berkeley Open Infrastructure for Network Computing)* is a software system for volunteer computing. It lets people donate time on their home computers and smartphones to science research projects.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Additional software]](#Additional_software)
    -   [[1.5] [Applications]](#Applications)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Permissions]](#Permissions)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Installation]

### [Kernel]

To run some projects, you need vsyscall emulation enabled:

[KERNEL] **Enable vsyscall support**

    Processor type and features --->
        vsyscall table for legacy applications (None) --->
            (X) Emulate

### [USE flags]

### [USE flags for] [sci-misc/boinc](https://packages.gentoo.org/packages/sci-misc/boinc) [[]] [The Berkeley Open Infrastructure for Network Computing]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)               Add support for X11
  [`cuda`](https://packages.gentoo.org/useflags/cuda)         Enable NVIDIA CUDA support (computation on GPU)
  [`gui`](https://packages.gentoo.org/useflags/gui)           Enable support for a graphical user interface
  [`opencl`](https://packages.gentoo.org/useflags/opencl)     Enable OpenCL support (computation on GPU)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 01:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sci-misc/boinc`

### [Additional software]

-   [[[app-admin/boinctui::guru]](https://gpo.zugaina.org/Overlays/guru/app-admin/boinctui)[]] -- a curses-based terminal BOINC client manager.
-   [[[net-p2p/gridcoin::guru]](https://gpo.zugaina.org/Overlays/guru/net-p2p/gridcoin)[]] -- a cryptocurrency rewarding volunteer computing.

### [Applications]

Some applications can be built from source with CPU-native optimizations and used via [anonymous platform](https://boinc.berkeley.edu/wiki/Anonymous_platform). A couple of them are currently packaged in [GURU](https://wiki.gentoo.org/wiki/GURU "GURU"):

-   [[[sci-biology/cmdock::guru]](https://gpo.zugaina.org/Overlays/guru/sci-biology/cmdock)[]] -- application for the [SiDock@home](https://sidock.si/sidock/) project.
-   [[[sci-biology/geneathome::guru]](https://gpo.zugaina.org/Overlays/guru/sci-biology/geneathome)[]] -- application for the [TN-Grid](http://gene.disi.unitn.it/test/)\'s gene@home project.

## [Configuration]

To learn about configuration files and environment variables, refer to the [Client configuration](https://boinc.berkeley.edu/wiki/Client_configuration) article of the BOINC user manual.

### [Permissions]

To be able to use [CUDA](https://wiki.gentoo.org/index.php?title=CUDA&action=edit&redlink=1 "CUDA (page does not exist)") or [OpenCL](https://wiki.gentoo.org/wiki/OpenCL "OpenCL"), you should add the [boinc] user to the [video] group:

`root `[`#`]`gpasswd -a boinc video`

To use the BOINC Manager and the [boinccmd] command-line tool, add youself to the [boinc] group^[\[1\]](#cite_note-1)^:

`root `[`#`]`gpasswd -a <user> boinc`

Changes will not take effect until you sign out and then sign in again (re-login).

### [Service]

#### [OpenRC]

`root `[`#`]`rc-service boinc start `

`root `[`#`]`rc-update add boinc default `

The OpenRC service also supports some common tasks, such as attaching to a new project and suspending work.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sci-misc/boinc`

Finally, remove BOINC\'s state directory:

`root `[`#`]`rm -r /var/lib/boinc`

## [External resources]

-   [List of active BOINC projects](http://wuprop.boinc-af.org/active_projects.py)
-   [Community-run Discord guild](https://discord.gg/UEwWbAv3)

## [References]

1.  [[[↑](#cite_ref-1)] [[Accessing BOINC on Linux](https://boinc.berkeley.edu/gui_rpc.php)]]