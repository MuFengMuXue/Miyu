# DaVinci Resolve

Davinci Resolve is a proprietary video editing, color grading, color correction, visual effects, motion graphics and audio post-production application.

## Installation
Both a limited free version and a paid (Studio) version are offered.

For the free version, install , for the Studio version, install .

To run DaVinci Resolve, it is required to use suitable OpenGL and OpenCL drivers. Open-source OpenCL drivers are supported via Mesa (Rusticl) for AMD cards and Intel cards. The NixOS wiki has a compatibility matrix of supported AMD GPUs for Davinci Resolve.

{| class="wikitable"  style="text-align:center"
|+Table of OpenGL drivers
|-
! GPU vendor !! OpenGL driver !! Open Source !! Documentation !! Tested driver version !! Works with DaVinci Resolve !! Tested DR version !! Notes
|-
! rowspan="1" | AMD
|  ||  || AMDGPU || 23.0.2-2 ||  || 18.1.4-1 || On pre-Vega GPUs, if using opencl-amd and mesa, DR crashes, see this bug report. You can instead use rocm with  or use opencl-amd with progl.

Tested with Radeon RX 580.

Tested with Radeon PRO W6600.
|-
! Intel
|  ||  || Intel graphics || 23.1.6 ||  || 19.1.3 || Works without issues.

Tested with Intel Iris Xe Graphics (Alder Lake Mobile).
|-
! rowspan="2" | NVIDIA
|  ||  || Nouveau || ||  || ||
|-
|  ||  || NVIDIA || 575.64.05-2 ||  || 19.1.3 || Previously tested on Optimus laptop using nvidia-xrun.

Tested with RTX 3060, works without issues or workarounds.
|-
|}

{| class="wikitable" style="text-align:center"
|+Table of tested OpenCL drivers
! GPU Vendor !! OpenCL driver !! Open Source !! Tested driver version !! Works with DR !! Tested DR version !! Comment
|-
!rowspan="2" | Neutral
| ||  || 1:23.3.2-2 ||  || 18.6.4-1 || Some kernel versions have an issue with ROCm, but 6.1 LTS and 6.10.2 work.

Tested with RX 6800M.
|-
|mesa-tkg-git ||  || 24.0.0_devel.180705.fdbb5d58983-1 ||  || 18.6 || DR works with rusticl now that MR 21305 has been merged (commit 0a072bb3).

Tested with RX 7600 using .
|-
!rowspan="3" | AMD
|  ||  || 1:5.6.0-2 ||  || 18.5b || There is no currently AUR package with only repackaged rocm drivers from Ubuntu (this opencl-amd packages both rocm and orca). On GFX8 (RX 580 and others), the ORCA legacy driver is used by default, which itself currently requires the AMDGPU-PRO OpenGL drivers to work (see above).

Tested with Radeon Pro W6600 (works, even with mesa)

Tested with Radeon RX 580 (works, currently only with progl).

Tested with Radeon RX 5700 XT, 6700 XT (with mesa)

Addresses crashing (encounted with rocm-opencl-runtime package) when attempting to perform color correction on the color page. Tested with Radeon 7900XT.
|-
|  ||  || 5.4.3-1 ||  || 18.1.4-1 || For GPUs older than GFX9/Vega use variable ; works with Mesa OpenGL

Tested with Radeon Pro W6600

Tested with AMD RX580. Color correction may result in crashing (did for Radeon )7900XT), consider using opencl-amd 5.6.0-2.
|-
|  ||  || 22.10.1_1401426-1 ||  || 17.4.6-2 || Note that this is simply the  package without the ROCm drivers.

Requires the AMDGPU-PRO OpenGL drivers to work.

Tested with Radeon RX580.
|-
!rowspan="5"|Intel
| ||  || 25.27.34303.5-1 ||  || 19.1.3 || Works without issues.

Tested with Intel Iris Xe Graphics (Alder Lake Mobile).
|-
|mesa with the cl-gl sharing MR applied ||  || 23.3.0 with MR applied ||  || 18.6 || Works with  exported as an environment variable
|-
| ||  || 1.3.2+12+gfc5f430c-2 ||  || || Core dumped
|-
| ||   || 5.0.r63503-2 ||  || || Core dumped
|-
| ||   || 1:18.1.0.013-2 ||  || || Core dumped
|-
!Nvidia
| ||  || 460.32.03-1 ||  || || Suitable, but working on cuda instead?
|}

