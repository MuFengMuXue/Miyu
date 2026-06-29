[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=SuperCollider&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://supercollider.github.io/)

[[]][Official documentation](https://doc.sccode.org/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/supercollider)

[[]][GitHub](https://github.com/supercollider/supercollider)

[SuperCollider] is a platform for audio synthesis and algorithmic composition.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Emacs]](#Emacs)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/supercollider](https://packages.gentoo.org/packages/media-sound/supercollider) [[]] [Environment and programming language for real time audio synthesis]

  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+fftw`](https://packages.gentoo.org/useflags/+fftw)                 Use FFTW library for computing Fourier transforms
  [`+gpl3`](https://packages.gentoo.org/useflags/+gpl3)                 Build GPL-3 licensed code (recommended)
  [`+sndfile`](https://packages.gentoo.org/useflags/+sndfile)           Add support for libsndfile
  [`+zeroconf`](https://packages.gentoo.org/useflags/+zeroconf)         Support for DNS Service Discovery (DNS-SD)
  [`X`](https://packages.gentoo.org/useflags/X)                         Add support for X11
  [`ableton-link`](https://packages.gentoo.org/useflags/ableton-link)   Enable support for Ableton Link
  [`debug`](https://packages.gentoo.org/useflags/debug)                 Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`emacs`](https://packages.gentoo.org/useflags/emacs)                 Enable the SCEL user interface
  [`jack`](https://packages.gentoo.org/useflags/jack)                   Add support for the JACK Audio Connection Kit
  [`qt6`](https://packages.gentoo.org/useflags/qt6)                     Add support for the Qt 6 application and UI framework
  [`server`](https://packages.gentoo.org/useflags/server)               Build with internal server
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)     Build static versions of dynamic libraries as well
  [`vim`](https://packages.gentoo.org/useflags/vim)                     Enable the SCVIM user interface
  [`webengine`](https://packages.gentoo.org/useflags/webengine)         Enable the internal help system using dev-qt/qtwebengine
  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-15 19:18] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/supercollider`

## [Usage]

The [[[media-sound/supercollider]](https://packages.gentoo.org/packages/media-sound/supercollider)[]] package provides three binaries:

-   **sclang**, the interpreter for the SuperCollider language. An interactive session can be started from the command line via [sclang]; a server can be started via [sclang -D].
-   **scide**, the IDE. An introduction to its use can be found in the \" [Getting started with SC](https://doc.sccode.org/Tutorials/Getting-Started/00-Getting-Started-With-SC.html)\" tutorial.
-   **scsynth**, a SuperCollider synthesizer.

There are no man pages for these binaries, but command-line options for **sclang** and **scsynth** can be listed by passing the `-help` option to either.

### [Emacs]

** Warning**\
Although SuperCollider provides an Emacs Lisp interface to the SuperCollider system, via the inclusion of [scel](https://github.com/supercollider/scel/), **scel** has not been updated since September 2021. Additionally, the [sclang-extensions](https://github.com/chrisbarrett/sclang-extensions) Emacs package, available via MELPA, has not been updated since May 2016, and is listed as unmaintained. Both might or might work adequately, depending on system configuration and use-case. In particular, note that starting an **sclang** server via `sclang-start` might result in issues, due to the command-line options `-iscel` being hard-coded in [sclang-interp.el].

To make **scel** available in Emacs:

[CODE]

    (add-to-list 'load-path "/usr/share/emacs/site-lisp/SuperCollider/")
    (require 'sclang)