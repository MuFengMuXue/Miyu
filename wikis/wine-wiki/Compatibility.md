<small>
&nbsp;[:flag_kr: 한국어](ko/Compatibility)
</small>

-----

## Improving Wine's Compatibility

We aim to make Wine compatible with as many systems and configurations
as possible. Whether you want to port Wine to a new architecture or OS,
build it with a different toolchain, or solve some other
platform-specific quirk, we always appreciate the help. These kinds of
improvements tend to provide secondary benefits too, maturing our code
and making it more robust on any platform.

If you're interested, try [Building Wine](Building-Wine) with
your specific configuration, keeping and sharing careful notes of your
results. Don't be shy about letting other
[Developers](Developers) know about your goals and progress
either. There's a good chance that at least one developer has tested the
same configuration some; if so, they can give you a headstart and
possibly point you towards trial patches or bug reports.

To narrow down problems, try varying as few parameters as possible from
our "control" case: vanilla 32-bit Wine, Linux or FreeBSD kernel, x86 or
amd64 arch, GCC / GNU build tools, and Wine header files.

The Clang compiler has come a long way; it can build the 32-bit version
of Wine without problems and could be considered a control in the near
future. However it still lacks a couple features that certain DLLs and
64-bit support depend on (see below for details).

## Different Options

### Operating Systems

| OS               | Compiles?          | Runs?              | Supports 64-bit Wine? | Notes                                                                                                                                  |
|------------------|:------------------:|:------------------:|:---------------------:|----------------------------------------------------------------------------------------------------------------------------------------|
| FreeBSD          | :white_check_mark: | :white_check_mark: | :white_check_mark:    | [FreeBSD wiki's page on Wine](https://wiki.freebsd.org/Wine)                                                                           |
| macOS            | :white_check_mark: | :white_check_mark: | :white_check_mark:    | Also see [MacOS Building](MacOS-Building) for a couple idiosyncrasies                                                                  |
| DragonFlyBSD     | :white_check_mark: | :white_check_mark: | :x:                   | Wine should still mostly work as on FreeBSD                                                                                            |
| Android          | Cross-compiled     | Partially          | ?                     | Still in progress; see [Alexandre Julliard's slides](/media/Wine-on-android-wineconf2014.pdf) from [FOSDEM 2014](WineConf/FOSDEM-2014) |
| NetBSD           | :white_check_mark: | :white_check_mark: | :x:                   | Packaged as recently as Dec 2015                                                                                                       |
| OpenBSD          | :x:                | :x:                | :x:                   | Was packaged before; Wine & OpenBSD code have since drifted apart (irreconcilably for the foreseeable future)                          |
| Cygwin           | Partially          | ?                  | ?                     |                                                                                                                                        |
| GNU [Hurd](Hurd) | :white_check_mark: | :white_check_mark: | :x:                   | See page for details                                                                                                                   |
| [Haiku](Haiku)   | :x:                | :x:                | :x:                   | See page for details                                                                                                                   |
| OpenIndiana      | :x:                | :x:                | :x:                   | No longer supported                                                                                                                    |

### Architectures

| Architecture   | Compiles?          | Runs?              | Notes               |
|----------------|:------------------:|:------------------:|---------------------|
| [ARM](ARM)     | :white_check_mark: | :white_check_mark: |                     |
| [ARM64](ARM64) | :white_check_mark: | :white_check_mark: |                     |
| PowerPC        | :x:                | :x:                | No longer supported |

### Compilers

| Compiler                                            | Finishes building? | Runs correctly?    | Notes                                                                                                                                                                                                 |
|-----------------------------------------------------|:------------------:|:------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Clang](Clang)                                      | :white_check_mark: | :white_check_mark: | Just can't build 64-bit Wine (~~[Bug #8851](https://llvm.org/bugs/show_bug.cgi?id=8851)~~, fixed in Clang v3.7.1) or expose certain APIs ([Bug #10212]("https://llvm.org/bugs/show_bug.cgi?id=10212)) |
| [icc](https://software.intel.com/en-us/c-compilers) | :x:                | :x:                | Hasn't been tested in a while; building required some workarounds                                                                                                                                     |

## Risky Bitness

In theory, 32-bit programs should run exactly the same, whether you're
using a vanilla 32-bit build of Wine or a WoW64-capable version.
Unfortunately, we still can't guarantee this is always the case. If you
come across a program that behaves differently between the two builds,
don't hesitate to file a bug mentioning the discrepancy in detail.

The [AMD64](AMD64) page has more ideas about testing for
these differences. There are also useful tips for anyone interested in
getting Wine to work on their favorite OS and AMD64 hardware.

## Legacy Systems

The Wine project has been around in one form or another for over 30
years now. In that time, systems have come and gone, but some of them
are still used in niche situations or maintained by dedicated users.
Here is a list of some systems wine was at least tested on in the past.

### Older Compilers

- Open64 (it and most of its derivatives have been discontinued; there
  are still 1 or 2 small forks like
  [OpenUH](https://web.cs.uh.edu/~openuh/) by universities though)
- MinGW/MSYS (project is still active but struggles to stay up-to-date;
  consider using [mingw-w64](https://mingw-w64.org/doku.php) instead)

### Platforms

- [SCO OpenServer](https://en.wikipedia.org/wiki/SCO_OpenServer) 5
  (based on AT&T SysV Release 3)
- [AT&T SysV Release 4](https://en.wikipedia.org/wiki/UNIX_System_V)
- SCO OpenServer 6 (based on AT&T SysV Release 5)
- Sun Solaris & OpenSolaris (superseded by FOSS OpenIndiana & commercial
  Oracle Solaris)

### Architectures

- [IA-64](https://en.wikipedia.org/wiki/IA-64) (aka Itanium) support was
  never implemented
- [Alpha](https://en.wikipedia.org/wiki/DEC_Alpha) support was
  completely removed in Wine v1.3.19
- [SPARC](https://en.wikipedia.org/wiki/SPARC) support was completely
  removed in Wine v1.5.26
- Supposedly, [someone was able to get wine-mine
  running](https://www.mail-archive.com/wine-devel@winehq.com/msg04305.html)
  on an [IBM s/390](https://en.wikipedia.org/wiki/IBM_ESA/390) a while
  back

## See Also

- [Buildroot](Buildroot)
