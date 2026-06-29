# Help / C / Index

Manual


        Project


       is the GNOME Partition Editor for creating,
      reorganizing, and deleting disk partitions.
       enables you to change the partition organization while preserving
      the partition contents.


       2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017
       Curtis Gedak


       2014, 2015, 2017, 2018, 2023
       Mike Fleetwood


       2009
       ME-THE-TRANSLATOR (Latin translation)

-->


      Permission is granted to copy, distribute and/or modify this document
      under the terms of the GNU Free Documentation License, Version 1.2
      or any later version published by the Free Software Foundation;
      with no Invariant Sections, no Front-Cover Texts, and no Back-Cover
      Texts.  You can find a copy of the GFDL at this
       link  or at

      or in the file COPYING-DOCS distributed with this manual.


         Curtis
         Gedak

            Project

             gedakc@users.sf.net


         Mike
         Fleetwood

            Project

             mike.fleetwood@googlemail.com


         Latin
         Translator 1

           Latin Translation Team
             translator@gnome.org

         Latin translation

-->


          Manual V1.13
         September 2023


Mike Fleetwood


 Project


Describes version 1.6.0 of


          Manual V1.12
         May 2018


Mike Fleetwood


 Project


Describes version 0.31.0 of


          Manual V1.11
         September 2017


Curtis Gedak & Mike Fleetwood


 Project


Describes version 0.29.0 of


          Manual V1.10
         January 2017


Curtis Gedak & Mike Fleetwood


 Project


Describes version 0.28.0 of


          Manual V1.9
         March 2015


Curtis Gedak & Mike Fleetwood


 Project


Describes version 0.22.0 of


          Manual V1.8
         September 2014


Curtis Gedak


 Project


Describes version 0.20.0 of


          Manual V1.7
         February 2014


Curtis Gedak


 Project


Describes version 0.18.0 of


          Manual V1.6
         December 2013


Curtis Gedak


 Project


Describes version 0.17.0 of


          Manual V1.5
         September 2013


Curtis Gedak


 Project


Describes version 0.16.2 of


          Manual V1.4
         February 2012


Curtis Gedak


 Project


Describes version 0.12.0 of


          Manual V1.3
         January 2011


Curtis Gedak


 Project


Describes version 0.8.0 of


          Manual V1.2
         June 2010


Curtis Gedak


 Project


Describes version 0.6.0 of


          Manual V1.1
         July 2009


Curtis Gedak


 Project


Describes version 0.4.6 of


          Manual V1.0
         January 2009


Curtis Gedak


 Project


Describes version 0.4.2 of


          Manual V0.3.9
         September 2008


Curtis Gedak


 Project


Describes version 0.3.9 of


    This manual describes version  of


Feedback


      To report a bug or make a suggestion regarding the
         application or this manual,
      follow the directions at
       .


Introduction


    The    application is the GNOME Partition
    Editor for creating, reorganizing, and deleting disk partitions.


    A disk device can be subdivided into one or more partitions.
    The    application enables you to
    change the partition organization on a disk device while
    preserving the contents of the partition.


    With    you can accomplish the following
    tasks:


          Create a partition table on a disk device.


          Enable and disable partition flags such as boot and hidden.


          Perform actions with partitions such as create, delete,
          resize, move, check, label, copy, and paste.


      Editing partitions has the potential to cause LOSS of DATA.


      The    application is
      designed to enable you to edit partitions while
      reducing the risk of data loss.
      The application is carefully tested and is used
      by the  project team.
      However, loss of data might occur due to software bugs,
      hardware problems, or power failure.


      You can help to reduce the risk of data loss by
      not mounting or unmounting partitions outside of
      the    application while
         is running.


      You are advised to BACKUP your DATA before using
      the    application.  This is
      especially true for encrypted data where all of the data can
      become permanently inaccessible after a failure.  Please refer to
       The Cryptsetup FAQ
      for backup and recovery advice of encrypted data.


Getting Started


Starting


      You can start    in the following ways:


 Applications  menu


            Choose   System Tools  GParted Partition Editor  .


Command line


            Execute the following command:


      On startup,    will scan your
      computer for disk devices.


The  Window


      When you start   , the following
      window is displayed:


 Window


               Shows  main window.


      The    window contains the following
      elements:


Menubar


            The menus on the menubar contain all of the commands you need
            to work with disk devices and partitions in
              .


Toolbar


            The toolbar contains a subset of the commands that you can
            access from the menubar.


Graphic Display Area


            The graphic display area contains the visual representation
            of the partitions on the selected disk device.


Text Display Area


            The text display area contains the text list
            of the partitions on the selected disk device.


Statusbar


            The statusbar displays information about current
               activity or the
            number of operations pending.


