MIDI should work in Wine as long as it works on your system in general,
with some caveats.

## Using MIDI with UNIX

There is no point in writing to the Wine bug tracker if MIDI does not
work on your UNIX system.

On Linux, `aconnect -o` lists the MIDI output ports known to ALSA. Of
these, `MIDI through` is of no use to you unless you have dedicated MIDI
hardware. It (presumably) sends bytes down the serial port where you
have no HW connected, so you hear no music.

If other ports are listed along with their number, verify that
`aplaymidi -p128:0 myfile.mid` produces sound. 128 is the port number
that software sequencers like Timidity and FluidSynth use by default.
Here's output from a system equipped with both FluidSynth and Timidity
simultaneously (and FluidSynth started first):

    $ aconnect -o
    client 14: 'Midi Through' [type=kernel]
        0 'Midi Through Port-0'
    client 128: 'FLUID Synth (31186)' [type=user]
        0 'Synth input port (31186:0)'
    client 129: 'TiMidity' [type=user]
        0 'TiMidity port 0 '
        1 'TiMidity port 1 '
        2 'TiMidity port 2 '
        3 'TiMidity port 3 '

The Linux kernel includes a mapper from OSS to ALSA. That's how
applications using the OSS API to play MIDI still get output from ALSA
sequencers like Timidity.

Sound from `aplaymidi -px:y file.mid` is the basic proof that your MIDI
setup is working in Linux. This is not necessarily enough to make it
work in Wine because Wine may end up using the silence "MIDI through"
port.

### Software sequencers like Timidity and FluidSynth

Installing Timidity or FluidSynth is not enough. These software
synthesizers need digitized sound sample collections (called patches and
soundfonts) to produce anything but silence. Depending on your package
management and package dependencies, you may need to additionally
install one of these or configure the software to use your soundfonts.
Freepats and Unison are examples of such patch collections.

You can start FluidSynth as follows:

```
fluidsynth -l -s -i -aalsa -o audio.alsa.device=default /usr/share/midi/sf2/mypatches.sf2
```

You can start Timidity as follows:

```
timidity -iAD -B2,8 -Os1l -s 44100 -x'soundfont /usr/share/midi/sf2/mypatches.sf2 order=1'
```

### Mac OS X

CoreAudio supports MIDI and Wine should be able to use it out of the box.

### Linux

- Fedora:
  Some ALSA/MIDI package is missing on a default install? (please check)

- Ubuntu: ?? (please check)
  In older versions of Ubuntu introducing PulseAudio, whatever application
  started using ALSA first would prevent the others from accessing it. For
  instance, any application using PulseAudio would prevent Timidity from
  producing sound. Conversely, playing a MIDI file would prevent
  PulseAudio from working.

- Debian: ??

- openSUSE: ?? (nothing known)

## Using MIDI in Wine

There is no point in creating an application-specific MIDI bug entry if
you have not verified that at least one other application in Wine is
able to play MIDI in Wine on your system.

### The MCI shell

One such application is the interactive MCI shell attached to [bug
\#20232, comment
\#10.](https://bugs.winehq.org/show_bug.cgi?id=20232#c10) It allows you
to send MCI string commands to any device. A sample session goes like
this:

    $ wine wintest.exe mcishell
    mci.c:891: Type your commands to the MCI, end with Ctrl-Z/^D
    open z:\home\me\Documents\file.mid alias m
    play m from 0
    status m position
    close m
    ^D <- Ctrl-D to end the session in UNIX, Ctrl-Z in DOS

Since wine-1.1.41, the MCI sequencer allows to select the MIDI device
instead of defaulting to the mapper.

    open ...
    status m port
    set m port mapper
    set m port 0
    set m port 1
    play m ...

You can use the MCI shell to play any .wav sample (even .mp3 depending
on your setup) as well as your audio CD and even play .avi files.

The MCI is just one of 4 API in MS-Windows to produce MIDI music. The
others are: midiOutOpen, midiStreamOpen (both in WINMM) and DirectMusic.

DirectMusic support is incomplete in Wine. Several apps have been
reported to work fine with native versions of the 5 dlls that belong to
DirectMusic.

### Selecting the Output - the MIDI mapper

The MIDI mapper is the default device on MS-Windows that almost every
MIDI playing application uses. It forwards MIDI commands to other MIDI
devices, depending on its configuration. Most applications will not let
you choose the MIDI output device -- they simply assume that the mapper
was correctly configured.

In Wine, the mapper forwards to the first device (number 0) by default.
`winmm:midiOutOpen` uses these exact same numbers. Wine associates one
device with every port (as known from aconnect). The order is shown in
winecfg, with device \#0 occuring topmost. If this happens to be the
"MIDI through" port on your system with SW-only synthesizers, you need
to change the configuration via the registry.

On one Ubuntu system equipped with both ALSA and OSS but lacking a HW
synthesizer, the ordering of the devices differs among ALSA and OSS! The
"MIDI through" port occurs last in the ALSA list of devices, but first
in the OSS list of devices (as seen in winecfg). This explains why an
applications therein manages to produces sound effects and MIDI music
with ALSA but is missing the MIDI music with OSS. (Actually you can use
`aconnect` to tap one port's output with another port's input and manage
to hear music originally sent to the "MIDI through" port, but that
consumed undue amounts of CPU% so I'll not explain the details here).

The [Midi mapper chapter of the Wine Developer's
Guide](Wine-Developer's-Guide/Wine-and-Multimedia#midi-mapper-midimap)
describes the registry entries used by the MIDI mapper and how to have
it use another device. You can either select the device by name or use
the "#1" notation to select it by number (again with device \#0 topmost
in winecfg). Feed this `.ini` file to regedit to have the mapper select
the *second* device in winmm & winecfg's list:

    REGEDIT4

    [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Multimedia\MIDIMap]
    "CurrentInstrument"="#1"

You can trace the mapper with `WINEDEBUG=+msacm wine app.exe`.

## Checklist prior to reporting a bug

`aconnect -o` lists relevant entries.

`aplaymidi -pX:Y file.mid` works -- or whatever is equivalent in your
OS.

winecfg's audio tab lists these same entries (in Linux, ideally with
both ALSA and OSS, although you can use only one inside one Wine
session)

You configured the registry for the MIDI mapper in case the topmost
device in winecfg's list is not one known working.

You tested basic MIDI playing ability using the interactive MCI shell or
you know that MIDI performs well with another application in Wine on
your system.

### Useful information to include in your bug report

- See [bug reporting guidelines](Bugs)
- Your OS and audio system (ALSA, OSS)
- Is it a regression? See [Regression
  Testing](Regression-Testing)
- Did you walk through this checklist?
- Many things can still go wrong and there are several known issues.
  You'll likely be asked to produce a `WINEDEBUG` trace using a choice
  among
  `+mci, +mcimidi, +driver, +mmsys, +winmm, +midi, +msacm and +tid`.
