# NAME

winetricks - manage virtual Windows environments using Wine

# SYNOPSIS

**winetricks ** \[options\] \[verb ... \]

# DESCRIPTION

**winetricks** is an easy way to work around common problems in Wine.

It provides simple commands to tweak Wine settings, download and install missing Windows DLLs and fonts, or install various applications with appropriate workarounds for the current version of Wine.

It can be used via GUI or command line. The command-line mode is intended both for interactive use and as a building block in fancier Wine frontends and in automated regression testing.

**winetricks** with no arguments displays a GUI using either Zenity or Kdialog.

# OPTIONS

**--country=CC**
Set country code to CC and don't detect your IP address when retrying downloads

**-f, --force**
Don't check whether packages were already installed

**--gui**
Show GUI diagnostics even when driven by the command-line interface

**--gui=OPT**
Set OPT to kdialog or zenity to override GUI engine

**--isolate**
Install each app or game in its own bottle

**--self-update**
Update this application to the last version

**--update-rollback**
Rollback the last self update

**--no-isolate**
Don't install each app or game in its own bottle (default)

**--no-clean**
Don't delete temp directories (useful during debugging)

**--optin**
Opt in to reporting which verbs you use to the Winetricks maintainers

**--optout**
Opt out of reporting which verbs you use to the Winetricks maintainers

**-q, --unattended**
Don't ask any questions, just install automatically

**-t, --torify**
Run downloads under torify, if available

**-v, --verbose**
Echo all commands as they are executed

**--verify**
Run (automated) GUI tests for verbs, if available

**-h, --help**
Display this message and exit

**-V, --version**
Display version and exit

# COMMANDS

**apps list**
list verbs in category 'applications'

**benchmarks list**
list verbs in category 'benchmarks'

**dlls list**
list verbs in category 'dlls'

**fonts list**
list verbs in category 'fonts'

**settings list**
list verbs in category 'settings'

**list**
list categories

**list-cached**
list cached-and-ready-to-install verbs

**list-download**
list verbs which download automatically

**list-manual-download**
list verbs which download with some help from the user

**list-installed**
list already-installed verbs

**arch=32\|64**
create wineprefix with 32 or 64 bit, this option must be given before prefix=foobar and will not work in case of the default wineprefix.

**prefix=foobar**
select WINEPREFIX=\$HOME/.local/share/wineprefixes/foobar

**annihilate**
Delete ALL DATA AND APPLICATIONS INSIDE THIS WINEPREFIX

# EXAMPLES

To see list of available packages to install:
winetricks list-download

To install a package:
winetricks 7zip

# ENVIRONMENT VARIABLES

Wine checks several environment variables on startup:

*WINE*
If set, this specifies which wine binary to use by default

*WINESERVER*
If set, this specifies which wineserver to use by default

*WINEPREFIX*
If set, this specifies the location of the default .wine directory ( usually *\$HOME/.wine* ).

*XDG_CACHE_HOME*
If set, this is path to system's user data cache (default: \$HOME/.cache) *W_CACHE* path to Winetricks' user data cache (default: \$XDG_CACHE_HOME/winetricks}