Device Information Pane


            The device information pane displays details about the selected
            disk device.


            By default the device information pane is not shown.
            To show the device information pane, choose
              View  Device Information  .


Pending Operations Pane


            The pending operations pane displays the current list of
            partition operations in the queue.


            By default the pending operations pane is not shown when there
            are 0 pending operations.
            To show the pending operations pane, choose
              View  Pending Operations  .


      When you left-click in either display area, you select a partition
      to use for partition editing actions.


      When you right-click in either display area, the application displays
      a popup menu.
      The popup menu contains the most common partition editing actions.


Like other GNOME applications, actions in
         can be performed in several ways:
      with the menu, with the toolbar, or with shortcut keys.


Running  from a Command Line


      You can run    from a command line
      and specify one or more disk devices.


      To work with multiple disk devices from a command line, type the following
      command, then press  Enter :


 $

/path-to-your-device1 /path-to-your-device2


Viewing File System Support


      To view the actions supported on file systems, choose:
        View  File System Support  .
      The application displays the  File System Support
      dialog.


      If you have installed software while
         is running,
      click  Rescan For Supported Actions
      to refresh the chart.
      The application refreshes the display of the chart.


      To close the  File System Support  dialog,
      click  Close .


Working with Devices


Selecting a Device


      To select a disk device, choose:
        GParted  Devices
      and select a device from the list.
      The application displays the device partition layout in the
         window.


Viewing Device Information


        To view information about a disk device:


            Select a disk device.
            See  .


            Select:
              View  Device Information  .
            The application opens a side pane in the
               window
            and displays information about the device.


      To close the  Device Information  side pane,
      deselect:
        View  Device Information  .


Refreshing All Devices


      To refresh all disk devices, choose:
        GParted  Refresh Devices  .
      The application rescans all the disk devices and refreshes the device
      partition layout in the    window.


Creating a New Partition Table


      To create a new partition table on a disk device:


            Select a disk device.
            See  .


            Choose:
              Device  Create Partition Table  .
            The application displays a
             Create partition table on
/path-to-device

            dialog.


            Optionally select a different partition table type from the
            list.


              The default partition table type is
               msdos  for disks smaller than 2
              Tebibytes in size (assuming a 512 byte sector size) and
               gpt  for disks 2 Tebibytes and
              larger.


              See   for
               msdos  partition table
              limitations.


              To use a disk without a partition table, choose
               loop  to create a virtual
              partition that spans the disk.  Then format to the
              desired file system.


              See   to format
              a virtual partition with a file system.


              Many operating systems recognize
               gpt  and
               msdos  partition tables, but
              do not recognize all types of file systems.  This lack
              of file system recognition means that using a disk
              without a partition table involves more risk.  For
              example, some operating systems might prompt to format an
              unpartitioned disk if the file system is not recognized.


            Click  Apply  to create the new partition table.
            The application writes the new partition table to the disk device.
            The application refreshes the device partition layout in the
               window.


        WARNING:  This will ERASE ALL DATA on the ENTIRE DISK DEVICE.


        If you accidentally overwrite your partition table, see
         .


Working with Partitions


Basic Partition Actions


      These actions will not alter partitions on your disk device.


Selecting a Partition


        To select a partition, use one of the following:


              Click on a partition in the graphic display area.


              Click on a partition in the text display area.


        The application highlights the partition in both the graphic
        display area and the text display area in the
           window.


          Partition operations such as delete, move, copy, format,
          check, label, and often resize require the partition to be
          unmounted.
          See  .


Selecting Unallocated Space


        To select unallocated space, use one of the following:


              Click on  unallocated  in the graphic display area.


              Click on  unallocated  in the text display area.


        The application highlights the unallocated space in both the graphic
        display area and the text display area in the
           window.


          If you do not have any disk devices with unallocated space,
          you might try the following:


              Add a new disk device to your computer.


              Shrink a partition that contains unused space.
              See  .


Viewing Partition Information


        To view information about a partition:


              Select a partition.
              See  .


              Choose:
                Partition  Information  .
              The application opens an  Information about

/path-to-partition
  dialog.


        To close the  Information about

/path-to-partition
  dialog,
        click  Close .


Mounting a Partition


        To mount a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition  Mount
              and select a mount point from the list.
              The application mounts the partition on the mount point and
              refreshes the device partition layout in the
                 window.


          If
            Partition  Mount
          is not visible, then
          does not know where the partition should be mounted.


Unmounting a Partition


        To unmount a partition:


              Select a mounted partition.
              See  .


              Choose:
                Partition  Unmount  .
              The application unmounts the partition from the mount point and
              refreshes the device partition layout in the
                 window.


          If
            Partition  Unmount
          does not succeed, then the partition is probably in use.


          To have all partitions unmounted and available for
          partition editing actions, boot from a Live CD and
          use   .
          See


