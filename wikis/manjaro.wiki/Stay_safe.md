\

## Contents

-   [[1] [Stay safe]](#Stay_safe)
    -   [[1.1] [Hardware]](#Hardware)
        -   [[1.1.1] [HDD / SSD]](#HDD_.2F_SSD)
        -   [[1.1.2] [Power supply]](#Power_supply)
        -   [[1.1.3] [Motherboard]](#Motherboard)
        -   [[1.1.4] [Upgrade]](#Upgrade)
            -   [[1.1.4.1] [CPU / RAM]](#CPU_.2F_RAM)
            -   [[1.1.4.2] [GPU]](#GPU)
            -   [[1.1.4.3] [HDD / SSD]](#HDD_.2F_SSD_2)
    -   [[1.2] [Software]](#Software)
        -   [[1.2.1] [Update]](#Update)
            -   [[1.2.1.1] [read]](#read)
            -   [[1.2.1.2] [consider]](#consider)
            -   [[1.2.1.3] [update]](#update_2)
            -   [[1.2.1.4] [reboot]](#reboot)
        -   [[1.2.2] [repartitioning]](#repartitioning)
        -   [[1.2.3] [next]](#next)
    -   [[1.3] [Be prepared]](#Be_prepared)
        -   [[1.3.1] [extern backup]](#extern_backup)
        -   [[1.3.2] [Live manjaro]](#Live_manjaro)
    -   [[1.4] [proven techniques]](#proven_techniques)
        -   [[1.4.1] [kernel]](#kernel)
        -   [[1.4.2] [BTRFS]](#BTRFS)
        -   [[1.4.3] [snapshots]](#snapshots)
            -   [[1.4.3.1] [timeshift]](#timeshift)
            -   [[1.4.3.2] [snapper]](#snapper)
        -   [[1.4.4] [Gparted]](#Gparted)
            -   [[1.4.4.1] [GPT]](#GPT)
        -   [[1.4.5] [encryption]](#encryption)
            -   [[1.4.5.1] [Your sub title 2]](#Your_sub_title_2)
    -   [[1.5] [This is Work in progress as of 30.05.2024]](#This_is_Work_in_progress_as_of_30.05.2024)

# [Stay safe]

This is a collection of options you have to operate your manjaro safely. This is about events that can happen to every Linux user. Please do not underestimate the relevant risks and warnings. You can easily start a search in the Manjaro forum for each of the following points. Then you will get an overview of what the current status is at each point.

## [Hardware]

Hardware tends to break from time to time ;-) . This most often happens shortly after installation (\< 1 month) or after the end of the average lifespan (e.g. \> 5 years). Sometimes it also has to do with beer, coffee or orange juice.

### [][HDD / SSD]

Please remember that every hard drive/SSD will fail at some point and be prepared. Sometimes the data can still be read (then it\'s time for a final backup). But you can\'t rely on that.

### [Power supply]

You can simply replace a broken power supply with a new one. If you have been very unlucky, the old power supply may have damaged other things like your motherboard or hard drives when it died. But that rarely happens.

### [Motherboard]

If you need to replace your motherboard, be aware that the new one usually won\'t boot right away. There is UEFI in the motherboard. This contains the configuration of the way you used to boot. With the replacement, this is missing from the new UEFI.

In the simplest case it is enough to go to the UEFI boot selection. Your UEFI will then search for a suitable UEFI partition. And ideally finds the boot entry for the grub of manjaro.

### [Upgrade]

Sometimes you want to improve your computer without replacing it entirely. If you do this carefully, Manjaro doesn\'t even need to be reinstalled.

#### [][CPU / RAM]

Nothing to do.

#### [GPU]

Especially when changing vendor, please ask in manjaro forum for help with the right steps.

#### [][HDD / SSD]

You can use Gparted to create a GPT and partitions on the SSD. You can then use btrfs to [add a partition](//wiki.manjaro.org/index.php?title=Btrfs#Extend_a_volume "Btrfs") to your existing volume.

If you want to keep your "old" HDD/SSD and have enough space, you can even easily [set up a RAID10](//wiki.manjaro.org/index.php?title=Btrfs#Btrfs_RAID "Btrfs") .

## [Software]

As a rolling release, the Manjaro software is renewed regularly. You need enough file system space and a way to rollback if the update fails catastrophically. Even when you install or reconfigure a program, a lot can go wrong. Better safe than sorry.

**Experienced system administrators say:**

------------------------------------------------------------------------

no backup - no pity

### [Update]

The closer you stay to updating, the fewer problems you will encounter. But that doesn\'t just mean installing the updates, but also reading the relevant thread beforehand. Carry out the necessary maintenance work after the update. Then a reboot should definitely follow.

Being careless in these matters can work well for a long time, but it usually takes its toll at some point. The clean-up work usually takes a lot longer than the time saved.

#### [read]

Best approach is to read posts 1 and 2 of the update announcement, before updating. That is where potential issues and required manual intervention steps are set out.

If the update thread is only a few hours old, it\'s better to wait a while. An update in the first 24 hours is only for people who can help themselves ;-)

#### [consider]

Consider whether any of the problems described may occur to you If so, there is usually a link with instructions on what you should do. Please read this carefully. Then act accordingly. This will save you a lot of problems.

#### [update]

Do the update on the console (tty). The GUIs are all well and good, but there are update situations where the GUI might freeze. This is the first step to disaster. And please do not let your computer go into sleep / power off while updating.

After the update has been completed, check again whether there are any errors or warnings. If so, read the message and see if there is a recommendation for action. If so, act.

If you are unsure, **copy the warnings** and ask on the Manjaro forum (before proceeding)

#### [reboot]

If you are afraid of booting, check if the necessary files are there to boot.

      * kernel(s)
      * modules
      * initr
      * grub.cfg
      (or use maxi to test this)

### [repartitioning]

There may be good reasons to change the partitions in your system. First, create a full backup (we hope you don\'t need to restore this). Then use a live manjaro with gparted to repartition to your liking.

### [next]

## [Be prepared]

#### [extern backup]

#### [Live manjaro]

You need a CD/DVD or USB to boot from. This should be a current version of manjaro. In no case older than 6 months. The desktop does not have to be the same as your usual desktop. For example, the version with XFCE (fast and robust) is well suited.

What you could do this way:

-   Boot into a Manjaro without changing the internal HDD or SSD
-   If possible, make an additional backup of certain "latest" data
-   Determine the real problem using guidance from the wiki/forum
-   Fix the problem using instructions from the wiki/forum
-   Roll back using snapper or timeshift
-   Perform a reinstallation
-   Import your backups

## [proven techniques]

### [kernel]

Keep at least 2 kernels installed. At least one of them should be a LTS-kernel.

[Manjaro Kernels](//wiki.manjaro.org/index.php?title=Manjaro_Kernels "Manjaro Kernels")

### [BTRFS]

BTRFS works with COW, checksums, logs, barriers \... to keep your filesystem safe.

-   Be sure to mount your btrfs-subvolumes with option *noatime*
-   Use *timeshift* or *snapper* together with btrfs
-   Use mount-option *comression=zstd* to save space (and eventually speed up a little)
-   do not forget to watch the unallocated space on your btrfs-volume

[Read more about BTRFS](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs")

### [snapshots]

BTRFS also enables you to make snapshots easily and without wasting time and space. This is the basis for easy rollbacks.

[read more about snapshots](//wiki.manjaro.org/index.php?title=Btrfs#Snapshot "Btrfs")

#### [timeshift]

Timeshift is very easy to use, and to rollback. It works best together with btrfs.

#### [snapper]

Snapper only works with btrfs. But it can do more than timeshift. In particular, it supports multiple profiles. This allows it to offer separate rollbacks for the system and for data in /home or elsewhere.

### [Gparted]

Gparted is a really well-functioning program for viewing the partitions of an HDD/SSD. It can move and resize existing partitions. It carries out all necessary changes so that the file system is preserved as much as possible.

This only can be done when the partitions are not mounted while gparted runs. So you will need to use a live manjaro to repartition your system.

**Although gparted works very well**

------------------------------------------------------------------------

That is not a sensible reason to forego a backup!

#### [GPT]

If it is possible for you to use a GPT partition table, it is strongly recommended to do so. Together with UEFI, this simplifies the boot process and is much easier to maintain in the long run.

\

**UEFI/GPT mixed with BIOS(CSM)/MBR boot**

------------------------------------------------------------------------

Don\'t ever mix UEFI-native booting and BIOS-compatible booting in one pc ([Source of Warning](https://www.happyassassin.net/posts/2014/01/25/uefi-boot-how-does-that-actually-work-then/))

### [encryption]

**It has been shown that encryption significantly complicates the task of saving a system**

------------------------------------------------------------------------

So only use this if you really do regular backups and are sure that you can get everything back if you accidentally lock yourself out of your system.

It would be really good if you understood exactly beforehand

-   At what level it is encrypted
-   Where the keys are
-   How to create a backup of the keys

#### [Your sub title 2]

**}}**

------------------------------------------------------------------------

}}

\

    Example codes should be here.

\

## [This is Work in progress as of 30.05.2024]

[Example Link Title](https://example.link) example text