* **Note:** OBS will not run by default from within the build directory, throwing an error similar to "error while loading shared libraries: libobs-frontend-api.so.0: cannot open shared object file: No such file or directory". Use the portable mode options for running the binaries without doing a system install.

<br>
<br>


# Getting the dependencies and source

## Dependencies

The required dependencies and how to set them up will vary based on your distro :

<details>
<summary> <strong>Debian-based</strong> </summary>

* Build system dependencies
```
sudo apt install cmake extra-cmake-modules ninja-build pkg-config clang clang-format build-essential curl ccache git zsh
```

* OBS dependencies (core):
```
sudo apt install libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev libx264-dev libcurl4-openssl-dev libmbedtls-dev libgl1-mesa-dev libjansson-dev libluajit-5.1-dev python3-dev libx11-dev libxcb-randr0-dev libxcb-shm0-dev libxcb-xinerama0-dev libxcb-composite0-dev libxcomposite-dev libxinerama-dev libxcb1-dev libx11-xcb-dev libxcb-xfixes0-dev swig libcmocka-dev libxss-dev libglvnd-dev libgles2-mesa-dev libwayland-dev librist-dev libsrt-openssl-dev libpci-dev libpipewire-0.3-dev libqrcodegencpp-dev uthash-dev libsimde-dev
```

* OBS Qt6 dependencies (UI):
```
sudo apt install \
       qt6-base-dev \
       qt6-base-private-dev \
       qt6-svg-dev \
       qt6-wayland \
       qt6-image-formats-plugins
```

* Plugin dependencies:
```
sudo apt install \
       libasound2-dev \
       libfdk-aac-dev \
       libfontconfig-dev \
       libfreetype6-dev \
       libjack-jackd2-dev \
       libpulse-dev libsndio-dev \
       libspeexdsp-dev \
       libudev-dev \
       libv4l-dev \
       libva-dev \
       libvlc-dev \
       libvpl-dev \
       libdrm-dev \
       nlohmann-json3-dev \
       libwebsocketpp-dev \
       libasio-dev
```

***
</details>

<details>
<summary> <strong>Red Hat-based</strong> </summary>

* Get RPM Fusion at http://rpmfusion.org/Configuration/

