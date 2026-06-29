Old **LSI Embedded MegaRAID** and **Embedded RAID-II** are *fakeraid* controllers. Historically they was only supported by proprietary driver named *megasr*, available only as RPM for RHEL with kernels 2.6.18.x. Luckily most functions of megasr unofficially supported by opensource *mptsas* driver.

## Contents

-   [[1] [No Warranty notice]](#No_Warranty_notice)
-   [[2] [(Unofficial) supported cards]](#.28Unofficial.29_supported_cards)
-   [[3] [Make mptsas to support controller]](#Make_mptsas_to_support_controller)
-   [[4] [RAID capabilities]](#RAID_capabilities)

## [No Warranty notice]

Since in this guide we use undocumented and unofficial features of mptsas drivers, there is **NO WARRANTY** of proper work of fakeraid. Please, before any actions on actual data perform backup first!

## [][(Unofficial) supported cards]

This list is not complete.

  ------------------------------ -----------
  Name (as shown in lspci)       PCI ID
  LSI MegaRAID SAS 8204ELP
  LSI MegaRAID SAS 8204XLP
  LSI MegaRAID SAS 8208XLP       1000:0055
  M1064E MegaRAID SAS            1000:0057
  MegaRAID SAS 8208ELP/8208ELP   1000:0059
  ------------------------------ -----------

## [Make mptsas to support controller]

By default *mptsas* no handles with *megasr*-compatible controllers. You need to provide corresponding PCI ID. First let\'s find out it:

`root `[`#`]`lspci -nn`

    ...
    08:00.0 SCSI storage controller [0100]: LSI Logic / Symbios Logic M1064E MegaRAID SAS [1000:0057] (rev 04)
    ...

In this example PCI ID is 1000:0057. Give it to mpt-sas:

`root `[`#`]`modprobe mptsas `

`root `[`#`]`echo "1000 0057" > /sys/bus/pci/drivers/mptsas/new_id `

Now, if all goes right, your disks will be appear in system (check dmesg). For permanent effect you need add *mptsas* to [/etc/modules.d] and \'echo \"1000 0057\" \> /sys/bus/pci/drivers/mptsas/new_id\' to [/etc/local.d/mptsas.start]:

`root `[`#`]`echo 'echo "1000 0057" > /sys/bus/pci/drivers/mptsas/new_id' > /etc/local.d/mptsas.start `

`root `[`#`]`chmod 755 /etc/local.d/mptsas.start `

## [RAID capabilities]

If RAID already configured in firmware and you need access to filesystem on it, you\'ll need to prepare your system and install [[[sys-fs/mdadm]](https://packages.gentoo.org/packages/sys-fs/mdadm)[]] package. [mdadm](https://wiki.gentoo.org/wiki/Mdadm "Mdadm") daemon will automatically take RAID configuration and provide it to system as /dev/mdX block device. At first time mdadm will start resynchronization, that OK.