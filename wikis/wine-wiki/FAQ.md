<small>
&nbsp;[:flag_fr: Français](fr/FAQ)
&nbsp;[:flag_nl: Nederlands](nl/FAQ)
&nbsp;[:flag_kr: 한국어](ko/FAQ)
</small>

-----

This FAQ, or **F**requently **A**sked **Q**uestions, covers general
topics about Wine. For questions related to Wine software development,
see the [Developer FAQ](Developer-FAQ).

Quick links:
- [Running a program in
Wine](#how-do-i-run-an-application-once-ive-installed-it)
- [Running Wine from a
terminal](#how-should-i-start-windows-programs-from-the-command-line)
- [Running program as root](#should-i-run-wine-as-root)
- [Uninstalling an application](#uninstalling)
- [Getting a debugging
log](#how-can-i-get-a-debugging-log-aka-terminal-output)
- [Using a
wineprefix](#can-i-store-the-virtual-windows-installation-somewhere-other-than-wine)
- [Creating a 32 bit
wineprefix](#how-do-i-create-a-32-bit-wineprefix-on-a-64-bit-system)
- [Solving dependency errors](#how-do-i-solve-dependency-errors-when-trying-to-install-wine)

## General questions

### Who is responsible for Wine?

Wine is available thanks to the work of many people around the world.
Some companies that are or have been involved with Wine development are
[CodeWeavers](https://www.codeweavers.com),
[Bordeaux](https://bordeauxgroup.com/), TransGaming, Corel, Macadamian
and Google. See [Acknowledgements](Acknowledgements) and
[Wine History](Wine-History).

### Does Wine hurt Linux or other free operating systems?

Wine increases the usefulness of Linux, makes it easier for users to
switch to free operating systems, and for Windows developers to make
applications that work on them. This greatly raises Linux marketshare,
drawing more commercial and community developers to Linux.

### Is Wine an emulator? There seems to be disagreement

There is a lot of confusion about this, particularly caused by people
getting Wine's name wrong and calling it WINdows Emulator.

When users think of an emulator, they tend to think of things like game
console emulators or virtualization software. However, Wine is a
[compatibility
layer](https://en.wikipedia.org/wiki/Compatibility_layer) - it runs
Windows applications in much the same way Windows does. There is no
inherent loss of speed due to "emulation" when using Wine, nor is there
a need to open Wine before running your application.

That said, Wine can be thought of as a Windows emulator in much the same
way that Windows Vista can be thought of as a Windows XP emulator: both
allow you to run the same applications by translating system calls in
much the same way. Setting Wine to mimic Windows XP is not much
different from setting Vista to launch an application in XP
compatibility mode.

A few things make Wine more than just an emulator:

- Sections of Wine can be used on Windows. Some virtual machines use
  Wine's OpenGL-based implementation of Direct3D on Windows rather than
  truly emulate 3D hardware.
- Winelib can be used for porting Windows application source code to
  other operating systems that Wine supports to run on any processor,
  even processors that Windows itself does not support.

"Wine is not just an emulator" is more accurate. Thinking of Wine as
just an emulator is really forgetting about the other things it is.
Wine's "emulator" is really just a binary loader that allows Windows
applications to interface with the Wine API replacement.

Note: The story is a bit different when Wine is being used to run
applications built for a different CPU architecture, thereby requiring
CPU emulation. See [Emulation](Emulation) for more on this.

### What is the difference between Wine, CrossOver, Proton, and Cedega?

Wine is the base of the project, where most of the work is being done.
Wine is not perfect, but [tens of
thousands](Usage-Statistics) of people nevertheless use
"vanilla" Wine successfully to run a large number of Windows programs.

CrossOver is a product made by a company called CodeWeavers that is
based directly on Wine with a few tweaks and proprietary add-ons. Unlike
the biweekly Wine releases, CrossOver releases are rigorously tested for
compatibility with CodeWeavers' supported applications in order to
prevent "regressions". CodeWeavers employs a large proportion of the
Wine developers and provides a great deal of leadership for the project.
All improvements to Wine eventually work their way into CrossOver.

Proton is a compatibility tool comprised of various software, developed
by Valve for use with their proprietary Steam client. It is a bundle
consisting of a fork of Wine, DXVK - a translation layer for converting
Direct3D 9/10/11 API calls to Vulkan, VKD3D-Proton - Valve's fork of
VKD3D for translating Direct3D 12 to Vulkan, FAudio, and a wide range of
experimental patches to increase performance and/or compatibility for
video games. It is only intended for use within the proprietary Steam
client, though nearly all of its components are open source, and it is
capable of running non-Steam software. The Steam client also provides
drop-in support for other user-created compatibility layers, such as
forks of Proton. All improvements to Wine will eventually work their way
into Proton, just like CrossOver.

Cedega (formerly WineX) was a product from a company called TransGaming.
TransGaming based their product on Wine back in 2002 when Wine had a
different license, closed their source code, and rebranded their version
as specialized for gamers. In the years since Cedega was originally
created from Wine, development on Wine and Cedega continued mostly
independently, until the discontinuation of Cedega in 2011. TransGaming
gave back very little code to Wine. Wine has had years of development
since Cedega was discontinued, and has surpassed Cedega in
compatibility. Notably, for a long time Cedega still had more advanced
copy protection support due to TransGaming's licensing of (closed
source) code from a handful of copy protection companies. Unlike
CrossOver and Proton, most improvements to Wine *didn't* get into Cedega
due to the license differences between Cedega and Wine. Cedega has been
unsupported for many years, and its usage should be avoided.

For more information, see [Wine History](Wine-History).

### How does the Wine version numbering system work?

See the explanation in the [Wine User's Guide](Wine-User's-Guide#wine-from-winehq).

### Do I have to use the command line?

Normally you do not have to use the command line to use Wine in Linux.
You can use a graphical interface for most things, much like on Windows.
In many cases you can right-click an installer and select "Open with
Wine", or just double-click it. You can start installed programs using
the shortcut icon or menu.

However, there are several situations when you might need to use the
command line. The most common reason is to get debug output when your
program does not run properly. You might also want to use utilities such
as `regedit` that do not have menu shortcuts (note that you can create
them using whatever tools your DE provides).

This does not hold true for Mac OS X Wine usage, which is all command
line currently, unless you use a [third party
application](Third-Party-Applications).

### What applications run well with Wine?

Thousands of applications work well. As a general rule, simpler or older
applications tend to work well, and the latest versions of complex
applications or games tend to not work well yet. See [the Wine
Application Database](https://appdb.winehq.org) for details on individual
applications. If your application is rated Silver, Gold or Platinum,
you're probably okay; if it's rated Bronze or Garbage, Wine isn't really
ready to run it for most users. If there aren't any reports using a
recent version of Wine, however, your best bet is to simply try and see.
If it doesn't work, it probably isn't your fault, Wine is not yet
complete. Ask for help on the forum if you get stuck.

### How can I help contribute to the Wine project, and in what ways?

You can contribute programming or documentation skills, or monetary or
equipment donations, to aid the Wine developers in reaching their goals.

One area where every Wine user can contribute to this project is by
sending high quality bug reports to our
[Bugzilla](https://bugs.winehq.org/) and helping the developers with any
followup questions that they may have about your bug. It is impossible
and impractical for a developer to have a copy of every program on the
market, so we need your help even after your initial bug report. If a
developer has a good idea what might be causing the bug, he or she may
ask if you can try a patch and see if it fixes the problem. If the patch
works and then makes its way into our main development tree, the bug
report will be closed, your help will be appreciated by everyone and
your problem will be fixed.

For a list of ideas of how you can help, please consult the
[Contribute](home#contribute) section of the main page.

### I think I've found a bug. How do I report this to WineHQ?

Bug reports should be submitted to our online [Bugzilla
system](https://bugs.winehq.org/). To increase developer productivity and
facilitate a resolution to submitted bugs, **please read the Wiki
article on [Bugs](Bugs)**. A poor bug report may be marked
INVALID and closed, leaving you no closer to resolving your problem.
High quality bug reports are an essential part of making Wine better.

Please note that you should *generally* avoid submitting bug reports if
you have used any [third party
applications](Third-Party-Applications) or native DLL
overrides.

### Where can I get further help?

In addition to this [wiki](home), check the [Wine HQ
Documentation](Documentation) and the [users
forum](https://forums.winehq.org/). If you're an ISV looking at porting
an application with Winelib you can also try
[wine-devel](Forums).

For help with a specific application, search the [Application
Database](https://appdb.winehq.org), a place where users share their
experiences by submitting test data, tips and tricks, and asking
questions.

The IRC channel: [\#WineHQ](irc://irc.libera.chat:6697/#winehq) on
irc.libera.chat. Wine users hang out there, and often developers will
lurk there too. See [IRC](IRC) for more important information.

## Installing Wine

### What are the system requirements for Wine?

Wine, along with the operating system you use to run it, generally
requires less disk space and memory than Windows itself. If you're not
currently running a Windows application, Wine won't consume any
resources at all other than about 1.4 Gigabytes of disk space.

Ideally, if an application runs fine in Windows, it should run fine on
the same hardware using Wine, *provided native drivers for your hardware
are installed and equivalent to the Windows drivers*. Open source Linux
graphics drivers in particular are often inadequate to run games that
work fine on the same hardware in Windows. If there is no native driver
for your hardware, Wine will not be able to use it.

#### Does Wine run on all Unix filesystems?

Mostly. Wine is written to be filesystem independent so MS Windows
applications should work on virtually any full-featured UNIX filesystem.
The key exception is that not all filesystems / drivers support every
feature of fat32 or NTFS. One example is that the ntfsv3 drivers do not
support shared-write mmap, a feature that cannot be emulated and is used
by applications such as Steam.

One other point is that Wine is a weird application in ways and some
programs work *better* on case-insensitive filesystems.

#### Will Wine run only under X?

Until recently with projects such as Wayland, serious alternatives to
x11drv weren't even on the horizon so development has focused on X.
However, Wine's interface with the graphics driver is designed to be
abstract so supporting future graphics systems will hopefully be
straight-forward.

### Which version of Wine should I use?

**Short answer:** Use the version that works best with the particular
applications you want to run. In most cases, this will be the latest
development version; however, in some cases it may take some
experimenting to find it.

**Longer answer:** Wine development is rapid, with new releases in the
development branch every two weeks or so. Functionality will usually be
best with the most recent development version, however, there are cases
where changes to existing code in Wine cause applications that worked
well in older versions to not work in the new one (these are called
regressions), as well as problems caused by the introduction of new, but
as-yet-incomplete and untested, functions.

A good rule of thumb is to start with the version of Wine installed with
your distro and see if that works with the applications you want to use.
If it does, good! If it doesn't, upgrade. In most cases the upgrade
should be to the latest development version, but it is a good idea to
check Bugzilla and the AppDB for any known regressions and/or new bugs.
If you find an existing bug marked STAGED, this means there is a patch
for the problem in wine-staging (the experimental branch), and you
should try the latest version in that branch. If there are known bugs
without a STAGED patch or easy workaround, upgrade to the most recent
version of Wine known to work for your application.

While Wine does have a "stable" branch, the term "stable" refers to the
branch as a whole, which is infrequently updated, and (for the minor
stable releases) only with bugfixes promised not to break functionality.
Users of a development or staging release can achieve the same degree of
stability by simply not upgrading. Note that user support for the stable
branch is limited to the ability to file AppDB test reports. Users who
ask for help on the forum/IRC or file bug reports for the stable branch
will be asked to retest in the current development release.

The current stable, development, and staging releases are listed on
the [WineHQ home page](https://www.winehq.org). See the [Wine User's
Guide](Wine-User's-Guide#wine-from-winehq) for a description of the
three branches and the version numbering system.

### How do I install Wine?

- Use a precompiled binary package for your operating
  system/distribution (see the [Download](Download) page for
  links and additional information).
- [Compile Wine from source](Building-Wine) - if you can't
  find an up-to-date package for your OS/distribution

### How do I solve dependency errors when trying to install Wine?

If your package manager complains about unmet dependencies when trying
to install Wine, work your way backwards. Try installing whatever
package your package manager complains has unmet dependencies, see what
your it complains about, then try to install that. Keep working your way
backwards until you solve whatever is blocking everything else.

A common problem on Ubuntu-based system is having installed a PPA
version of a library that is newer than what is available in the
standard repository. PPA packages may not be multiarch compatible and/or
may not have i386 packages built, and since *Debian/Ubuntu-based systems
require the i386 and x86_64 versions of a package to be exactly the
same*, the user is unable to install the i386 version needed by Wine
because no matching version can be found. The solution is to either
change the installed version of the library back to the one from the
standard repository so you can install both the 32 and 64 bit packages,
or find an i386 package whose version exactly matches the one already
installed.

### I have a problem installing my distro's Wine package and need help

WineHQ only supports the binary packages that we build ([available
here](Download), only the ones listed under 'WineHQ Binary
Packages'). Consult your distro's support channels for help using your
package manager and interpreting any error messages you may be
receiving if you're having problems with distro packages. If you are
an experienced user and believe there is a problem with the package
itself and/or the repository, please report it to your distro's Wine
package maintainer.

### Can I install more than one Wine version on my system?

Yes, but you will have to build Wine yourself (see [Building
Wine](Building-Wine)), as it is not possible to have multiple
distro packages installed. The easiest way to do this is to run Wine
from the build directory (don't do `make install`). If you want to
actually install multiple versions, use `--prefix` when building Wine to
designate a different install directory for each version, e.g.

```sh
./configure --prefix=_path_to_install_directory_ && make
```

then install it with

```sh
sudo make install
```

On Linux, you may need to set LD_LIBRARY_PATH, like so:

```sh
export LD_LIBRARY_PATH="$PREFIX/lib:$LD_LIBRARY_PATH"
```

Note that regardless of whether you install multiple versions or run
them from the build directory, you will still have to designate which
version of Wine you wish to use when running applications. It is also
recommended that applications being run with different Wine versions be
installed into separate wineprefixes.

### Is there a 64 bit Wine?

Yes. 64 bit Wine has been available on Linux since 1.2. WineHQ binary
packages are available for 64 bit, and most major distros package it for
users. Normally, installation should be as simple as installing the Wine
package for your distribution through your package manager. Check the
[Download](Download) page. If you are building Wine from
source, see [Building Wine](Building-Wine) for instructions
on how to build 32 bit Wine on a 64 bit system and instructions on how
to build 64 bit Wine in a shared WoW64 setup.

A few things to note:

- 32 bit Wine runs on both 32-bit and 64-bit Linux/Unix installations.
  16-bit and 32-bit Windows applications will run on it.
- 64-bit Wine runs only on 64 bit installations, and so far has only
  been extensively tested on Linux. It requires the installation of 32
  bit libraries in order to run 32 bit Windows applications. Both 32-bit
  and 64-bit Windows applications (should) work with it; however, there
  are still [many
  bugs](https://bugs.winehq.org/buglist.cgi?keywords=win64&resolution=---).
- Current Wine includes support for 64 bit Wine on Mac OS X; however,
  this has not been tested very much, and some applications may never
  work due to an [ABI incompatibility between Win64 and OS
  X](https://www.winehq.org/wwn/364#Wine64%20on%20Mac%20OS%20X).

### Where can I find old Wine binary packages?

Old WineHQ binary packages are kept in their respective directories in
the the [WineHQ download server](https://dl.winehq.org/wine-builds).

Consult your distro for information on obtaining old versions of distro
Wine packages.

### How do I install Wine on my netbook (eeePC, Acer Aspire One, etc.)?

If you have replaced the customized distro that came preinstalled on
your netbook (Xandros, Linpus, etc.) with one of the mainstream distros
that provide up-to-date Wine packages, you should be able to install
Wine as normal for that distro.

If you are still using Xandros (eeePC), Linpus ([Acer Aspire
One](https://www.aspireoneuser.com/forum/)) or any other customized
distro, you will have to ask on your netbook's support forum. Only other
users of those distros can advise you on what, if any, binary packages
will work on your system, where to find them, and how to install them.

You can also try building Wine from source following the instructions in
[Building Wine](Building-Wine), but you will still need to
consult your netbook's support forum regarding satisfying dependencies
on your particular system.

### Installing on Apple

#### How do I install Wine on my Mac?

- **[WineHQ Packages](MacOS)** are available for macOS 10.15.4)
  and higher.
- Build and install Wine using [Homebrew](https://brew.sh),
  [MacPorts](https://www.macports.org), or
  [Fink](https://www.finkproject.org) to install Wine. All support the
  current releases of macOS. The [MacPorts](https://www.macports.org)
  installation of Wine will automatically install any necessary
  Dependencies for a Wine installation.
- If this is too complicated, there are several [third party
  apps](Third-Party-Applications) you can use like [Codeweavers'
  CrossOver Mac](https://www.codeweavers.com/crossover).
- **Linux**: If you are running Linux on your Mac, installing Wine is as
  simple as installing it under Linux on a PC. Visit the
  [Download](Download) page for more info.

#### Can I use Wine on an older Mac without an Intel chip?

No, not even in Linux. Older Macs used PowerPC processors are
incompatible with code compiled for x86 (Intel and AMD) processors,
unless the code is run under CPU emulation. Wine Is Not a (CPU)
Emulator, nor does it include one. The Darwine project was an effort to
do just that, but it has not been maintained in many years.

## Compiling Wine

### How do I compile Wine from source?

See [Building Wine](Building-Wine).

### How do I apply a patch?

You have to build Wine from source; see above.

## Uninstalling

### How do I uninstall Wine?

**Uninstalling Wine itself will not revert your Wine settings or
uninstall your Windows apps, which are permanently stored in your user's
home directory**. Do not uninstall Wine if you only wish to remove all
of your settings and apps. For instructions on removing your Wine
settings and apps, see [How do I wipe the virtual Windows
installation?](#how-do-i-wipe-the-virtual-windows-installation)

- If you installed Wine with your distribution's package manager, use it
  again to uninstall Wine.
- If you installed Wine from source, use `sudo make uninstall` in the
  source directory to remove it.

### How do I uninstall individual Windows applications?

You can run Wine's `uninstaller` command; this is like Windows'
"Add/Remove Programs" function. To uninstall 64 bit applications,
including wine-mono, you need to run it with wine64. The uninstaller
should remove menu and desktop entries... but it's not well tested; it
might not work with all apps. See below for a reliable way to remove
**all** Windows apps.

### How do I clean the Open With List?

To clean **Open With List**, please **carefully** paste the following
commands into a terminal:

```sh
rm -f ~/.local/share/mime/packages/x-wine*
rm -f ~/.local/share/applications/wine-extension*
rm -f ~/.local/share/icons/hicolor/*/*/application-x-wine-extension*
rm -f ~/.local/share/mime/application/x-wine-extension*
```

### How do I wipe the virtual Windows installation?

You can remove your virtual Windows installation and start from scratch
by deleting the hidden `.wine` directory in your user's home directory.
This will remove all of your Wine settings and Windows applications. The
simplest and safest way to do this is through your file manager. Simply
set your file manager to show hidden files, browse to your home
directory, and delete `.wine` the same way you would any other
directory. If you want to keep it as a backup, you can rename or move it
instead. To the host system, a wineprefix is just another directory that
can be deleted, moved, renamed, etc., the same as any other directory.

If you prefer to do it from the command line, **carefully** paste the
following commands into a terminal:

```sh
cd
rm -rf .wine
```

To rename it from the command line instead of deleting it:

```sh
mv ~/.wine ~/.wine-old
```

Your Windows applications, though deleted, will remain in your system
menu (remaining desktop files and icons are located in
`~/.local/share`).

To remove these leftover menu entries, **carefully** paste the following
commands into a terminal:

```sh
rm -f ~/.config/menus/applications-merged/wine*
rm -rf ~/.local/share/applications/wine
rm -f ~/.local/share/desktop-directories/wine*
rm -f ~/.local/share/icons/????_*.{xpm,png}
rm -f ~/.local/share/icons/*-x-wine-*.{xpm,png}
```

Alternatively, you can [stop Wine from creating menu entries in the
first
place](#how-can-i-prevent-wine-from-changing-the-filetype-associations-on-my-system-or-adding-unwanted-menu-entriesdesktop-links).

## Installing and Running Windows Applications

### I have lots of applications already installed in Windows. How do I run them in Wine?

Short answer: you have to [install them in
Wine](Wine-User's-Guide#how-to-install-and-run-windows-programs) just
like you did in Windows. Applications usually have a setup or
installer program.

Long answer: some applications can be copied from Windows to Wine and
still work, but don't try this unless you like tinkering under the hood
of your car while it's running.

**Wine is not designed to interact with an existing Windows
installation. If you have any data you need from a Windows installation,
browse your Windows filesystems in your normal file manager and copy the
data to another location.**

Do not try to configure Wine to point to your actual Windows `C:\`
drive. **This will break Windows and require a Windows reinstall.** We
have tried to make this hard to do, so you probably cannot do it by
accident. If you do manage this, Wine may or may not continue to
operate, but your Windows install will be 100% dead due to critical
parts of it being overwritten. The only way to fix Windows after this
has happened is to reinstall it.

### How do I run an installer using Wine?

See the [Wine User's Guide chapter on how to install and run Windows
programs](Wine-User's-Guide#how-to-install-and-run-windows-programs).

### How do I run an application once I've installed it?

See the [Wine User's Guide chapter on how to install and run Windows
programs](Wine-User's-Guide#how-to-install-and-run-windows-programs).

### How should I start Windows programs from the command line?

See the [Wine User's Guide chapter on how to run Windows programs from the command
line](Wine-User's-Guide#how-to-run-windows-programs-from-the-command-line).

### How do I pass command line arguments to a program?

See the [Wine User's Guide chapter on passing Windows command-line
arguments](Wine-User's-Guide#passing-windows-command-line-arguments)

### How do I install/run a `.msi` file?

See the [Wine User's Guide chapter on running .msi
files](Wine-User's-Guide#running-msi-files).

### How do I install/run a ClickOnce (`.application`) file?

Use winetricks to install whatever version of .NET the program requires,
cd to the directory containing the .application file, and run it with

```sh
wine start whatever.application
```

### How do I launch native applications from a Windows application?

First, run `regedit` and add a dot character to the end of the list of
extensions in
`HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment\PATHEXT`.

Note that this change will have to be made every time you upgrade Wine,
as it will be reverted whenever the wineprefix is updated.

You can then start native applications using **wine cmd** if you specify
the full path or use the shell, e.g.:

```sh
wine cmd /c /usr/bin/glxgears
```

or

```sh
wine cmd /c /bin/sh -c glxgears
```

You might also need `winepath` to translate the filename from Windows
format to Linux format (see [How do I associate a native program with a
file type in
Wine?](#how-do-i-associate-a-native-program-with-a-file-type-in-wine)).

### My installer tells me I don't have enough free disk space

Usually, you really don't have enough free disk space. Wine's C: drive
is located in your home directory. Whatever partition contains `/home`
must have enough free space for your program. You can check by running:

```sh
df -h ~
```

If the amount of space you need is less than 1 GB, and `df` reports you
have more than 1 GB available, try setting the Windows version to
Windows 98. This will work around bugs in some old (Windows 98 era)
installers that could not cope with large drives.

If you want to use a different partition that has more free space, use a
wineprefix that is located on the other partition. Note that your other
partition must be a Unix filesystem: FAT and NTFS partitions will not
work. See [How can I run two programs as if they were on different
computers?](#how-can-i-run-two-programs-as-if-they-were-on-different-computers)
for instructions.

### When I double-click on a `.exe` file in my file manager, nothing happens

Note: if you can, start applications by clicking on the application's
icon in the Applications / Wine menu or desktop instead. Double-clicking
`.exe` files is typically only needed for applications that aren't
installed yet, e.g. to run the `setup.exe` on a CD-ROM game or a
downloaded installer.

If double-clicking doesn't work, you might need to right-click the file
and choose "Run with Wine". It depends on your file manager. If that
also doesn't work, contact whoever built your Wine packages and let them
know there's a problem.

You can work around this by using the command line instead of your
file manager (see the [Wine User's Guide chapter on how to run Windows
programs from the command
line](Wine-User's-Guide#how-to-run-windows-programs-from-the-command-line)).

### I double-clicked on an .exe file, but the system said "The file foo.exe is not marked as executable..."

If the dialog says "Read about the executable bit", with a hyperlink,
try clicking on the hyperlink and reading about the executable bit.

If the file is on your hard drive, right-click it, choose Properties /
Permissions, and check "Allow executing file as program".

If the file is on a CD-ROM, you can run it from the command line as
described above. Or, if you know how to use `mount`, remount the cd-rom
to mark all files as executable with a command like
`mount -o remount,mode=0777,exec /media/cdrom` but using the real mount
point if it's different from `/media/cdrom`.

## Using Wine

### How do I run Wine?

Wine is not an application you run. Wine enables your computer to run
Windows applications. Simply install and run your applications as you
would in Windows. See [How do I run an installer using
Wine?](#how-do-i-run-an-installer-using-wine).

### Should I run Wine as root?

:warning: ***NEVER run Wine as root!*** Doing so
gives Windows programs (and viruses) full access to your computer and
every piece of media attached to it. Running with sudo also has these
same risks but with the added bonus of breaking the permissions on your
`~/.wine` folder in the process. If you have run Wine with sudo you need
to fix the permission errors as described in the next question, and then
run `winecfg` to set Wine up again. You should always run Wine as the
normal user you use to login.

As of Wine 9.4, Wine programs run as a limited user by default, but will automatically and silently elevate themselves if necessary (in the same situations that Windows would spawn a UAC prompt), at which point they will report administrator privileges while still running as the same Unix user.

This is fine for the vast majority of applications, but you may need to manually "run as administrator", by launching the Wine file explorer (explorer.exe), navigating to the program, right-clicking, and selecting "Run as Administrator". This will cause Wine to report administrator privileges but, again, will not affect permissions on the Unix side.

If an application still reports that it lacks access or needs administrator, file a bug report. Running Wine as root will never help in these cases; rather, it is always because of a bug in Wine.

For Linux systems, all ideas that Wine needs root can be solved through
[Posix Capabilities](https://www.linuxjournal.com/article/5737) or [Posix
File
Capabilities](https://www.ibm.com/developerworks/linux/library/l-posixcap/index.html)
or correcting other security settings.

### I ran wine with sudo or as root. How do I fix my permission errors?

You need to fix the permissions on your `~/.wine` directory, this is
where all Wine state, configuration and any important data you might
have such as installed programs, saved data within Wine programs, etc.
are stored. Once you delete or fix the permissions on this directory,
rerun Wine as a regular user always! Run the following to fix the
permissions on your `~/.wine` directory if it now has root permissions.

```sh
cd $HOME
sudo chown -R $USER:$USER .wine
```

### How do I know what version of Wine I have?

Open up a terminal and run `wine --version`. It will say something like
"wine-1.9.2"; if you are using [Git](Git-Wine-Tutorial) then
you will have a version along the lines of "wine-1.9.2-231-gb922b55".

**TIP:** You can find out what the latest release of Wine is from
[WineHQ's main page](https://www.winehq.org). Currently, Wine development
releases come out every two weeks. Your operating system may ship with
an out of date (obsolete) version of Wine. Depending on what OS you use,
you may be able to add an update source to your package management
system to keep up to date. Check the [Download](Download)
page for details.

### Wineprefixes

#### Where is my C: drive?

Wine uses a virtual C: drive instead of your real C: drive. The
directory in which this is located is called a 'wineprefix.'

By default, it's in your home directory's `.wine/drive_c` subdirectory.
(On macOS, see the [macOS FAQ](MacOS-FAQ) for how to find
this.)

See also the [`WINEPREFIX`](Wine-User's-Guide#wineprefix)
environment variable; if this is set, wine uses it to find the
wineprefix.

#### Can I store the virtual Windows installation somewhere other than ~/.wine?

Yes: `~/.wine` is just the default wineprefix (a.k.a. "configuration
directory" or "bottle").

You can change which prefix Wine uses by changing the `WINEPREFIX`
environment variable (outside Wine). To do this, run something like the
following in a terminal:

```sh
export WINEPREFIX=~/.wine-new
wine winecfg
```

Wine will then create a new prefix in `~/.wine-new`.

To use the default prefix, use the command `unset WINEPREFIX` . Or just
set `WINEPREFIX` to `~/.wine`.

Alternatively, you can specify the wine prefix in each command, e.g.

```sh
WINEPREFIX=path_to_wineprefix wine winecfg
```

You can rename, move, copy and delete prefixes without affecting others,
and each prefix has its own `wineserver` instance.

Wherever you see `~/.wine` or `$HOME/.wine` in this Wiki, you can
usually replace it with `$WINEPREFIX`.

#### How do I create a 32 bit wineprefix on a 64 bit system?

At present there are some significant
[bugs](https://bugs.winehq.org/buglist.cgi?keywords=win64&resolution=---)
that prevent many 32 bit applications from working in a 64 bit
wineprefix. To work around this, you can create a new 32 bit wineprefix
using the `WINEARCH` environment variable. In a terminal, type:

```sh
WINEARCH=win32 WINEPREFIX=path_to_wineprefix winecfg
```

(use the actual path to the wineprefix) Do **not** use an existing
directory for the new wineprefix: Wine cannot convert existing one and
must create a new one.

Once a 32 bit wineprefix is created, you no longer have to specify
`WINEARCH` in the command line to use it, as the architecture of an
existing wineprefix cannot be changed. Note that if the wineprefix is
not the default (`~/.wine`, you **do** have to specify the `WINEPREFIX`
variable when installing anything (including winetricks) to it:

```sh
WINEPREFIX=path_to_wineprefix wine start /unix path_to_installer
```

#### Why aren't versions of Windows prior to XP available in 64 bit wineprefixes?

Short answer: because there were no 64 bit versions of Windows prior to
XP.

If you are on a 64 bit system, you will have to [create a 32 bit
wineprefix](FAQ#how-do-i-create-a-32-bit-wineprefix-on-a-64-bit-system)
to be able to select a version of Windows older than XP in winecfg.

Starting with Wine 9.0-rc3, it is possible to select any Windows
version. No matter if the prefix is 32 or 64 bit.

#### How can I run two programs as if they were on different computers?

Example: You have server and client programs. One won't run in the
presence of the other.

Using different wineprefixes will help you here, since they simulate two
Windows computers, in essence.

Run the first program as normal:

```sh
wine first-program.exe
```

The second needs to be run in a different prefix, so we need to change
the `WINEPREFIX` environment variable:

```sh
WINEPREFIX="$HOME/.wine-second" wine second-program.exe
```

The *first-program.exe* and *second-program.exe* can be two copies of
the same program.

### Configuring

#### How do I get Wine to launch an application in a virtual desktop?

You can do this with [winecfg](Commands/winecfg). Add the application
in the Applications tab and then, in the Graphics tab, enable "Emulate a
virtual desktop".

You can also use the following command:

```sh
wine explorer /desktop=name,1024x768 program.exe
```

Replace *program.exe* with the name of your program, and change the
resolution to the size of the virtual desktop you want. Changing *name*
allows you to open several desktops simultaneously.

#### How do I edit the Wine registry?

The Wine registry is stored in the `.reg` files in `~/.wine`, however
you should not edit these files by hand due to the encoding that they
use. Always use the `regedit` program that comes with Wine. This can be
run by typing `wine regedit` in the terminal. Wine's regedit is
virtually identical to the Windows version of regedit and also supports
importing and exporting of registry files. NEVER try and import your
entire Windows registry, this will just break Wine.

See also: [Useful Registry Keys](Useful-Registry-Keys)

#### How do I associate a native program with a file type in Wine?

There are two ways using which you can associate a native program with a
file type. The first method is to use `winebrowser` and an alternative
would be to write a shell script.

The example below uses `winebrowser` to launch the default PDF handler
on your system (on a Unix desktop it uses `xdg-open`). Save the lines
below to a file `pdf.reg`.

```
[HKEY_CLASSES_ROOT\.pdf]
@="PDFfile"
"Content Type"="application/pdf"
[HKEY_CLASSES_ROOT\PDFfile\Shell\Open\command]
@="winebrowser \"%1\""
```

Import the `.reg` file into the registry using the command

```sh
regedit $HOME/pdf.reg
```

Another option is to use a shell script to call a native application.
Save it as `run_linux_program` under `$HOME/bin`:

```sh
#!/bin/sh $1
wine winepath -u "$2"
```

Don't forget to run `chmod a+x $HOME/bin/run_linux_program` to make it
executable. Also make sure that `$HOME/bin` directory is in your
`$PATH`. Otherwise it will not work.

To associate (say) .pdf files with the `acroread` Linux program save the
following as `$HOME/pdf.reg` and then import it with the command
`regedit $HOME/pdf.reg`:

```
[HKEY_CLASSES_ROOT\.pdf]
@="PDFfile"
"Content Type"="application/pdf"
[HKEY_CLASSES_ROOT\PDFfile\Shell\Open\command]
@="/bin/sh run_linux_program acroread \"%1\""
```

You can reuse this script and just edit the registry file. For example
to associate .doc documents with OpenOffice (`ooffice`):

```
[HKEY_CLASSES_ROOT\.doc]
@="DOCfile"
"Content Type"="application/msword"
[HKEY_CLASSES_ROOT\DOCfile\Shell\Open\command]
@="/bin/sh run_linux_program ooffice \"%1\""
```

#### How can I prevent Wine from changing the filetype associations on my system or adding unwanted menu entries/desktop links?

Beginning with wine-3.14, winecfg has a "Manage File Associations"
checkbox on the Desktop Integration tab. Checking it enables
winemenbuilder to create file associations and unchecking it disables
that behavior.

Users of older Wine versions and those who also want to disable the
creation of menu items can accomplish this by disabling
`winemenubuilder.exe` . There are several ways to do this:

- *In winecfg:* before running the installer, run `winecfg`. Go to the
  Libraries tab and type `winemenubuilder.exe` into the "New overrides"
  box (it is not in the dropdown list). Click add, then select it from
  the "Existing overrides" box. Click "Edit" and select "Disable" from
  the list, then click "OK".
- *Registry file:* If you need to apply the setting many times (e.g.
  every time you recreate the Wine prefix), this approach may be more
  convenient. Create a text file named with extension .reg (e.g.,
  `disable-winemenubuilder.reg`) containing the following:

  ```
  [HKEY_CURRENT_USER\Software\Wine\DllOverrides]
  "winemenubuilder.exe"=""
  ```

  To apply the setting, run:

  ```sh
  wine regedit disable-winemenubuilder.reg
  ```

- *Environment variable:* set the `WINEDLLOVERRIDES` environment
  variable when you run the installer, e.g.,

  ```sh
  WINEDLLOVERRIDES=winemenubuilder.exe=d wine setup.exe
  ```

  Users who frequently create new wineprefixes may wish to put
  `WINEDLLOVERRIDES=winemenubuilder.exe=d` in their `.bashrc` to avoid
  having to specify it for every wineprefix.

#### How do I disable the GUI crash dialog?

Wine includes a GUI crash dialog that is turned on by default. Users of
apps that work despite a background crash may find the GUI dialog
annoying, and in some cases the dialog itself has been reported to
prevent an app from working.

The easiest way to disable the crash dialog is with
[winetricks](Winetricks):

```sh
sh winetricks nocrashdialog
```

If you prefer to do it manually, copy the following key to a text
editor:

```
[HKEY_CURRENT_USER\Software\Wine\WineDbg]
"ShowCrashDialog"=dword:00000000
```

Save the file with a .reg extension (e.g. `crashdialog.reg`), then apply
it with regedit:

```sh
wine regedit crashdialog.reg
```

(You may need to specify the full path to the file, depending on where
you saved it.)

To turn the GUI crash dialog back on, change `00000000` to `00000001` and
reapply.

These changes can also be made by simply running `regedit` and
adding/changing the appropriate key the point-and-click way.

#### How can I make Wine fonts anti-aliased?

Support for subpixel font rendering was added to Wine in version 1.1.12,
but it may not be enabled. Use `winetricks` and select one of the
fontsmooth-gray, fontsmooth-rgb or fontsmooth-bgr options.

#### How do I change the DPI (font size)?

First, you should try editing with `winecfg`. Go to the Graphics tab,
and slide the "Screen Resolution" slider accordingly. Changes will not
effect the winecfg window until you restart it.

If windows and fonts are so big you can't get to the controls in
winecfg, see [Wine's windows and fonts are extremely
large](#wines-windows-and-fonts-are-extremely-large).

#### How do I configure a proxy?

If you want to use a proxy server for all HTTP connections, simply set
the `http_proxy` environment variable. On many Linux distributions,
configuring a network proxy, e.g. with the Network Proxy tool, does this
for you automatically.

Alternatively, you can configure a proxy in the registry. There are
separate locations for wininet.dll and winhttp.dll.

For wininet, use `regedit` to add the following values to the
`[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet
Settings]` key:

```
"ProxyEnable"=dword:00000001
"ProxyServer"="proxy-server-address:port"
```

At present, Wine's `wininet.dll` does not support proxy
autoconfiguration (PAC) scripts.

For winhttp, you'll need to use the `proxycfg.exe` utility to configure
the registry. This utility is available in the system32 directory of a
Windows installation, and MSDN describes its usage.

## Limitations and Risks

### Can Wine run in character mode?

Most of Wine's development effort is geared towards programs written for
the Windows GUI, but some limited support for character mode is
available with the "null" driver. Wine automatically activates "null"
whenever x11driver isn't loaded, but even then, Wine depends on the xorg
libraries.

Also the "null" driver will only work for *pure* console applications
that never use any windowing functions (for example, parts of OLE create
purely internal windows).

See the [Wine User's Guide chapter on text mode
programs](Wine-User's-Guide#text-mode-programs-cui-console-user-interface)
for more information.

### Can I install applications to be shared by multiple users?

Wine does not currently allow sharing its configuration ("prefixes")
between users, due to the risk of registry corruption from running
multiple wineservers simultaneously (bug #11112). At present,
applications must be installed separately for each user.

However, you can copy Wine prefixes; you can install everything to one
prefix, then make a copy of it in each user's home directory. This saves
running installers repeatedly.

### Can I use Wine to install drivers for my hardware?

No. Wine requires your hardware to already be working on your operating
system. The technical reason for this is that Wine, like most
applications, runs in user mode and not [kernel
mode](https://en.wikipedia.org/wiki/Kernel_mode).

### Is Wine malware-compatible?

Yes. Just because Wine runs on a non-Windows OS doesn't mean you're
protected from viruses, trojans, and other forms of malware.

There are several things you can do to protect yourself:

- Never run executables from sites you don't trust. [Infections have
  already
  happened.](https://list.winehq.org/mailman3/hyperkitty/list/wine-devel@winehq.org/thread/YQLLCOJ6S545G3BHNI7KSFVTI6RZNAK4)
- In web browsers and mail clients, be suspicious of links to URLs you
  don't understand and trust.
- Never run any application (including Wine applications) as root (see
  [above](#should-i-run-wine-as-root)).
- Use a virus scanner, e.g. [ClamAV](https://www.clamav.org) is a free
  virus scanner you might consider using if you are worried about an
  infection; see also [Ubuntu's notes on how to use
  ClamAV](https://help.ubuntu.com/community/ClamAV). No virus scanner is
  100% effective, though.
- Removing the default Wine Z: drive, which maps to the unix root
  directory, is a weak defense. It will not prevent Windows applications
  from reading your entire filesystem, and **will prevent you from
  running Windows applications that aren't reachable from a Wine drive
  (like C: or D:)**. A workaround is to copy/move/symlink downloaded
  installers to `~/.wine/drive_c` before you can run them.
- If you're running applications that you suspect to be infected, run
  them as their own Linux user or in a virtual machine (the ZeroWine
  malware analyzer works this way).

### How good is Wine at sandboxing Windows apps?

**Wine does not sandbox in any way at all.** When run under Wine, a
Windows app can do anything your user can. Wine does not (and cannot)
stop a Windows app directly making native syscalls, messing with your
files, altering your startup scripts, or doing other nasty things.

You need to use AppArmor, SELinux or some type of virtual machine if you
want to properly sandbox Windows apps.

Note that the [winetricks](Winetricks) `sandbox` verb merely
removes the desktop integration and Z: drive symlinks and is not a true
sandbox. It protects against errors rather than malice. It's useful for,
e.g., keeping games from saving their settings in random subdirectories
of your home directory.

## Applications

### What applications/services conflict with Wine?

Many distributions are moving towards enabling Compiz/Beryl/other eye
candy by default. The problem is that these programs conflict with Wine
over the display driver. Disable these programs before using any
applications with Wine (especially games, or when noticing weird window
problems). Also, disabling the Composite extension in
`/etc/X11/xorg.conf` will most certainly prevent compositing from
affecting Wine.

Keyboard tools such as IBUS, `xneur` (`gxneur`, `kxneur`) and SCIM have
been reported to conflict with keyboard input in Wine.

### Does Wine support .NET? Should I install native .NET in Wine?

Recent versions of Wine will prompt you to download
[wine-mono](Wine-Mono) on wineprefix creation. For many .NET apps,
particularly older ones, this is sufficient.

If wine-mono does not work for your app/game, file a bug (if one has not
been already filed), and try native .NET. You can install it by running
[winetricks](Winetricks) and selecting the appropriate .NET
version. Note that native .NET can at present only be installed to a 32
bit wineprefix, so if your app/game is 64 bit, you are out of luck for
now.

### Does Wine support DirectX? Should I install Microsoft's DirectX under Wine?

Wine itself provides a DirectX implementation that, although it has a
few bugs left, should run fine.

**If you attempt to install Microsoft's DirectX, you will run into
problems.** It is not recommended nor supported by Wine HQ to attempt
this. You can install the runtime, but it will not run. The runtime
needs access to the Windows drivers, and Wine cannot access them for
obvious reasons. The only native Microsoft DLLs that could be useful
anyway are the `d3dx9_xx.dll` type ones, and these require you to accept
Microsoft's license. Additionally, versions of these DLLs are now part
of the Wine tree. So, as Wine improves these DLLs will only become less
relevant.

That said, there are some guides out there which describe how you can
install Microsoft's DirectX. We reiterate: it is not recommended nor
supported by Wine HQ to attempt this. Furthermore it is considered off
topic in Wine HQ support mediums (such as the forums). Please use a
clean Wine configuration folder before seeking help (delete your
`~/.wine` or use another [wineprefix](#wineprefixes) and
re-install your Windows applications).

### Does Wine support Internet Explorer? Should I install Microsoft's Internet Explorer in Wine?

Wine uses the core of Firefox to implement its own Internet Explorer
replacement (wine-gecko). Recent versions of Wine should prompt you to
install it on wineprefix creation. In most cases Wine's IE replacement
(wine-gecko) is sufficient.

If you really need the real IE for a specific application to work, use
[winetricks](Winetricks) to install ie6, ie7 or ie8. You
should put IE in a [separate
wineprefix](#can-i-store-the-virtual-windows-installation-somewhere-other-than-wine),
with whatever app really needs it. Note that the Wine project does not
support installing the real Internet Explorer, as it requires a huge
number of native DLLs, which is hard to configure. Please do not ask the
Wine project for help if you run into problems.

You may also try commercial solutions, such as
[CrossOver](https://www.codeweavers.com), but if you do so and run into
problems, do not seek help on the forum/mailing list or IRC, as third
party applications such as these are not supported here.

### Why doesn't Wine work well with some copy protection?

Copy protection uses several "dirty" methods to detect if discs are
"real" or not. Some of these methods work in Wine but many do not, such
as the extremely invasive StarForce system. Wine would need to be
altered to allow for almost rootkit-like functionality of programs to
get some of these copy protection schemes to work, so support is likely
to be a long time off if ever (some people use illegally modified or
"cracked" games with the copy protection removed, but the Wine project
cannot advocate that).

See also our page on [copy protection](Copy-Protection).

### I followed a howto I found on a website, and the application still doesn't work

There are many unofficial howtos for various apps posted on blogs and
forums. They are rarely maintained by their authors, and because of
Wine's rapid rate of development, even ones that were correct at the
time they were posted can quickly become outdated. Applying tweaks that
are no longer needed in current Wine can actually prevent an app that
now runs fine without tweaks from working at all (Office 2007 is a prime
example). The only howtos supported here are the ones on this site. If
you insist on following an outside one, ask its author for help.

If in doubt, start again installing the app in a fresh wineprefix and
ask for help on the user forum.

### I used a third party application (PlayOnLinux, WineBottler, etc.) to install or manage applications in Wine and need help

Consult the support channels for whatever third party application you
used. Links to some of these outside applications are provided as a
convenience on the [Third Party
Applications](Third-Party-Applications) page, but they are
not supported here. Before seeking help on the forum/mailing list/IRC or
filing bugs, reinstall your Windows application using plain Wine.

### My application worked with an older version of Wine, but now it's broken!

This is called a regression. Please perform a [regression
test](Regression-Testing) to identify which patch caused it,
then [file a bug report](https://bugs.winehq.org) and add the
"regression" keyword: we'll pay special attention to it, since
regressions are a lot easier to fix when caught early.

### I really need this particular application to work. How can I go about making this happen?

Briefly, you can improve Wine yourself, convince someone else to do it
for you, or try some complicated hacks involving native Windows DLLs
rather than Wine's unfinished ones.

### I'm writing a Windows app. How can it detect if it's running under Wine?

This is a bad idea. See the [Developer
FAQ](Developer-FAQ#how-can-i-detect-wine).

## Performance

### My 3D application/game is very slow (FPS)

Usually a 3D performance issue, indicates that something is wrong with
your OpenGL 3D drivers. See [3D Driver
Issues](3D-Driver-Issues) for more information.

### Is Wine slower than just using Windows?

Actually, Wine is sometimes faster. The speed of an application depends
on a lot of factors: the available hardware and their drivers, the
quality of the code in the APIs the application uses, and the quality of
the code in the underlying operating system.

Driver code matters a lot. If you're running a graphics-heavy
application using a video card with very poor drivers such as an ATI
card under Linux, performance will degrade substantially. On the other
hand, Linux has superior memory management, and comes out ahead of
Windows in many CPU-related tasks.

Sometimes, bugs in Wine can make applications excessively slow. That
said, Wine works on correctness first, performance second.

See [Performance](Performance) for more information.

### I get lots of "fixme:" messages in the terminal and Wine runs a bit slow

Ignore them. Generally speaking, a `fixme` message will not make much
sense to someone unfamiliar with Wine development. They are for Wine
[developers](Developers). Also, it's important to understand
that `fixme` messages often *do not* indicate a serious problem. Many
applications will work fine even though Wine prints a few `fixme`
messages. That said, they can still sometimes provide insight into how a
particular application works (or doesn't work).

If there are a very large number of these messages scrolling repeatedly,
you can sometimes speed Wine up a little by turning them off altogether.
You can do so by setting the `WINEDEBUG` environment variable to `-all`.
For example, your command line could look something like:

```sh
WINEDEBUG=-all wine program.exe
```

More advanced users and programmers interested in debugging Wine should
see [Debug Channels](Debug-Channels) and the
[Developers](Developers) wiki pages. Here's an example to
selectively turn off `fixme` messages from dsound and part of D3D only:

```sh
WINEDEBUG=fixme-dsound,fixme-d3d_surface wine program.exe
```

## Troubleshooting

### General

#### How can I get a debugging log (a.k.a. terminal output)?

Run your application from the command line (see the [Wine User's Guide
chapter on
how to run Windows programs from the command line](Wine-User's-Guide#how-to-run-windows-programs-from-the-command-line)).

You can then copy the log from the screen and paste it into a file if
it's short; otherwise redirect the output of wine to a file using a
[Unix shell
redirection](https://en.wikipedia.org/wiki/Redirection_(computing)), e.g.

```sh
cd ~/.wine/drive_c/Games/Tron
wine tron.exe &> log.txt
```

**Important**: Unless you have been asked specifically to provide a
[debug trace](#how-do-i-get-a-debug-trace) then do not do
so. Simply follow the instructions above.

**Important**: If you get a crash dialog while doing this, please click
**Close**. Otherwise your log will be incomplete.

**Important**: If the resulting text file doesn't have names of C source
files in it, your copy of wine probably lacks debugging symbols. Please
either build wine from source, or install the debug symbols package.

#### How do I get a debug trace?

**Note**: Please only use this procedure when instructed. In most cases
a regular terminal output is enough (see above). When filing bugs, it is
often necessary to get additional debug trace (generally `+relay,+seh`,
but you might be asked for specific [debug
channels](Debug-Channels)). To retrieve a trace, run:

```sh
WINEDEBUG=+relay,+seh,+tid wine your_program.exe >> /tmp/output.txt 2>&1
```

Then **attach** `/tmp/output.txt` to the bug. If the resulting file is
larger than 1 MB, compress it with `bzip2` or `rzip` before attaching.
There are some cases where the bug seems to disappear when `WINEDEBUG`
is used with the right channel. Please mention that in the bug report.
For a list of debug channels that are available in Wine, see [Debug
Channels](Debug-Channels)

### Crashes and Freezes

#### My program froze up, how do I close it?

If you ran the program from a terminal window by typing `wine
program.exe`, you can usually just go back to that terminal window and
press Ctrl+C. If you ran the application some other way, such as from
a launcher shortcut, then you can open up a terminal and forcibly kill
the process:

```sh
killall -9 Application.exe
```

If you want to kill all Wine programs at once, you can run:

```sh
wineserver -k
```

You can also open up a Wine version of the Windows task manager by
running `wine taskmgr` in a terminal. This will allow you to kill
individual Wine processes.

#### My whole computer freezes, reboots, or shuts off when I run my game in Wine!

If you are getting a complete deadlock and are unable to even use your
mouse after running Wine, it's probably not a specific problem with the
Wine software. Wine is a user-level process, and shouldn't be able to
completely hang the operating system under any circumstances. Instead,
Wine is likely exposing a deeper problem with the system, such as a
defective hardware driver, a bad memory stick, or overclocking
flakiness.

It's often a graphics driver problem, in which case non-Wine apps might
also be affected. If running `glxgears` also crashes, it's definitely a
graphics driver problem. The most common cause is upgrading to a new
kernel without also updating the graphics drivers to match. Try
reinstalling your graphics drivers.

If the computer is a laptop and shutting itself off entirely, a likely
cause is overheating. Some laptops have problems with cooling to begin
with, and the Linux ACPI code controlling fans is known to be buggy.

If that doesn't help, ask for help on the wine-users forum. Be sure to
mention the name of the app, the version of Wine, the output of
`cat /etc/issue` , `lspci | grep -i vga` , and, if you're using the
proprietary NVidia drivers, `cat /proc/driver/nvidia/version` . Maybe
someone can help.

#### Every app I try to start crashes

You may have a messed-up `.wine` directory (aka wineprefix). For
instance, if you install an app that starts a service when the system
boots, and that service crashes, you'll see a crash every time you start
wine.

To work around this, try [removing your .wine
directory](#how-do-i-wipe-the-virtual-windows-installation)
and reinstall your apps, but skip the one that broke things.

### Warning and Error Messages

#### My application says some DLL or font is missing. What do I do?

Applications *should* come with all the DLLs they need (except for core
Windows DLLs). They sometimes forget to, and rely on you to already have
the DLL or font installed. You can install the missing DLL or font in
several ways:

- downloading it from the original creators of the runtime (e.g.
  Microsoft). The easiest way to do this is with
  [winetricks](Winetricks).
- install other applications which do include them.
- copy it from a licensed version of Windows installed on the same
  machine.

*Do not download DLLs or scripts from websites you do not know and
trust!* Fake or infected DLLs can cause you great pain, even on Wine.

See the [winetricks wiki page](Winetricks) for more
information on winetricks.

#### `Too many open files, ulimit -n probably needs to be increased`

Your operating system is probably living in the past, and has too low a
hard limit on the number of open file descriptors. (See
<https://bugs.launchpad.net/ubuntu/+bug/663090> for why raising the hard
limit is the right thing to do, and why raising the soft limit by
default is dangerous.)

For Ubuntu and most modern versions of Linux, you can edit
`/etc/security/limits.conf` as root, and change the line

```
* hard nofile 2048 (or whatever the current limit is)
```

to

```
* hard nofile 8192
```

(The asterisk means 'for all users'.)

Then log out and log in again, and do `ulimit -H -n`. It should show
8192 now, and Wine should have access to more file descriptors.

Here's another method that's more portable (might even work on Mac OS
X), but only works temporarily, and only raises the limit for apps
started from the current terminal window:

```sh
sudo bash
ulimit -n 8192
su yourusername
wine yourprogram.exe
```

#### `preloader: Warning: failed to reserve range 00000000-60000000` or `winevdm: unable to exec <application>: DOS memory range unavailable`

This issue is being followed in bug #12516.

The cause is a Linux kernel setting. Run
`cat /proc/sys/vm/mmap_min_addr` as root: if it does not equal 0 then
running `sysctl -w vm.mmap_min_addr=0` as root can be used to
temporarily fix the issue; to fix it permanently, add the line
`vm.mmap_min_addr=0` to `/etc/sysctl.conf`. Please record if you do this
alteration, as the area Wine needs may change.

See [Preloader Page Zero
Problem](Preloader-Page-Zero-Problem) for more information.

#### `Failed to use ICMP (network ping), this requires special permissions`

On \*NIX systems ICMP ping requires use of raw sockets, which is limited
to super user (root) only. And running Wine as root is a [bad
idea](#run-as-root). Fortunately newer versions of Linux
allow granular permission control to grant only required permissions to
specified files.

To allow Wine opening raw sockets run this command:

```sh
sudo setcap cap_net_raw+epi /usr/bin/wine-preloader
```

**Note**: This works with default binary Wine install only on most
distros. WineHQ packages install Wine to `/opt/wine-stable`,
`/opt/wine-devel`, or `/opt/wine-staging`. Self-compiled Wine will be
located under `/usr/local/bin`. The 64-bit name is
`wine64-preloader`. Third party Wine wrappers (such as PlayOnLinux)
might keep Wine binary in other places. You will need to rerun the
command after updating Wine.

To remove the permissions use:

```sh
sudo setcap -r /usr/bin/wine-preloader
```

Beginning with Wine 5.7, the WineHQ Debian and Ubuntu packages have an
optional debconf setting to enable CAP_NET_RAW to allow applications
that need to send and receive raw IP packets to do so. This is disabled
by default because it carries a potential security risk, and the vast
majority of applications do not need that capability. Users of
applications that do need it can enable CAP_NET_RAW after installing
Wine by running

```sh
dpkg-reconfigure wine-<branch>-amd64 wine-<branch> wine-<branch>-i386
```

and answering yes to the three questions. (Substitute devel, staging, or
stable for `<branch>` in the above command.)

#### `err:virtual:map_image failed to set 60000020 protection on section .text, noexec filesystem?`

This can be caused by filesystems mounted with user or noexec options,
or by SELinux. Make sure the app in question isn't on a funny
filesystem, or try disabling SELinux temporarily.

#### `Broken NVIDIA RandR detected, falling back to RandR 1.0`

[RandR](https://en.wikipedia.org/wiki/RandR) is a protocol used by
applications to talk to the X server to change screen resolution, among
other things. nVidia's proprietary drivers for GNU/Linux intentionally
do not properly implement newer versions of RandR, which Wine normally
relies upon. This could present problems, particularly in software that
attempts to change resolution or output to multiple monitors. (See
bug #34348)

The open source Nouveau driver is not affected by this issue, and is the
recommended solution for users who do not need the proprietary driver
for any of their apps or games. Users who require the proprietary driver
should try the workaround described below.

Many applications will attempt to start in lower resolutions if (and
only if) they are available - but will happily use a higher resolution
if that is the only option. In this case, you may be able to avoid a
crash on nVidia drivers by forcing your X server to only support your
monitor's native resolution and nothing else. This has proven to work
for a range of games.

To make this change to Xorg, edit (as root) /etc/X11/xorg.conf and add
the following line:

```
Option "metamodes" "1920x1080 +0+0"
```

within the Screen section (changing 1920x1080 to whatever supported
resolution you require).

Upon restarting Xorg, you can test your changes using the xrandr
command. `xrandr` should list your chosen resolution, and `xrandr --q1`
should do the same. There should not be any additional resolutions
listed. You may now re-test your Windows application, hopefully with
more success. Remember to comment out the line and restart Xorg when you
are finished if you need other resolutions working for other software.

### Graphics

#### My application complains about being unable to change the resolution or color depth

You generally need to edit the Screen section of your
`/etc/X11/xorg.conf` to support additional color depths and resolutions.
There may also be a problem with Xrandr.

#### The application I am trying to run complains that it needs 256 colors but I have millions!

The inability to switch from 24bpp mode to 8bpp mode is a limitation of
X, not a bug in Wine. See [256 Color Mode](256-Color-Mode)
for some possible workarounds.

#### My X screen won't go back to its normal resolution after running a game fullscreen

You can often work around this by changing the screen resolution and
then changing it back again under the system preferences.

Alternately, you can run this terminal command to restore your X
settings:

```sh
xrandr -s 0
```

#### I'm using Desktop Effects with Compiz, Fusion, or XGL and get poor performance/odd messages/broken applications

Using compositing managers in X11 tends to cripple OpenGL performance or
break OpenGL entirely (this does not apply to the Mac OS X compositor,
which cannot be disabled). We recommend that you disable them entirely
before trying to use Wine. If you are using one and experiencing slow
performance then please do not file bugs in Wine, as these are bugs in
your window manager or your video drivers. Also, disabling the Composite
extension within `/etc/X11/xorg.conf` will most certainly prevent any
compositing from affecting Wine.

#### Graphics in games with good ratings in AppDB are scrambled

- Retry using the latest graphics drivers.
- Most [AppDB](https://appdb.winehq.org/) entries are based on
  **NVIDIA/GeForce** hardware running the proprietary driver.
- **ATI**/**AMD**/**Radeon** cards running the proprietary fglrx driver
  have problems in Wine. As a rule of thumb, at least games that use
  shaders are broken. See [this
  posting](https://article.gmane.org/gmane.comp.emulators.wine.user/36669)
  and bug #7411 for details.
- **Other hardware** (Intel/S3/Matrox etc.) will probably run only old
  (non-shader) games. Compatibility is not well tested.
- Same for **open source** drivers as their 3D support is typically
  basic only.

#### Wine displays corrupted or missing text

This may be bug #16146, caused by the `nvidia-96xx` legacy driver, or
bug #18120, which affects QT 4.5.0 applications. It could also be
caused by missing fonts, font conflicts, or adding new fonts to Wine.

Try using a fresh Wine prefix (by moving or deleting `~/.wine`, or
changing the `$WINEPREFIX` environment variable). If you still have this
problem, try setting the following in the Wine registry:

```
[HKEY_CURRENT_USER\Software\Wine\X11 Driver]
"ClientSideWithRender"="N"
```

Place above in a text file called `norender.txt` and it can be inserted
into the registry with the command `regedit norender.txt`. Please apply
only as required. (This was reported as being required of OS X on the 1
Dec 2007, and more recently on other platforms, such as Ubuntu.)

#### Wine's windows and fonts are extremely large

Sometimes you can use the Alt key and the mouse to move the winecfg
window so you can reach the "Screen Resolution" slider on the Graphics
tab; slide it down. Changes will not effect the winecfg window until
it's restarted.

If that doesn't work, you can use this one line registry change (all one
line):

```sh
echo -e "[HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Hardware Profiles\\Current\\Software\\Fonts]\n\"LogPixels\"=dword:60\n" | wine regedit -
```

If all fails, you could remove your `~/.wine` directory and reinstall
your Windows applications.

### Sound

#### MP3s do not play in Windows Media Player or applications that depend on it

For MP3 sound to play out of the box in apps that use the WMP engine and
codecs, you must have 32-bit `libmpg123` installed on your system and
Wine must have been compiled with MP3 support. Historically, not all
distros have provided this for legal reasons, though this problem should
be much less widespread now that all mp3 patents have expired.

For users still affected by this, the workaround for lack of libmpg123
and/or winemp3.acm is to use the codec installed by WMP9, l3cod­eca.acm.
Copy l3codeca.acm to the wineprefix's /windows/system32 directory (or
use winetricks to install WMP9), then create a symlink to it named
winemp3.acm in the same directory. Wine will then use the native codec
to play MP3s.

This only affects WMP and apps that rely on it for MP3 playback
(including Powerpoint). Apps that install their own MP3 codec, such as
Winamp or VLC Player, should be able to play MP3s without this
workaround.

#### Bad or no sound on systems using PulseAudio

Bad or no sound was a problem on some systems with Pulseaudio in older
versions of Wine using the winealsa driver. If you are using a version
of Wine older than 1.8, please upgrade, as most such problems should be
solved by the winepulse driver. If the problem still occurs, try
unsetting the `PULSE_LATENCY_MSEC` environment variable. Some distro
packages (notably Debian) formerly set this variable to work around the
sound issue with the winealsa driver, but it is not needed with the
winepulse driver and may prevent sound from working.

### Networking

#### My program fails to do networking, but my other applications can get online

**Note:** These instructions are for older Wine installs. If you're
using Wine 1.x and your application still fails to do networking, you
can give this a try as well. If you're running Wine 1.x and below
instructions work for you, **file a bug** so we can fix Wine to improve
other people's experience.

You need to make sure that your hostname resolves to the IP address of
your network interface. To verify if you have this problem run `hostname
-i`. If it returned IP address starting from "127." then read on.

To set this up correctly, you can type the following from a terminal:

```sh
hostname
```

This will return your hostname the way your computer sees it. Now, you
need to open an editor with system administrator privileges, how you do
this will depend on the distribution you are using. Open the file
`/etc/hosts` and see if there is an entry for your hostname. Assuming
your hostname is "yourhost" and your network IP address is 192.168.0.23,
the entry might look like this:

```
127.0.0.1 yourhost.yourdomain.com yourhost
```

Change this to (or add, if there is no such line):

```
192.168.0.23 yourhost.yourdomain.com yourhost
```

For most Windows games with networking problems, this is all you need to
get networking to work.

#### Why doesn't DNS resolve in 64-bit operating systems?

Many distributions don't provide all the 32-bit compatibility libraries
that wine needs. In this case, wine needs 32-bit DNS libraries. On
Ubuntu/Debian, this package is `libnss-mdns:i386`. For other operating
systems, the package name may differ. Consult your distribution's
support channels.

### Removable Media

#### My CD or DVD disc won't eject

Try `wine eject`. It is a function to free up, unlock, and eject the
drive. Make sure that the drive is mapped as a CD-ROM in `winecfg` and
specify the drive letter in the command line, e.g.

```sh
wine eject d:
```

#### The application's CD or DVD looks empty or is missing some files!

Some discs are poorly mastered in a way that affects only Unix-based
operating systems.

You may need to use the "unhide" or "norock" mount options for these
discs.

Run `mount` once to see where the disc is mounted, then mount it again
in the same place with the needed option (and the "remount" option).
Some assembly required.

Examples:

```sh
sudo mount -o remount,unhide /dev/sr0 /mnt/cdrom
```

or

```sh
sudo mount -t iso9660 -o ro,unhide /dev/cdrom /media/cdrom0
```

See also your operating system's documentation, e.g.
<https://help.ubuntu.com/community/Mount> or
<https://manpages.ubuntu.com/manpages/natty/man8/mount.8.html>

### Input Devices

#### Some key combinations in my application do not work

Even in full screen mode, window managers typically capture some keys.
For example, in KDE and GNOME, Alt+Left Click is used to move the whole
application window by default. Thus, this key combination is not
available to applications in Wine. You have to disable the colliding
combinations in your window manager. For KDE, see Control Center/Window
Behaviour or (better) Window-specific settings/Workarounds/Block global
shortcuts. For GNOME, see System/Preferences/Windows and change the
"Movement Key" setting. Also see System/Preferences/Keyboard Shortcuts
for specific keyboard combinations.

(Keywords: Keyboard, Shortcut, Modifier, Alt, Ctrl, Control.)

#### My mouse jumps around/resets its position often in games

See #27156 and <https://bugs.freedesktop.org/show_bug.cgi?id=30068>.

### Miscellaneous

#### My application runs, but text areas act strangely (e.g. lines don't wrap, double-clicking doesn't select words)

You may have run into a bug in Wine's RICHED20.DLL. You can try using
Microsoft's RICHED20.DLL by running [winetricks](Winetricks)
and selecting `riched20`. This may let you work around the problem until
the Wine developers fix the bug.

#### I deleted my Wine menu, and now I can't get it back

Rather than actually delete anything, menu editors on Unix desktops
simply mark menu entries as hidden so that they don't show up in the
menu. Thus, they remain hidden after reinstalling the application.
First, see if these menu entries can be found your menu editor and
re-enabled.

This information is stored in `~/.config/menus/applications.menu` . Edit
`~/.config/menus/applications.menu` and you should find a section near
the end that looks similar to this:

```xml
<Menu>
    <Name>wine-wine</Name>
    <Deleted/>
</Menu>
```

or perhaps this:

```xml
<Menu>
    <Name>wine-wine</Name>
    <Menu>
        <Name>wine-Programs</Name>
        <Menu>
            <Name>wine-Programs-AutoHotkey</Name>
            <DirectoryDir>/home/user/.local/share/desktop-directories</DirectoryDir>
        </Menu>
    </Menu>
    <Deleted/>
</Menu>
```

Remove the `<Deleted/>` line and your Wine menu will reappear.

#### 16-bit applications fail to start

See #36664. For 64 bit Linux Kernels 3.15+, 3.14.6+, 3.10.42+,
3.13.22+, 3.4.92+ and 3.2.60+. You'll need to run:

```sh
echo 1 > /proc/sys/abi/ldt16
```

as root, but be aware that this has security implications.

If your kernel is older than the above stated versions
`/proc/sys/abi/ldt16` most likely will be missing.

The security fix is espfix64 and as of yet only exists in development
branch for 3.16 Linux Kernel. At some point in a future I will put a
list of kernels containing the security fix as it most likely will be
backported when it is tested. Doing `/proc/sys/abi/ldt16` will be
required on the security fixed kernels just like the current insecure
ones.

#### Input doesn't work over SSH

When using Wine over SSH, you must run in 'trusted X11 forwarding'
mode.  For OpenSSH, this means using `-Y` instead of `-X`. See for
example bug #41476.
