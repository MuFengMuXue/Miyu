**Resources**

[[]][Home](https://www.asrock.com/mb/AMD/C70M1)

[![](/images/thumb/b/bd/Pavlix-asrock-c70m1.jpg/300px-Pavlix-asrock-c70m1.jpg)](https://wiki.gentoo.org/wiki/File:Pavlix-asrock-c70m1.jpg)

[](https://wiki.gentoo.org/wiki/File:Pavlix-asrock-c70m1.jpg "Enlarge")

Asrock C70M1 with four hard drives and a power supply in a box.

Asrock C70M1 is a low-cost small form factor motherboard with integrated AMD Dual-Core Ontario C-70 APU and four SATA connectors which makes it suitable for small storage or server use.

## Contents

-   [[1] [Hardware notes]](#Hardware_notes)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Installation notes]](#Installation_notes)
    -   [[3.1] [Compilation speed]](#Compilation_speed)
        -   [[3.1.1] [LVM]](#LVM)
-   [[4] [Resources]](#Resources)

## [Hardware notes]

When initramfs fails and upon enter recovery shell, USB keyboard won\'t work and you\'ll have to use PS/2. On the other hand, USB keyboard can be used for choosing the boot media and entering UEFI setup as well as working with the setup.

## [Configuration]

[CODE] **/etc/portage/make.conf**

    CHOST="x86_64-pc-linux-gnu"
    CFLAGS="-march=native -O2 -pipe"
    CXXFLAGS="$"
    CPU_FLAGS_X86="mmx mmxext popcnt sse sse2 sse3 sse4a ssse3"
    MAKEOPTS="-j3"

## [Installation notes]

### [Compilation speed]

The CPU is rather slow so it may be worth avoiding some steps that make the installation unnecessarily time consuming.

#### [LVM]

Unless it is required, disabling the `thin` USE on [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]] may save some extensive compilation times:

`root `[`#`]`echo sys-fs/lvm2 -thin >> /etc/portage/package.use/lvm2`

## [Resources]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 14h Processor Root Complex
    00:01.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Wrestler [Radeon HD 7290]
    00:04.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Family 14h Processor Root Port
    00:11.0 SATA controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 SATA Controller [AHCI mode] (rev 40)
    00:12.0 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
    00:12.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
    00:13.0 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
    00:13.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 SMBus Controller (rev 42)
    00:14.1 IDE interface: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 IDE Controller (rev 40)
    00:14.2 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 Azalia (Intel HDA) (rev 40)
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 LPC host controller (rev 40)
    00:14.4 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] SBx00 PCI to PCI Bridge (rev 40)
    00:14.5 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI2 Controller
    00:15.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] SB700/SB800/SB900 PCI to PCI bridge (PCIE port 0)
    00:15.1 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] SB700/SB800/SB900 PCI to PCI bridge (PCIE port 1)
    00:16.0 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB OHCI0 Controller
    00:16.2 USB controller: Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 USB EHCI Controller
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 12h/14h Processor Function 0 (rev 43)
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 12h/14h Processor Function 1
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 12h/14h Processor Function 2
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 12h/14h Processor Function 3
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 12h/14h Processor Function 4
    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 12h/14h Processor Function 6
    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 12h/14h Processor Function 5
    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 12h/14h Processor Function 7
    04:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)

`user `[`$`]`gcc -march=native -Q --help=target`

    The following options are target specific:
      -m128bit-long-double                  [disabled]
      -m32                                  [disabled]
      -m3dnow                               [disabled]
      -m3dnowa                              [disabled]
      -m64                                  [enabled]
      -m80387                               [enabled]
      -m8bit-idiv                           [disabled]
      -m96bit-long-double                   [enabled]
      -mabi=                                sysv
      -mabm                                 [enabled]
      -maccumulate-outgoing-args            [disabled]
      -maddress-mode=                       short
      -madx                                 [disabled]
      -maes                                 [disabled]
      -malign-double                        [disabled]
      -malign-functions=                    0
      -malign-jumps=                        0
      -malign-loops=                        0
      -malign-stringops                     [enabled]
      -mandroid                             [disabled]
      -march=                               btver1
      -masm=                                att
      -mavx                                 [disabled]
      -mavx2                                [disabled]
      -mavx256-split-unaligned-load         [disabled]
      -mavx256-split-unaligned-store        [disabled]
      -mbionic                              [disabled]
      -mbmi                                 [disabled]
      -mbmi2                                [disabled]
      -mbranch-cost=                        0
      -mcld                                 [disabled]
      -mcmodel=                             32
      -mcpu=
      -mcrc32                               [disabled]
      -mcx16                                [enabled]
      -mdispatch-scheduler                  [disabled]
      -mf16c                                [disabled]
      -mfancy-math-387                      [enabled]
      -mfentry                              [enabled]
      -mfma                                 [disabled]
      -mfma4                                [disabled]
      -mforce-drap                          [disabled]
      -mfp-ret-in-387                       [enabled]
      -mfpmath=                             387
      -mfsgsbase                            [disabled]
      -mfused-madd
      -mfxsr                                [enabled]
      -mglibc                               [enabled]
      -mhard-float                          [enabled]
      -mhle                                 [disabled]
      -mieee-fp                             [enabled]
      -mincoming-stack-boundary=            0
      -minline-all-stringops                [disabled]
      -minline-stringops-dynamically        [disabled]
      -mintel-syntax
      -mlarge-data-threshold=               0x10000
      -mlong-double-64                      [disabled]
      -mlong-double-80                      [enabled]
      -mlwp                                 [disabled]
      -mlzcnt                               [enabled]
      -mmmx                                 [disabled]
      -mmovbe                               [disabled]
      -mms-bitfields                        [disabled]
      -mno-align-stringops                  [disabled]
      -mno-fancy-math-387                   [disabled]
      -mno-push-args                        [disabled]
      -mno-red-zone                         [disabled]
      -mno-sse4                             [enabled]
      -momit-leaf-frame-pointer             [disabled]
      -mpc32                                [disabled]
      -mpc64                                [disabled]
      -mpc80                                [disabled]
      -mpclmul                              [disabled]
      -mpopcnt                              [enabled]
      -mprefer-avx128                       [disabled]
      -mpreferred-stack-boundary=           0
      -mprfchw                              [enabled]
      -mpush-args                           [enabled]
      -mrdrnd                               [disabled]
      -mrdseed                              [disabled]
      -mrecip                               [disabled]
      -mrecip=
      -mred-zone                            [enabled]
      -mregparm=                            0
      -mrtd                                 [disabled]
      -mrtm                                 [disabled]
      -msahf                                [enabled]
      -msoft-float                          [disabled]
      -msse                                 [disabled]
      -msse2                                [disabled]
      -msse2avx                             [disabled]
      -msse3                                [disabled]
      -msse4                                [disabled]
      -msse4.1                              [disabled]
      -msse4.2                              [disabled]
      -msse4a                               [disabled]
      -msse5
      -msseregparm                          [disabled]
      -mssse3                               [disabled]
      -mstack-arg-probe                     [disabled]
      -mstackrealign                        [enabled]
      -mstringop-strategy=                  [default]
      -mtbm                                 [disabled]
      -mtls-dialect=                        gnu
      -mtls-direct-seg-refs                 [enabled]
      -mtune=                               btver1
      -muclibc                              [disabled]
      -mveclibabi=                          [default]
      -mvect8-ret-in-mem                    [disabled]
      -mvzeroupper                          [disabled]
      -mx32                                 [disabled]
      -mxop                                 [disabled]
      -mxsave                               [disabled]
      -mxsaveopt                            [disabled]

      Known assembler dialects (for use with the -masm-dialect= option):
        att intel

      Known ABIs (for use with the -mabi= option):
        ms sysv

      Known code models (for use with the -mcmodel= option):
        32 kernel large medium small

      Valid arguments to -mfpmath=:
        387 387+sse 387,sse both sse sse+387 sse,387

      Known vectorization library ABIs (for use with the -mveclibabi= option):
        acml svml

      Known address mode (for use with the -maddress-mode= option):
        long short

      Valid arguments to -mstringop-strategy=:
        byte_loop libcall loop rep_4byte rep_8byte rep_byte unrolled_loop

      Known TLS dialects (for use with the -mtls-dialect= option):
        gnu gnu2

`user `[`$`]`cpuinfo2cpuflags-x86`

    CPU_FLAGS_X86="mmx mmxext popcnt sse sse2 sse3 sse4a ssse3"

`user `[`$`]`cat /proc/cpuinfo`

    processor   : 0
    vendor_id   : AuthenticAMD
    cpu family  : 20
    model       : 2
    model name  : AMD C-70 APU with Radeon(tm) HD Graphics
    stepping    : 0
    microcode   : 0x500010d
    cpu MHz     : 1000.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 2
    core id     : 0
    cpu cores   : 2
    apicid      : 0
    initial apicid  : 0
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 6
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc extd_apicid aperfmperf pni monitor ssse3 cx16 popcnt lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch ibs skinit wdt arat cpb hw_pstate npt lbrv svm_lock nrip_save pausefilter vmmcall
    bugs        : fxsave_leak
    bogomips    : 2000.09
    TLB size    : 1024 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management: ts ttp tm stc 100mhzsteps hwpstate cpb

    processor   : 1
    vendor_id   : AuthenticAMD
    cpu family  : 20
    model       : 2
    model name  : AMD C-70 APU with Radeon(tm) HD Graphics
    stepping    : 0
    microcode   : 0x500010d
    cpu MHz     : 1000.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 2
    core id     : 1
    cpu cores   : 2
    apicid      : 1
    initial apicid  : 1
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 6
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc extd_apicid aperfmperf pni monitor ssse3 cx16 popcnt lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch ibs skinit wdt arat cpb hw_pstate npt lbrv svm_lock nrip_save pausefilter vmmcall
    bugs        : fxsave_leak
    bogomips    : 2000.09
    TLB size    : 1024 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management: ts ttp tm stc 100mhzsteps hwpstate cpb