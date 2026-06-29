[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Erlang&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.erlang.org/)

[[]][Official documentation](https://www.erlang.org/docs)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/erlang)

[[]][GitHub](https://github.com/erlang/otp)

[[]][[#erlang](ircs://irc.libera.chat/#erlang)] ([[webchat](https://web.libera.chat/#erlang)])(unofficial)

**Erlang** is a concurrent, functional language, adapted to writing distributed, fault tolerant systems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/erlang](https://packages.gentoo.org/packages/dev-lang/erlang) [[]] [Erlang programming language, runtime environment and libraries (OTP)]

  --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+kpoll`](https://packages.gentoo.org/useflags/+kpoll)         Enable kernel polling support
  [`doc`](https://packages.gentoo.org/useflags/doc)               Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`emacs`](https://packages.gentoo.org/useflags/emacs)           Add support for GNU Emacs
  [`java`](https://packages.gentoo.org/useflags/java)             Add support for Java
  [`odbc`](https://packages.gentoo.org/useflags/odbc)             Add ODBC Support (Open DataBase Connectivity)
  [`sctp`](https://packages.gentoo.org/useflags/sctp)             Support for Stream Control Transmission Protocol
  [`ssl`](https://packages.gentoo.org/useflags/ssl)               Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)       Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`tk`](https://packages.gentoo.org/useflags/tk)                 Add support for Tk GUI toolkit
  [`wxwidgets`](https://packages.gentoo.org/useflags/wxwidgets)   Add support for wxWidgets/wxGTK GUI toolkit
  --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 18:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install:

`root `[`#`]`emerge --ask dev-lang/erlang`

## [Usage]

### [Invocation]

`user `[`$`]`erl`

    Erlang/OTP 24 [erts-12.0.2] [source] [64-bit] [smp:12:12] [ds:12:12:10] [async-threads:1] [jit]

    Eshell V12.0.2  (abort with ^G)
    1>

To exit the shell: [Ctrl]+[g] then [q] and [Return].