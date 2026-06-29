[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Partitioning+Overview+and+Existing+Partition+Tables&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Partitioning_Overview_and_Existing_Partition_Tables "Partitioning Overview and Existing Partition Tables (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Partitioning_Overview_and_Existing_Partition_Tables/fr "Partitions et Partitionner (82% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Partitioning_Overview_and_Existing_Partition_Tables/ru "Обзор разделов и существующие таблицы разделов (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Primary and Logical Partitions]](#Primary_and_Logical_Partitions)
    -   [[1.2] [Conventions and Guidelines]](#Conventions_and_Guidelines)
    -   [[1.3] [Where Using an Existing Linux Partition Table]](#Where_Using_an_Existing_Linux_Partition_Table)
-   [[2] [See Also]](#See_Also)

# [Overview]

Manjaro uses a text-based disk partitioning tool called *cfdisk*. How you choose to partition your hard disk manually is largely down to personal preference. However, some guidance has been provided, particularly for any new users wishing to manually partition their hard disks. Partitioning (that is, dividing) your hard disk when installing an operating system may be undertaken for a number of different reasons. The most common examples include:

-   Meeting the requirements of certain operating systems, such as Windows, which requires at least two partitions: one for boot and one for Windows itself.
-   The ability to install multiple operating systems on a single hard disk
-   Separating parts of the hard disk to serve specific purposes, for example, for booting or to serve as virtual memory or Swap, and
-   Separating parts of the hard disk to store specific types of files: system files, personal files and so on.

\

## [Primary and Logical Partitions]

There are two types of partition that may be used to divide a hard disk. These are **Primary Partitions** and **Logical Partitions**. *Primary partitions* are a throwback to the early days of computing, and only allow for a hard disk to be divided into a maximum of four parts, for example, you can have a maximum of four primary partitions, or three primaries and one extended partition which may contain several *Logical partitions* depending upon the architecture. They are, in essence, a way of further sub-dividing one primary partition into logical partitions is known as an **Logical partitions**. For example:

-   sda1 = 1st Primary
-   sda2 = 2nd Primary
-   sda3 = 3rd Primary
-   sda4 = 4th Extended Primary Partition (not actually usable as such)
    -   sda5 = 5th Logical
    -   sda6 = 6th Logical
    -   sda7 = 7th Logical
    -   sda8 = 8th Logical
    -   and so on, depending upon your disk space and needs.

While the maximum number of Primary Partitions allowed on any drive is 4, through using Logical partitions, an IDE drive can be subdivided into just over 60 partitions, while a SCSI drive can be subdivided into over a dozen. Below is a simple illustration of how logical partitions can be used to partition a hard disk into eight parts:

[![Partitions.png](/images/8/8c/Partitions.png)](//wiki.manjaro.org/index.php?title=File:Partitions.png)

(courtesy of [LinuxQuestions.org](http://www.linuxquestions.org/questions/slackware-14/primary-vs-logical-487883/))

\

## [Conventions and Guidelines]

-   The convention for listing drives and partitions is: sd **\[hard disk letter\] \[partition number\]**. For example, the first (or only) hard disk connected to your system will be listed as sd**a**, the second sd**b**, and so on. In respect to partitions, sda**1** would be the first partition found in the first hard disk, sda**2** would be the second partition, and so on. Logical Partitions will always begin from \'5\'.

<!-- -->

-   Unlike Windows (which requires that there is a primary partition specifically to boot), Linux systems such as Manjaro have no specific requirements for the use of Primary or Logical Partitions. For example, Manjaro may be installed using all Primary Partitions, all Logical Partitions, or a mixture of the two.

<!-- -->

-   Although the assisted preparation method creates separate partitions for the GRUB (Boot), virtual memory (Swap), Manjaro operating system (Root), and personal files (Home), this is an entirely optional set up. For example, the Boot, Root, and Home partitions can be easily combined into a single partition. This is the case with other popular distributions such as Mint.

<!-- -->

-   Separating or combining partitions is where personal preference comes in. Each set-up will have its own advantages and disadvantages. For example, separating Boot, Root and Home has the advantage of easily backing up and/or repairing problems without affecting anything else. A disadvantage is the potential to run out of pre-allocated space for a partition (e.g. the Root), even if ample space is available on the hard disk itself.

<!-- -->

-   Although allocating a swap partition is itself entirely optional, it is still **strongly recommended** that you do so, particularly if you wish to use *hibernate* or *suspend* functions, as these will require use of a swap partition. Manjaro should therefore be installed using a minimum of two partitions.

<!-- -->

-   Unless you know exactly what you are doing, the size of the swap partition should be the same as the amount of RAM your system is using (e.g. 2 gigabytes of space would be allocated to a swap partition if using 2 gigabytes of memory).

<!-- -->

-   However you decide to partition your hard disk, almost any of them can be designated as a bootable partition and contain the GRUB. The exception is the swap partition.

<!-- -->

-   Two Linux operating systems installed on the same system can share the same GRUB and Swap Partition; they don\'t need one each.

\

## [Where Using an Existing Linux Partition Table]

It is worthwhile noting that the Manjaro installer will not overwrite a Home folder if it contains an existing username. As a consequence, the pre-installed desktop environment will lose its Manjaro configurations, and revert back to its basic (\'vanilla\') settings. In order to restore the Manjaro configuration settings, having booted into the freshly installed system, it will be necessary to enter the following command in your terminal:

    cp -a /etc/skel/. /home/[username]

\
For example, for an account called *carl*, the following command would be entered:

    cp -a /etc/skel/. /home/carl

\
Once complete, it will then be necessary to ensure that you have full ownership of the Home folder by entering the following command:

    chown -R [username] /home/[username]

\
For example, for the same account called *carl*, the following command would be entered:

    chown -R carl /home/carl

# [See Also]

-   **[Installation Guides](//wiki.manjaro.org/index.php?title=Installation_Guides "Installation Guides")**
-   **[Basic Partitioning Scenarios](//wiki.manjaro.org/index.php?title=Cfdisk_Basic_Partitioning_Scenarios "Cfdisk Basic Partitioning Scenarios")**