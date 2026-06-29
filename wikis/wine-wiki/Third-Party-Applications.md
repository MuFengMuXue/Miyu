Over time, there have been a variety of **Third Party Applications**
that have attempted to make Wine more useful or easier to use. **It is
important to understand that although these third party applications may
make Wine more usable, they are *not* supported by the Wine project.**
If you have questions regarding the use of a third party application,
please use the support mediums provided by that third party rather than
Wine HQ.

## Why Third Party Applications Exist

Users want to run applications and sometimes a change to Wine can cause
an application to work, but this change cannot be incorporated into Wine
for some reason. For example, the change may break Wine for other
applications and/or platforms. As such changes to Wine must meet some
level of QA. If the change is a dirty hack to Wine's source code that
allows an application to run, then the change may end up within Wine's
source code only after it has been properly fixed.

In theory, any third party application here is essentially a temporary
workaround until underlying bugs in Wine can be fixed properly. As Wine
improves, parts or all of these third party applications may become
obsolete or incompatible with Wine (at least until the third party
provides a suitable update).

## Current Third Party Applications

The applications below should work with the latest Wine and are still
being maintained.

- **[Crossover](https://www.codeweavers.com)**

  The Crossover series of products are a repackaging with added patches to
  support more applications and added interfaces on top of WineHQ.

- **[DOSBox](https://www.dosbox.com/wiki/)**

  DOSBox is an emulator for legacy x86 PCs, which is particularly useful
  for old MS-DOS programs since they often used hardware in rigid ways
  (e.g. using CPU clock cycles directly for timing). Wine uses DOSBox for
  its virtual 8086 mode (for more details, see Wine Wiki's
  [DOSBox](DOSBox) page).

- **[exe-thumbnailer](https://github.com/exe-thumbnailer/exe-thumbnailer)**

  This module allows UNIX windows managers to generate crisp desktop icons
  from the icons embedded in Windows executables.

- **[Glintwine](https://bitbucket.org/andycellar/glintwine/src)**

  A Python-based GUI tool that provides managing of registry keys for
  Wine.

- **[Lutris](https://lutris.net/)**

  Lutris is an open gaming platform for Linux. It helps you install and
  manage your games in a unified interface. This support includes managing
  Windows games (run via Wine).

- **[PlayOnLinux](https://www.playonlinux.com)**

  A tool which is aiming on making it easy for the user to install Windows
  software, like World of Warcraft, Adobe Photoshop, Guild Wars and much
  more.

- **[PlayOnMac](https://www.playonmac.com)**

  A tool made by the same team as PlayOnLinux but for Mac user.

- **[PortingKit (for Mac OS X)](https://portingkit.com)**

  Using Wineskin technology, Porting Kit can install games and apps
  compiled for Microsoft Windows® in macOS. It's free, it's simple, it's
  the Porting Kit.

- **[Q4Wine](https://q4wine.brezblock.org.ua/)**

  A Qt GUI for Wine. It will help you manage wine prefixes and installed
  applications.

- **[Unofficial Wineskin (for Mac OS
  X)](https://github.com/Gcenx/WineskinServer)**

  Create wrappers used to make ports that work like Native macOS
  applications. Uses WineHQ portable releases, bundles all needed dylibs
  and binarys for use with winetricks, always downloads the current
  version of winetricks.

- **[WineD3D for Windows](https://fdossena.com/?p=wined3d/index.frag)**

  A DirectX 1-11 to OpenGL wrapper based on WineD3D.

- **[WineGUI](https://winegui.melroy.org)**

  User-friendly graphical interface for Wine. (See also the
  [WineGUI](WineGUI) wiki page)

- **[Winetricks](https://winetricks.org)**

  A tool for installing games, applications, and various redistributable
  runtimes, e.g. mono, dcom98, fonts. Workarounds to Wine bugs are run
  automatically. (See also the [Winetricks](Winetricks) page on
  this wiki).

------------------------------------------------------------------------

## Obsolete Third Party Applications

These applications are no longer useful, unmaintained, and do not work
with current Wine releases. **You should not use these.**

- **osxwinebuilder (for Mac OS X)**

  A command line script to compile and install Wine and a number of
  prerequisite packages from source on Mac OS X.

- **[WineBottler (for Mac OS X)](https://winebottler.kronenberg.org/)**

  A tool to install and run pre- or custom configured apps. It comes with
  precompiled wine and allows to create fully self-contained .app bundles.

- **[Wineskin (for Mac OS
  X)](https://wineskin.urgesoftware.com/tiki-index.php)**

  Make wrappers or ports of Windows software to Macs. Wine and custom
  Xquartz X11 all built in. Pre-built packages, or you can custom compile
  your own Wine source to use too. Finished products look and work like
  native Mac apps. File associations, fullscreen, multi-monitors,
  resolution switching... great for games. LGPL licensed open source.

- **[Wine bottle management (for
  Linux)](https://wibom.sourceforge.net/)**

  GUI bottle manager to import, create and clone bottles. Edit registers
  of the bottles. Set colors according to your GTK theme.

- **[WineD3D installer for native
  Windows](https://www.nongnu.org/wined3d/)**

  provide an OpenGL-based free replacement for Microsoft Direct3D (useful
  for things like [VirtualBox](https://www.virtualbox.org/))

- **[Swine](https://www.swine-tool.de)**

  A graphical frontend for Wine that offers prefix management, winetricks
  integration and access to most of the Wine command-line utilities in one
  GUI.

- **WineXS**

  A GUI for Wine.

- **Pipelight**

  A tool to use windows only plugins inside Linux browsers.

- **Bordeaux**

  A tool for installing a lot of Windows applications on Linux,
  Free***'BSD, PC-BSD, Open***'Solaris & Mac like Microsoft Office,
  Microsoft Project, Adobe Photoshop, and more.

- **[Winetools](https://www.von-thadden.de/Joachim/WineTools/)**

  A menu driven installer for around 90 windows applications. No longer
  being maintained.

- **WineDoors**

  A tool to install and configure Wine, as well as many Windows programs.

- **Winesetuptk**

  A Wine setup tool formerly provided by CodeWeavers, Inc. Wine can
  now setup its own environment automatically, and
  [Winecfg](Commands/winecfg) has now replaced the other limited
  configuration that winesetuptk allowed.

- **[XWine](https://freshmeat.net/projects/xwine/)**

  A graphical user interface for the Wine emulator. It provided an
  interface for configuring and running MS-Windows applications. It is no
  longer useful now.

- **WineBot**

  A tool to automate Windows program installation under Wine

- **[wine-launcher](https://code.launchpad.net/~ubuntu-wine/+junk/wine-helper)**

  A python-based, command-line replacement for
  [Winecfg](Commands/winecfg). Has not been updated since 2009.

- **wisotool**

  A tool for automated installs of various Windows programs (downloadable
  demos and from disk images), including workarounds. It was merged into
  winetricks.

- **[Zero Wine](https://sourceforge.net/projects/zerowine/)**

  A malware-analyzer that sandboxes Wine on Debian in a QEMU image
  (remember **Wine provides no sandboxing**). Windows executables are then
  loaded into the sandbox, and Wine's function-tracing system is used to
  detect suspicious behavior.
