[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Elixir&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://elixir-lang.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/elixir)

[[]][Official documentation](https://elixir-lang.org/docs.html)

[[]][GitHub](https://github.com/elixir-lang/elixir)

[[]][[#elixir](ircs://irc.libera.chat/#elixir)] ([[webchat](https://web.libera.chat/#elixir)])

**Elixir** is a dynamic programming language, with a functional paradigm to easily write scalable and maintainable projects. Elixir runs on [Erlang\'s](https://wiki.gentoo.org/wiki/Erlang "Erlang") BEAM virtual machine.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/elixir](https://packages.gentoo.org/packages/dev-lang/elixir) [[]] [Elixir programming language]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-18 16:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-lang/elixir`

## [Usage]

### [Invocation]

`user `[`$`]`iex --help`

    Usage: iex [options] [.exs file] [data]

    The following options are exclusive to IEx:

      --dot-iex "PATH"    Overrides default .iex.exs file and uses path instead;
                          path can be empty, then no file will be loaded
      --remsh NAME        Connects to a node using a remote shell

    It accepts all other options listed by "elixir --help".