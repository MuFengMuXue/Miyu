*Not to be confused with [Sandbox](https://wiki.gentoo.org/wiki/Sandbox "Sandbox").*

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Sandbox "Project:Sandbox")][Project](https://wiki.gentoo.org/wiki/Project:Sandbox "Project:Sandbox")

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/sandbox)

[[]][GitWeb](https://gitweb.gentoo.org/proj/sandbox.git)

[[]][GitHub](https://github.com/gentoo/sandbox)

** Tip**\
This article describes Sandbox from a user\'s perspective. Those looking to contribute to Sandbox development should visit the [Sandbox project page](https://wiki.gentoo.org/wiki/Project:Sandbox "Project:Sandbox")

Sandbox is a library (and helper utility) to run programs in a \"sandboxed\" environment, i.e. to restrict a process\'s access to system ressources. This is used as a QA measure to try and prevent applications from modifying files they should not.

In Gentoo, it is used to build applications as root, making sure that the build system does not do anything harmful outside of its build directory - such as install files to the live root file system or modify config files on the fly.

For people who are familiar with the Debian \"fakeroot\" project or the RPM based \"InstallWatch\", sandbox is in the same vein of these projects.

## Contents

-   [[1] [How sandboxing works]](#How_sandboxing_works)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Sandbox Violations]](#Sandbox_Violations)
-   [[5] [External resources]](#External_resources)

## [How sandboxing works]

When using the sandbox, some environment variables are set to provide some configuration to sandbox, then the LD_PRELOAD variable is set.

When the ELF loader runs, it will now load the sandbox library first. Whenever applications make a library call that is wrapped by sandbox, the arguments will be checked and any access that is not permitted is logged and an error is returned. Any access that is permitted is of course forwarded along to the real C library.

Static ELFs and setuid/setgid programs require [another method](https://gitweb.gentoo.org/proj/sandbox.git/tree/README.md).

## [Installation]

All Gentoo installations come with Sandbox. Like all data, there is a possibility Sandbox can become corrupted or even uninstalled, which is *very* bad. If this is the case there *are* ways Sandbox can be recovered.

### [Emerge]

`root `[`#`]`emerge --ask --oneshot sys-apps/sandbox`

## [Configuration]

### [Files]

There are multiple files used to configure Sandbox.

See [/etc/sandbox.conf](https://wiki.gentoo.org/wiki//etc/sandbox.conf "/etc/sandbox.conf") and [/etc/sandbox.d/\*] configuration files for more information.

## [Troubleshooting]

### [Sandbox Violations]

-   [[[bug #717586]](https://bugs.gentoo.org/show_bug.cgi?id=717586)[]]

## [External resources]

-   [https://wiki.debian.org/FakeRoot](https://wiki.debian.org/FakeRoot)
-   [https://asic-linux.com.mx/\~izto/checkinstall/installwatch.html](https://asic-linux.com.mx/~izto/checkinstall/installwatch.html)