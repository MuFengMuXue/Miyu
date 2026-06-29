<small>
&nbsp;[:flag_fr: Français](fr/MacOS)
</small>

-----

## Notice

Only supports macOS Catalina (10.15.4) or later, wine also works on
Apple Silicon systems via Rosetta2.

## Homebrew

To install wine the following command can be used;

`brew install --cask --no-quarantine (selected wine package)`

**wine-stable**, **wine@devel** or **wine@staging** packages can be
installed using the above example. The advantage of installing via
homebrew means wine is available from a standard terminal session The
**--no-quarantine** line is to avoid brew adding the quarantine flag.

## MacPorts

`sudo port install (selected wine package)`

**wine-stable**, **wine-devel** or **wine-staging**

## Building Wine

See [Building Wine on macOS](MacOS-Building)

## Uninstalling source build

- Remove the source tree and binaries. Otherwise and if you used `sudo
  make install`, revert it:

  `sudo make uninstall`

- Then simply delete your local Wine source code directory:

  `rm -rf src/wine`

- Clean-up pseudo C: drive and registry entries as well as all programs
  installed to C:

  `rm -rf $HOME/.wine`

- Check the hidden directory `$HOME/.local/` where Wine stores some
  desktop menu entries and icon files as it interoperates with the
  [X.Org Foundation](https://www.x.org/) and the [Free
  Desktop](https://www.freedesktop.org/wiki/).

  `rm -rf $HOME/.local`

Note: Files in this directory are unused on macOS **unless** you use a
UNIX window manager and other X11 applications instead of the native
MacOS apps.

## Homebrew

`brew uninstall --cask (selected wine package)`

**wine-stable**, **wine@devel** or **wine@staging**

## MacPorts

`sudo port uninstall --follow-dependencies (selected wine package)`

**wine-stable**, **wine-devel** or **wine-staging**

## Installing Deprecated WineHQ packages

Official WineHQ packages of the development and stable branches are
available for macOS 10.8 to 10.14 ***(Wine won't work on macOS Catalina
10.15 as 32-bit x86 support is required)***. Please test these packages
and report any bugs at <https://bugs.winehq.org>.

Note that work is being done to convert core modules of Wine to PE
format which will allow Wine to work on newer versions of macOS in the
future.

**Prerequisites:**

1.  XQuartz \>= 2.7.7
2.  Gatekeeper must not be set to block unsigned packages.

**Installing:**

Both .pkg files and tarball archives are available at
<https://dl.winehq.org/wine-builds/macosx/download.html>.

Installing from a .pkg file is recommended for inexperienced users.

**To install from a .pkg file**, double-click on the package, and the
usual macOS installer wizard should open. The process should be
self-explanatory. It is possible to install the package either for all
users (needs administrator privileges), or just for your current user.
After the installation is finished, you should find an entry "Wine
Staging" or "Wine Devel" in your Launchpad. By clicking on it, a new
Terminal window opens with a short introduction into some important wine
commands. You can now directly start wine/winecfg/... from the Terminal,
as the PATH variable is set correctly. For user convenience, the package
also associates itself with all \*.exe files, which means you can run
windows executables just by double-clicking on them.

**To install from a tarball archive**, simply unpack it into any
directory. There is no need to set DYLD_\* environment variables; all
paths are relative, so it should work as long as the directory structure
is preserved (you can skip the /usr prefix though using
--strip-components 1).

For more information, see
<https://www.winehq.org/pipermail/wine-devel/2015-December/110990.html>
and
<https://www.winehq.org/pipermail/wine-devel/2016-January/111010.html>.

## Third Party Versions

Third party versions of Wine, such as Wineskin, Winebottler, and
PlayOnMac, are not supported by WineHQ. If you are using one of those
products, please retest in plain Wine before filing bugs, submitting
AppDB test reports, or asking for help on the forum or in IRC.

## See Also

- [macOS FAQ](MacOS-FAQ)
- [macOS Building](MacOS-Building)
