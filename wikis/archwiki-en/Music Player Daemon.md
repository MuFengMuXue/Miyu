# Music Player Daemon

Music Player Daemon (MPD) is an audio player that has a server-client architecture. MPD plays audio files, organizes playlists and maintains a music database, all while using  very few resources. In order to interface with it, a separate client is needed.

 is an alternative to MPD written in Python. It is not a complete MPD replacement—its advantage is that it has plug-ins for playing music from cloud services like Spotify, SoundCloud, and Google Play Music.

## Installation
Install the  package.

## Configuration
MPD is able to run in #Per-user configuration or #System-wide configuration mode (settings apply to all users). Also it is possible to run multiple instances of MPD in a #Multi-MPD setup.
The way of setting up MPD depends on the way it is intended to be used: a local per-user configuration is easier to set up and may prove more adapted on a desktop system. The system-wide setup might be better suited for a always-on audio server with multiple users but a shared MPD instance.

In order for MPD to be able to playback audio, ALSA, optionally with PulseAudio or PipeWire, must be set up and working. The #Audio configuration section thereafter describes the parameters needed for ALSA, PulseAudio or PipeWire.

MPD is configured in the file  which can be located in various paths depending on the setup chosen (system-wide or per-user). In short, the two common locations used are:
#  in per-user configuration mode, this is the first location searched,
#  in system-wide configuration.

These are some of the most commonly used configuration options:
*  -  The file where MPD stores its process ID
*  - The music database
*  - MPD's current state is noted here
*  - The directory where playlists are saved into
*  - The directory that MPD scans for music
*  - The sticker database

## Per-user configuration
MPD can be configured per-user. Running it as a normal user has the benefits of:

* Regrouping into one single directory  (or any other directory under ) all the MPD configuration files.
* Avoiding unforeseen directory and file permission errors.

## Configure the location of files and directories
In user mode, the configuration is read from .
We will assume here  equals the default of .

To build the user configuration, the MPD configuration example included in the package is a good starting point, copy it using the following lines:

 $ mkdir -p ~/.config/mpd
 $ cp /usr/share/doc/mpd/mpdconf.example ~/.config/mpd/mpd.conf

A good practice is to use this newly created  directory to store, together with the configuration file, other MPD related files like the database or the playlists. The user must have read write access to this directory.

Then edit the configuration file in order to specify the required and optional files and directories:

If playlists are enabled in the configuration, the specified playlist directory must be created:

 $ mkdir ~/.config/mpd/playlists

If  is set, the specified directory must be created:

 $ mkdir -p ~/.local/state/mpd

MPD can now be started (an optional custom location for the configuration file can be specified):

 $ mpd In order to build the database file, MPD must scan into the  defined above. To request this task, one of the MPD clients must be used. For example with mpc'' the command is:

 $ mpc update

or alternatively one can set the option  to  in the configuration to refresh the database whenever files are changed in .

## Audio configuration
By default, no audio outputs are configured, which leads MPD to perform auto-detection using ALSA. However, it is possible to configure outputs manually; MPD even supports the ability to emit to more than one at once.

