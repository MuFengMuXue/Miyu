The Beelink GTR7 (GTR7 Pro) models were released in 2023. Mini PCs are based on the Ryzen 7000 mobile platform. Combining efficient cooling, fast storage, and versatile connectivity, this compact mini PC making it an enticing choice for various tasks and gaming. The differences between them are essentially only in overclocking the processor. The GTR7 and GTR7 Pro mini PCs are powered by the AMD Ryzen 7 7840HS (5.1 GHz) and AMD Ryzen 9 7940HS (5.2 GHz) processors, respectively. **Below we will talk about the GTR7 PRO model**.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [BIOS]](#BIOS)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [make.conf]](#make.conf)
    -   [[2.2] [Firmware]](#Firmware)
    -   [[2.3] [Kernel]](#Kernel)
    -   [[2.4] [Emerge]](#Emerge)
    -   [[2.5] [GPU software support notes]](#GPU_software_support_notes)
-   [[3] [Perfomance]](#Perfomance)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Random reboots]](#Random_reboots)
    -   [[4.2] [Periodic loss of I/O devices]](#Periodic_loss_of_I.2FO_devices)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Hardware]

### [Standard]

  -------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------------- ---------------- --------------------------------------------------------------- --
  Device                           Make/model                                                                                                                            Status        Kernel driver(s)          Kernel version   Notes
  CPU                              AMD Ryzen 9 7940HS                                                                                                                    Works         N/A                       6.1.67           Zen 4
  GPU                              Advanced Micro Devices, Inc. \[AMD/ATI\] Phoenix1 (rev c1)                                                                            Works         amdgpu                    6.1.67           Integrated Ryzen 7000 graphics
  PCI Bridge                       Advanced Micro Devices, Inc. \[AMD\] Family 19h USB4/Thunderbolt PCIe tunnel                                                          Works         pcieport                  6.1.67
  SMBus                            Advanced Micro Devices, Inc. \[AMD\] FCH SMBus Controller (rev 71)                                                                    Works         piix4_smbus, sp5100_tco   6.1.67
  Ethernet controller              Realtek Semiconductor Co., Ltd. RTL8125 2.5GbE Controller (rev 05)                                                                    Works         r8169                     6.1.67
  Network controller               Intel Corporation Wi-Fi 6 AX200 (rev 1a)                                                                                              Works         mt7921e                   6.1.67           Bluetooth works after adding the firmware files listed below.
  Non-Volatile memory controller   Micron/Crucial Technology P2 \[Nick P2\] / P3 / P3 Plus NVMe PCIe SSD (DRAM-less) (rev 01)                                            Works         nvme                      6.1.67
  Audio device                     Advanced Micro Devices, Inc. \[AMD/ATI\] Renoir Radeon High Definition Audio Controller, \[AMD\] Family 17h/19h HD Audio Controller   Works         snd_hda_intel             6.1.67
  Multimedia controller            Advanced Micro Devices, Inc. \[AMD\] ACP/ACP3X/ACP6x Audio Coprocessor (rev 63)                                                       Works         snd_rn_pci_acp3x          6.1.67
  Encryption controller            Advanced Micro Devices, Inc. \[AMD\] Family 19h (Model 74h) CCP/PSP 3.0 Device                                                        Not tested    ccp                       6.1.67
  USB controller                   Advanced Micro Devices, Inc. \[AMD\] ASM2142/ASM3142 USB 3.1 Host Controller                                                          Works         xhci_hcd                  6.1.67
  Fingerprint reader                                                                                                                                                     Not tested                              6.1.67
  -------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------------- ---------------- --------------------------------------------------------------- --

`root `[`#`]`lscpu`

    Architecture:            x86_64
      CPU op-mode(s):        32-bit, 64-bit
      Address sizes:         48 bits physical, 48 bits virtual
      Byte Order:            Little Endian
    CPU(s):                  16
      On-line CPU(s) list:   0-15
    Vendor ID:               AuthenticAMD
      BIOS Vendor ID:        Advanced Micro Devices, Inc.
      Model name:            AMD Ryzen 9 7940HS w/ Radeon 780M Graphics
        BIOS Model name:     AMD Ryzen 9 7940HS w/ Radeon 780M Graphics      Unknown CPU @ 4.0GHz
        BIOS CPU family:     107
        CPU family:          25
        Model:               116
        Thread(s) per core:  2
        Core(s) per socket:  8
        Socket(s):           1
        Stepping:            1
        CPU(s) scaling MHz:  17%
        CPU max MHz:         6228.0000
        CPU min MHz:         400.0000
        BogoMIPS:            7984.88
        Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm con
                             stant_tsc rep_good amd_lbr_v2 nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popc
                             nt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_co
                             re perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba perfmon_v2 ibrs ibpb stibp ibrs_enhanced vmmcall fsgsbase bmi1 avx2 smep
                             bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsa
                             ves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_s
                             cale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2
                              gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid overflow_recov succor smca flush_l1d
    Virtualization features:
      Virtualization:        AMD-V
    Caches (sum of all):
      L1d:                   256 KiB (8 instances)
      L1i:                   256 KiB (8 instances)
      L2:                    8 MiB (8 instances)
      L3:                    16 MiB (1 instance)
    NUMA:
      NUMA node(s):          1
      NUMA node0 CPU(s):     0-15
    Vulnerabilities:
      Gather data sampling:  Not affected
      Itlb multihit:         Not affected
      L1tf:                  Not affected
      Mds:                   Not affected
      Meltdown:              Not affected
      Mmio stale data:       Not affected
      Retbleed:              Not affected
      Spec rstack overflow:  Vulnerable: No microcode
      Spec store bypass:     Mitigation; Speculative Store Bypass disabled via prctl
      Spectre v1:            Mitigation; usercopy/swapgs barriers and __user pointer sanitization
      Spectre v2:            Mitigation; Enhanced / Automatic IBRS, IBPB conditional, STIBP always-on, RSB filling, PBRSB-eIBRS Not affected
      Srbds:                 Not affected
      Tsx async abort:       Not affected

### [BIOS]

[Official Beelink Drivers and Software Download](https://dr.bee-link.cn/?dir=uploads%2FGTR%2FGTR+7840+GTR+7940%2F)

For the regular and PRO versions, the BIOS firmware is identical. Latest known version [v39](https://disk.yandex.ru/d/_wu8jUflwpgChQ) (prev. [v38](https://disk.yandex.ru/d/tHTM2Bq6um53yQ), [v37](https://disk.yandex.ru/d/MTSvcugX8qydAg), [v35](https://disk.yandex.ru/d/bQPoCSq837yriQ)). [Instructions for flashing BIOS](https://disk.yandex.ru/i/BJVI5UOFbYornQ)

## [Installation]

### [make.conf]

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="-march=znver4 -O2 -pipe"
    RUSTFLAGS="-C target-cpu=znver4"
    MAKEOPTS="-j8"

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx avx2 avx512f avx512dq avx512cd avx512bw avx512vl avx512vbmi f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi

[FILE] **`/etc/portage/package.use/00grub`**

    */* GRUB_PLATFORMS: efi-64

### [Firmware]

For wifi, bluetooth, integrated graphics, and microcode updates add the following firmware files:

[FILE] **`/usr/src/linux/.config`**

    CONFIG_EXTRA_FIRMWARE="amd-ucode/microcode_amd_fam19h.bin iwlwifi-cc-a0-77.ucode"

### [Kernel]

The Ryzen 7 7840HS and Ryzen 9 7940HS processors have full support for kernel versions 6.4 and higher. Recommended kernel version 6.5+ due to the *new AMD P-State EPP Driver*.

[KERNEL] **menuconfig**

    [*] 64-bit kernel
        Processor type and features  --->
            [*] AMD ACPI2Platform devices support
            Processor family (AMD Zen4)
        Device Drivers  --->
            [*] PCI support  --->
                [*] PCI Express Port Bus support
            NVME Support  --->
                <*> NVM Express block device
            [*] Network device support  --->
                [*] Wireless LAN --->
                    [*] Intel devices
                    <M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                    <M> Intel Wireless WiFi DVM Firmware support
                    <M> Intel Wireless WiFi MVM Firmware support
                [*] Ethernet driver support  --->
                    [*] Realtek devices
                    <*> Realtek 8169/8168/8101/8125 ethernet support
            Graphics support  --->
                < > ATI Radeon
                <M> AMD GPU
                    ACP (Audio CoProcessor) Configuration  --->
                        [*] Enable AMD Audio CoProcessor IP support
                    Display Engine Configuration  --->
                        [*] AMD DC - Enable new display engine
                [*] HSA kernel driver for AMD GPU devices
            <*> Sound card support  --->
                <*> Advanced Linux Sound Architecture  --->
                    HD-Audio  --->
                       <*> Build Realtek HD-audio codec support
            [*] USB support  --->
                <*> xHCI HCD (USB 3.0) support
                <*> EHCI HCD (USB 2.0) support
                <*> USB Mass Storage support
                <*> USB Type-C Support  --->
                    <*> USB Type-C Port Controller Manager
                    <*> Type-C Port Controller Interface driver
                    <*> USB Type-C Connector System Software Interface driver
            [*] IOMMU Hardware Support  --->
                [*]   AMD IOMMU support

### [Emerge]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware media-libs/mesa x11-apps/mesa-progs dev-util/vulkan-tools`

### [GPU software support notes]

`root `[`#`]`vulkaninfo --summary`

    ==========
    VULKANINFO
    ==========

    Vulkan Instance Version: 1.3.268

    Instance Extensions: count = 20
    -------------------------------
    VK_EXT_acquire_drm_display             : extension revision 1
    VK_EXT_debug_report                    : extension revision 10
    VK_EXT_debug_utils                     : extension revision 2
    VK_EXT_direct_mode_display             : extension revision 1
    VK_EXT_display_surface_counter         : extension revision 1
    VK_EXT_surface_maintenance1            : extension revision 1
    VK_EXT_swapchain_colorspace            : extension revision 4
    VK_KHR_device_group_creation           : extension revision 1
    VK_KHR_display                         : extension revision 23
    VK_KHR_external_fence_capabilities     : extension revision 1
    VK_KHR_external_memory_capabilities    : extension revision 1
    VK_KHR_external_semaphore_capabilities : extension revision 1
    VK_KHR_get_display_properties2         : extension revision 1
    VK_KHR_get_physical_device_properties2 : extension revision 2
    VK_KHR_get_surface_capabilities2       : extension revision 1
    VK_KHR_portability_enumeration         : extension revision 1
    VK_KHR_surface                         : extension revision 25
    VK_KHR_surface_protected_capabilities  : extension revision 1
    VK_KHR_wayland_surface                 : extension revision 6
    VK_LUNARG_direct_driver_loading        : extension revision 1

    Instance Layers: count = 1
    --------------------------
    VK_LAYER_MESA_device_select Linux device selection layer 1.3.211  version 1

    Devices:
    ========
    GPU0:
        apiVersion         = 1.3.267
        driverVersion      = 23.3.3
        vendorID           = 0x1002
        deviceID           = 0x15bf
        deviceType         = PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU
        deviceName         = AMD Radeon Graphics (RADV GFX1103_R1)
        driverID           = DRIVER_ID_MESA_RADV
        driverName         = radv
        driverInfo         = Mesa 23.3.3
        conformanceVersion = 1.3.0.0
        deviceUUID         = 00000000-c800-0000-0000-000000000000
        driverUUID         = 414d442d-4d45-5341-2d44-525600000000

`root `[`#`]`vainfo`

    Trying display: wayland
    libva info: VA-API version 1.20.0
    libva info: Trying to open /usr/lib64/va/drivers/radeonsi_drv_video.so
    libva info: Found init function __vaDriverInit_1_20
    libva info: va_openDriver() returns 0
    vainfo: VA-API version: 1.20 (libva 2.20.1)
    vainfo: Driver version: Mesa Gallium driver 23.3.3 for AMD Radeon Graphics (radeonsi, gfx1103_r1, LLVM 17.0.6, DRM 3.56, 6.7.0-gentoo)
    vainfo: Supported profile and entrypoints
          VAProfileH264ConstrainedBaseline: VAEntrypointVLD
          VAProfileH264ConstrainedBaseline: VAEntrypointEncSlice
          VAProfileH264Main               : VAEntrypointVLD
          VAProfileH264Main               : VAEntrypointEncSlice
          VAProfileH264High               : VAEntrypointVLD
          VAProfileH264High               : VAEntrypointEncSlice
          VAProfileHEVCMain               : VAEntrypointVLD
          VAProfileHEVCMain               : VAEntrypointEncSlice
          VAProfileHEVCMain10             : VAEntrypointVLD
          VAProfileHEVCMain10             : VAEntrypointEncSlice
          VAProfileJPEGBaseline           : VAEntrypointVLD
          VAProfileVP9Profile0            : VAEntrypointVLD
          VAProfileVP9Profile2            : VAEntrypointVLD
          VAProfileAV1Profile0            : VAEntrypointVLD
          VAProfileAV1Profile0            : VAEntrypointEncSlice
          VAProfileNone                   : VAEntrypointVideoProc

## [Perfomance]

Average package installation time:

`root `[`#`]`emerge -avq gcc firefox python libreoffice`

    [ebuild   R   ] sys-devel/gcc-13.2.1_p20231216  USE="(cxx) fortran lto nls openmp pgo (pie) sanitize ssp -ada (-cet) (-custom-cflags) -d -debug -default-stack-clash-protection -default-znow -doc (-fixed-point) -go -graphite -hardened (-ieee-long-double) -jit (-libssp) -modula2 (-multilib) -objc -objc++ -objc-gc (-pch) -systemtap -test -valgrind -vanilla -vtv -zstd"
    [ebuild   R   ] dev-lang/python-3.11.7  USE="bluetooth ensurepip gdbm ncurses pgo readline sqlite ssl -build -debug -examples -libedit -test -tk -valgrind -verify-sig"
    [ebuild   R   ] www-client/firefox-121.0.1  USE="clang dbus gmp-autoupdate hwaccel jumbo-build lto pgo pulseaudio system-av1 system-harfbuzz system-icu system-jpeg system-libevent system-libvpx system-webp telemetry wayland wifi -X -debug -eme-free -geckodriver -hardened -jack -libproxy -openh264 -screencast (-selinux) -sndio -system-png (-system-python-libs) (-valgrind)" L10N="ru -ach -af -an -ar -ast -az -be -bg -bn -br -bs -ca -ca-valencia -cak -cs -cy -da -de -dsb -el -en-CA -en-GB -eo -es-AR -es-CL -es-ES -es-MX -et -eu -fa -ff -fi -fr -fur -fy -ga -gd -gl -gn -gu -he -hi -hr -hsb -hu -hy -ia -id -is -it -ja -ka -kab -kk -km -kn -ko -lij -lt -lv -mk -mr -ms -my -nb -ne -nl -nn -oc -pa -pl -pt-BR -pt-PT -rm -ro -sc -sco -si -sk -sl -son -sq -sr -sv -szl -ta -te -th -tl -tr -trs -uk -ur -uz -vi -xh -zh-CN -zh-TW"
    [ebuild   R   ] app-office/libreoffice-7.5.9.2  USE="bluetooth branding cups dbus gtk postgres vulkan -accessibility -base -clang -coinmp -custom-cflags -debug -eds -firebird -googledrive -gstreamer -java -kde -ldap -mariadb -odk -pdfimport -test -valgrind" LIBREOFFICE_EXTENSIONS="-nlpsolver -scripting-beanshell -scripting-javascript -wiki-publisher" PYTHON_SINGLE_TARGET="python3_11 -python3_10 -python3_12"

`root `[`#`]`qlop -c gcc firefox python libreoffice`

    app-office/libreoffice: 26′26″ average for 1 merge
    dev-lang/python: 2′49″ average for 2 merges
    sys-devel/gcc: 33′51″ average for 1 merge
    www-client/firefox: 21′23″ average for 3 merges

## [Troubleshooting]

### [Random reboots]

In the first revision (v1.0) of the motherboard, a hardware error was made that caused the device to reboot when trying to switch to energy-efficient mode (C6 state). In newer revisions (v1.1) of the motherboard, this problem could be fixed. In revision v3.0 the problem is definitely fixed. A software solution to the problem is to disable ACPI: BIOS:

1.  Advanced\>ACPI Settings: Disable "Enable ACPI Auto Config" and set both options below that appear to Disable and Suspend Disable
2.  Advanced\> AMD CBS\>NBIO Common Options\>GFX Configuration: Set iGPU to UMA_Specified. Set UMA Frame Buffer Size to a static size. You choose what you want or what you can afford to give to the GPU for memory. Suggested 2GB or 4GB. (This supposedly helps with keeping both DIMM's awake).

### [][Periodic loss of I/O devices]

Periodic loss of screen and freezing of input/output devices. The cause and solution have not yet been found.

## [See also]

-   [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") --- a semiconductor company. AMD is best known for producing CPUs based on [x86 intruction set](https://en.wikipedia.org/wiki/x86 "wikipedia:x86"), motherboard chipsets and their own line of GPUs.
-   [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen") --- a multithreaded, high performance processor manufactured by AMD.
-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.
-   [VAAPI](https://wiki.gentoo.org/wiki/VAAPI "VAAPI") --- provides access to graphics hardware (GPU) acceleration for video processing.
-   [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") --- a family of *open source* graphics drivers for *older* AMD/ATI Radeon graphics cards.

## [References]