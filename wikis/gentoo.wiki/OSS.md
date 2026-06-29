**Resources**

[[]][Home](http://www.opensound.com/wiki/index.php/Main_Page)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Open_Sound_System "wikipedia:Open Sound System")

Open Sound System (OSS) v4 is an alternative to [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") as a layer between programs and sound hardware. Users of v3 are encouraged to use the not so maintained v4 version which has a BSD and GPL-2 licences.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Ebuild]](#Ebuild)
        -   [[1.2.1] [Bug Report]](#Bug_Report)
    -   [[1.3] [Install]](#Install)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Compatibility]](#Compatibility)
    -   [[2.2] [CMI878x]](#CMI878x)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [osstest]](#osstest)
    -   [[3.2] [ossxmix]](#ossxmix)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [External Resources]](#External_Resources)

## [Installation]

Currently there is no maintained ebuild in portage for this software.

### [Kernel]

[KERNEL] **Sound card support**

    Device Drivers  --->
            <M> Sound card support  --->
                 --- Sound card support
                 < >   Advanced Linux Sound Architecture --->
                 < >   Open Sound System (DEPRECATED)  --->

### [Ebuild]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Open_Sound_System_(OSS)&action=edit).

You will first need [eselect-repository](https://wiki.gentoo.org/wiki/Eselect-repository "Eselect-repository")

`root `[`#`]`emerge --ask dev-vcs/git app-eselect/eselect-repository`

#### [Bug Report]

Ebuilds can also be found in [[[bug #184123]](https://bugs.gentoo.org/show_bug.cgi?id=184123)[]], which would need to be added to the local overlay

### [Install]

Build the modules and add [/etc/init.d/oss] to the default runlevel:

`root `[`#`]`emerge oss `

`root `[`#`]`rc-update add oss default`

## [Configuration]

General configuration after install.

### [Compatibility]

Many applications only provide support for ALSA, so it is a good idea to keep both USE flags enabled.

[FILE] **`/etc/portage/make.conf`**

    USE="... alsa oss ..."

OSS will create ALSA devices for those applications.

** Note**\
In the current ebuilds, this feature can be disabled using a USE flag like *salsa* or *libalsa*.

-   To be able to use OSS4 with [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") or other gstreamer-dependent desktop environments like xfce4: [[[media-plugins/gst-plugins-oss4]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-oss4)[]] (included in [[[media-libs/gst-plugins-good]](https://packages.gentoo.org/packages/media-libs/gst-plugins-good)[]]) was dropped from the official tree, so making an ebuild is necessary (quite easy for this one) or getting one from somewhere (bar-overlay, for example).

`root `[`#`]`emerge --ask media-plugins/gst-plugins-oss4`

### [CMI878x]

Unlike ALSA, OSS4 has fewer complex options to configure, so you won\'t need any \`soundon.user\'. Especially if your setup isn\'t complex or are using more than one sound card. In the latter case, you may want to keep a \`soundon.user\' file to be able to choose your first card (default card). And then, insert a few lines correcting devices nodes which can be problematic.

[FILE] **[`/usr/lib/oss/soundon.user`](https://raw.github.com/tokiclover/dotfiles/master/.scripts/soundon.user)**

    #!/bin/sh
    # $ID: /usr/lib/oss/soundon.user, 2012/07/27 12:57:40 -tclover Exp $
    modprobe -a oss_
    /usr/sbin/ossdetect -diu
    /usr/sbin/ossdevlinks
    # Remapping ossdevlinks links
    if [ -d /dev/oss/oss_cmi878x ]; then
        ln -sf /dev/oss/oss_cmi878x0/pcm1 /dev/dsp
        ln -sf /dev/oss/oss_cmi878x0/pcm1 /dev/dsp_ac3
        ln -sf /dev/oss/oss_cmi878x0/pcm1 /dev/dsp_in
        ln -sf /dev/oss/oss_cmi878x0/pcm1 /dev/dsp_mmap
        ln -sf /dev/oss/oss_cmi878x0/pcm1 /dev/dsp_multich
        ln -sf /dev/oss/oss_cmi878x0/pcm1 /dev/dsp_out
        vmixctl attach /dev/oss/oss_cmi878x0/pcm1 /dev/oss/oss_cmi878x0/pcm1
    else
        ln -sf /dev/oss/oss_hdaudio0/pcm0 /dev/dsp
        ln -sf /dev/oss/oss_hdaudio0/pcmin0 /dev/dsp_in
    #  ln -sf /dev/oss/oss_hdaudio0/spdout0 /dev/dsp
        ln -sf /dev/oss/oss_hdaudio0/spdout0 /dev/dsp_ac3
    #  ln -sf /dev/oss/oss_hdaudio0/spdin0 /dev/dsp_in
        ln -sf /dev/oss/oss_hdaudio0/spdout0 /dev/dsp_mmap
        ln -sf /dev/oss/oss_hdaudio0/spdout0 /dev/dsp_multich
        ln -sf /dev/oss/oss_hdaudio0/spdout0 /dev/dsp_out
    #  vmixctl attach /dev/oss/oss_hdaudio0/pcm0 /dev/oss/oss_hdaudio0/pcmin0
    fi
    # vim:fenc=utf-8:ft=sh:ci:pi:sts=0:sw=2:ts=2:

The previous script will check if there are devices nodes, so a sound card, with CMI878x driver and then relink almost everything to it or else use HDAudio.

** Note**\
Notice that, that file will be overridden whenever media-sound/oss is updated so you will have to add that file to:

[FILE] **`/etc/portage/make.conf`**

    CONFIG_PROTECT="... /usr/lib/oss/soundon.user ..."

Or else, create a file like \`\~/.scripts/soundon.user\' and edit \`/etc/init.d/oss\' to your liking.

[FILE] **`/etc/init.d/oss`**

    /usr/sbin/soundon
    /root/.scripts/soundon.user
    /usr/sbin/savemixer -L

Now you can enjoy Open Sound System. I found the sound with OSS4 to be better than what I can get with ALSA. There was a time when my CMI878x sound works only with OSS4 but a few things changed.

OSS4 has its own mixer so using extra sound daemons like pulseaudio, esd etc. is not necessary.

## [Usage]

OSS4 has several comandline tools and one gtk-GUI to configure the devices.

### [osstest]

Test all audio devices with the following command:

`user `[`$`]`osstest`

### [ossxmix]

ossxmix is the graphical tool to configure devices:

[![Oss ossxmix.png](/images/thumb/3/32/Oss_ossxmix.png/512px-Oss_ossxmix.png)](https://wiki.gentoo.org/wiki/File:Oss_ossxmix.png)

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=oss&order=bug_id%20DESC)[]]

## [External Resources]

-   [configuring applications for OSSv4](http://www.opensound.com/wiki/index.php/Configuring_Applications_for_OSSv4)
-   [building OSSv4 from source](http://www.opensound.com/wiki/index.php/Building_OSSv4_from_source)