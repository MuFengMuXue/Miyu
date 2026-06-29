[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Rex&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.rexify.org/)

[[]][Official documentation](https://www.rexify.org/docs/rex_book/index.html)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/rex)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Rex_(software) "wikipedia:Rex (software)")

[[]][GitHub](https://github.com/RexOps/Rex)

[[]][Bugs (upstream)](https://github.com/RexOps/Rex/issues)

[[]][[#rexops](irc://irc.oftc.net/#rexops) (on [irc://irc.oftc.net](irc://irc.oftc.net)])

**[rex]** sometimes stylized as **`(R)?ex`** is a configuration automation framework written in [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") known for its shallow learning curve and ease of extensibility. Widely regarded as a user-friendly automation framework, unlike better known alternatives such as [Ansible](https://wiki.gentoo.org/wiki/Ansible "Ansible"), [rex] does not use YAML to describe tasks by default. Rather, it uses small easily understood snippets of Perl to describe tasks. Indeed, the entire system can readily be extended with custom Perl modules if needed.

Like many other configuration management tools [rex] is agentless, only requiring valid SSH keys and a working Perl interpreter on the managed system to function. Further, development currently targets Perl 5.10.1 (2009) which makes it possible to easily support legacy systems that would be difficult or impossible for other tools to manage.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Unmerge]](#Unmerge)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/rex](https://packages.gentoo.org/packages/app-admin/rex) [[]] [(R)?ex, the friendly automation framework]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`minimal`](https://packages.gentoo.org/useflags/minimal)   Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-07-20 11:13] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-admin/rex`

## [Usage]

### [Invocation]

`user `[`$`]`rex -h`

    usage:
      rex [<options>] [-H <host>] [-G <group>] <task> [<task-options>]
      rex -T[m|y|v] [<string>]

      -b     Run batch
      -e     Run the given code fragment
      -E     Execute a task on the given environment
      -G|-g  Execute a task on the given server groups
      -H     Execute a task on the given hosts (space delimited)
      -z     Execute a task on hosts from this command's output

      -K     Public key file for the ssh connection
      -P     Private key file for the ssh connection
      -p     Password for the ssh connection
      -u     Username for the ssh connection

      -d     Show debug output
      -ddd   Show more debug output (includes profiling output)
      -m     Monochrome output: no colors
      -o     Output format
      -q     Quiet mode: no log output
      -qw    Quiet mode: only output warnings and errors
      -Q     Really quiet: output nothing

      -T     List tasks
      -Ta    List all tasks, including hidden
      -Tm    List tasks in machine-readable format
      -Tv    List tasks verbosely
      -Ty    List tasks in YAML format

      -c     Turn cache ON
      -C     Turn cache OFF
      -f     Use this file instead of Rexfile
      -F     Force: disregard lock file
      -h     Display this help message
      -M     Load this module instead of Rexfile
      -O     Pass additional options, like CMDB path
      -s     Use sudo for every command
      -S     Password for sudo
      -t     Number of threads to use (aka 'parallelism' param)
      -v     Display (R)?ex version

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-admin/rex`

## [See also]

-   [Ansible](https://wiki.gentoo.org/wiki/Ansible "Ansible") --- an agentless automation system written in [Python](https://wiki.gentoo.org/wiki/Python "Python").
-   [Sparrow](https://wiki.gentoo.org/index.php?title=Sparrow&action=edit&redlink=1 "Sparrow (page does not exist)")
-   [dsh](https://wiki.gentoo.org/wiki/Dsh "Dsh") --- a shell that allows parallel execution of remote commands across large numbers of servers