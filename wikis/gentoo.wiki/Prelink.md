Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Prelink/fr "Prelink (100% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Prelink/it "Prelink (6% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Prelink/hu "Prelink (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Prelink/ru "Prelink (92% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Prelink/ja "Prelink (19% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Prelink/ko "Prelink (90% translated)")

**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only. *Page archived as of **Feb 23, 2022**.*

\
TLDR: **Do not use this article!**

\

** Warning**\
The glibc upstream has removed prelink support in glibc-2.35, so support for prelinking cannot be kept. The core package *sys-devel/prelink* explained below, is no longer available from the Gentoo ebuild repository since Feb 23, 2022. See [[[bug #579374]](https://bugs.gentoo.org/show_bug.cgi?id=579374)[]] or [[[bug #726062]](https://bugs.gentoo.org/show_bug.cgi?id=726062)[]] for details.

This guide tells you how to make use of prelink support in Portage 2.0.46 and later.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [What is Prelink and how can it help me?]](#What_is_Prelink_and_how_can_it_help_me.3F)
    -   [[1.2] [Summary]](#Summary)
-   [[2] [Setting up Prelink]](#Setting_up_Prelink)
    -   [[2.1] [Installing the Programs]](#Installing_the_Programs)
    -   [[2.2] [Preparing your System]](#Preparing_your_System)
    -   [[2.3] [Configuration]](#Configuration)
-   [[3] [Prelinking]](#Prelinking)
    -   [[3.1] [Prelink Usage]](#Prelink_Usage)
    -   [[3.2] [Prelink Cron Job]](#Prelink_Cron_Job)
    -   [[3.3] [Speeding Up KDE After Prelinking]](#Speeding_Up_KDE_After_Prelinking)
    -   [[3.4] [Removing prelink]](#Removing_prelink)
-   [[4] [Known Problems and Fixes]](#Known_Problems_and_Fixes)
    -   [[4.1] [\"Cannot prelink against non-PIC shared library\"]](#.22Cannot_prelink_against_non-PIC_shared_library.22)
    -   [[4.2] [When I prelink my system some static binaries don\'t work anymore]](#When_I_prelink_my_system_some_static_binaries_don.27t_work_anymore)
    -   [[4.3] [Prelink aborts with \"prelink: dso.c:306: fdopen_dso: Assertion \`j == k\' failed.\"]](#Prelink_aborts_with_.22prelink:_dso.c:306:_fdopen_dso:_Assertion_.60j_.3D.3D_k.27_failed..22)
    -   [[4.4] [I use grsecurity and it seems that prelinking doesn\'t work.]](#I_use_grsecurity_and_it_seems_that_prelinking_doesn.27t_work.)
    -   [[4.5] [Prelink fails with error \"prelink: Can\'t walk directory tree XXXX: Too many levels of symbolic links\"]](#Prelink_fails_with_error_.22prelink:_Can.27t_walk_directory_tree_XXXX:_Too_many_levels_of_symbolic_links.22)
-   [[5] [Conclusion]](#Conclusion)

## [Introduction]

### [][What is Prelink and how can it help me?]

Most common applications make use of shared libraries. These shared libraries need to be loaded into memory at runtime and the various symbol references need to be resolved. For most small programs this dynamic linking is very quick. But for programs written in C++ and that have many library dependencies, the dynamic linking can take a fair amount of time.

On most systems, libraries are not changed very often and when a program is run, the operations taken to link the program are the same every time. Prelink takes advantage of this by carrying out the linking and storing it in the executable, in effect prelinking it.

Prelinking can cut the startup times of applications. For example, a typical KDE program\'s loading time can be cut by as much as 50%. The only maintenance required is re-running prelink every time a library is upgraded for a pre-linked executable.

** Warning**\
Prelink will not work with Hardened Gentoo. This is because both projects try to change the address space mapping of shared libraries. But prelink with the -R option randomises library base addresses, providing some degree of hardened protection.

### [Summary]

-   Prelinking is done via a program called, surprisingly, `prelink` . It changes the binary to make it start faster.
-   If an application\'s dependent libraries change after you have prelinked it, you need to re-prelink the application, otherwise you lose the speed advantage. This is to say, everytime you update a package via portage that updates libraries, they need to be re-prelinked.
-   The change to the binary is fully reversible. `prelink` has an undo function.
-   Current versions of Portage can handle, via `prelink` , the changing MD5sums and mtimes of the binaries.
-   You do not need to set `FEATURES="prelink"` in your [make.conf] file; Portage will automatically support prelink if it can find the prelink binary.

## [Setting up Prelink]

### [Installing the Programs]

First you need to install the `prelink` tool. The emerge process automatically verifies that your system can prelink safely.

`root `[`#`]`emerge --ask prelink`

A number of people get errors in emerging prelink because of the failed tests. The tests were put in for safety reasons, prelink\'s behavior is undefined if you disable them. The emerge errors are usually only dependent on the core packages; binutils, gcc, and glibc. Try re-emerging those packages in that order.

** Note**\
Tip: If you get an error try compiling and testing `prelink` yourself ( `./configure` ; `make` ; `make check` ). On a failure you can view the \*.log files in the testsuite directory. They may provide you with some useful clues.

If you have a set of steps that reproduces the emerge error on another system please check [Bugzilla](https://bugzilla.gentoo.org) and create a bug report if it has not already been reported.

### [Preparing your System]

Also make sure that you do *not* have -fPIC set in your CFLAGS/CXXFLAGS. If you do, you will need to rebuild your entire system without.

### [Configuration]

Running `env-update` will generate the [/etc/prelink.conf] file that tells [prelink] which files to prelink.

`root `[`#`]`env-update`

Unfortunately you cannot prelink files that were compiled by old versions of binutils. Most of these applications come from pre-compiled, binary only packages which are installed in [/opt] . Making the following file will tell prelink not to attempt to prelink them.

[FILE] **`/etc/env.d/60prelink`**

    PRELINK_PATH_MASK="/opt"

** Note**\
You can add more or less directories to the colon separated list.

## [Prelinking]

### [Prelink Usage]

I use the following command to prelink all the binaries in the directories given by [/etc/prelink.conf] .

`root `[`#`]`prelink -amR`

** Warning**\
It has been observed that if you are low on disk space and you prelink your entire system then there is a possibility that your binaries may be truncated. The result being a b0rked system. Use the `file` or `readelf` command to check the state of a binary file. Alternatively, check the amount of free space on your harddrive ahead of time with `df -h` .

  ------------------------ -------------------------------------------------------------------------------------------------------------
  The options explained:
  -a                       \"All\": prelinks all the binaries
  -m                       Conserve the virtual memory space. This is needed if you have a lot of libraries that need to be prelinked.
  -R                       Random \-- randomize the address ordering, this enhances security against buffer overflows.
  ------------------------ -------------------------------------------------------------------------------------------------------------

** Note**\
For more options and details see `man prelink` .

### [Prelink Cron Job]

`sys-devel/prelink` installs a cron job in [/etc/cron.daily/prelink] . To enable it, edit the configuration file [/etc/conf.d/prelink] . This will run prelink daily in the background, as needed, saving you running the command manually.

### [Speeding Up KDE After Prelinking]

KDE\'s loading time can be greatly reduced after prelinking. If you inform KDE that it has been prelinked it will disable the loading of `kdeinit` (as it isn\'t required anymore) which speeds up KDE even more.

Set `KDE_IS_PRELINKED=1` in [/etc/env.d/\*kdepaths\*] to inform KDE about the prelinking.

### [Removing prelink]

If you ever change your mind about prelinking, before you unmerge prelink, you\'ll first need to remove the prelink cronjob from [/etc/cron.daily] and [/etc/conf.d/prelink] . Next, you\'ll have to remove prelinking from all binaries:

`root `[`#`]`prelink -au`

Finally, unmerge the `prelink` package itself:

`root `[`#`]`emerge -c prelink`

## [Known Problems and Fixes]

### [][\"Cannot prelink against non-PIC shared library\"]

The cause of this problem is from badly compiled shared libraries that were compiled without the -fPIC gcc option for all their object files.

Here are the libraries that haven\'t been fixed or cannot be fixed:

-   The libraries in the wine package, including winex. Prelinking wouldn\'t speed up MS Windows executables anyway.
-   The library in media-video/mjpegtools, [/usr/lib/liblavfile-1.6.so.0] .
-   Nvidia OpenGl libraries, [/usr/lib/opengl/nvidia/lib/libGL.so.\*] . Due to performance reasons they were compiled without PIC support.

If your problem library was not listed please report it with, preferably, a patch to add `-fPIC` to the relevant CFLAGS.

### [][When I prelink my system some static binaries don\'t work anymore]

Where glibc is concerned, there is no such thing as a 100% static binary. If you statically compile a binary with glibc, it may still depend on other system files. Below is an explanation by Dick Howell,

\"I suppose the idea is that everything will be in the downloaded file, so nothing depends on the local libraries on the target system. Unfortunately with Linux, and I think anything else using GLIBC, this still isn\'t quite true. There\'s this \"libnss\" (name service switch, some people seem to call it network security system) which provides functions for accessing various databases for authentication, network information, and other things. It\'s supposed to make application programs independent of the separately configured actual network environment of the machine. A nice idea, but changes to GLIBC can lead to problems loading it. And you can\'t statically link \"libnss\", since it is configured for each machine individually. The problem comes, I think, mainly from statically linking other GLIBC libraries, notably \"libpthread\", \"libm\", and \"libc\", from which come incompatible calls to \"libnss\" functions.\"

### [][Prelink aborts with \"prelink: dso.c:306: fdopen_dso: Assertion \`j == k\' failed.\"]

This a known problem, kindly diagnosed [[[here]](https://bugs.gentoo.org/show_bug.cgi?id=13878)[]]. Prelink cannot cope with UPX-compressed executables. As of prelink-20021213 there is no fix except to hide the executables while you are prelinking. See the section above for an easy way to do this.

### [][I use grsecurity and it seems that prelinking doesn\'t work.]

In order to prelink on a system with grsecurity using a randomized mmap() base, it is necessary to turn \"randomized mmap() base\" OFF for [/lib/ld-2.3.\*.so] . This can be done with the `chpax` utility, but it must be done when the file is not in use (f.i. boot from a rescue CD).

### [][Prelink fails with error \"prelink: Can\'t walk directory tree XXXX: Too many levels of symbolic links\"]

Your symlinks are nested too deeply. This happens when a symlink points to itself. For example, [/usr/lib/lib -\> lib] is the most common. To fix this, you can find the symlink manually or use the utility provided by the `symlinks` package:

`root `[`#`]`emerge symlinks `

`root `[`#`]`symlinks -drv /`

More details can be found at [[[Bugzilla]](https://bugs.gentoo.org/show_bug.cgi?id=82117)[]] and this [forum post](https://forums.gentoo.org/viewtopic-t-458144-highlight-prelink.html) .

## [Conclusion]

Prelinking can drastically speed up the start up times for a number of large applications. Support is built into Portage. Prelinking is also safe as you can always undo the prelinking for any binary if you come across any problems. Just remember that when you update glibc or other libraries that you prelinked with, you need to rerun [prelink] ! In short good luck!

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Stefan Jones, John P. Davis, Jorge Paulo, Erwin, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*