Opening an Encrypted Partition


        To open a LUKS encrypted partition:


              Select a closed LUKS encrypted partition.
              See  .


              Choose:
                Partition  Open Encryption  .


              If    doesn't yet know the
              LUKS Passphrase it will open a  LUKS Passphrase

/path-to-partition

              dialog.  Type the LUKS Passphrase into the
               Passphrase  text box and click
               Unlock .


              The application opens the encrypted partition and
              refreshes the device partition layout in the
                 window.


             remembers each LUKS
          Passphrase in the computer's memory for as long as it is
          running.  This is so that it doesn't have to prompt when
          reopening the same encrypted partition again.  When
             is closed all remembered LUKS
          Passphrases are cleared from memory and forgotten.


Closing an Encrypted Partition


        To close a LUKS encrypted partition:


              Select an unmounted and LUKS encrypted partition.
              See  .


              Choose:
                Partition  Close Encryption  .
              The application closes the LUKS encryption and refreshes
              the device partition layout in the
                 window.


Intermediate Partition Actions


      These actions will alter partitions on your disk device.
      These actions will not modify the start or end boundaries
      of your existing partitions.


Creating a New Partition


        To create a new partition:


              Select an unallocated space on the disk device.
              See  .


              Choose:
                Partition  New  .
              The application displays the  Create new Partition  dialog.


              Specify the size and the location for the partition.
              See  .


              Specify the alignment for the partition.
              See  .


              Specify the type of partition.
              See  .


              Specify the name of the partition when the field is
              enabled.
              See  .


              Specify the type of file system for the partition.
              See  .


              Specify the label of the file system for the partition.
              See  .


              Click  Add  to add the create partition
              operation to the operation queue.
              The application displays the create partition operation
              in the  Pending Operations  pane
              in the    window.


Deleting a Partition


        To delete a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition  Delete  .
              The application displays the delete partition operation in
              the  Pending Operations  pane.


          If you delete a logical partition, then all existing logical
          partitions after the deleted logical partition will
          experience changes in device names.


          For example, an extended partition contains four logical
          partitions A, B, C, and D.  These logical partitions are accessed by the
          operating system as follows:


              Partition A as /dev/sda5.


              Partition B as /dev/sda6.


              Partition C as /dev/sda7.


              Partition D as /dev/sda8.


          If partition B is deleted, then the remaining logical
          partitions will be accessed by the operating system as follows:


              Partition A as /dev/sda5.


              Partition C as /dev/sda6.  Note the change in device name.


              Partition D as /dev/sda7.  Note the change in device name.


          Changes in a device name can cause problems if a
          partition is mounted using a device name.
          You can avoid the problem by using the file system label or
          Universally Unique Identifier (UUID) of
          the partition when mounting the partition.


          Changes in a device name might adversely affect the
          following files:


                /etc/fstab - Contains a list of file systems to mount.


                /boot/grub/menu.lst - Contains operating system boot
                instructions for the  grub
                boot loader.


          Disks with  loop  or
           none  partition tables do not
          contain a partition table, and do not contain partitions.  A
          file system on a disk without a partition table is
          represented in  by a virtual partition.


          To delete the file system and virtual partition, choose
          format to  cleared .


          See  .


Naming a Partition


          Naming of partitions is only available with GUID partition
          tables (GPT).


          Also see  .


        To set a name of a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition
               Name Partition  .
              The application opens a  Set partition name on

/path-to-partition
  dialog.


              Type a partition name in the  Name  text box.


              Click  OK .
              The application displays the set partition name operation
              in the  Operations Pending  pane.


Formatting a Partition


        To format a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition  Format to  ,
              and select a type of file system from the list.
              The application displays the format partition operation
              in the  Operations Pending  pane.


              See
              for the meaning of the  cleared
              file system type.


Setting a Partition File System Label


        To set a label or a volume name of a file system in a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition
               Label File System  .
              The application opens a  Set file system label on

/path-to-partition
  dialog.


              Type a label name in the  Label  text box.


              Click  OK .
              The application displays the set file system label operation
              in the  Operations Pending  pane.


