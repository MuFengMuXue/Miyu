# OpenGL ES

Mesa implements OpenGL ES 1.1, 2.0, 3.0, 3.1 and 3.2, although some drivers
may expose lower limited set. More information about OpenGL ES can be found at
https://www.khronos.org/opengles/.

OpenGL ES depends on a working EGL implementation. Please refer to
Mesa EGL for more information about EGL.

## Build the Libraries

1. Run `meson configure` with `-D gles1=enabled -D gles2=enabled` and
   enable the Gallium driver for your hardware.
1. Build and install Mesa as usual.

This will install libGLESv1_CM, libGLESv2, libEGL, and one or
more EGL drivers for your hardware.

## Run the Demos

There are some demos in `mesa/demos` repository.
