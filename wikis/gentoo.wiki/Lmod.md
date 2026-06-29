[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lmod&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.tacc.utexas.edu/research-development/tacc-projects/lmod)

[[]][Official documentation](https://lmod.readthedocs.io/en/latest/)

[[]][GitHub](https://github.com/TACC/Lmod)

[Lmod] is a [Lua](https://wiki.gentoo.org/wiki/Lua "Lua")-based module system that easily handles the MODULEPATH Hierarchical problem. Environment Modules provide a convenient way to dynamically change the users\' environment through modulefiles. A modulefile contains the necessary information to manipulate the users\' environment; such as information to add or remove directories from the `PATH`, `LD_LIBRARY_PATH`, `CPATH` and other environment variables. All popular [shells](https://wiki.gentoo.org/wiki/Shell "Shell") are supported, including [Bash](https://wiki.gentoo.org/wiki/Bash "Bash"), csh, [fish](https://wiki.gentoo.org/wiki/Fish "Fish"), ksh, sh, tcsh, [zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh"), as well as some scripting languages such as [Tcl/Tk](https://wiki.gentoo.org/wiki/Tkinter "Tkinter"), [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") and [Python](https://wiki.gentoo.org/wiki/Python "Python").

[Lmod] is used in HPC clusters, research labs and scientific computing environments all over the world. It is an alternative implementation for the classic Tcl/TK [environment modules](https://modules.readthedocs.io/en/latest/index.html) and improves upon it by creating module hierarchies, which allow setting of proper dependency structures for more stringent regulation of module loading and unloading.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
-   [[4] [Spider Cache]](#Spider_Cache)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-cluster/lmod](https://packages.gentoo.org/packages/sys-cluster/lmod) [[]] [Environment Module System based on Lua]

  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+auto-swap`](https://packages.gentoo.org/useflags/+auto-swap)             enable auto swapping of compiler
  [`+cache`](https://packages.gentoo.org/useflags/+cache)                     enable caching of modules
  [`duplicate-paths`](https://packages.gentoo.org/useflags/duplicate-paths)   allow duplicate entries in path
  [`test`](https://packages.gentoo.org/useflags/test)                         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-22 13:06] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-cluster/lmod`

## [Configuration]

### [Files]

-   [/etc/modulefiles/] - Default location for modulefiles.
-   [/etc/lmod_cache/spider_cache] - Default spider cache directory.
-   [/etc/lmod_cache/system.txt] - Default spider cache file.

## [Usage]

The default installation enables the [module] command for all users, by sourcing [/etc/profile.d/lmod.sh].\

`user `[`$`]` man module `

`user `[`$`]` module -h `

## [Spider Cache]

By default, [Lmod] enables spider cache. It is highly recommended to keep the spider cache enabled and up to date. The following command updates the spider cache.

`root `[`#`]`/usr/share/Lmod/libexec/update_lmod_system_cache_files $MODULEPATH`

## [References]