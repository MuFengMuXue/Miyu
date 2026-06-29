riscv has quite a few ABIs, this page will describe their properties: pointer sizes, compatibility, gcc flags, default linker path.

RISC-V has two integer ABIs and three floating-point ABIs, which can essentially be combined at will. Code generation is controlled by the `-mabi` argument to compiler calls, which concatenates the integer and floating point ABI name.

Example: `-mabi=ilp32d`

The choice of ABI places requirements on the instruction set supported by the hardware and emitted by the compiler.

TODO:

[ **Todo:**]

-   add details.

\

## Contents

-   [[1] [Integer ABIs]](#Integer_ABIs)
    -   [[1.1] [ilp32]](#ilp32)
    -   [[1.2] [lp64]](#lp64)
-   [[2] [Floating Point ABIs]](#Floating_Point_ABIs)
    -   [[2.1] [\"\" (empty string)]](#.22.22_.28empty_string.29)
    -   [[2.2] [f]](#f)
    -   [[2.3] [d]](#d)
-   [[3] [References]](#References)

## [Integer ABIs]

### [ilp32]

-   int, long, pointers are 32bit
-   long long is 64bit
-   char is 8bit
-   short is 16bit

ilp32 is currently only supported for 32-bit targets.

### [lp64]

-   int is 32bit
-   long and pointers are 64bit
-   long long is 64bit
-   char is 8bit
-   short is 16bit

lp64 is only supported for 64-bit targets.

## [Floating Point ABIs]

### [][\"\" (empty string)]

-   No floating point arguments are passed in registers.
-   No requirements on instruction set / hardware.

### [f]

-   32bit and smaller floating point types are passed in registers.
-   Requires F type floating point registers and instructions.

### [d]

-   64bit and smaller floating point types are passed in registers.
-   Requires D type floating point registers and instructions.

\

## [References]

-   [The -march, -mabi, and -mtune arguments to RISC-V Compilers](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)