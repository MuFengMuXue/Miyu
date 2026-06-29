**Resources**

[[]][Product Information](https://www.hp.com/nl-nl/shop/products/laptops/hp-omnibook-ultra-flip-laptop-14-fh0645nd-b5up5ea-abh)

[[]]\[None Specifications\]

[[]][Article Title](https://en.wikipedia.org/wiki/HP_OmniBook#List_of_models "wikipedia:HP OmniBook")

HP Omnibook Ultra Flip 14-fhxxxxnl is a series of 2-in-1 laptop devices released by Hewlett-Packard in 2024. They are compact, light, reasonably powerful and elegant. They are produced with Intel chipsets and CPU, providing good support on Linux.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
    -   [[1.3] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage settings]](#Portage_settings)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Audio]](#Audio)
    -   [[4.2] [Bluetooth]](#Bluetooth)
    -   [[4.3] [Fingerprint Reader]](#Fingerprint_Reader)
-   [[5] [References]](#References)

## [Hardware]

Full list of hardware also available [Linux Hardware](https://linux-hardware.org/?probe=e84d432fdc)

### [Standard]

  ----------------------- -------------------------------------------------------------- --------- ------------------------ --------------------------- ---------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --
  Device                  Make/model                                                     Status    Vendor ID / Product ID   Kernel driver(s)            Kernel version                     Notes
  CPU                     Intel® Core™ Ultra 7 258V                                      Works     intel-6-189-1            N/A                         6.12.21                            This CPU rocks!
  Wireless                Intel® Wi-Fi 7 BE201 (2x2)/Wi-Fi 6E AX231 160MHz               Works     8086:2723                iwlwifi                     N/A                                Requires firmware from [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]
  Bluetooth               Intel® Wi-Fi 7 BE201 (2x2)/Wi-Fi 6E AX231 160MHz               Work      8086:a876                btintel_pcie                N/A                                Make sure to have firmware sys-kernel/linux-firmware-20250410. Reported [here](https://bbs.archlinux.org/viewtopic.php?id=304221) as well
  Quanta Computer, Inc.   HP 9MP Camera                                                  Works     0408:546e                uvcvideo                    N/A                                Tested with V4l tester. Make sure to install V4L. You can test with v4l2-ctl
  Touch screen            ELAN2513:00                                                    Works     04F3:4301                hid_multitouch              unknown, tested working in 5.10+   Multi-touch works
  Audio                   Lunar Lake-M HD Audio Controller                               Works     8086:a828                snd_hda_intel, snd_sof_pc   unknown, tested working in 5.10+
  Fingerprint reader      Synaptics, Inc                                                 Works     06cb:0174                N/A                         N/A                                Support in libfprint available from version [1.94.9](https://gitlab.freedesktop.org/libfprint/libfprint/-/releases/v1.94.9)
  Video card              Intel® Arc™ graphics card \[Intel Arc Graphics 130V / 140V\]   Borked    8086:64a0                N/A                         N/A                                Need to test it yet
  ----------------------- -------------------------------------------------------------- --------- ------------------------ --------------------------- ---------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --

### [Accessories]

(Optional section. Describe any accessories that may be possible in this section. Anything from external plug-and-play LCD screens to computer docks.)

  -------- ------------------------------- ------------- ------------------------ ------------------ ---------------- ---------------------------
  Device   Make/model                      Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Pen      HP 700 Rechargeable Multi Pen   Not tested    N/A                      N/A                N/A              Waiting for the delivery.
  -------- ------------------------------- ------------- ------------------------ ------------------ ---------------- ---------------------------

### [Detailed information]

`root `[`#`]`uname -r`

    6.12.21-gentoo-dist

`root `[`#`]`lscpu`

    Architecture:             x86_64
      CPU op-mode(s):         32-bit, 64-bit
      Address sizes:          42 bits physical, 48 bits virtual
      Byte Order:             Little Endian
    CPU(s):                   8
      On-line CPU(s) list:    0-7
    Vendor ID:                GenuineIntel
      Model name:             Intel(R) Core(TM) Ultra 7 258V
        CPU family:           6
        Model:                189
        Thread(s) per core:   1
        Core(s) per socket:   8
        Socket(s):            1
        Stepping:             1
        CPU(s) scaling MHz:   20%
        CPU max MHz:          4800.0000
        CPU min MHz:          400.0000
        BogoMIPS:             6607.00
        Flags:                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_goo
                              d nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_
                              timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb intel_ppin ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep
                              bmi2 erms invpcid rdt_a rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni lam wbnoinvd dtherm ida arat pln pts hwp hwp_notify hw
                              p_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_detect movdiri movdir64b fsrm md_clear serialize pconfig arch_lbr ibt flush_l1d arch_capabilit
                              ies
    Virtualization features:
      Virtualization:         VT-x
    Caches (sum of all):
      L1d:                    320 KiB (8 instances)
      L1i:                    512 KiB (8 instances)
      L2:                     14 MiB (5 instances)
      L3:                     12 MiB (1 instance)
    NUMA:
      NUMA node(s):           1
      NUMA node0 CPU(s):      0-7
    Vulnerabilities:
      Gather data sampling:   Not affected
      Itlb multihit:          Not affected
      L1tf:                   Not affected
      Mds:                    Not affected
      Meltdown:               Not affected
      Mmio stale data:        Not affected
      Reg file data sampling: Not affected
      Retbleed:               Not affected
      Spec rstack overflow:   Not affected
      Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
      Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
      Srbds:                  Not affected
      Tsx async abort:        Not affected

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Device [8086:6400] (rev 04)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
    00:02.0 VGA compatible controller [0300]: Intel Corporation Lunar Lake [Intel Arc Graphics 130V / 140V] [8086:64a0] (rev 04)
            DeviceName: Onboard IGD
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: xe
            Kernel modules: xe
    00:04.0 Signal processing controller [1180]: Intel Corporation Device [8086:641d] (rev 04)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: proc_thermal_pci
            Kernel modules: processor_thermal_device_pci
    00:07.0 PCI bridge [0604]: Intel Corporation Lunar Lake-M Thunderbolt 4 PCI Express Root Port #0 [8086:a84e] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: pcieport
    00:07.2 PCI bridge [0604]: Intel Corporation Lunar Lake-M Thunderbolt 4 PCI Express Root Port #2 [8086:a860] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: pcieport
    00:0a.0 Signal processing controller [1180]: Intel Corporation Device [8086:647d] (rev 04)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: intel_vsec
            Kernel modules: intel_vsec
    00:0b.0 Processing accelerators [1200]: Intel Corporation Lunar Lake NPU [8086:643e] (rev 04)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: intel_vpu
            Kernel modules: intel_vpu
    00:0d.0 USB controller [0c03]: Intel Corporation Lunar Lake-M Thunderbolt 4 USB Controller [8086:a831] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: xhci_hcd
    00:0d.2 USB controller [0c03]: Intel Corporation Lunar Lake-M Thunderbolt 4 NHI #0 [8086:a833] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: thunderbolt
            Kernel modules: thunderbolt
    00:0d.3 USB controller [0c03]: Intel Corporation Lunar Lake-M Thunderbolt 4 NHI #1 [8086:a834] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: thunderbolt
            Kernel modules: thunderbolt
    00:12.0 Serial controller [0700]: Intel Corporation Lunar Lake-M Integrated Sensor Hub [8086:a845] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: intel_ish_ipc
            Kernel modules: intel_ish_ipc
    00:13.0 Communication controller [0780]: Intel Corporation Device [8086:a862] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
    00:14.0 USB controller [0c03]: Intel Corporation Lunar Lake-M USB 3.2 Gen 2x1 xHCI Host Controller [8086:a87d] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: xhci_hcd
    00:14.2 RAM memory [0500]: Intel Corporation Device [8086:a87f] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
    00:14.3 Network controller [0280]: Intel Corporation Device [8086:a840] (rev 10)
            Subsystem: Intel Corporation Device [8086:00e4]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi
    00:14.7 Bluetooth [0d11]: Intel Corporation Device [8086:a876] (rev 10)
            Subsystem: Intel Corporation Device [8086:000e]
            Kernel driver in use: btintel_pcie
            Kernel modules: btintel_pcie
    00:15.0 Serial bus controller [0c80]: Intel Corporation Lunar Lake-M Serial IO I2C Controller #0 [8086:a878] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: intel-lpss
    00:15.2 Serial bus controller [0c80]: Intel Corporation Lunar Lake-M Serial IO I2C Controller #2 [8086:a87a] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: intel-lpss
    00:16.0 Communication controller [0780]: Intel Corporation Device [8086:a870] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: mei_me
            Kernel modules: mei_me
    00:19.0 Serial bus controller [0c80]: Intel Corporation Device [8086:a850] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: intel-lpss
    00:19.1 Serial bus controller [0c80]: Intel Corporation Device [8086:a851] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: intel-lpss
    00:1c.0 PCI bridge [0604]: Intel Corporation Lunar Lake-M PCI Express Root Port #5 [8086:a83c] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Device [8086:a807] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
    00:1f.3 Multimedia audio controller [0401]: Intel Corporation Lunar Lake-M HD Audio Controller [8086:a828] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: sof-audio-pci-intel-lnl
            Kernel modules: snd_hda_intel, snd_sof_pci_intel_lnl
    00:1f.4 SMBus [0c05]: Intel Corporation Lunar Lake-M SMbus Controller [8086:a822] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
    00:1f.5 Serial bus controller [0c80]: Intel Corporation Lunar Lake-M SPI Controller [8086:a823] (rev 10)
            Subsystem: Hewlett-Packard Company Device [103c:8cde]
            Kernel driver in use: intel-spi
            Kernel modules: spi_intel_pci
    55:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller PM9A1/PM9A3/980PRO [144d:a80a]
            Subsystem: Samsung Electronics Co Ltd SSD 980 PRO [144d:a801]
            Kernel driver in use: nvme
            Kernel modules: nvme

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 002: ID 06cb:0174 Synaptics, Inc.
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 004 Device 002: ID 0408:546e Quanta Computer, Inc. HP 9MP Camera

`root `[`#`]`lsusb -vt`

    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/3p, 20000M/x2
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/8p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 005: Dev 002, If 0, Class=Vendor Specific Class, Driver=[none], 12M
            ID 06cb:0174 Synaptics, Inc.
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 20000M/x2
        ID 1d6b:0003 Linux Foundation 3.0 root hub
        |__ Port 002: Dev 002, If 0, Class=Video, Driver=uvcvideo, 5000M
            ID 0408:546e Quanta Computer, Inc.
        |__ Port 002: Dev 002, If 1, Class=Video, Driver=uvcvideo, 5000M
            ID 0408:546e Quanta Computer, Inc.
        |__ Port 002: Dev 002, If 2, Class=Video, Driver=uvcvideo, 5000M
            ID 0408:546e Quanta Computer, Inc.
        |__ Port 002: Dev 002, If 3, Class=Video, Driver=uvcvideo, 5000M
            ID 0408:546e Quanta Computer, Inc.
        |__ Port 002: Dev 002, If 4, Class=Human Interface Device, Driver=usbhid, 5000M
            ID 0408:546e Quanta Computer, Inc.
        |__ Port 002: Dev 002, If 5, Class=Application Specific Interface, Driver=[none], 5000M
            ID 0408:546e Quanta Computer, Inc.

## [Installation]

Nothing more than what is written in the AMD64 Handbook. The only caveat is that you need to disable a couple of things in the EUFI system in order to boot from USB. You need to disable \`BIOS sure start\` e \`Secure boot\`

### [Firmware]

(Optional section.)

### [Kernel]

I used a dist kernel. So, no extra options for me.

[KERNEL] **Enable support for these hardware drivers**

    Write menuconfig instructions here.

### [Emerge]

TO make sure you have tools to run some checks, you need to emerge several packages:

\

`root `[`#`]`emerge --ask app-misc/wayland-utils`

`root `[`#`]`emerge --ask x11-apps/mesa-progs`

## [Configuration]

### [Portage settings]

[FILE] **`/etc/portage/make.conf`Suggested Portage settings**

    # These settings were set by the catalyst build script that automatically
    # built this stage.
    # Please consult /usr/share/portage/config/make.conf.example for a more
    # detailed example.
    COMMON_FLAGS="-O2 -pipe -march=arrowlake-s -fno-semantic-interposition "
    CFLAGS="$"
    CXXFLAGS="$"
    FCFLAGS="$"
    FFLAGS="$"
    MAKEOPTS="-j4 -l5"

    # NOTE: This stage was built with the bindist USE flag enabled

    # This sets the language of build output to English.
    # Please keep this setting intact when reporting bugs.
    LC_MESSAGES=C.utf8

    # Use binhost when possible
    # Appending getbinpkg to the list of values within the FEATURES variable
    FEATURES="$ getbinpkg"
    # Require signatures
    FEATURES="$ binpkg-request-signature"

    # License
    # Overrides the profile's ACCEPT_LICENSE default value
    ACCEPT_LICENSE="-* @FREE @BINARY-REDISTRIBUTABLE"
    USE="X a52 aac acl acpi activities alsa amd64 bluetooth branding bzip2 cairo cdda cdr cet crypt cups dbus declarative dri dts dvd dvdr encode exif flac gdbm gif gpm gtk gui iconv icu ipv6 jpeg kde kwallet lcms libnotify libtirpc mad mng mp3 mp4 mpeg multilib ncurses networkmanager nls ogg opengl openmp pam pango pcre pdf pipewire plasma png policykit ppds pulseaudio qml qt5 qt6 readline screencast sdl seccomp semantic-desktop sound sound-server spell ssl startup-notification svg systemd test-rust tiff truetype udev udisks unicode upower usb v4l vorbis vulkan wayland widgets wxwidgets x264 xattr xcb xft xml xv xvid zlib modules-sign secureboot dist-kernel"

    # Optionally, to use custom signing keys.
    MODULES_SIGN_KEY="/usr/src/certs/kernel_key.pem"
    MODULES_SIGN_CERT="/usr/src/certs/kernel_key.pem" # Only required if the MODULES_SIGN_KEY does not also contain the certificate.
    MODULES_SIGN_HASH="sha512" # Defaults to sha512.
    # Optionally, to boot with secureboot enabled, may be the same or different signing key.
    SECUREBOOT_SIGN_KEY="/usr/src/certs/kernel_key.pem"
    SECUREBOOT_SIGN_CERT="/usr/src/certs/kernel_key.pem"

    # Python
    PYTHON_TARGETS="python3_13"
    # GRUB
    GRUB_PLATFORMS="efi-64"

    # L10N
    L10N="it en-GB"

\

## [Troubleshooting]

Audio, bluetooth and fingerprint do not work out of the box.

### [Audio]

Audio does not work. Pipewire seems to only see a dummy devices. I did the following. First, I installed sof. See handbook [here](https://wiki.gentoo.org/wiki/Handbook:AMD64/Blocks/Firmware "Handbook:AMD64/Blocks/Firmware")

Then, I noticed that the devices were loaded but still no audio. The logs were telling me the following:

    wireplumber[2626]: wp-internal-comp-loader: Loading profile 'main'
    wireplumber[2626]: spa.bluez5: BlueZ system service is not available
    wireplumber[2626]: wp-device: SPA handle 'api.v4l2.enum.udev' could not be loaded; is it installed?
    wireplumber[2626]: s-monitors-v4l2: PipeWire's V4L2 SPA plugin is missing or broken. Some camera types may not be supported.
    wireplumber[2626]: wp-device: SPA handle 'api.libcamera.enum.manager' could not be loaded; is it installed?
    wireplumber[2626]: s-monitors-libcamera: PipeWire's libcamera SPA plugin is missing or broken. Some camera types may not be supported.
    systemd[1008]: Reload requested from client PID 2668 ('systemctl') (unit app-org.kde.konsole@88d14af7c1dd415e826b030cde16c7cc.service)...
    systemd[1008]: Reloading...
    systemd[1008]: Reloading finished in 203 ms.

So, I tried to add V4L to USE flags. There are records on [reddit of this](https://www.reddit.com/r/Gentoo/comments/124z0ra/wireplumber_problems_while_running/) Re-emerging pipewire with v4l use flag enabled fixed the issue and sound is working now.

`root `[`#`]`echo "<media-video/pipewire v4l" >> /etc/portage/package.use/system`

`root `[`#`]`emerge --ask media-video/pipewire`

-1.4.2:0/0.4::gentoo USE=\"X bluetooth dbus extra ffmpeg gstreamer readline sound-server ssl systemd v4l

### [Bluetooth]

Bluetooth did not work.

    $ journalctl -b | grep Bluetooth
    May 06 22:32:47 elea systemd[1]: Reached target Bluetooth Support.
    May 06 22:32:47 elea kernel: Bluetooth: hci0: Device moved to D0 in 4367 usecs
    May 06 22:32:47 elea kernel: Bluetooth: hci0: dsbr: enable: 0x01 value: 0x0b
    May 06 22:32:47 elea kernel: Bluetooth: hci0: Failed to load Intel firmware file intel/ibt-0190-0291-pci.sfi (-2)
    May 06 22:32:47 elea kernel: Bluetooth: hci0: Failed to read MSFT supported features (-56)
    May 06 22:39:13 elea systemd[1]: Stopped target Bluetooth Support.

One needs to use a firmware newer than linux-firmware 20250311.b69d4b74-3 Being discussed on reddit^[\[1\]](#cite_note-1)^ and Arch community^[\[2\]](#cite_note-2)^

`root `[`#`]`echo "<=sys-kernel/linux-firmware-20250410 **" >> /etc/portage/package.accept_keywords/system`

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

\

### [Fingerprint Reader]

Fingerprint reader did not work out of the box. The device is supported by libfprint, but only in release 1.94.9. On Gentoo, there is an [open bug](https://bugs.gentoo.org/955926) with a pull request for the version 1.94.9 that we hope to merge soon.

Once that is available, you can simple add it to your keywords and emerge it.

`root `[`#`]`echo "<=sys-auth/libfprint-1.94.9 **" >> /etc/portage/package.accept_keywords/system`

`root `[`#`]`emerge --ask sys-auth/libfprint`

## [References]

1.  [[[↑](#cite_ref-1)] [[Reddit discussion on Intel BT firmware](https://www.reddit.com/r/archlinux/comments/1ja6y69/it_looks_like_linuxfirmware_20250311b69d4b742_has/), Full discussion.]]
2.  [[[↑](#cite_ref-2)] [[Arch forum text](https://bbs.archlinux.org/viewtopic.php?id=304221)]]