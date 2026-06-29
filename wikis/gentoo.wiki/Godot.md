[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Godot&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://godotengine.org/)

[[]][Official documentation](https://docs.godotengine.org/en/stable/)

[[]][Package information](https://packages.gentoo.org/packages/dev-games/godot)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Wikipedia_page_title "wikipedia:Wikipedia page title")

[[]][GitHub](https://github.com/godotengine/godot)

Godot is an open-source game engine. Godot enables the user to write cross-platform 2D and 3D from an unified interface, without having to reinvent the wheel.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Wayland native mode]](#Wayland_native_mode)
    -   [[2.2] [On a tiling window manager]](#On_a_tiling_window_manager)
    -   [[2.3] [Invocation]](#Invocation)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Pop-up windows behave strangely]](#Pop-up_windows_behave_strangely)
-   [[4] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [dev-games/godot](https://packages.gentoo.org/packages/dev-games/godot) [[]] [Multi-platform 2D and 3D game engine with a feature-rich editor]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+dbus`](https://packages.gentoo.org/useflags/+dbus)                         Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`+fontconfig`](https://packages.gentoo.org/useflags/+fontconfig)             Support for configuring and customizing font access via media-libs/fontconfig
  [`+gui`](https://packages.gentoo.org/useflags/+gui)                           Enable support for a graphical user interface
  [`+sdl`](https://packages.gentoo.org/useflags/+sdl)                           Add support for Simple Direct Layer (media library)
  [`+theora`](https://packages.gentoo.org/useflags/+theora)                     Add support for the Theora Video Compression Codec
  [`+tools`](https://packages.gentoo.org/useflags/+tools)                       Enable the Godot Editor for game development
  [`+udev`](https://packages.gentoo.org/useflags/+udev)                         Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`+upnp`](https://packages.gentoo.org/useflags/+upnp)                         Enable UPnP port mapping support
  [`+vulkan`](https://packages.gentoo.org/useflags/+vulkan)                     Add support for 3D graphics and computing via the Vulkan cross-platform API
  [`+webp`](https://packages.gentoo.org/useflags/+webp)                         Add support for the WebP image format
  [`accessibility`](https://packages.gentoo.org/useflags/accessibility)         Add support for accessibility (eg \'at-spi\' library)
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                           Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`debug`](https://packages.gentoo.org/useflags/debug)                         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`deprecated`](https://packages.gentoo.org/useflags/deprecated)               Enable support for deprecated features
  [`double-precision`](https://packages.gentoo.org/useflags/double-precision)   Use double-precision floats (default: single-precision)
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)               Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`raycast`](https://packages.gentoo.org/useflags/raycast)                     Enable the raycast Editor module using media-libs/embree
  [`speech`](https://packages.gentoo.org/useflags/speech)                       Enable text-to-speech support
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                     Enable dev-libs/wayland backend
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 07:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-games/godot`

## [Usage]

To run Godot without any options:

`user `[`$`]`godot`

### [Wayland native mode]

** Important**\
Godot does not always run perfectly on Wayland. On Wayland and Xwayland issues may arise such as, broken UI and crashes. If the user experiences problems, refer to [Pop-up windows behave strangely](#Pop-up_windows_behave_strangely).

Since Godot version 4.3 Wayland is natively supported, but not the default.^[\[1\]](#cite_note-1)^ To run Godot in native Wayland mode:

`user `[`$`]`godot --display-driver wayland`

### [On a tiling window manager]

If Godot runs on a window manager without any floating capabilities, then pop-op windows (which are heavily used in Godot) will not behave correctly.

This can be fixed by running Godot in single-window mode:

`user `[`$`]`godot --single-window`

### [Invocation]

`user `[`$`]`godot --help`

[\ ]

Godot Engine v4.5.1.stable.gentoo.f62fdbde1 - [https://godotengine.org](https://godotengine.org) Free and open source software under the terms of the MIT license. (c) 2014-present Godot Engine contributors. (c) 2007-present Juan Linietsky, Ariel Manzur.

Usage:

     godot [options] [path to "project.godot" file]

Option legend (this build = editor):

     R  Available in editor builds, debug export templates and release export templates.
     D  Available in editor builds and debug export templates only.
     E  Only available in editor builds.

General options:

     -h, --help                        R  Display this help message.
     --version                         R  Display the version string.
     -v, --verbose                     R  Use verbose stdout mode.
     --quiet                           R  Quiet mode, silences stdout messages. Errors are still displayed.
     --no-header                       R  Do not print engine version and rendering method header on startup.

Run options:

     --, ++                            R  Separator for user-provided arguments. Following arguments are not used by the engine, but can be read from `OS.get_cmdline_user_args()`.
     -e, --editor                      E  Start the editor instead of running the scene.
     -p, --project-manager             E  Start the project manager, even if a project is auto-detected.
     --recovery-mode                   E  Start the editor in recovery mode, which disables features that can typically cause startup crashes, such as tool scripts, editor plugins, GDExtension addons, and others.
     --debug-server <uri>              E  Start the editor debug server (://<host/IP>[:port], e.g. tcp://127.0.0.1:6007)
     --dap-port                  E  Use the specified port for the GDScript Debug Adapter Protocol. Recommended port range [1024, 49151].
     --lsp-port                  E  Use the specified port for the GDScript Language Server Protocol. Recommended port range [1024, 49151].
     --quit                            R  Quit after the first iteration.
     --quit-after <int>                R  Quit after the given number of iterations. Set to 0 to disable.
     -l, --language <locale>           R  Use a specific locale (<locale> being a two-letter code).
     --path <directory>                R  Path to a project (<directory> must contain a "project.godot" file).
     --scene                     R  Path or UID of a scene in the project that should be started.
     -u, --upwards                     R  Scan folders upwards for project.godot file.
     --main-pack <file>                R  Path to a pack (.pck) file to load.
     --render-thread <mode>            R  Render thread mode ("safe", "separate").
     --remote-fs <address>             R  Remote filesystem (<host/IP>[:] address).
     --remote-fs-password    R  Password for remote filesystem.
     --audio-driver <driver>           R  Audio driver ["PulseAudio", "Dummy"].
     --display-driver <driver>         R  Display driver (and rendering driver) ["x11" ("vulkan", "opengl3", "opengl3_es", "dummy"), "wayland" ("vulkan", "opengl3", "opengl3_es", "dummy"), "headless" ("dummy")].
     --audio-output-latency <ms>       R  Override audio output latency in milliseconds (default is 15 ms).
                                          Lower values make sound playback more reactive but increase CPU usage, and may result in audio cracking if the CPU can't keep up.
     --rendering-method <renderer>     R  Renderer name. Requires driver support.
     --rendering-driver <driver>       R  Rendering driver (depends on display driver).
     --gpu-index <device_index>        R  Use a specific GPU (run with --verbose to get a list of available devices).
     --text-driver <driver>            R  Text driver (used for font rendering, bidirectional support and shaping).
     --tablet-driver <driver>          R  Pen tablet input driver.
     --headless                        R  Enable headless mode (--display-driver headless --audio-driver Dummy). Useful for servers and with --script.
     --log-file <file>                 R  Write output/error log to the specified path instead of the default location defined by the project.
                                          <file> path should be absolute or relative to the project directory.
     --write-movie <file>              R  Write a video to the specified path (usually with .avi or .png extension).
                                          --fixed-fps is forced when enabled, but it can be used to change movie FPS.
                                          --disable-vsync can speed up movie writing but makes interaction more difficult.
                                          --quit-after can be used to specify the number of frames to write.

Display options:

     -f, --fullscreen                  R  Request fullscreen mode.
     -m, --maximized                   R  Request a maximized window.
     -w, --windowed                    R  Request windowed mode.
     -t, --always-on-top               R  Request an always-on-top window.
     --resolution <W>x<H>              R  Request window resolution.
     --position <X>,<Y>                R  Request window position.
     --screen <N>                      R  Request window screen.
     --single-window                   R  Use a single window (no separate subwindows).
     --xr-mode <mode>                  R  Select XR (Extended Reality) mode ["default", "off", "on"].
     --wid <window_id>                 R  Request parented to window.
     --accessibility <mode>            R  Select accessibility mode ['auto' (when screen reader is running, default), 'always', 'disabled'].

Debug options:

     -d, --debug                       R  Debug (local stdout debugger).
     -b, --breakpoints                 R  Breakpoint list as source::line comma-separated pairs, no spaces (use %%20 instead).
     --ignore-error-breaks             R  If debugger is connected, prevents sending error breakpoints.
     --profiling                       R  Enable profiling in the script debugger.
     --gpu-profile                     R  Show a GPU profile of the tasks that took the most time during frame rendering.
     --gpu-validation                  R  Enable graphics API validation layers for debugging.
     --gpu-abort                       D  Abort on graphics API usage errors (usually validation layer errors). May help see the problem if your system freezes.
     --generate-spirv-debug-info       R  Generate SPIR-V debug information. This allows source-level shader debugging with RenderDoc.
     --extra-gpu-memory-tracking       R  Enables additional memory tracking (see class reference for `RenderingDevice.get_driver_and_device_memory_report()` and linked methods). Currently only implemented for Vulkan. Enabling this feature may cause crashes on some systems due to buggy drivers or bugs in the Vulkan Loader. See https://github.com/godotengine/godot/issues/95967
     --accurate-breadcrumbs            R  Force barriers between breadcrumbs. Useful for narrowing down a command causing GPU resets. Currently only implemented for Vulkan.
     --remote-debug <uri>              R  Remote debug (://<host/IP>[:], e.g. tcp://127.0.0.1:6007).
     --single-threaded-scene           R  Force scene tree to run in single-threaded mode. Sub-thread groups are disabled and run on the main thread.
     --debug-collisions                D  Show collision shapes when running the scene.
     --debug-paths                     D  Show path lines when running the scene.
     --debug-navigation                D  Show navigation polygons when running the scene.
     --debug-avoidance                 D  Show navigation avoidance debug visuals when running the scene.
     --debug-stringnames               D  Print all StringName allocations to stdout when the engine quits.
     --debug-canvas-item-redraw        D  Display a rectangle each time a canvas item requests a redraw (useful to troubleshoot low processor mode).
     --max-fps <fps>                   R  Set a maximum number of frames per second rendered (can be used to limit power usage). A value of 0 results in unlimited framerate.
     --frame-delay <ms>                R  Simulate high CPU load (delay each frame by <ms> milliseconds). Do not use as a FPS limiter; use --max-fps instead.
     --time-scale <scale>              R  Force time scale (higher values are faster, 1.0 is normal speed).
     --disable-vsync                   R  Forces disabling of vertical synchronization, even if enabled in the project settings. Does not override driver-level V-Sync enforcement.
     --disable-render-loop             R  Disable render loop so rendering only occurs when called explicitly from script.
     --disable-crash-handler           R  Disable crash handler when supported by the platform code.
     --fixed-fps <fps>                 R  Force a fixed number of frames per second. This setting disables real-time synchronization.
     --delta-smoothing <enable>        R  Enable or disable frame delta smoothing ["enable", "disable"].
     --print-fps                       R  Print the frames per second to the stdout.
     --editor-pseudolocalization       E  Enable pseudolocalization for the editor and the project manager.

Standalone tools:

     -s, --script <script>             R  Run a script.
     --main-loop <main_loop_name>      R  Run a MainLoop specified by its global class name.
     --check-only                      R  Only parse for errors and quit (use with --script).
     --import                          E  Starts the editor, waits for any resources to be imported, and then quits.
     --export-release    E  Export the project in release mode using the given preset and output path. The preset name should match one defined in "export_presets.cfg".
                                           should be absolute or relative to the project directory, and include the filename for the binary (e.g. "builds/game.exe").
                                          The target directory must exist.
     --export-debug      E  Export the project in debug mode using the given preset and output path. See --export-release description for other considerations.
     --export-pack       E  Export the project data only using the given preset and output path. The  extension determines whether it will be in PCK or ZIP format.
     --export-patch      E  Export pack with changed files only. See --export-pack description for other considerations.
     --patches                  E  List of patches to use with --export-patch. The list is comma-separated.
     --install-android-build-template  E  Install the Android build template. Used in conjunction with --export-release or --export-debug.
     --doctool [path]                  E  Dump the engine API reference to the given  (defaults to current directory) in XML format, merging if existing files are found.
     --no-docbase                      E  Disallow dumping the base types (used with --doctool).
     --gdextension-docs                E  Rather than dumping the engine API, generate API reference from all the GDExtensions loaded in the current project (used with --doctool).
     --gdscript-docs             E  Rather than dumping the engine API, generate API reference from the inline documentation in the GDScript files found in  (used with --doctool).
     --build-solutions                 E  Build the scripting solutions (e.g. for C# projects). Implies --editor and requires a valid project to edit.
     --dump-gdextension-interface      E  Generate a GDExtension header file "gdextension_interface.h" in the current folder. This file is the base file required to implement a GDExtension.
     --dump-extension-api              E  Generate a JSON dump of the Godot API for GDExtension bindings named "extension_api.json" in the current folder.
     --dump-extension-api-with-docs    E  Generate JSON dump of the Godot API like the previous option, but including documentation.
     --validate-extension-api    E  Validate an extension API file dumped (with one of the two previous options) from a previous version of the engine to ensure API compatibility.
                                          If incompatibilities or errors are detected, the exit code will be non-zero.
     --benchmark                       E  Benchmark the run time and print it to console.
     --benchmark-file            E  Benchmark the run time and save it to a given file in JSON format. The path should be absolute.

\

\</pre\>

## [Troubleshooting]

### [Pop-up windows behave strangely]

If the Godot pop-up windows behave strangely, try running Godot in single-window mode.

To run Godot in single-window mode:

`user `[`$`]`godot --single-window`

## [References]

1.  [[[↑](#cite_ref-1)] [[https://godotengine.org/article/dev-snapshot-godot-4-3-dev-3/#wayland-support-for-linux](https://godotengine.org/article/dev-snapshot-godot-4-3-dev-3/#wayland-support-for-linux)]]