## Installing distro packages

New versions of openSUSE ship with the Wine development release that was
current at the time packages were frozen for release.

Up-to-date Wine packages are available through the [Wine
repository](https://en.opensuse.org/Additional_package_repositories#Wine)
on the OBS. The package maintainer is [Marcus
Meissner](mailto:meissner@suse.de). The repository includes packages for
the biweekly releases of both Wine and Wine-staging, daily "snapshot"
packages of git, and packages for wine-gecko and wine-mono. Simply add
the repository to Yast2 or zypper and install as you would any other
package.

Some notes about the openSUSE Wine packages:

- The packages include winetricks, installed to /usr/bin/.
- The packages include .desktop files for Wine's builtin programs
  (winecfg, notepad, etc.), which are not part of vanilla Wine. Report
  any problems with them to the package maintainer.
- The distro does not package the stable branch; however, packages for
  the stable releases may be available from personal projects on the
  OBS. Note that these packages are not supported by either WineHQ or
  the distro package maintainer.
- Restricted codecs needed by winegstreamer are available in the
  [Packman](https://packman.links2linux.org/) repository.

## Building Wine

### On the OBS

If you merely wish to recreate the distro package with minor
modifications (e.g., adding custom patches), the easiest way to do that
is by branching the
[Emulators:Wine](https://build.opensuse.org/project/show/Emulators:Wine)
package on the OBS, applying whatever changes you wish to make to the
spec file, and building from that. See the [openSUSE Build Service
Tutorial](https://en.opensuse.org/openSUSE:Build_Service_Tutorial) for
information on how to use the OBS.

### From Git

Building from git is necessary to run regression tests or test patches.

#### Cloning the Wine Git Repository

Follow the instructions in [the Git Wine
Tutorial](Git-Wine-Tutorial#set-up-your-git-repository) for cloning
the Wine git repository.

#### Build Tools and Dependencies

*The information in this section is based on openSUSE Leap 15 and Wine
3.13. Exact package names may vary depending on your version of
openSUSE, and new dependencies may be added in future Wine versions.
Always check the output of ./configure to verify that you have all
needed dependencies installed.*

The following repositories should be enabled to obtain basic build tools
and Wine's build dependencies:

- [OSS](https://en.opensuse.org/Package_repositories#OSS) (the main
  repository; this one is required, and should already be set up on your
  system)
- [Update](https://en.opensuse.org/Package_repositories#Update)
  (recommended in order to have the most up-to-date versions; for most
  people, this should also already be set up)
- [Wine](https://en.opensuse.org/Additional_package_repositories#Wine)
  (recommended, as installing a distro package will pull in Wine's
  runtime dependencies)

**Basic Build Tools**

The meta-package `patterns-openSUSE-devel_basis` will install the basic
tools needed for building (`gcc`, `make`, `flex`, `bison`). You should
also install `ccache`, and `git`. On a 64 bit system, you will also need
to install gcc-32bit and bison-32bit.

**Dependencies**

Installing the distro wine or wine-staging package is the easiest way to
install the libraries Wine depends on, as zypper or Yast2 will
automatically pull them in.

In addition to the runtime dependencies, the following development
packages are needed:

    alsa-devel capi4linux-devel dbus-1-devel fontconfig-devel freeglut-devel freetype2-devel giflib-devel glib2-devel glibc-devel glu-devel gstreamer-devel gstreamer-plugins-base-devel krb5-devel libcom_err-devel libexif-devel libgnutls-devel libgphoto2-devel libgsm-devel libjpeg8-devel liblcms2-devel libmpg123-devel libOSMesa-devel libpcap-devel libpng16-compat-devel libpulse-devel libSDL2-devel libtiff-devel libudev-devel libv4l-devel libX11-devel libXcomposite-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXxf86vm-devel libxml2-devel libXrandr-devel libXrender-devel libxslt-devel Mesa-libGL-devel mpg123-devel ncurses-devel openal-soft-devel opencl-headers openldap2-devel libopenssl-devel sane-backends-devel unixODBC-devel xorg-x11-devel vulkan-devel xz-devel zlib-devel

(Some of these packages may be installed by the
patterns-openSUSE-devel_basis package.)

On a 64 bit system, you will also need to install the following -32bit
packages:

    alsa-devel-32bit capi4linux-devel-32bit dbus-1-devel-32bit fontconfig-devel-32bit freeglut-devel-32bit freetype2-devel-32bit giflib-devel-32bit glib2-devel-32bit glibc-devel-32bit glu-devel-32bit krb5-devel-32bit libcom_err-devel-32bit libgnutls-devel-32bit libgphoto2-devel-32bit libgsm-devel-32bit libjpeg8-devel-32bit liblcms2-devel-32bit libOSMesa-devel-32bit libpcap-devel-32bit libpng16-compat-devel-32bit libpulse-devel-32bit libSDL2-devel-32bit libtiff-devel-32bit libv4l-devel-32bit libX11-devel-32bit libXcomposite-devel-32bit libXcursor-devel-32bit libXext-devel-32bit libXfixes-devel-32bit libXi-devel-32bit libXinerama-devel-32bit libXxf86vm-devel-32bit libxml2-devel-32bit libXrandr-devel-32bit libXrender-devel-32bit libxslt-devel-32bit Mesa-libGL-devel-32bit mpg123-devel-32bit ncurses-devel-32bit openal-soft-devel-32bit openldap2-devel-32bit libopenssl-devel-32bit unixODBC-devel-32bit xz-devel-32bit zlib-devel-32bit

(Installing the `wine-32bit-build-deps` package will install most of the
-32bit packages listed above.)

The glib2-devel-32bit packages for openSUSE versions 13.1, 13.2, and
Leap 42.1 were missing the 32 bit header and pkgconfig files needed to
compile 32 bit Wine with gstreamer support on a 64 bit system. The
workaround was to extract the missing files from the i586 glib2-devel
package and manually place the needed files in `/usr/include` and
`/usr/lib/pkgconfig`. This problem has been fixed in Leap 42.2 and
later. (See bug
[973217](https://bugzilla.opensuse.org/show_bug.cgi?id=973217))

After installing the above, in Leap 15 you will need to make the
following symlinks in `/usr/lib` or `./configure` will complain about
not being able to find the libraries:

```sh
$ ln -s libgstreamer-1.0.so.0 libgstreamer-1.0.so
$ ln -s libgstbase-1.0.so.0 libgstbase-1.0.so
$ ln -s libGL.so.1 libGL.so
```

The targets of the above symlinks may need to be adjusted for other
versions of openSUSE, depending on what version of the library you have
installed.

If ./configure complains about any other missing 32 bit development
files that you are sure are installed, check /usr/lib for missing .so
symlinks to the relevant library and create them.

At present no vkd3d packages have been built for Leap 15, and
./configure will complain about the missing vkd3d headers. Installing
the packages built for Tumbleweed may be an option, but this has not
been tested. The alternative would be to build vkd3d yourself locally.
Note that vkd3d is only needed for DirectX 12 support; if you do not
have any applications or games that need that, it is not necessary to
build Wine with vkd3d support.

Packages needed to build with HAL and OSSv4 support are not available
from any of the openSUSE repositories, and ./configure will complain
about it. Neither is needed on current versions of openSUSE; if those
are the only things ./configure complains about, you are good to go.

#### Building 32 bit Wine

**On a 32 bit system**

After cloning the git repository, cd to the wine-git directory and run

```sh
$ CC="ccache gcc"  ./configure  --disable-tests
```

Check the output of ./configure to make sure there are no missing
dependencies for features that you need. If there are, install them.
Assuming all is well, just run

```sh
$ make
```

**On a 64 bit system**

After cloning the git repository, cd to the wine-git directory and run

```sh
$ CC="ccache gcc -m32" PKG_CONFIG_PATH=/usr/lib/pkgconfig ./configure --disable-tests
```

Check the output of ./configure to make sure there are no missing
dependencies for features that you need. If there are, install them.
Assuming all is well, just run

```sh
$ make
```

#### Building Shared WoW64

If all your apps/games are 32 bit, there is no need to build 64 bit Wine
at all unless you are interested in helping with testing. Simply follow
the instructions in the preceding section to build 32 bit Wine on a 64
bit system.

Pure 64 bit Wine is not a supported configuration (and is generally
useless, as most Windows apps are still 32 bit). For 64 bit support, you
must build both 64 bit and 32 bit Wine in a [shared
WoW64](Building-Wine#shared-wow64) setup. This does not
require a container or chroot on openSUSE, but the builds must be done
out of tree, and in the order specified below.

**1. Build the 64 bit side**

Create a directory for the 64 bit build and run configure from within
that directory:

```sh
$ cd $HOME
$ mkdir wine64
$ cd wine64
$ CC="ccache gcc" ../wine-git/configure  --enable-win64 --disable-tests
```

Double check the output of configure for any missing 64 bit dependencies
and install any that are needed. If all is well, run

```sh
$ make
```

from within the wine64 directory.

**2. Build the 32 bit side**

Create a directory for the 32 bit build and run configure from within
that directory:

```sh
$ cd ..
$ mkdir wine32
$ cd wine32
$ CC="ccache gcc -m32" PKG_CONFIG_PATH=/usr/lib/pkgconfig ../wine-git/configure  --with-wine64=../wine64 --disable-tests
```

Double check the output of configure for any missing 32 bit dependencies
and install any that are needed. If all is well, run

```sh
$ make
```

from within the wine32 directory.

### From a Source Tarball

Building from a source tarball offers less flexibility than git while
requiring the same amount of work

If you prefer to build from a source tarball rather than git, follow the
instructions above for building from git, but instead of cloning the git
repository, download the tarball for the version you want from
<https://dl.winehq.org/wine/source/> and extract it. Substitute the
source directory for the wine-git directory when following the
instructions.

In versions of Wine prior to 2.3, the tools directory contained a script
called `wineinstall`. Do not use this script, even for building old
versions of Wine. It was not updated for years and cannot build 64 bit
Wine.

## See Also

[Building Wine](Building-Wine)