Changing a Partition UUID


        To change the Universally Unique Identifier (UUID) of a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition
               New UUID  .
              The application displays the set a new random UUID
              operation in the  Operations Pending
              pane.


                Changing the UUID might invalidate the Windows Product
                Activation key (WPA).


                On FAT and NTFS file systems, the Volume Serial Number
                is used as UUID.  Changing the Volume Serial
                Number on the Windows system partition, normally C:,
                might invalidate the WPA key.  An invalid WPA key will
                prevent login until you reactivate Windows.


                In an attempt to avoid invalidating the WPA key, on
                NTFS file systems only half of the UUID is set to a
                new random value. On FAT file systems, such a precaution
                is not possible.


                The WPA key should not be affected by changing the
                UUID of data partitions or removable media partitions.
                In rare cases, a partition that is present
                at boot time might be an exception to this rule.


                Changing the UUID when there is no need to do so might
                cause a GNU/Linux system to fail to boot, or to fail
                to mount a file system.


                Changing the UUID is only required after copying a
                partition.  The UUID change is needed to prevent
                duplicate UUIDs when both the source and the copy of
                the partition are used on the same computer.


                If boot or mount problems occur you might need to edit
                configuration files, such as /etc/fstab, and
                regenerate the grub menu to ensure that the correct
                UUID is specified.


Specifying Partition Details


        Specifying partition details is useful when performing actions
        such as create, resize, and move.


Specifying Partition Size and Location


          To specify the size and the location of the partition,
          use one or a combination of the following:


                Click-and-hold the arrow at either end of the graphic area.
                Drag the arrow left or right within the display range.


                Click-and-hold the middle of the partition in the graphic area.
                Drag the partition left or right within the display range.


                Click the spin button arrows, or type numeric values
                to adjust the following fields:


                       Free Space Preceding


                       New Size


                       Free Space Following


          The application refreshes both the graphic area
          and the numbers beside the three field labels.


Specifying Partition Alignment


          To specify the alignment of the partition, click the
           Align to  arrow button, and select from the list.


              Use  MiB  alignment for modern
              operating systems.  This setting aligns partitions to
              start and end on precise mebibyte (1,048,576 byte)
              boundaries.  MiB alignment provides enhanced performance
              when used with RAID systems and with Solid State Drives,
              such as USB flash drives.


              Use  Cylinder  alignment to maintain
              compatibility with operating systems released before the
              year 2000, such as DOS.  This setting aligns partitions
              to start and end on disk cylinder boundaries.


                The Cylinder/Head/Sector values reported by modern
                disk devices no longer have a direct physical
                relationship to the data stored on the disk device.
                Hence it is no longer valid to use this alignment
                setting to achieve enhanced performance.


              Use  None  only if you have an
              in-depth knowledge of disk structure, partition tables,
              and boot records.  This setting places partition
              boundaries relative to the end of any immediately
              preceding partition on the disk device.  This setting
              is not guaranteed to reserve or respect space required
              for boot records.


Specifying Partition Type


          To specify the partition type, click the
           Create as  arrow button, and select from the list.


            The msdos partition table limits partitions as follows:


                  Maximum of 4 primary partitions.


                  Maximum of 3 primary partitions, and 1 extended partition.


                  The extended partition can contain multiple logical
                  partitions.
                  Some GNU/Linux distributions support accessing at most
                  15 partitions on a disk device.


                  Maximum size of a partition is 2 Tebibytes using
                  a sector size of 512 bytes.  The partition must also
                  start within the first 2 Tebibytes of the disk device.


            Primary partitions provide better data recoverability
            because the partition boundaries are stored at known
            locations on the disk device.


Specifying Partition Name


            Naming of partitions is only available with GUID partition
            tables (GPT).  Therefore the field is only enabled on disk
            devices partitioned using GPT.


            Also see  .


          To specify the partition name, type the name in the
           Partition name  text box.


Specifying Partition File System


          To specify the type of file system for the partition, click the
           File System  arrow button, and select from the list.


            Examples of uses for some file systems are as follows:


                   ext2 ,
                   ext3  and
                   ext4  file systems can be
                  used for installing GNU/Linux, and for data.


                   linux-swap  can be used with
                  GNU/Linux to increase the virtual memory of your
                  computer.


                   fat16  and
                   fat32  file systems can be
                  used to share data between free and commercial
                  operating systems.


                   cleared  can be used to
                  clear any existing file system signatures and ensure
                  that the partition is recognised as empty.


                   unformatted  can be used to
                  just create a partition without writing a file system.


Specifying Partition File System Label


          To specify the file system label in the partition, also known
          as a volume label, type a label name in the
           Label  text box.


            File system labels can be used to help you remember what is
            stored in the partition.


            Unique labels can be used to mount file systems with the
            GNU/Linux operating system.


Advanced Partition Actions


      These actions will alter partitions on your disk device.
      These actions might modify the start or end boundaries
      of your existing partitions.
      These actions might cause operating systems to fail to boot.


