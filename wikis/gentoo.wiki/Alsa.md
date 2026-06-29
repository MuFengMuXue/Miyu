This page contains [[changes](https://wiki.gentoo.org/index.php?title=ALSA&oldid=1430336&diff=1442257)] which are not marked for translation.

[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=ALSA&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

**This article needs to be updated according to the standards found in the [Guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines").**

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/ALSA/de "ALSA/de (46% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/ALSA/hu "ALSA (90% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/ALSA/sv "ALSA/sv (17% translated)")
-   [русский](https://wiki.gentoo.org/wiki/ALSA/ru "ALSA (92% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/ALSA/ta "ALSA/ta (50% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/ALSA/zh-cn "ALSA (45% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/ALSA/ja "ALSA (69% translated)")

**Resources**

[[]][Home](https://www.alsa-project.org/wiki/Main_Page)

[[]][Package information](https://packages.gentoo.org/packages/media-libs/alsa-lib)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture "wikipedia:Advanced Linux Sound Architecture")

\
ALSA, the **A**dvanced **L**inux **S**ound **A**rchitecture, is the Linux kernel\'s API for sound cards, together with an associated software framework. Sound servers such as [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire"), [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"), and [JACK](https://wiki.gentoo.org/wiki/JACK "JACK") all function as a layer on top of ALSA. ALSA can be used directly, without a sound server; however, sound servers provide various additional conveniences and functionality.

As of 2026-01-14, desktop profiles enable the PipeWire sound server. This includes support for packages which make use of the PulseAudio interface (e.g. via the `pulseaudio` USE flag), by using [[[media-sound/libpulse]](https://packages.gentoo.org/packages/media-sound/libpulse)[]] and the [pipewire-pulse.conf] configuration.

Those using PipeWire as a sound server - whether via a profile or otherwise - should typically not need to manually configure ALSA. However, those with more complex hardware and software setups might need to do so.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Hardware detection]](#Hardware_detection)
    -   [[1.2] [Kernel]](#Kernel)
        -   [[1.2.1] [Kernel modules]](#Kernel_modules)
    -   [[1.3] [Software]](#Software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
        -   [[2.1.1] [\~/.asoundrc]](#.7E.2F.asoundrc)
    -   [[2.2] [S/PDIF or HDMI .asoundrc]](#S.2FPDIF_or_HDMI_.asoundrc)
        -   [[2.2.1] [Background]](#Background)
        -   [[2.2.2] [Preference for connections versus media types]](#Preference_for_connections_versus_media_types)
            -   [[2.2.2.1] [Basic analog]](#Basic_analog)
            -   [[2.2.2.2] [S/PDIF]](#S.2FPDIF)
                -   [[2.2.2.2.1] [S/PDIF digital coaxial]](#S.2FPDIF_digital_coaxial)
                -   [[2.2.2.2.2] [S/PDIF optical (TOSLINK)]](#S.2FPDIF_optical_.28TOSLINK.29)
            -   [[2.2.2.3] [HDMI]](#HDMI)
        -   [[2.2.3] [Configuration]](#Configuration_2)
    -   [[2.3] [A/52, AC3, Dolby, DTS]](#A.2F52.2C_AC3.2C_Dolby.2C_DTS)
        -   [[2.3.1] [Decode or playback]](#Decode_or_playback)
        -   [[2.3.2] [Encode to A/52]](#Encode_to_A.2F52)
            -   [[2.3.2.1] [Upmix two channel audio to a A/52 multi-channel audio stream]](#Upmix_two_channel_audio_to_a_A.2F52_multi-channel_audio_stream)
            -   [[2.3.2.2] [Encode PCM 5.1 24-bit audio into a A/52 16-bit audio stream (for streaming via S/PDIF)]](#Encode_PCM_5.1_24-bit_audio_into_a_A.2F52_16-bit_audio_stream_.28for_streaming_via_S.2FPDIF.29)
    -   [[2.4] [Clone audio for 2 or more devices]](#Clone_audio_for_2_or_more_devices)
    -   [[2.5] [JACK Audio Connection Kit]](#JACK_Audio_Connection_Kit)
    -   [[2.6] [Permissions]](#Permissions)
    -   [[2.7] [Service]](#Service)
        -   [[2.7.1] [OpenRC]](#OpenRC)
        -   [[2.7.2] [systemd]](#systemd)
    -   [[2.8] [PulseAudio emulation]](#PulseAudio_emulation)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Test speakers]](#Test_speakers)
    -   [[3.2] [Test microphone]](#Test_microphone)
-   [[4] [Tips]](#Tips)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [No sound]](#No_sound)
    -   [[5.2] [Firefox, Chromium, and YouTube have no audio with custom .asoundrc but other apps do]](#Firefox.2C_Chromium.2C_and_YouTube_have_no_audio_with_custom_.asoundrc_but_other_apps_do)
    -   [[5.3] [Sound card only available for one application]](#Sound_card_only_available_for_one_application)
    -   [[5.4] [Missing dialogue/sound with 4.0 speakers]](#Missing_dialogue.2Fsound_with_4.0_speakers)
    -   [[5.5] [HDMI/SPDIF 5.1 and 7.1 speaker testing]](#HDMI.2FSPDIF_5.1_and_7.1_speaker_testing)
        -   [[5.5.1] [MPlayer]](#MPlayer)
        -   [[5.5.2] [VLC]](#VLC)
    -   [[5.6] [APlay SPDIF/HDMI output has incorrect speaker channels]](#APlay_SPDIF.2FHDMI_output_has_incorrect_speaker_channels)
    -   [[5.7] [Weak center channel on PCM 5.1 live music]](#Weak_center_channel_on_PCM_5.1_live_music)
    -   [[5.8] [More detailed information about an ALSA stream]](#More_detailed_information_about_an_ALSA_stream)
    -   [[5.9] [HTML5 does not play in a browser]](#HTML5_does_not_play_in_a_browser)
        -   [[5.9.1] [HTML5 does not play in the Firefox browser]](#HTML5_does_not_play_in_the_Firefox_browser)
    -   [[5.10] [Laptops with HDMI audio output]](#Laptops_with_HDMI_audio_output)
    -   [[5.11] [Headset jack not working]](#Headset_jack_not_working)
    -   [[5.12] [udev/alsactl errors on boot]](#udev.2Falsactl_errors_on_boot)
    -   [[5.13] [No sound after rebooting following a system update]](#No_sound_after_rebooting_following_a_system_update)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installation]

### [Hardware detection]

** Important**\
It is often found during an ALSA installation, that the kernel driver modules for soundcards have not been properly installed on the system. To check if one\'s system has working soundcard driver modules, run [lsmod]. If there are no modules with the prefix of `snd_`, consider properly installing the kernel driver module for the system\'s specific soundcard. A more detailed guide can be found in the [Kernel Modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules") page.

To choose the right driver, first detect the used audio controller. Use [[lspci](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection")] for this task:

`user `[`$`]`lspci | grep -i audio`

With the controller name determined, the needed driver can be found in the [ALSA sound card matrix](https://www.alsa-project.org/wiki/SoundCard-Matrix).

### [Kernel]

Activate the following kernel options:

[KERNEL]

    Device Drivers --->
        <*> Sound card support
            <*> Advanced Linux Sound Architecture --->
                [*] PCI sound devices  --->
                    <Select the audio controller driver for your audio controller...>
                HD-Audio  --->
                   <Select a codec or enable all and let the generic parse choose the right one...>
                   [*] ...
                [*] USB sound devices  --->
                    Must have as some cards are presented as USB devices.
                    [*] USB Audio/MIDI driver
    General setup --->
        [*] System V IPC

If the system has more than eight sound outputs (note that each HDMI output on a GPU counts as an output), the maximum number of sound cards will need to be increased:

[KERNEL]

    Device Drivers --->
        <*> Sound card support
            <*> Advanced Linux Sound Architecture --->
                [*] Dynamic device file minor numbers
                (32) Max number of sound cards

#### [Kernel modules]

For advanced configurations (e.g. involving multiple sound cards), it can be better to select all the ALSA-related kernel options as modules. Then, their use can be configured via two files:

-   [/etc/modules-load.d/alsa.conf] - one line per module, normally only needed for virtual sound cards.
-   [/etc/modprobe.d/alsa.conf] - for the modules\' options.

For example, assume a laptop with two hda-intel sound cards and an external USB card. If the aloop and VirMIDI virtual sound cards are also required, together with a card order that persists across reboots:

1.  the aloop virtual card
2.  the hda-intel PCM device
3.  the hda-intel HDMI device
4.  the VirMIDI virtual device
5.  the USB card

then the relevant modules should be loaded in that order:

[FILE] **`/etc/modprobe.d/alsa.conf`**

    options snd slots=snd-aloop,snd-hda-intel,snd-hda-intel,snd-virmidi,snd-usb-audio
    options snd-hda-intel index=1,2 model=1002:1637,1022:15e3

Card indexes start from 0.

To get the model strings, use [[[lspci(1)]](https://man.archlinux.org/man/lspci.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] (or [[[lsusb(1)]](https://man.archlinux.org/man/lsusb.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for USB cards):

`root `[`#`]`lspci -nn`

    04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller [1002:1637]
    04:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller [1022:15e3]

Instruct the kernel to load the virtual sound cards:

[FILE] **`/etc/modules-load.d/alsa.conf`**

    snd-aloop
    snd-virmidi

### [Software]

Portage knows the global USE flag `alsa` for enabling support for ALSA in other packages. Enabling this USE flag will pull in [[[media-libs/alsa-lib]](https://packages.gentoo.org/packages/media-libs/alsa-lib)[]] automatically (default in **[x86]** and **[amd64]** desktop profiles):

`root `[`#`]`euse -E alsa`

The [euse] command is part of [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]].

After setting this be sure to update the system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

The [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]] package provides some tools for troubleshooting and testing the sound system. It is a good idea to merge the package if it is not already installed:

`root `[`#`]`emerge --ask media-sound/alsa-utils`

## [Configuration]

### [Files]

-   [/etc/asound.conf] - Global (system wide) configuration file.
-   [\~/.asoundrc] - Local (per user) configuration file.

#### [][\~/.asoundrc]

This file can be optionally used so that on a per-user basis, ALSA defaults can be overridden. If the system has special hardware it is likely the card 0 and device 0 (the defaults) are not going to work.

One of the simplest changes is card and device. This is the case for me with an HDMI coming from an Nvidia card connected to an onboard Realtek ALC88\* audio device.

[FILE] **`~/.asoundrc`**

    defaults.pcm.!card 1
    defaults.pcm.!device 7

If you can\'t seem to find the card number assigned to the device that is the sound card you intend to use, don\'t panic --- the card number is internally a name, which you can use. If your card is listed like this\...

`user `[`$`]`aplay -L`

    front:CARD=Generic,DEV=0
    HD-Audio Generic, ALC282 Analog
    Front speakers

\... then it means the [\~/.asoundrc] file should be like this:

[FILE] **`~/.asoundrc`**

    defaults.pcm.!card Generic
    defaults.pcm.!device 0
    defaults.ctl.!card Generic

** Warning**\
These settings disable all software mixing. To output everything at 96kHz, add `defaults.pcm.dmix.rate 96000` to the [\~/.asoundrc] file.

When multiple sound cards are in use, the device numbers could be reordered across boots, such that using a name is advantageous.

If the correct name is unclear, a list of valid names can be easily obtained with:

`user `[`$`]`cat /sys/class/sound/card*/id`

Here is output from a developer\'s system that has multiple sound cards:

`user `[`$`]`cat /sys/class/sound/card*/id`

    Q1U
    HDMI
    PCH
    C930e

Here we have the Q1U microphone as Q1U, the builtin HDMI as HDMI, the analog audio jacks as PCH and a webcam\'s builtin microphone as C930e. Any of these are valid names for the card.

** Warning**\
Specifying numbers instead of names when multiple sound cards are used can result in device reordering across boots, which will prevent sound from working properly until the configuration file is edited to use the new number.

### [][S/PDIF or HDMI .asoundrc]

#### [Background]

Most sound cards allow passing through audio to an external consumer receiver or DAC using S/PDIF digital coaxial or optical cables. Doing so, preserves sound quality and compressed Dolby/DTS encoded material. Uncompressed Dolby/DTS or Bluray material require a HDMI connection. The more common mono or analog stereo cables cannot carry Dolby/DTS signals.

With a default installed ALSA installation, it is possible for a S/PDIF or HDMI connection to work out of the box (no [.asoundrc] file alterations). While only some applications, such as the web browser\'s Adobe Flash plugin will fail playing sound. As such, the below [.asoundrc] is usually required for most S/PDIF and HDMI connections. Also, any media applications open will need to be restarted for the [.asoundrc] files to take affect (i.e. web browsers using the Adobe Flash plugin).

#### [Preference for connections versus media types]

##### [Basic analog]

Basic analog (i.e. RCA) connections - Basic user. Quality depends on sound card DAC. Look for a sound card with a high SNR db level.

##### [][S/PDIF]

S/PDIF provides good quality audio for music, videos, and DVD quality movies containing Dobly/DTS compressed signals. Most sound cards and motherboards, these days, provide some sort of S/PDIF port. Nowadays, it is more common to see S/PDIF Toslink ports on motherboards. Many computer games provide compressed Dolby/DTS signals.

###### [][S/PDIF digital coaxial]

S/PDIF digital coaxial may have problems with voltage cross talk, but is more common as it only requires a simple mini jack or RCA coaxial cable.

###### [][S/PDIF optical (TOSLINK)]

[S/PDIF](https://en.wikipedia.org/wiki/S/PDIF "wikipedia:S/PDIF") ([TOSLINK](https://en.wikipedia.org/wiki/TOSLINK "wikipedia:TOSLINK")) optical cable completely avoids possible electrical cross talk or interference among cables since it is fiber optic, however it is susceptible to signal degradation if the cable is bent too much. Audiophiles tend to favor this type of cable.

##### [HDMI]

[HDMI](https://en.wikipedia.org/wiki/HDMI "wikipedia:HDMI") (High-Definition Multimedia Interface) cable can carry compressed Dolby/DTS and uncompressed (i.e. [Blu-ray](https://wiki.gentoo.org/wiki/Blu-ray "Blu-ray")) Dolby/DTS signals. The audio market has favored this connection, but still preserves S/PDIF connections. One concern being, HDMI cables are copper wire, still susceptible to electrical cross talk or interference, similar to S/PDIF Digital Coaxial connections.

HDMI optical cables are produced, but they are generally too expensive for the consumer market. If audiophiles have S/PDIF Optical ports, they will use the S/PDIF connections for other media such as music and DVD movies, while only using HDMI when needed for processing uncompressed Dolby/DTS encoded material such as Blu-ray media. Again, the basic user will likely just use HDMI, avoiding the fuss of changing configuration files.

#### [Configuration]

Find the digital output device:

`user `[`$`]`aplay --list-devices`

Adjust the below file to use the card/device number.

[FILE] **`~/.asoundrc`**

    pcm.!spdif

    pcm.!default
    }

    # Share a single card with multiple applications
    #pcm.!default

** Note**\
The above will not allow sound to be played from more than one sound application, or more than two sounds played at once through one sound card. In order to perform this task, the sounds are remixed with a slight degradation with sound quality. Most people listening to music, prefer not to allow this due to interruptions and decreased sound quality. However, for those that desire this, the above commented section of code will achieve this.

** Note**\
When playing sound files using [aplay], the beginning of the playback will be clipped because the digital S/PDIF or HDMI connection is not held open and needs to be started each time a sound file is played. Notice Microsoft Windows both, holds open the receiver or DAC and remixes media on playback.

### [][A/52, AC3, Dolby, DTS]

Sound cards providing S/PDIF output can pass through lossy compressed multichannel audio. To my ears, the high bit rate compressed media has little loss in comparison to two channel CD or DVD audio. I surmise this is because we now have multichannels feeding multiple speakers. Hence, the more hardware, the equivelant or better sounding?

If a sound card states it has S/PDIF, it will likely pass through Dolby or DTS even though it does not specifically show a Dolby or DTS icon or listed within its features. This is because, when they do list Dolby or DTS, it is because they\'re providing software for upmixing, or providing the decoded signal through analog output.

HDMI will pass through uncompressed multichannel audio, but a video feed is interleaved as required by the HDMI specification. In comparison to DVD video and audio, I see and hear very little quality difference, if any! About the only thing I noticed between S/PDIF Toslink and HDMI, HDMI seems to amplify the signal by a few watts or 5db. (I conclude this is because of the higher bit rate?)

As such, S/PDIF is still quite popular, even today.

** Note**\
A S/PDIF or HDMI connection is required for passing through advanced encodings. Analog connections (RCA and minijacks) do not support any advanced encoding.

Decoding or encoding to Dolby or DTS requires a license. If you have already purchased a sound card with this multichannel support, then you likely already have a license. See [this article](https://www.alsa-project.org/main/index.php/A52_plugin) for more information.

ALSA [[[media-plugins/alsa-plugins]](https://packages.gentoo.org/packages/media-plugins/alsa-plugins)[]] package requires recompilation to include the ffmpeg USE Flag with the A/52 (pcm.a52encode) plugin.

`root `[`#`]`USE="ffmpeg" emerge -q media-plugins/alsa-plugins`

#### [Decode or playback]

Recompile [mplayer] or another other favorite software player to include the ALSA libraries.

`root `[`#`]`USE="a52 dts" emerge -q media-video/mplayer`

Add the multichannel codecs to [mplayer.conf], so media attempting to be played has first been provided the option of hardware passthrough rather then down mixing.

[FILE] **`/etc/mplayer/mplayer.conf`**

    ac=hwac3,hwdts,hwmpa,spdifac3,spdifeac3,spdifaac,spdifdts,spdifmpa,spdifthd,dts,ffaac,

You should now be able to pass through (and enjoy) almost any Dolby or DTS signal through S/PDIF to the receiver.

#### [][Encode to A/52]

##### [][Upmix two channel audio to a A/52 multi-channel audio stream]

To simulate A/52 encoded audio from normal one or two channel audio streams or files, ALSA can upmix using its A/52 plugin. (A/52 is also known as AC-3 or Dolby Digital encoding.)

A/52 upmixing preferred when playing computer games or watching video without Dolby/DTS encoded material, such as older Movies. Many sound card manufacturers provide their applications with a feature for software upmixing to Dolby Digital, and recommend enabling this upmixing when listening to such media, except for Music.

Upmixing to A/52 is frowned upon by audiophiles. As such, it is a user\'s preference to upmix all the sounds to A/52 before sending the stream to the consumer stereo receiver or DAC. Matter of fact, audiophiles prefer simple stereo, and further state stereo is still better quality than Dolby/DTS material or other audio encoded with gimmicks. Also, the consumer stereo or DAC likely possibly includes a feature for upmixing audio into five channel audio.

[FILE] **`~/.asoundrc`**

    pcm.!default

    ctl.!default

    pcm.a52encode

    pcm.surroundaudio a52encode

    ctl.surroundaudio

`user `[`$`]`speaker-test -Dsurroundaudio -c 6`

##### [][Encode PCM 5.1 24-bit audio into a A/52 16-bit audio stream (for streaming via S/PDIF)]

Also known as, encoding PCM 5.1 audio stream into a compressed Dolby Digital stream for playing over S/PDIF. No real need to use this if you\'re using HDMI, as HDMI can handle the bandwidth of a PCM 5.1 audio stream. S/PDIF Toslink has also supposedly been upgrade to do so also, but most hardware has yet to be upgraded to the new specifications, and some doubt it will ever happen.

For some reason, the previous [.asoundrc] section previously mentioned doesn\'t work with PCM 5.1 streams. Another issue I run into with 24 bit PCM 5.1 audio streams, they require downmixing from S24_LE to S16_LE bit format. Reason being, 24 bit is a common format for most media, however receivers can sometimes only decode 16 or 32 bit audio. Also, the S/PDIF can only handle 16 bit audio when encoding to multi-channel formats such as A/52, for the time being until S/PDIF TosLink hardware specifications are upgraded.

The following [.asoundrc] excerpt will encode a PCM 5.1 24 bit stream into a 16 bit A/52 stream, for streaming over S/PDIF.

[FILE] **`~/.asoundrc`**

    #####
    # Description: This will make it possible to use a52 with PulseAudio out of
    #         the box. It may be useful for other use cases. Just include
    #         this in the ~/.asoundrc file.

    pcm.a52
        type plug
        slave
            # Convert to S16 bit format, per SPDIF spec
            format S16_LE # Required for current S/PDIF spec
        }
    }

`user `[`$`]`aplay -D pcm.a52 /home/me/Music/Led_Zeppelin/Celegration_Day/PCM51-24bit/*.wav`

### [Clone audio for 2 or more devices]

Sometimes you need to clone audio (example using 2 cloned screens with different inputs (first screen HDMI and second screen DVI + Analog audio)). This is a simple script that you can use as global or local configuration for clone 2 (or more) channels. You must adjust to your system the lines below commented lines. More information of the author of the script and forum discussion [here.](https://forums.gentoo.org/viewtopic-t-902670-start-0.html)

[FILE] **`/etc/asound.conf`**

    ctl.!default

    pcm.!default both

    pcm.both
                                    buffer_size 4096
                                    channels 2
                                }
                            }
                            slaves.b.pcm
                                    buffer_size 4096
                                    channels 2
                                }
                            }
                            slaves.a.channels 2
                            slaves.b.channels 2
                            bindings.0.slave a
                            bindings.0.channel 0
                            bindings.1.slave a
                            bindings.1.channel 1
                            bindings.2.slave b
                            bindings.2.channel 0
                            bindings.3.slave b
                            bindings.3.channel 1
                        }
                    }
                    ttable.0.0 1
                    ttable.1.1 1
                    ttable.0.2 1
                    ttable.1.3 1
                }
            }
        }
    }
    control

### [JACK Audio Connection Kit]

It is possible to interconnect JACK and ALSA. For more information, refer to [this section of the \"JACK\" page](https://wiki.gentoo.org/wiki/JACK#ALSA "JACK").

### [Permissions]

If the `acl` USE flag enabled globally and a login daemon (e.g. systemd-logind or elogind) is being used (i.e the system is using a *desktop* [profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")) permissions to sound cards will be handled automatically. Permissions can be checked using [getfacl]:

`user `[`$`]`getfacl /dev/snd/controlC0 | grep larry`

`user:`**`larry`**`:rw-`

A broader solution is to add the user you want to be able to access the sound card to the *audio* group:

`root `[`#`]`gpasswd -a larry audio`

`user `[`$`]`grep audio /etc/group`

**`audio`**`::18:larry`

** Warning**\
You should logout and login again to make [alsamixer] work, otherwise running the [alsamixer] command will give you the error \"cannot open mixer: No such file or directory\"

### [Service]

#### [OpenRC]

If using OpenRC start ALSA now using the [service] command:

`root `[`#`]`rc-service alsasound start`

To have start ALSA at boot time, add it the boot runlevel using [rc-update]:

`root `[`#`]`rc-update add alsasound boot`

#### [systemd]

If using systemd, ALSA state will be preserved and restored automatically across system restarts.

The status of ALSA can be checked using the [systemctl] command:

`root `[`#`]`systemctl status alsa-restore`

### [PulseAudio emulation]

Some software (e.g. [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox")) makes use of the Pulse API. For [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") support on a pure-ALSA system (i.e. one not using a sound server such as PipeWire or Pulse), install [apulse](https://wiki.gentoo.org/wiki/Apulse "Apulse").

## [Usage]

### [Test speakers]

If everything above is perfect, it should now be able to test the sound card and the speakers. The [speaker-test] command-line tool from package [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]] (this should already be installed as per the previous recommendation).

`user `[`$`]`speaker-test -t wav -c 2`

For configurations using a 5.1 surround sound system:

`user `[`$`]`speaker-test -t wav -c 6 -D surround51`

Press [Ctrl]+[C] to interrupt the test.

If [speaker-test] returns an error about [IPC](https://en.wikipedia.org/wiki/Inter-process_communication "wikipedia:Inter-process communication") semaphore not being implemented, ensure the kernel\'s \"System V IPC\" option is enabled:

[KERNEL]

    General setup --->
        [*] System V IPC

### [Test microphone]

If needed, select the audio device if no default one is provided and add the `--device=hw:0,0` to the incantation of [arecord], substituting the CardNumber,DeviceNumber in the integer fields.

The following will list possible devices.

`user `[`$`]`arecord --list-devices`

** Note**\
You may also need to unmute the line or microphone channel. Open [alsamixer] and first select the sound card (i.e. [F6]), then press [F4] to show the Capture Channels, \"left/right cursor keys\" to select the \"Mic\" channel and press [Space] to toggle CAPTURE the channel.

The following will record indefinitely until [CTRL]+[C] is depressed and provide a default 8000 Hz mono quality recording:

`user `[`$`]`arecord /tmp/test.wav`

The following will provide will record for two seconds (\--duration=2) using DAT 48000 Hz quality (`--format=dat`) and display the curses vumeter in stereo (`--vumeter=stereo`) and save to [/tmp/test.wav].

`user `[`$`]`arecord --channels=1 --duration=2 --format=dat --vumeter=stereo /tmp/test.wav`

Or optionally:

[FILE] **`~/.bashrc`**

    # Simple convenience wrapper to record then play back a temporary sound file.
    # Usage: arecord-mic duration
    function arecord-mic " -- "$tmpFile" && aplay -- "$tmpFile"
        rm -f -- "$tmpFile"
    }

Notice, [arecord] cannot record in S24_LE, and is only capable of recording using S16_LE or S32_LE formats. For the human ear, any audio resolutions greater than 24 bit (S24_LE) or 48000Hz are said to be indistinguishable to differentiate using the human ear. Reference Sampling (signal processing) Wikipedia, Audio sampling. Users should also specify channels=1, as all recordings are performed in mono/monaural when typically using the Microphone Input unless recordings are using the stereo Line Input. In order to further encourage [arecord] to record monaural or only one channel, using the device=plughw:0,0 is further specified. (Alleviates a common problem, microphone/mic playback only occurs on the right or left channels.)

Use [mplayer] or [aplay] to playback the saved file. I usually record in \"dat\" or atleast \"cd\" quality formats. DAT is best when benchmarking.

## [Tips]

Try one of the many configuration options in [PaulBredbury\'s asoundrc file](https://gist.github.com/thanley11/100754cc911442901867).

## [Troubleshooting]

### [No sound]

If there\'s no sound, output channels may be muted. Unmute the channels, either by using the GUI environment\'s mixer, or by using [alsamixer] (from the [[[media-audio/alsa-utils]](https://packages.gentoo.org/packages/media-audio/alsa-utils)[]] package), selecting the appropriate channels and pressing the [M] key to mute or unmute:

`user `[`$`]`alsamixer`

### [][Firefox, Chromium, and YouTube have no audio with custom .asoundrc but other apps do]

Browsers are sometimes picky about [\~/.asoundrc] settings. If you\'re specifying the default audio device (likely given that most computers nowadays have an HDMI A/V output and the analog and HDMI audio outputs are viewed as two separate sound cards), try doing this specifically as follows:

[FILE] **`~/.asoundrc`**

    defaults.pcm.card <number of your default sound card>
    defaults.ctl.card <default sound card>

** Note**\
Since version 52, Firefox has made PulseAudio a hard requirement and dropped support for direct output to ALSA. To enable sound in these versions of Firefox enable the `pulseaudio` USE flag. See [PulseAudio requirement breaks Firefox on ALSA-only systems](https://bugzilla.mozilla.org/show_bug.cgi?id=1345661). This limitation does not affect Firefox (version 52 only) built from sources ([[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]]). Chromium is also not immune to problem. Both browsers either depend on pulseaudio to set up correct sample rate or in absence of pulseaudio set sample rate to 48000 as defacto standard in sound card world. So if you have 96000 hz sample rate, downgrade it to 48000 and sound will work once again.

### [Sound card only available for one application]

Sometimes one app essentially takes over all sound devices, e.g. for performance reasons.

To force the use of dmix instead of direct audio output (which is what most things, such as [Wine](https://wiki.gentoo.org/wiki/Wine "Wine"), use by default), when the device is card 1 device 7:

[FILE] **`~/.asoundrc`**

    pcm.dmixed

                period_size 1024
                buffer_size 8192
            }

            bindings
        }
        capture.pcm "hw:0"
    }

    pcm.!default

Use of [\~/.asoundrc] is immediate: as long as use of a specific device is not being forced by any applications, applications will either begin to produce audio output immediately, or will require a restart. One of the best tests is to open a browser, go to YouTube, open a terminal, and use an audio or video player to try to play an audio or video file: success is indicated by an absence of errors (e.g. \"Device or resource busy\").

### [][Missing dialogue/sound with 4.0 speakers]

If using a 4.0 sound card (like an old SB Live), or 4.0 speakers in general, the dialogue in some games or movies might be very quiet or even missing. This is because most applications and movies support only either 2.0 (stereo) or 5.1 output. In order to achieve surround sound, the 5.1 audio track is used, but two channels are discarded: the center channel (which usually carries dialogue), and the subwoofer channel.

This issue can be circumvented by creating a virtual device which downmixes 5.1 to 4.0, mixing the center and subwoofer channels with other audio channels.

[FILE] **`~/.asoundrc`**

    pcm.downmix

    # ttable.A.B G
    # where A - input channel
    #       B - output channel
    #       G - volume gain (1.0 = original)

    # Copy channels 0-3
        ttable.0.0 1
        ttable.1.1 1
        ttable.2.2 1
        ttable.3.3 1

    # Mix channel 4 (center) into front speakers, and a bit (0.3) into rear ones
        ttable.4.0 1.0
        ttable.4.1 1.0
        ttable.4.2 0.3
        ttable.4.3 0.3

    # Mix channel 5 (subwoofer) mostly (0.6) into rear speakers, and a bit (0.3) into front ones
        ttable.5.0 0.3
        ttable.5.1 0.3
        ttable.5.2 0.6
        ttable.5.3 0.6
    }

    ctl.downmix

### [][HDMI/SPDIF 5.1 and 7.1 speaker testing]

The [[[speaker-test(1)]](https://man.archlinux.org/man/speaker-test.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] utility doesn\'t test audio with more than two channels over HDMI or SPDIF, but [MPlayer](https://wiki.gentoo.org/wiki/MPlayer "MPlayer") and [VLC](https://wiki.gentoo.org/wiki/VLC "VLC") can be used instead.

To do so, download a [5.1 channel (FLAC)](https://github.com/sfiera/flac-test-files/raw/master/surround51.flac) or [7.1 channel (FLAC)](https://github.com/sfiera/flac-test-files/raw/master/surround71.flac) speaker test file.

Then, play the provided sound file, specifying the HDMI or SPDIF device, the PCM file, and the number of channels (which will likely be either 6, for 5.1 surround, or 8, for 7.1 channel surround).

#### [MPlayer]

Test a 5.1 channel file:

`user `[`$`]`mplayer -channels 6 "/path/to/downloaded/flac_file.flac" -channels 6`

Test a 7.1 channel file:

`user `[`$`]`mplayer -channels 8 "/path/to/downloaded/flac_file.flac" -channels 8`

** Note**\
When testing in the absence of a default device, pass the additional option `-ao alsa:device=hw=<value>` where `<value>` is the value of the appropriate device.

Refer to the [[[mplayer(1)]](https://man.archlinux.org/man/mplayer.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for more information.

#### [VLC]

`user `[`$`]`cvlc /path/to/downloaded/flac_file.flac`

Refer to the [[[cvlc(1)]](https://man.archlinux.org/man/cvlc.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for more information.

### [][APlay SPDIF/HDMI output has incorrect speaker channels]

Now that you know how to use MPlayer to play a speaker test PCM WAV file per \"HDMI/SPDIF 5.1 and 7.1 Speaker Testing\" above, you now find APlay doesn\'t output to the speaker channels properly when using SPDIF/HDMI. With HDMI, this is likely caused by the snd_hda_intel HDMI audio module/driver which is used by other manufacturers such as NVidia HDMI aside from just Intel\'s HDMI hardware. As to why MPlayer does use the correct channels, MPlayer is usually under constant development and manually corrects this issue?

Another problem this solution pertains to, trying to play a 24-bit PCM 2.0 or PCM5.1 WAV files and finding APlay constantly refuses to play the stream, due to incorrect bit rate, etc.

To correct this for ALSA (APlay) with minimal alterations to the PCM streams, we\'ll need to remap the speaker channels within a [\$/.asoundrc] file. Add the following to the bottom of your [\$/.asoundrc] file. Also note, the below configuration is for both 5.1 and 7.1 audio, or you could further map/copy the two extra channels to your 5.1 channels incase you do not want to omit the audio from a 7.1 stream.

[FILE] **`.asoundrc`**

    pcm.myHDMI
        ttable
    }

It seems that most HDMI to Stereo Receiver connections only stream 16 and 32 bit formats, skipping 24 bit. The above configuration up-mixes any PCM stream to 32 bit when using the pcm.myHDMI profile, as it is quite common to see PCM 2.0 and 5.1 24 bit audio files. It just doesn\'t seem right to down-mix everything to 16 bit, or use Float as the latter uses more processing power. (Users can also set an alias within their bashrc file for 16 bit or 24 bit incantations as well.)

Test the speaker routing using a surround test PCM file. (See the above previously mentioned \"8 Channel Speaker Test\".)

`user `[`$`]`aplay -D my.HDMI 8Channel.wav`

### [Weak center channel on PCM 5.1 live music]

If a multi-channel soundtrack or piece of music has an apparently weak center channel, and the sound track is a live recording, it might be possible to map the center channel to the rear channels, e.g. when using [mplayer](https://wiki.gentoo.org/wiki/Mplayer "Mplayer"):

`user `[`$`]`mplayer -ao alsa:device=hw=1.7 Music/MyAlbum/PCM51-24bit/01.MyMusic.wav -channels 6 -format s32le -af channels=6:6:0:0:1:1:4:2:4:3:4:4:5:5`

The above incantation of [mplayer](https://wiki.gentoo.org/wiki/Mplayer "Mplayer") specifies:

-   an HDMI device of `hw:1.7`;
-   the PCM 5.1 audio file;
-   the number of channels;
-   the format (not needed if the receiver can natively handle 24 bit; receivers that can only natively handle 16- or 32-bit audio need to be upmixed); and
-   the mapping.

The mapping specifies:

-   a 6 channel audio stream, with 6 mappings immediately following, then to copy:
-   the left front channel to left speaker;
-   the right channel to right speaker;
-   the center channel to left rear speaker;
-   the center channel to right rear speaker;
-   the center channel to center speaker; and
-   the subwoofer channel to the subwoofer speaker.

Note that the rear channels on live recordings usually contain only the audience screaming, with very little music.

For further details, refer to the [[[mplayer(1)]](https://man.archlinux.org/man/mplayer.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.

### [More detailed information about an ALSA stream]

For in-depth information about a program\'s usage of ALSA, such as its PID (`owner_pid`) and sample rate (`rate`), use the [/proc] interface. This can be done by substituting the relevant card/device details into the command below.

`user `[`$`]`cat /proc/asound/card2/pcm0p/sub0/*`

    access: RW_INTERLEAVED
    format: S16_LE
    subformat: STD
    channels: 2
    rate: 44100 (44100/1)
    period_size: 5513
    buffer_size: 22050
    card: 2
    device: 0
    subdevice: 0
    stream: PLAYBACK
    id: USB Audio
    name: USB Audio
    subname: subdevice #0
    class: 0
    subclass: 0
    subdevices_count: 1
    subdevices_avail: 0
    state: RUNNING
    owner_pid   : 934
    trigger_time: 86393.193574796
    tstamp      : 86540.250594985
    delay       : 17714
    avail       : 4602
    avail_max   : 7379
    -----
    hw_ptr      : 6485052
    appl_ptr    : 6502500
    tstamp_mode: NONE
    period_step: 1
    avail_min: 5513
    start_threshold: 2147483647
    stop_threshold: 22050
    silence_threshold: 0
    silence_size: 0
    boundary: 6206523236469964800

### [HTML5 does not play in a browser]

If there is no sound in any browser used (Firefox, SeaMonkey, Otter Browser, etc.) and ALSA generally works, there is a workaround that might solve this particular issue: try removing the [/etc/asound.conf] file.

`root `[`#`]`mv /etc/asound.conf /etc/asound.conf.old`

Restart the browser and test the sound output for HTML5. It might just work now after applying this workaround.

#### [HTML5 does not play in the Firefox browser]

Some system motherboards (i.e. Asus Z87-EXPERT) cause Card 0 to be a MID device instead of a PCM device. The same driver module snd_hda_intel is used for both the MID and PCM cards on this motherboard. For some reason Firefox HTML 5 requires Card 0 of the snd_hda_intel no matter how you change it with asoundrc. You can make flash work using the asoundrc file, but HTML 5 audio is silent.

You must remap the PCM device in Linux as card 0 and remove the changes to asoundrc that were added to make Flash work. This wiki page indicates that you should compile the snd_hda_intel driver into the kernel. Using this configuration you must remap the card 0 and card 1 devices using boot parameters instead of a [/etc/modprobe.d/alsa.conf] file. For example the following kernel command line option will swap the MID and PCM card indicies so that the default card 0 is the PCM card:

`snd-hda-intel.index=1,0`

** Note**\
The module is named snd_hda_intel, but the boot parameter name is snd-hda-intel.

### [Laptops with HDMI audio output]

Some laptops with an HDMI audio output will map /proc/asound/card0 as HDMI and therefore makes it default output device for applications as stated above in the Firefox section. Another way to remap is to add these two lines to [/etc/modprobe.d/alsa.conf]

[FILE] **`/etc/modprobe.d/alsa.conf`**

    # Set this to the correct number of cards.
    options snd cards_limit=2
    options snd-hda-intel index=1,0

Verify the order change by checking this command

`user `[`$`]`cat /proc/asound/cards`

     0 [PCH            ]: HDA-Intel - HDA Intel PCH
                          HDA Intel PCH at 0xf2534000 irq 45
     1 [HDMI           ]: HDA-Intel - HDA Intel HDMI
                          HDA Intel HDMI at 0xf2530000 irq 46

This method only works if snd-hda-intel is compiled as a module not built-in

### [Headset jack not working]

Sometimes, to get a headset jack working, additional model information needs to be passed to the audio driver. For example, in case of a Dell Latitude E7470 laptop with snd-hda-intel driver, the following needs to be added to [/etc/modprobe.d/alsa.conf]:

[FILE] **`/etc/modprobe.d/alsa.conf`**

    options snd-hda-intel model=headset-mic

More information can be found in [this section of the Linux kernel documentation](https://www.kernel.org/doc/html/latest/sound/hd-audio/models.html).

### [][udev/alsactl errors on boot]

Due to partitioning, encryption, or having a [split /usr](https://wiki.gentoo.org/wiki/Split_/usr "Split /usr") system, these errors may appear on boot:

`root `[`#`]`journalctl -b | grep alsa`

    (udev-worker)[2594]: controlC2: Process '/usr/sbin/alsactl restore 2' failed with exit code 2.

    (udev-worker)[2611]: controlC0: Process '/usr/sbin/alsactl restore 0' failed with exit code 2.

    (udev-worker)[2579]: controlC1: Process '/usr/sbin/alsactl restore 1' failed with exit code 2.

To fix the issue, add `TEST=="@sbindir@/alsactl"` to [/lib/udev/rules.d/90-alsa-restore.rules]:

[FILE] **`/lib/udev/rules.d/90-alsa-restore.rules`**

    TEST!="/etc/alsa/state-daemon.conf", TEST=="@sbindir@/alsactl", RUN+="/usr/sbin/alsactl restore $attr"
    TEST=="/etc/alsa/state-daemon.conf", TEST=="@sbindir@/alsactl", RUN+="/usr/sbin/alsactl nrestore $attr"

For further details and discussion, refer to [this discussion on alsa-devel](https://patchwork.kernel.org/project/alsa-devel/patch/1482964275.11185.34.camel@users.sourceforge.net/) and [this discussion on bugs.debian.org](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=636437).

### [No sound after rebooting following a system update]

If, after a system update followed by a reboot, sound is not working, resulting in e.g. [[[speaker-test(1)]](https://man.archlinux.org/man/speaker-test.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] producing an error like:

     ALSA lib /var/tmp/portage/media-libs/alsa-lib-1.2.14/work/alsa-lib-1.2.14/src/pcm/pcm_dmix.c:1000:(snd_pcm_dmix_open) unable to open slave
     Playback open error: -2,No such file or directory

and [[[alsaplayer(1)]](https://man.archlinux.org/man/alsaplayer.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] producing an error like:

     /usr/lib64/alsaplayer/output/libalsa_out.so failed to load
     NOTE: THIS IS THE NULL PLUGIN.      YOU WILL NOT HEAR SOUND!!

It might be that a stale [/var/lib/alsa/asound.state] file is present (e.g. due to the format of that file changing between kernel versions). Remove that file and reboot.

## [See also]

-   [Power management/Soundcard](https://wiki.gentoo.org/wiki/Power_management/Soundcard "Power management/Soundcard") --- describes the setup of [power management](https://wiki.gentoo.org/wiki/Power_management "Power management") of [sound devices](https://wiki.gentoo.org/wiki/Category:Sound_devices "Category:Sound devices").
-   [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") --- low-latency, graph-based, processing engine and server, for interfacing with audio and video devices.
-   [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") --- a multi-platform, open source, *sound server* that provides a number of features on top of the low-level audio interface [ALSA]
-   [JACK](https://wiki.gentoo.org/wiki/JACK "JACK") --- describes the setup of a playing sound with **JACK** (**J**ACK **A**udio **C**onnection **K**it).

## [External resources]

-   [ALSA project - the C library reference](https://www.alsa-project.org/alsa-doc/alsa-lib/) - home page with links to official information about ALSA configuration and the ALSA API.
-   ALSA Project - the C library reference, [PCM (digital audio) plugins](https://www.alsa-project.org/alsa-doc/alsa-lib/pcm_plugins.html) - ALSA PCM (digital audio) plugin descriptions and configuration file examples.
-   [A close look at ALSA](https://www.volkerschatz.com/noise/alsa.html) - introductory tutorial.

## [References]