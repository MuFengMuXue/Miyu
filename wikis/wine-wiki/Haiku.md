## Haiku

Haiku is an open source operating system inspired by the Be Operating
System. Haiku is fast, simple to use, easy to learn and yet very
powerful.

Homepage: <https://www.haiku-os.org>

### Wine port

Haiku meanwhile has ported Wine: [github
repo](https://github.com/X547/wine)

It can be installed via HaikuDepot and also includes a Haiku specific
display driver!

For more information see: [My progress in porting Wine by
X512](https://discuss.haiku-os.org/t/my-progress-in-porting-wine)

## What Wine needs from Haiku (as of ~2012)

- in general: LDT support, m(un)lock, pthread_attr_setstack, a fix for
  the Address Space Layout problem
- dbghelp: Elf32_Ehdr, Elf32_Shdr, Elf32_Phdr, Elf32_Dyn, DT_DEBUG,
  DT_NULL, SHT_NULL, SHT_NOBITS, SHT_SYMTAB, SHT_DYNSYM, SHT_DYNAMIC,
  STT_NOTYPE, STT_FILE, STT_OBJECT, STT_FUNC, SHN_UNDEF, STB_LOCAL,
  ELFMAG0, ELFMAG1, ELFMAG2, ELFMAG3, EI_CLASS, ELFCLASS32, ELFCLASS64,
  PT_LOAD
- network related: ESOCKTNOSUPPORT, ETOOMANYREFS
- ntdll: SIGIO, an improved ucontext_t

## See also

- [Thread on haiku-development mailing list from June
  2014](https://www.freelists.org/post/haiku-development/Wine-for-Haiku)

- [Patchseries: configure.ac: fix libpthread detection on
 Haiku](https://www.winehq.org/pipermail/wine-patches/2011-July/104639.html)

- [older
  Patch](https://www.winehq.org/pipermail/wine-patches/2009-September/078726.html)

- ~~[Bug 20116](#20116)~~

- ~~[Bug 4606 at Haiku](https://dev.haiku-os.org/ticket/4606)~~

- [Bug 7502 at Haiku](https://dev.haiku-os.org/ticket/7502) (missing LDT table)

- ~~[Bug 9205 at Haiku](https://dev.haiku-os.org/ticket/9205) (needed mmap improvements)~~

- [Wine on
  HaikuDepot](https://depot.haiku-os.org/#!/pkg/wine_bin/haikuports/haikuports_x86_64/7/5/-/-/1/x86_64)