Resizing a Partition


        Resizing and moving a partition can be performed by a single
           operation.


        To resize a partition:


              Select a partition.
              See  .


                Unmounted or inactive partitions enable the most
                resize options.


                Support is available for online resize of some
                mounted or otherwise active partitions.  However this
                support is often limited to grow only.


              Choose:
                Partition  Resize/Move  .
              The application displays the
               Resize/Move
/path-to-partition

              dialog.


              Adjust the size of the partition.
              See  .


                If you do not want the start of an existing partition
                to move, then do not change the  free space
                preceding  value.  If the partition is
                mounted or otherwise active, then you will not be able
                to change the  free space
                preceding  value.


              Specify the alignment of the partition.
              See  .


              Click  Resize/Move .
              The application displays the resize/move partition operation
              in the  Pending Operations  pane.


              Examine the operation that was added to the
               Pending Operations  pane.


              If the operation involves a move step, then
              consider the following:


                    A move step might take a long time
                    to complete.


                    If the partition is an operating system boot partition,
                    then a move step might cause the operating system
                    to fail to boot.


              If you are not prepared to wait
              or to fix potential operating system boot problems,
              then you might want to undo the operation.
              See  .


          To grow or move a partition, unallocated space must be available adjacent
          to the partition.


          If you are growing a logical partition, then the unallocated space
          must be within the extended partition.


          If you are growing a primary partition, then the unallocated space
          must not be within the extended partition.


          You can move unallocated space to be inside or outside of the
          extended partition by resizing the extended partition boundaries.


          A LUKS encrypted partition and the file system within can only
          be resized when the encryption mapping is open.


          To improve the ability to shrink NTFS partitions, you
          might consider one or more of the following:


                Defragment the file system.


                Booting into Safe Mode with the
                commercial operating system that uses NTFS
                can improve the ability to defragment
                the file system.
                To enter Safe Mode press  F8
                while your computer is booting
                the operating system.


                Check the partition for errors with the following command:

 C:>
chkdsk
 /f /r

                Remember to reboot back into the commercial operating system
                that uses NTFS to allow the
chkdsk
 command
                to execute.


                Temporarily disable the paging file.
                The paging file occupies a fixed location
                in the partition that the defragmentation
                process is unable to move.


                Temporarily move large files to another partition
                or disk device.  Large files are defined as greater
                than a few hundred Megabytes (MB).


                Ensure a proper shut down of the commercial operating
                system that uses NTFS before you resize the NTFS
                partition


                Leave at least 10 percent unused space in the NTFS partition.
                If you shrink the partition too much,
                then the commercial operating system might have difficulty
                functioning properly.


                Reboot twice into the commercial operating system that
                uses NTFS after shrinking the NTFS partition.


Moving a Partition


        Moving and resizing a partition can be performed by a single
           operation.


        To move a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition  Resize/Move  .
              The application displays the
               Resize/Move
/path-to-partition

              dialog.


              Adjust the location of the partition.
              See  .


              Specify the alignment of the partition.
              See  .


              Click  Resize/Move .
              The application displays the resize/move partition operation
              in the  Pending Operations  pane.


          If the partition is an operating system boot partition,
          then the operating system might not boot after the move
          operation is applied.


          If the operating system fails to boot, see
           .


          A LUKS encrypted partition can only be moved when the
          encryption mapping is closed.


Copying and Pasting a Partition


        To copy a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition  Copy  .
              The application marks the partition as the
              source partition.


        To Paste a partition:


              Select an unallocated space on a disk device.
              See  .


              Choose:
                Partition  Paste  .
              The application displays the
               Paste
/path-to-partition

              dialog.


              If you want you can adjust the size and location of the partition.
              See  .


              If you want you can specify the alignment of partition.
              See  .


              Click  Paste .
              The application displays the copy partition operation
              in the  Pending Operations  pane.


          The copy of the partition has the same file system label
          and Universally Unique Identifier (UUID) as the source
          partition.
          This can cause a problem when booting, or when mount actions
          use the file system label or UUID to identify the partition.


          The problem is that the operating system will randomly
          select to mount either the source, or the copy of the
          partition.  For example, on the first mount action the
          source partition might be mounted.  On the next mount action
          the copy of the partition might be mounted.  Over time this
          random nature of partition mounting might make files seem to
          mysteriously appear or disappear depending upon which
          partition is mounted.  Random mounting of the source or the
          copy of the partition might also cause severe data
          corruption or loss.


          To avoid the problem you are advised to do one of the
          following:


                After you have queued or applied the copy operation:


                      Change the UUID of either the source, or the copy
                      of the partition.
                      See  .


                      If the file system label is not blank then change
                      the file system label of either the source, or the
                      copy of the partition.
                      See  .


                After you have applied the copy operation, delete or
                reformat the source partition.


                Use some other method to ensure that the source
                partition and the copy of the partition are not used
                on the same computer at the same time.  For example,
                if the copy of the partition is on a separate drive
                then remove the drive from the computer.


          The file system within a LUKS encrypted partition can only be
          copied when the encryption mapping is open.


          To prevent unintended decryption of data, pasting into
          unallocated space creating a new partition is not permitted.
          However a LUKS encrypted partition can be pasted into an
          existing open LUKS encrypted partition maintaining an
          encrypted, or pasted into a plain partition making an
          unencrypted copy of the file system.


