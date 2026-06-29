**Resources**

[[]][Home](https://cr.yp.to/daemontools.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-process/daemontools)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Daemontools "wikipedia:Daemontools")

Daniel J. Bernstein\'s daemontools package, described by him as \"*a collection of tools for managing UNIX services*\", is the pioneer of what some people call today *process supervision suites*, i.e. packages that provide tools for performing process supervision^[\[1\]](#cite_note-1)^ ^[\[2\]](#cite_note-2)^ ^[\[3\]](#cite_note-3)^. There are no further releases of daemontools after 0.76 (released in 2001), but other software packages have been inspired by its design principles, notably [runit](https://wiki.gentoo.org/wiki/Runit "Runit"), [s6](https://wiki.gentoo.org/wiki/S6 "S6"), [perp](http://b0llix.net/perp/site.cgi?page=about), [nosh](https://jdebp.uk/Softwares/nosh/), and an enhanced succesor, [daemontools-encore](https://wiki.gentoo.org/wiki/Daemontools-encore "Daemontools-encore") ^[\[4\]](#cite_note-4)^.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-process/daemontools](https://packages.gentoo.org/packages/sys-process/daemontools) [[]] [Collection of tools for managing UNIX services]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)     !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-19 02:53] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-process/daemontools`

## [Configuration]

### [Files]

-   [/service] - Location of the scan directory when using [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), [svscanboot], or [svscan-add-to-inittab] from [[[sys-process/supervise-scripts]](https://packages.gentoo.org/packages/sys-process/supervise-scripts)[]].

### [Service]

#### [OpenRC]

See [here](https://wiki.gentoo.org/wiki/Daemontools-encore#openrclaunch "Daemontools-encore") for details.

## [Usage]

See [daemontools-encore](https://wiki.gentoo.org/wiki/Daemontools-encore#Usage "Daemontools-encore").

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-process/daemontools`

The same extra steps after [removing daemontools-encore](https://wiki.gentoo.org/wiki/Daemontools-encore#Removal "Daemontools-encore") apply here.

## [See also]

-   [Runit](https://wiki.gentoo.org/wiki/Runit "Runit") --- lightweight process supervision suite, originally inspired by [daemontools] that offers fast and reliable service management.
-   [S6](https://wiki.gentoo.org/wiki/S6 "S6") --- a package that provides a [daemontools-inspired] process supervision suite, a notification framework, a UNIX domain super-server, and tools for file descriptor holding and suidless privilege gain.
-   [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") --- a dependency-based [init system](https://en.wikipedia.org/wiki/Init "wikipedia:Init") for Unix-like systems that maintains compatibility with the system-provided [init system](https://wiki.gentoo.org/wiki/Init_system "Init system")
-   [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") --- a modern SysV-style init and [[rc](https://wiki.gentoo.org/wiki/Rc "Rc")] replacement for Linux systems.

## [External resources]

-   [https://cr.yp.to/daemontools/install.html](https://cr.yp.to/daemontools/install.html) - A very short guide on how to install daemontools.

## [References]

1.  [[[↑](#cite_ref-1)] [D. J. Bernstein, [daemontools FAQ](https://cr.yp.to/daemontools/faq/create.html#why), which includes one about the benefits of process supervision. Retrieved on April 23rd, 2017.]]
2.  [[[↑](#cite_ref-2)] [Gerrit Pape, [runit benefits](http://smarden.org/runit/benefits.html), which includes a short description of process supervision in general. Retrieved on April 23rd, 2017.]]
3.  [[[↑](#cite_ref-3)] [Laurent Bercot, [s6 overview](https://www.skarnet.org/software/s6/overview.html), which contains an introduction to process supervision. Retrieved on April 23rd, 2017.]]
4.  [[[↑](#cite_ref-4)] [Jonathan de Boyne Pollard, [The daemontools family](https://jdebp.uk/FGA/daemontools-family.html). Retrieved on May 16th, 2017.]]