[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-ALSA&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=ALSA "ALSA (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=ALSA/tr "ALSA (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=ALSA/ru "ALSA (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=ALSA/fa "معمار صوتی پیشرفته لینوکس (ALSA) (8% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Use ALSA on with Applications requiring PulseAudio]](#Use_ALSA_on_with_Applications_requiring_PulseAudio)
    -   [[2.1] [Install apulse]](#Install_apulse)
    -   [[2.2] [Using apulse]](#Using_apulse)
-   [[3] [Selecting the Primary Audio Device]](#Selecting_the_Primary_Audio_Device)
-   [[4] [See also]](#See_also)

## [Overview]

The [Advanced Linux Sound Architecture (ALSA)](https://www.alsa-project.org/wiki/Main_Page) provides audio and MIDI functionality to the Linux operating system.

## [Use ALSA on with Applications requiring PulseAudio]

Using applications which require PuleAudio on systems which only have ALSA installed can be accomplished through the use of **apulse** which is a pulse emulator for ALSA.

### [Install apulse]

Install **apulse** from the [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") using a your preferred package manager or the command:

[user \$ ][ pamac build apulse [COPY TO CLIPBOARD]]

\

It is built from source so it may take some time to install. Once it is done, create a basic config file using the command:

[user \$ ][ cp /usr/share/apulse/asoundrc.sample \~/.asoundrc [COPY TO CLIPBOARD]]

\

### [Using apulse]

Using apulse is a simple typing **apulse \** in a terminal. For example:

[user \$ ][ apulse /usr/lib/firefox/firefox [COPY TO CLIPBOARD]]

\

If all is working, you should now have sound in Firefox without needing pulseaudio

## [Selecting the Primary Audio Device]

If your system keeps on using the wrong device (HDMI instead of PCH or vica versa for example), you can force ALSA to use the correct device. Start by getting a list of your audio devices with the command:

[user \$ ][ cat /proc/asound/cards [COPY TO CLIPBOARD]]

\

Note the number of the sound device that you want to make the primary. Then using a [text editor](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files "Viewing and editing configuration files"), put the following into **/etc/asound.conf** (You may need to create **/etc/asound.conf** if it doesn\'t already exist).

[user \$ ][ sudo nano /etc/asound.conf [COPY TO CLIPBOARD]]

\

/etc/asound.conf

    defaults.pcm.card 1
    defaults.ctl.card 1

Replace 1 in the above example with the number you noted down above.

## [See also]

-   [The official apulse site](https://github.com/i-rinat/apulse)
-   [apulse Forum Topic](https://forum.manjaro.org/t/how-to-run-pulseaudio-only-apps-on-an-alsa-only-system/34235)