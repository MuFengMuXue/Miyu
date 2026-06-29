**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-w-series-laptops/thinkpad-w540)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_W540/ThinkPad_W540_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_W540)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/t540p_w540_w541_hmm_en_sp40a26003_03.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/t540p_w540_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad W series](https://en.wikipedia.org/wiki/ThinkPad_W_series "wikipedia:ThinkPad W series")

This article describes installation and configuration instructions for the Lenovo ThinkPad W540. Although several different configurations for the model exist, these instructions should work for all of them. Note that the model documented does not contain a WAN card, and other sources should be explored for configuration of the hardware.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Video Card Setup with NVIDIA Binary Drivers]](#Video_Card_Setup_with_NVIDIA_Binary_Drivers)
        -   [[3.1.1] [Prime Synchronization]](#Prime_Synchronization)
    -   [[3.2] [Thinkfan]](#Thinkfan)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  -------------------- ------------------------------------------------------------------------------------------------------------------ ------------- ------------------------ ------------------- ---------------- -------
  Device               Make/model                                                                                                         Status        Vendor ID / Product ID   Kernel driver(s)    Kernel version   Notes
  CPU                  Intel® Core™ i7-4600M Processor (4M Cache, up to 3.60 GHz)                                                         Works         N/A                      N/A                 4.12.5
  GPU                  NVIDIA® Quadro® K1100M with Optimus                                                                                Works         N/A                      nvidia_drm nvidia   4.12.5
  Display              15.6\" FHD (1920 x 1080), anti-glare, 300 nits, 500:1 contrast ratio                                               Works         N/A                      N/A                 4.12.5
  RAM                  16GB PC3-12800 1600MHz DDR3L, non-parity, dual-channel capable DDRM                                                Works         N/A                      N/A                 4.12.5
  Battery              9-cell Li-Ion battery - 57++ (99.9Wh)                                                                              Works         N/A                      N/A                 4.12.5
  Card Reader          O2 Micro, Inc. SD/MMC Card Reader Controller (4-in-1 card reader (MMC, SD, SDHC, SDXC), supports UHS-II SD card)   Works         N/A                      sdhci-pci           4.12.5
  Ethernet             Intel Corporation Ethernet Connection I217-LM                                                                      Works         N/A                      e1000e              4.12.5
  Wi-Fi                Intel Corporation Wireless 7260                                                                                    Works         N/A                      iwlwifi             4.12.5
  Bluetooth            Intel Corporation Wireless 7260                                                                                    Not tested    N/A                      N/A                 4.12.5
  Webcam               Integrated 720p HD Camera                                                                                          Not tested    N/A                      N/A                 4.12.5
  Fingerprint Reader   Validity Sensors, Inc. Fingerprint Reader                                                                          Not tested    138a:0017                N/A                 4.12.5
  -------------------- ------------------------------------------------------------------------------------------------------------------ ------------- ------------------------ ------------------- ---------------- -------

### [Accessories]

  ---------- ---------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- -------
  Device     Make/model                                                 Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  WAN Card   Ericsson N5321 Mobile Broadband HSPA+                      Not tested    N/A                      N/A                N/A
  WAN Card   Sierra Wireless EM7355 (mutually exclusive with M.2 SSD)   Not tested    N/A                      N/A                N/A
  ---------- ---------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- -------

`root `[`#`]`lspci -k`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor DRAM Controller (rev 06)
        Subsystem: Lenovo Xeon E3-1200 v3/4th Gen Core Processor DRAM Controller
    libkmod: kmod_config_parse: /etc/modprobe.d/nvidia.conf line 5: ignoring bad line starting with 'nvidia'
    libkmod: kmod_config_parse: /etc/modprobe.d/nvidia.conf line 6: ignoring bad line starting with 'nvidia_modeset'
    libkmod: kmod_config_parse: /etc/modprobe.d/nvidia.conf line 7: ignoring bad line starting with 'nvidia_uvm'
    libkmod: kmod_config_parse: /etc/modprobe.d/nvidia.conf line 8: ignoring bad line starting with 'nvidia_drm'
    00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor PCI Express x16 Controller (rev 06)
        Kernel driver in use: pcieport
    00:02.0 VGA compatible controller: Intel Corporation 4th Gen Core Processor Integrated Graphics Controller (rev 06)
        Subsystem: Lenovo 4th Gen Core Processor Integrated Graphics Controller
        Kernel driver in use: i915
    00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller (rev 06)
        Subsystem: Lenovo Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller
        Kernel driver in use: snd_hda_intel
    00:14.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB xHCI (rev 04)
        Subsystem: Lenovo 8 Series/C220 Series Chipset Family USB xHCI
        Kernel driver in use: xhci_hcd
    00:16.0 Communication controller: Intel Corporation 8 Series/C220 Series Chipset Family MEI Controller #1 (rev 04)
        Subsystem: Lenovo 8 Series/C220 Series Chipset Family MEI Controller
    00:19.0 Ethernet controller: Intel Corporation Ethernet Connection I217-LM (rev 04)
        Subsystem: Lenovo Ethernet Connection I217-LM
        Kernel driver in use: e1000e
    00:1a.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #2 (rev 04)
        Subsystem: Lenovo 8 Series/C220 Series Chipset Family USB EHCI
        Kernel driver in use: ehci-pci
    00:1b.0 Audio device: Intel Corporation 8 Series/C220 Series Chipset High Definition Audio Controller (rev 04)
        Subsystem: Lenovo 8 Series/C220 Series Chipset High Definition Audio Controller
        Kernel driver in use: snd_hda_intel
    00:1c.0 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #1 (rev d4)
        Kernel driver in use: pcieport
    00:1c.1 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #2 (rev d4)
        Kernel driver in use: pcieport
    00:1c.2 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #3 (rev d4)
        Kernel driver in use: pcieport
    00:1c.4 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #5 (rev d4)
        Kernel driver in use: pcieport
    00:1d.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #1 (rev 04)
        Subsystem: Lenovo 8 Series/C220 Series Chipset Family USB EHCI
        Kernel driver in use: ehci-pci
    00:1f.0 ISA bridge: Intel Corporation QM87 Express LPC Controller (rev 04)
        Subsystem: Lenovo QM87 Express LPC Controller
    00:1f.2 SATA controller: Intel Corporation 8 Series/C220 Series Chipset Family 6-port SATA Controller 1 [AHCI mode] (rev 04)
        Subsystem: Lenovo 8 Series/C220 Series Chipset Family 6-port SATA Controller 1 [AHCI mode]
        Kernel driver in use: ahci
    00:1f.3 SMBus: Intel Corporation 8 Series/C220 Series Chipset Family SMBus Controller (rev 04)
        Subsystem: Lenovo 8 Series/C220 Series Chipset Family SMBus Controller
        Kernel driver in use: i801_smbus
    01:00.0 VGA compatible controller: NVIDIA Corporation GK107GLM [Quadro K1100M] (rev a1)
        Subsystem: Lenovo GK107GLM [Quadro K1100M]
        Kernel driver in use: nvidia
        Kernel modules: nvidia_drm, nvidia
    02:00.0 SD Host controller: O2 Micro, Inc. SD/MMC Card Reader Controller (rev 01)
        Subsystem: Lenovo SD/MMC Card Reader Controller
        Kernel driver in use: sdhci-pci
    03:00.0 Network controller: Intel Corporation Wireless 7260 (rev 83)\
        Subsystem: Intel Corporation Dual Band Wireless-AC 7260
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi

`root `[`#`]`lsusb -tv`

    /:  Bus 04.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/15p, 480M
        |__ Port 5: Dev 2, If 0, Class=Chip/SmartCard, Driver=, 12M
        |__ Port 6: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 6: Dev 3, If 1, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 6: Dev 3, If 2, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 7: Dev 4, If 0, Class=Vendor Specific Class, Driver=, 12M
        |__ Port 12: Dev 6, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 12: Dev 6, If 1, Class=Video, Driver=uvcvideo, 480M
    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/3p, 480M
        |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/8p, 480M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/3p, 480M
        |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/6p, 480M

`root `[`#`]`lsusb`

    Bus 002 Device 002: ID 8087:8000 Intel Corp.
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 8087:8008 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 004: ID 138a:0017 Validity Sensors, Inc. Fingerprint Reader
    Bus 003 Device 003: ID 046d:c52b Logitech, Inc. Unifying Receiver
    Bus 003 Device 002: ID 058f:9540 Alcor Micro Corp. AU9540 Smartcard Reader
    Bus 003 Device 006: ID 5986:026a Acer, Inc
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

### [Firmware]

All of the required firmware, including the wifi driver should be available in the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

** Note**\
At the time this article was written, the kernel version used was 4.12.5.

[KERNEL] **Enable support for these hardware drivers**

    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  --->
        <*> AC Adapter
        <*> Battery
        <*> Button
        <*> Video
        <*> Fan
        <*> Dock
    CPU Frequency scaling  --->
        <*> CPU Frequency Transition Statistics
        Default CPUFreq governor (performance)
        <*> 'performance' governor
        <*> 'powersave' governor
        [*] Intel P state control
    [*] Networking support  --->
      <*> Bluetooth subsystem support  --->
        Bluetooth device drivers  --->
          <*> HCI USB driver
      <*> Wireless  --->
        <*> cfg80211 - wireless configuration API -->
            <*> cfg80211 - wireless extensions compatability
        <*> Generic IEEE 802.11 Networking Stack (mac80211)
      <*> RF switch subsystem support
    Device Drivers  --->
      <*> Serial ATA and Parallel ATA drivers  --->
        <*> AHCI SATA support
      [*] Network device support  --->
        [*] Ethernet driver support  --->
          [*] Intel devices
            <*> Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support
        [*] Wireless LAN  --->
          <M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
          <M> Intel Wireless WiFi MVM Firmware support
      <*> I2C support  --->
        I2C Hardware Bus support  --->
          <*> Intel 82801 (ICH/PCH)
      <*> Hardware Monitoring support  --->
        <*> Intel Core/Core2/Atom temperature sensor
      Multifunction device drivers  --->
        <*> Intel SCH LPC
        <*> Realtek PCI-E card reader
      <*> Multimedia support  --->
        [*] Media USB Adapters  --->
          <*> USB Video Class (UVC)
      Graphics support  --->
        <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) -->
            [*] Enable legacy fbdev support for the modesettting intel driver
        <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
          [*] Enable modesetting on intel by default
          [*] Enable alpha quality support for new intel hardware by default
        Console display driver support  --->
          <*> Framebuffer Console support
        Support for Framebuffer Devices -->
          <*> EFI based Framebuffer support
      <*> Sound card support  --->
        <*> Advanced Linux Sound Architecture  --->
          [*] PCI sound devices  --->
            [*] Intel/SiS/nVidia/AMD Controller
            [*] Intel/SiS/nVidia/AMD Modem
          <*> Intel HD Audio  --->
              [*] Build HDMI/DisplayPort HD-audio codec support
      [*] USB support  --->
        <*> xHCI HCD (USB 3.0) support
        <*> EHCI HCD (USB 2.0) support
      <*> MMC/SD/SDIO card support
        <*> Realtek PCI-E SD/MMC Card Interface Driver
      [*] X86 Platform Specific Device Drivers  --->
        <*> ThinkPad ACPI Laptop Extras
      [*] IOMMU Hardware Support  --->
        [*] Support for Intel IOMMU using DMA Remapping Devices

## [Configuration]

### [Video Card Setup with NVIDIA Binary Drivers]

The laptop has a dual GPU setup operating on NVIDIA Optimus. The integrated intel card is what is attached to the laptop screen, and the discrete Quadro card is what interfaces with the outside HDMI and DisplayPort. It is possible to run the laptop without the discrete graphics card for better power usage, however doing so will sacrifice the ability to output to HDMI or Display Port. To do so, simply compile only for the intel driver, and X-server should pick everything up by default without any extra configuration.

The better option is to use the discrete card. Note that it\'s recommended to use the binary NVIDIA driver in place of the open source nouveau driver, as the binary driver offers the best performance, and features Prime Synchronization, which eliminates screen tearing (a prominent problem on the laptop as it uses hybrid graphics). The caveat is that the discrete card has no ability to turn off on the binary driver, thus offering worse battery performance compared to the nouveau driver.

To configure the system to use the binary driver, add to the VIDEO_CARDS field in make.conf:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* nvidia intel i965

Update the system, which should automatically install the NVIDIA driver package.

`root `[`#`]`emerge --ask --changed-use --deep @world`

The X.org server configuration should look like this. This will enable PRIME on the device, allowing the machine to use both its discrete card for rendering, and intel card for displaying to laptop screen.

[FILE] **`/etc/X11/xorg.conf`**

    Section "ServerLayout"
        Identifier "layout"
        Screen 0 "nvidia"
        Inactive "intel"
    EndSection

    Section "Device"
        Identifier "nvidia"
        Driver "nvidia"
        BusID "PCI:1:0:0"
    EndSection

    Section "Screen"
        Identifier "nvidia"
        Device "nvidia"
        Option "AllowEmptyInitialConfiguration"
        #Option "UseDisplayDevice" "none"
    EndSection

    Section "Device"
        Identifier "intel"
        Driver "modesetting"
        BusID "PCI:0:2:0"
        #Option "AccelMethod"  "sna"
        #Option "TearFree" "True"
        #Option "Tiling" "True"
        #Option "SwapbuffersWait" "True"
    EndSection

    Section "Screen"
        Identifier "intel"
        Device "intel"
    EndSection

#### [Prime Synchronization]

To eliminate any screen tearing, PRIME Synchronization will need to be enabled. To do this, some NVIDIA kernel modules have to be loaded in at startup. Add the following entries to the nvidia.conf file in the modprobe.d folder:

[FILE] **`/etc/modprobe.d/nvidia.conf`**

    nvidia
    nvidia_modeset
    nvidia_uvm
    nvidia_drm

    options nvidia_drm modeset=1

Also, add the following lines to the user\'s [\~/.xinitrc] when using startx or display manager start script:

[FILE] **`~/.xinitrc`**

    xrandr --setprovideroutputsource modesetting NVIDIA-0
    xrandr --auto
    xrandr --dpi=96 # Optional, if the text is too large or small by default when started

After a restart, verify that prime is working and functioning by running xrandr, which should produce the following outputː

`user `[`$`]`xrandr --listproviders`

    Providers: number : 2
    Provider 0: id: 0x316 cap: 0x1, Source Output crtcs: 4 outputs: 2 associated providers: 1 name:NVIDIA-0
    Provider 1: id: 0x48 cap: 0x2, Sink Output crtcs: 3 outputs: 6 associated providers: 1 name:modesetting

Alternatively, verify that Prime Synchronization is turned on by looking at the Prime Synchronization field under the eDP-1-1 field:

`user `[`$`]`xrandr --props`

    eDP-1-1 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 344mm x 194mm
        EDID:
            00ffffffffffff000daec01500000000
            04170104952213780246359e57579427
            14505400000001010101010101010101
            010101010101383b802c71383a405a3c
            690058c210000018000000fe004e3135
            364847452d4541310a20000000fe0043
            4d4e0a202020202020202020000000fe
            004e3135364847452d4541310a2000ab
        PRIME Synchronization: 1
            supported: 0, 1
        scaling mode: Full aspect
            supported: None, Full, Center, Full aspect
        Broadcast RGB: Automatic
            supported: Automatic, Full, Limited 16:235
        audio: auto
            supported: force-dvi, off, auto, on
        link-status: Good
            supported: Good, Bad

### [Thinkfan]

Install Thinkfan:

`root `[`#`]`emerge --ask thinkfan`

When installation has been completed, find the sensors location:

`user `[`$`]`find /sys/devices -type f -name "temp*_input"`

Take note of the output. This will be the hwmon location for thinkfan configuration. Now edit the thinkfan.conf using a text editor.

Example config for thinkfan:

[FILE] **`/etc/thinkfan.conf`**

    ######################################################################
    ## thinkfan 0.9 example config file
    ## ================================
    ##
    ## ATTENTION: There is only very basic sanity checking on the configuration.
    ## That means you can set your temperature limits as insane as you like. You
    ## can do anything stupid, e.g. turn off your fan when your CPU reaches 70°C.
    ##
    ## That's why this program is called thinkfan: You gotta think for yourself.
    ##
    #######################################################################
    ##
    ## This file shows how to use sensor-specific temperature limits.
    ## First of all, you need to specify temperature inputs. On a ThinkPad, you can
    ## just use:
    ##
    tp_thermal /proc/acpi/ibm/thermal  # provides us with 16 temperature inputs

    ##
    ## On other systems, you have to specify a file in /sys/class/hwmon for each
    ## sensor you want to use. They are numbered in their order of appearance.
    ## For example:
    #
    # hwmon /sys/class/hwmon5/temp2_input           #1
    # hwmon /sys/class/hwmon0/device/temp3_input    #2
    #
    ## If you want to read temperatures directly from the hard disk, thinkfan needs
    ## to be compiled with -DUSE_ATASMART. Then you can do:
    #
    # atasmart /dev/sda                             #3
    # ...
    #
    ## You can have as many temperature inputs as you like. You should at get the
    ## temperature from the CPU, the GPU and the hard disk.
    #

    #
    ## Next we specify the fan we want to use. On a ThinkPad, this is:
    #
    tp_fan /proc/acpi/ibm/fan

    #
    ## On anything other than a ThinkPad you'll probably use some PWM control file
    ## in /sys/class/hwmon. Remember that fan levels range from 0 to 255 and that
    ## they're just a number, not including the word "level" as seen below.
    ## A sysfs fan would be specified like this:
    #
    # pwm_fan /sys/class/hwmon/hwmon2/device/pwm1
    #
    ## But remember you can only have one fan.

    #
    ## Then you need to specify the temperature limits for each of the sensors.
    ## A dot means that the corresponding sensor should be ignored. The length of the
    ## UPPER and LOWER limits must be the same as the number of temperatures. In this
    ## example, /proc/acpi/ibm/thermal contains 16 sensors (on older thinkpads,
    ## there may be only 8), some of which are unused (hence the dots).
    ## A sysfs temperature input always contains only one sensor, so if you specify
    ## 5 sysfs files above, the length of your limits must be 5, too.
    #
    ## I've come up with these preliminary settings for my ThinkPad T61p. They probably
    ## don't make sense for anything else, so you most definitely have to work
    ## something out for yourself.
    #












Add below line in [/etc/modprobe.d/thinkfan.conf]:

    options thinkpad_acpi fan_control=1

Now run thinkfan:

`root `[`#`]`thinkfan -q`

or via init.d

`root `[`#`]`rc-service thinkfan start`

## [See also]

-   [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") --- The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package contains the *proprietary* graphics driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.
-   [NVIDIA/Optimus](https://wiki.gentoo.org/wiki/NVIDIA/Optimus "NVIDIA/Optimus") --- a proprietary technology that seamlessly switches between two GPUs.

## [External resources]

-   [http://www.thinkwiki.org/wiki/Category:W540](http://www.thinkwiki.org/wiki/Category:W540)
-   [https://wiki.archlinux.org/index.php/PRIME](https://wiki.archlinux.org/index.php/PRIME)
-   [https://wiki.archlinux.org/index.php/NVIDIA_Optimus](https://wiki.archlinux.org/index.php/NVIDIA_Optimus)
-   [https://wiki.archlinux.org/index.php/NVIDIA](https://wiki.archlinux.org/index.php/NVIDIA)
-   [https://www.thinkwiki.org/wiki/How_to_control_fan_speed](https://www.thinkwiki.org/wiki/How_to_control_fan_speed)
-   [https://github.com/vmatare/thinkfan](https://github.com/vmatare/thinkfan)