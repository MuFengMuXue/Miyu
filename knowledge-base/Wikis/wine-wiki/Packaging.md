Here are some guidelines for anyone interested in packaging Wine for
their favorite distro.

Even most new distros these days wind up using a variation on one of a
few mature packaging systems. If you're interested in packaging wine for
a new distro (or helping out with an existing one), a good place to
start would be to get in touch with the current packager for the distro
most similar to yours.

## Packaging Goals

Any Wine package should meet several criteria so that the end-user has a
good experience.

Here are some main guidelines:

- Installation should be quick, simple, and require as little user input
  as possible
- The install locations should comply with [Filesystem Hierarchy
  Standard (FHS)](https://wiki.linuxfoundation.org/en/FHS)
- The package and installation should have as small a footprint as
  possible
- After installation, the average user should have to make minimal
  config changes
- However, none of Wine's flexibility should be taken from the user; all
  config options should be preserved and accessible
- A 64-bit package should have full WoW64 capabilities (details about
  making your package WoW64-ready are below)

## Preparation

For the most part, you should try to follow the normal steps for
[building Wine](Building-Wine). Use the plain vanilla instructions for
the 32-bit build and try the WoW64 build first for your 64-bit package
(so 32-bit applications are still supported).

If for some reason, you can't perform the combined WoW64 build on your
system, it is still possible to splice files from a 32-bit build into a
64-bit package. See the workarounds section towards the bottom of this
page for more details.

You also want to build Wine with as many build-time dependencies
satisfied as possible. That way your users have a full range of features
when running Wine (depending on your audience, you might leave out some
legacy or niche features).

## Dependencies

Since Wine is designed to support a wide range of programs, many users
might not need all of the features Wine provides. For that reason, a
major design goal of Wine is to make features pluggable with "soft"
dependencies. However, since different users have different needs, these
features should still be activated by default to give a good
out-of-the-box experience.

When you write up your package's dependencies, you should instruct the
package manager to install all of these soft dependencies by default but
allow removing them later, without marking any dependencies as broken.
For example, .deb packages use the "Recommends" field for this.
Recommended dependencies are automatically pulled in during
installation, but removing them only disables narrow features within
Wine.

## Subpackages & Directories

While the FHS is pretty simple to read and understand, here are some
basic guidelines on where components should be installed...

- Commands intended to be directly invoked by the user [belong in
  /usr/bin](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s04.html).
- Programs meant to be called indirectly should either go [into /usr/lib
  (mixed with
  libraries)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s06.html)
  or [/usr/libexec (only for binaries and scripts; no libraries
  allowed)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s07.html)
- The FHS allows for a distro to take either approach, but they're
  mutually exclusive and cannot be mixed; be sure to check which your
  distro uses.
- Libraries (SO files) should be placed in */usr/lib* (or some variation
  for multilib)
- In recent versions of Wine, most of the supplementary programs are
  built as SO libraries too; if you want users to be able to invoke them
  directly, you'll want to provide wrapped symlinks inside */usr/bin*
- Any read-only, arch-independent data files should go [inside
  /usr/share](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s11.html);
  this includes Wine's config files, fonts, and docs
- The manpages for Wine belong specifically [in
  /usr/share/man](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s11.html#usrsharemanManualPages);
  all of the current manpages are of category *man1*, though in the
  future *man5* (e.g. for Wine's registry file format) or *man6* (for
  demos like winemine) could come into play
- The FHS allows for an application to have its own directory within
  */usr/share* for app-specific data files
- For developer packages, all headers and other include files [belong in
  /usr/include](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s05.html)
- It isn't explicitly stated as allowed or forbidden in the FHS, but you
  should consider installing all of wine's include files to a *wine/*
  subdirectory

### Multilib / Multiarch

If you're packaging a 64-bit version of Wine, you'll also need to make
sure you have 32-bit libraries for WoW64 support. Normally, the best way
to do this is to split Wine into at least 2 distinct packages:

- A common package with only arch-independent parts common to both
  versions of Wine
- An arch-specific package, built for each architecture separately,
  containing libraries and binaries like the wineserver

Then, when marking these packages' dependencies, just make sure the
arch-specific package depends on the common one (or vice versa)

For an example of a variation, currently (August 2015) in Debian
Stretch...

- The main *wine-development* package (development release) is identical
  for all arches & contains only symlinks, scripts, and documents.
- It in turn depends on at least one of two small packages:
  *wine32-development* (for i386, ARM, etc.) or
  *wine64-development* (for AMD64 or ARM64).
- Each of these contains only the binary loader for Windows applications
  of the respective bitness.
- Since the Windows corpus is overwhelmingly 32-bit, the 64-bit package
  recommends the 32-bit one.
- Finally, each of these loader packages depends on its own arch's
  *libwine-development* package, which contains all of Wine's DLLs,
  programs, plus the wineserver.

At least in the Debian example, the need for two separate versions of
libwine leads to a lot of duplication. Someone better-versed on WoW64
should write if and how that can be reduced.

Another point is that for multilib and [Multiarch](Multiarch)
packaging, symlinks take on a new level of importance. Because the FHS
currently only allows qualifications for the */lib* and */usr/lib*
directories, files that must be sorted by ABI or architecture have to go
there. Since this often includes binaries that normally go in */usr/bin*
(and you probably don't want to add all your libraries to your PATH
variable), you'll want to install symlinks and/or scripts to the
*/usr/bin* directory that point to the real programs in the *lib*
directories.

## Wine Components

Here is a breakdown of components that you'll want to include in your
wine package(s) for **end-users**. Your distro will probably require one
or more additional folders with packaging code.

These tables and lists are based on the packaging structure for Wine's
development release on Debian Stretch. Your distro will probably have
some variations, but it's not a bad example to start from, especially
for reconciling multilib with the FHS.

### Binaries

These are the actual Unix-compatible, ELF binaries that form the core of
Wine.

In isolation, all of these could theoretically be placed in */usr/bin*
and invoked from a terminal without any other setup. However, for both
better usability and multilib compatibility, you'll probably want to
place most or all of them in the appropriate variant of */usr/lib*.
Setting up the appropriate symlinks in */usr/bin* to enable the commands
is discussed in its own section below.

- **wine:** The binary loader, which arranges program instructions and
  all necessary libraries in memory, then starts execution
- Install to */usr/bin* **only if** you're not concerned about multilib
- If you want to split WoW64 wine into multiple packages, consider
  giving the 32- and 64-bit versions different names or subdirectories,
  then calling them from a wrapper script that decides which to use at
  runtime
- **wine-preloader:** An alternative, prelinked version of the binary
  loader
- Prelinking is only available on Linux
- This is needed to run some programs successfully (particularly ones
  with CopyProtection)
- Since only some users need it (or can even use it), consider packaging
  it separately
- Otherwise, the same notes about the standard loader apply
- **wineserver:** The core process that manages program execution
- Place in */usr/bin* **only if** you're unconcerned about multilib
  **and** you want to give direct access to your typical end-user
- Because of how the binary loader implicitly calls the wineserver, if
  you're modularly packaging WoW64 wine, you may want to rename the
  wineserver binaries and use a wrapper script to choose one at runtime

### Wrapper Scripts

In order to allow for modular packaging and elegant commands, there are
a few places you might want to insert a script between a command or
symlink and it's normal target.

- **wineapploader (Highly Recommended):** A wrapper script for calling
  winelib applications from symlinks as if they're unix commands
- Since this isn't intended to be called directly, it naturally belongs
  somewhere in */usr/lib*
- The script is agnostic about both arch and directory so it can be part
  of a common wine package
- It may need a few modifications for your distro
- It is part of the codebase here upstream and can be found in the
  *tools/* directory of the source tree
- **wine (Recommended for WoW64 Packaging):** A substitute for the
  normal wine command that can sort out bitness and multilib issues at
  runtime
- Since this is a wrapper for the normal wine command, you'll want to
  put it in */usr/bin*
- There doesn't seem to be a canonical version of this upstream (should
  there be?)
- For one example, take a peek at the [wrapper script used in the Debian
  package](https://anonscm.debian.org/cgit/pkg-wine/wine.git/tree/debian/scripts/wine)
- **wineserver (Recommended if Packaging WoW64 with Multilib)**: A
  mediating script that ensures the wineserver of the correct bitness is
  called, regardless of order in \$PATH
- To use this, you'll want to rename the actual wineserver binaries
  first (e.g. *wineserver.real*)
- Since it needs to be where the wine loader expects *wineserver*, place
  a copy alongside each of the true binaries (i.e. in the same
  directory)
- Beyond that, it should be very simple and the multilib standards
  should take care of the rest.
- For an example, see this [one-liner from the Debian
  package](https://anonscm.debian.org/cgit/pkg-wine/wine.git/tree/debian/scripts/wineserver)

### Commands

These are some actual commands you should consider providing to the
end-user. As a result, you'll want to place them all in */usr/bin*, but
they aren't all necessarily ELF binaries.

Anyways, here is a chart with notes about exactly how to provide them...

| Command Name | Description                                                                             | Vanilla Command Form | Multilib Command Form    | Target (if Redirecting)                       | Notes                                                                                                                      |
|--------------|-----------------------------------------------------------------------------------------|----------------------|--------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| regedit      | A GUI to edit your Wine registry or import a Windows registry                           | Symlink              | Symlink                  | *wineapploader* (script, mentioned above)     |                                                                                                                            |
| regsvr32     | A service to register/unregister DLL and OCX files                                      | Symlink              | Symlink                  | *wineapploader* (script, mentioned above)     | Only works for self-registering libraries                                                                                  |
| wine         | The main wine command, which calls the binary loader to start running a Windows program | Binary               | Script (mentioned above) | Correct binary loader (in */usr/lib* aut al.) |                                                                                                                            |
| wineboot     | Simulates startup and shutdown on Windows                                               | Symlink              | Symlink                  | *wineapploader* (script, mentioned above)     | Allows certain services (e.g. upgrades) and applies changes to a prefix's configuration                                    |
| winecfg      | The GUI for configuring individual Wine prefixes                                        | Symlink              | Symlink                  | *wineapploader* (script, mentioned above)     |                                                                                                                            |
| winedbg      | The debugging service for applications on Wine, not to mention Wine itself              | Symlink              | Symlink                  | *wineapploader* (script, mentioned above)     | Needed to report bugs upstream, but not to run wine; more appropriate in debug/dev package (depending on distro audience)? |
| winefile     | A clone of the Windows 3.x file manager (?)                                             | Symlink              | Symlink                  | *wineapploader* (script, mentioned above)     | How does this program relate to the \["explorer"\] program?                                                                |
| winepath     | A tool for easily converting between Windows and Unix paths                             | Symlink              | Symlink                  | *wineapploader* (script, mentioned above)     |                                                                                                                            |

### DLLs

Most of Wine's functionality is provided by SO libraries that substitute
for Windows DLLs. These should go inside */usr/lib* or a multilib
equivalent....

To obtain a current list of DLLs, after a successful build, *cd* to the
top of your Wine build tree and list all *.so* files in the *dlls/*
directory:

```
ls dlls/*.so
```

Some of the files here (such as Control Panel applets and drivers)
aren't called DLLs from a Windows standpoint, but they're effectively
the same for Wine.

### EXEs

These are supplementary programs that substitute for common ones on
Windows. Although they are compiled as Winelib executables, they're
linked to wine itself as Unix .so libraries. As a result, they'll also
go inside whatever variation of */usr/lib* your distro uses....

Just like with the DLLs, you can get a current list of wine executables,
after a successful build, by listing all *.so* files in the *programs/*
directory:

```
ls programs/*.so
```

### Fonts

Wine also provides alternate versions of the fonts used by Windows.
These actually take two different forms: .ttf (TrueType fonts) and .fon
(DOS-compatible bitmap fonts). The TrueType files are currently
developed here at WineHQ using a special version of
[FontForge](https://fontforge.github.io/en-US/), then distributed (along
with the source .sfd files) as binaries in git. The .fon files, however
are built-up at compile time.

After a successful build, to get full lists of the needed font files,
try this from the top of your build tree:

```
ls fonts/*.ttf
ls fonts/*.fon
```

Wine's fonts should be a natural candidate for their own subpackage;
just remember to put them into at least */usr/share* (if not wine's
subdirectory of */usr/share*)

### Manpages

These are the command-line manuals for wine's main commands (and will go
in */usr/share/man*). You can programmatically grab a current list of
man files right after running *configure*; just use the *find* command
at the top of your build directory:

```
find . -name "\*.man"
```

If you decide to provide a specific command or subprogram through a
separate package, don't forget to shift any corresponding manpages to
that package too

### Config Files

Wine also depends on a couple data files; it makes sense to place these
in a wine-specific share folder (e.g. */usr/share/wine*)

- **wine.inf**: This is the global Wine setup file; it uses the MS
  Installer .inf file format
- **l_intl.nls**: This file is used in the absence of unicode support to
  properly handle text and filenames from different character sets

Wine will automatically generate its registry files the first time it
runs. So as a packager, you shouldn't need to worry about them.

## WoW64 Workarounds

Sometimes, a distro's standard build process for packaging conflicts
with the steps necessary for the shared WoW64 build (e.g. approved build
tools conflict with a chroot). Thankfully, this turns out to be a minor
obstacle; a WoW64-capable Wine installation only needs to pull in the
DLLs (and a couple binaries and libraries) from 32-bit Wine...

- All DLLs (including ones only built for 32-bit)
- Static libraries of form *libwine.so\**
- The 32-bit *wineserver*
- The 32-bit binary loader
- Optionally, the prelinked version of the 32-bit binary loader

As for how you get these individual files, you shouldn't need to worry
about relinking as long as you built them correctly. You can either
build the 32-bit package with a custom hook, which copies the needed
files into a separate WoW64 sub-package, or just finish the 32-bit
package, then extract and splice the files into your 64-bit package.

Just be careful to keep the 32- and 64-bit versions separated correctly,
both in the package and when installed to the system

## Developer Spec Package

*This section is still incomplete; if you're familiar with packaging
include files and build tools, please fill in any gaps*

According to the FHS, all include files belong in */usr/include*, though
there's no prohibition against an app-specific subdirectory
(*/usr/include/wine*). An up-to-date list of the used header and include
files can be found in the source tree at *include/Makefile.in*

Note that during build-time, the non-standard include files (such as
.idl and .x files), will generate corresponding .h files; both are
needed in your package and should go into */usr/include*

Your package may also need to include definition files. However, it's
not clear from existing docs how these are generated, only that they
should go in the same directory as the runtime wine libraries they apply
to (in the proper subdirectory of */usr/lib*)

## Developer Tools Package

*This section should also be filled out more and checked*

For those interested in using wine as a framework for developing their
own programs, there are also some tools that can be packaged...

- **winebuild**: A tool used for building Winelib applications (and by
  Wine itself to translate .spec into .spec.c files)
- **winedump**: Dumps the imports and exports of NE and PE files
- **winecpp**: ???
- **winegcc** and **wineg++**: Wrappers for gcc and g++ respectively,
  which allow the native gcc & g++ to stand in for MinGW's compilers;
  useful for porting apps to Winelib
- **winemaker**: Winemaker is a perl script designed to help you convert
  your Windows projects to Winelib ones
- **wmc**: The Wine Message Compiler translates Windows message files
  into a format that Wine can work with
- **wrc**: The Wine Resource Compiler is an alternative to Microsoft's
  *rc* program

Don't forget to put the manpage for the primary *winegcc* command inside
*/usr/share/man*

## See Also

- [v3.0 of the Filesystem Hierarchy
  Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

- [Building Wine](Building-Wine)
- [Compatibility](Compatibility)
- [Multiarch](Multiarch) in Wine build dependencies
