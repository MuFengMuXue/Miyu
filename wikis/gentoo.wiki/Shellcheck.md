[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Shellcheck&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.shellcheck.net/)

[[]][Package information](https://packages.gentoo.org/packages/dev-util/shellcheck)

[[]][GitHub](https://github.com/koalaman/shellcheck)

[[]][Bugs (upstream)](https://github.com/koalaman/shellcheck/issues)

[[]][Official project wiki](https://www.shellcheck.net/wiki/Home)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/shellcheck)

**ShellCheck** is a [shell](https://wiki.gentoo.org/wiki/Shell "Shell") script static analysis tool written in [Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell"). It gives various warnings about shell scripts --- mainly syntax and semantic problems related to the typical beginner issues, counter-intuitive behavior, or various corner cases.

As of version 0.9.0, ShellCheck supports [sh], [[bash]](https://wiki.gentoo.org/wiki/Bash "Bash"), [[dash]](https://wiki.gentoo.org/wiki/Dash "Dash"), and [ksh] shells.^[\[1\]](#cite_note-1)^

It can be integrated in a build suite or [CI/CD](https://en.wikipedia.org/wiki/CI/CD "wikipedia:CI/CD") pipelines such as [Jenkins](https://wiki.gentoo.org/wiki/Jenkins "Jenkins") or [GitLab](https://wiki.gentoo.org/wiki/GitLab "GitLab").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [Binary package (shellcheck-bin)]](#Binary_package_.28shellcheck-bin.29)
        -   [[1.2.2] [Source package]](#Source_package)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/shellcheck](https://packages.gentoo.org/packages/dev-util/shellcheck) [[]] [Shell script analysis tool]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`hscolour`](https://packages.gentoo.org/useflags/hscolour)   Include coloured haskell sources to generated documentation (dev-haskell/hscolour)
  [`profile`](https://packages.gentoo.org/useflags/profile)     Add support for software performance analysis (will likely vary from ebuild to ebuild)
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2023-11-19 18:32] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

** Tip**\
The binary version is intended for systems with no Haskell toolchain present.

#### [][Binary package (shellcheck-bin)]

`root `[`#`]`emerge --ask dev-util/shellcheck-bin`

#### [Source package]

`root `[`#`]`emerge --ask dev-util/shellcheck`

## [Configuration]

### [Files]

ShellCheck\'s behavior can be modified using directives (like `disable` or `enable`) directly in the validated script or using configuration files:

-   [\~/.shellcheckrc] - Local (per user) configuration file.
-   [/home/larry/project/.shellcheckrc] - Per project configuration file.

## [Usage]

### [Invocation]

Script validation with an example error output:

`user `[`$`]`shellcheck validated-script.sh`

    In validated-script.sh line 5:
    echo $DATE
         ^---^ SC2086 (info): Double quote to prevent globbing and word splitting.

    Did you mean:
    echo "$DATE"

    For more information:
      https://www.shellcheck.net/wiki/SC2086 -- Double quote to prevent globbing ...

## [See also]

-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users

## [References]

1.  [[[↑](#cite_ref-1)] [[ShellCheck: SC1008](https://www.shellcheck.net/wiki/SC1008), GitHub. Retrieved on January 30, 2023]]