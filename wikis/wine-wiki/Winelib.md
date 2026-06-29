# Winelib

*Motto: The journey of a thousand miles starts with a single step.*

# Introduction

Theoretically, any Win32 app should be compilable out of the box under
Wine. This, of course, is not the case. We have incompatible headers,
and a bunch of other problems described in [Winelib User's
Guide](Winelib-User's-Guide). A good way to fix these is to
try to compile applications for which we have the source under Winelib.

## Why

But what do we hope to achieve? Well, the purpose of this project is
four-fold:

- Document our experience on porting these applications to Winelib
- Improve Winelib based on the above such that the porting process
  becomes very simple
- Update the [Winelib User's Guide](Winelib-User's-Guide) to
  the latest porting process
- Fixing header and library problems in the process.

## Where

There are many such apps around, and a lot of them are hosted at
[SourceForge](https://sourceforge.net/). There are over [10,000
apps](https://sourceforge.net/directory/os:windows/) listed as running
under Windows OS. All of the above have publicly available source code,
and most are decent candidates for this project.

Obviously, we cannot start porting all these applications. We have to
pick a few important ones, and work with those.

## How

Compiling apps under Winelib should theoretically involve only makefile
changes. In practice, you will encounter header problems, and the likes
-- for these it is much better (and faster) to submit a patch, rather
than document them. So for the remainder of the section, let's assume
the Wine headers are good enough for the application in question.

We are now faced with adapting the build process to Wine's needs. As
things stand today, we have to make another assumption: you aim at
compiling the application using the GNU toolchain (gmake, gcc, ld,
etc.). In theory, it should be possible to accomplish this with other
tools, but at this point this is a rather unexplored territory. That
being said, we now distinguish two large application classes:

**Non-GNU tools build process**

For these, winemaker does a decent job of generating a build system. I
will not cover this type of applications here, for the time being.
Please refer to the winemaker [documentation](Commands/winemaker) for
more information.

**GNU tools based build process**

Fortunately, most OSS applications have a build system based around the
[MinGW](https://www.mingw.org/) tool chain. Sometimes they have
alternative build systems for the Borland and/or Microsoft tools, but
more often than not they have to support the MinGW tools out of
necessity.

## What

If you know of an application that could be listed here, please add it.

# Suggestions & Successes

Here is a list of programs that have been suggested for porting or
already ported with Winelib

## Suggested, No Active Worker

- [CD-DA X-Tractor](https://xtractor.sourceforge.net/)
- [CDex](https://cdexos.sourceforge.net/)
- [DX SDK Examples](https://github.com/walbourn/directx-sdk-samples)
- [Easy Code](https://www.easycode.cat/English/index.htm)
- [Gimp](https://www.gimp.org/)
- [LibreOffice](https://www.libreoffice.org/)
- [Ultimate++](https://upp.sourceforge.net/)
- [VirtualDub](https://www.virtualdub.org/)

## In Progress

- ATL
- [Firefox](https://www.mozilla.org/en-US/firefox/fx/)
- [TeXnicCenter](https://www.texniccenter.org/)
- [WinAMP](https://www.wasabidev.org/)

## Mostly Works

- MFC
- [AbiWord](https://www.abisource.com/)
- [CoolPlayer](https://coolplayer.sourceforge.net/)
- [GNU Winboard](https://www.tim-mann.org/xboard.html)
- [WinVi](https://www.winvi.de)

## Done

- [Petzold's Examples](https://www.computersciencelab.com/Petzold.htm)
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [Visual MinGW](https://visual-mingw.sourceforge.net/)
