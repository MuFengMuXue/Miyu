## Building Wine on macOS

If you just want to install a recent version of Wine, and possibly
report [Bugs](Bugs) or [AppDB](https://gitlab.winehq.org/winehq/appdb/-/wikis/Maintainers)
tests, you should be fine just following the instructions on the main
[macOS](MacOS) page for installing a WineHQ package.

If you're interested in [Submitting
Patches](Submitting-Patches) or [Regression
Testing](Regression-Testing) though, you'll want to build
Wine from the tip of WineHQ's [Git](Git-Wine-Tutorial) repo;
this page explains how to do that on macOS in more detail.

[homebrew](https://brew.sh) and [MacPorts](https://www.macports.org) are
package managers that can make it easier to build Wine on macOS, and
some notes on using them are provided below. Note, however, that they
are not part of the Wine Project; any problems with homebrew or Macports
should be reported to the respective site.

*From macOS Catalina Apple removed 32-bit support, which makes it
impossible to use 32-bit Wine.*

# Preliminaries

In order to build and run Wine, you might need to install some extra
software. Getting it shouldn't be much trouble though.

## Xcode

The [Xcode development suite](https://developer.apple.com/xcode/) is the
primary kit you will need, regardless of whether you decide to do a
minimal build from git, use a build script, or download from one of the
ports projects. A version of it will be included in the *Optional
Installs* folder of your macOS installation DVD. You should also be able
to [download the latest
version](https://developer.apple.com/download/applications/) for your model
from the Apple developer site.

**Note:** If you don't want to install the full suite, you should be
able to make due with just the *Command-Line Tools* component of Xcode.
This will include all of the necessary build tools and even git. Any
other libraries should come pre-installed in macOS or can be pulled in
automatically by other tools.

## XQuartz

In the past, Wine's native Mac driver still needed a good deal of work
so running Wine on macOS required installing an X11 server too. This is
no longer necessary, but there are still some features missing from the
Mac driver (see the to-dos on the [macOS](MacOS) page) so you
still might want to run Wine with the X11 driver.

According to Wikipedia, from v10.3 (Panther) to v10.7 (Lion) of macOS,
Apple at least included a Mac-compatible X11 server as an optional
install. However, since v10.8 (Mountain Lion), Apple has stopped
providing its own release of the X11 server and advises all users to
download the newest version of a compatible X11 server directly from
upstream.

The open-source [XQuartz](https://xquartz.macosforge.org) project
develops the Mac version of X11; you can download the disk-image file
directly from there, then just use the macOS installer.

During setup, the upstream XQuartz disk-image will replace */usr/X11*
(which is in most PATH variables) with a symlink to */opt/X11* (where it
installs the files). However, if you upgrade your release of macOS, this
symlink may get clobbered, leading to fatal errors in X11 programs.
Reinstalling XQuartz will repair the link automatically, or you can
manually restore it with:

`sudo ln -s /opt/X11 /usr/X11`

If you have a supplementary package manager, you might also be able to
grab XQuartz (or an equivalent port of the vanilla xorg server):

- [On
  homebrew](https://github.com/Homebrew/homebrew-x11/blob/master/README.md),
  you can grab XQuartz from the related Caskroom repo:

  `brew install --cask xquartz`

- [On MacPorts](https://www.macports.org/install.php), you can get fresh
  ports of either the *xorg-server* (stable X11 server),
  *xorg-server-devel* (development X11 server), or *xorg* (full X11
  system) packages. For example:

  `sudo port -v install xorg-server`

# Dependencies

Once you have Xcode and a version of the X11 server (not required but
highly recommended), you need to grab both the build and runtime
dependencies for Wine. While you can just run Wine's configure script
and keep installing libraries that it complains are missing, using a
package manager will save you a lot of trouble and keep your system
cleaner.

The main caveat with the various macOS package repos is that you do
**not** want to mix them. Once you've decided to use one, stick with it,
and if you decide to switch to a different one, it's probably best to
uninstall all of your old packages first, then reinstall them with the
new system.

The subsections below describe ways you can get just the necessary
dependencies for Wine. If you want, you can always just install the
appropriate wine package, which will pull in all the other packages you
need. At that point, you can either uninstall just the wine package, or
keep it and run your own build from within its directory.

## homebrew

homebrew no longer provide a **wine** formula instead opting to use
their cask system to install Winehq provided packages.

Build dependencies;

`brew install --formula bison mingw-w64 pkgconfig`

Runtime dependencies;

`brew install --formula freetype gnutls molten-vk sdl2`

**Please note** Homebrew doesn’t add bison to \$PATH so this needs to be
handled manually.

## MacPorts

The current wine packages available from Macports are obsolete so can’t
be used as a reference for needed build/runtime dependencies. Here’s an
updated list for wine-8.x

**Built-time dependency list:**

```
sudo port install bison \
                  mingw-w64 \
                  pkgconfig
```

**Runtime dependency list:**

```
sudo port install freetype \
                  gnutls \
                  moltenvk \
                  libsdl2
```

**Please Note:**
For macOS Mojave and below use the following options +universal -x11
macOS Mojave you need to do some workarounds to enable 32Bit builds see
<https://trac.macports.org/ticket/56991#comment:70>

# Building from Source

Now with the dependencies installed, you will use almost the same
procedure as described on the [Building Wine](Building-Wine)
page. You should be able to run *./configure* and make with the same
parameters as on another system.

**Note:** Almost all libraries are correctly detected and configured by
pkgconfig.

You can configure your build directory to compile with clang like so:

```
./configure CC="clang" CXX="clang++"
```

**Note:** The minimum SDK to compile wine is MacOSX10.10.SDK (14D125).
The final SDK to support 32Bit is MacOSX10.13.SDK later SDKs support
64Bit and arm64 (MacOSX11.1.SDK and later for arm64)

**Please Note:** Wine uses standard dlopen() to find libraries meaning
wine will only check standard location /usr/local/lib & /usr/lib so wine
will have trouble finding the needed libraries when using macports and
XQuartz. To avoid this let’s use rpath.

```
LDFLAGS="-Wl,-rpath,/opt/X11/lib"
```

**Note:** The provided example when set during configure will ensure
wine checks /opt/X11/lib for any needed libraries before the standard
locations.

# Running a Custom Build

When installing Wine from source on macOS, you may need to make some
quick configuration changes.

After compiling Wine from source, you can install it into */usr/local*
with *make install*, but it's **highly recommended** that you run it
from the build directory.

Depending on how you installed XQuartz, you might see fatal errors in
X11 when you try to run your own build of wine from the command-line.
This is due to XQuartz installing into the */opt/X11/* directory and
creating symlinks to */usr/X11/*, neither of which is typically checked
by the macOS dynamic linker. There are a couple of workarounds for this:

- The first is to add the *usr/X11/lib* directory to the
  DYLD_FALLBACK_LIBRARY_PATH environment variable. You can do this when
  invoking wine like so:

  ```
  DYLD_FALLBACK_LIBRARY_PATH="${DYLD_FALLBACK_LIBRARY_PATH}:/usr/lib:/usr/X11/lib" wine program_name.exe
  ```

- The other method is to create symlinks to the libraries in
  *usr/X11/lib/* from inside */usr/local/lib*:

  ```
  cd /usr/local/lib
  sudo ln -s /usr/X11/lib/*
  ```

However, this second approach is more tedious to undo and may be more
fragile in some situations.

You might need to tweak the actual directories in your list, but you can
avoid the tedium of typing the list every time by setting it in one of
your shell config files (e.g. *.profile*, *.bash_profile*, or
*.bashrc*):

```
export DYLD_FALLBACK_LIBRARY_PATH="${DYLD_FALLBACK_LIBRARY_PATH}:/usr/lib:/usr/X11/lib"
```

Joerg Hoehle proposed [patching the
winewrapper](https://www.winehq.org/pipermail/wine-patches/2009-July/075290.html)
to adjust DYLD_FALLBACK_LIBRARY_PATH every time wine is invoked. For
some reason, the patch was rejected (perhaps changing PATH variables or
symlinking should be done upstream by XQuartz?)

# See Also

- [Building Wine](Building-Wine)
- [Compatibility](Compatibility)
- [Packaging](Packaging)
