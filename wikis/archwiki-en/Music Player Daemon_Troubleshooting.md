# Music Player Daemon/Troubleshooting

## Troubleshooting
## Autodetection failed
During the start of MPD, it tries to auto detect your set-up and configure output and volume control accordingly. Though this mostly goes well, it will fail for some systems. It may help to tell MPD specifically what to use as output and mixer control. If you copied  over from  as mentioned above, you can simply uncomment:

Example for  output type and ALSA mixer:

 audio_output {
 	type			"alsa"
 	name			"My ALSA Device"
 	device			"hw:0,0"	# optional
 	format			"44100:16:2"	# optional
 	mixer_type		"hardware"
 	mixer_device		"default"
 	mixer_control		"PCM"
 }

## MPD hangs on first startup
This is a common error that's caused by corrupt mp3 tags.
Here is an experimental way to solve this issue.
Requirements:
* kid3
* easytag

This method is very tedious, especially with a huge database. Just as a baseline it took 2.5h to fix a 16GB database.

## EasyTAG
The purpose of  here is that easytag detects the error in the tags, but like MPD it hangs and dies. The trick here is that easy tags actually tells you what file is causing the problem on the status bar.
Before starting easytag make sure to have a terminal close to be ready to kill easy tag to avoid a hang. Once you are ready, on the tree view select the directory where all your music is located. By default easytag starts to search all subdirectories for mp3 files. Once you notice that easytag stopped scanning for songs, make note of the culprit and kill easytag.

## Kid3
Here is where  comes in handy. With kid3 go to the offending song and rewrite one of the tags. then save the file. This should force kid3 to rewrite the whole tag again fixing the problem with MPD and easy tag hanging.

Repeat this procedure until your music library is done.

## Cannot connect to mpd: host "localhost" not found: Temporary failure in name resolution
Cannot connect to MPD (with ncmpcpp), if you are disconnected from network. Solution is disable IPv6 or add line to /etc/hosts
 ::1 localhost.localdomain localhost

## Other issues when attempting to connect to mpd with a client
Some have reported being unable to access mpd with various clients, for example seeing errors like these:
 $ ncmpcpp
 Cannot connect to mpd: Connection closed by the server
 $ sonata
 2011-02-13 18:33:05  Connection lost while reading MPD hello
 2011-02-13 18:33:05  Not connected
 2011-02-13 18:33:05  Not connected

Please see posts on ncmpcpp on the Arch Forums HERE and HERE. Also see .

## First fix
Check  for a line like  and remove it. The mpd error file is deprecated and has been removed.

## Second fix
If that does not help, add the following to :

Afterwards, instruct your client to connect via 127.0.0.1. For example, add the following to the ncmpcpp configuration file:

## Binding to IPV6 before IPV4
If on startup, mpd displays the following message:
 listen: bind to '0.0.0.0:6600' failed: Address already in use (continuing anyway, because binding to 'succeeded)
it means mpd binds to the ipv6 interface before binding to ipv4. If you want to use your ipv4 interface, hardcode it in , like:
 bind_to_address "0.0.0.0"
Several binds can also be specified, for example, to have mpd listen both to localhost and to the external IP of your network card:
 bind_to_address "127.0.0.1"
 bind_to_address "192.168.1.13"

## daemon: cannot setgid for user "mpd": Operation not permitted
The error is stating that the user starting the process does not have permissions to become another user (mpd) which the configuration has told the process to run as.

To solve the issue, simply start  as the root user instead of starting a user unit.

## daemon: fatal_error: Failed to set group NN: Operation not permitted
The error is stating that mpd cannot set the group. This is if you have set any other group in  than the default: mpd. This is because of the default  file. It starts mpd as user mpd (and if no group specified with the default group of this user as stated in your ) and therefore mpd does not have any rights to change its group.

## First fix
In  comment out the  part or change it to

## Second fix
Extend the unit  and add your desired group. E.g. run mpd with the group "audio":

## Third fix
Change the default group of the user mpd in your .

## MPD & ALSA
Sometimes, when using other audio outputs, e.g: some web pages containing Flash applets, MPD is rendered unable to play (until it is restarted). The error comes up in mpd's log:

 Error opening alsa device "hw:0,0": Device or resource busy

Reasons for this may be:
* The sound card does not support hardware mixing (uses dmix plugin)
* An application does not work with ALSA's default settings

For a detailed description, it is recommended to take a look at [https://mpd.wikia.com/wiki/Alsa this link.

This problem may be solved by adding the following lines to :
{{hc|mpd.conf|2=
audio_output {
        type                    "alsa"
        name                    "Sound Card"
        options                 "dev=dmixer"
        device                  "plug:dmix"
}
}}

To make the changes have effect, restart .

## High CPU usage with ALSA
When using MPD with ALSA, users may experience MPD taking up lots of CPU (around 20-30%). This is caused by most sound cards supporting 48kHz and most music being 44.1kHz, thus forcing MPD to resample it. This operation takes lots of CPU cycles and results into high usage.

For most users the problem should be solved by telling MPD not to use resampling by adding  into audio_output-part of .

{{hc|mpd.conf|2=
audio_output {
   type			"alsa"
   name			"My ALSA Device"
   auto_resample	"no"
}
}}

Although it may not give as drastic a speedup, enabling mmap may still speed things up:
{{hc|mpd.conf|2=
audio_output {
   type			"alsa"
   name			"My ALSA Device"
   use_mmap		"yes"
}
}}

Some users might also want to tell dmix to use 44kHz as well. More info about tuning performance of your MPD can be found on the MPD wiki

## Playing audio files with different rate (works for EMU 0202/0204/0404)
To play audio files of different rate with automatic card rate change install  and  and keep using ALSA as output:
{{hc|mpd.conf|2=
audio_output {
    type          "alsa"
    name          "Emu 0202 USB"
    device        "hw:2,0"
}
}}

## Changing user
Changing the group that MPD runs as may result in errors like:
 output: Failed to open "My ALSA Device"

 Failed to open ALSA device "default": No such file or directory
or
 player_thread: problems opening audio device while playing "Song Name.mp3"

This is because the MPD users need to be part of the audio group to access sound devices under . To fix it add user make the MPD user part of the audio group:
 # gpasswd -a 'mpd' audio

## MPD includes music from hidden folders in database
MPD includes hidden folders in its database such as repetitive backups of music made by [https://archlinux.org/packages/?name=syncthing syncthing such as . To correct for this, create a  file in the same directory with a list of folders or files to ignore on each line as per the mpd documentation.
