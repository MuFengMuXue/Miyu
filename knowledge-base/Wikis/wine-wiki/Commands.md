## Programs

These sub-programs are usually accessible by running:

`wine wineprogram arg1 arg2 ...`

at the shell. For example:

`wine winecfg`

For Wine 1.1.15 and before, executable wrappers were provided for some
of these programs, but as this messed up out-of-tree builds, the
wrappers were removed from Wine 1.1.16. These wrappers allowed you to
type just:

`winecfg`

at the shell (as long as Wine is installed in the user's $PATH).

A complete list of these programs can be found in Wine's source, under
[programs/](https://gitlab.winehq.org/wine/wine/-/tree/master/programs).

- cacls - edit ACLs
- clock - displays a rudimentary clock
- [cmd](Commands/cmd) - Command prompt implementation
- cmdlgtst - (for developers) commdlg.dll test jig
- [control](Commands/control) - Control Panel implementation
- [eject](Commands/eject) - ejects optical discs (note that wine eject
  is different from the normal eject command)
- [expand](Commands/expand) - expands cabinet (.cab) files
- [explorer](Commands/explorer) - explorer.exe implementation
- [hh](Commands/hh) - HTML help (.chm file) viewer
- icinfo - shows installed video compressors for Wine
- iexplore - Internet Explorer implementation
- lodctr - load performance monitor counters
- [msiexec](Commands/msiexec) - msiexec.exe implementation for
  installing .msi files
- net - starts and stops services
- notepad - Notepad, a simple text editor
- oleview - allows browsing and exploring COM objects as well as
  configuring DCOM
- progman - Program Manager implementation
- reg - console-based registry editor
- [regedit](Commands/regedit) - Registry Editor implementation
- regsvr32 - register OLE components in the registry
- rpcss - quasi-implementation of rpcss.exe
- rundll32 - loads a DLL and runs an entry point with the specified
  parameters
- secedit - security configuration edit command
- services - manages services
- spoolsv - print wrapper
- [start](Commands/start) - starts a program or opens a document in
  the program normally used for files with that suffix
- svchost - (internal) host process for services
- taskmgr - Task Manager implementation
- [uninstaller](Commands/uninstaller) - basic program uninstaller
- unlodctr - unload performance monitor counters
- view - metafile viewer
- [wineboot](Commands/wineboot) - "reboots" (restarts) Wine, for when
  Windows apps call for a real reboot
- [winebrowser](Commands/winebrowser) - launches native OS browser or
  mail client
- [winecfg](Commands/winecfg) - GUI configuration tool for Wine
- wineconsole - displays Windows console
- [winedbg](Commands/winedbg) - Wine debugger core
- winedevice - (internal) manages devices
- winefile - file explorer implementation
- [winemenubuilder](Commands/winemenubuilder) - helps to build Unix
  menu entries
- winemine - classic minesweeper game
- [winepath](Commands/winepath) - translates between Windows and Unix
  paths formats
- winetest - all the DLL conformance test programs suitable for
  unattended testing and report submission
- winevdm - Wine virtual DOS program
- [winhelp](Commands/winhelp) - Help viewer
- winhlp32 - Help viewer (32-bit)
- winver - displays an "about Wine" window
- wordpad - wordpad.exe implementation
- write - starts wordpad (for Win16 compatibility)
- xcopy - Wine-compatible xcopy program

## Programs not run with wine

These programs are run directly (i.e. not `wine program`, just
`program`):

- winelauncher - attempts to intelligently manage the process of
  launching a program with Wine
- [wineserver](Commands/wineserver) - daemon process that provides to
  Wine roughly the same services that the Windows kernel provides on
  Windows

## Tools

These tools are a collection of scripts and executables to aid
development of Wine. They are invoked as a standalone command while in
the tools directory (e.g. `~/wine-git/tools/wineinstall`).

A complete list of these commands can be found in Wine's source, under
[tools/](https://gitlab.winehq.org/wine/wine/-/tree/master/tools).

- buildimage - generates bitmap and icon files from SVG files
- config.guess - attempts to guess a canonical system name
- findfunc - attemps to locate a specified Wine program/tool
- install-sh - installs a program, script, or datafile
- makedep - generates makefiles and dependencies prior to building Wine
- make_fir - generates the FIR filter used by dsound
- make_makefiles - updates configure and the Makefile.in files based on
  changes to the source tree
- make_requests - updates the Wine server protocol description files
- make_specfiles - updates the .spec files when something has changed
- make_unicode - rebuild the Unicode tables based on the files from
  unicode.org
- make_xftmpl - generates a binary header from a .x source file
- runtest - wrapper script to run one of the Wine regression tests from
  inside the build tree
- sfnt2fon - converts bitmap-only ttf to Window font files
- wineapploader - wrapper script to start a Winelib application once it
  is installed
- wineinstall - Wine installation script (last updated in 2009; not
  recommended)
- [winemaker](Commands/winemaker) - helps converting Windows sources
  to Winelib programs
