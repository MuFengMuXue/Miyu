[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Find&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/findutils/)

[[]][Official documentation](https://www.gnu.org/software/findutils/manual/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/findutils)

[[]][Wikipedia](https://en.wikipedia.org/wiki/find_(Unix "wikipedia:find (Unix")

}

GNU [find], provided by the [[[sys-apps/findutils]](https://packages.gentoo.org/packages/sys-apps/findutils)[]] package, is a utility to search for files in a directory hierarchy. It is an implementation of [the [find] utility specified by the](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/find.html) [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX") standard. POSIX behavior can be requested via the `POSIXLY_CORRECT` environment variable; refer to the [[[find(1)]](https://man.archlinux.org/man/find.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for further information.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/findutils](https://packages.gentoo.org/packages/sys-apps/findutils) [[]] [GNU utilities for finding files]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)           !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`test-full`](https://packages.gentoo.org/useflags/test-full)     Run expensive tests (mostly memory intensive).
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 18:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

The [[[sys-apps/findutils]](https://packages.gentoo.org/packages/sys-apps/findutils)[]] package is part of [the \@system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), so is installed by default.

`root `[`#`]`emerge --ask sys-apps/findutils`

## [Usage]

Find all files (`-type f`) in the current directory and its subdirectories (`.`) whose name ends in `.txt`:

`user `[`$`]`find . -type f -name '*.txt'`

Find all directories (`-type d`) in [/tmp] and its subdirectories whose name begins with `test`:

`user `[`$`]`find /tmp -type d -name 'test*'`

Find all files in [/home/user/test/] whose name ends in `.txt` and change their permissions to 700:

`user `[`$`]`find /home/user/test -type f -name '*.txt' -exec chmod 700  +`

The `` sequence will be replaced by the name of each file found. The `+` character designates the end of the command to be executed; an alternative is the `;` character, although that typically needs to be escaped in order to prevent it from being interpreted by the shell:

`user `[`$`]`find /home/user/test -type f -name '*.txt' -exec chmod 700  \;`

## [See also]

-   The GNU [[[find(1)]](https://man.archlinux.org/man/find.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page

## [External resources]

-   [[find] in the Gentoo Devmanual](https://devmanual.gentoo.org/tools-reference/find/)