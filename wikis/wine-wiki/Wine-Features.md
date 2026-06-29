<small>
&nbsp;[:flag_fr: Français](fr/Wine-Features)
</small>

-----

## Binary Compatibility

- Loads 64-bit, 32-bit, 16-bit Windows 9x/NT/2000/XP/Vista/7/8/10 and
  Windows 3.x programs and libraries
- Win32 compatible memory layout, exception handling, threads and
  processes
- Designed for POSIX compatible operatings systems (eg. Linux, macOS and
  FreeBSD) and Android
- "bug-for-bug" compatibility with Windows

## Win32 API support

- Support for DirectX based games and applications (Direct3D support up
  to DirectX 12)
- Support for OpenGL and Vulkan based games and applications
- DirectShow support with use of GStreamer for codecs
- Direct2D, DirectWrite support
- MMDevice API, XAudio, WinMM, DirectSound audio APIs are supported
- Printing via PostScript driver to the host printing system (usually
  CUPS)
- Enhanced Metafile (EMF) and Windows Metafile (WMF) driver
- Desktop-in-a-box or mixable windows

## Allows Windows program to interface with:

- X11-based graphics which allow remote display to any X terminal
- macOS and Android based graphics
- X11, TrueType (.ttf/.ttc) and Windows Bitmap (.fon) fonts
- Sound devices via ALSA, OSS, PulseAudio, Core Audio, etc.
- Multi-lingual keyboards and CJK input method support via XIM
- Modems, serial devices
- Networks (TCP/IP and IPX)
- ASPI Scanners
- Windows Tablets via XInput (eg. Wacom)
- Video capture devices via v4l2
- HID devices via IOHid (MacOS), evdev (Linux), hidraw (Linux), SDL2

## API Coverage and Portability

- Designed for source and binary compatibility with Win32 code
- Win32 API test suite to ensure compatibility
- Compilable on a wide range of C compilers
- Permits mixing of Win32 and POSIX code
- Permits mixing of ELF (.so) and PE (.dll/.exe) binaries in one address
  space
- Win32 compatible header files
- Automatically generated API documentation
- Resource compiler
- Message compiler
- IDL compiler
- Extensive Unicode support
- Internationalization -- Wine supports 50 languages
- Built-in debugger and configurable trace messages
- External memory checker support using Valgrind
- Sample programs