Managing Partition Flags


        To manage partition flags:


              Select a partition.
              See  .


              Choose:
                Partition  Manage Flags  .
              The application opens a  Manage flags on

/path-to-partition
  dialog.


                    To enable a flag, select the check box beside the flag.
                    The application writes the enabled flag to the partition
                    and refreshes the  Manage flags on

/path-to-partition
  dialog.


                    To disable a flag, deselect the check box beside the flag.
                    The application writes the disabled flag to the partition
                    and refreshes the  Manage flags on

/path-to-partition
  dialog.


                 Manage Flags  is only
                available for disks with partition tables.  Disks with
                 loop  or
                 none  partition tables do
                not contain a partition table, and do not have
                partition flags.


                See
                to view the type of partition table.


        To close the  Manage flags on

/path-to-partition
  dialog,
        click  Close .


          A description of flags in an msdos partition table
          follows:


                Boot is used by some commercial operating system
                boot loaders.
                The boot flag indicates the partition is active
                or bootable.
                Only one partition on a disk device can be active.


                Diag is used to indicate the partition is used for
                diagnostics / recovery.


                ESP indicates an EFI System Partition used to boot
                computers with the Unified Extensible Firmware
                Interface (UEFI) class 2 that includes compatibility
                support for BIOS functions including the MBR partition
                structure.


                Hidden is used by some commercial operating systems.
                The hidden flag makes the partition invisible to the
                operating system.


                Irst identifies an Intel Rapid Start Technology
                partition.


                LBA is used by some commercial operating system
                boot loaders.
                The LBA flag indicates the partition should be
                accessed using Logical Block Addressing (LBA), instead
                of Cylinder-Head-Sector (CHS) addressing.


                LVM is used to indicate the partition is used by a
                Logical Volume Manager (LVM).


                Palo is used by the Precision Architecture -
                Reduced Instruction Set Computing (PA-RISC)
                boot loader, palo.


                Prep is used to indicate the boot partition
                on Power Performance Computing (PowerPC) hardware.


                RAID is used to indicate the partition is used in a
                Redundant Array of Inexpensive Disks (RAID).


          A description of flags in a gpt partition table follows:


                Atvrecv is used to indicate an Apple TV Recovery
                partition.


                BIOS_GRUB indicates a BIOS boot partition often used
                by the GRUB 2 boot loader.


                Boot is used by some commercial operating system
                boot loaders.
                The boot flag indicates the partition is active
                or bootable.
                Only one partition on a disk device can be active.


                Diag indicates the partition is used for diagnostics
                or recovery.


                ESP indicates an EFI System Partition used to boot
                computers with Extensible Firmware Interface (EFI)
                class 1 or Unified Extensible Firmware Interface
                (UEFI) class 2 or UEFI class 3.


                Hidden is used by some commercial operating systems.
                The hidden flag makes the partition invisible to the
                operating system.


                HP-service is used to indicate a Hewlett Packard
                service partition.


                Irst identifies an Intel Rapid Start Technology
                partition.


                Legacy_boot is used by some special purpose software
                to indicate the partition might be bootable.


                LVM indicates the partition is used by a Logical
                Volume Manager (LVM).


                Msftdata identifies partitions that contain Microsoft
                file systems such as NTFS or FAT.


                Msftres is used to indicate a Microsoft Reserved
                partition.


                Prep is used to indicate the boot partition
                on Power Performance Computing (PowerPC) hardware.


                RAID indicates the partition is used in a Redundant
                Array of Inexpensive Disks (RAID).


Checking a Partition


        Checking a partition will attempt to find and fix problems
        in the file system.
        Checking a partition will attempt to grow the file system
        to fill the partition.


        To check a partition:


              Select an unmounted partition.
              See  .


              Choose:
                Partition  Check  .
              The application displays the check partition operation
              in the  Pending Operations  pane.


Working with the Operation Queue


Undoing Last Operation


        To undo the last operation in the operation queue, choose:
          Edit  Undo Last Operation  .
        The application removes the last operation from the queue
        displayed in the  Pending Operations  pane.
        If there are no operations remaining in the queue,
        the application closes the
         Pending Operations  pane.


Clearing All Operations


        To clear all operations in the operation queue, choose:
          Edit  Clear All Operations  .
        The application removes all operations from the queue
        and closes the  Pending Operations  pane.


Applying All Operations


        To apply all operations:


              Choose:
                Edit  Apply All Operations  .
              The application displays an
               Apply operations to device  dialog.


                Editing partitions has the potential to cause LOSS of DATA.
                You are advised to backup your data before applying your
                partition editing operations.


              Click  Apply .
              The application displays an
               Applying pending operations  dialog.
              The application applies each pending operation
              in the order you created the operations.
              The application displays a status update when each
              operation is completed.


                    To view more information,
                    click  Details .
                    The application displays more details about operations.


                    To view more information about the steps in each operation,
                    click the arrow button beside each step.


                    To stop the operations while they are executing,
                    click  Cancel .
                    The application displays a disabled
                     Force Cancel (5)  button and
                    counts down for 5 seconds.


                       Cancel  instructs the
                      application to stop or roll back operations
                      as necessary to ensure data integrity.


                    If operations have not halted after 5 seconds the
                    application enables the  Force
                    Cancel  button.


                    To force the operations to stop, click
                     Force Cancel .
                    The application displays a warning dialog.


                    Click  Continue Operation  to
                    allow the roll back operations to complete, or
                    click  Cancel Operation  to
                    cancel the roll back operations.


                       Cancel Operation
                      terminates the safe roll back of operations and
                      might cause SEVERE file system damage and data
                      loss.  You are advised to click
                       Continue Operation  to
                      allow the roll back to complete.


                    When the application finishes performing operations,
                    the application displays the
                     Save Details  button and the
                     Close  button.


              If you want to save the details from applying all operations,
              then click  Save Details .
              The application displays a  Save Details
              dialog.


                    If you want to change the default file name,
                    then type a file name in the
                     Name  text box.


                    If you want to save the file in a folder
                    different than /root,
                    click  Browse for other folders .
                    The application displays a file system navigator.


                    Use the file system navigator to select a folder.


                    Click  Save  to save the file.
                    The application saves the details file.


                If you use    from a Live CD, then
                the root file system exists in RAM memory.  All files saved
                to the Live CD root file system will be lost when you shut down
                the computer.


                If you saved the  details to the Live CD root file system,
                then you need to copy the file to more permanent storage.
                Examples of more permanent storage are a hard disk drive
                or a USB flash memory drive.


              Click  Close .
              The application closes the
               Applying pending operations  dialog.
              The application rescans all the disk devices and refreshes the device
              partition layout in the    window.


Acquiring GParted on Live CD


    A Live CD is a Compact Disc that contains a bootable operating system.
    A Live CD enables you to boot your computer from the CD.


    Using    from a Live CD
    has the following advantages:


          You can edit all of your partitions
          because the partitions are not mounted.


          You can edit partitions on computers that
          do not have a bootable operating system.


    The    application is available on many
    Live CD distributions.


    You can download a Live CD image containing
       from the following web sites:


          GParted Live CD


          SystemRescue (also known as SystemRescueCD)


      The GParted Live CD image can be written to a USB flash drive.


      If your computer can boot from Universal Serial Bus (USB) then
      you might prefer to boot and use
         from a USB flash drive.


      To avoid wasting a blank CD when burning a CD image file,
      use the following tips:


          Ensure the checksum of the downloaded file matches
          the checksum posted on the download page.


          Be sure to burn the .iso file as an image to the blank CD.
          If you burn the .iso file as data to a blank CD then the
          CD will not boot in your computer.


Fixing Operating System Boot Problems


    Your computer might fail to boot an operating system
    when you perform one of the following actions:


          Delete a partition.


          Move a partition.


          Install another operating system and
          overwrite the Master Boot Record (MBR).


    Fortunately the failure to boot can be often be fixed.


    If your computer uses the GRUB boot loader,
    see
    to restore the ability to boot.


    If your computer does not use GRUB then you are advised to consult
    documentation for your boot loader to learn how to fix the
    problem.
    You might consult the
      FAQ ,
    or the
      forum .
    You might also search the Internet to learn how other people have
    solved similar problems.


Fixing GRUB boot problem


      The Grand Unified Boot loader (GRUB) is used by many GNU/Linux
      distributions.  To fix GRUB boot problems you start by
      determining which major version of GRUB was used.


      There are two major versions of GRUB:


            GRUB, also known as GRUB 2, covers versions 1.98 and
            higher.  GRUB 2 works with both GUID partition tables
            (GPT) and msdos partition tables.


            GRUB Legacy, traditionally known as GRUB, covers versions
            0.9x and earlier.  GRUB Legacy works with msdos partition
            tables only.


      GRUB 2 is used as the default boot loader in the following
      GNU/Linux distributions:


            CentOS 7 and higher


            Debian 6 (Squeeze) and higher


            Fedora 16 (Verne) and higher


            openSUSE 12.2 and higher


            Ubuntu 9.10 (Karmic Koala) and higher


      If you are unsure whether your computer uses GRUB 2 or GRUB
      Legacy, you might try searching for the answer on the Internet.