## DaVinci Resolve Checker
You can run davinci-resolve-checker script, which will tell you if your configuration is suitable for running DR (doesn't work for Intel iGPUs - says OpenCL driver is unsupported, though it does now work). In good configurations it should output:

 All seems good. You should be able to run DaVinci Resolve successfully.

## BlackMagic Design Cards
If using DeckLink, UltraStudio or Intensity cards for video capture and playback, install Desktop Video Software with the  package.

## Manual Install
Since version 19.1.3-2 installing the AUR package out of the box no longer works. Instead clone the package (change davinci-resolve to the version you want, e.g. davinci-resolve-studio)

 git clone https://aur.archlinux.org/davinci-resolve.git

and download the latest Linux version of your preferred installation from BlackMagic's support website. Place the zip file in the cloned repo, beside the other files like PKGBUILD and note down the version (such as 20.0.1) at the end of the file. Also note down the output of running  on the downloaded zip. Now edit the PKGBUILD: Change the pkgver to your version and change the first sha256sum, leaving the other unchanged, to yours. Execute  and you're ready to go.

## Tips and tricks
## Using ffmpeg encoder plug in
Install the  package. New ffmpeg encoders for AV1, HEVC and AVC (that use SVT-AV1, x265, x264 software, and NVAPI for hardware) will be available through the options in the Deliver tab. Note that encoder plug ins are available in the studio version only.

## Decrease installation time
Compression of the Davinci Resolve package takes a significant amount of time because the binary is quite large. You can instruct makepkg to use a different compression algorithm, which in this case disables compression altogether, speeding up the process tremendously.

 PKGEXT='.pkg.tar'

## Using application in portable way
There may be reasons you may want to not install the davinci resolve package to the system. For example, you may not want such a big package to take up space in the system partition. Or you want to quickly switch between different versions of the application: free and studio, current and previous versions. To do this, just unpack the contents of the downloaded installer to a newly created directory (under your $HOME) , and directly run the opt/resolve/bin/resolve from that directory.

## Automating with scripts
DaVinci Resolve supports scripting. The free version supports launching the scripts only from within DaVinci Resolve itself, while with the Studio version you can also invoke scripts externally. To allow it, go to Preferences -> System -> General -> External scripting using. You can choose: None (similarly to Free version, only from within dr), Local (allow invokes from local host), and Network (allow invokes from remote host).

The documentation can be found in Help -> Documentation -> Developer.

## Remap keyboard modifiers used with mouse wheel for scroll and zoom
The application uses very strange bindings of keyboard modifiers for zooming and scrolling timeline. Original behavior is the following:

* shift + vertical wheel = height of tracks
* ctrl + wheel or horizontal wheel = scroll timeline
* alt + vertical wheel = zoom timeline
* no modifiers + vertical wheel = vertical scroll

By disabling “2D scroll” (in Settings → User → UI), it is possible to remap vertical wheel onto timeline scroll, with horizontal wheel losing its function (and therefore no keybindings for vertical scroll). It is impossible to customize this any more from the application, see A workaround (working in X11 and Wayland) is to use evsieve. Replace  and  with your keyboard and mouse events in the following command:

Another workaround (working in X11 (and Xwayland), is worse and sometimes skips events) of this problem, you can use IMWheel utility. It can remap modifiers only for the application described by regular expression.

Use the following config:

Alternatively, use the following blocks:

## Prevent prompt returning before full exit
When you exit application, the terminal prompt is returned to you, but suddenly the terminal is polluted with "Socket disconnected" message. To prevent this, pipe output of main process via . See [https://unix.stackexchange.com/a/698155 here for explanation.

## Troubleshooting
## Logs
DaVinci Resolve creates the log file  at every launch. Inspecting it can help diagnose problems.

## Application window misses title bar
There is a workaround for KDE - a window rule to force enable title bar. See You can manually create a file describing needed window rule:

Then go to System Settings > Window Management > Window Rules and import this file.

## MP4, H.264, H.265 and AAC Support
It's a misconception that DaVinci Resolve free does not support the MP4 container type.  It is more accurate to say DaVinci Resolve free does not support decoding or encoding H.264 and H.265 video, regardless of the container type.

For example, an MP4 containing an AV1 video stream and MP3 or PCM audio stream, can be decoded by DaVinci Resolve free.

Neither DaVinci Resolve free or Studio versions support decoding or encoding of AAC audio streams.

For more information, see the [https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_20_Supported_Codec_List.pdf official Blackmagic codec documentation (for DR 20, similarly: for DR 19 and 18).

{| class="wikitable"  style="text-align:center"
|+Table of MP4, H.264, H.265 and AAC Support
|-
! Release !! MP4 !! H.264 !! H.265 !! AAC !! Tested Version !! Notes
|-
! Free
|   ||  ||  ||  || 18.6.6-2 || MP4 supported provided supported codecs are being used (eg: AV1 and PCM).
|-
! Studio
|   ||  ||  ||  || 18.6.6-2 ||
|}

## Workaround for DaVinci Resolve Free
If your MP4's video is H.264 or H.265, but audio is MP3 or PCM, you need only transcode your video to a supported codec, as the audio is already supported.

 $ ffmpeg -i input.mp4 -c:v dnxhd -profile:v dnxhr_hq -pix_fmt yuv422p -c:a copy output.mov

If your MP4's video is H.264 or H.265, and the audio is AAC, you need to transcode both your video and audio to a supported codec.

 $ ffmpeg -i input.mp4 -c:v dnxhd -profile:v dnxhr_hq -pix_fmt yuv422p -c:a alac output.mov

If your MP4's video is AV1, but the audio is AAC, transcode just the audio to a supported codec:

 $ ffmpeg -i input.mp4 -c:v copy -c:a pcm_s32le output.mp4

If your space is limited, you could use this option (still x4..5 increase in file size) - but bear in mind, this is a lossy format so you could possibly get compression artefacts at later stages - for example, due to color correction - and lose your work :

 $ ffmpeg -i input.mp4 -c:v mpeg4 -q:v 2 -c:a alac output.mp4

You could also use alac codec for initial recording in OBS, and then copy audio with "-c:a copy" as ffmpeg parameter, to avoid encoding.

You can automate this task using incron. It will automatically convert files appeared in specified folder. See setup example on this article. Another alternative is to write a resolve script for that purpose. See documentation for Resolve Scripting (linked in the see also section) for more information.

## Workaround for DaVinci Resolve Studio
Both H.264 and H.265 video is supported by Studio, but AAC audio is not.  You can transcode the audio from the unsupported AAC format, into a supported lossless format without destructively re-compressing the video, or separating the audio from the video.

In #See also section, note a link to a PDF containing an official list of supported codecs.

To transcode audio into Apple Lossless Audio Codec ().  This is a good option if you prefer using MOV containers.

 $ ffmpeg -i input.mp4 -c:v copy -c:a alac output.mov

FLAC offers just a minor compression advantage over ALAC.  To transcode into FLAC, you will need to use the MKV container.
 $ ffmpeg -i input.mp4 -c:v copy -c:a flac -compression_level 12 output.mkv

There's probably no real advantage to using PCM, except that MP4, MOV and MKV containers all support it, if that's important to you.
 $ ffmpeg -i input.mp4 -c:v copy -c:a pcm_s32le output.mov

## HiDPI
To enable compatibility with high-resolution displays, set the following environment variable accordingly:

 QT_AUTO_SCREEN_SCALE_FACTOR=1

You can change UI scaling in settings: Preferences (ctrl + ,) > User tab > UI settings > UI Display Scale.

## Wine version
Some plugins are available for Windows, but not available for Linux, so you may want to use Davinci Resolve via wine. Also, wine version could potentially workaround the linux-only problem of mp4 format issues. Wine 6.5 brings OpenCL 1.2 support, which is required for DR. Unfortunately, there was no success to start DR via wine.
See test results here. In 17.4.1 DR cannot see the list of available gpus (wine 6.21). Probably, need some hack to make wine present gpus to applications. In dr 18.5b1 with wine 8.7-1 I get the rocm error (5.4.3-1) that is filed here.

## Wrong OpenCL Version
If the application simply is not starting, even after showing installer and "tour" successfully your OpenCL Version may not match your NVIDIA driver.
If you have installed nvidia-440xx make sure to install opencl-nvidia-440xx as well.
A possible error message:

## Get back to Onboarding screen
If you are experimenting with driver installation, you may want to start from the welcome tour and onboarding screen, which checks your system and graphics card. You can achieve that by removing configs directory:

 rm -r $HOME/.local/share/DaVinciResolve/configs

## Full screen preview function missing
This function is only available in the studio version. It is in menu Workspace > Video Clean Feed.

## No audio during video preview
DaVinci interfaces the ALSA directly, so if you use PulseAudio you need to install  or . Alternatively you can redirect it to use PulseAudio yourself by creating  in  with the following content:

## Error code 999 on Intel/NVIDIA hybrid graphics card
"The GPU failed to perform image processing because of an error. Error Code: 999."

If the NVIDIA GPU is used in on-demand mode, you have to explicitly demand it. To enable set the following environment variables:

 __NV_PRIME_RENDER_OFFLOAD=1
 __GLX_VENDOR_LIBRARY_NAME=nvidia

Note: The same environment variable setup can also resolve the "Your GPU memory is full" error on (Intel OR AMD)/NVIDIA hybrid graphics configurations.

## Silent crash related to libcrypto.so.1.0.0
DaVinci Resolve is not starting in graphical mode.
In the console, this error is thrown:

 $ /opt/resolve/bin/resolve
 bin/resolve: error while loading shared libraries: libcrypt.so.1: cannot open shared object file: No such file or directory

You need to install .

## Missing Workflow Integrations menu
In DR Studio for Windows and Mac OS there is Workspace -> Workflow Integrations menu. Workflow Integration plugins are written in JavaScript (electron applications). As noted in documentation (you can reach it in Help -> Documentation -> Developer), Linux currently is not supported (checked in 17.4.3). They say Integration Scripts are supported in Linux, this is most probably a mistake, because they did not provided a path where to put them and still the menu is missing (it is that same Workspace -> Workflow Integrations).

## Python 3.6 not found
When going to Workspace -> Console -> Py3 the error window appears saying "Python 3.6 not found".

One solution is the following (from this question):

 env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.6.11
 sudo ln -s $HOME/.pyenv/versions/3.6.11/lib/python3.6 /usr/local/lib/python3.6
 sudo ln -s $HOME/.pyenv/versions/3.6.11/lib/libpython3.so /usr/local/lib/libpython3.6.so

In DR 18 they say that all python 3 versions are supported.

## Kill hanged process
If dr hanged, fails to release a terminal when you press ctrl + c (to send sigint), and when its window is not shown and you cannot open dr again (it is saying another instance is already running), you can still fix it. Open task manager (ctrl + esc in KDE), then search for process named "GUI", then kill it (send signal 9). Now you can start dr normally.

## Use Dolphin instead of Qt File Picker
Unfortunately, DR does not support XDG desktop portals yet. See for feature request. As a workaround, you can use Andrew Shark's script [https://gitlab.com/AndrewShark/davinci-resolve-scripts/-/blob/main/import%20media%20via%20dolphin.py Import Media via Dolphin.

## Unable to start (onetbb/log4cxx)
The switch to  is causing a hang with the following message:

One suggested workaround is to temporarily rename  to something else.

See the tbb is replaced by onetbb and resolve cannot start on linux forum post for further discussion.

## Unable to start (libpango/glib)
Due to the way Resolve handles libraries, starting the software may fail if the system libraries differ too much from the ones resolve ships.

 /opt/resolve/bin/resolve: symbol lookup error: /usr/lib64/libpango-1.0.so.0: undefined symbol: g_string_free_and_steal

To circumvent it you can force Resolve to use the systems' version instead:

 $ LD_PRELOAD="/usr/lib64/libglib-2.0.so" /opt/resolve/bin/resolve

Resolve may fail to launch on the first try, but it will work on subsequent attempts.

It may be resulted in a new error:

 /opt/resolve/bin/resolve: symbol lookup error: /usr/lib/libgdk_pixbuf-2.0.so.0: undefined symbol: g_task_set_static_name

As of 2024-05-23, the fix for that `g_task_set_static_name` error is (source for solution in Arch forum):
 $ LD_PRELOAD="/usr/lib/libgio-2.0.so /usr/lib/libgmodule-2.0.so" /opt/resolve/bin/resolve

Another workaround is to remove a few libs from Resolve's directory. This way Resolve will be forced to use system libs, not the ones packaged with it. See also the AUR comments for the packages and the PKGBUILD itself for more information on this trick.
 /opt/resolve/libs/libglib-2.0.so*
 /opt/resolve/libs/libgio-2.0.so*
 /opt/resolve/libs/libgmodule-2.0.so*

## Unable to start (wayland)
In a wayland session, environment variable  may be already set to enable other QT programs to launch with Wayland support. However, DaVinci Resolve will fail to launch with the following error:

 qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
 This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

DaVinci Resolve can instead be forced to use X11 when launched with:

 QT_QPA_PLATFORM=xcb /opt/resolve/bin/resolve

## Exiting “successfully” at start
DaVinci Resolve may be unable to start, yet never exit abnormally (exit code 0) and not produce log files. The standard output of  is something like this:

 ActCCMessage Already in Table: Code= c005, Mode= 13, Level=  1, CmdKey= -1, Option= 0
 ActCCMessage Already in Table: Code= c006, Mode= 13, Level=  1, CmdKey= -1, Option= 0
 ActCCMessage Already in Table: Code= c007, Mode= 13, Level=  1, CmdKey= -1, Option= 0
 ActCCMessage Already in Table: Code= 2282, Mode=  0, Level=  0, CmdKey= 8, Option= 0
 log4cxx: No appender could be found for logger (BtCommon).
 log4cxx: Please initialize the log4cxx system properly.

This state is usually related to lock files. Resolve uses lock files in  to check for a running instance. For a variety of reasons, if Resolve didn’t exit properly the last time around, this lock file will hang around and prevent any new instance of Resolve starting up.

The lock file has the naming scheme  where xxx is some kind of hexadecimal ID. You can manually remove this lock file and Resolve should start up again.

## Unable to download extras
When using the Extras Download Manager to download AI Voice Training data or other additions, all downloads immediately fail with Status Download failed. This is due to a hardcoded TLS certificate path in Resolve. You can manually add a symlink to get the internal downloader to work.

 mkdir -p /etc/pki/
 ln -s /etc/ssl /etc/pki/tls

Extras are stored in /opt/resolve/Extras/, make sure there is enough space left and the account used to start Resolve has write permission.

## Cannot activate license. Please try again later
This error sometimes occurs when activating Davinci Resolve Studio for the first time after a fresh install or update. This can usually be fixed by executing

 sudo chmod -R 7777 /opt/resolve/.license/

Otherwise if you still have the .license folder from your previous installation the issue can also be fixed by copying it over.

## Installed fonts do not show up in DaVinci Resolve
DaVinci Resolve’s “Text” object only attempts to load fonts installed on the system-wide  or  folder. However, the “Text+” object (which is also used for text in Fusion compositions) only loads fonts from .

If you aren't finding a font that you installed, check if it is installed in  (system-wide fonts) instead of  (system-wide fonts) or  (user fonts). It is possible to create a symlink inside  that points to . However, this is not recommended, as this directory is managed by pacman and may lead to conflicts with font packages.

## Crash when clicking key in Fusion tab
Fusion seems to require the US-locales, add them and generate locales Locale#Generating locales :

## Playback only possible in Fairlight
DaVinci Resolve with a Radeon 6700 XT (probably similar cards too) seems to need  and doesn’t work with .

## Davinci Resolve does not start (segfault) when using opencl-amd 7.2
Revert to the last working version of :
 git clone https://aur.archlinux.org/opencl-amd.git
 cd opencl-amd
 git checkout 42c9eb7
 makepkg -si

Additionally, you can block the package from being updated by editing your /etc/pacman.conf file with:
 IgnorePkg = opencl-amd
