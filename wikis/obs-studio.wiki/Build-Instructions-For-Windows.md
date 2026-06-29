**NOTE:** Since July 2023, `obs-studio` uses an updated build system on Windows that automates most steps required in old build systems. Build instructions for the legacy build system for OBS Studio 28.0 to 29.1 are retained at [Legacy Build Instructions For Windows](https://github.com/obsproject/obs-studio/wiki/Legacy-Build-Instructions-For-Windows).

## Prerequisites
* Windows 10 1909+ (or Windows 11)
* [Visual Studio](https://visualstudio.microsoft.com/) 2022 or newer
  * Version 17.13.2 (or greater) 
  * Windows 11 SDK (minimum 10.0.22621.0)
  * C++ ATL for latest v143 build tools (x86 & x64)
  * MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)
* [Git for Windows](https://gitforwindows.org/)
* [CMake](https://cmake.org/) 3.28 or newer

## Configure Build Project

1. Clone the repository including **submodules**:

    `git clone --recursive https://github.com/obsproject/obs-studio.git`

2. Set current directory to `obs-studio`
3. Check available CMake presets: `cmake --list-presets`
4. Select the `windows-x64` preset: `cmake --preset windows-x64`
    - Available and supported architectures are: `x64`
      - x86 (32-bit) builds of obs-studio are no longer supported
    - Any other CMake variables can be provided as usual and can also override variables set by the preset if necessary

> [!IMPORTANT]  
> Do not overide the [-Generator/-G](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html) flag to anything other than `Visual Studio XX 20XX`
> as Cmake will not populate it's Windows 11 SDK variable, and cause the config to fail.
> Cmake will also overide `CXX`, `CC` and `LD` Variables, so please ensure `CCFLAGS`, `CXXFLAGS` `LDFLAGS` are  properly reconfigured if set

## Build obs-studio

1. Open the Visual Studio solution file in the generated build directory (`build_x64\obs-studio.sln`)
2. Select the build configuration that you want to build (Debug, MinSizeRel, Release, RelWithDebInfo)
3. Press `<Control>+<Shift>+<B>` to build the solution (Build -> Build Solution)
   1. Alternatively, press `<F5>` to build and run it (Debug -> Start Debugging)

Alternatively the project can also be built on the command line:

1. Make sure the current directory is set to the `obs-studio` source code directory (if you continued from "Configuring Build Project" above, you are already there)
2. Run `cmake --build --preset windows-x64`
3. Run the app by navigating to `.\build_x64\rundir\<Debug|Release|RelWithDebInfo|MinSizeRel>\bin\64bit`, either on command line or in File Explorer, and run `obs64.exe`.

While it is possible to do so, we generally do not recommend running OBS from command line.

## Custom Build Options

Custom build options can be provided to CMake. You can either:

* Specify them directly as cache variables
  * From command line when Configuring Build Project: `cmake --preset windows-x64 -DENABLE_BROWSER:BOOL=OFF`)
  * In the CMake GUI 
* Override them in a CMake User Preset specified in your local CMakeUserPresets.json

## Install the Virtual Camera

If you want to use the Virtual Camera created by this build, you will have to run its install script and also remove the Virtual Camera from a standard OBS installation first:

* To uninstall the OBS Virtual Camera
    1. Close any applications that were using the OBS Virtual Camera.
    2. In the OBS Studio installation directory, run `data\obs-plugins\win-dshow\virtualcam-uninstall.bat` as administrator.

* To install an OBS Virtual Camera:

    1. In the OBS Studio artifact directory (for Visual Studio builds, this is `<BUILD DIRECTORY>/rundir/<CONFIG>`), run `data\obs-plugins\win-dshow\virtualcam-install.bat` as administrator.

**Don't forget to uninstall your build's virtual camera before cleaning/deleting your build files.**

## Integrating clang-format into Visual Studio

Use of `clang-format` is required for pull requests, and OBS targets the version shipped with Visual Studio 2022 17.13, `clang-format 19.1.1`. If you are using Visual Studio 2022 17.13, it should automatically format code for you.

To configure any other Visual Studio installation to use `clang-format 19.1.1`:

1. Download and install [LLVM 19.1.1](https://releases.llvm.org/).
2. Run Visual Studio, select `Tools -> Options` from the menu.
    * Go to `Text Editor -> C/C++ -> Code Style -> Formatting -> General`.
    * Enable "Use custom clang-format.exe" and enter the file name, e.g. `C:\Program Files\LLVM\bin\clang-format.exe`.
    * The default keyboard shortcut for formatting a document (Edit.FormatDocument) is Ctrl+K, Ctrl+D.
