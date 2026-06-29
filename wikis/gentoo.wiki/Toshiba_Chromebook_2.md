\

## Contents

-   [[1] [Summary]](#Summary)
-   [[2] [Hardware]](#Hardware)
-   [[3] [Disclaimer/Prerequisites]](#Disclaimer.2FPrerequisites)
-   [[4] [Notes]](#Notes)

## [Summary]

Everything works as of 13th August, after this [SeaBIOS update](https://johnlewis.ie/baytrail-update/) by John Lewis. Latest ChromeOS fw + John Lewis\' SeaBIOS has both working suspend and working VPX (kvm)

## [Hardware]

-   Intel Celeron N2840 - Dual Core, fanless
-   4 GB RAM (for model CB30-B-104) or 2 GB RAM (for model CB30-B-103)
-   1080p IPS screen (non-touch)
-   Elan Touchpad
-   16 GB eMMC card as storage (embedded in mainboard, cannot be replaced)
-   SD Card slot
-   Intel 7260 AC-Wifi with Bluetooth
-   Chromebook codename from Google: swanky

## [][Disclaimer/Prerequisites]

-   You have to open the machine, dismantle and cut off a piece of the heat shield to disable flash write protect.^[\[1\]](#cite_note-coreboot-1)^
-   You must install [John Lewis\' SeaBIOS](https://johnlewis.ie/custom-chromebook-firmware/rom-download/) to the flash, and to begin this you first have to do the aforementioned modification, and then enable developer mode on your Chromebook. You can enter this mode in the same way as on a Acer C7 Chromebook, and the procedure is described [here](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/acer-c7-chromebook#TOC-Entering).
-   You should have a large SD Card (SDXC UHC-1-type cards seems to work) if you want to use it as a normal laptop, as 16 GB storage can be a tad small. The internal storage cannot be upgraded, it\'s soldered to the mainboard.
-   The swanky board code, blobs and config are not upstreamed to coreboot as of 2015/08/21, so it\'s not an easy task to compile your own firmware for this. So, the best (and maybe only) solution yet is to use John Lewis\' SeaBIOS flasher.

## [Notes]

-   The sound driver name is CONFIG_SND_SOC_INTEL_BYT_MAX98090_MACH
-   You cannot use genkernel on this if you want sound, the sound driver (BYT_MAX98090) depends on having all other codecs disabled, so normal distro kernels do not support sound^[\[2\]](#cite_note-BYT_MAX98090-2)^
-   This makes the arch wiki^[\[3\]](#cite_note-Arch_Wiki_Toshiba_Chromebook_2-3)^ refer to sound not having support after kernel 4.5.0, but this is not true, you just have to enable the right config and disable all others.
-   First time you boot you might have to use alsamixer and unmute \"Left Speaker Mixer Right DAC\" and \"Right Speaker Mixer Right DAC\" (see [this blogpost](https://johnlewis.ie/procedure-to-get-sound-working-in-fedora-22-on-asus-c300-chromebook/))
-   Setting up the kernel config is a bit hard if doing it from scratch. A nice way to make your own kernel config right, is using a Fedora LiveUSB environment and use \`make localmodconfig´ or \`make localyesconfig´ when configuring your kernel.
-   The kernel need some msecs of time to enumerate your eMMC device and eventual SD card, so you won\'t get this system to boot without either an initrd, or if you don\'t use an initrd, the kernel boot parameters \`rootdelay=2´. One second might be enough, but with two seconds you\'re sure.
-   On my setup I use pulseaudio, and I had to have this .asoundrc^[\[4\]](#cite_note-PulseAudio_Perfect_Setup-4)^ file in my home folder to make sound in alsa applications works (for instance adobe-flash)

[FILE] **`.asoundrc`**

    pcm.!default
    ctl.!default

1.  [[[↑](#cite_ref-coreboot_1-0)] [[See the two pictures of Swanky mainboard for how to disable flash write protect](http://www.coreboot.org/Chromebooks)]]
2.  [[[↑](#cite_ref-BYT_MAX98090_2-0)] [[LKML about BYT_MAX98090](https://lkml.org/lkml/2016/8/12/180)]]
3.  [[[↑](#cite_ref-Arch_Wiki_Toshiba_Chromebook_2_3-0)] [[Arch Wiki Toshiba Chromebook 2](https://wiki.archlinux.org/index.php/Toshiba_Chromebook_2)]]
4.  [[[↑](#cite_ref-PulseAudio_Perfect_Setup_4-0)] [[PulseAudio Perfect Setup](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/PerfectSetup/)]]