# Tutorial - Part 1: Getting Started

Index | Tutorial - Part 2: Enumerating Objects

In this tutorial we show the basics of a simple PipeWire application.
Use this tutorial to get started and help you set up your development
environment.

# Initialization

Let get started with the simplest application.

 tutorial1.c code

Before you can use any PipeWire functions, you need to call `pw_init()`.

# Compilation

PipeWire provides a pkg-config file named `libpipewire-0.3` (note: the version
suffix may change with future releases of PipeWire).
To compile the simple test application, copy it into a test1.c file and
use pkg-config to provide the required dependencies:

    gcc -Wall test1.c -o test1 $(pkg-config --cflags --libs libpipewire-0.3)

then run it with:

    # ./test1
    Compiled with libpipewire 0.3.5
    Linked with libpipewire 0.3.5
    #

Use your build system's pkg-config support to integrate it into your project.
For example, a minimal [meson.build](https://mesonbuild.com/) entry would look
like this:

    project('test1', ['c'])
    pipewire_dep = dependency('libpipewire-0.3')
    executable('test1', 'test1.c',
               dependencies: [pipewire_dep])

Index | Tutorial - Part 2: Enumerating Objects
