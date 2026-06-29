As riscv has a few [ABIs](https://wiki.gentoo.org/wiki/RISC-V_ABIs "RISC-V ABIs") and the multilib story is a bit complicated as well.

Gentoo will use a multilib compatible LIBDIR layout for both multilib and non-multilib profiles.

TODO: add details on what other distros do

## [rv64gc]

This is the 64bit architecture (rv64) with extensions imadfc (i.e., g is a shorthand for imadf). It supports 2 ABIs, lp64 (softfloat) and lp64d (hardfloat double).

The gcc default is

    -march=rv64gc -mabi=lp64d

Our multilib structure follows the guidelines as implemented in GCC:

    # from profiles/arch/riscv/rv64gc/make.defaults

    # Library directories
    LIBDIR_lp64d="lib64/lp64d"
    LIBDIR_lp64="lib64/lp64"
    SYMLINK_LIB="no"

    # Flags for lp64d
    CFLAGS_lp64d="-mabi=lp64d"

    # Flags for lp64
    CFLAGS_lp64="-mabi=lp64"

## [rv32i]

This is the 32-bit architecture, which is not supported by glibc yet (but will be soon), but [rv32ia](https://github.com/riscv-collab/riscv-gnu-toolchain/issues/798) should be already.

## [References]

-   [Per-march and per-mabi Library Paths on RISC-V Systems](https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib)