[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ardour&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://ardour.org/)

[[]][Official documentation](https://manual.ardour.org/toc/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/ardour)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ardour_(software) "wikipedia:Ardour (software)")

[[]][GitWeb](https://git.ardour.org/ardour/ardour)

[[]][GitHub](https://github.com/Ardour/ardour)

[[]][Bugs (upstream)](https://tracker.ardour.org/)

**Ardour** is a professional grade, multiplatform, digital audio workstation, and hard disk recorder.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Creating a session]](#Creating_a_session)
        -   [[2.2.1] [Screenshots]](#Screenshots)
    -   [[2.3] [Quick start to MIDI recording]](#Quick_start_to_MIDI_recording)
-   [[3] [See also]](#See_also)
-   [[4] [External references]](#External_references)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/ardour](https://packages.gentoo.org/packages/media-sound/ardour) [[]] [Digital Audio Workstation]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`jack`](https://packages.gentoo.org/useflags/jack)               Add support for the JACK Audio Connection Kit
  [`phonehome`](https://packages.gentoo.org/useflags/phonehome)     contact ardour.org at startup for new announcements
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-12 17:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install Ardour:

`root `[`#`]`emerge --ask media-sound/ardour`

### [Additional software]

[JACK](https://wiki.gentoo.org/wiki/JACK "JACK") is a good audio backend choice for working with Ardour. To use Ardour with JACK, make sure it is properly installed and working.

See the article on [music production](https://wiki.gentoo.org/wiki/Music_production "Music production") for software to use in conjunction with Ardour.

## [Usage]

This section aims to provide basic Ardour usage information, to get started recording and editing audio for novice users.

### [Invocation]

Ardour should be found in the desktop environment menu under \"Multimedia\". It may also be started with the [ardour8] command (where the number 8 is Ardour\'s current version and so may change):

`user `[`$`]`ardour8 --help`

    Usage: Ardour [ OPTIONS ] [ SESSION-NAME ]

    Ardour is a multichannel hard disk recorder (HDR) and digital audio workstation (DAW).

    Options:
      -a, --no-announcements      Do not contact website for announcements
      -A, --actions               Print all possible menu action names
      -b, --bindings              Display all current key bindings
      -B, --bypass-plugins        Bypass all plugins in an existing session
      -c, --name <name>           Use a specific backend client name, default is ardour
      -d, --disable-plugins       Disable all plugins (safe mode)
      -h, --help                  Print this message
      -k, --keybindings <file>    Path to the key bindings file to load
      -m, --menus file            Use "file" to define menus
      -n, --no-splash             Do not show splash screen
      -N, --new <session-name>    Create a new session from the command line
      -O, --no-hw-optimizations   Disable h/w specific optimizations
      -P, --no-connect-ports      Do not connect any ports at startup
      -S, --sync                  Draw the GUI synchronously
      -T, --template <name>       Use given template for new session
      -v, --version               Print version and exit

    Report bugs to http://tracker.ardour.org
    Website http://ardour.org

### [Creating a session]

When starting Ardour, it will show a \"Session Setup\" dialog (this may be obstructed by the splash screen, use the taskbar to bring the dialog forward, or [Alt]+click the window to move it). A session stores the Ardour state and Data for a project. Click the \"New session\" button at the top of the dialog to follow on with this article, otherwise a pre-existing session may be opened.

In the next \"Session setup\" dialog, select a session template depending on the work planned - to follow on with this article, select \"Recording session\". The session can be given a descriptive name, and the location to save the files can be chosen. Click \"Open\" once everything is correctly selected.

In the next (\"Audio/MIDI setup\") dialog, configure the audio setup. To follow the rest of this article, select [JACK](https://wiki.gentoo.org/wiki/JACK "JACK"), which is a good choice for audio quality, latency, and flexibility - JACK must be properly installed and configured, and the global \"jack\" [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") should probably be set. Choose the sound device (with jack, all inputs and outputs necessary should be on the same device). Change any other parameters necessary, though the defaults will probably be fine. When done, click \"Start\" to launch JACK (if it is not already running, and if \"Autostart\" was left enabled), and open the main Ardour windows.

A \"Template setup\" dialog will pop up, proposing to create one or more new (audio) tracks. If only [MIDI](https://wiki.gentoo.org/wiki/MIDI_controller_guide "MIDI controller guide") tracks are required, click \"cancel\" in this dialog.

#### [Screenshots]

-   ::::::
    ::::
    :::
    [![](/images/thumb/f/fe/Ardour_session_setup.png/250px-Ardour_session_setup.png)](https://wiki.gentoo.org/wiki/File:Ardour_session_setup.png)
    :::
    ::::

    ::: gallerytext
    Session setup dialog.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/9/98/Ardour_session_setup2.png/227px-Ardour_session_setup2.png)](https://wiki.gentoo.org/wiki/File:Ardour_session_setup2.png)
    :::
    ::::

    ::: gallerytext
    Second session setup dialog.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/8/85/Ardour_audio_midi_setup.png/250px-Ardour_audio_midi_setup.png)](https://wiki.gentoo.org/wiki/File:Ardour_audio_midi_setup.png)
    :::
    ::::

    ::: gallerytext
    Audio/MIDI setup dialog.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/5/5a/Ardour_template_setup.png/250px-Ardour_template_setup.png)](https://wiki.gentoo.org/wiki/File:Ardour_template_setup.png)
    :::
    ::::

    ::: gallerytext
    Template setup dialog.
    :::
    ::::::

### [Quick start to MIDI recording]

[![](/images/thumb/d/d7/Ardour_main_window.png/300px-Ardour_main_window.png)](https://wiki.gentoo.org/wiki/File:Ardour_main_window.png)

[](https://wiki.gentoo.org/wiki/File:Ardour_main_window.png "Enlarge")

Ardour main window (after MIDI track added).

[![](/images/thumb/9/95/Ardour_add_track.png/300px-Ardour_add_track.png)](https://wiki.gentoo.org/wiki/File:Ardour_add_track.png)

[](https://wiki.gentoo.org/wiki/File:Ardour_add_track.png "Enlarge")

Add Track/Bus/VCA dialog.

To record a MIDI track, click the large \"Rec\" (text) button at the top right of the main window (or in the menu: \"Window-\>Recorder-\>Show Recorder\"), to show the recorder pane. To add a MIDI track, in the menu, click \"Track-\>Add Track, Bus or Vca\", then select the \"MIDI tracks\" tab on the left of the new window. Select an instrument from the list in this \"Add Track/Bus/VCA\" dialog, such as the \"ACE Reasonable Synth\" which is provided with Ardour (other instruments should be available if they are installed as plugins).

If a physical MIDI instrument, such as a keyboard, is correctly set up with [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA"), it should now play by default, with audio output. If not, the connection managers from the \"Window\" menu may help: \"MIDI Connections\", \"Audio Connections\", and \"Tracks and busses\". The [[[media-sound/qjackctl]](https://packages.gentoo.org/packages/media-sound/qjackctl)[]] or [[[media-sound/vmpk]](https://packages.gentoo.org/packages/media-sound/vmpk)[]] packages may also be of use.

To record, once an instrument is working, the track must first be \"armed\" by clicking on the button with the red circle *to the left of the newly added track line*. **This will not start recording**, it just marks this track for recording to.

Next, arm Ardour for recording by clicking the button with the red circle in the transport group *at the top left of the main window*. **This will not start recording** either - the button will flash, and Ardour is \"armed\" to start recording.

Now, to actually start recording, either press the \"play\" button to the left of the Ardour \"arm recording\" button, or press [space]. To stop, press the \"stop\" button to the left of the Ardour \"arm recording\" button, or press [space]. Be aware that stopping recording will \"disarm\" Ardour, so be sure to \"re-arm\" to record again. Also note that pressing the Ardour record button during recording will halt input, but will not stop the transport.

## [See also]

-   [List of music production software](https://wiki.gentoo.org/wiki/List_of_music_production_software "List of music production software") --- Gentoo can be a good platform for **music production**.

## [External references]

[Instruments for Use with Ardour 3](https://ardour.org/instruments.html) - some suggested instruments to play sound into Ardour.