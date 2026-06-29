[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Go&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://go.dev/)

[[]][Official documentation](https://go.dev/doc/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/go)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Go_(programming_language) "wikipedia:Go (programming language)")

[[]][[#go-nuts](ircs://irc.libera.chat/#go-nuts)] ([[webchat](https://web.libera.chat/#go-nuts)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/go)

**[Go]** is an open source, statically typed, compiled programming language.

Go can be used to write software, and is used to make some of the packages that are available in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Update]](#Update)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/go](https://packages.gentoo.org/packages/dev-lang/go) [[]] [A concurrent garbage collected and typesafe programming language]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-09 13:01] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install Go:

`root `[`#`]`emerge --ask dev-lang/go`

## [Update]

Because of Go static linking packages built with an old version of Go will retain vulnerabilities that were fixed in newer versions until rebuilt. Fortunately portage will take care of recompiling vulnerable packages for you with BDEPEND slot-operators.

## [Configuration]

### [Environment variables]

Users may customize how Go builds packages by setting these variables, similar to the way the C build system is configured using `CFLAGS` or `LDFLAGS`:

-   `GOAMD64` (corresponds to x86_64 [microarchitecture levels](https://en.wikipedia.org/wiki/X86-64#Microarchitecture_levels "wikipedia:X86-64"))
-   `GO386` (for x86)
-   `GOARM` (for arm)
-   `CGO_CFLAGS`
-   `CGO_CXXFLAGS`
-   `CGO_FFLAGS`
-   `CGO_LDFLAGS`

For example, in [/etc/portage/make.conf], one may set:

[FILE] **`/etc/portage/make.conf`**

    CGO_CFLAGS="$"
    CGO_CXXFLAGS="$"
    CGO_FFLAGS="$"
    CGO_LDFLAGS="$"

    # https://github.com/golang/go/wiki/MinimumRequirements#architectures
    # Pick carefully based on https://en.wikipedia.org/wiki/X86-64#Microarchitecture_levels!
    # For amd64 (v1 (default)/v2/v3/v4):
    #GOAMD64="v3"
    # For x86 (sse2 (default)/softfloat):
    #GO386=sse2
    # For arm (5/6 (usually default)/7):
    #GOARM=6

** Warning**\
The `MinimumRequirements` variables for optimization at compilation time, as with [CFLAGS](https://wiki.gentoo.org/wiki/CFLAGS "CFLAGS"), will produce binaries that will not run on unsupported processors.

## [Usage]

### [Invocation]

`user `[`$`]`go --help`

    Go is a tool for managing Go source code.

    Usage:

        go <command> [arguments]

    The commands are:

        bug         start a bug report
        build       compile packages and dependencies
        clean       remove object files and cached files
        doc         show documentation for package or symbol
        env         print Go environment information
        fix         update packages to use new APIs
        fmt         gofmt (reformat) package sources
        generate    generate Go files by processing source
        get         add dependencies to current module and install them
        install     compile and install packages and dependencies
        list        list packages or modules
        mod         module maintenance
        work        workspace maintenance
        run         compile and run Go program
        test        test packages
        tool        run specified go tool
        version     print Go version
        vet         report likely mistakes in packages

    Use "go help <command>" for more information about a command.

    Additional help topics:

        buildconstraint build constraints
        buildmode       build modes
        c               calling between Go and C
        cache           build and test caching
        environment     environment variables
        filetype        file types
        go.mod          the go.mod file
        gopath          GOPATH environment variable
        gopath-get      legacy GOPATH go get
        goproxy         module proxy protocol
        importpath      import path syntax
        modules         modules, module versions, and more
        module-get      module-aware go get
        module-auth     module authentication using go.sum
        packages        package lists and patterns
        private         configuration for downloading non-public code
        testflag        testing flags
        testfunc        testing functions
        vcs             controlling version control with GOVCS

    Use "go help <topic>" for more information about that topic.

## [Removal]

### [Unmerge]

To remove Go:

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/go`

## [See also]

-   [Writing go Ebuilds](https://wiki.gentoo.org/wiki/Writing_go_Ebuilds "Writing go Ebuilds") --- a short reference, intended to be read alongside [Basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") and the [go-module.eclass documentation](https://devmanual.gentoo.org/eclass-reference/go-module.eclass/index.html)
-   [Application level package management](https://wiki.gentoo.org/wiki/Application_level_package_management "Application level package management") --- provides best practice recommendations on managing the coexistence of operating system and **application level package managers** on Gentoo.