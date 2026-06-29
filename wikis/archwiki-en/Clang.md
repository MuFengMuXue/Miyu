# Clang

Clang is a C/C++/Objective C/CUDA compiler based on LLVM. The most recent iteration is distributed under the "Apache 2.0 License with LLVM exceptions".

## Installation
Install the  package.

## Build packages with Clang
## Generic setup
To change the default compiler for building packages, edit:

To use  as the C++ Standard Library instead of GCC's : install the  package, then add  to  in your .

For LTO support: install the  package, then add  to  in your .

If you are building with , you also need to remove  from  and , as Clang does not support it.

## Qt packages
Qt packages may require extra setup. Qt has predefined build configurations called mkspecs, defaulting to GCC for Linux.

In some cases, the mkspec will be automatically set to  based on / variables.
But in other cases (e.g. packages with direct call of ) it will not, so we can set it explicitly:

## Rust packages
Whenever clang is set as the system default compiler, Rust needs to be configured to use clang as the linker for C code often compiled as a part of the process for building Rust applications.

To do so, clang (and optionally lld) needs to be specified in .

For example, to use clang and lld:

## Using the Static Analyzer
To analyze a project, simply place the word  in front of your build command. For example:
 $ scan-build make

If your project is already compiled,  will not rebuild and will not analyse it. To force recompilation and analysis, use  switch:

 $ scan-build make -B

It is also possible to analyze specific files:

 $ scan-build gcc -c t1.c t2.c

## Tips and tricks
## Bash completion
In order to enable Bash completion, install .

## Troubleshooting
## Stack protector
The  package enables  on default. This practice should not cause any problem for compiling most programs and improve the overall security and robustness with a minimal cost. However, there are situations where the stack protector canary is uninitialized in TLS (for example, when you are implementing the  function on yourself). In such cases, compiling with  may lead to segmentation faults or other unexpected errors. One should be aware of the divergence between the  package and upstream.