Restoring GRUB 2 Boot Loader


        Use the following steps to restore the GRUB 2 boot loader:


              Boot from Live media such as GParted Live or your
              GNU/Linux distribution image.  Open a terminal window.


              Determine which partition contains the / file system for
              your GNU/Linux distribution.


              Use GParted to list the partitions on your disk device.
              Look for a partition that contains your GNU/Linux / file
              system.  This Linux partition will likely use a file
              system such as ext2, ext3, ext4, or btrfs.


                If the / partition is on LVM then the Logical Volume
                Manager must be active.  LVM can be started with the
                command:

 #
vgchange
 -a y


                With LVM, the equivalent of a disk partition is a
                Logical Volume.  Logical Volumes can be listed with
                the command:

 #
lvscan


                If the / partition is on RAID, then the RAID must be
                active.  Linux Software RAID can be started with the
                command:

 #
mdadm
 --assemble --scan


              Create a mount point directory by entering (as root):

 #
mkdir
 /tmp/mydir


              Mount the / partition on the mount point directory.  For
              example assume the / file system is contained in the
              /dev/sda5 partition.  Enter (as root):

 #
mount

/dev/sda5
 /tmp/mydir


              If you have a separate /boot partition, for example at
              /dev/sda3, then an extra step is required.  Mount the
              /boot partition at /tmp/mydir/boot by entering (as
              root):

 #
mount

/dev/sda3
 /tmp/mydir/boot


                If you do not know whether you have a separate boot
                partition then you probably do not and can ignore this
                step.


              Prepare to change the root environment by entering (as
              root):

 #
mount
 --bind /dev /tmp/mydir/dev


 #
mount
 --bind /proc /tmp/mydir/proc


 #
mount
 --bind /sys /tmp/mydir/sys


              Change the root environment by entering (as root):

 #
chroot
 /tmp/mydir


              Reinstall GRUB 2 on the boot device.  Note that the
              device name is used and not the partition name.  For
              example, if the / partition is /dev/sda5 then the device
              is /dev/sda.


              For Debian, Ubuntu, and other offshoot GNU/Linux
              distributions, enter the command (as root):

 #
grub-install

/dev/sda


              For CentOS, Fedora, openSUSE and other offshoot
              GNU/Linux distributions, enter the command (as root):

 #
grub2-install

/dev/sda


              Exit the chroot environment by entering (as root):

 #
exit


              Reboot your computer.


Restoring GRUB Legacy Boot Loader


        Use the following steps to restore the GRUB Legacy boot
        loader:


              Boot from Live media such as your GNU/Linux distribution
              image.  Open a terminal window.


                The Live media must contain the GRUB Legacy boot
                loader.  If your GNU/Linux distribution uses GRUB
                Legacy, then the distribution Live media will also
                contain GRUB Legacy.


              Start the  grub  application
              from the command line (as root).

 #
grub


              Find where  grub  stage1 is
              located by using one of the following:


              If the /boot folder is stored in the / partition,
              use the command:

 grub>
find
 /boot/grub/stage1

              If the /boot folder is stored in a partition
              different than the / partition, use the command:

 grub>
find
 /grub/stage1


              The output from the
find
 command
              might look like the following:


(hd0,0)


              If more than one line is listed in the command output,
              you will need to decide which device you use for
               grub .


              Set the  grub  root device by
              specifying the device returned by the

find
 command.  This should be the
              partition containing the boot directory.

 grub>  root
(hd0,0)


              Reinstall the  grub  boot
              loader into the Master Boot Record (MBR) with:

 grub>  setup
(hd0)


              If you want to install the
               grub  boot loader into the
              boot sector of a partition, instead specify a partition
              with:

 grub>  setup
(hd0,0)


              Exit  grub .

 grub>  quit


              Reboot your computer.


Recovering Partition Tables


    If you accidentally overwrite your partition table, there is a chance
    that you might be able to recover it.


    The  testdisk  application is designed to help
    recover lost partitions.  For more information about
     testdisk , see
     .


    If no partitions are found, you have other options to try to rescue
    your data.  The  photorec  application is
    designed to help recover many different types of lost files.  For
    more information about  photorec , see
     .


    Both  testdisk  and
     photorec  applications are included on
    each Live CD listed in  .
