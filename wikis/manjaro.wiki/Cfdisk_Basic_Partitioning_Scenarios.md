+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) | **This article or section is out of date.**                                                                                                                                                                                                                                                                                                                                                                                                                  | [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) |
|                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | **Reason:** This information can be outdated. [Oguzkagan](//wiki.manjaro.org/index.php?title=User:Oguzkagan&action=edit&redlink=1 "User:Oguzkagan (page does not exist)") ([talk](//wiki.manjaro.org/index.php?title=User_talk:Oguzkagan "User talk:Oguzkagan")) ([Discuss](//wiki.manjaro.org/index.php?title=Talk:Cfdisk_Basic_Partitioning_Scenarios&action=edit&redlink=1 "Talk:Cfdisk Basic Partitioning Scenarios (page does not exist)")) |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [A Two Partition Scenario]](#A_Two_Partition_Scenario)
    -   [[2.1] [Creating the Partitions]](#Creating_the_Partitions)
    -   [[2.2] [Finalising the Disk Preparation]](#Finalising_the_Disk_Preparation)
    -   [[2.3] [Install Manjaro]](#Install_Manjaro)
-   [[3] [A Three Partition Scenario]](#A_Three_Partition_Scenario)
    -   [[3.1] [Creating the Partitions]](#Creating_the_Partitions_2)
    -   [[3.2] [Finalising the Disk Preparation]](#Finalising_the_Disk_Preparation_2)
-   [[4] [See Also]](#See_Also)

# [Overview]

**Tip**

------------------------------------------------------------------------

The **[Partitioning Overview and Existing Partition Tables](//wiki.manjaro.org/index.php?title=Partitioning_Overview_and_Existing_Partition_Tables "Partitioning Overview and Existing Partition Tables")** guide provides an overview and explanation of primary and logical partitions, as well as advice on what to do if intending to use a shared Home Partition.

\
Basic partitioning scenarios have been presented below for illustrative purposes. In particular, the intention is to illustrate the substantial degree of flexibility when deciding upon an appropriate partitioning scheme when using *cfdisk*.

\

# [A Two Partition Scenario]

In this scenario, Boot, Root, and Home will be combined into a single bootable partition (SDA1). A seperate swap partition will also be created in the remaining space, using a logical partition (SDA2/SDA5).

## [Creating the Partitions]

[![NewPpart-082.png](/images/thumb/b/b6/NewPpart-082.png/375px-NewPpart-082.png)](//wiki.manjaro.org/index.php?title=File:NewPpart-082.png)

[](//wiki.manjaro.org/index.php?title=File:NewPpart-082.png "Enlarge")

\
Use the left and right arrow keys to select the available options in *cfdisk*. The up and down arrow keys are used to select disk space / partitions. In this instance, Manjaro is being installed on a clean hard disk with no existing partitions or data. **New** has been highlighted to create the first new partition.

Press \<enter\> to continue.\

[![Newprimary-082.png](/images/thumb/b/bb/Newprimary-082.png/375px-Newprimary-082.png)](//wiki.manjaro.org/index.php?title=File:Newprimary-082.png)

[](//wiki.manjaro.org/index.php?title=File:Newprimary-082.png "Enlarge")

\
The first step will be to define if it is a Primary or Logical Partition. In this instance, **Primary** has been selected.

Press \<enter\> to continue.\

[![NewPsize-082.png](/images/thumb/4/4e/NewPsize-082.png/375px-NewPsize-082.png)](//wiki.manjaro.org/index.php?title=File:NewPsize-082.png)

[](//wiki.manjaro.org/index.php?title=File:NewPsize-082.png "Enlarge")

\
The second step is to define the size of the partition. In this instance, 40,949MB (40GB) out of a total of 42,949MB (42GB), has been allocated, with the intention to leave approximately 2000MB (2GB) remaining for the swap partition.

\

\

**Tip**

------------------------------------------------------------------------

If, for example, the intention was to leave 20GB of unallocated space on the author\'s hard drive to install another operating system later, then 20949MB (20GB) would be allocated instead. Once the 2GB swap partition was allocated, this would leave 20GB of space remaining. An installer used by a distro like Mint or Ubuntu would even automatically detect and use this unallocated space for installation alongside Manjaro.

Once the value has been set, press \<enter\> to continue.\

\

[![NewPplace-082.png](/images/thumb/9/97/NewPplace-082.png/375px-NewPplace-082.png)](//wiki.manjaro.org/index.php?title=File:NewPplace-082.png)

[](//wiki.manjaro.org/index.php?title=File:NewPplace-082.png "Enlarge")

\
The third (and final) step is to define where the partition starts on your hard drive (i.e. from the beginning or the end of the available space). As with this instance - unless you have a specific reason to do otherwise - it is recommended to always start your partition(s) at the beginning of your hard drive / available space on your hard drive.

Once the selection has been highlighted, press \<enter\> to continue.\

[![NewPboot-082.png](/images/thumb/d/d6/NewPboot-082.png/375px-NewPboot-082.png)](//wiki.manjaro.org/index.php?title=File:NewPboot-082.png)

[](//wiki.manjaro.org/index.php?title=File:NewPboot-082.png "Enlarge")

\
This partition must also be bootable, as it is intended to contain the Boot/GRUB. To mark it as such, the **Bootable** flag/option has been highlighted.

\

**Note**

------------------------------------------------------------------------

Unless you intend to use an existing bootable partition (i.e. used by an existing Linux operating system), then you must also do the same for the partition where you intended to store the GRUB.

Press \<enter\> to continue.\

[![NewLpart-082.png](/images/thumb/3/3b/NewLpart-082.png/375px-NewLpart-082.png)](//wiki.manjaro.org/index.php?title=File:NewLpart-082.png)

[](//wiki.manjaro.org/index.php?title=File:NewLpart-082.png "Enlarge")

\
Note that the partition - listed as sda1 - has now been flagged as *boot*.

With this complete, the swap partition will now be created. This is undertaken by first selecting the free space underneath the partition, and then highlighting the **New** option.

Press \<enter\> to continue.\

[![NewLogical-082.png](/images/thumb/2/26/NewLogical-082.png/375px-NewLogical-082.png)](//wiki.manjaro.org/index.php?title=File:NewLogical-082.png)

[](//wiki.manjaro.org/index.php?title=File:NewLogical-082.png "Enlarge")

\
As before, the first step is to define the type of partition to be used. In this instance, for illustrative purposes, the swap partition has been defined as a **Logical** partition, although it would make no real difference if it were defined as a primary partition instead.

Press \<enter\> to continue.\

[![LogicalPsize-082.png](/images/thumb/e/eb/LogicalPsize-082.png/375px-LogicalPsize-082.png)](//wiki.manjaro.org/index.php?title=File:LogicalPsize-082.png)

[](//wiki.manjaro.org/index.php?title=File:LogicalPsize-082.png "Enlarge")

\
Again, the second step is to define the size of the new partition. In this instance, the remaining space of 2GB has been allocated, which has already been listed by default.

Press \<enter\> to continue.\

[![Swapdefine-082.png](/images/thumb/8/83/Swapdefine-082.png/375px-Swapdefine-082.png)](//wiki.manjaro.org/index.php?title=File:Swapdefine-082.png)

[](//wiki.manjaro.org/index.php?title=File:Swapdefine-082.png "Enlarge")

\
As this newly created partition is intended to be used as a swap partition, it is necessary to specifically define its type as such. To do so, the **Type** option has been highlighted.

Press \<enter\> to continue.\

[![Typedefine-082.png](/images/thumb/2/24/Typedefine-082.png/375px-Typedefine-082.png)](//wiki.manjaro.org/index.php?title=File:Typedefine-082.png)

[](//wiki.manjaro.org/index.php?title=File:Typedefine-082.png "Enlarge")

\
A list of (hexadecimal) codes corresponding to the available types of partition will be displayed. It will be necessary to press a key to continue and enter the appropriate code.

In this instance - as illustrated - the code **82** has been typed in to define the partition type as swap.

Once the code has been typed in, press \<enter\> to continue.\

[![Writepartv2-082.png](/images/thumb/5/5d/Writepartv2-082.png/375px-Writepartv2-082.png)](//wiki.manjaro.org/index.php?title=File:Writepartv2-082.png)

[](//wiki.manjaro.org/index.php?title=File:Writepartv2-082.png "Enlarge")

\
Note that the swap partition has been listed as **sda5**. This is because primary partitions only range from sda1 to sda4, while logical partitions always start from sda5. Also note that sda5 is listed as a swap partition.

With both partitions created and defined, the partition table must now be written to the hard disk. To do so, the **write** option must be highlighted, before pressing \<enter\> to continue.

Upon doing so a warning message will appear. It will also be necessary to confirm your intention to write the new partitions by typing in **yes** at the prompt and then pressing \<enter\> again.\

[![Cfdiskquit-082.png](/images/thumb/4/48/Cfdiskquit-082.png/375px-Cfdiskquit-082.png)](//wiki.manjaro.org/index.php?title=File:Cfdiskquit-082.png)

[](//wiki.manjaro.org/index.php?title=File:Cfdiskquit-082.png "Enlarge")

\
With the partitions completed and written, highlight **quit** to exit from *cfdisk*.

Press \<enter\> to continue.\

\

## [Finalising the Disk Preparation]

[![Partitiondone-082.png](/images/thumb/7/71/Partitiondone-082.png/375px-Partitiondone-082.png)](//wiki.manjaro.org/index.php?title=File:Partitiondone-082.png)

[](//wiki.manjaro.org/index.php?title=File:Partitiondone-082.png "Enlarge")

\
You will be returned to the hard disk selection menu. Highlight **Done** as the disk partitioning has been completed.

Press \<enter\> to continue.\

[![Partitionmsg-082.png](/images/thumb/3/3f/Partitionmsg-082.png/375px-Partitionmsg-082.png)](//wiki.manjaro.org/index.php?title=File:Partitionmsg-082.png)

[](//wiki.manjaro.org/index.php?title=File:Partitionmsg-082.png "Enlarge")

\
A message will appear stating that it will now be necessary to select the appropriate partitions to use for the Manjaro installation.

Press \<enter\> to continue.\

[![Selectdiskagain-082.png](/images/thumb/1/16/Selectdiskagain-082.png/375px-Selectdiskagain-082.png)](//wiki.manjaro.org/index.php?title=File:Selectdiskagain-082.png)

[](//wiki.manjaro.org/index.php?title=File:Selectdiskagain-082.png "Enlarge")

\
As before,The installer will automatically detect and display all hard discs connected to your system. Where more than one drive is present on your system, highlight the drive partitioned earlier.

Press \<enter\> to continue.\

[![Confirmswap-082.png](/images/thumb/d/d7/Confirmswap-082.png/375px-Confirmswap-082.png)](//wiki.manjaro.org/index.php?title=File:Confirmswap-082.png)

[](//wiki.manjaro.org/index.php?title=File:Confirmswap-082.png "Enlarge")

\
**Select the appropriate partition to use for the Swap**. In this instance, the swap partition is **sda5**, which has been highlighted for selection.

Press \<enter\> to continue.\

[![Swapwarn-082.png](/images/thumb/3/33/Swapwarn-082.png/375px-Swapwarn-082.png)](//wiki.manjaro.org/index.php?title=File:Swapwarn-082.png)

[](//wiki.manjaro.org/index.php?title=File:Swapwarn-082.png "Enlarge")

\
**Confirm that you wish to format your chosen partition.**

Press \<enter\> to continue.\

[![Confirmroot-082.png](/images/thumb/0/0a/Confirmroot-082.png/375px-Confirmroot-082.png)](//wiki.manjaro.org/index.php?title=File:Confirmroot-082.png)

[](//wiki.manjaro.org/index.php?title=File:Confirmroot-082.png "Enlarge")

\
**Select the appropriate partition to use for the Root**. Again, this is where Manjaro itself (and later, any newly installed applications for it) will be stored. In this instance, it\'s an easy choice as the only remaining partition available is **sda1**.

Press \<enter\> to continue.\

[![ConfirmFS-082.png](/images/thumb/2/20/ConfirmFS-082.png/375px-ConfirmFS-082.png)](//wiki.manjaro.org/index.php?title=File:ConfirmFS-082.png)

[](//wiki.manjaro.org/index.php?title=File:ConfirmFS-082.png "Enlarge")

\
**Set the file system to manage your files**. If you are unsure which file system to choose, as illustrated, then it is recommend to highlight [ext4](http://en.wikipedia.org/wiki/Ext4), as this is one of the latest and perhaps most widely used Linux file systems.

Press \<enter\> to continue\

[![ConfirmRT-082.png](/images/thumb/8/81/ConfirmRT-082.png/375px-ConfirmRT-082.png)](//wiki.manjaro.org/index.php?title=File:ConfirmRT-082.png)

[](//wiki.manjaro.org/index.php?title=File:ConfirmRT-082.png "Enlarge")

\
**Confirm that you wish to format your chosen partition.**

Press \<enter\> to continue.\

[![MntBoot-082.png](/images/thumb/f/f1/MntBoot-082.png/375px-MntBoot-082.png)](//wiki.manjaro.org/index.php?title=File:MntBoot-082.png)

[](//wiki.manjaro.org/index.php?title=File:MntBoot-082.png "Enlarge")

\
**Select any other partitions to mount at bootup.** If a separate *Boot Partition* had been created, it would be selected here. Upon pressing \<enter\> to continue, it would then be necessary to select which file system to use for it (e.g. ext4), and then to confirm that it is to be mounted at \'/boot\'.

Once completed, the process would also be repeated for any other relevant partitions, such as if a separate *Home Partition* had been created. **In essence, it will be necessary to select and mount all of the partitions you had created for your Manjaro installation so that they will all be available for use upon booting up**.

However, as in this instance only two partitions had been created (one of which combines Boot, Root, and Home), there are no further partitions to select.

Press \<enter\> to continue.\

[![ConfirmPart-082.png](/images/thumb/e/eb/ConfirmPart-082.png/375px-ConfirmPart-082.png)](//wiki.manjaro.org/index.php?title=File:ConfirmPart-082.png)

[](//wiki.manjaro.org/index.php?title=File:ConfirmPart-082.png "Enlarge")

\
**Review and confirm the mounted partitions.** A confirmation message will appear, listing all of the partitions to mounted during the bootup of your Manjaro installation. Ensure that all of your intended partitions have been listed, and that they have been listed correctly (e.g. purposes and file systems). If something is amiss, highlight *No* to be taken back.

Again, in this instance, the message confirms that sda5 is to be mounted as the Swap Partition, and that sda1 is to be mounted (using the ext4 file system) for everything else.

Press \<enter\> to continue.

\

[![Mntsuccess-082.png](/images/thumb/2/25/Mntsuccess-082.png/375px-Mntsuccess-082.png)](//wiki.manjaro.org/index.php?title=File:Mntsuccess-082.png)

[](//wiki.manjaro.org/index.php?title=File:Mntsuccess-082.png "Enlarge")

\
After a few moments, a message will appear to confirm that the partitions have been successfully mounted.

Press \<enter\> to continue.\

[![Pewgoback-082.png](/images/thumb/1/11/Pewgoback-082.png/375px-Pewgoback-082.png)](//wiki.manjaro.org/index.php?title=File:Pewgoback-082.png)

[](//wiki.manjaro.org/index.php?title=File:Pewgoback-082.png "Enlarge")

\
**Return to the Main Menu.** As this step has been completed, highlight **Main menu** and press \<enter\> to be taken back to the installer\'s main menu.\

## [Install Manjaro]

**[Return to the Installation Guide for Experienced Users](//wiki.manjaro.org/index.php?title=Installation_Guide_for_Experienced_Users_0.8.2&action=edit&redlink=1 "Installation Guide for Experienced Users 0.8.2 (page does not exist)")**

\

# [A Three Partition Scenario]

In this scenario, a partition will be created especially for Boot, seperate from the partition for Root and Home. A seperate swap partition will also be created. All the partitions created will be Primary Partitions.

## [Creating the Partitions]

[![Partition free.png](/images/thumb/2/26/Partition_free.png/375px-Partition_free.png)](//wiki.manjaro.org/index.php?title=File:Partition_free.png)

[](//wiki.manjaro.org/index.php?title=File:Partition_free.png "Enlarge")

\
In order to create a new partition, use your arrow keys to switch through the options and choose **new**.\

[![Partition pref.png](/images/thumb/6/6f/Partition_pref.png/375px-Partition_pref.png)](//wiki.manjaro.org/index.php?title=File:Partition_pref.png)

[](//wiki.manjaro.org/index.php?title=File:Partition_pref.png "Enlarge")

\
There are two preferences when creating partitions. *Primary* and *Logical* partitions. It\'s good to know that you can only create four primary partitions per Hard Drive. Choose the desired preference, then press enter to select it.\

[![Partition boot 100.png](/images/thumb/b/b5/Partition_boot_100.png/375px-Partition_boot_100.png)](//wiki.manjaro.org/index.php?title=File:Partition_boot_100.png)

[](//wiki.manjaro.org/index.php?title=File:Partition_boot_100.png "Enlarge")

\
We are now going to create the *boot* partition. For the *boot* partition, 100 MB and higher in recommended. Enter the desired size and press ENTER.\

[![Boot part beg.png](/images/thumb/d/d7/Boot_part_beg.png/375px-Boot_part_beg.png)](//wiki.manjaro.org/index.php?title=File:Boot_part_beg.png)

[](//wiki.manjaro.org/index.php?title=File:Boot_part_beg.png "Enlarge")

\
After that, the *Beginning* option will be highlighted. It\'s recommended to keep it that way, press ENTER to continue.\

[![Boot bootable.png](/images/thumb/c/c5/Boot_bootable.png/375px-Boot_bootable.png)](//wiki.manjaro.org/index.php?title=File:Boot_bootable.png)

[](//wiki.manjaro.org/index.php?title=File:Boot_bootable.png "Enlarge")

\
We also need to make the *boot* partition *Bootable*, press ENTER when *Bootable* is highlighted.\

[![New freespace.png](/images/thumb/4/47/New_freespace.png/375px-New_freespace.png)](//wiki.manjaro.org/index.php?title=File:New_freespace.png)

[](//wiki.manjaro.org/index.php?title=File:New_freespace.png "Enlarge")

\
We are now going to create a *swap* partition. After creating the *boot* partition, use your UP/DOWN arrow keys and choose *Free Space*. Use your arrow keys to navigate to the *new* option then, press ENTER.\

[![Free primary.png](/images/thumb/5/51/Free_primary.png/375px-Free_primary.png)](//wiki.manjaro.org/index.php?title=File:Free_primary.png)

[](//wiki.manjaro.org/index.php?title=File:Free_primary.png "Enlarge")

\
After that, press ENTER again when the *Primary* preference is highlighted.\

[![Swap size.png](/images/thumb/7/77/Swap_size.png/375px-Swap_size.png)](//wiki.manjaro.org/index.php?title=File:Swap_size.png)

[](//wiki.manjaro.org/index.php?title=File:Swap_size.png "Enlarge")

\
Now, enter a size for your *swap* partition. The recommended size for the swap partition is the same as your RAM. In this tutorial we are going to make a 1 GB swap partition, for that we will enter *1000* because *cfdisk* measures the size in MB.\

[![Swap type1.png](/images/thumb/6/6f/Swap_type1.png/375px-Swap_type1.png)](//wiki.manjaro.org/index.php?title=File:Swap_type1.png)

[](//wiki.manjaro.org/index.php?title=File:Swap_type1.png "Enlarge")

\
Because we\'ll use this partition for swap, we have to change it\'s type, so, when the *Type* option is highlighted, press ENTER.\

[![Swap type2.png](/images/thumb/6/68/Swap_type2.png/375px-Swap_type2.png)](//wiki.manjaro.org/index.php?title=File:Swap_type2.png)

[](//wiki.manjaro.org/index.php?title=File:Swap_type2.png "Enlarge")

\
You will be prompted with a list of file systems, for swap we\'ll have to enter *82*, we\'ll confirm by pressing ENTER.\

[![Root new.png](/images/thumb/4/49/Root_new.png/375px-Root_new.png)](//wiki.manjaro.org/index.php?title=File:Root_new.png)

[](//wiki.manjaro.org/index.php?title=File:Root_new.png "Enlarge")

\
After that, we are going to create a *root* (/) partition. Here\'s where the Operating System is going to be installed. Again, use your UP/DOWN keys to select the *Free Space* option, press ENTER to confirm. Using your arrow keys, choose *new* from the options at the bottom then press ENTER.\

[![Root size.png](/images/thumb/5/50/Root_size.png/375px-Root_size.png)](//wiki.manjaro.org/index.php?title=File:Root_size.png)

[](//wiki.manjaro.org/index.php?title=File:Root_size.png "Enlarge")

\
Enter the size in MB for your *root* partition. The recommended size for the *root* partition would be 4 GB or more and confirm it by pressing the ENTER key.\

[![Part write.png](/images/thumb/9/96/Part_write.png/375px-Part_write.png)](//wiki.manjaro.org/index.php?title=File:Part_write.png)

[](//wiki.manjaro.org/index.php?title=File:Part_write.png "Enlarge")

\
After that, you\'ll be prompted with your new partition scheme. To continue, use your arrow keys and select the *Write* option at the bottom and press ENTER, this will apply the changes we\'ve made so far.\

[![Part quit.png](/images/thumb/7/72/Part_quit.png/375px-Part_quit.png)](//wiki.manjaro.org/index.php?title=File:Part_quit.png)

[](//wiki.manjaro.org/index.php?title=File:Part_quit.png "Enlarge")

\
That being done, use your arrow keys and select the *Quit* option and press ENTER to exit *cfdisk*.\

\

## [Finalising the Disk Preparation]

[![Part done.png](/images/thumb/d/d2/Part_done.png/375px-Part_done.png)](//wiki.manjaro.org/index.php?title=File:Part_done.png)

[](//wiki.manjaro.org/index.php?title=File:Part_done.png "Enlarge")

\
Now, hit ENTER on the *Done* option.\

[![Prompt ok.png](/images/thumb/7/7f/Prompt_ok.png/375px-Prompt_ok.png)](//wiki.manjaro.org/index.php?title=File:Prompt_ok.png)

[](//wiki.manjaro.org/index.php?title=File:Prompt_ok.png "Enlarge")

\
Press ENTER again, when you get prompted with some information about what\'s coming next.\

[![Disk list.png](/images/thumb/b/bd/Disk_list.png/375px-Disk_list.png)](//wiki.manjaro.org/index.php?title=File:Disk_list.png)

[](//wiki.manjaro.org/index.php?title=File:Disk_list.png "Enlarge")

\
You will be prompted with a list of available drives, choose the one you\'ve partitioned earlier, then press ENTER.\

[![Choose swap.png](/images/thumb/c/cf/Choose_swap.png/375px-Choose_swap.png)](//wiki.manjaro.org/index.php?title=File:Choose_swap.png)

[](//wiki.manjaro.org/index.php?title=File:Choose_swap.png "Enlarge")

\
You will now have to select the swap partition. In this case it\'s */dev/sda2*. Use your arrow keys and highlight your previously created swap partition and press ENTER.\

[![Format swap.png](/images/thumb/e/e4/Format_swap.png/375px-Format_swap.png)](//wiki.manjaro.org/index.php?title=File:Format_swap.png)

[](//wiki.manjaro.org/index.php?title=File:Format_swap.png "Enlarge")

\
When getting prompted for formatting the swap partition, choose *Yes* and hit ENTER.

**Warning**

------------------------------------------------------------------------

This will format the partition, the changes cannot be reverted.

\

[![Choose root.png](/images/thumb/e/e6/Choose_root.png/375px-Choose_root.png)](//wiki.manjaro.org/index.php?title=File:Choose_root.png)

[](//wiki.manjaro.org/index.php?title=File:Choose_root.png "Enlarge")

\
You will now have to select the *root* ( / ) partition. In this particular case it\'s */dev/sda3*.\

[![Root fs.png](/images/thumb/b/b4/Root_fs.png/375px-Root_fs.png)](//wiki.manjaro.org/index.php?title=File:Root_fs.png)

[](//wiki.manjaro.org/index.php?title=File:Root_fs.png "Enlarge")

\
You\'ll be prompted with a list of file systems, choose one of them, preferably EXT4 and hit ENTER.\

[![Format root.png](/images/thumb/f/f3/Format_root.png/375px-Format_root.png)](//wiki.manjaro.org/index.php?title=File:Format_root.png)

[](//wiki.manjaro.org/index.php?title=File:Format_root.png "Enlarge")

\
Choose *Yes* when prompted to format the partition.\

[![Boot prompt.png](/images/thumb/0/04/Boot_prompt.png/375px-Boot_prompt.png)](//wiki.manjaro.org/index.php?title=File:Boot_prompt.png)

[](//wiki.manjaro.org/index.php?title=File:Boot_prompt.png "Enlarge")

\
There will be an option to mount static partitions at boot. Here you\'ll select the *boot* partition you\'ve created earlier.\

[![Boot fs.png](/images/thumb/6/6b/Boot_fs.png/375px-Boot_fs.png)](//wiki.manjaro.org/index.php?title=File:Boot_fs.png)

[](//wiki.manjaro.org/index.php?title=File:Boot_fs.png "Enlarge")

\
Now, you will have to select a file system for you *boot* partition. The EXT2 file system is recommended but not necessary.\

[![Boot mount.png](/images/thumb/d/d0/Boot_mount.png/375px-Boot_mount.png)](//wiki.manjaro.org/index.php?title=File:Boot_mount.png)

[](//wiki.manjaro.org/index.php?title=File:Boot_mount.png "Enlarge")

\
Set the mount point to */boot* then hit ENTER.\

[![Format boot.png](/images/thumb/e/e6/Format_boot.png/375px-Format_boot.png)](//wiki.manjaro.org/index.php?title=File:Format_boot.png)

[](//wiki.manjaro.org/index.php?title=File:Format_boot.png "Enlarge")

\
Select *Yes* and press ENTER when prompted for formatting.\

[![Additional boot.png](/images/thumb/8/8c/Additional_boot.png/375px-Additional_boot.png)](//wiki.manjaro.org/index.php?title=File:Additional_boot.png)

[](//wiki.manjaro.org/index.php?title=File:Additional_boot.png "Enlarge")

\
You will be able to mount other partitions at boot up. It\'s very useful in case you have a *home* partition for example. Otherwise, select *Done* and hit ENTER.\

[![Final prompt.png](/images/thumb/1/1c/Final_prompt.png/375px-Final_prompt.png)](//wiki.manjaro.org/index.php?title=File:Final_prompt.png)

[](//wiki.manjaro.org/index.php?title=File:Final_prompt.png "Enlarge")

\
An informational window will be prompted. Here you will be able to see info about your previously created partitions, including the mount points and types. Hit ENTER if you want to continue. Note: This will write the changes to your Hard Drive. The process if irreversible.\

[![Installer format.png](/images/thumb/8/8b/Installer_format.png/375px-Installer_format.png)](//wiki.manjaro.org/index.php?title=File:Installer_format.png)

[](//wiki.manjaro.org/index.php?title=File:Installer_format.png "Enlarge")

\
If you chose to continue (selected *Yes*), the installer will format and set mount points for your partitions.\

[![Part success.png](/images/thumb/3/3f/Part_success.png/375px-Part_success.png)](//wiki.manjaro.org/index.php?title=File:Part_success.png)

[](//wiki.manjaro.org/index.php?title=File:Part_success.png "Enlarge")

\
The process will take just a few seconds, depending on your hardware. Press ENTER when prompted with the success message.\

[![Main menu.png](/images/thumb/4/47/Main_menu.png/375px-Main_menu.png)](//wiki.manjaro.org/index.php?title=File:Main_menu.png)

[](//wiki.manjaro.org/index.php?title=File:Main_menu.png "Enlarge")

\
Now, we\'re done setting up the partitions. Use your arrow keys and highlight *Main menu*, then press ENTER.\

\

# [See Also]

-   **[Installation Guides](//wiki.manjaro.org/index.php?title=Installation_Guides "Installation Guides")**