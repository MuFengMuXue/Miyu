# SDL

From Wikipedia:

:SDL (Simple DirectMedia Layer) is a cross-platform software development library designed to provide a hardware abstraction layer for computer multimedia hardware components. Software developers can use it to write high-performance computer games and other multimedia applications that can run on many operating systems such as Android, iOS, Linux, macOS, and Windows. SDL manages video, audio, input devices, CD-ROM, threads, shared object loading, networking and timers. For 3D graphics, it can handle an OpenGL, Vulkan, Metal, or Direct3D11 (older Direct3D version 9 is also supported) context. A common misconception is that SDL is a game engine. However, the library is suited to building games directly, or is usable indirectly by engines built on top of it.

## Installation
Install the  package for the latest major version of SDL, SDL3. Binary releases for the official additional modules are still in progress; see this search query for the current status.

For SDL2 applications, the  compatibility layer is recommended as it uses SDL3 behind the scenes and will benefit from updates. SDL2 proper, from , is also an option. Additional SDL2 modules are: , , and .

For SDL 1.2 applications, you can install the  compatibility layer. Additional SDL 1.2 modules are: , , .

## Configuration
SDL allows the application and user to specify "hints" to alter (usually platform-specific) functionality. See SDL3 hint documentation, SDL2 hint documentation.

For specific considerations, see Wayland#SDL and HiDPI#SDL.

## Documentation
The official SDL3 Wiki provides the most essential resources to learn and utilize SDL3. Additionally, SDL3 Examples has a selection of small sample programs.
