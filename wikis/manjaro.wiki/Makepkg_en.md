[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Makepkg&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Makepkg "Makepkg (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Makepkg/tr "Makepkg (3% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Makepkg/ru "Makepkg (100% translated)")

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Architecture, compile flags]](#Architecture.2C_compile_flags)
        -   [[1.1.1] [MAKEFLAGS]](#MAKEFLAGS)
    -   [[1.2] [Package output]](#Package_output)
    -   [[1.3] [Signature checking]](#Signature_checking)
-   [[2] [Usage]](#Usage)
-   [[3] [Tips and Tricks]](#Tips_and_Tricks)
    -   [[3.1] [Improving compile times]](#Improving_compile_times)
    -   [[3.2] [Generate new md5sums]](#Generate_new_md5sums)
    -   [[3.3] [Makepkg source PKGBUILD twice]](#Makepkg_source_PKGBUILD_twice)
    -   [[3.4] [WARNING: Package contains reference to \$srcdir]](#WARNING:_Package_contains_reference_to_.24srcdir)
    -   [[3.5] [Create uncompressed packages]](#Create_uncompressed_packages)

makepkg is used for compiling and building packages suitable for installation with [pacman](//wiki.manjaro.org/index.php?title=Pacman "Pacman"). makepkg is a script that automates the building of packages. It can download and validate source files, check dependencies, configure build-time settings, compile the sources, install into a temporary root, make customizations, generate meta-info, and package everything together.

makepkg is provided by the [pacman](//wiki.manjaro.org/index.php?title=Pacman "Pacman") package.

## [Configuration]

`/etc/makepkg.conf` is the main configuration file for makepkg. Most users will wish to fine-tune makepkg configuration options prior to building any packages.

A user specific configuration file which takes precedence over the system wide configuration may exist in `$HOME/.makepkg.conf`. This is important to note if using i3, cinnamon, or deepin as the manjaro-desktop-settings packages for these desktop environments automatically create the user configuration file for new users by way of `/etc/skel/.makepkg.conf`.

### [][Architecture, compile flags]

The `MAKEFLAGS`, `CFLAGS`, and `CXXFLAGS` options are used by `make`, `gcc`, and `g++` whilst compiling software with makepkg. By default, these options generate generic packages that can be installed on a wide range of machines. A performance improvement can be achieved by tuning compilation for the host machine. The downside is that packages compiled specifically for the compiling host\'s processor may not run on other machines.

\

**Note**

------------------------------------------------------------------------

Do keep in mind that not all package build systems will use your exported variables. Some override them in the original Makefiles or the [PKGBUILD](//wiki.manjaro.org/index.php?title=PKGBUILD "PKGBUILD").

```
/etc/makepkg.conf
```

```
[...]

#########################################################################
# ARCHITECTURE, COMPILE FLAGS
#########################################################################
#
CARCH="x86_64"
CHOST="x86_64-unknown-linux-gnu"

#-- Exclusive: will only run on x86_64
# -march (or -mcpu) builds exclusively for an architecture
# -mtune optimizes for an architecture, but builds for whole processor family
CPPFLAGS="-D_FORTIFY_SOURCE=2"
CFLAGS="-march=x86-64 -mtune=generic -O2 -pipe -fstack-protector --param=ssp-buffer-size=4"
CXXFLAGS="-march=x86-64 -mtune=generic -O2 -pipe -fstack-protector --param=ssp-buffer-size=4"
LDFLAGS="-Wl,-O1,--sort-common,--as-needed,-z,relro"
#-- Make Flags: change this for DistCC/SMP systems
#MAKEFLAGS="-j2"

[...]
```

The default makepkg.conf `CFLAGS` and `CXXFLAGS` are compatible with all machines within their respective architectures.

On x86_64 machines, there are rarely significant enough real world performance gains that would warrant investing the time to rebuild official packages.

As of version 4.3.0, GCC offers the `-march=native` switch that enables CPU auto-detection and automatically selects optimizations supported by the local machine at GCC runtime. To use it, just modify the default settings by changing the `CFLAGS` and `CXXFLAGS` lines as follows:

    # -march=native also sets the correct -mtune=
    CFLAGS="-march=native -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -D_FORTIFY_SOURCE=2"
    CXXFLAGS="$"

\

\

**Tip**

------------------------------------------------------------------------

To see what `march=native` flags are, run:

    $ gcc -march=native -E -v - </dev/null 2>&1 | sed -n 's/.* -v - //p'

Further optimizing for CPU type can theoretically enhance performance because `-march=native` enables all available instruction sets and improves scheduling for a particular CPU. This is especially noticeable when rebuilding applications (for example: audio/video encoding tools, scientific applications, math-heavy programs, etc.) that can take heavy advantage of newer instructions sets not enabled when using the default options (or packages) provided by Manjaro Linux.

It is very easy to reduce performance by using \"non-standard\" CFLAGS because compilers tend to heavily blow up the code size with loop unrolling, bad vectorization, crazy inlining, etc. depending on compiler switches. Unless you can verify/benchmark that something is faster, there is a very good chance it is not!

See the GCC man page for a complete list of available options. The Gentoo [Compilation Optimization Guide](http://www.gentoo.org/doc/en/gcc-optimization.xml) and [Safe CFLAGS](http://wiki.gentoo.org/wiki/Safe_CFLAGS) wiki article provide more in-depth information.

#### [MAKEFLAGS]

The `MAKEFLAGS` option can be used to specify additional options for make. Users with multi-core/multi-processor systems can specify the number of jobs to run simultaneously. This can be accomplished with the use of `nproc` to determine the number of available processors, e.g. `-j4` *(where 4 is the output of `nproc`)*. Some [PKGBUILD](//wiki.manjaro.org/index.php?title=PKGBUILD "PKGBUILD")\'s specifically override this with `-j1`, because of race conditions in certain versions or simply because it is not supported in the first place. Packages that fail to build because of this should be [reported](//wiki.manjaro.org/index.php?title=Reporting_Bug_Guidelines&action=edit&redlink=1 "Reporting Bug Guidelines (page does not exist)") on the bug tracker after making sure that the error is indeed being caused by your MAKEFLAGS.

See `man make` for a complete list of available options.

### [Package output]

Next, one can configure where source files and packages should be placed and identify themselves as the packager. This step is optional; packages will be created in the working directory where makepkg is run by default.

```
/etc/makepkg.conf
```

```
[...]

#########################################################################
# PACKAGE OUTPUT
#########################################################################
#
# Default: put built package and cached source in build directory
#
#-- Destination: specify a fixed directory where all packages will be placed
#PKGDEST=/home/packages
#-- Source cache: specify a fixed directory where source files will be cached
#SRCDEST=/home/sources
#-- Source packages: specify a fixed directory where all src packages will be placed
#SRCPKGDEST=/home/srcpackages
#-- Packager: name/email of the person or organization building packages
#PACKAGER="John Doe <john@doe.com>"

[...]
```

For example, create the directory:

    $ mkdir /home/$USER/packages

Then modify the `PKGDEST` variable in `/etc/makepkg.conf` accordingly.

The `PACKAGER` variable will set the `packager` value within compiled packages\' `.PKGINFO` metadata file. By default, user-compiled packages will display:

```
pacman -Qi package
```

```
[...]
Packager       : Unknown Packager
[...]
```

Afterwards:

```
pacman -Qi package
```

```
[...]
Packager       : John Doe <john@doe.com>
[...]
```

This is useful if multiple users will be compiling packages on a system, or you are otherwise distributing your packages to other users.

### [Signature checking]

The following procedure is not necessary for compiling with makepkg, for your initial configuration proceed to [#Usage](#Usage). To temporarily disable signature checking call the makepkg command with the `--skippgpcheck` option. If a signature file in the form of .sig is part of the [PKGBUILD](//wiki.manjaro.org/index.php?title=PKGBUILD "PKGBUILD") source array, makepkg validates the authenticity of source files. For example, the signature pkgname-pkgver.tar.gz.sig is used to check the integrity of the file pkgname-pkgver.tar.gz with the gpg program. If desired, signatures by other developers can be manually added to the gpg keyring. Look into the [GnuPG](//wiki.manjaro.org/index.php?title=GnuPG&action=edit&redlink=1 "GnuPG (page does not exist)") article for further information.

\

**Note**

------------------------------------------------------------------------

The signature checking implemented in makepkg does not use pacman\'s keyring. Configure gpg as explained below to allow makepkg reading pacman\'s keyring.

The gpg keys are expected to be stored in the user\'s `~/.gnupg/pubring.gpg` file. In case it does not contain the given signature, makepkg shows a warning.

```
makepkg
```

```
[...]
==> Verifying source file signatures with gpg...
pkgname-pkgver.tar.gz ... FAILED (unknown public key 1234567890)
==> WARNING: Warnings have occurred while verifying the signatures.
    Please make sure you really trust them.
[...]
```

To show the current list of gpg keys use the gpg command.

    gpg --list-keys

If the pubring.gpg file does not exist it will be created for you immediatly. You can now proceed with configuring gpg to allow compiling AUR packages submitted by Arch Linux developers with successful signature checking. Add the following line to the end of your gpg configuration file to include the pacman keyring in your user\'s personal keyring.

```
~/.gnupg/gpg.conf
```

```
[...]
keyring /etc/pacman.d/gnupg/pubring.gpg
```

When configured as before, the output of `gpg --list-keys` contains a list of keyrings and developers. Now makepkg can compile AUR packages submitted by Arch Linux developers with successful signature checking.

## [Usage]

Before continuing, ensure the \"base-devel\" group is installed. Packages belonging to this group are not required to be listed as dependencies in [PKGBUILD](//wiki.manjaro.org/index.php?title=PKGBUILD "PKGBUILD") files. Install the \"base-devel\" group by issuing (as root):

    # pacman -S base-devel

\

**Note**

------------------------------------------------------------------------

Before complaining about missing (make) dependencies, remember that the \"base\" group is assumed to be installed on all Manjaro Linux systems. The group \"base-devel\" is assumed to be installed when building with **makepkg**.

To build a package, one must first create a [PKGBUILD](//wiki.manjaro.org/index.php?title=PKGBUILD "PKGBUILD"), or build script, as described in [Create Manjaro Packages](//wiki.manjaro.org/index.php?title=Create_Manjaro_Packages "Create Manjaro Packages"), or obtain one from the [Manjaro Gitlab Repositories](https://gitlab.manjaro.org), [Arch User Repository](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository"), or some other source.

\

**Warning**

------------------------------------------------------------------------

Only build and/or install packages from trusted sources.

Once in possession of a `PKGBUILD`, change to the directory where it is saved and issue the following command to build the package described by said `PKGBUILD`:

    $ makepkg

To have makepkg clean out leftover files and folders, such as files extracted to the \$srcdir, add the following option. This is useful for multiple builds of the same package or updating the package version, while using the same build folder. It prevents obsolete and remnant files from carrying over to the new builds.

    $ makepkg -c

If required dependencies are missing, makepkg will issue a warning before failing. To build the package and install needed dependencies automatically, simply use the command:

    $ makepkg -s

Note that these dependencies must be available in the configured repositories; see [pacman](//wiki.manjaro.org/index.php?title=Pacman "Pacman") for details. Alternatively, one can manually install dependencies prior to building (`pacman -S --asdeps dep1 dep2`).

Once all dependencies are satisfied and the package builds successfully, a package file (`pkgname-pkgver.pkg.tar.xz`) will be created in the working directory. To install, run (as root):

    # pacman -U pkgname-pkgver.pkg.tar.xz

Alternatively, to install, using the `-i` flag is an easier way of running `pacman -U pkgname-pkgver.pkg.tar.xz`, as in:

    $ makepkg -i

## [Tips and Tricks]

### [Improving compile times]

As an I/O intensive task, the use of a [tmpfs](//wiki.manjaro.org/index.php?title=Tmpfs&action=edit&redlink=1 "Tmpfs (page does not exist)") for compiling packages may bring signifiant improvements in build times. Relevant option in `/etc/makepkg.conf` is to be found at the end of the `BUILD ENVIRONMENT` section:

```
/etc/makepkg.conf
```

```
[...]

#########################################################################
# BUILD ENVIRONMENT
#########################################################################
#
# Defaults: BUILDENV=(fakeroot !distcc color !ccache check !sign)
#  A negated environment option will do the opposite of the comments below.
#
#-- fakeroot: Allow building packages as a non-root user
#-- distcc:   Use the Distributed C/C++/ObjC compiler
#-- color:    Colorize output messages
#-- ccache:   Use ccache to cache compilation
#-- check:    Run the check() function if present in the PKGBUILD
#-- sign:     Generate PGP signature file
#
BUILDENV=(fakeroot !distcc color !ccache check !sign)
#
#-- If using DistCC, your MAKEFLAGS will also need modification. In addition,
#-- specify a space-delimited list of hosts running in the DistCC cluster.
#DISTCC_HOSTS=""
#
#-- Specify a directory for package building.
#BUILDDIR=/tmp

[...]
```

Uncommenting the `BUILDDIR=/tmp` line and setting it to e.g. `BUILDDIR=/tmp/builds` (or leaving it to its default value) will make use of Arch default `/tmp` [tmpfs](//wiki.manjaro.org/index.php?title=Tmpfs&action=edit&redlink=1 "Tmpfs (page does not exist)").

**Note**

------------------------------------------------------------------------

The [tmpfs](//wiki.manjaro.org/index.php?title=Tmpfs&action=edit&redlink=1 "Tmpfs (page does not exist)") folder needs to be mounted without the `noexec` option, else it will prevent build scripts or utilities from being executed. Also, as stated in [fstab#tmpfs](//wiki.manjaro.org/index.php?title=Fstab#tmpfs "Fstab"), its default size is half of the available RAM so you may run out of space.

For more information, please refer to [fstab](//wiki.manjaro.org/index.php?title=Fstab "Fstab") and [Tmpfs#Improving compile times](//wiki.manjaro.org/index.php?title=Tmpfs&action=edit&redlink=1 "Tmpfs (page does not exist)").

### [Generate new md5sums]

Since [pacman 4.1](http://allanmcrae.com/2013/04/pacman-4-1-released/) `makepkg -g >> PKGBUILD` is no longer required as pacman-contrib was [merged](https://projects.archlinux.org/pacman.git/tree/NEWS) along with the `updpkgsums` script that will generate new checksums and replace them in the PKGBUILD:

    $ updpkgsums

### [Makepkg source PKGBUILD twice]

Makepkg sources the PKGBUILD twice (once when initially run, and the second time under fakeroot). Any non-standard functions placed in the PKGBUILD will be run twice as well.

### [][WARNING: Package contains reference to \$srcdir]

Somehow, the literal strings `$srcdir` or `$pkgdir` ended up in one of the installed files in your package.

To identify which files, run the following from the makepkg build directory:

    $ grep -R "$(pwd)/src" pkg/

[Link](http://www.mail-archive.com/arch-general@archlinux.org/msg15561.html) to discussion thread.

### [Create uncompressed packages]

If you only want to install packages locally, you can speed up the process by avoiding compression and subsequent decompression. In `makepkg.conf`, change `PKGEXT='.pkg.tar.xz'` to `PKGEXT='.pkg.tar'`.