<small>
&nbsp;[:flag_fr: Français](fr/Winetricks)
&nbsp;[:flag_nl: Nederlands](nl/Winetricks)
&nbsp;[:flag_th: ภาษาไทย](th/Winetricks)
&nbsp;[:flag_kr: 한국어](ko/Winetricks)
</small>

-----

## What is winetricks?

**Winetricks** is a helper script to download and install various
redistributable runtime libraries needed to run some programs in Wine.
These may include replacements for components of Wine using closed
source libraries.

**Note:** Although using winetricks may be *very* useful for getting
some programs working in Wine, doing so may limit your ability to get
support though WineHQ. In particular, reporting bugs may not be possible
if you've replaced parts of Wine with it. See [Reporting bugs after you
have used Winetricks](#reporting-bugs-after-you-have-used-winetricks) below.

**Note:** Some of the packages listed below may not work well with older
versions of Wine. As always we recommend you use the [latest version of
Wine](Download).

## Getting winetricks

The script is maintained by Austin English at
<https://github.com/Winetricks/winetricks>. The latest release is
available at
<https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks>.
Right-click on that link and use 'Save As' to save a fresh copy.
Alternatively you can get winetricks, using the commandline, with the
command:

```sh
$ cd $HOME/Downloads
$ wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
$ chmod +x winetricks
```

Also, some winetricks "packages" require a few external tools to be
installed, namely: `cabextract`, `unzip`, `p7zip`, `wget` (or
`curl`). For GUI support, either `zenity` or `kdialog`.
Linux users can usually get these via their distribution's package
management system.

## Using winetricks

Once you've obtained winetricks you can run it simply by typing `sh
winetricks` at the console. You can also use `./winetricks` if you
`chmod +x winetricks` first. If run without parameters, winetricks
displays a GUI with a list of available packages. If you know the names
of the package(s) you wish to install, you can append them to the
winetricks command and it will immediately start the installation
process. For example,

```sh
$ sh winetricks corefonts vcrun6
```

will install both the corefonts and vcrun6 packages.

## Options

Version 20200412 help text:

```
Usage: /usr/bin/winetricks [options] [command|verb|path-to-verb] ...
Executes given verbs.  Each verb installs an application or changes a setting.

Options:
    --country=CC      Set country code to CC and don't detect your IP address
-f,  --force           Don't check whether packages were already installed
    --gui             Show gui diagnostics even when driven by commandline
    --isolate         Install each app or game in its own bottle (WINEPREFIX)
    --self-update     Update this application to the last version
    --update-rollback Rollback the last self update
-k, --keep_isos       Cache isos (allows later installation without disc)
    --no-clean        Don't delete temp directories (useful during debugging)
-q, --unattended      Don't ask any questions, just install automatically
-r, --ddrescue        Retry hard when caching scratched discs
-t  --torify          Run downloads under torify, if available
    --verify          Run (automated) GUI tests for verbs, if available
-v, --verbose         Echo all commands as they are executed
-h, --help            Display this message and exit
-V, --version         Display version and exit

Commands:
list                  list categories
list-all              list all categories and their verbs
apps list             list verbs in category 'applications'
benchmarks list       list verbs in category 'benchmarks'
dlls list             list verbs in category 'dlls'
games list            list verbs in category 'games'
settings list         list verbs in category 'settings'
list-cached           list cached-and-ready-to-install verbs
list-download         list verbs which download automatically
list-manual-download  list verbs which download with some help from the user
list-installed        list already-installed verbs
arch=32|64            create wineprefix with 32 or 64 bit, this option must be
                      given before prefix=foobar and will not work in case of
                      the default wineprefix.
prefix=foobar         select WINEPREFIX=/home/$USER/.local/share/wineprefixes/foobar
annihilate            Delete ALL DATA AND APPLICATIONS INSIDE THIS WINEPREFIX
```

**Tip:** As with all Wine commands, winetricks knows about the
`WINEPREFIX` environment variable. This is useful for using winetricks
with different Wine prefix locations. For example,

```sh
$ env WINEPREFIX=~/.winetest sh winetricks mfc40
```

installs the mfc40 package in the `~/.winetest` prefix.

**Tip:** Users with more than one version of Wine on their system (for
example, an installed package and an uninstalled Wine built from git)
can specify which version winetricks should use. For example,

```sh
$ env WINE=~/wine-git/wine sh winetricks mfc40
```

installs the mfc40 package using the Wine in the `~/wine-git` directory.

## Reporting bugs after you have used Winetricks

Please do not report bugs if you have used winetricks to install native
(ie non Wine) files, as we cannot support Microsoft dlls.

Using winetricks to install gecko, mono, and fakeie6 options is
acceptable for bug reports - just be sure to mention that's what you've
done.

Additionally if you found it necessary to use winetricks for an
application please mention it when submitting to the AppDB, mailing
lists, and other Wine resources.

## Reporting bugs **in** Winetricks

Winetricks has a bug tracking system at
<https://github.com/Winetricks/winetricks/issues>, please use it. If you
don't want to get an account there to file a bug, posting on the Wine
user forum may also eventually get noticed.

## How to remove things installed by Winetricks

It's easy to install an entire wineprefix, so by default, winetricks
installs each app into its own Wine prefix, and offers an easy way to
remove wineprefixes and the menu items they created.

Winetricks does not provide a way to uninstall individual apps or DLLs
inside a Wine prefix. This is for several reasons, but mainly because
the preferred way to uninstall anything in Wine is to simply install
into a fresh Wine prefix. (Yes, it would be nice to have uninstallers
for everything, but I don't need it myself. Patches welcome.)

If for some reason, you still don't want to fiddle at all with your Wine
prefixes, Wine does offer a built-in
[Uninstaller](Commands/uninstaller) program. Like the Windows
"Add/Remove Programs" applet though, it only recognizes programs
installed by well-behaved Windows installers that respect the registry,
like InstallShield or WISE. There are no guarantees it will work with a
program installed by Winetricks or other installers like `.msi`
packages.

## Installing winetricks

It's not necessary to install winetricks to use it. You may choose to
install winetricks in a global location so you can just type
`winetricks` on the command line. Some Linux distributions include
winetricks in their Wine packages, so you don't have to download it
separately. You probably do want to follow these steps, if the
distributions packaged winetricks version lags behind the current
winetricks release (e.g. Debian/Ubuntu users).

To download and install your own copy of winetricks, you can install it
manually like this:

```sh
$ cd $HOME/Downloads
$ wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
$ chmod +x winetricks
$ sudo cp winetricks /usr/local/bin
```

To download and install the (separate) BASH completion script for
winetricks:

```sh
$ cd $HOME/Downloads
$ wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks.bash-completion
$ sudo cp winetricks.bash-completion /usr/share/bash-completion/completions/winetricks  # Standard location for BASH completion scripts (Arch, Gentoo, OpenSUSE, Fedora, Debian/Ubuntu, Solus)
```

## See Also

- <https://github.com/Winetricks/winetricks/wiki>
- <https://www.cabextract.org.uk/> -- cabextract is a tool for
  extracting MS cabinet files under Unix environments.
