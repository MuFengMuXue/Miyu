This page contains [[changes](https://wiki.gentoo.org/index.php?title=Bluetooth_headset&oldid=1411448&diff=1439589)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Bluetooth_headset/hu "Bluetooth headset (99% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Bluetooth_headset/ta "ஊடலை தலையணி ஒலிவாங்கி (18% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Bluetooth_headset/ja "Bluetooth ヘッドセット (45% translated)")

This article describes the configuration of Bluetooth [headsets](https://en.wikipedia.org/wiki/Headset_(audio) "wikipedia:Headset (audio)") within Gentoo Linux.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [PipeWire]](#PipeWire)
    -   [[2.2] [ALSA + Bluez 5]](#ALSA_.2B_Bluez_5)
-   [[3] [Testing]](#Testing)
-   [[4] [Working devices]](#Working_devices)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Failed to connect (br-connection-profile-unavailable)]](#Failed_to_connect_.28br-connection-profile-unavailable.29)
    -   [[5.2] [Can\'t open input device]](#Can.27t_open_input_device)
    -   [[5.3] [No audio service is available]](#No_audio_service_is_available)
    -   [[5.4] [Audio device not visible when using GDM]](#Audio_device_not_visible_when_using_GDM)
    -   [[5.5] [Audio device not visible using PulseAudio volume control (but working with ALSA)]](#Audio_device_not_visible_using_PulseAudio_volume_control_.28but_working_with_ALSA.29)
    -   [[5.6] [Transport already configured with Couldn\'t select codec]](#Transport_already_configured_with_Couldn.27t_select_codec)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Prerequisites]

The configurations for [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") and [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") must have been previously completed (just configurations, some devices do not connect without [[[media-sound/bluez-alsa]](https://packages.gentoo.org/packages/media-sound/bluez-alsa)[]] setup).

Also, `ofono-headset` USE flags might be useful:

[FILE] **`/etc/portage/package.use/pulseaudio`**

    media-sound/pulseaudio-daemon ofono-headset

Additionally, if you have `CONFIG_BT_RFCOMM` set as builtin in the kernel, it is possible that the microphone (if there is one) of the headset will not be found by PipeWire/PulseAudio/ALSA. In this situation, setting `CONFIG_BT_RFCOMM` as module should be enough for it to be detected.

## [Configuration]

### [PipeWire]

Following instructions from [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") and [BlueZ 5](https://wiki.gentoo.org/wiki/Bluetooth#BlueZ_5 "Bluetooth") should be sufficient to make Bluetooth headsets work (through *pavucontrol* for instance).

There is two protocols for handling microphone input (and button input) from headsets: HSP and HFP. In order for the microphone to work the headset has to switch from the A2DP protocol to HSP/HFP. Headset using HSP will usually work out-of-the-box with the current pipewire version.

### [][ALSA + Bluez 5]

You can use [bluez-alsa](https://github.com/Arkq/bluez-alsa) to provide integration between Bluez and ALSA. This setup can be used either completely without Pulseaudio, or you can then use your headset as another ALSA device in Pulseaudio (in which case disable its bluetooth support, so the two don\'t collide).

Install bluez-alsa:

`root `[`#`]`emerge --ask media-sound/bluez-alsa`

in /etc/dbus-1/system.d/bluealsa.conf add lines that allow \"sink\" and \"source\" destinations as a part after \"org.bluealsa\" dbus address.

[FILE] **`/etc/dbus-1/system.d/bluealsa.conf`**

    <busconfig>

        <allow own_prefix="org.bluealsa" />
        <allow send_destination="org.bluealsa" />
        <allow send_destination="org.bluealsa.sink" />
        <allow send_destination="org.bluealsa.source" />
      </policy>


        <allow send_destination="org.bluealsa" />
        <allow send_destination="org.bluealsa.sink" />
        <allow send_destination="org.bluealsa.source" />
      </policy>
    </busconfig>

Run bluez-alsa under root:

`root `[`#`]`bluealsa -p a2dp-sink -p a2dp-source --initial-volume=20 & `

Some headphones require both the a2dp and hsp protocols in order to use a2dp. A simple alternative command to try that allows headphones to be used for listening-only is:

`root `[`#`]`bluealsa -p hsp-ag -p a2dp-source & `

This will enable the headset gateway protocol along with A2DP for enhanced audio playback.

In your ALSA configuration, [/etc/asound.conf] (system-wide) or [\~/.asoundrc] (user-level), specify the parameters of the Bluetooth connection (replace the MAC address with the MAC address of your device):

[FILE] **`/etc/asound.conf or ~/.asoundrc`**

    # Bluetooth headset
    defaults.bluealsa

A static ALSA configuration is also possible, make sure to change the device name in the below examples for aplay.

[FILE] **`/etc/asound.conf or ~/.asoundrc`**

    # Bluetooth headset
    pcm.!default
            hint
    }
    ctl.!default

Make sure the *bluetooth* and *bluealsa* services are started. You probably want to add them to your default runlevel via *rc-config*. Make sure the device is paired and connected to your computer (see [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") for details) and test with aplay, passing the PCM device `bluealsa`:

`user `[`$`]`aplay -D bluealsa some_file.wav`

For other applications, the precise option to set the output device may differ.

** Note**\
Changes to ALSA configuration files [/etc/asound.conf] and [\~/.asoundrc] are picked up automatically at application start, you don\'t need to restart the *alsasound* service.

Hardware volume control:

`user `[`$`]`alsamixer -D bluealsa`

## [Testing]

Play a sound file with [mplayer](https://wiki.gentoo.org/wiki/Mplayer "Mplayer"):

`user `[`$`]`mplayer -ao alsa:device=bluealsa `*`filename`*

Or with [mpv](https://wiki.gentoo.org/wiki/Mpv "Mpv"):

`user `[`$`]`mpv --audio-device=alsa/bluealsa `*`filename`*

If it works, please add your device to the table of [working](https://wiki.gentoo.org/wiki/Bluetooth_headset#Working_devices "Bluetooth headset") devices.

## [Working devices]

** Note**\
The capabilities of the device are dependent on the Bluetooth controller being used.

  ------------------------------------------------------- ----------- ------------- --------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
  Device                                                  Headphone   Microphone    BlueZ Version   Notes
  AfterShokz TREKZ Titanium                               Yes         Not tested    5.50-r2
  AKG N700NC                                              Yes         Not tested    5.52            Update headset firmware to latest version 0.2.7.
  Beats By Dre PowerBeats3                                Yes         Not tested    5.55            Apply module loading to /etc/pulse/default.pa and system.pa with latest version of Bluez as device and module will not load otherwise. Supports a2dp. Media key presses work for volume, double press next, single press pause, triple click previous.
  Bose SoundSport Free (423729)                           Yes         Not tested    5.55
  Bose SoundSport Free (774373-0010)                      Yes         Not tested    5.48-r1
  Bose QC Earbuds                                         Yes         Not tested    5.55
  Bose QC35 II Headset                                    Yes         Yes           5.61
  Bose QC45 Headset (marketing rename A.K.A: \"QC SE\")   Yes         Not tested    5.82            A2DP only works after interaction of Bose app. FW upgrades from this era of Bose are known to brick headsets (some buds too), beware.
  the BTunes 3                                            Yes         Not tested    5.54
  Cellular Innovations HFBLU-ST6                          Yes         No            ?
  Comexion M100                                           Yes         Yes           5.64            Pulseaudio needed **native-headset** USE flag. Manual switching between A2DP and HFP bluetooth profiles is done with pavucontrol.
  Creative BT-W2 USB Bluetooth Dongle                     Yes         Not tested    5.52            Tested on desktop PC without built-in Bluetooth. Very straightforward setup. Requires kernel USB audio enabled. Volume and Play/Pause work. Pair with any Bluetooth headphones. Compile alsa-plugins with speex libsamplerate and ffmpeg USE flags to provide options for better sampling.
  Dell BH200                                              Yes         Not tested    ?
  Google Pixel Buds                                       Yes         Yes           5.49-r1
  Huawei FreeBuds                                         Yes         Not tested    5.49-r1
  Jabra MOVE v2.3.0                                       Yes         Yes           5.39            If supported, AAC codec is selected, otherwise SBC
  Jabra Elite 65t                                         Yes         Yes           5.70-r1
  Jabra Elite 2                                           Yes         Yes           5.70-r1         Sometimes the audio is lost for a very short time.
  Jabra Evolve2 75                                        Yes         Yes           5.66-r1         I needed to install \*both\* pulseaudio-daemon and pulseaudio with appropriate USE flags (sys-apps/portage-3.0.44-r1 dated Sat Apr 1 2023. Feel free to remove this instruction if the dependency is no longer present.)
  JBL CLUB PRO+ TWS                                       Yes         Not tested    5.66-r1
  JBL E40BT                                               Yes         Not tested    5.47
  JBL JBL Endurance SPRINT                                Yes         Not tested    5.55
  JBL GO+                                                 Yes         Not tested    5.50-r2
  JBL Live 400BT                                          Yes         Yes           5.62-r3         It seems some them come with factory defect making mic level too low and impossible to change
  JBL T450BT                                              Yes         Not tested    5.43
  JBL Live 500BT                                          Yes         No            5.54
  JBL Live 770NC                                          Yes         Yes           5.71-r1         The kernel option *CONFIG_BT_RFCOMM* need to be set as module. This was tested with [[[media-video/pipewire]](https://packages.gentoo.org/packages/media-video/pipewire)[]] 1.0.1 (via [[[media-video/wireplumber]](https://packages.gentoo.org/packages/media-video/wireplumber)[]] 0.5.17-r1).
  JBL FLIP5                                               Yes         No            5.70-r1
  LG HBS730                                               Yes         No            ?
  Lenovo HX106                                            Yes         Yes           5.61            media-sound/bluez-alsa-3.1.0 is necessary
  Marshall Major II                                       Yes         Not tested    5.51
  Marshall MID                                            Yes         Not tested    5.51
  Marshall Stockwell                                      Yes         Not tested    BlueZ 5.54      Bluetooth Speaker tested successfully. Microphone not applicable
  Mi Bluetooth Headset Basic LYEJ02LM                     Yes         Yes           BlueZ 5.61-r1   Bluetooth Headset Speaker and Microphone both tested successfully.
  Nokia BH-214                                            Yes         No            4.101 & 5.39
  Nokia BH-604                                            Yes         Yes           ?
  Parrot Zik                                              Yes         Not tested    ?
  Philips SBH6201                                         Yes         Yes           ?
  Philips SBH9100                                         Yes         Not tested    ?
  Pioneer SE-MS9BN-G                                      Yes         Yes           5.50-r1         Microphone tested successfully with BlueZ 5.50-r1 and HSP/HFP profile. Volume and play-pause buttons recognized as Multimedia events in Xfce (XF86AudioNext - XF86AudioPrev - XF86AudioPlay). No special bluetooth configuration is required. You should only make sure that pulseaudio is built with native-headset useflag, and that pulseaudio spawns correctly from your X session.
  Plantronics BackBeat GO                                 Yes         Not tested    ?
  Plantronics BackBeat PRO 2                              Yes         Yes           5.52            The microphone works with HSP/HFP. Pulseaudio have to be built with native-headset USE flag to have the microphone working. Buttons work when \"User level driver support\" is added in the kernel.
  Prestigio PBHS1                                         Yes         Not tested    ?
  Sennheiser HD 4.40 BT                                   Yes         Not tested    5.50-r2
  Sennheiser MM 550-X Travel                              Yes         Yes           5.27            Microphone tested successfully with BlueZ 4.x/HSF. With bluez 5.58-r1 switch of audio profile from A2DP to HSP/HFP does not work. Hence microphone does not work.
  Sennheiser PXC 550                                      Yes         Not tested    5.50-r1         Confirmed working with older versions, but not sure how far back. Tested with bluez-alsa (currently 1.3.1), not Pulse Audio. Media controls not tested.
  Sennheiser URBANITE XL Wireless                         Yes         Not tested    5.46            Volume swipes are working
  Shure Aionic TW2                                        Yes         Not tested    5.64            May need to re-pair after pairing with another device.
  Shure RMCE-BT2                                          Yes         Not tested    5.52            Volume buttons adjust volume locally, not on host device. Microphone not detected. Tested with Pulseaudio, not with bluez-alsa.
  Shure True Wireless Secure Fit Adapter 2                Yes         Not tested    5.52            No issues.
  Sony DR-BTN200                                          Yes         No            5.39            All buttons except \"Call\" work and can be assigned shortcuts in the DE
  Sony MDR-1000X                                          Yes         No            5.50-r3         Volume swipes are working, prev/next swipes don\'t work.
  Sony MDR-ZX750BN                                        Yes         No            ?               The change track and volume buttons work.
  Sony MDR-ZX770BT                                        Yes         Not tested    4.101 & 5.25    4.101 requires Enable=Socket in /etc/bluetooth/audio.conf
  Sony SBH20                                              Yes         Not tested    ?
  Sony SBH52                                              Yes         Yes           ?               The buttons work and can be assigned actions in KDE. Supported rate 4800.
  Sony WH-XB900N                                          Yes         Yes           5.62-r3         Everything works well at least with [pipewire](https://wiki.gentoo.org/wiki/Pipewire "Pipewire"). Make sure kernel\'s RFCOMM/BNEP are compiled as modules and upower is compiled with \"ios\" use flag
  Sony WH-CH700N                                          Yes         Not tested    5.50-r3         Volume control works. BlueZ 5: blue-alsa
  Sony WH-CH710N                                          Yes         Yes           5.62-r3         Tested with pipewire-0.3.36. A2DP bt profile for good audio quality only, HSP/HFP bt profile for having both mic and audio.
  Sony WH-CH720N                                          Yes         Yes           5.84-r1
  Sony WH-1000XM2                                         Yes         Yes           5.56-r1         The touch interface (volume) on the right speaker works.
  Sony WH-1000XM3                                         Yes         Yes           5.55:0/3        The touch interface on the right speaker works. Strange echo of external sounds in headset mode (possibly feature not error). With bluez 5.58-r1 switch of audio profile from A2DP to HSP/HFP does not work. Hence microphone does not work.
  Sony WH-1000XM4                                         Yes         Yes           5.77            I\'m not sure which did it, but the microphone didn\'t work until after I changed CONFIG_BT_RFCOMM from builtin to module and set \"User level driver support\" in the kernel
  Sony WH-1000XM5                                         Yes         Yes           5.68            Touch panel is fine. Maybe you need to configure touch controls by hand in KDE for some app like Audacious. Auto-switch A2DP/HSP profile when activate mic, LDAC and mSBC supported. Pair with Intel AX201 USB adapter.
  Sony WI-1000X                                           Yes         Not Tested    5.62-r3
  Sony Ericsson HBH-DS200                                 Yes         Not tested    4.101 & 5.43    BlueZ 4: software volume control via .asoundrc. BlueZ 5: BlueALSA
  Sony Ericsson HBH-DS970                                 Yes         Not tested    ?               Requires *Enable=Socket* in [/etc/bluetooth/audio.conf].
  Soundcore Spirit Bluetooth Headphones                   Yes         Not tested    5.50-r2
  Teufel MUTE BT                                          Yes         Yes           5.47
  Apple AirPods Pro                                       Yes         No            5.54            Recording looks like it could work in ALSA, when profile is set to \"sco\". Recording does not work under normal PulseAudio use.
  Apple AirPods (1st generation)                          Yes         No            5.54            Recording is probably same as AirPods Pro.
  Xiaomi Redmi AirDots                                    Yes         No            5.54            There might be a way to make the microphone work, if you mess with pulseaudio and manage to get HSP/HFP to work, but I couldn\'t do it.
  CaseGuru CGpods 5.0                                     Yes         Not tested    5.54
  XO-ET32                                                 Yes         Not tested    5.68
  Soundcore Life Q30                                      Yes         Yes           5.55            Playback via Pulseaudio worked with A2DP out of the box, attempts to get the microphone work via HSP/HFP were unsuccessful with both native-headset and ofono/phonesim mess. I was able to get it working with bluez-alsa and then added the device to Pulseaudio as described [on bluez-alsa wiki](https://github.com/Arkq/bluez-alsa/wiki/PulseAudio-integration).
  Soundcore Liberty 4 NC                                  Yes         Yes           5.72            Playback and microphone work out of the box. After firmware update with smartphone, playback with LDAC also works. But with enabled LDAC it\'s not longer possible to dual-connect, and microphone doesn\'t work.
  ------------------------------------------------------- ----------- ------------- --------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## [Troubleshooting]

### [][Failed to connect (br-connection-profile-unavailable)]

When you have minimal setup, you may encounter:

`user `[`$`]`bluetoothctl`

    [bluetooth]# connect <MAC>
    Attempting to connect to <MAC>
    Failed to connect: org.bluez.Error.Failed br-connection-profile-unavailable

This may be due to PulseAudio not running [\[1\]](https://bbs.archlinux.org/viewtopic.php?pid=2011077#p2011077), so start some audio playback first to trigger PA server startup and then try again to connect with BT headset.

Also ensure that the `bluetooth` USE flag is enabled on your respective sound server, such as PulseAudio or PipeWire.

### [][Can\'t open input device]

Compile and load the *uinput* kernel module, when things don\'t work, and the logs show this error:

[CODE]

    bluetoothd: Can't open input device: No such file or directory (2)
    bluetoothd: AVRCP: failed to init uinput for 00:16:44:FD:6B:A0
    bluetoothd: Unable to select SEP

[KERNEL]

     Device Drivers  --->
        Input device support  --->
          [*]   Miscellaneous devices Search for <code>CONFIG_INPUT_MISC</code> to find this item.  --->
            <M>   User level driver support Search for <code>CONFIG_INPUT_UINPUT</code> to find this item.

### [No audio service is available]

After updating to [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]]-5.xx it might happen, that a Bluetooth headset is connected, but [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA")/[PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") fails to pick up the connected device.

An error message like this might be shown in the output of PulseAudio:

[CODE]

    I: [pulseaudio] module-card-restore.c: Restoring profile for card bluez_card.00_16_94_0B_6F_DE.
    I: [pulseaudio] card.c: Created 10 "bluez_card.00_16_94_0B_6F_DE"
    bt_audio_service_open: connect() failed: Connection refused (111)
    W: [pulseaudio] module-bluetooth-device.c: Bluetooth audio service not available
    W: [pulseaudio] module-bluetooth-device.c: Service not connected
    I: [pulseaudio] card.c: Freed 10 "bluez_card.00_16_94_0B_6F_DE"
    E: [pulseaudio] module.c: Failed to load module "module-bluetooth-device" (argument: "address="00:16:94:0B:6F:DE" path="/org/bluez/31716/hci0/dev_00_16_94_0B_6F_DE""): initialization failed.

To fix this, the following needs to be done:

-   Enable the audio socket of bluetoothd:

[FILE] **`/etc/bluetooth/audio.conf`**

    [General]
    Enable=Socket

-   Restart *bluetoothd* by doing one of the following things:
    -   Turn the software wireless kill switch off and on again

`root `[`#`]`rfkill block bluetooth`

`root `[`#`]`rfkill unblock bluetooth`

-   -   Turn the hardware wireless kill switch off and on again
    -   Reboot the computer
-   Reconnect the Bluetooth headset

### [Audio device not visible when using GDM]

If you are using GDM, but not logging into [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") (e.g. i3 instead), GDM might block your headset, which will it not being available for PulseAudio. This will result in your headset being connected, but the applications won\'t see it.

As a workaround, you can switch to a different display manager (e.g. [LXDM](https://wiki.gentoo.org/index.php?title=LXDM&action=edit&redlink=1 "LXDM (page does not exist)")), or disable PulseAudio for GDM^[\[1\]](#cite_note-1)^:

[FILE] **`/var/lib/gdm/.config/pulse/client.conf`**

    autospawn = no
    daemon-binary = /bin/true

If you have created the file, make sure that GDM can read it:

`root `[`#`]`chown gdm:gdm /var/lib/gdm/.config/pulse/client.conf`

### [][Audio device not visible using PulseAudio volume control (but working with ALSA)]

According to [this forum post](https://forums.gentoo.org/viewtopic-p-8392318.html#8392318), add the following to [/etc/pulse/default.pa] (and possibly [/etc/pulse/system.pa]):

[FILE] **`/etc/pulse/default.pa`**

    ### Automatically load driver modules for Bluetooth hardware
    .ifexists module-bluez5-device.so
    load-module module-bluez5-device
    .endif

    .ifexists module-bluez5-discover.so
    load-module module-bluez5-discover
    .endif

Ensure that the `pulseaudio` and `bluetooth` USE flags are enabled

### [][Transport already configured with Couldn\'t select codec]

If you are using certain headphones (Sony WH-1000XM5 for example) and trying to use A2DP, you may encounter an error from bluealsa such as:

`root `[`#`]`bluealsa -p hsp-ag -p a2dp-source`

    bluealsa: E: Transport already configured: /org/bluez/hci0/dev_xx_xx_xx_xx_xx_xx/sep1/fd0
    bluealsa: E: Couldn't set A2DP configuration: GDBus.Error:org.bluez.Error.Failed: Resource temporarily unavailable
    bluealsa: E: Couldn't select codec: SBC: Input/output error

If this occurs, try adding the option `--a2dp-force-audio-cd` to bluealsa. It is not clear why this works, but a good guess is that there is an attempt to open multiple connections to the headphones at different rates, and only one connection at a time is supported by bluealsa.

## [See also]

-   [Music Player Daemon (Bluetooth headset)](https://wiki.gentoo.org/wiki/MPD#Bluetooth_headset_.28optional.29 "MPD")

## [External resources]

-   [Gentoo Forums - Use headsets with Bluez 5 mini HowTo](https://forums.gentoo.org/viewtopic-p-7559356.html)

## [References]

1.  [[[↑](#cite_ref-1)] [Stanislav Naumuk. [Bluetooth a2dp](https://wiki.debian.org/BluetoothUser/a2dp#Workaround_1:_disable_pulseaudio_in_gdm), [Debian Wiki](https://wiki.debian.org/FrontPage), June 13th, 2015. Retrieved on March 18th, 2019.]]