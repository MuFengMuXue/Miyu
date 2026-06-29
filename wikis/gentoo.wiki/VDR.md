This page contains [[changes](https://wiki.gentoo.org/index.php?title=VDR&oldid=1046220&diff=1324080)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/VDR/es "VDR (95% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/VDR/hu "Video Disk Recorder (VDR) (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/VDR/ru "VDR (33% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/VDR/ja "VDR (33% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/VDR/ko "VDR (85% translated)")

[]  As of **March 12th, 2015**, the information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=VDR&action=edit).

This article contains instructions on how to prepare Gentoo Linux for DVB and VDR.

## Contents

-   [[1] [General information to DVB]](#General_information_to_DVB)
    -   [[1.1] [What is DVB?]](#What_is_DVB.3F)
    -   [[1.2] [Types and requirement of DVB cards]](#Types_and_requirement_of_DVB_cards)
-   [[2] [Preparing the system]](#Preparing_the_system)
    -   [[2.1] [Configuring the kernel]](#Configuring_the_kernel)
    -   [[2.2] [Checking the kernel output]](#Checking_the_kernel_output)
-   [[3] [Installing VDR]](#Installing_VDR)
-   [[4] [Installing the remote control]](#Installing_the_remote_control)
    -   [[4.1] [Installing vdr-remote]](#Installing_vdr-remote)
    -   [[4.2] [Alternative: installing LIRC]](#Alternative:_installing_LIRC)
-   [[5] [Video output methods]](#Video_output_methods)
    -   [[5.1] [Hardware decoding: full-featured DVB cards]](#Hardware_decoding:_full-featured_DVB_cards)
    -   [[5.2] [Hardware decoding: DXR3/Hollywood+ cards]](#Hardware_decoding:_DXR3.2FHollywood.2B_cards)
    -   [[5.3] [Hardware decoding: PVR350 cards]](#Hardware_decoding:_PVR350_cards)
    -   [[5.4] [Software decoding: vdr-xineliboutput]](#Software_decoding:_vdr-xineliboutput)
-   [[6] [Creating a channel list]](#Creating_a_channel_list)
    -   [[6.1] [Using dvbscan from linuxtv-dvb-apps]](#Using_dvbscan_from_linuxtv-dvb-apps)
    -   [[6.2] [Using vdr-reelchannelscan]](#Using_vdr-reelchannelscan)
    -   [[6.3] [Channels for systems using vdr-analogtv]](#Channels_for_systems_using_vdr-analogtv)
-   [[7] [Starting VDR]](#Starting_VDR)
-   [[8] [VDR and Kodi]](#VDR_and_Kodi)
-   [[9] [Troubleshooting]](#Troubleshooting)

## [General information to DVB]

### [][What is DVB?]

*DVB* stands for *Digital Video Broadcasting*. DVB describes methods to transfer digital data of TV, radio, interactive services like MHP, EPG and teletext. Through data compression with MPEG-2, or H.264 for HDTV, it\'s possible to transfer several channels on the same frequency. The more data compression, the more channels can be transferred, however it is paid for by loss of quality.

DVB can be transferred in several ways. The trailing letter identifies the method of transfer, e.g. DVB-*T* for terrestrial transmission. There are several more types:

-   DVB-S for transmission over satellites;
-   DVB-C for transmission over cable;
-   DVB-H for transmission to mobile devices (terrestrial);
-   DVB-IPI for transmission over IP based networks, e.g. internet;
-   DVB-RC(S/C/T) return channel for the transmission of data services, e.g. broadband internet.

### [Types and requirement of DVB cards]

Besides the different methods available to receive a DVB stream, the cards are classified by their type of produced output. There are cards with a decoder implemented which offer direct access to the stream by the device [/dev/video]. These cards are *full featured cards*. Other cards have no own decoder implemented and require a software decoder on the computer and are *budget cards*. This implies higher system requirements. The computer\'s CPU should run at at least 600 MHz, and have at least 256MB of RAM. [This list](http://linuxtv.org/wiki/index.php/DVB_Card_Vendors) is useful for identifying the card.

## [Preparing the system]

### [Configuring the kernel]

First, ensure that the kernel supports DVB and the DVB device. Since kernel version 2.6 the necessary drivers are included. Check the kernel configuration and make sure the following options are selected as a static driver or as modules.

[KERNEL] **Required kernel options**

    Input Device Support --->
    * Event Interface
    Device Drivers --->
    <M> Multimedia Support --->
      [*] Digital TV support
       M  [Enable driver(s)]

Additionally select the proper driver for the system\'s hardware. To find the right module for the card mark every driver as module. If a PCI card is being used, then install the [[[sys-apps/pciutils]](https://packages.gentoo.org/packages/sys-apps/pciutils)[]] package if it has not been previously installed. This will provide a helpful tool called [lspci]. For built-in drivers or if there is no PCI card in the system then skip this step and continue with [Checking the kernel output](#Checking_the_kernel_output).

`root `[`#`]`emerge --ask sys-apps/pciutils`

After booting from the new kernel, run [pcimodules] to list the required modules:

`root `[`#`]`pcimodules`

    ohci-hcd
    ehci-hcd
    sis900
    snd-emu10k1
    b2c2-flexcop-pci
    nvidia
    nvidiafb

In this case the module `b2c2-flexcop-pci` needs to be loaded. Add the module\'s name to the [/etc/conf.d/modules] file:

[FILE] **`/etc/conf.d/modules`**

    modules="b2c2-flexcop-pci"

### [Checking the kernel output]

It is recommended to mark every driver as module, so that the required module can be added dynamically, especially if it is unclear at first which module should be added. If the module name is known then select the driver as a built-in driver. Compile the kernel, install the modules, and boot the new kernel. Verify the kernel has successfully detected the PCI card by using the [dmesg] utility.

If the system has a TerraTec Cinergy T2 card the output might look something like the following:

`root `[`#`]`dmesg | grep DVB`

    DVB: registering new adaptor (TerraTec/qanu USB2.0 Highspeed DVB-T Receiver).
    input: TerraTec/qanu USB2.0 Highspeed DVB-T Receiver remote control as /class/input/input2

## [Installing VDR]

To install VDR simply emerge it:

`root `[`#`]`emerge --ask media-video/vdr`

## [Installing the remote control]

There are at least two ways to control VDR via an infrared remote control. If the TV card has an onboard IR receiver then `vdr-remote` can be used. Otherwise, use LIRC.

### [Installing vdr-remote]

Install the plugin via an [emerge] command:

`root `[`#`]`emerge --ask media-plugins/vdr-remote`

`root `[`#`]`eselect vdr-plugin enable remote`

When using the remote plugin for the IR port on a DVB card everything should be fine with the default configuration. It automatically uses the input device which has \"dvb\" in its name. For more advanced uses take a look at [/etc/conf.d/vdr.remote] file.

### [Alternative: installing LIRC]

If the card can be remotely controlled but managing it via `vdr-remote` is not desired, then LIRC should be configured. LIRC interprets the pressed keys and returns a name for each one. A program that supports LIRC waits for key events and runs the action configured in the configuration file, mostly stored in the configuration directory of the executing program (e.g. [mplayer] loads the file [\~/.mplayer/lircrc]). Before LIRC is installed add `lirc` as a USE flag and add a special variable called `LIRC_DEVICES` to [/etc/portage/make.conf]. Use [this list](http://www.lirc.org/html/table.html) to find the proper arguments for the new [make.conf] variable.

[FILE] **`/etc/portage/make.conf`**

    USE="lirc"

[FILE] **`/etc/portage/package.use/00lirc=bash`**

    */* LIRC_DEVICES:  devinput # (Replace "devinput" with the proper driver)

`root `[`#`]`emerge --ask app-misc/lirc`

At start each key code must be defined with a name. Most supported remote controls are configured already, so take a look at the [remote list](http://lirc.sourceforge.net/remotes/). Download the required file and save it as [/etc/lircd.conf]. Now find out where to access the remote control. Run the following command to get a list of the current input devices (make sure the device is running).

`root `[`#`]`cat /proc/bus/input/devices`

    I: Bus=0000 Vendor=0000 Product=0000 Version=0000
    N: Name="TerraTec/qanu USB2.0 Highspeed DVB-T Receiver remote control"
    P: Phys=usb-0000:00:1d.7-1/input0
    S: Sysfs=/class/input/input2
    H: Handlers=kbd event1
    B: EV=100003
    B: KEY=108fc210 2043 0 0 0 0 8000 2080 1 9e1680 0 0 ffc

In this case the Terratec Cinergy T2 device plugged in, so the device can be accessed over [/dev/input/\<event1\>]. Replace `<event1>` with the matching device listed in the output.

[lircd] needs to know the device to use. Add the following line to the [/etc/conf.d/lircd] file. Remember to replace `<devinput>` with the name of the driver and `<event1>` with the actual device:

[FILE] **`/etc/conf.d/lircd`**

    LIRCD_OPTS="-H <devinput> -d /dev/input/<event1>"

It is time to start [lircd]:

`root `[`#`]`/etc/init.d/lircd start`

Now it should be possible to watch [lircd] capturing and decoding key presses. Run the [irw] command. Stop it by pressing [Ctrl]+[C] when enough keys have been pressed.

`root `[`#`]`irw`

    0000000000001aa2 00 Exit Technisat_TTS35AI.conf
    0000000000001a8d 00 Mute Technisat_TTS35AI.conf
    0000000000000a97 00 OK Technisat_TTS35AI.conf
    0000000000000a97 01 OK Technisat_TTS35AI.conf
    0000000000000a92 00 Menu Technisat_TTS35AI.conf

Next, add it to the default runlevel so that it starts automatically at boot time:

`root `[`#`]`rc-update add lircd default`

To be able to use the remote control, LIRC support must be enabled in VDR. Add the following line to the [/etc/conf.d/vdr] file:

[FILE] **`/etc/conf.d/vdr`**

    IR_CTRL="lirc"

## [Video output methods]

Now decide on one (and only one) of the following video output devices which show the picture and the overlayed On Screen Display (OSD).

### [Hardware decoding: full-featured DVB cards]

Install [[[media-plugins/vdr-dvbhddevice]](https://packages.gentoo.org/packages/media-plugins/vdr-dvbhddevice)[]] when using an TechnoTrend Premium S2-6400 Twin HD, or general hardware decoding for SDTV and HDTV (MPEG2 and MPEG4 AVC/H.264):

`root `[`#`]`emerge --ask media-plugins/vdr-dvbhddevice`

For Fujitsu_Siemens, Hauppage WinTV and TechnoTrend Premium S2300 and cards based on this reference design, or general hardware decoding for SDTV (MPEG1 and MPEG2):

`root `[`#`]`emerge --ask vdr-dvbsddevice`

### [][Hardware decoding: DXR3/Hollywood+ cards]

To use a DXR3 card for VDR output the `vdr-dxr3` plugin is needed:

`root `[`#`]`emerge --ask vdr-dxr3`

[FILE] **`/etc/conf.d/modules`**

    modules="em8300"

The em8300 module need some configuration that depends on the exact revision of that card.

### [Hardware decoding: PVR350 cards]

Since PVR350 cards have an onboard MPEG-Decoder chip it should be used to its full potential. In order for this to happen the `vdr-pvr350` plugin is needed. If `ivtv-driver` is not yet installed emerge should automatically install it. To have the `ivtv` module loaded at boot time add it to the [/etc/conf.d/modules] list:

`root `[`#`]`emerge --ask media-plugins/vdr-pvr350`

[FILE] **`/etc/conf.d/modules`**

    modules="ivtv"

### [Software decoding: vdr-xineliboutput]

Some people prefer to use `vdr-xineliboutput`, because it can work remotely. Follow the next set of instructions to configure `vdr-xineliboutput` on a host and client. First, the host setup:

`root `[`#`]`emerge --ask media-plugins/vdr-xineliboutput`

`root `[`#`]`eselect vdr-plugin enable xineliboutput`

Adding command line options at this point is crucial for xineliboutput to work. For more options, see [vdr \--help].

[FILE] **`/etc/conf.d/vdr.xineliboutput`**

    _EXTRAOPTS="--local=none --remote=37890"

The next step is to edit [/etc/vdr/svdrphosts.conf]. This file describes a number of host addresses that are allowed to connect to the SVDRP port of the video disk recorder running on the host system.

[FILE] **`/etc/vdr/svdrphosts.conf`**

    # (The proper syntax is: IP-Address[/Netmask])
    127.0.0.1             (always accept localhost)
    192.168.1.0/24        (any host on the local net)
    #204.152.189.113      (a specific host)
    #0.0.0.0/0            (any host on any net - USE THIS WITH CARE!)

When using `vdr-xineliboutput` to view the picture on the same computer as the one running VDR it is now possible to continue with [#creating the channel list](#creating_the_channel_list).

Otherwise, simply [emerge] [[[media-plugins/vdr-xineliboutput]](https://packages.gentoo.org/packages/media-plugins/vdr-xineliboutput)[]] on the client:

`root `[`#`]`emerge --ask media-plugins/vdr-xineliboutput`

Later (after having started VDR) the [vdr-sxfe xvdr://hostname] command can be used to connect to the VDR and view its picture and OSD.

** Note**\
There is also a plugin which simulates the existence of a real output device (`vdr-dummydevice`) for some fancy uses like record-only servers, but that is more advanced than a normal VDR setup.

## [Creating a channel list]

To make VDR really useful an appropriate channel list must be created. There is more than one way to get a working list of channels (besides downloading one). The channel list installed by default is for DVB-S reception on Astra on 19.2° E.

### [Using dvbscan from linuxtv-dvb-apps]

`root `[`#`]`emerge --ask media-tv/linuxtv-dvb-apps`

Find the correct frequency list for region and type of reception of interest. These files are stored under [/usr/share/dvb]. For reception with DVB-T in Germany, Berlin [/usr/share/dvb/dvb-t/de-Berlin] should be used:

`user `[`$`]`dvbscan -o vdr /usr/share/dvb/dvb-t/de-Berlin > /etc/vdr/channels.conf`

### [Using vdr-reelchannelscan]

First, delete the contents of the existing channel list:

`root `[`#`]`rm /etc/vdr/channels.conf`

`root `[`#`]`emerge --ask vdr-reelchannelscan`

`root `[`#`]`eselect vdr-plugin enable reelchannelscan`

### [Channels for systems using vdr-analogtv]

It is a good idea to configure channels at this point. The VDR project provides users with some examples which can be found at [/usr/share/doc/vdr-analogtv-\$version/examples/], as long as `media-plugins/vdr-analogtv-1.0.00-r1` and up has been installed.

## [Starting VDR]

After having all basic software parts ready on the system the VDR with its OSD must be configured.

If a hardware decoder for picture output is used, then the connected TV should be turned on. When using software output the client for this must be started after VDR.

First, learn the key definitions; that is, connecting keys on the remote control to VDR\'s internal commands.

** Note**\
To edit the keyboard configuration, or (more likely) to delete it to go back to learning the keys the special configuration file can be modified. VDR stores its key-definitions in [/etc/vdr/remote.conf].

We begin with starting VDR:

`root `[`#`]`/etc/init.d/vdr start`

    * Preparing start of vdr:
    *   config files ...                                        [ ok ]
    *   Waiting for prerequisites (devices nodes etc.) ...      [ ok ]
    * Starting vdr ...                                          [ ok ]
    * First start of vdr: No check for running vdr possible
    * until control device (remote/keyboard) keys are learnt!

** Note**\
Users of software decoders should now start the client program that opens the window to show the TV picture and the OSD.

For users of vdr-softdevice:

`root `[`#`]`ShmClient`

For users of vdr-xineliboutput:

`root `[`#`]`vdr-sxfe xvdr://hostname`

The most useful keys for VDR are:

-   Cursor keys (Left/Right/Up/Down)
-   Menu/Exit/Ok
-   Colors (Red/Green/Yellow/Blue)
-   Number keys (0-9)

** Important**\
If not many keys exist on the remote be sure to assign these. Some remotes have Play/Pause/etc. on the same keys as the colors, so use them for the colors.

Now that the basic installation is over it is time to configure VDR. Switch to the output screen and follow the on-screen instructions. VDR asks the user to press various keys on the remote control so it can learn the correct key codes. If a remote control is not present, then the keyboard can be used as an alternative.

Now add the VDR init script to the default runlevel to get it started each time the computer boots:

`root `[`#`]`rc-update add vdr default`

## [VDR and Kodi]

Enable the vdr-devel overlay

`root `[`#`]`eselect repository enable vdr-devel `

`root `[`#`]`emerge --sync`

`root `[`#`]`emerge --ask media-plugins/vdr-vnsiserver media-plugins/kodi-pvr-vdr-vnsi`

There\'s a systemd service part of the vdr package, obviously for those using systemd.

`root `[`#`]`systemctl start vdr.service`

## [Troubleshooting]

If help is needed feel free to ask someone in [#gentoo-vdr](irc://irc.gentoo.org/gentoo-vdr), or look around on the [Gentoo forums](http://forums.gentoo.org/)

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Norman Golisz, Dimitry Bradt, Matthias Schwarzott, Joshua Saddler**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*