All audio outputs accept a  setting, which is displayed by MPD clients in output control dialogs. ([https://mpd.readthedocs.io/en/stable/user.html#configuring-audio-outputs Full list of common settings)

The exact ALSA device can be indicated with the  option; devices can be listed using  from the package . (Full list of ALSA-specific settings)
{{hc|~/.config/mpd/mpd.conf|2=
audio_output {
        type          "alsa"
        name          "ALSA sound card"
        # Optional
        #device        "iec958:CARD=Intel,DEV=0"
        #mixer_control "PCM"
}
}}

The following configures a PulseAudio output (list of specific settings). Sink identifiers can be obtained with .
{{hc|~/.config/mpd/mpd.conf|2=
audio_output {
        type            "pulse"
        name            "PulseAudio output"
        # Optional
        #sink            "alsa_output.pci-0000_c1_00.6.analog-stereo"
}
}}

The following configures a PipeWire output (list of specific settings). Target identifiers can be obtained with  as the  property; audio outputs can be identified by the  property (or obtained via , if available).
{{hc|~/.config/mpd/mpd.conf|2=
audio_output {
        type            "pipewire"
        name            "PipeWire output"
        # Optional
        #target          "bluez_output.F4_9D_8A_B4_8D_37.1"
}
}}

## Listen on Unix domain socket
Running MPD on an IPC socket instead of the network stack can be advantageous for performance and security if MPD is going to be used locally only.

To do this, set the bind_to_address to either a variable or an absolute path. MPD will fail when using a relative path.

Then export the environment variable

## Autostart with systemd
The  package provides a user service file. The service starts the process as user, there is no need to change permission nor use the  and  variables in the MPD configuration file.

Start/enable the user unit  (i.e. with the  flag).

## Autostart on tty login
To start MPD on login add the following to  or another autostart file:

 # MPD daemon start (if no other user instance exists)
 [ ! -s ~/.config/mpd/pid ] && mpd

## Scripted configuration
The mpd-configure tool creates a MPD configuration optimized for bit perfect audio playback, without any resampling or conversion, using the ALSA interface hardware address (hw:x,y).

## System-wide configuration
The default  keeps the setup in  which is assigned to user as well as primary group MPD.

## Music directory
The music directory is defined by the option  in the configuration file .

MPD needs to have execute permission on all parent directories of the music collection and also read access to all directories containing music files. This may conflict with the default configuration of the user directory, like , where the music is stored.

While there are several solutions to this issue, one of these should be most practical:
* Switch to the #Per-user configuration mode instead
* Add the  user to the user's group and grant group execute permission to the user directory. This way the  user has permission to open the user directory:
 # gpasswd -a mpd user_group_name
 $ chmod 710 /home/user_directory
* Store the music collection in a different path, either:
** by moving it entirely,
** with a bind mount,
** or with Btrfs#Subvolumes (you should make this change persistent with an entry to  ).

The MPD configuration file must define only one music directory. If the music collection is contained under multiple directories, create symbolic links under the main music directory in . Remember to set permissions accordingly on the directories being linked.

To exclude a file - or files - from the update, create a file called  in its parent directory. Each line of that file may contain a list of shell wildcards. Matching files in the current directory and all subdirectories are then excluded from subsequent updates.

## Start with systemd
MPD can be controlled with  using systemd. The first startup can take some time as MPD will scan your music directory.

Test everything by starting a client application ( is a light and easy to use client), and play some music!

## Socket activation
 provides a  unit. If  is enabled (and  is disabled), systemd will not start MPD immediately, it will just listen to the appropriate sockets. Then, whenever an MPD client attempts to connect to one of these sockets, systemd will start  and transparently hand over control of these ports to the MPD process.

If you prefer to listen to different UNIX sockets or network ports (even multiple sockets of each type), or if you prefer not to listen to network ports at all, edit the  unit appropriately and modify  to match the configuration (see  for details).

## User id startup workflow
MPD should never run as root; you may use the  option in the configuration to make MPD change its user id after initialization. Do not use this option if you start MPD as an unprivileged user.
To describe how MPD drops its superuser privileges and switch to those of the user set in the configuration, the steps of a normal MPD startup are listed thereafter:

# Since MPD is started as root by systemd, it first reads the  file.
# MPD reads the  variable in the configuration, and changes from root to this user.
# MPD then reads the rest of the configuration file and configures itself accordingly. Uses of  in the configuration file points to the home user's directory, and not root's directory.

## Multi-MPD setup
## Running an Icecast server
For a second MPD (e.g. with Icecast output to share music over the network) using the same music and playlist as the one above, simply copy the above configuration file and make a new file (e.g., ), and only change the , , , and  parameters (e.g. , , and so on). Using the same directory paths for the music and playlist directories would ensure that this second MPD uses the same music collection as the first one, e.g. creating and editing a playlist under the first daemon would affect the second daemon as well. Users do not have to create the same playlists all over again for the second daemon. Call this second daemon the same way from  above - but be sure to have a different port number, avoiding a conflict with the first MPD daemon.

## Satellite setup
The method described in #Running an Icecast server works, but at least in theory could lead to issues with the database, when both MPD instances try to write to the same database file concurrently. MPD has a satellite mode where one instance can receive the database from an already running MPD instance.

In your  add this, where host and port reflect your primary MPD server:

{{bc|
database {
    plugin "proxy"
    host "localhost"
    port "6600"
}
}}

## Clients
A separate client is needed to control MPD. See a long list of clients at the mpd website. Popular options are:

## Command-line
*

## Console
*
*
*
*
*
*
*
*
*
*
*

## Graphical
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*

## Misc
*
*
*
