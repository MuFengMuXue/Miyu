:warning: **This page is about disassembling third-party
applications. Never disassemble Microsoft DLLs or programs!**

## Caveats

Although at first, disassembly and decompilation may seem like very
useful techniques for Wine developers to use, they should probably only
be seen as a last resort for a few different reasons. The purely
practical reason is that in most cases, compilation strips and optimizes
away much of what makes the original source code easy for a human to
understand. It often requires a lot of analysis, work, and skill just to
have a reasonable guess at what a bit of diassembled code is doing.
Other debugging techniques will usually allow you to narrow down your
problem faster and more clearly. This is especially true for native
Windows DLLs, where disassembly is almost always useless (in addition to
bringing up the issue below).

The other problem is more legal in nature. Because Wine is very strict
about [Clean Room Guidelines](Clean-Room-Guidelines), in
order to keep from violating any Microsoft copyrights, any contamination
of the "cleanroom" by a developer puts the whole project at risk. While
this shouldn't be an issue so long as you are only disassembling a
third-party application, even briefly studying disassembled Microsoft
code for a feature that Wine plans to implement could lead to legal
trouble. While in theory it is still possible for someone that has
disassembled Microsoft code to *document* what the code does generally,
in their own words, this can become a legal grey area. If in doubt about
whether you might violate the [Clean Room
Guidelines](Clean-Room-Guidelines), or if you think you may
but would still like to help the project somehow, please ask on the
[Wine developer's mailing
list](https://list.winehq.org/mailman3/postorius/lists/wine-devel.winehq.org/).

**Do not try submitting disassembled or decompiled code to the
project.** It's been tried before, it didn't work then, it won't work
now, and the developers know disassembled code when they see it. Not
only will your patch not be accepted, but your reputation will be
permanently tarnished, and you probably will not be allowed to
contribute to Wine again.

## Tools

- **objdump**, part of GNU binutils, is a useful free tool for
  disassembling binaries of many types. It is capable of reading MZ
  (16-bit DOS), PE (32-bit) and PE+ (64-bit) binaries as well as native
  ELF binaries, and is often already installed on Linux distributions.
  It does not support NE (16-bit protected mode) binaries.
- **[winedbg](Commands/winedbg)**, Wine's own debugger, can be used in
  typical fashion to dump specific sequences of instructions. Use the
  command 'disas' in non-GDB mode, or 'x/i' in GDB mode.
- **[semblance](https://github.com/zfigura/semblance)** is a free tool,
  written in the absence of any other tool capable of dumping 16-bit
  (NE) code. It supports MZ, NE, PE, and PE+ binaries.

## Starting Tips

When working backwards from a particular address try and choose aligned
addresses, otherwise you risk starting the disassembly from the middle
of an instruction which will produce garbage. Also, if you aren't
already familiar with [x86
assembly](https://en.wikipedia.org/wiki/X86_assembly_language), you might
consider practicing by using the disassembler in
[gdb](https://www.gnu.org/software/gdb/) on ELF binaries that you've
compiled yourself, then going back and comparing the disassembled code
to the original source code. The Intel instruction set is vast, but very
few instructions are used frequently. If you know what to expect, you
won't be tripped up by bad disassembles or anti-disassembly tricks which
can corrupt the output.

There are a few common patterns that you especially might want to look
for:

- Code which moves values into **0x0(%fs)** is probably setting up an
  SEH handler frame.

- The return code of a function is stored in **%eax** on all calling
  conventions used in Windows, so if you see a function call followed by
  a check against this register, you're very likely to be seeing a check
  for an error code.

- Call instructions which dereference a value, such as
  `call *0x12345678` are usually calls into other DLLs (often API
  calls). Winedbg should be able to show you which API the call
  instruction is invoking. Also keep in mind that instruction sequences
  that move a value into a register from the stack and then dereference
  it in a call instruction could well be COM method invocations.

- C++ applications compiled using Microsoft Visual C++ (the most popular
  C++ compiler on Windows) use the "thiscall" calling convention, in
  which the instance pointer is stored in **%ecx**. If you get a crash
  dereferencing the value of **%ecx** in a C++ program, you might be
  seeing a null pointer dereference on an object instance. This is
  especially likely if the offset is quite large, i.e. a crash accessing
  **0x36** is a pretty good indication that it's a C++ object and not
  just a very large C struct.

- Optimizing compilers do a lot of interesting things, such as
  rearranging instructions to better match the internal scheduling
  algorithms on superscalar processors. This can seriously obfuscate the
  assembly stream, so don't be at all surprised if you find it hard to
  read. A common trick is to use `xorl %eax, %eax` to clear the **%eax**
  register rather than the more intuitive `movl $0, %eax`. Why? Because
  the instruction is smaller, so it takes less space, so it uses the CPU
  cache more effectively.

## See also

- [Clean Room Guidelines](Clean-Room-Guidelines)
