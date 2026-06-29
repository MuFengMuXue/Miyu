# ARM64 support

### Status

- Yes, It works! (TM)
- Backtraces work
- WOW64 setup works now
- Stubs
- Relay tracing

### Todo

- [wine-gecko](Gecko)/[wine-mono](Wine-Mono) ARM64 port.

### ABI Problems

As of now, we found two ABI incompatibilities:

- ~~[Bug 38780 (X18 needs to be preserved)](#38780)~~
- ~~[Bug 38886 (variable arguments ABI)](#38886)~~

### How to help

- Report bugs with winelib or Windows applications.

### Compiling

In the likely case that you don't own ARM64 Hardware at the moment, have
a look at [Linaro Engineering: ARMv8
activity](https://www.linaro.org/engineering/armv8)/[downloads](https://www.linaro.org/downloads),

there you get a cross-toolchain, a bootable system and instruction on
how to get the Foundation Model from ARM. (qemu should also work, but i
haven't had much success with it yet) For the start run configure like:

`../configure --host=aarch64-linux-gnu host_alias=aarch64-linux-gnu --with-wine-tools=../yourotherbuilddir/ --without-freetype --without-x --enable-win64`

### Running Windows arm64 Applications

The SDK for win10 includes some PEs for arm64, have a look at ~~bug #38714~~.

You may run into ABI problems described above.

### Running Windows/x86 Applications

See [Emulation](Emulation)

### See also

- AArch32: [ARM](ARM)

- [Discussion on linux-arch mailing
  list](https://marc.info/?t=135820649100003&r=1&w=2)
