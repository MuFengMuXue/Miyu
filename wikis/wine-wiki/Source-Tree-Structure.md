Wine was originally organized by topic so each related area of the API
had its own directory. Unfortunately this didn't work out too well as
Windows itself is rather badly organized, especially in the older parts,
so now the Wine source tree is closely based on Windows modules. Most of
the source is concerned with implementing the Wine API, although there
are also various tools, documentation, and code specific to the binary
loader. Note that several of the libraries listed here are "stubbed
out", meaning they still need to be implemented.

## Overall structure

| Directory      | Contents                                                                                                              |
|----------------|-----------------------------------------------------------------------------------------------------------------------|
| dlls/          | Implementations of all native DLLs (kernel32, ntdll, user32, gdiplus, etc). This is the bulk of Wine's code.          |
| documentation/ | Translations of the README.                                                                                           |
| fonts/         | Reimplementations of Windows fonts.                                                                                   |
| include/       | Header files. This closely matches the PSDK.                                                                          |
| libs/          | Source code for static libraries.                                                                                     |
| loader/        | The Wine loader and preloader, and some files which are installed in the initial wineprefix.                          |
| po/            | Translations.                                                                                                         |
| programs/      | Executable programs supplied with Windows, including some Wine-specific programs. See also [Wine Commands](Commands). |
| server/        | The [wineserver](Commands/wineserver).                                                                                |
| tools/         | Native tools used to build Wine.                                                                                      |

## Under dlls/

Each DLL is in its own directory, named after the DLL itself. The ".dll"
extension is omitted, except for 16-bit DLLs. All 16-bit DLLs also have
the suffix "16" appended to them.

### Notes on Core DLLs

A few of the DLLs are particularly central to the Win32 API. As a
result, some extra notes have been included for them:

- **ntdll** : forms the core of the Windows system. It first appeared in
  Windows NT, but didn't become part of the consumer-oriented versions
  of Windows (3.1/95/98/Me) until XP. In Windows, this has become little
  more than a userspace to kernelspace shim, and analogously in Wine,
  it's mostly an interface either to the wineserver or the underlying
  Unix kernel. It also contains things like the PE (EXE/DLL format)
  dynamic linker.

- **kernel32** : mostly just forwards to **ntdll** in NT-based Windows,
  but in Windows 9x, most of the code from **ntdll** is here. The
  thinking behind this split was that NT would be able to support
  multiple modules for different operating system APIs, i.e. there could
  be a POSIX module, an OS/2 module, and **kernel32** would be the Win32
  module. In practice Microsoft wiped out the competition so effectively
  that this abstraction was never really needed or used, so in today's
  NT-based, Windows systems, **kernel32** is mostly just a set of
  forwarders. In Wine, the migration of code from **kernel32** to
  **ntdll** isn't finished yet so we actually have a fairly even split.

- **user32** : userspace code responsible for most of the core windowing
  and messaging, as well as various other random things like the
  clipboard, networking, and a wsprintf implementation. Originally
  **user32** (actually, user.exe) *was* the Windows API, until it grew
  large enough that having multiple DLLs made more sense, thus the
  rather odd and unrelated collection of code in this DLL. Basically,
  the very old mechanisms that date from the Windows 3.1 era are likely
  to be either in this DLL or **kernel32**.

- **ole32**, **rpcrt4** : together implement COM and DCOM.

## Under libs/

Each static library is in its own directory, named after the library
itself. The extension is omitted.

This directory also contains third-party libraries that have been
imported into Wine to enable building them in PE format.

## Under tools/

| Directory        | Contents                                    |
|------------------|---------------------------------------------|
| tools/sfnt2fon/  | the .FON compiler                           |
| tools/widl/      | the IDL compiler                            |
| tools/winapi/    | A Win32 API checker                         |
| tools/winebuild/ | Wine DLL builder                            |
| tools/winedump/  | dumps DLL headers and generates .spec files |
| tools/winegcc/   | a MinGW-compatible gcc wrapper              |
| tools/winemaker  | a Makefile generator for winelib            |
| tools/wmc/       | the message compiler                        |
| tools/wrc/       | the resource compiler                       |

## Under include/

| Directory       | Contents                       |
|-----------------|--------------------------------|
| include/        | Windows standard includes      |
| include/ddk/    | Windows DDK compatible headers |
| include/msvcrt/ | MSVC-compatible libc headers   |
| include/wine/   | Wine-specific headers          |
