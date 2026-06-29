**Resources**

[[]][Home](https://learn.microsoft.com/en-us/powershell/)

[[]][Official documentation](https://learn.microsoft.com/en-us/powershell/scripting/overview)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/pwsh)

[[]][Wikipedia](https://en.wikipedia.org/wiki/PowerShell "wikipedia:PowerShell")

[[]][GitHub](https://github.com/PowerShell/PowerShell)

[[]][Bugs (upstream)](https://github.com/PowerShell/PowerShell/issues/)

[[]][[#powershell](ircs://irc.libera.chat/#powershell)] ([[webchat](https://web.libera.chat/#powershell)])

[[]][Blog](https://devblogs.microsoft.com/powershell/)

**PowerShell** is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. PowerShell runs on Windows, Linux, and macOS.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Changing the default version]](#Changing_the_default_version)
-   [[3] [Installing user-local modules]](#Installing_user-local_modules)
    -   [[3.1] [Installing system-wide modules]](#Installing_system-wide_modules)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See Also]](#See_Also)

## [Installation]

In Gentoo, PowerShell is provided by either the app-shells/pwsh-bin or app-shells/pwsh package. The first one is the official binary package from Microsoft that supports generic Linux systems, the second one is built from source on a given Gentoo system. Both of those packages can be installed simultaneously on the system. The selection between PowerShell versions and flavors (\"bin\" vs \"from-source\") on Gentoo systems is managed by the \"pwsh\" eselect module from the app-eselect/eselect-pwsh package.

There also exists a generic pwsh \"provider\" package virtual/pwsh that will default to the \"bin\" package first if it is possible to install it on the current system\'s architecture.

### [USE flags]

Only the app-shells/pwsh has some USE flags available, that is: \"debug\" and \"gui\".

### [USE flags for] [app-shells/pwsh](https://packages.gentoo.org/packages/app-shells/pwsh) [[]] [Cross-platform automation and configuration tool]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`gui`](https://packages.gentoo.org/useflags/gui)           Enable support for a graphical user interface
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)   Do not add extra patches which change default behaviour; DO NOT USE THIS ON A GLOBAL SCALE as the severity of the meaning changes drastically
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-23 23:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install PowerShell:

`root `[`#`]`emerge --ask virtual/pwsh`

## [Usage]

Launch PowerShell with:

`user `[`$`]`pwsh`

You can also launch individual PowerShell versions (installed via Gentoo SLOTs) directly. The following will start official PowerShell of version 7.4:

`user `[`$`]`pwsh-bin-7.4`

### [Changing the default version]

Using the pwsh eselect module you can switch the default PowerShell versions.

List available versions:

`root `[`#`]`eselect pwsh list`

Update current implementation:

`root `[`#`]`eselect pwsh update`

Set current implementation to the 1st item:

`root `[`#`]`eselect pwsh set 1`

## [Installing user-local modules]

List available modules:

`PS />``Get-Module -ListAvailable`

Install a module under the current user:

`PS />``Install-Module -Scope CurrentUser PSScriptAnalyzer`

### [Installing system-wide modules]

Gentoo provides a convenient way of installing PowerShell modules by just providing them as packages that can be emerged.

`root `[`#`]`emerge --ask app-shells/posh-git`

## [Removal]

To completely remove all packages related with PowerShell on Gentoo systems the support packages listed in above section have to be uninstalled as well as the main PowerShell provider package.

### [Unmerge]

To remove PowerShell:

`root `[`#`]`emerge --ask --depclean --verbose virtual/pwsh`

Then, if you installed the binary package:

`root `[`#`]`emerge --ask --depclean --verbose app-shells/pwsh-bin`

and in case of source-built:

`root `[`#`]`emerge --ask --depclean --verbose app-shells/pwsh`

A quick one-liner:

`root `[`#`]`emerge --deselect app-shells/pwsh app-shells/pwsh-bin virtual/pwsh app-eselect/eselect-pwsh && emerge --ask --depclean`

## [See Also]

-   [Project:Dotnet](https://wiki.gentoo.org/wiki/Project:Dotnet "Project:Dotnet") --- an effort to provide support for the .NET Core development platform within the Gentoo Linux operating system and a comprehensive set of packages for the .NET ecosystem, including the .NET SDK, development tools, and popular applications written using .NET.
-   [Dotnet/Devguide](https://wiki.gentoo.org/wiki/Dotnet/Devguide "Dotnet/Devguide") --- A .NET guide for Gentoo developers.