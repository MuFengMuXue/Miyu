**Resources**

[[]][[#gentoo-prefix](ircs://irc.libera.chat/#gentoo-prefix)] ([[webchat](https://web.libera.chat/#gentoo-prefix)])

This article provides instructions for any poor soul attempting to bootstrap Gentoo Prefix on a Microsoft Windows system via Cygwin.

## Contents

-   [[1] [Preface: Prefix on Cygwin]](#Preface:_Prefix_on_Cygwin)
    -   [[1.1] [Overview]](#Overview)
    -   [[1.2] [What is this?]](#What_is_this.3F)
    -   [[1.3] [Why do this?]](#Why_do_this.3F)
-   [[2] [Restrictions]](#Restrictions)
-   [[3] [Installing Cygwin]](#Installing_Cygwin)
    -   [[3.1] [Space and paths]](#Space_and_paths)
    -   [[3.2] [User and permissions]](#User_and_permissions)
    -   [[3.3] [Additional packages]](#Additional_packages)
    -   [[3.4] [Additional setup]](#Additional_setup)
-   [[4] [Install Gentoo Prefix]](#Install_Gentoo_Prefix)
-   [[5] [External resources]](#External_resources)

## [Preface: Prefix on Cygwin]

How to bootstrap Gentoo Prefix on Cygwin?

### [Overview]

At the beginning some general advice is given on how to setup Cygwin. There are a few restrictions for the Cygwin setup that users need to bear in mind to have success with Gentoo Prefix on Cygwin.

### [][What is this?]

There was also a project \"Gentoo on Cygwin\" which is unmaintained as of 2008. Note the difference to \"Gentoo Prefix on Cygwin\". \"Gentoo Prefix on Cygwin\" is not a project itself but simply a try to run the well maintained \"Gentoo Prefix\" sources on Cygwin.

### [][Why do this?]

Running Prefix on Cygwin provides the same runtime environment on Windows as possible on Linux or Mac. It brings much more options than a Java runtime environment and it requires less resources than a virtual machine. Additionally, any program can be compiled by using Gentoo\'s package manager. Finally, all this happens in the userspace which provides independence from the administrator account. Nothing compares to this.

## [Restrictions]

Unix/Linux based package managers usually do require the `fork()` system call, which is not available in Windows in general. Nevertheless, Cygwin implements the `fork()` system call using the `CreateProcess()` and `LoadLibrary()` Windows calls, combined with sophisticated duplication of process memory, loaded libraries, and open handles into the child process.

But this requires `CreateProcess()` and `LoadLibrary()` to locate the very same binaries (executable and DLLs) as loaded in the parent process.

Imagine what happens when the package manager has replaced these binaries, while existing processes (including the package manager itself) still want to fork.

Since Cygwin 3.0.0-0.8, the `fork()` system call is able to deal with removed or updated binaries. However, the implementation still imposes some additional requirements to the Cygwin setup to actually work:

-   An **NTFS** file system for the Cygwin installation to install into.
-   Use this very **same** NTFS file system for Gentoo Prefix to install into.

The reason here is that the original executables are *hardlinked* into the [/var/run/cygfork/] directory. Please find more details under the [Additional setup](#Additional_setup) section.

## [Installing Cygwin]

Cygwin comes with a full featured installer that explains itself:

-   64-bit: [https://www.cygwin.com/setup-x86_64.exe](https://www.cygwin.com/setup-x86_64.exe)
-   32-bit: [https://www.cygwin.com/setup-x86.exe](https://www.cygwin.com/setup-x86.exe)
    -   Important: Although it may \'work\', 32-bit Cygwin is *not* supported by the Gentoo Prefix project!

### [Space and paths]

Before installing Cygwin consider the path. Prefix does not play nicely with paths that include whitespace (a space character); not all scripts can handle whitespace in paths. Ensure a Windows user account *without* whitespace in the username. Have enough free space. A minimum 4 GB will be needed. Up to 10 GB or more may be (eventually) consumed.

Presume \"prefix\" has been chosen as the username and Cygwin is installed at [P:\\cygwin64] (being a mnemonic for Prefix Cygwin):

-   Windows perspective: [P:\\cygwin64\\home\\prefix]
-   Cygwin perspective: [/home/prefix]

** Important**\
Remember to **choose the same NTFS** partition for both the Cygwin installation directory and the Gentoo Prefix installation directory.

### [User and permissions]

Install Cygwin from the same windows account that will be using it. This way some trouble can be avoided with user permissions and administration.

### [Additional packages]

The Gentoo Prefix bootstrap aims to require as less as possible packages installed on the underlying operating system. However, a minimal set of compilation environment plus a file download tool is required. In addition to the default selection done by the Cygwin setup please install these additional packages and their automatically added dependencies:

-   [gcc-g++]
-   [wget]

### [Additional setup]

The extended fork feature mentioned above is disabled by default, it will need to be enabled manually:

-   Unfortunately, Cygwin version 3.0.7 still lacks some patches for the `fork()` implementation to be good enough for Gentoo Prefix. So you need to use a [cygwin1.dll with additional patches applied](http://dev.gentoo.org/~haubi/cygwin-gentoo/).

<!-- -->

-   Don\'t forget to set the executable permission when you download a precompiled cygwin1.dll using some Cygwin program. Windows programs may already set the executable permission for a downloaded dll.

<!-- -->

-   Use Windows utilities to replace the current [cygwin1.dll] file with the new one located the [bin] directory of the cygwin installation (probably [C:\\cygwin\\bin] if defaults were used).

<!-- -->

-   Create the [/var/run/cygfork/] Cygwin directory; the Cygwin setup does not create it. To do so start the [mintty] console and run:

`user `[`$`]`mkdir --mode=a=rwxt /var/run/cygfork`

-   Finally, **reboot** Windows, to make sure the initial Cygwin process started already finds the [/var/run/cygfork/] directory in place, to actually activate the fork handler for removed or replaced binaries for this Cygwin instance.

## [Install Gentoo Prefix]

Simply follow the [general bootstrap process](https://wiki.gentoo.org/wiki/Project:Prefix/Bootstrap "Project:Prefix/Bootstrap").

## [External resources]

-   [Interix](https://en.wikipedia.org/wiki/Interix "wikipedia:Interix") - A now deprecated, optional, POSIX-conformant Unix subsystem for Windows NT operating systems.