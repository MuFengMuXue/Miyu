[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Application_level_package_management&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/List_of_software_package_management_systems#Application-level_package_managers "wikipedia:List of software package management systems")

This meta article provides best practice recommendations on managing the coexistence of operating system and **application level package managers** on Gentoo.

## Contents

-   [[1] [Considerations]](#Considerations)
    -   [[1.1] [When to use an application level package manager]](#When_to_use_an_application_level_package_manager)
    -   [[1.2] [Best practices]](#Best_practices)
        -   [[1.2.1] [THOU SHALT NOT]](#THOU_SHALT_NOT)
        -   [[1.2.2] [THOU SHALL]](#THOU_SHALL)
-   [[2] [Available software and articles]](#Available_software_and_articles)
    -   [[2.1] [Programming language package managers]](#Programming_language_package_managers)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [User profiles]](#User_profiles)
        -   [[3.1.1] [Shell]](#Shell)
-   [[4] [See also]](#See_also)

## [Considerations]

Gentoo offers a variety of application level (or language based) package managers. Some application level package managers have been patched to prevent accidental misuse by the end users.

### [When to use an application level package manager]

It is typical for an operating system\'s package manager and an application level package manager to provide the same package. Should the OS level or the application level package manager be used? The answer depends on purpose of the package. Generally speaking, the package provided via the OS level package manager should be used by default for the following reasons:

1.  Portage will keep the package up-to-date during standard system updates.
2.  Gentoo\'s [glsa-check] tool can be used to test for security vulnerabilities.

However, if the package is unavailable via the main ebuild repository and/or overlays, then alternatives such as application level package managers should be considered.

** Note**\
A limitation to the above recommendation would be for software development on Gentoo. Software developers must frequently employ application level package manager to install the necessary packages to build their application(s). Even in this case, the [best practices](#Best_practices) should be observed.

### [Best practices]

#### [THOU SHALT NOT]

End users should **NOT** install packages from application level package managers:

1.  With root user privileges. This *includes* using privilege escalation such as [sudo], [doas], or [su]!
2.  Into system directories such as [/bin], [/lib], [/lib64], [/sbin], or [/usr]. Installing to these directories should not be possible if the first rule is observed.

Performing either of the above actions could irrevocably ruin the integrity of the OS packages.

#### [THOU SHALL]

End users **should** install packages from application level package managers:

1.  With standard user permissions.
2.  Into a home directory or software development workspace such as any non-LFH mount point, [/srv], [/mnt], or [/opt].

## [Available software and articles]

The following are some of the application level package managers available in Gentoo:

### [Programming language package managers]

  --------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------
  Name                                                Package                                                                                                                                                                                                                                                                                                                                                                     Homepage                                                                                                           Description
  Conan                                               [[[dev-util/conan]](https://packages.gentoo.org/packages/dev-util/conan)[]]            [https://conan.io/](https://conan.io/)                                             Best C++ package manager after Portage.
  Bundler                                             [[[dev-ruby/bundler]](https://packages.gentoo.org/packages/dev-ruby/bundler)[]]      [https://bundler.io/](https://bundler.io/)                                         Provides a method to \'vendor\' gems for Ruby projects (depends on [Ruby gems](https://wiki.gentoo.org/wiki/Gem "Gem")).
  Shards                                              [[[dev-lang/crystal]](https://packages.gentoo.org/packages/dev-lang/crystal)[]]      [https://github.com/crystal-lang/shards](https://github.com/crystal-lang/shards)   A dependency manager for the Crystal language
  [Gem](https://wiki.gentoo.org/wiki/Gem "Gem")       [[[dev-ruby/rubygems]](https://packages.gentoo.org/packages/dev-ruby/rubygems)[]]   [https://rubygems.org/](https://rubygems.org/)                                     A centralized Ruby extension management system
  [Go](https://wiki.gentoo.org/wiki/Go "Go")          [[[dev-lang/go]](https://packages.gentoo.org/packages/dev-lang/go)[]]                     [https://go.dev](https://go.dev)                                                   A concurrent garbage collected and typesafe programming language from Google
  [Cargo](https://wiki.gentoo.org/wiki/Rust "Rust")   [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]]               [https://github.com/rust-lang/cargo](https://github.com/rust-lang/cargo)           Rust\'s build system and package manager
  Nimble                                              [[[dev-lang/nim]](https://packages.gentoo.org/packages/dev-lang/nim)[]]                  [https://github.com/nim-lang/nimble](https://github.com/nim-lang/nimble)           A package manager for the Nim programming language
  [Pip](https://wiki.gentoo.org/wiki/Pip "Pip")       [[[dev-python/pip]](https://packages.gentoo.org/packages/dev-python/pip)[]]            [https://pip.pypa.io/en/stable/](https://pip.pypa.io/en/stable/)                   The PyPA recommended tool for installing Python packages
  Pipx                                                [[[dev-python/pipx]](https://packages.gentoo.org/packages/dev-python/pipx)[]]         [https://pipx.pypa.io](https://pipx.pypa.io)                                       Install and run Python applications in isolated environments (testing branch only as of 2025-09)
  uv                                                  [[[dev-python/uv]](https://packages.gentoo.org/packages/dev-python/uv)[]]               [https://github.com/astral-sh/uv/](https://github.com/astral-sh/uv/)               A faster alternative for [Pip](https://wiki.gentoo.org/wiki/Pip "Pip").
  --------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------

## [Configuration]

### [User profiles]

#### [Shell]

A user\'s shell can set environment variables in order to instruct application level package managers to safely place new packages into a user\'s home directory. A system admin can use shell defaults at a global level (for all new users) via the [/etc/skel] directory.

For example, a bash shell user is developing a project and would like to add a Go package via [go install]. The user would modify their [\~/.bash_profile] file with the following values to define a path that Go will use to install packages, then modify their shell\'s `PATH` variable to source the newly added binaries.

[FILE] **`~/bash_profile`Defining GOPATH, GOBIN, and append Go binaries to user\'s PATH**

    # Set GOPATH path for bash shell users
    export GOPATH="$/go"
    # Set GOBIN path for bash shell users
    export GOBIN="$/bin"
    # Append Go binary to user's PATH for binaries added via `go install`
    export PATH="$:$"

For currently running instances of [bash] to recognize the environment changes, source the [.bash_profile] file:

`user `[`$`]`source $/.bash_profile`

## [See also]

-   [Bundler](https://wiki.gentoo.org/index.php?title=Bundler&action=edit&redlink=1 "Bundler (page does not exist)")
-   [Go](https://wiki.gentoo.org/wiki/Go "Go") --- an open source, statically typed, compiled programming language
-   [Pip](https://wiki.gentoo.org/wiki/Pip "Pip") --- [Python](https://wiki.gentoo.org/wiki/Python "Python")\'s package management system. It references packages available in the official **Py**thon **P**ackage **I**ndex (PyPI).
-   [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") --- a general-purpose, multi-paradigm, compiled, programming language.
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.
-   [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak") --- a package management framework aiming to provide support for sandboxed, distro-agnostic binary packages for Linux desktop applications.
-   [An old and yet still correct article on package management](https://michael.orlitzky.com/articles/motherfuckers_need_package_management.xhtml)