* Get the required packages:

   ```bash
   sudo yum install \
          alsa-lib-devel \
          asio-devel \
          cmake extra-cmake-modules \
          ffmpeg-free-devel \
          fontconfig-devel \
          freetype-devel \
          gcc \
          gcc-c++ \
          gcc-objc \
          git \
          glib2-devel \
          json-devel \
          libavcodec-free-devel \
          libavdevice-free-devel \
          libcurl-devel \
          libdrm-devel \
          libglvnd-devel \
          jansson-devel \
          libuuid-devel \
          libva-devel \
          libv4l-devel \
          libX11-devel \
          libXcomposite-devel \
          libXinerama-devel \
          luajit-devel \
          make \
          mbedtls-devel \
          pciutils-devel \
          pipewire-devel \
          pulseaudio-libs-devel \
          python3-devel \
          qt6-qtbase-devel \
          qt6-qtbase-private-devel \
          qt6-qtsvg-devel \
          qt6-qtwayland-devel \
          speexdsp-devel \
          swig \
          systemd-devel \
          vlc-devel \
          wayland-devel \
          websocketpp-devel \
          x264-devel
   ```

  * If `speexdsp-devel` is not available, it can be built from source (https://gitlab.xiph.org/xiph/speexdsp)

***
</details>

<details>
<summary> <strong>Fedora</strong> </summary>

* Add the RPM Fusion repo. This is required for `x264-devel`.

```
sudo dnf install \
  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
```

* Get the required packages:

   ```bash
   sudo dnf install \
          alsa-lib-devel \
          asio-devel \
          cmake extra-cmake-modules \
          extra-cmake-modules \
          ffmpeg-free-devel \
          fontconfig-devel \
          freetype-devel \
          gcc \
          gcc-c++ \
          gcc-objc \
          git \
          glib2-devel \
          jansson-devel \
          json-devel \
          libavcodec-free-devel \
          libavdevice-free-devel \
          librist-devel \
          libcurl-devel \
          libdatachannel-devel \
          libdrm-devel \
          libglvnd-devel \
          libqrcodegencpp-devel \
          libuuid-devel \
          libva-devel \
          libv4l-devel \
          libvpl-devel \
          libX11-devel \
          libXcomposite-devel \
          libXdamage \
          libXinerama-devel \
          libxkbcommon-devel \
          luajit-devel \
          make \
          mbedtls-devel \
          ninja \
          nv-codec-headers \
          pciutils-devel \
          pipewire-devel \
          pulseaudio-libs-devel \
          python3-devel \
          qt6-qtbase-devel \
          qt6-qtbase-private-devel \
          qt6-qtsvg-devel \
          qt6-qtwayland-devel \
          rnnoise-devel \
          simde-devel \
          speexdsp-devel \
          srt-devel \
          swig \
          systemd-devel \
          uthash-devel \
          vlc-devel \
          wayland-devel \
          websocketpp-devel \
          x264-devel
   ```

***
</details>

<details>
<summary> <strong>openSUSE</strong> </summary>

* See [openSUSE install instructions](install-instructions#opensuse-unofficial) for details on adding Packman repository.

* Get the required packages:

   ```bash
   sudo zypper in cmake \
                fontconfig-devel \
                freetype2-devel \
                gcc \
                gcc-c++ \
                libcurl-devel \
                ffmpeg2-devel \
                libjansson-devel \
                libpulse-devel \
                libspeexdsp-devel \
                libudev-devel \
                libv4l-devel \
                libXcomposite-devel \
                libXinerama-devel \
                libXrandr-devel \
                luajit-devel \
                mbedtls \
                qt6-qtbase-dev \
                qt6-qtbase-private-dev \
                swig \
                python3-devel \
                libxss-dev
   ```

***
</details>

### OBS-browser

If you wish to build OBS with browser support, you will need to download the pre-built obs-browser CEF framework (or build it yourself, but that is beyond the scope of this guide) and uncompress it in a folder that will be accessible to cmake.\
Version 127.0.6533.120, for use with OBS 32+ can be found [here](https://cdn-fastly.obsproject.com/downloads/cef_binary_6533_linux_x86_64_v6.tar.xz).

While ARM is not yet fully supported by OBS, we still provide a prebuilt CEF if you're wanting to head into the danger zone, which can be found [here](https://cdn-fastly.obsproject.com/downloads/cef_binary_6533_linux_aarch64_v6.tar.xz).

<!-- CHECK : Should we also link to older versions? is there any way to setup a permalink to latest?  -->

## Source code

1. Open a Terminal window, create and switch to a directory you want to have OBS checked out into.
2. Clone the repository including **submodules**: `git clone --recursive https://github.com/obsproject/obs-studio.git`

If you do not know what submodules are, or you are not using Git from the command line, **PLEASE make sure to fetch the submodules too**. Do not use the GitHub source .tar as it does not include all the required source files. Always use the appropriate Git tag with the associated submodules.


<br>
<br>

# Configuring the build

Configuring the build project is done through cmake presets, e.g.:
```
cmake --preset <preset_name>
```

It is recommended that you create your own preset in order to easily change the options you need. This is done by creating a `CMakeUserPresets.json` file and specifiying your custom preset in it. See the cmake-presets [documentation](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html) for details.\
Alternatively, you can specify options overrides directly on the command line with the `-D` switch, e.g.:
```
cmake --preset <preset_name> -DENABLE_BROWSER=ON
```
to set `ENABLE_BROWSER` to `ON`.

It is recommended you configure your build to run in portable mode.
The intricacies of which folder to install to for a system install, or how to create a package for a given manager vary from distro to distro and are outside the scope of this guide.

<br>

## Common build options

Available build options are listed in the [CMake build system documentation](https://github.com/obsproject/obs-studio/wiki/building-obs-studio#cmake). We'll cover here the commonly needed ones for Linux builds.

### Portable mode
To configure a build that can be launched in portable mode, you need :
* `"ENABLE_RELOCATABLE": true,`
* `"ENABLE_PORTABLE_CONFIG": true,`
* `"CMAKE_INSTALL_PREFIX": {"type": "STRING", "value": "<path_to_install_to>"},`

### OBS-browser
To configure a build with browser support, you need :
* `"ENABLE_BROWSER" : true,`
* `"CEF_ROOT_DIR": {"type": "STRING", "value": "<path_to_CEF_Framework>"},`\
 (I.e., the path to which you uncompressed the file downloaded in [the section above](#obs-browser))

### Deprecation as warning
By default deprecations are treated as errors and stop the build process. This can easily break the build if you are not compiling with the exact same versions that OBS is set for.\
To allow for deprecation to be treated as warnings, use :
* `"OBS_COMPILE_DEPRECATION_AS_WARNING": true,`

### Nvenc
There are two options to enable/disable building with NVENC :
* `"ENABLE_NVENC"` for the native obs-nvenc
* `"ENABLE_FFMPEG_NVENC"` for the ffmpeg-provided nvenc

### LibajanTV2
By default, OBS is configured to build with AJA I/O devices support enabled. This requires [libajantv2](https://github.com/aja-video/libajantv2) to be installed.
Alternatively, you can disable it with :
* `"ENABLE_AJA": false,`


## Distro-specific build options
<details>
<summary> <strong>Red Hat-based</strong> </summary>

On Red Hat-based distros, you need to configure with `"CMAKE_POSITION_INDEPENDENT_CODE": true,`.
<!-- Need norihiro' confirmation on whether this is still necessary -->

***
</details>

<br>
<br>

# Building and installing

Once you properly configured your build project, you can build and install it with :
```
cmake --build <build_dir> && cmake --install
```
where `<build_dir>` is the build folder of the preset you used (`build_ubuntu` for the default `ubuntu` preset)

if you configured it to run as portable, you can then launch obs with:
```
<portable_install_path>/bin/obs -p
```

<br>

Building only libobs can be done with :
```
cmake --build <build_dir> -t libobs
```

Cleaning the build directory can be done with :
```
cmake --build <build_dir> -t clean
```
