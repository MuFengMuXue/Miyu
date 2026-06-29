**Resources**

[[]][Home](https://www.asus.com/us/displays-desktops/mini-pcs/pn-series/mini-pc-pn50/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ryzen "wikipedia:Ryzen")

The Asus PN50 is a Mini PC based on AMD Ryzen mobile processors, This page aims to provide some information for a proper Gentoo setup.

## Contents

-   [[1] [Compiler configuration]](#Compiler_configuration)
-   [[2] [Kernel]](#Kernel)
    -   [[2.1] [Firmware]](#Firmware)
-   [[3] [Hardware]](#Hardware)
    -   [[3.1] [Graphics]](#Graphics)
        -   [[3.1.1] [X11 Driver]](#X11_Driver)
    -   [[3.2] [Network peripherals]](#Network_peripherals)
        -   [[3.2.1] [Ethernet controller]](#Ethernet_controller)
        -   [[3.2.2] [Wi-Fi controller]](#Wi-Fi_controller)
        -   [[3.2.3] [Bluetooth support]](#Bluetooth_support)
    -   [[3.3] [Other peripherals]](#Other_peripherals)
        -   [[3.3.1] [SD Card Reader]](#SD_Card_Reader)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Compiler configuration]

Package [[[app-portage/cpuid2cpuflags]](https://packages.gentoo.org/packages/app-portage/cpuid2cpuflags)[]] can be used to setup correct `CPU_FLAGS_*`^[\[1\]](#cite_note-1)^.

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3

The following command can be used to verify CPU related info^[\[2\]](#cite_note-2)^.

`user `[`$`]`grep -m1 -A3 "vendor_id" /proc/cpuinfo`

    vendor_id    : AuthenticAMD
    cpu family  : 23
    model       : 96
    model name  : AMD Ryzen 5 4500U with Radeon Graphics

The following configuration shall be applied:

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="-march=znver2 -O2 -pipe"
    CFLAGS="$"
    CXXFLAGS="$"

Note on `MAKEOPTS`: there are lots of discussions related to the best way to configure how many parallel make jobs can be launched from Portage^[\[3\]](#cite_note-3)^. An example for Asus PN50, using the following command output:

`user `[`$`]`lscpu`

    Architecture:                    x86_64
    CPU op-mode(s):                  32-bit, 64-bit
    Byte Order:                      Little Endian
    Address sizes:                   48 bits physical, 48 bits virtual
    CPU(s):                          6
    On-line CPU(s) list:             0-5
    Thread(s) per core:              1
    Core(s) per socket:              6
    Socket(s):                       1
    NUMA node(s):                    1
    Vendor ID:                       AuthenticAMD
    CPU family:                      23
    Model:                           96
    Model name:                      AMD Ryzen 5 4500U with Radeon Graphics

would suggest, since 6 logical CPUs are available, 6 physical cores each with 1 thread, to setup `MAKEOPTS` variable to:

[FILE] **`/etc/portage/make.conf`**

    MAKEOPTS="-j6"

However, considering also the fact that higher the value of `MAKEOPTS`, higher the RAM request is (and hence possible usage of swap ) it is suggested to lower the value coming from previous computation, or at least to make such considerations.

## [Kernel]

The information reported on this page have been tested with the following kernel:

-   5.4.80-gentoo-r1-x86_64
-   6.1.67-gentoo-x86_64

\
Note: earlier kernel versions are also supported^[\[4\]](#cite_note-4)^

### [Firmware]

Dedicated firmware files provided by [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] are needed to have full Asus PN50 functionalities.

The following minimum firmware files are suggested:

`user `[`$`]`cat /etc/portage/savedconfig/sys-kernel/linux-firmware`

    # Remove files that shall not be installed from this list.
    amd/amd_sev_fam17h_model3xh.sbin
    amd-ucode/microcode_amd_fam17h.bin
    amdgpu/renoir_dmcub.bin
    amdgpu/renoir_ce.bin
    amdgpu/renoir_mec2.bin
    amdgpu/renoir_sdma.bin
    amdgpu/renoir_gpu_info.bin
    amdgpu/renoir_mec.bin
    amdgpu/renoir_rlc.bin
    amdgpu/renoir_ta.bin
    amdgpu/renoir_pfp.bin
    amdgpu/renoir_asd.bin
    amdgpu/renoir_vcn.bin
    amdgpu/renoir_me.bin
    intel/ibt-20-1-3.ddc
    intel/ibt-20-1-3.sfi
    iwlwifi-cc-a0-50.ucode

After [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] has been emerged, the following files shall be present:

`user `[`$`]`tree /lib/firmware/`

    /lib/firmware/
    ├── amd
    │   └── amd_sev_fam17h_model3xh.sbin
    ├── amd-ucode
    │   └── microcode_amd_fam17h.bin
    ├── amdgpu
    │   ├── renoir_asd.bin
    │   ├── renoir_ce.bin
    │   ├── renoir_dmcub.bin
    │   ├── renoir_gpu_info.bin
    │   ├── renoir_me.bin
    │   ├── renoir_mec.bin
    │   ├── renoir_mec2.bin
    │   ├── renoir_pfp.bin
    │   ├── renoir_rlc.bin
    │   ├── renoir_sdma.bin
    │   ├── renoir_ta.bin
    │   └── renoir_vcn.bin
    ├── intel
    │   ├── ibt-20-1-3.ddc
    │   └── ibt-20-1-3.sfi
    ├── iwlwifi-cc-a0-50.ucode
    ├── regulatory.db
    └── regulatory.db.p7s

In order to properly boot the system, at least `amd`, `amd-ucode` and `amdgpu` firmware files shall be compiled within kernel.

[FILE] **`/usr/src/linux/.config`Kernel configuration for firmware loader**

    #
    # Firmware loader
    #
    CONFIG_FW_LOADER=y
    CONFIG_FW_LOADER_PAGED_BUF=y
    CONFIG_EXTRA_FIRMWARE="amd-ucode/microcode_amd_fam17h.bin amd/amd_sev_fam17h_model3xh.sbin amdgpu/renoir_asd.bin amdgpu/renoir_ce.bin amdgpu/renoir_dmcub.bin amdgpu/renoir_gpu_info.bin amdgpu/renoir_me.bin amdgpu/renoir_mec2.bin amdgpu/renoir_pfp.bin amdgpu/renoir_rlc.bin amdgpu/renoir_sdma.bin amdgpu/renoir_ta.bin amdgpu/renoir_vcn.bin amdgpu/renoir_mec.bin"
    CONFIG_EXTRA_FIRMWARE_DIR="/lib/firmware"
    # CONFIG_FW_LOADER_USER_HELPER is not set
    CONFIG_FW_LOADER_COMPRESS=y
    # end of Firmware loader

\

## [Hardware]

The information reported on this page have been tested on the following hardware:

-   Asus PN50 AMD Ryzen 5 4500U

### [Graphics]

Asus PN50 provides AMD® Radeon Vega (6) Graphics.

`user `[`$`]`lspci | grep -i vga`

     04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir (rev c3)

3D hardware acceleration is supported using Linux firmware code (see Kernel section).

The kernel module to be loaded (or built in kernel) is `amdgpu`. In addition, the experimental HW support shall be enabled on the kernel command line to load `amdgpu`, for example:

[KERNEL] **Kernel command line**

    BOOT_IMAGE=/boot/vmlinuz-5.4.80-gentoo-r1-x86_64 root=UUID=6e1d35b8-5e2a-4bdb-8fc0-2f4b70dee0ac ro ''amdgpu.exp_hw_support=1''

#### [X11 Driver]

The following configuration shall be used:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi

X11 driver [[[x11-drivers/xf86-video-amdgpu]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-amdgpu)[]] shall be emerged.

Package [[[x11-apps/mesa-progs]](https://packages.gentoo.org/packages/x11-apps/mesa-progs)[]] can be used to verify if 3D hardware acceleration has been properly enabled.

`user `[`$`]`glxinfo | grep -i render`

    [...]
    direct rendering: Yes
    [...]
    OpenGL renderer string: AMD RENOIR (DRM 3.35.0, 5.4.80-gentoo-r1-x86_64, LLVM 11.0.0)
    [...]

### [Network peripherals]

#### [Ethernet controller]

Asus PN50 provides a 10/100/1000 Mbps RJ45 Ethernet.

`user `[`$`]`lspci | grep -i ethernet`

    02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 0e)

The kernel module to be loaded (or built in kernel) is `r8169`

#### [Wi-Fi controller]

Asus PN50 provides Intel® Wi-Fi 6 AX200 (802.11ax), 2x2, up to 2.4 Gbps with Bluetooth 5

`user `[`$`]`lspci | grep -i network`

    03:00.0 Network controller: Intel Corporation Wi-Fi 6 AX200 (rev 1a)

The kernel module to be loaded (or built in kernel) is `iwlwifi`.

Dedicated kernel microcode is also needed (see Kernel section)

Package [[[net-wireless/wpa_supplicant]](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)[]] can be emerged to easy handle Wi-Fi device.

#### [Bluetooth support]

Asus PN50 Bluetooth support may be found on USB bus.

`user `[`$`]`lsusb | grep -i bluetooth`

    Bus 005 Device 003: ID 8087:0029 Intel Corp. AX200 Bluetooth

Package [[[net-wireless/blueman]](https://packages.gentoo.org/packages/net-wireless/blueman)[]] can be emerged to easy handle Bluetooth device.

### [Other peripherals]

#### [SD Card Reader]

Asus PN50 comes with SD Card Reader connected on USB bus.

`user `[`$`]`lsusb | grep -i card`

    Bus 004 Device 003: ID 0bda:0129 Realtek Semiconductor Corp. RTS5129 Card Reader Controller

In order to properly use it, the following Kernel modules need to be compiled:

[FILE] **`/usr/src/linux/.config`Kernel configuration for SD Card Reader**

    CONFIG_MMC_BLOCK=m
    CONFIG_MISC_RTSX_USB=m

Once modules have been loaded, an SD Card should be visible when inserted into slot:

`user `[`$`]`lsblks`

    [...]
    mmcblk0     179:0    0 117.8G  0 disk
    └─mmcblk0p1 179:1    0 117.7G  0 part
    [...]

## [See also]

-   [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen") --- a multithreaded, high performance processor manufactured by AMD.
-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.
-   [AMDGPU-PRO](https://wiki.gentoo.org/wiki/AMDGPU-PRO "AMDGPU-PRO") --- the next generation *closed source* graphics component that operates on top of the open source [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") drivers for newer AMD/ATI Radeon graphics cards.
-   [AMD microcode](https://wiki.gentoo.org/wiki/AMD_microcode "AMD microcode") --- describes updating the [microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") for [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") processors.

## [References]

1.  [[[↑](#cite_ref-1)] [[CPU_FLAGS\_\* Wiki Page](https://wiki.gentoo.org/wiki/CPU_FLAGS_* "CPU FLAGS *")]]
2.  [[[↑](#cite_ref-2)] [[Safe CFLAGS Wiki Page](https://wiki.gentoo.org/wiki/Safe_CFLAGS "Safe CFLAGS")]]
3.  [[[↑](#cite_ref-3)] [[MAKEOPTS Wiki Page](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS")]]
4.  [[[↑](#cite_ref-4)] [[Kernel versions on Ryzen Wiki Page](https://wiki.gentoo.org/wiki/Ryzen#Hardware "Ryzen")]]