On a lot of systems 3D drivers are missing or not installed correctly.
This prevents OpenGL/Direct3D games from functioning correctly. This
page is meant to assist you with solving common 3D issues. It is not
meant to provide a complete tutorial on how to install lets say
AMD/Nvidia/DRI drivers. We might provide links to where to find this
information for a specific Linux distribution though.

## Investigating 3D performance issues

The primary cause of 3D performance issues in Wine is due to 3D driver
issues. It is not always trivial to find the root of the problem, here
some suggestions are given.

First we are going to check is whether 3D acceleration is working
correctly. If possible try a native 3D program like Google Earth, Quake
3, Unreal Tournament 2004 and if those don't work well, likely because
you don't have OpenGL drivers installed, try to fix those issues first,
before you continue below.

In order to find out what's wrong, we are going to inspect the
GLX/OpenGL information provided by the display driver. Normally you can
obtain this information using the \`glxinfo\` tool. We don't use glxinfo
here, because it can't be used to diagnose 3D issues on 64-bit systems
since Wine relies on 32-bit OpenGL. Instead, we are going to use
diangostic information built into Wine. For this you need a Windows 3D
program (it doesn't matter what) and run it like:

```sh
$ WINEDEBUG=+wgl wine your_3d_app.exe &> wine.log
```

The contents of \`wine.log\` for a working installation, may look like
this and it is similar to glxinfo:

    trace:wgl:X11DRV_WineGL_InitOpenglInfo GL version             : 2.1.2 NVIDIA 169.12.
    trace:wgl:X11DRV_WineGL_InitOpenglInfo GL renderer            : GeForce 8800 GT/PCI/SSE2.
    trace:wgl:X11DRV_WineGL_InitOpenglInfo GLX version            : 1.4.
    trace:wgl:X11DRV_WineGL_InitOpenglInfo Server GLX version     : 1.4.
    trace:wgl:X11DRV_WineGL_InitOpenglInfo Server GLX vendor:     : NVIDIA Corporation.
    trace:wgl:X11DRV_WineGL_InitOpenglInfo Client GLX version     : 1.4.
    trace:wgl:X11DRV_WineGL_InitOpenglInfo Client GLX vendor:     : NVIDIA Corporation.
    trace:wgl:X11DRV_WineGL_InitOpenglInfo Direct rendering enabled: True
    ...

A broken/incomplete install with indirect rendering (this can still mean
that you have some 3D acceleration) could look like this:

    ...
    trace:wgl:X11DRV_WineGL_InitOpenglInfo GL version             : 1.4 (1.5 Mesa 6.5.2)
    trace:wgl:X11DRV_WineGL_InitOpenglInfo GL renderer            : Mesa GLX Indirect
    trace:wgl:X11DRV_WineGL_InitOpenglInfo Direct rendering enabled: False

A broken/incomplete install with pure software rendering could look like
this:

    ...
    trace:wgl:X11DRV_WineGL_InitOpenglInfo GL version             : 2.1 Mesa 7.8-devel
    trace:wgl:X11DRV_WineGL_InitOpenglInfo GL renderer            : Software Rasterizer
    trace:wgl:X11DRV_WineGL_InitOpenglInfo Direct rendering enabled: True

This case occurs when you use a DRI driver, but libGL is not able to
load your dri module (e.g. /usr/lib/dri/i965_dri.so). In such a case
Mesa falls back to software rendering. (It might look weird that direct
rendering is enabled but this is actually correct. The definition of
direct rendering is that rendering is done client side without
interference of X/GLX. OpenGL drivers prefer to bypass X in order to
achieve maximum performance but pure software rendering also bypasses
X.)

In case of a problem like the line 'Direct rendering enabled' showing
False. Consult the support channels provided by your OS and graphics
card manufacture for help getting hardware accelerated GL installed and
working correctly.

For a Radeon card you might get info here: [Use 32-bit GL applications
on 64-bit
systems](https://www.x.org/wiki/radeonBuildHowTo#Use_32-bit_GL_applications_on_64-bit_systems).
