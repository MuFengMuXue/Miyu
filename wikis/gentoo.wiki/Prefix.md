**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Prefix "Project:Prefix")][Project](https://wiki.gentoo.org/wiki/Project:Prefix "Project:Prefix")

**Gentoo Prefix** enables the power of Gentoo and [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") on other distributions and/or operating systems (Microsoft Windows via Cygwin, Android via Termux, etc.).

Prefix can be thought of as being like an app store, along the lines of Homebrew, Snap, or Flatpak - which opens all the packages offered in Gentoo to systems that do not have such functionality.

** Tip**\
Whenever a piece of software needs to be compiled on a binary distribution, why download and compile source tarballs and dependencies, only to clutter the root filesystem with files that don\'t always have an easy way to be uninstalled ? Let Gentoo Prefix handle downloading, dependency resolution, configuration, compiling, installation, updates, removal, and more.\
\
Be it because there is no binary installation option available, or because a **particular compile time option is needed** - use Gentoo Prefix to easily compile and install the software safely, as a package!

Gentoo prefix grants access to the huge amount of up-to-date software from the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), as well as from [GURU](https://wiki.gentoo.org/wiki/GURU "GURU"), and from any other publicly accessible repository. It brings with it the great flexibility of the [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") system, with easy installation, updates, and removal of packages.

Gentoo Prefix is installed onto a system as a third party piece of software, and will work with with most Linux, and some Unix(like), systems.

While the Gentoo Linux distribution is traditionally used to install a Linux kernel with a boot loader, like most other Linux distributions, Prefix is a way of installing a Gentoo system in a non-standard location, designated by a \'prefix\', on a preexisting system.

Prefix is tested on many [GNU/Linux distributions](https://wiki.gentoo.org/wiki/Prefix/tested "Prefix/tested"), and should work on most. Of course, Prefix can also be used on a Gentoo installation.

See the [Prefix project page](https://wiki.gentoo.org/wiki/Project:Prefix "Project:Prefix") for more information.

## [Examples of when to use Prefix]

-   If using a campus server with an old version of Linux and only have limited access, then Prefix would give the user the ability to run newer software for their needs.
-   The ability to use Linux programs inside operating systems such as macOS and Solaris.

\

## [See also]

-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.
-   [Prefix/CJK](https://wiki.gentoo.org/wiki/Prefix/CJK "Prefix/CJK") - use CJK characters in Prefix, independently of the host system.

### [Gentoo prefix on different systems]

-   [Gentoo in WSL](https://wiki.gentoo.org/wiki/Gentoo_in_WSL "Gentoo in WSL") --- documents the process and some configuration tips to get Gentoo running on [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux "wikipedia:Windows Subsystem for Linux") (Windows Subsystem for Linux) - to effectively **run Gentoo under Windows**.
-   [Prefix/Cygwin](https://wiki.gentoo.org/wiki/Prefix/Cygwin "Prefix/Cygwin") --- instructions for any poor soul attempting to bootstrap Gentoo Prefix on a Microsoft Windows system via Cygwin.
-   [Prefix/Darwin](https://wiki.gentoo.org/wiki/Prefix/Darwin "Prefix/Darwin") --- brings the power of Gentoo to Darwin (macOS/OS X) based systems, similar to pkgsrc, macports, and homebrew.
-   [Prefix/NetBSD](https://wiki.gentoo.org/wiki/Prefix/NetBSD "Prefix/NetBSD") --- work in progress; page simply contains notes about efforts to get it up and running.
-   [Project:Android](https://wiki.gentoo.org/wiki/Project:Android "Project:Android")