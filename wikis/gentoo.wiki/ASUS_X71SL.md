[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ASUS_X71SL&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Asus X71SL is a laptop manufactured by Asus.

Product page: [http://www.asus.com/Notebooks/Multimedia_Entertainment/X71SL/](http://www.asus.com/Notebooks/Multimedia_Entertainment/X71SL/)

This article describes the hardware on the X71SL and the drivers required to use it.

## [Hardware]

  ------------------- -------------------- -------------------------------------------- --------- -------------------------------
  Hardware Type       Device               Model                                        Support   Driver
  Processor           Processor            Intel Pentium(R) Dual-Core T4200 (2.00GHz)   Full      acpi-cpufreq
                      Power Management     ACPI                                         Full      acpi
                      PCI Express Bus      SiS 671MX                                    Full      pcieport
  Secondary Storage   Hard Disk            SiS (SATA / IDE mode!)                       Full      pata_sis?
                      DVD RW Drive         TSSTcorp CDDVDW TS-L633A                     Full      sata_sis
                      Memory Card Reader   Ricoh R5C822                                 Full      sdhci-pci
  Video Chipset       Discrete GPU         nVidia 9300M GS                              Full      nvidia
  Input               Keyboard             \-                                           Full      evdev
                      Touchpad             \-                                           Partial   synaptics
  Network             Gigabit Ethernet     SiS 191                                      Full      sis190
                      802.11n Wifi         Atheros AR928X                               Full      ath9k
                      Modem                N/A                                          ?         ?
                      Infrared Interface   N/A                                          ?         ?
  Sound               HD Audio             SiS, Azalia                                  Full      snd_hda_intel (realtek codec)
  Peripheral          USB 1.1              SiS USB 1.1 Controller                       Full      ohci_hcd
                      USB 2.0              SiS USB 2.0 Controller                       Full      ehci_hcd
                      IEEE 1394 Firewire   Ricoh R5C832                                 Full      firewire_ohci
                      Bluetooth            N/A (optional?)                              ?         ?
                      Webcam               Chicony USB2.0 1.3M UVC WebCam               ?         ?
                      Fingerprint Reader   N/A
                      Brightness Sensor    \-                                           ?         asus_laptop
                      Info LEDs            \-                                           ?         asus_laptop
  ------------------- -------------------- -------------------------------------------- --------- -------------------------------

  : Hardware Summary and Support Status

## [General Configuration]

Wired network doesn\'t work perfectly by default. MTU need to be set to 1492 instead of the default 1500 to work. I don\'t know why. This problem happens with systemresc cd, Ubuntu and every Linux distribution I tried.

[FILE] **`/etc/conf.d/net`Wired Network**

    mtu_eth0="1492"

You have to create the [/etc/init.d/net.eth0] symlink to [/etc/init.d/net.lo] and start it at boot by:

`root `[`#`]`rc-update add net.eth0 default`

You don\'t really need to add it to the default boot level, because net.eth0 is started by hotplug by default. But I noticed that if I use dracut to boot the system, the ip is fine, but the settings in [/etc/conf.d/net] are ignored!

### [Sound]

The audio hardware is supported by the Intel HD Audio drivers:

[KERNEL] **Audio Support**

    Device Drivers  --->
        <*> Sound card support  --->
            <*> Advanced Linux Sound Architecture  --->
                [*] PCI sound devices  --->
                    <*> Intel HD Audio  --->
                        [*]   Build Realtek HD-audio codec support
                            [ ]     Build static quirks for Realtek codecs