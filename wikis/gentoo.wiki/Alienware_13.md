**Resources**

[[]][Home](http://www.dell.com/us/p/alienware-13-r2/pd)

## [Hardware]

  ------------------------- ---------- ----------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Category                  Make       Model                                                             Specs
  Processor                 Intel      Core i7-5500U @ 2.4Ghz (Broadwell)                                [Intel Reference documentation.](http://ark.intel.com/products/85214/Intel-Core-i7-5500U-Processor-4M-Cache-up-to-3_00-GHz) Exact model varies based on purchase. CPU soldered to mainboard.
  Mainboard Chipset         Intel      ?
  RAM                       Micron     16KTF1G64HZ-1G6E1                                                 Make and model vary. Amount depends on purchase. This info was recorded for 16G of RAM
  Graphics Card #1          Intel      Intel® HD Graphics 6000                                           [Intel Reference Documentation](http://ark.intel.com/products/84992/Intel-Core-i7-5550U-Processor-4M-Cache-up-to-3_00-GHz).
  Graphics Card #2          nVidia     GeForce GTX 960M                                                  [nVidia reference documentation](http://www.geforce.com/hardware/notebook-gpus/geforce-gtx-960m/specifications). Model varies from 860M-960M. This info was recorded for 960M.
  Hard Disk                 LiteOn     L8T-25G                                                           [LiteOn Reference Documentation](http://www.liteonssd.com/datasheet/LiteOn.L9G.US.lores.pdf). Model will vary on what was ordered.
  Panel Display             SHP        ?                                                                 3200 x 1800 (QHD+) (touch screen) Non-touch has alternate specs. See [Dell Specifications](http://downloads.dell.com/manuals/all-products/esuprt_laptop/esuprt_alienware_laptops/alienware-13_reference%20guide_en-us.pdf).
  Sound Card                Intel      Wildcat Point-LP High Definition Audio Controller (Broadwell-U)
  Ethernet                  Qualcomm   Atheros Killer E220x                                              [Killer E2200 Network literature](http://www.killernetworking.com/products/e2200)
  Wireless Ethernet         Qualcomm   Atheros QCA6174 802.11ac
  USB 3.0 Host Controller   Intel      Wildcat Point-LP USB xHCI Controller
  USB 2.0 Host Controller   Intel      Wildcat Point-LP USB EHCI Controller
  ------------------------- ---------- ----------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Broadwell-U Host Bridge -OPI [8086:1604] (rev 09)
    00:02.0 VGA compatible controller [0300]: Intel Corporation Broadwell-U Integrated Graphics [8086:1616] (rev 09)
    00:03.0 Audio device [0403]: Intel Corporation Broadwell-U Audio Controller [8086:160c] (rev 09)
    00:04.0 Signal processing controller [1180]: Intel Corporation Broadwell-U Camarillo Device [8086:1603] (rev 09)
    00:14.0 USB controller [0c03]: Intel Corporation Wildcat Point-LP USB xHCI Controller [8086:9cb1] (rev 03)
    00:16.0 Communication controller [0780]: Intel Corporation Wildcat Point-LP MEI Controller #1 [8086:9cba] (rev 03)
    00:1b.0 Audio device [0403]: Intel Corporation Wildcat Point-LP High Definition Audio Controller [8086:9ca0] (rev 03)
    00:1c.0 PCI bridge [0604]: Intel Corporation Wildcat Point-LP PCI Express Root Port #3 [8086:9c94] (rev e3)
    00:1c.3 PCI bridge [0604]: Intel Corporation Wildcat Point-LP PCI Express Root Port #4 [8086:9c96] (rev e3)
    00:1c.4 PCI bridge [0604]: Intel Corporation Wildcat Point-LP PCI Express Root Port #5 [8086:9c98] (rev e3)
    00:1d.0 USB controller [0c03]: Intel Corporation Wildcat Point-LP USB EHCI Controller [8086:9ca6] (rev 03)
    00:1f.0 ISA bridge [0601]: Intel Corporation Wildcat Point-LP LPC Controller [8086:9cc3] (rev 03)
    00:1f.2 SATA controller [0106]: Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode] [8086:9c83] (rev 03)
    00:1f.3 SMBus [0c05]: Intel Corporation Wildcat Point-LP SMBus Controller [8086:9ca2] (rev 03)
    01:00.0 Network controller [0280]: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter [168c:003e] (rev 20)
    02:00.0 Ethernet controller [0200]: Qualcomm Atheros Killer E220x Gigabit Ethernet Controller [1969:e091] (rev 10)
    03:00.0 3D controller [0302]: NVIDIA Corporation GM107M [GeForce GTX 960M] [10de:139b] (rev ff)

`root `[`#`]`lsusb `

    Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 002 Device 005: ID 0cf3:e300 Atheros Communications, Inc.
    Bus 002 Device 004: ID 187c:0527 Alienware Corporation
    Bus 002 Device 003: ID 0c45:6708 Microdia
    Bus 002 Device 002: ID 04f3:0441 Elan Microelectronics Corp.
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 8087:8001 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

`root `[`#`]`lshw -class CPU`

      *-cpu
           description: CPU
           product: Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz
           vendor: Intel Corp.
           physical id: 39
           bus info: cpu@0
           version: Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz
           serial: NULL
           slot: SOCKET 0
           size: 2492MHz
           capacity: 2492MHz
           width: 64 bits
           clock: 100MHz
           capabilities: x86-64 fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch ida arat epb pln pts dtherm intel_pt tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap xsaveopt cpufreq
           configuration: cores=2 enabledcores=2 threads=4

### [When installing GRUB 2 on EFI]

This system uses EFI vars which will cause GRUB 2 to fail silently with \`grub-install\`. Grub will appear to have completed successfully, but there will be no EFI partition entry(efibootmgr can verify).

To fix this, use the EFI vars(under Configuration) steps from [Gentoo\'s Wiki for Efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr"):

When the system is in EFI mode, run the following command to check for the existence of [efivarfs](https://wiki.gentoo.org/wiki/Filesystem#Disk_filesystems "Filesystem"):

\

`root `[`#`]`mount | grep efivars`

    efivarfs on /sys/firmware/efi/efivars type efivarfs (ro,relatime)

\
It is mounted ro through the [sysfs] init script), so it needs to be remounted rw manually using the following command:

\

`root `[`#`]`mount -o remount,rw -t efivarfs efivarfs /sys/firmware/efi/efivars`

\
After the above rw remount of the efivarfs, then you will be able to run \'grub-install\' and have it successfully install the EFI partition entry.