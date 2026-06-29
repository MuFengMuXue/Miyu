# Introduction

In Windows Vista, Microsoft rewrote most of their audio systems. There
are a number of audio APIs in the Windows API, notably dsound.dll,
mmdevapi.dll, winmm.dll, and xaudio2\*.dll. WinMM and DSound can be
considered "legacy" APIs. For Windows Vista, Microsoft rewrote the
legacy APIs to route their audio through the main audio system called
MMDevAPI. Around the same time, the XAudio2 APIs were introduced as a
replacement for dsound. More information can be found on [MSDN's
User-Mode Audio Components
page](https://msdn.microsoft.com/en-us/library/dd316780%28v=vs.85%29.aspx).

Wine's audio DLLs are implemented similarly. All of our audio DLLs route
through MMDevAPI. Wine's MMDevAPI currently supports several backends:
ALSA, PulseAudio, OSSv4, and CoreAudio on OS X.

## Limitations

Wine's audio systems require a lot from your system's audio libraries.
It relies on your system to perform mixing of separate audio streams, as
well as to provide resampling. On modern ALSA machines, the "default"
device can typically do both. However, if you configure Wine or another
application to use your audio hardware directly (the "hw:0" interface,
for example), you may find that only a single audio stream will play,
which can cause audio problems in many applications. Please be sure to
use only interfaces which support multiple streams.

## System sounds

Ever missed the 'Ding' system sound and other standard Windows audio
cues? Wine can play them if you tell it where to find PCM .wav files.
Because every UNIX is different, Wine can't guess where to find them.
See bug #21277 and add a section like this to your `drive_c/windows/win.ini`

```
[Sounds]
Default=/usr/share/sounds/question.wav
SystemExclamation=/usr/share/sounds/error.wav
```

Of course you must substitute paths to .wav PCM files found on your
disk. Either UNIX or DOS pathname syntax is acceptable.

# Help! My sound isn't working!

Here is some information about how to debug sound issues, or give the
developers enough information to help you.

Make sure that Wine chose the correct driver backend. Wine should
select the correct backend for you. If you don't know which backend is
correct, this is probably not your problem. To see which backend Wine
chose, launch the Wine configuration program `winecfg` and click the
Audio tab.  If you are using a Wine prefix from an older version of
Wine, you may have an incompatible driver hard-coded into the
registry. Please delete the Audio entry inside of the
`[HKEY_CURRENT_USER\Software\Wine\Drivers]` registry key with the
[regedit](Commands/regedit) program. If none of the above apply and
Wine is failing to select the correct backend, then you have
encountered a bug in Wine's automatic driver selection and you should
[report it](Bugs).

If Wine is using the correct backend and audio still does not work,
please consider [filing a bug](Bugs). See below for a list of
information to include when filing a bug.

One thing you can try is switching Wine's compatibility mode between
Windows 7 and Windows XP. Recent applications will detect the Windows
version and either use the legacy APIs for pre-Vista operating systems,
or the new MMDevAPI or XAudio2 modules for post-Vista operating systems.
Choosing either Windows 7 or Windows XP may cause your application to
use a different audio system, which may have better success. Please
consider [filing a bug](Bugs) if you find that your
application's audio works in one mode but not the other, as Wine should
support both.

## SDL applications

SDL is a cross-platform graphics and sound library commonly used by
games. The Windows SDL library contains support for several audio
backends, such as "winmm" and "dsound". If the `SDL_AUDIODRIVER`
environment variable is set, then SDL loads the matching backend, or
fails if the backend isn't available.

Since SDL is a cross-platform library, it has this same functionality on
Linux. Accordingly, some Linux distributions' SDL package will set the
`SDL_AUDIODRIVER` environment variable to match the Linux backend so
that SDL-using Linux applications will use the appropriate backend (e.g.
"pulse").

But this creates problems for SDL applications run in Wine. The Windows
SDL library loads the Linux `SDL_AUDIODRIVER` environment variable,
which contains "pulse" or some other invalid backend for the Windows SDL
library, and so audio fails to initialize in SDL-using Windows
applications run through Wine.

The solution here is to unset your `SDL_AUDIODRIVER` environment
variable before running Wine. This should restore your audio, as SDL
will fall back on one of its default Windows drivers. Alternatively, you
can create a new registry entry which will override the
`SDL_AUDIODRIVER` environment variable for your Wine prefix:

```
[HKLM\System\CurrentControlSet\Control\Session Manager\Environment]
SDL_AUDIODRIVER=""
```

There is a patch available
[here](https://bugs.winehq.org/attachment.cgi?id=37173) which adds this
environment variable override automatically. Packagers may find it
useful.

## OpenAL source limit

Many modern games and applications use the xaudio2 API. For a [small
handful of applications](#39591), Wine may issue this warning:

`warn:xaudio2:OpenAL ran out of sources, consider increasing its source limit.`

This means the application tried to create very many audio voices, and
your OpenAL implementation refuses to create that many. To fix this,
you can configure openal-soft to allow more voices. Edit the OpenAL
configuration file. Possible paths include
`$HOME/.config/alsoft.conf`, `$HOME/.alsoftrc`, or
`/etc/openal/alsoft.conf`. You can use the Apply button in the
`alsoft-config` program to generate this file, and then edit it
manually. Add this section to the file:

```
[General]
sources=1024
```

This will increase the source voice limit to 1,024. If you continue to
get the warning, feel free to increase it further, though be aware that
some poorly behaved OpenAL applications may not react well to very many
OpenAL sources.

## DirectMusic support

Wine's directmusic implementation (dmusic, dmime, dmloader, etc) is very
incomplete. If your application uses directmusic for its audio, then it
will not play audio. This includes most games made with GameMaker.
However, installing both "directmusic" and "dsound" using
[winetricks](Winetricks) should give you working audio.

## What to include when filing a bug

In addition to the usual [bug guidelines](Bugs), please also
include all of the following information:

- Audio driver being used
- Operating system
- If possible, a
  `+tid,+seh,+mmdevapi,+winmm,+driver,+msacm,+midi,+dsound,+dsound3d,+xaudio2,+xapofx,+dmusic,+mci,+pulse,+oss,+alsa,+coreaudio,+timestamp`
  [log](FAQ#how-do-i-get-a-debug-trace). These can get
  very large very quickly, so try to do enough to trigger the bug, but
  no more.

# Backend information

## PulseAudio

Wine has official support for PulseAudio. The driver should work well,
but there are some known issues with unusual audio buffer and latency
settings. If you find you are having choppy or no audio with some
applications, then check to ensure the PULSE_LATENCY_MSEC variable is
unset, and that you're using default buffering values in
`/etc/pulse/daemon.conf`. Certain audio devices, especially USB audio
devices, can cause PulseAudio to use different latency and buffering
settings, which can cause issues with Wine. [This is a known bug in
Wine](#39814).

## ALSA

Wine does its best to probe your system for information about the
available devices, but ALSA's device enumeration does not work very
well. Wine will detect your hardware devices, but it may not be able to
find software devices you have configured. To tell Wine about these
devices, please set the following registry keys:

```
HKCU\Software\Wine\Drivers\winealsa.drv\ALSAOutputDevices  #Multi-string value containing output interface names
HKCU\Software\Wine\Drivers\winealsa.drv\ALSAInputDevices  #Multi-string value containing input interface names
```

You can specify them as defaults in the Audio tab in winecfg.

# What about JACK?

[JACK](https://jackaudio.org/), the low-latency sound server, had a
driver in the old driver architecture. It has been removed as part of
the transition to MMDevAPI. This means that there is no JACK support in
Wine at this time. If a developer is sufficiently motivated, they could
implement an audio driver to restore support for JACK. The new driver
would be expected to pass all tests, especially those in
<dlls/mmdevapi/tests>, <dlls/winmm/tests>, and <dlls/dsound/tests>. An
external git tree, frequently synced with main Wine, would be the best
way to start. If this is a project you think you might undertake, please
contact the wine-devel mailing list before you begin.

Users wanting to create a "bridge" to forward Wine's ALSA output to JACK
can find streamlined setup instructions
[here](https://gamesplusone.com/alsa_to_jack.html).

[WineASIO](https://sourceforge.net/projects/wineasio/) users need not
fear! WineASIO's implementation is completely separate from the old
drivers. If your application does all of its audio IO through ASIO, then
your audio experience should not change.

# See Also

- [MIDI](MIDI)
