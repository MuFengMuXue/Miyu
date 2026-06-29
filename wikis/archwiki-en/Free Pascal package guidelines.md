# Free Pascal package guidelines

This page explains on how to write PKGBUILDs for software built with the Free Pascal Compiler (FPC). Compiling for x86_64 Arch Linux requires the  package.

## Free Pascal
## Package naming
The project name alone is usually sufficient. However, in the case of cross-compiling, the package should be prefixed with  when targeting i686 Linux from multilib and named in the format of  when targeting non-Arch Linux systems.

## Helpful snippets
Determine FPC's version and the CPU and OS of the units to output:

 _unitdir=`fpc -iSP`-`fpc -iSO`
 _fpcver=`fpc -iV`

## Packaging
Please adhere to the following when making an FPC-based package:

* always add  to either  or
* always put all compiled units (*.a, *.compiled, *.o, *.ppu, *.res, *.rsj) under
* add  to  if installing an import library

## Cross compiling
* always add the corresponding cross compiler package mentioned above () to
* always add  to  for non-Unix-based systems
* always put all compiled units (*.a, *.compiled, *.o, *.ppu, *.res, *.rsj) under  (or if multilib, )
* always use  ( if multilib) as the architecture
* add  to  if installing an import library
