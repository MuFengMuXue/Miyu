Alongside their original line of Single Board Computers, the Raspberry Pi Foundation also produce the Pico series of boards based around their [RP2040 and RP2350 microcontrollers](https://www.raspberrypi.com/documentation/microcontrollers/). The RP2040 features two Arm cores, and the RP2350 can be selected to use either two Arm cores or two RISC-V cores. Development for these microcontrollers is supported on Gentoo using [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev"), the Pico-SDK and your editor/IDE of choice. There is also a toolchain installer script and official VS Code plugin which are detailed in the [Pi Pico getting started guide](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf) if you do not wish to manage the compiler through portage.

\

## [Building a toolchain with Crossdev]

You will need at least one of the following toolchain targets:

  ----------------------- --------------- ------------------------------
  Microcontroller/Board   Arm Target      Risc-V Target
  RP2040 / Pi Pico        arm-none-eabi   N/A
  RP2350 / Pi Pico 2      arm-none-eabi   riscv32imac-unknown-none-elf
  ----------------------- --------------- ------------------------------

Installation of the toolchain is done using [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") in the standard way. Crossdev will require a suitable local portage repo to create the cross compiler ebuilds in, for which [Eselect/Repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") can be used.

`root `[`#`]` emerge --ask app-eselect/eselect-repository sys-devel/crossdev `

`root `[`#`]` eselect repository create crossdev-$ `

`root `[`#`]` crossdev --target $ `