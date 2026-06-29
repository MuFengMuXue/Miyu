**Resources**

[[]][Home](https://cmus.github.io/)

[[]][Official documentation](https://cmus.github.io/#documentation)

[[]][Official project wiki](https://github.com/cmus/cmus/wiki/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/cmus)

[[]][GitHub](https://github.com/cmus/cmus)

[[]][Bugs (upstream)](https://github.com/cmus/cmus/issues)

[[]][Wikipedia](https://en.wikipedia.org/wiki/cmus "wikipedia:cmus")

[**cmus**] is a small, fast, and powerful console music player for Unix-like operating systems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Starting Cmus]](#Starting_Cmus)
    -   [[2.2] [Adding Music]](#Adding_Music)
    -   [[2.3] [Playing Tracks From The Library]](#Playing_Tracks_From_The_Library)
    -   [[2.4] [Settings]](#Settings)
-   [[3] [Keys]](#Keys)
    -   [[3.1] [Changing views]](#Changing_views)
    -   [[3.2] [Navigation and track selection]](#Navigation_and_track_selection)
    -   [[3.3] [Volume control]](#Volume_control)
    -   [[3.4] [Searching]](#Searching)
    -   [[3.5] [Playback control]](#Playback_control)
    -   [[3.6] [Managing playlists and queues]](#Managing_playlists_and_queues)
-   [[4] [Configuration]](#Configuration)
-   [[5] [Colors]](#Colors)
    -   [[5.1] [The playlist]](#The_playlist)
    -   [[5.2] [Search]](#Search)
    -   [[5.3] [Tree view]](#Tree_view)
    -   [[5.4] [Quit]](#Quit)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/cmus](https://packages.gentoo.org/packages/media-sound/cmus) [[]] [Ncurses based music player with plugin support for many formats]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+flac`](https://packages.gentoo.org/useflags/+flac)                   Add support for FLAC: Free Lossless Audio Codec
  [`+mad`](https://packages.gentoo.org/useflags/+mad)                     Add support for mad (high-quality mp3 decoder library and cli frontend)
  [`+unicode`](https://packages.gentoo.org/useflags/+unicode)             Add support for Unicode
  [`+vorbis`](https://packages.gentoo.org/useflags/+vorbis)               Add support for the OggVorbis audio codec
  [`aac`](https://packages.gentoo.org/useflags/aac)                       Enable support for MPEG-4 AAC Audio
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                     Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`ao`](https://packages.gentoo.org/useflags/ao)                         Use libao audio output library for sound playback
  [`cddb`](https://packages.gentoo.org/useflags/cddb)                     Access cddb servers to retrieve and submit information about compact disks
  [`cdio`](https://packages.gentoo.org/useflags/cdio)                     Use libcdio for CD support
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`discid`](https://packages.gentoo.org/useflags/discid)                 Enable reading the ID of the inserted CD
  [`elogind`](https://packages.gentoo.org/useflags/elogind)               Enable MPRIS support via sys-auth/elogind
  [`examples`](https://packages.gentoo.org/useflags/examples)             Install examples, usually source code
  [`ffmpeg`](https://packages.gentoo.org/useflags/ffmpeg)                 Enable ffmpeg/libav-based audio/video codec support
  [`jack`](https://packages.gentoo.org/useflags/jack)                     Add support for the JACK Audio Connection Kit
  [`libsamplerate`](https://packages.gentoo.org/useflags/libsamplerate)   Build with support for converting sample rates using libsamplerate
  [`mikmod`](https://packages.gentoo.org/useflags/mikmod)                 Add libmikmod support to allow playing of SoundTracker-style music files
  [`modplug`](https://packages.gentoo.org/useflags/modplug)               Add libmodplug support for playing SoundTracker-style music files
  [`mp4`](https://packages.gentoo.org/useflags/mp4)                       Support for MP4 container format
  [`musepack`](https://packages.gentoo.org/useflags/musepack)             Enable support for the musepack audio codec
  [`opus`](https://packages.gentoo.org/useflags/opus)                     Enable Opus audio codec support
  [`oss`](https://packages.gentoo.org/useflags/oss)                       Add support for OSS (Open Sound System)
  [`pidgin`](https://packages.gentoo.org/useflags/pidgin)                 Install support script for net-im/pidgin
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)         Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`sndio`](https://packages.gentoo.org/useflags/sndio)                   Add support for media-sound/sndio
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Enable MPRIS support via sys-apps/systemd
  [`tremor`](https://packages.gentoo.org/useflags/tremor)                 Use libivorbis from media-libs/tremor instead of media-libs/libvorbis
  [`wavpack`](https://packages.gentoo.org/useflags/wavpack)               Add support for wavpack audio compression tools
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-03 22:19] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/cmus`

## [Usage]

### [Starting Cmus]

When launching cmus (just type cmus in a terminal and press Enter) it will open to the album/artist view, which looks something like this:

    +---------------------------------------------------------------------+
    | Artist / Album             Track                            Library |
    |                          |                                          |
    |                          |                                          |
    |                          |                                          |
    |                          |                                          |
    |                          |                                          |
    |                          |                                          |
    |                          |                                          |
    |                                                                     |
    | . 00:00 - 00:00 vol: 100                     all from library | C   |
    |                                                                     |
    +---------------------------------------------------------------------+

** Note**\
This is the default view where artists and albums will be displayed.

### [Adding Music]

To add music to the cmus library, press [5] to switch to the file-browser view.

** Note**\
In the file-browser view, browse through files and directories, and add music files or entire folders to the library.

### [Playing Tracks From The Library]

To start playing tracks from the library, press [2] to go to the simple library view.

    +---------------------------------------------------------------------+
    | Artist / Album            Track                              Library|
    | The Beatles              | Come Together                     04:18  |
    |                          | Something                         03:02  |
    |                          | Maxwell's Silver Hammer           03:27  |
    |                          | Oh! Darling                       03:26  |
    |                          | Octopus's Garden                  02:51  |
    |                          | Here Comes The Sun                03:05  |
    |                          | Because                           02:45  |
    |                          | You Never Give Me Your Money      04:02  |
    |                          | Sun King                          02:26  |
    | . 00:00 - 47:49 vol: 100                     all from library | C   |
    +---------------------------------------------------------------------+

To control the playback, the following keys can be used:

-   Press [C] to pause/unpause.
-   Press [→]/[←] to seek by 10 seconds.

### [Settings]

Cmus offers a variety of customizable settings. Press [7] to go to the settings menu where settings can be changed, new keys bound, and colors changed.

    +---------------------------------------------------------------------+
    | Settings                                                            |
    | aaa_mode                                 all                        |
    | altformat_current                        %F                         |
    | altformat_playlist                       %f%= %d                    |
    | altformat_title                          %f                         |
    | ltformat_trackwin                        %f%= %d                    |
    | auto_expand_albums_follow                true                       |
    |                                                                     |
    | . 00:00 - 2:16:25 vol: 100                                          |
    |                                                                     |
    +---------------------------------------------------------------------+

** Note**\
The continue, repeat, and shuffle options allow playback to be controlled in various ways, such as continuing to the next track, repeating the current track or playlist, or playing tracks in a random order.

## [Keys]

### [Changing views]

-   Press [1] for the library view.
-   Press [3] for the playlist view.
-   Press [4] for the play queue view.
-   Press [6] for the live filter view.
-   Press [8] for the browser view.

### [Navigation and track selection]

-   Press [J] or [↓] to move down.
-   Press [K] or [↑] to move up.
-   Press [L] or [→] to enter directory or play selected track.
-   Press [H] or [←] to navigate to the parent directory.
-   Press [ENTER] to add selected track or all tracks in selected directory to play queue.

### [Volume control]

-   Press [-] to lower the volume.
-   Press [+] to raise the volume.

### [Searching]

-   Press [/] followed by the search term and [ENTER] to search.
-   Press [n] to move to the next match.
-   Press [N] to move to the previous match.

### [Playback control]

-   Press [B] to play the next track in the playlist.
-   Press [Z] to play the previous track in the playlist.
-   Press [X] to stop playing.
-   Press [V] to show/hide the status window.
-   Press [SPACE] to toggle play/pause.

### [Managing playlists and queues]

-   Press [U] to update the database.
-   Press [E] to clear the play queue.
-   Press [SHIFT]+[Y] to add all tracks in the library view to the play queue.
-   Press [Y] to add all tracks in the current view to the play queue.

## [Configuration]

Documented default settings for cmus with detailed descriptions.

For alternative values, please refer to the cmus manual. Additionally, provided a comprehensive table showcasing all available settings.

  ---------------------------- -------------------------------------------------- ----------------------------------------------------------------------------------------------------------------
  Config Option                Value                                              Description
  aaa_mode                     all                                                Sets the behavior for the \'a\' key. \'all\' plays the current track and adds the whole album to the playlist.
  altformat_current            %F                                                 Specifies the alternative format for the current track.
  altformat_playlist           %f%= %d                                            Sets the alternative format for the playlist view.
  altformat_title              %f                                                 Specifies the alternative format for the title line.
  altformat_trackwin           %f%= %d                                            Sets the alternative format for the track window.
  auto_expand_albums_follow    true                                               Automatically expands albums when using the \'follow\' command.
  auto_expand_albums_search    true                                               Automatically expands albums when searching.
  auto_expand_albums_selcur    true                                               Automatically expands albums when selecting the current track.
  auto_reshuffle               true                                               Automatically reshuffles the playlist after reaching the end.
  buffer_seconds               10                                                 Specifies the number of seconds to buffer for gapless playback.
  fset 90s                     date\>=1990&date\<2000                             Defines a filter set named \'90s\' to match tracks with a date between 1990 and 1999.
  fset classical               genre=\"Classical\"                                Defines a filter set named \'classical\' to match tracks with the genre \"Classical\".
  fset missing-tag             album=\"\"\|title=\"\"\|tracknumber=-1\|date=-1)   Defines a filter set named \'missing-tag\' to match tracks with missing tags.
  fset mp3                     filename=\"\*.mp3\"                                Defines a filter set named \'mp3\' to match tracks with the .mp3 file extension.
  fset ogg                     filename=\"\*.ogg\"                                Defines a filter set named \'ogg\' to match tracks with the .ogg file extension.
  fset ogg-or-mp3              mp3                                                Defines a filter set named \'ogg-or-mp3\' to match tracks with either the .ogg or .mp3 file extension.
  fset unheard                 play_count=0                                       Defines a filter set named \'unheard\' to match tracks with a play count of 0.
  factivate                                                                       Activates the last defined filter set.
  input.aac.priority           50                                                 Sets the priority for AAC audio files.
  input.cue.priority           50                                                 Sets the priority for CUE sheet files.
  input.flac.priority          50                                                 Sets the priority for FLAC audio files.
  input.mad.priority           55                                                 Sets the priority for MP3 audio files using the MAD plugin.
  input.mp4.priority           50                                                 Sets the priority for MP4 audio files.
  input.vorbis.priority        50                                                 Sets the priority for Ogg Vorbis audio files.
  input.wav.priority           50                                                 Sets the priority for WAV audio files.
  lib_add_filter                                                                  Specifies additional filtering rules for the library.
  lib_sort                     Sets the sorting rules for the library view.
  mixer.alsa.channel                                                              Specifies the ALSA mixer channel to use for volume control.
  mixer.alsa.device                                                               Specifies the ALSA mixer device to use for volume control.
  mixer.pulse.restore_volume   1                                                  Specifies whether to restore the volume level when restarting cmus with the PulseAudio output plugin.
  mouse                        true                                               Enables mouse support.
  mpris                        true                                               Enables support for the MPRIS D-Bus interface.
  output_plugin                pulse                                              Sets the output plugin for audio playback.
  passwd                                                                          Sets the password for connecting to password-protected streams.
  pause_on_output_change       false                                              Specifies whether to pause playback when changing the output plugin.
  pl_sort                                                                         Specifies the sorting rules for the playlist view.
  play_library                 true                                               Enables playback from the library.
  play_sorted                  false                                              Enables playback from the sorted view.
  repeat                       false                                              Enables repeat mode.
  repeat_current               false                                              Enables repeat current track mode.
  replaygain                   disabled                                           Sets the replay gain mode.
  replaygain_limit             true                                               Specifies whether to apply the replay gain limit.
  replaygain_preamp            0.000000                                           Sets the replay gain pre-amplification level.
  resume                       false                                              Enables resume playback from the last position.
  rewind_offset                5                                                  Sets the rewind offset in seconds.
  scroll_offset                2                                                  Sets the scroll offset for lists and windows.
  set_term_title               true                                               Sets the terminal window title.
  show_all_tracks              true                                               Specifies whether to show all tracks in the library view.
  show_current_bitrate         false                                              Specifies whether to display the current bitrate in the status line.
  show_hidden                  false                                              Specifies whether to show hidden files and directories.
  show_playback_position       true                                               Specifies whether to display the playback position in the status line.
  show_remaining_time          false                                              Specifies whether to display the remaining time in the status line.
  shuffle                      off                                                Sets the shuffle mode.
  skip_track_info              false                                              Specifies whether to skip track information when available.
  smart_artist_sort            true                                               Enables smart sorting for artist names.
  softvol                      false                                              Enables software volume control.
  softvol_state                0 0                                                Sets the initial software volume control state.
  start_view                   tree                                               Sets the initial view when starting cmus.
  status_display_program                                                          Specifies a custom program to display the status line.
  stop_after_queue             false                                              Specifies whether to stop playback after the queue has been played.
  time_show_leading_zero       true                                               Specifies whether to show leading zeros in time displays.
  tree_width_max               0                                                  Sets the maximum width of the tree view.
  tree_width_percent           33                                                 Sets the width percentage for the tree view.
  wrap_search                  true                                               Specifies whether to wrap around when searching.
  device                       /dev/cdrom                                         Sets the device to use for CD playback.
  display_artist_sort_name     false                                              Specifies whether to display the artist\'s sort name instead of the artist name.
  dsp.alsa.device                                                                 Specifies the ALSA device to use for audio output.
  follow                       false                                              Sets the behavior for the \'f\' key. \'false\' disables auto-following.
  icecast_default_charset      ISO-8859-1                                         Sets the default character set for Icecast streams.
  id3_default_charset          ISO-8859-1                                         Sets the default character set for ID3 tags.
  confirm_run                  true                                               Enables confirmation prompt before executing shell commands.
  continue                     true                                               Enables continuous playback when reaching the end of the playlist.
  continue_album               true                                               Enables continuous playback when reaching the end of an album.
  ---------------------------- -------------------------------------------------- ----------------------------------------------------------------------------------------------------------------

## [Colors]

In Cmus, a custom theme can be specified by \'theme_name\' or by editing the colors directly in the [\~/.config/cmus/autosave] file. Alternatively, the [7] key can be pressed in the player to open the settings, and if the mouse is enabled, right-click to generate the setting in the command line. Alternatively, navigate to the option in the list and press Enter. For certain settings, press the [tab] key after selecting the option and delete the current value to display alternatives.

Below are all the possible options with explanations. Colors can be selected by their names, such as \'red\', or by the corresponding ANSI color codes from 0 to 256.

-   0: Black
-   1: Red
-   2: Green
-   3: Yellow
-   4: Blue
-   5: Magenta
-   6: Cyan
-   7: White

When using ANSI color codes ranging from 1 to 256 to specify colors, it can be helpful to display a list of possible colors. To display a list, copy and paste the following code into the terminal:

[CODE] **Color printing example (ANSI)**

    awk 'BEGIN '

  --------------------------------- ------------- ------------------------------------------------------------------------------------------------
  Config option                     Value         Description
  color_cmdline_attr                default       Sets the attribute color for the command line.
  color_cmdline_bg                  default       Sets the background color for the command line.
  color_cmdline_fg                  default       Sets the foreground color for the command line.
  color_cur_sel_attr                default       Sets the attribute color for the currently selected item.
  color_error                       lightred      Sets the color for error messages.
  color_info                        lightyellow   Sets the color for informational messages.
  color_separator                   blue          Sets the color for separators.
  color_statusline_attr             default       Sets the attribute color for the status line.
  color_statusline_bg               gray          Sets the background color for the status line.
  color_statusline_fg               black         Sets the foreground color for the status line.
  color_titleline_attr              default       Sets the attribute color for the title line.
  color_titleline_bg                blue          Sets the background color for the title line.
  color_titleline_fg                white         Sets the foreground color for the title line.
  color_trackwin_album_attr         bold          Sets the attribute color for the album name in the track window.
  color_trackwin_album_bg           default       Sets the background color for the album name in the track window.
  color_trackwin_album_fg           default       Sets the foreground color for the album name in the track window.
  color_win_attr                    default       Sets the attribute color for the windows.
  color_win_bg                      default       Sets the background color for the windows.
  color_win_cur                     lightyellow   Sets the color for the currently selected item in the windows.
  color_win_cur_attr                default       Sets the attribute color for the currently selected item in the windows.
  color_win_cur_sel_attr            default       Sets the attribute color for the currently selected and playing item in the windows.
  color_win_cur_sel_bg              blue          Sets the background color for the currently selected and playing item in the windows.
  color_win_cur_sel_fg              lightyellow   Sets the foreground color for the currently selected and playing item in the windows.
  color_win_dir                     lightblue     Sets the color for directories in the windows.
  color_win_fg                      default       Sets the foreground color for the windows.
  color_win_inactive_cur_sel_attr   default       Sets the attribute color for the inactive currently selected and playing item in the windows.
  color_win_inactive_cur_sel_bg     gray          Sets the background color for the inactive currently selected and playing item in the windows.
  color_win_inactive_cur_sel_fg     lightyellow   Sets the foreground color for the inactive currently selected and playing item in the windows.
  color_win_inactive_sel_attr       default       Sets the attribute color for the inactive selected item in the windows.
  color_win_inactive_sel_bg         gray          Sets the background color for the inactive selected item in the windows.
  color_win_inactive_sel_fg         black         Sets the foreground color for the inactive selected item in the windows.
  color_win_sel_attr                default       Sets the attribute color for the selected item in the windows.
  color_win_sel_bg                  blue          Sets the background color for the selected item in the windows.
  color_win_sel_fg                  white         Sets the foreground color for the selected item in the windows.
  color_win_title_attr              default       Sets the attribute color for the window titles.
  color_win_title_bg                blue          Sets the background color for the window titles.
  color_win_title_fg                white         Sets the foreground color for the window titles.
  --------------------------------- ------------- ------------------------------------------------------------------------------------------------

  : Configuration options

### [The playlist]

The playlist works like another library (like view 2) except that (like the queue) you manually set the order of the tracks. This can be quite useful when creating a mix of specific tracks or to listen to an audio book without having the chapters when playing \"all from library\".

The playlist is on view 3. But before we go there, let\'s add some tracks. Press [2] to go to the simple library view, go to a desired track and press [Y] to add it to the playlist. The visual feedback will present the highlighting of the track and the cursor will move down one row. Select a few more tracks for a working list.

Now press [3] to go to the playlist.

Just like the queue, use the [P], [SHIFT]+[P], and [SHIFT]+[D] keys to move and delete tracks from the playlist.

** Note**\
Changing the view (e.g., by pressing [3]) does not affect what cmus will play next. To put cmus into \"play from the playlist\" mode, press [ENTER] on one of the tracks in the playlist. To switch modes without interrupting the currently-playing song, you can press [SHIFT]+[M].

### [Search]

Press [2] to be sure the simple library view is shown, then press [/] to start a search. Type a word or two from the track to be queried. cmus will search for all tracks that have all those words in their titles. Press [ENTER] to get the keyboard out of the search command, and [N] to find the next match.

### [Tree view]

Press [1] to select the tree view. Scroll to the artist, press [SPACE] to show their albums, scroll to the desired album, then press [TAB] so the keyboard controls the right column. Press [TAB] again to get back to the left column.

### [Quit]

When done, type [:q] and press Enter to quit. This will save the settings, library, playlist, and queue.

## [See also]

-   [VLC](https://wiki.gentoo.org/wiki/VLC "VLC") --- a wildly popular, cross platform video player and streamer.