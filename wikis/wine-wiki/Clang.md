[Clang](https://clang.llvm.org/) is a compiler front end
for the C, C++, and Objective-C programming languages, using the Low
Level Virtual Machine (LLVM) as its back end. The goal is to offer a
replacement to the GNU Compiler Collection (GCC) software stack.

To compile wine with Clang, use:

``` bash
#!/bin/bash
export CC=clang
export CXX=clang
./configure
make
```

## Current Status

Using Wine 1.8 and Clang 3.7.0, the Wine code was built successfully. As
Clang is developing fast, it's recommended to use new releases.

## Known bugs

| Bug                                           | Wine bug url | clang bug url                                                  |
|-----------------------------------------------|--------------|----------------------------------------------------------------|
| Can't build wine in 64-bit mode               | n/a          | <https://llvm.org/bugs/show_bug.cgi?id=8851> (resolved fixed)  |
| Clang doesn't support ms_hook_prologue        | n/a          | <https://llvm.org/bugs/show_bug.cgi?id=10212>                  |
| Dragonegg fails to compile loader/preloader.c | #28050       | <https://llvm.org/bugs/show_bug.cgi?id=11173> (resolved fixed) |

## Static analyzer bugs

- [static analyzer + wine = Assertion \`Loc.isMacroID() && "Not a macro
  expansion loc!"' failed
  (1/3)](https://llvm.org/bugs/show_bug.cgi?id=14633)
- [static analyzer + wine = 'Assertion \`T-\>isIntegerType() ||
  Loc::isLocType(T)' failed'
  (2/3)](https://llvm.org/bugs/show_bug.cgi?id=14634)
- [static analyzer + wine = 'Assertion \`isa<X>(Val) && "cast<Ty>()
  argument of incompatible type!'
  (3/3)](https://llvm.org/bugs/show_bug.cgi?id=14635)

## See also

- [StaticAnalysis - Using the Clang Static
  Analyzer](StaticAnalysis#clang)
- [Bugs found using
  Clang/LLVM](https://gitlab.winehq.org/wine/wine/-/commits/master?search=clang)
- [Clang meta-bug for Wine](https://llvm.org/bugs/show_bug.cgi?id=10638)
- [Dragonegg meta-bug for
  Wine](https://llvm.org/bugs/show_bug.cgi?id=10682)
