If you want to develop for OBS, please visit our [Discord](https://obsproject.com/discord) and get to know the devs or have questions answered!

Also, if there is something in this guide you want to change/improve on, it is recommended that you talk about it with the devs in Discord or IRC first.

Please note that any install directions/packages for Linux/FreeBSD distributions listed as *Unofficial* means that they are community provided, and any support for those packages should be directed at the appropriate distro/package maintainers.

# OBS build dependencies

| Dependency | Available Pre-Built (macOS and Windows)|
|---|---|
| FFmpeg | `YES` |
| x264 | `YES` |
| cURL | `YES` (required on Windows only) |
| mbedTLS | `YES` |
| Chromium Embedded Framework | `YES` |
| Qt | `YES` |

We suggest having a current version of Git and CMake installed on the build system. **Linux** systems also require the _Ninja build system_ to be installed. _CCache_ can be installed to speed up consecutive builds as well and is supported by the build system.

OBS Studio's CMake will automatically download prebuilt dependencies on Windows and macOS. Check out the OS-specific build instructions pages for more detail on available functionality.

# CMake

OBS uses CMake to create build environments for different platforms and IDEs. As a modular project, each module can introduce its own build options and requirements, which are gathered and managed by CMake when invoking it.

While these build options are detected and set automatically by CMake, they can also be changed after build configuration has finished or can be changed via overrides at configuration time.

This article explains some intricacies of OBS' CMake build system structure and the available options to change its behavior.

## CMake Presets

Instead of defining CMake options when invoking CMake, it is recommended to create a [CMake Preset](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html) that defines the options. Custom presets can be defined in CMakeUserPresets.json. Officially defined presets are located in CMakePresets.json.

## OBS CMake Build System

OBS requires at least CMake v3.28 or newer due to many quality-of-life changes introduced in this version. On Windows and macOS the most current CMake version (as of writing v3.31) is preferred, even if the current feature level is capped to v3.30.

Due to OBS' modular structure, some build configuration settings are available globally, while others are introduced by modules. They are listed here in order of appearance (as defined by each `CMakeLists.txt` file, which is processed procedurally by CMake).

### Global Options

| Variable  | Description | Default | OS  |
|-----------|-------------|---------|-----|
| CMAKE_BUILD_TYPE | Sets the build configuration (available values are `Debug`, `RelWithDebInfo`, `Release` and `MinSizeRel`) | `RelWithDebInfo` | All |
| CMAKE_INSTALL_PREFIX | Sets either an absolute installation path or path relative to the build directory | `rundir` inside build directory (`install` on macOS) | All | 
| CMAKE_PREFIX_PATH | Additional search path for dependencies, use semicolons to seperate multiple paths | None | All |
| CMAKE_OSX_ARCHITECTURES | Specify architecture(s) to build binaries for (available values are `x86_64` and `arm64`) | `x86_64` | macOS |
| CMAKE_OSX_DEPLOYMENT_TARGET | Minimum macOS versions to deploy binaries for | `10.13` for x86_64, `11.0` for `arm64` | macOS |
| CEF_ROOT_DIR | Specify root directory of pre-built Chromium Embedded Framework (required for Browser source plugin) | None | All |
| VLC_PATH | Specify directory of downloaded VLC source files (required for VLC source plugin) | None | macOS and Windows |

### OBS Build Options

| Variable  | Description | Default | OS  |
|-----------|-------------|---------|-----|
| ENABLE_UI | Enable building with UI (main OBS application) | `ON` | All |
| ENABLE_SCRIPTING | Enable scripting functionality (Lua and/or Python) | `ON` | All |
| ENABLE_RELOCATABLE | Use a portable directory structure for OBS installation | `OFF` | Linux |
| ENABLE_PORTABLE_CONFIG | Enable support for portable config file location | `OFF` | All |
| OBS_VERSION_OVERRIDE | Specify OBS version for configured build | Most recent Git tag | All |
| OBS_BUILD_NUMBER | Continuous build number for configured build | Automatically incremented on local builds | All |
| OBS_CODESIGN_IDENTITY | Identity to use for code signing on macOS | `-`  | macOS |
| OBS_CODESIGN_TEAM | Team to use for code signing on macOS | None | macOS |

### OBS Feature Options

| Variable  | Description | Default | OS  |
|-----------|-------------|---------|-----|
| ENABLE_PLUGINS | Enable building with plugins | `ON` | All |
| ENABLE_WAYLAND | Enable support for Wayland compositor | `ON` | Linux |
| ENABLE_PIPEWIRE | Enable support for Pipewire graphics processing engine | `ON` | Linux |

### OBS Module Options

| Variable  | Description | Default | OS  |
|-----------|-------------|---------|-----|
| ENABLE_AJA | Enable building with AJA NTV2 support | `ON` | All |
| ENABLE_COREAUDIO_ENCODER | Enable support for CoreAudio encoder | `ON` | Windows (cannot be disabled on macOS) |
| ENABLE_DECKLINK | Enable building with Decklink support | `ON` | All |
| ENABLE_ALSA | Enable building with Advanced Linux Sound Architecture (ALSA) support | `ON` | Linux |
| ENABLE_JACK | Enable support for JACK audio server | `OFF` | Linux |
| ENABLE_PULSEAUDIO | Enable Pulse Audio support | `ON` | Linux |
| ENABLE_V4L2 | Enable Video4Linux v2 support | `ON` | Linux |
| ENABLE_VIRTUALCAM | Enable building with Virtual Camera modules | `ON` | Windows and macOS |
| VIRTUALCAM_GUID | Specify global unique identifier (GUID) for Virtual Camera Plugin | None | Windows |
| ENABLE_BROWSER | Enable buidling Browser Source plugin | `ON` | All |
| ENABLE_BROWSER_LEGACY | Enable building Browser Source plugin with legacy CEF version 3770 | `OFF` | Windows |
| ENABLE_BROWSER_SHARED_TEXTURE | Enable building Browser Source plugin with shared texture support | `ON` | Windows and macOS |
| ENABLE_BROWSER_QT_LOOP | Enable building Browser source plugin with Qt message loop | `ON` | macOS |
| ENABLE_BROWSER_PANELS | Enable building Browser source plugin with support for browser panels | `ON` | All |
| ENABLE_FFMPEG_LOGGING | Enable more verbose logging for FFmpeg-based operations | `OFF` | All |
| ENABLE_SPEEXDSP | Enable noise suppression using SpeexDSP | `ON` | All |
| ENABLE_RNNOISE | Enable noise suppression using RNNoise | `ON` | All |
| ENABLE_NVAFX | Enable noise suppression using NVidia Audio Effects SDK | `ON` | Windows |
| ENABLE_LIBFDK | Enable building support for Fraunhofer AAC codec | `OFF` | All |
| ENABLE_RTMPS | Enable support for TLS-based RTMP connections | `AUTO` | All |
| ENABLE_VST | Enable VST plugin support | `ON` | All |
| ENABLE_OSS | Enable building with Open Sound System support | `ON` | Linux |
| ENABLE_SERVICE_UPDATES | Enable automatic streaming service updates | `OFF` | All |
| ENABLE_SNDIO | Enable sndio framework support | `OFF` | Linux |
| ENABLE_FREETYPE | Enable support for FreeType 2 based text rendering | `ON` | macOS and Linux |
| ENABLE_VLC | Enable support for VLC-based sources | `ON` | All |

## General CMake guidance

All these commands implicitly expect to be run from within the OBS source code directory checked out via `git` including all submodules (check the [Installing and Building]() page for more details):

### Create Build Configuration

Just running `cmake` triggers an "in-source" build (meaning: build artifacts are placed with the source code directory structure). Due to OBS' modular structure this build variant is not allowed, instead an "out-of-source" build needs to be configured.

To create a build configuration in a **desired subdirectory** run `cmake -S . -B <YOUR_BUILD_DIR>`. This will configure OBS with most modules available to the host operating system enabled.

To change the **CMake generator** (and the build tool used to compile the project) pass a compatible generator name via the `-G` switch. Supported generators by CMake and OBS are:

* Unix Makefiles
* Ninja
* Xcode
* Visual Studio 17 2022

Other generators are supported by CMake but have neither been tested nor are officially supported by the OBS team.

### Change Configuration Options

To change a configuration option, supported variables can be passed via the `-D` switch. E.g. to disable building with the browser plugin, pass `-DENABLE_BROWSER=OFF`. While CMake supports several values as binary switches, within OBS `ON` or `OFF` are used.

These changes are additive, as CMake stores these options as "cache variables" in a file called `CMakeCache.txt` in the specified build directory and reads from this file when `cmake` is run again. As such cache options can either be changed in this file directly, or overwritten by specifying new values for them via the `-D` switch (see above).

#### CMake GUIs

CMake build configurations can also be managed using graphical user interfaces: On Windows `cmake-gui` is installed with the CMake package available for the platform and allows selection of source and build directories (`-S` and `-B` switches respectively) as well as direct manipulation of all cache variables. Detailed instructions for this GUI are available in the [Installation and Building]() article.

On POSIX-based systems a `ncurses`-based user interface is available via the `ccmake` command which allows editing of cache variables. Note that due to CMake's internal processes, a configuration step (via the `c` shortcut) needs to be repeated until no *new* cache variables are created by it. Only then will the generation step (`g` shortcut) be made available.

### Apply Changes

Whether changes to CMake script files themselves or to cache variables, CMake needs to be run again to "pick up" on these changes and apply them (as build system files are generated according to these changes). When using the GUI a repeat run of configuration and generation steps should be enough to pick up those changes; when using the command line a repeat invocation of `cmake -S . -B <YOUR_BUILD_DIR>` will do the same.

## Modern CMake

OBS uses "Modern CMake" which differentiates from patterns and practices used by CMake before version 2.8/3 - for the full details please refer to [An Introduction To Modern CMake](https://cliutils.gitlab.io/modern-cmake/).

Here are some general rules of thumb (lifted from the article mentioned above):

### CMake Antipatterns

* Do not use global functions: This includes `link_directories`, `include_libraries`, and similar.
* Don't add unneeded `PUBLIC` requirements: You should avoid forcing something on users that is not required (`-Wall`). Make these `PRIVATE` instead.
* Don't `GLOB` files: Make or another tool will not know if you add files without rerunning CMake. Note that CMake 3.12 adds a `CONFIGURE_DEPENDS` flag that makes this far better if you need to use it.
* Do not link to built files directly: Always link to targets if available.
* Never skip `PUBLIC/PRIVATE` when linking: This causes all future linking to be keyword-less.

### CMake Patterns

* Treat CMake as code: It is code. It should be as clean and readable as all other code.
* Think in targets: Your targets should represent concepts. Make an (`IMPORTED`) `INTERFACE` target for anything that should stay together and link to that.
* Export your interface: You should be able to run from build or install.
* Write a `Config.cmake` file: This is what a library author should do to support clients.
* Make `ALIAS` targets to keep usage consistent: Using `add_subdirectory` and `find_package` should provide the same targets and namespaces.
* Combine common functionality into clearly documented functions or macros: Functions are better usually.
* Use lowercase function names: CMake functions and macros can be called lower or upper case. Always use lower case. Upper case is for variables.
* Use `cmake_policy` and/or range of versions: Policies change for a reason. Only piecemeal set `OLD` policies if you have to.

### Examples

* Using (internal) finder variables to add libraries and their include directories:
    ```
    LEGACY:
    ---------------
    find_package(MyLibrary)
    link_directores(${MY_LIBRARY_INCLUDE_DIRS})
    include_libraries(${MY_LIBRARY_LIB})

    MODERN:
    ---------------
    find_package(MyLibrary)
    target_link_libraries(my_target PRIVATE My_Library::My_Library)
    ```

    **NOTE:** If the package does not create an imported library target (`My_Library::My_Library`), an issue should be filed with the respective library maintainer(s) to drop the outdated `FindXYZ.cmake` pattern and update to CMake's `export` function to create a CMake package. In the interim the finder module can be patched to create namespaced imported targets (see some examples in OBS' `CMake/Modules` directory.
* Gathering source files in variables and adding them at the bottom of the script:
    ```
    LEGACY:
    ---------------
    set(mytarget_SOURCES
        my_source.c)
    set(mytarget_HEADERS
        include/my_headers.h)

    add_library(my_target SHARED ${mytarget_SOURCES} ${mytarget_HEADERS)

    MODERN:
    ---------------
    add_library(my_target SHARED)
    target_sources(my_target
        include/my_headers.h)
    ```
* Polluting the build environment with local compilation requirements
    ```
    LEGACY:
    ---------------

    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    set(CMAKE_CXX_EXTENSIONS OFF)

    add_compile_options(-Wextra -Wvla -Wno-unused-function -Wno-missing-field-initializers -fno-strict-aliasing)
    add_link_options(/INCREMENTAL)

    MODERN:
    ---------------
    target_compile_features(my_target PRIVATE cxx_std_17)
    target_compile_options(my_target PRIVATE -Wextra PUBLIC -fno-strict-aliasing)
    target_link_options(my_target PRIVATE LINKER:-z,defs)
    ```

    **NOTE:** The correct use of `PRIVATE` and `PUBLIC` is important here: `PRIVATE` target properties only apply to the target itself, while `PUBLIC` options are also inherited by targets linking to _this_ target. Also note the `LINKER:` prefix for the link options - this allows CMake to use the compiler specific linker flags (e.g `-Xlinker -z -Xlinker defs` for Clang and `-Wl,-z,defs` for GNU GCC).

### Think In Targets

This cannot be stressed enough: In Modern CMake everything revolves around targets, which allows CMake to resolve dependencies and relationships using target properties and the information contained within. E.g. when linking `target_a` with `target_b` (via `target_link_libraries()`) CMake will look up the `INTERFACE_INCLUDE_DIRECTORIES` property on `target_b` to yield the directory containing library headers, as well as `INTERFACE_LINK_LIBRARIES` which will contain the actual library files in the file system. Required compile options and defines are also read from `INTERFACE_COMPILE_OPTIONS` and `INTERFACE_COMPILE_DEFINITIONS` respectively and added to `target_a`'s compile options automatically.

Using namespaces (`My_Library::My_Library`) when specifying targets for linking has the added benefit of ensuring a target reference (instead of a file reference), as colons are invalid for file names in many file systems.