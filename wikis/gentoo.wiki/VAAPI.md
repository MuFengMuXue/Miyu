This page contains [[changes](https://wiki.gentoo.org/index.php?title=VAAPI&diff=1433343)] which are not marked for translation.

\

**Resources**

[[]][Home](https://01.org/linuxmedia/vaapi)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Video_Acceleration_API "wikipedia:Video Acceleration API")

**VAAPI** (**V**ideo **A**cceleration **API**) provides access to graphics hardware (GPU) acceleration for video processing.

## Contents

-   [[1] [Hardware support]](#Hardware_support)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
-   [[3] [Usage]](#Usage)
-   [[4] [Software support]](#Software_support)
    -   [[4.1] [Firefox]](#Firefox)
    -   [[4.2] [VLC]](#VLC)
    -   [[4.3] [mpv]](#mpv)
    -   [[4.4] [ffmpeg]](#ffmpeg)
-   [[5] [Verification]](#Verification)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Hardware support]

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
  Driver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Chipset                                                                                Formats
  [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") or [AMDGPU-PRO](https://wiki.gentoo.org/wiki/AMDGPU-PRO "AMDGPU-PRO")                                                                                                                                                                                                                                                                                                                                                                                                 All supported AMD graphics cards using either the open source or proprietary driver.
  [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") (via [multiple packages](https://wiki.gentoo.org/wiki/Intel#VAAPI "Intel"))                                                                                                                                                                                                                                                                                                                                                                                              Intel GMA X4500HD and newer                                                            See [01.org - VAAPI Supported Hardware & Features](https://01.org/linuxgraphics/community/vaapi).
  [Mesa](https://wiki.gentoo.org/index.php?title=Mesa&action=edit&redlink=1 "Mesa (page does not exist)")                                                                                                                                                                                                                                                                                                                                                                                                                All supported AMD or NVIDIA graphics cards using the open source drivers.
  [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") (via [[[media-libs/nvidia-vaapi-driver]](https://packages.gentoo.org/packages/media-libs/nvidia-vaapi-driver)[]])   NVIDIA GeForce 8 and newer                                                             See [https://github.com/elFarto/nvidia-vaapi-driver?tab=readme-ov-file#codec-support](https://github.com/elFarto/nvidia-vaapi-driver?tab=readme-ov-file#codec-support)
  [VDPAU](https://wiki.gentoo.org/wiki/VDPAU "VDPAU")                                                                                                                                                                                                                                                                                                                                                                                                                                                                          All supported graphics cards
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## [Installation]

### [USE flags]

VAAPI support can be enabled system-wide by adding the `vaapi` value to the `USE` variable:

[FILE] **`/etc/portage/make.conf`**

    USE="vaapi"

Enabling VAAPI support will pull in the [[[media-libs/libva]](https://packages.gentoo.org/packages/media-libs/libva)[]] package, which has the following USE flags:

### [USE flags for] [media-libs/libva](https://packages.gentoo.org/packages/media-libs/libva) [[]] [Video Acceleration (VA) API for Linux]

  ----------------------------------------------------------- ------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)               Add support for X11
  [`glx`](https://packages.gentoo.org/useflags/glx)           Enable GLX backend (requires X). Provides libva-glx.so, needed only by some prebuilt binaries.
  [`wayland`](https://packages.gentoo.org/useflags/wayland)   Enable dev-libs/wayland backend
  ----------------------------------------------------------- ------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 02:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

These flags can be adjusted in [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")].

The system needs to be updated if the `USE` variable has been set to `vaapi`:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [Usage]

Install VAAPI-related utilities from [[[media-video/libva-utils]](https://packages.gentoo.org/packages/media-video/libva-utils)[]]:

`root `[`#`]`emerge --ask media-video/libva-utils`

Run [vainfo] to check VAAPI support.

** Note**\
[Hardware support](https://wiki.gentoo.org/wiki/VAAPI#Hardware_support "VAAPI") was NOT emerged if [vainfo] concludes with:

    libva info: va_openDriver() returns -1
    vaInitialize failed with error code -1 (unknown libva error),exit

`root `[`#`]`vainfo`

    vainfo: VA-API version: 0.35 (libva 1.3.1)
    vainfo: Driver version: Intel i965 driver - 1.3.0
    vainfo: Supported profile and entrypoints
          VAProfileMPEG2Simple            : VAEntrypointVLD
          VAProfileMPEG2Simple            : VAEntrypointEncSlice
          VAProfileMPEG2Main              : VAEntrypointVLD
          VAProfileMPEG2Main              : VAEntrypointEncSlice
          VAProfileH264ConstrainedBaseline: VAEntrypointVLD
          VAProfileH264ConstrainedBaseline: VAEntrypointEncSlice
          VAProfileH264Main               : VAEntrypointVLD
          VAProfileH264Main               : VAEntrypointEncSlice
          VAProfileH264High               : VAEntrypointVLD
          VAProfileH264High               : VAEntrypointEncSlice
          VAProfileVC1Simple              : VAEntrypointVLD
          VAProfileVC1Main                : VAEntrypointVLD
          VAProfileVC1Advanced            : VAEntrypointVLD
          VAProfileNone                   : VAEntrypointVideoProc
          VAProfileJPEGBaseline           : VAEntrypointVLD

It is possible to override the automatic VAAPI driver selection with the `LIBVA_DRIVER_NAME` variable:

-   Intel:
    -   For libva-intel-driver use `i965`
    -   For libva-intel-media-driver use `iHD`

<!-- -->

-   NVIDIA:
    -   For Nouveau use `nouveau`
    -   For NVIDIA use `nvidia`
        1.  Users need to install [[[media-libs/nvidia-vaapi-driver]](https://packages.gentoo.org/packages/media-libs/nvidia-vaapi-driver)[]] first
        2.  If vainfo shows errors, try adding the following line to the grub file and then regenerate it using [grub-mkconfig]:

[FILE] **`/etc/default/grub`**

    # ...
    GRUB_CMDLINE_LINUX_DEFAULT="(...) nvidia_drm.modeset=1 (...)"
    # ...

-   ATI/AMD:
    -   For AMDGPU driver use `radeonsi`

When setting `LIBVA_DRIVER_NAME` to a driver for a secondary GPU, be sure to set `DRI_PRIME` accordingly as well.

## [Software support]

### [Firefox]

[Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") state can checked in `about:support`.

### [VLC]

[VLC](https://wiki.gentoo.org/wiki/VLC "VLC") supports VAAPI natively. Activate the appropriate setting through the preferences menu ([Tools → Preferences → Input/Codecs → Hardware accelerated decoding]).

### [mpv]

[mpv](https://wiki.gentoo.org/wiki/Mpv "Mpv") also supports the VAAPI acceleration through the command-line option `--hwdec=vaapi`.

If the hardware supports only h264 decoding, creating a configuration file similar to the following will enable the hardware to use VAAPI for h264 decoding to watch YouTube:

[FILE] **`~/.config/mpv/mpv.conf`**

    ytdl-format=bestvideo[height<=1080][ext=mp4]+bestaudio/best
    hwdec=vaapi

### [ffmpeg]

To record screen with VAAPI^[\[1\]](#cite_note-1)^:

`user `[`$`]`ffmpeg -vaapi_device /dev/dri/renderD128 -f x11grab -video_size 1366x768 -i :0 -vf 'format=nv12,hwupload' -c:v h264_vaapi o.mp4`

## [Verification]

Intel iGPUs provide a way to verify usage of hardware encoding or decoding. Package [[[x11-apps/igt-gpu-tools]](https://packages.gentoo.org/packages/x11-apps/igt-gpu-tools)[]] provides [intel_gpu_top] utility which can be used for a [top]-like GPU monitoring.

Hardware encoding/decoding activity can be observed. A greater-than-zero **Video BUSY** value means an active hardware processing:

    intel-gpu-top: Intel Ivybridge (Gen7) @ /dev/dri/card0 -  558/ 558 MHz;  68% RC6;  1.05/ 9.46 W;      185 irqs/s

          IMC reads:        0 MiB/s
         IMC writes:     1120 MiB/s

             ENGINES     BUSY                                                                        MI_SEMA MI_WAIT
           Render/3D   23.92% |█████████████████████                                              |      0%      0%
             Blitter    0.00% |                                                                   |      0%      0%
               Video    7.98% |███████                                                            |      0%      0%

## [See also]

-   [VDPAU](https://wiki.gentoo.org/wiki/VDPAU "VDPAU") --- how to setup the **V**ideo **D**ecode and **P**resentation **A**PI for **U**nix (VDPAU).

## [References]

1.  [[[↑](#cite_ref-1)] [[https://trac.ffmpeg.org/wiki/Encode/H.264](https://trac.ffmpeg.org/wiki/Encode/H.264)]]