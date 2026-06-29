[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://www.asus.com/Motherboards/TUF-GAMING-B550M-PLUS/overview)

This article details the ASUS TUF GAMING B550M-PLUS motherboard; providing Linux kernel configuration hints and workarounds. The motherboard has an B550 chipset and AM4 CPU socket compatible with Ryzen CPUs.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
-   [[3] [Performance and CPU temperature]](#Performance_and_CPU_temperature)
    -   [[3.1] [Known hardware issues]](#Known_hardware_issues)
        -   [[3.1.1] [Ethernet timeouts]](#Ethernet_timeouts)
        -   [[3.1.2] [Bridge interface is not working with kvm]](#Bridge_interface_is_not_working_with_kvm)

## [Hardware]

### [Standard]

  ------------------------- ----------------------------------------------------------------------------------------- -------- ----------- ---------------------------- ---------------- -----------------------------------------------------------------------------------
  Device                    Make/model                                                                                Status   Bus ID      Kernel driver(s)             Kernel version   Notes
  CPU                       AMD Ryzen 7 3800X 8-Core Processor                                                        Works    N/A         N/A                          5.8.6-gentoo     This CPU rocks!
  Audio device (on board)   Starship/Matisse HD Audio Controller                                                      Works    09:00.4     snd_hda_codec_realtek        5.8.6-gentoo
  USB controller            USB controller: Advanced Micro Devices, Inc. \[AMD\] Device 43ee                          Works    09:00.3     ohci-pci                     5.8.6-gentoo
  SATA controller           SATA controller: Advanced Micro Devices, Inc. \[AMD\] Device 43eb                         Works    02:00.1     ahci                         5.8.6-gentoo
  NVMe disk                 Non-Volatile memory controller: Kingston Technology Company, Inc. Device 2263 (rev 03)    Works    01:00.0     nvme                         5.8.6-gentoo     KINGSTON A2000 SA2000M8/500G 500ГБ, M.2 2280, PCI-E x4, NVMe on M2_1
  Ethernet controller       Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8125 2.5GbE Controller (rev 04)   Works    06:00.0     r8169                        5.9.6-gentoo     Kernel 5.9.6 and \>=sys-kernel/linux-firmware-20201022-r2 for RTL8125(B) support.
  Video card                NVIDIA Corporation TU116 \[GeForce GTX 1660 SUPER\]                                       Works    10de:0185   x11-drivers/nvidia-drivers   5.8.6-gentoo
  Memory                    CRUCIAL BL16G32C16U4B.M16FE                                                               Works                                             5.8.6-gentoo     2 modules
  ------------------------- ----------------------------------------------------------------------------------------- -------- ----------- ---------------------------- ---------------- -----------------------------------------------------------------------------------

## [Installation]

Network is not working in standard Gentoo image. I was using [USB WiFi TP-LINK Archer T1U](https://www.tp-link.com/us/home-networking/usb-adapter/archer-t1u/) during installation:

[CODE] **dmesg**

    [ 2881.069381] usb 1-7.2: new high-speed USB device number 7 using xhci_hcd
    [ 2881.198045] usb 1-7.2: New USB device found, idVendor=2357, idProduct=0105, bcdDevice= 1.00
    [ 2881.198049] usb 1-7.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [ 2881.198050] usb 1-7.2: Product: WiFi
    [ 2881.198052] usb 1-7.2: Manufacturer: MediaTek
    [ 2881.198053] usb 1-7.2: SerialNumber: 1.0
    [ 2881.257391] cfg80211: Loading compiled-in X.509 certificates for regulatory database
    [ 2881.259086] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
    [ 2881.348204] usb 1-7.2: reset high-speed USB device number 7 using xhci_hcd
    [ 2881.478048] mt76x0u 1-7.2:1.0: ASIC revision: 76100002 MAC revision: 76502000
    [ 2885.026042] mt76x0u 1-7.2:1.0: EEPROM ver:02 fae:01
    [ 2885.283132] ieee80211 phy0: Selected rate control algorithm 'minstrel_ht'
    [ 2885.283604] usbcore: registered new interface driver mt76x0u

### [Kernel]

The kernel configuration described in

-   [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen")
-   [Gigabyte_X570-UD](https://wiki.gentoo.org/wiki/Gigabyte_X570-UD "Gigabyte X570-UD") is more specific

You should except from [Gigabyte_X570-UD](https://wiki.gentoo.org/wiki/Gigabyte_X570-UD "Gigabyte X570-UD") this items:

-   Ethernet driver section
-   Do not enable \`AMD Secure Memory Encryption (SME) support\` because with this option kernel doesn\'t boot

[KERNEL]

    Processor type and features  --->
        [ ] AMD Secure Memory Encryption (SME) support
        [ ]   Activate AMD Secure Memory Encryption (SME) by default

\

[KERNEL] **Network requires Kernel 5.9.8**

    Device Drivers  --->
      [*] Network device support  --->
         [*]   Ethernet driver support  --->
            [*]   Realtek devices
               <*>     Realtek 8169/8168/8101/8125 ethernet support

## [Performance and CPU temperature]

The [my kernel config](https://github.com/sergeygalkin/cookbook/blob/master/gentoo/kernel_config/home/config) build time (after make clean) is about 3 minutes on this hardware

-   disk is INTEL SSDSC2CW240A3
-   memory is 2 x CRUCIAL BL16G32C16U4B.M16FE with Configured Memory Speed: 2666 MT/s

`root `[`#`]`time make -sj 17`

    real  2m58,980s
    user    38m32,045s
    sys 4m14,134s

The maximum temperature is about 81°C during kernel build with standard AMD Box cooler without overclocking

`user `[`$`]`sensors`

    k10temp-pci-00c3

    Adapter: PCI adapter
    Vcore:         1.38 V
    Vsoc:          1.10 V
    Tctl:         +81.5°C
    Tdie:         +81.5°C
    Tccd1:        +80.0°C
    Icore:        60.00 A
    Isoc:          6.50 A

### [Known hardware issues]

#### [Ethernet timeouts]

-   use fresh kernel, 5.14+
-   disable scatter-gather on every boot via \`/usr/sbin/ethtool -K eth0 sg off\`

#### [Bridge interface is not working with kvm]

Found on 5.8.8 kernel. This bridge is standard bridge interface:

`root `[`#`]`brctl show`

    bridge name  bridge id       STP enabled interfaces
    br10        8000.10c37b6d02a3   no      eth0

With kvm interface like this:

[CODE]

    <interface type='bridge'>
          <mac address='52:54:00:9d:cd:d0'/>
          <source> bridge='br10'/>
          <model type='rtl8139'/>
          <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
        </interface>

Network stop working until kvm stopped. Error is

[CODE]

    [ 6037.109831] ------------[ cut here ]------------
    [ 6037.109850] NETDEV WATCHDOG: eth0 (r8125): transmit queue 0 timed out
    [ 6037.109866] WARNING: CPU: 3 PID: 0 at net/sched/sch_generic.c:442 dev_watchdog+0x279/0x280
    [ 6037.109869] Modules linked in: razerkbd(O) ebtable_filter ebtables ip6table_filter ip6_tables rpcsec_gss_krb5 auth_rpcgss nfsv4 dns_resolver nfs lockd grace fscache xt_REDIRECT xt_MASQUERADE xt_addrtype iptable_nat nf_nat nvidia_drm(PO) snd_usb_audio snd_usbmidi_lib snd_rawmidi nvidia_modeset(PO) snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi snd_hda_intel nvidia(PO) snd_intel_dspcfg snd_hda_codec snd_hwdep snd_hda_core kvm_amd snd_pcm snd_timer kvm irqbypass snd r8125(O) uvcvideo videobuf2_vmalloc videobuf2_memops videobuf2_v4l2 videobuf2_common xhci_pci xhci_pci_renesas sunrpc [last unloaded: razerkbd]
    [ 6037.109900] CPU: 3 PID: 0 Comm: swapper/3 Tainted: P           O    T 5.8.8-gentoo #2
    [ 6037.109903] Hardware name: ASUS System Product Name/TUF GAMING B550M-PLUS, BIOS 1004 08/13/2020
    [ 6037.109906] RIP: 0010:dev_watchdog+0x279/0x280
    [ 6037.109909] Code: 90 e9 7a ff ff ff 4c 89 f7 c6 05 0f 3d b5 00 01 e8 3c 11 fc ff 44 89 e9 48 89 c2 4c 89 f6 48 c7 c7 68 33 28 82 e8 7d 5b 6b ff <0f> 0b e9 58 ff ff ff 0f 1f 44 00 00 41 54 48 8d 87 40 01 00 00 31
    [ 6037.109912] RSP: 0018:ffffc900001b8e88 EFLAGS: 00010282
    [ 6037.109915] RAX: 0000000000000000 RBX: ffff8888023a3600 RCX: 0000000000000000
    [ 6037.109917] RDX: 0000000000000103 RSI: ffffffff821e22d7 RDI: 00000000ffffffff
    [ 6037.109920] RBP: ffff888806e9839c R08: 0000000000000486 R09: 0000000000000007
    [ 6037.109922] R10: 0000000000000000 R11: 0000000000000000 R12: ffff888806e98440
    [ 6037.109924] R13: 0000000000000000 R14: ffff888806e98000 R15: ffff8888023a3680
    [ 6037.109927] FS:  0000000000000000(0000) GS:ffff88880ecc0000(0000) knlGS:0000000000000000
    [ 6037.109929] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
    [ 6037.109931] CR2: 00000169fb970000 CR3: 0000000601970000 CR4: 0000000000340ee0
    [ 6037.109933] Call Trace:
    [ 6037.109937]  <IRQ>
    [ 6037.109942]  ? pfifo_fast_init+0x130/0x130
    [ 6037.109946]  ? pfifo_fast_init+0x130/0x130
    [ 6037.109950]  call_timer_fn+0x46/0x1a0
    [ 6037.109957]  ? pfifo_fast_init+0x130/0x130
    [ 6037.109960]  __run_timers.part.0+0x17b/0x280
    [ 6037.109966]  ? _raw_spin_lock_irq+0x14/0x40
    [ 6037.109970]  ? __hrtimer_run_queues+0x14c/0x320
    [ 6037.109974]  ? rebalance_domains+0x102/0x3b0
    [ 6037.109978]  ? ktime_get+0x4a/0xc0
    [ 6037.109982]  run_timer_softirq+0x31/0x60
    [ 6037.109986]  __do_softirq+0x103/0x36d
    [ 6037.109991]  asm_call_on_stack+0x12/0x20
    [ 6037.109994]  </IRQ>
    [ 6037.109997]  do_softirq_own_stack+0x5e/0x80
    [ 6037.110001]  irq_exit_rcu+0xc8/0x120
    [ 6037.110006]  sysvec_apic_timer_interrupt+0x54/0x100
    [ 6037.110011]  asm_sysvec_apic_timer_interrupt+0x12/0x20
    [ 6037.110016] RIP: 0010:cpuidle_enter_state+0xc1/0x400
    [ 6037.110023] Code: 85 c0 0f 8f 5f 02 00 00 31 ff e8 6a 0c 7b ff 45 84 f6 74 12 9c 58 f6 c4 02 0f 85 0a 03 00 00 31 ff e8 23 a3 80 ff fb 45 85 ed <0f> 88 fa 00 00 00 49 63 c5 be 68 00 00 00 4d 29 fc 48 89 c2 48 8d
    [ 6037.110026] RSP: 0018:ffffc900000cbe80 EFLAGS: 00000202
    [ 6037.110030] RAX: ffff88880ecc0000 RBX: ffffffff824a2360 RCX: 000000000000001f
    [ 6037.110033] RDX: 0000000000000000 RSI: ffffffff821e22d7 RDI: ffffffff821eaad3
    [ 6037.110036] RBP: ffff88880afc1400 R08: 0000000000000002 R09: 000000000000000a
    [ 6037.110039] R10: 000000000000095c R11: ffff88880ece9364 R12: 0000057d9fc95bf6
    [ 6037.110042] R13: 0000000000000002 R14: 0000000000000000 R15: 0000057d9f978024
    [ 6037.110049]  cpuidle_enter+0x37/0x60
    [ 6037.110052]  do_idle+0x1f0/0x2b0
    [ 6037.110055]  cpu_startup_entry+0x19/0x20
    [ 6037.110059]  start_secondary+0x154/0x180
    [ 6037.110061]  secondary_startup_64+0xa4/0xb0
    [ 6037.110065] ---[ end trace fa1f4a48a1b3cbc7 ]---