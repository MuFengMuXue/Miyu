# Custom FreeBSD builds

OBS Studio's CMake options allow customization of the desired build configuration but also require manual setup and preparation. Available CMake configuration variables can be found in the [CMake build system documentation](https://github.com/obsproject/obs-studio/wiki/building-obs-studio#cmake). The recommended action is to create a [CMake Preset](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html) for each build configuration.

**NOTE:** FreeBSD is not officially supported by the OBS team and is provided as-is.

## Prerequisites

* FreeBSD 13 or newer
* CMake 3.28 or newer
* Git
* Ninja
* *Optional:* Ccache to improve compilation speeds on consecutive builds
* Several additional dependencies (see step 2 below)

## Build Procedure

### 1. Get the source code

1. Open a Terminal window, create and switch to a directory you want to have OBS checked out
2. Clone the repository including **submodules**: `git clone --recursive https://github.com/obsproject/obs-studio.git`

(If you do not know what submodules are, or you are not using Git from the command line, **PLEASE make sure to fetch the submodules too**.)

### 2. Get the dependencies

* Alternatively the required dependencies can be installed using `pkg`:
    * Build system dependencies
    ```
    sudo pkg install cmake ninja binutils pkgconf curl ccache kf6-extra-cmake-modules
    ```

    * OBS dependencies (core):
    ```
    sudo pkg install ffmpeg libx264 mbedtls mesa-libs jansson lua52 luajit python37 libX11 xorgproto libxcb libXcomposite libXext libXfixes libXinerama libXrandr swig dbus jansson libICE libSM libsysinfo
    ```

    * OBS dependencies (UI):
    ```
    sudo pkg install qt6-base qt6-imageformats qt6-svg
    ```

    * Plugin dependencies:
    ```
    sudo pkg install v4l_compat fdk-aac fontconfig freetype2 speexdsp libudev-devd libv4l vlc audio/jack pulseaudio sndio
    ```

### 3. Set up the build project

1. Run CMake to generate a build environment

```
cmake -S . -B <YOUR_BUILD_DIRECTORY> -G Ninja \
    -DENABLE_RELOCATABLE=ON \
    -DENABLE_PORTABLE_CONFIG=ON \
    -DENABLE_PIPEWIRE=OFF
```

**Optional Settings:**

2. To change the build type, pass either `Debug`, `Release`, `RelWithDebInfo`, or `MinSizeRel` as `-DCMAKE_BUILD_TYPE`

**NOTE:** When building OBS with `ENABLE_RELOCATABLE` disabled, OBS expects GNU-based install paths (e.g. `/usr/local/[bin,lib,share]`) and is built for a single architecture only. To create separate builds for 32-bit and 64-bit architectures, always enable portable builds.

### 4. Build the project

1. Run `cmake --build <YOUR_BUILD_DIRECTORY>` to build the entire OBS project
2. Run `cmake --build <YOUR_BUILD_DIRECTORY> -t libobs` to build only libobs or any other valid target
3. Run `cmake --build <YOUR_BUILD_DIRECTORY> -t clean` to clean your current build directory

### 6. Install the project

Installation will use the directory specified via `-DCMAKE_INSTALL_PREFIX` or can be customised with the `--prefix` switch:

1. Run `cmake --install <YOUR_BUILD_DIRECTORY>` to install OBS to the prefix the project was configured with
2. Run `cmake --install <YOUR_BUILD_DIRECTORY> --prefix <YOUR_INSTALL_LOCATION>` to install OBS to a custom location

### 7. Create installer package

1. Run `cmake --package <YOUR_BUILD_DIRECTORY>` - CMake will handle all operations necessary to create a installer package (compressed archive as well as shell script with embedded binary)
