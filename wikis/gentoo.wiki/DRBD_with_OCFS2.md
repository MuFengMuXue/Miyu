** Warning**\
The ebuild sys-fs/ocfs2 was removed from main portage tree.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [USE flags]](#USE_flags)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [DRBD Configuration]](#DRBD_Configuration)
-   [[4] [OCFS2 Configuration]](#OCFS2_Configuration)
-   [[5] [DRBD Initialization and Setup]](#DRBD_Initialization_and_Setup)
-   [[6] [OCFS2 Setup]](#OCFS2_Setup)
    -   [[6.1] [Enable Dual-Primary Mode]](#Enable_Dual-Primary_Mode)
-   [[7] [Adding both DRBD and OCFS2 on system boot]](#Adding_both_DRBD_and_OCFS2_on_system_boot)
-   [[8] [Manual Split Brain Recovery]](#Manual_Split_Brain_Recovery)
    -   [[8.1] [Split Brain Victim, Choose a node upon which the changes will be discarded]](#Split_Brain_Victim.2C_Choose_a_node_upon_which_the_changes_will_be_discarded)
    -   [[8.2] [Split Brain Survivor, Choose The node upon which we have the latest version of files]](#Split_Brain_Survivor.2C_Choose_The_node_upon_which_we_have_the_latest_version_of_files)
    -   [[8.3] [Result]](#Result)
-   [[9] [See also]](#See_also)
-   [[10] [References]](#References)

## [Introduction]

This is a guide for DRBD with OCFS2.\
The tough part came with finding that Samba Active Directory (AD) Domain Controller (DC) sysvol is not being replicated between DC -- a current Samba4 known limitation.\

** Warning**\
Dropping the sysvol though is a bad idea. Without CTDB, files would corrupted when accessed twice simultaneously, however CTDB is not compatible with Samba AD.

** Warning**\
With this guide, the OCFS2 does not have a DLM, required by Corosync, cman, openais and pacemaker. I\'ve yet to have a proper configuration and thus the current way is improper. Also it will not run with a shared lock on CTDB.

Q: Why DRBD only is not enough\...\
There might be case in which there is multiple write access to the block device by multiple servers, thus without cluster files system we will have trouble on file locking etc. due to the fact that DRBD volumes are being mounted by two or more servers, so OCFS2 is selected for its performance and also its popularity.\

You can use always use other cluster files system.\

This guide covers only a two node, dual primary configuration. If you required more nodes, please read up on DRBD for more information.

** Warning**\
The Samba team does not suggest using this solution, so this is ***purely experimental***. But still, other DRBD + OCFS2 examples are available to assist in other configurations.\

## [Installation]

### [Kernel]

[KERNEL] **3.10.25-gentoo**

    File systems --->
        [*] OCFS2 file system support
        [*]   O2CB Kernelspace Clustering
        [*]   OCFS2 statistics
        [*]   OCFS2 logging support
        [ ]   OCFS2 expensive checks
        <*> Distributed Lock Manager (DLM)
    Device Drivers  --->
        [*] Block devices  --->
            [*]   DRBD Distributed Replicated Block Device support
            [ ]     DRBD fault injection

### [USE flags]

### [USE flags for] [sys-cluster/drbd-utils](https://packages.gentoo.org/packages/sys-cluster/drbd-utils) [[]] [mirror/replicate block-devices across a network-connection]

  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+udev`](https://packages.gentoo.org/useflags/+udev)           Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`pacemaker`](https://packages.gentoo.org/useflags/pacemaker)   Enable Pacemaker integration
  [`selinux`](https://packages.gentoo.org/useflags/selinux)       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`split-usr`](https://packages.gentoo.org/useflags/split-usr)   Enable behavior to support maintaining /bin, /lib\*, /sbin and /usr/sbin separately from /usr/bin and /usr/lib\*
  [`xen`](https://packages.gentoo.org/useflags/xen)               Enable Xen integration
  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 23:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Cannot load package information. Is the atom *sys-fs/ocfs2-tools* correct?

### [Emerge]

Install the following packages:

`root `[`#`]`emerge --ask sys-cluster/drbd-utils sys-fs/ocfs2-tools`

The DRBD 8.4 guide suggests the use of heartbeat and pacemaker, but I think that was just too complicated. You are welcome to try and add on an option with heartbeat and pacemaker.

## [DRBD Configuration]

We will now configure DRBD.

** Note**\
DRBD version check and prompt are a bit annoying as it will suggest you to upgrade every time you execute a command.

Please check the DRBD User's Guide Ver 8.4^[\[1\]](#cite_note-drbdManual-1)^ on their website it is well written with examples.

\
This is a Global DRBD configuration. It will need to change according to your DRBD need. Please check the on the manual for more info.

[FILE] **`/etc/drdb.d/global_common.conf`**

    global

    common

            startup

            options

            disk

            net
    }

** Note**\
DRBD manual doesn\'t recommended to set the allow-two-primaries option to yes until the initial resource synchronization has completed.

** Warning**\
By configuring auto-recovery policies, you are effectively configuring automatic data-loss! Be sure you understand the implications. - By DRBD Manual

Please create the files below.\
If you have multiple resource setup, you can do it one resource per files to avoid confusion.\

Below files is a 2 Node Resource example. Note on the Comment Part, they will need to be uncommented later when we enable dual primary.

[FILE] **`/etc/drdb.d/r0.res`Resource name r0 DRBD**

    resource r0
            startup
            on serverNode01
            on serverNode02
            net
    }

In plain English, we will use [/dev/sda5] on serverNode01 (IP 192.168.11.23) and [/dev/sda5] on serverNode02 (IP 192.168.11.27) to create a drbd node [/dev/drbd1] respectively on both server. Both drbd nodes will store the metadata internally.

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Name                              | Description                                                                                                               |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| resource r0                       | The DRBD resource named r0                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| on serverNode01\                  | The Server Name for each node for your reference.                                                                         |
| on serverNode01                   |                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| device /dev/drbd1;                | The device node which will be created by DRBD that need to be mounted.                                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| disk /dev/sda5;                   | The physical partition that DRBD will be using to store the information.                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| address 192.168.11.23:7789;\      | The server ip address for DRBD will be used to sync between all nodes, you will have to assign this ip to the interface.\ |
| address 192.168.11.27:7789;       |                                                                                                                           |
|                                   | Also DRBD does not support multiple ip address. Use Channel Bonding/Teaming like LACP.\                                   |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| meta-disk internal;               | This tells DRBD where to store the metadata; it can be external as well.                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+

## [OCFS2 Configuration]

We will now continue with OCFS2 setup.\
Unfortunately ocfs2 configuration doesn\'t include the cluster files example and thus you will need to copy the files below as an example.\
Please change as necessary to suit your needs:

[FILE] **`/etc/ocfs2/cluster.conf`Create this file (and directory)**

    cluster:
            node_count = 2
            name = ocfs2cluster

    node:
            number = 1
            cluster = ocfs2cluster
            ip_port = 7777
            ip_address = 192.168.11.23
            name = serverNode01

    node:
            number = 2
            cluster = ocfs2cluster
            ip_port = 7777
            ip_address = 192.168.11.27
            name = serverNode02

  ----------------------------------- --------------------------------------------------------------------
  Name                                Descriptions

  cluster:                            OCFS2 cluster declaration

  node_count = 2                      How many nodes do we have in this cluster?

  name = ocfs2cluster                 The ocfs2 cluster name

  node:                               The Node declaration

  number = 1\                         The node number, it must be different on all nodes
  number = 2

  cluster = ocfs2cluster              The name of the cluster

  ip_port = 7777                      The ocfs2 node service port, you can change it if you want to.

  ip_address = 192.168.11.23\         The ocfs2 node ip address. Please change this to your interface ip
  ip_address = 192.168.11.27

  name = serverNode01\                The node servername for your reference.
  name = serverNode02
  ----------------------------------- --------------------------------------------------------------------

Now it is time to change [/etc/conf.d/ocfs2] files. There are a lot of configurable parameters there but we will only make one change. `OCFS2_CLUSTER` and change it to ocfs2 cluster name.

[FILE] **`/etc/conf.d/ocfs2`Change OCFS2 Cluster Name**

    OCFS2_CLUSTER="ocfs2cluster"

It is also time we add the required mount to [/etc/fstab]. Please add the following.

[FILE] **`/etc/fstab`add the following**

    # Needed by ocfs2
    none                    /sys/kernel/config            configfs        defaults                                  0 0
    none                    /sys/kernel/dlm               ocfs2_dlmfs     defaults                                  0 0

    # Our DRBD and OCFS2 mount
    /dev/drbd1              /ocfs2cluster/                ocfs2            _netdev,nointr,user_xattr,acl            0 0

## [DRBD Initialization and Setup]

After we have all this.\
It is time to initial DRBD

** Note**\
Run this command on both node.

`root `[`#`]`drbdadm create-md r0`

    DRBD module version: 8.4.3
       userland version: 8.4.2
    you should upgrade your drbd tools!
    Writing meta data...
    initializing activity log
    NOT initializing bitmap
    New drbd meta data block successfully created.
    success

Let us up the DRBD devices.

** Note**\
Run this command on both node.

`root `[`#`]`drbdadm up r0`

    DRBD module version: 8.4.3
       userland version: 8.4.2
    you should upgrade your drbd tools!

When both nodes are up we can check on the BRDB status.

`root `[`#`]`cat /proc/drbd`

    version: 8.4.3 (api:1/proto:86-101)
    built-in

     1: cs:WFConnection ro:Secondary/Unknown ds:Inconsistent/DUnknown C r----s
        ns:0 nr:0 dw:0 dr:0 al:0 bm:0 lo:0 pe:0 ua:0 ap:0 ep:1 wo:f oos:2026376

When Both node is up, we will see something\...\
The **Secondary/*Unknown*** become **Secondary/*Secondary***.

`root `[`#`]`cat /proc/drbd`

    version: 8.4.3 (api:1/proto:86-101)
    built-in

     1: cs:Connected ro:Secondary/Secondary ds:Inconsistent/Inconsistent C r-----
        ns:0 nr:0 dw:0 dr:0 al:0 bm:0 lo:0 pe:0 ua:0 ap:0 ep:1 wo:f oos:2026376

We now have the DRBD device.

** Note**\
I do have a question, should we format this partition to OCFS2 at this time then only sync it or not?\
Please try and let me know.

Lets start to synchronize both DRBD nodes by making it primary\

** Note**\
We should only run this command on one node only

`root `[`#`]`drbdadm primary --force r0`

    DRBD module version: 8.4.3
       userland version: 8.4.2
    you should upgrade your drbd tools!

Let us check the synchronization status

`root `[`#`]`cat /proc/drbd`

    version: 8.4.3 (api:1/proto:86-101)
    built-in

     1: cs:SyncSource ro:Primary/Secondary ds:UpToDate/Inconsistent C r---n-
        ns:313236 nr:0 dw:0 dr:315032 al:0 bm:19 lo:5 pe:2 ua:7 ap:0 ep:1 wo:f oos:1715080
            [==>.................] sync'ed: 15.6% (1715080/2026376)K
            finish: 0:00:44 speed: 38,912 (38,912) K/sec

Please wait until it is done.

`root `[`#`]`cat /proc/drbd`

    version: 8.4.3 (api:1/proto:86-101)
    built-in

     1: cs:Connected ro:Primary/Secondary ds:UpToDate/UpToDate C r-----
        ns:2026376 nr:0 dw:0 dr:2027040 al:0 bm:124 lo:0 pe:0 ua:0 ap:0 ep:1 wo:f oos:0

Let make 2nd Node primary\

** Note**\
We should only run this command the 2nd node only

`root `[`#`]`drbdadm primary --force r0`

    DRBD module version: 8.4.3
       userland version: 8.4.2
    you should upgrade your drbd tools!

Let start the DRBD services

`root `[`#`]`/etc/init.d/drbd start `

Yes, our DRBD cluster are done. Now lets continue to the OCFS2 Setup

## [OCFS2 Setup]

The 1st things that we need to do are to mount the required kernel config and dlm that is needed by OCFS2. Since that we already modified the [/etc/fstab]. You can simple follow the command below.

`root `[`#`]`mount /sys/kernel/config `

`root `[`#`]`mount /sys/kernel/dlm `

We should now start the OCFS2 Cluster

`root `[`#`]`/etc/init.d/ocfs2 start`

     * Starting OCFS2 cluster
     *  - ocfs2cluster...

Now let us make the DRBD cluster run OCFS2

** Note**\
You should create more node than what you need on OCFS in case when more server need to access this OCFS2 cluster.

`root `[`#`]`mkfs.ocfs2 -N 8 -L "ocfs2cluster" /dev/drbd1`

    mkfs.ocfs2 1.8.2
    Cluster stack: classic o2cb
    Label: ocfs2cluster
    Features: sparse extended-slotmap backup-super unwritten inline-data strict-journal-super xattr indexed-dirs refcount discontig-bg
    Block size: 4096 (12 bits)
    Cluster size: 4096 (12 bits)
    Volume size: 2075009024 (506594 clusters) (506594 blocks)
    Cluster groups: 16 (tail covers 22754 clusters, rest cover 32256 clusters)
    Extent allocator size: 4194304 (1 groups)
    Journal size: 67108864
    Node slots: 8
    Creating bitmaps: done
    Initializing superblock: done
    Writing system files: done
    Writing superblock: done
    Writing backup superblock: 1 block(s)
    Formatting Journals: done
    Growing extent allocator: done
    Formatting slot map: done
    Formatting quota files: done
    Writing lost+found: done
    mkfs.ocfs2 successful

### [Enable Dual-Primary Mode]

Enabling Dual-Primary mode is easy, just uncomment the resources files we have made on top.

[FILE] **`/etc/drdb.d/r0.res`Resource name r0 DRBD Dual Primary**

    resource r0
            startup
            on serverNode01
            on serverNode02
            net
    }

Then it\'s time to make changes on both nodes, in sequence primary then only secondary.

`root `[`#`]`drbdadm adjust r0 `

`root `[`#`]`drbdadm primary r0 `

Check if drbd are now dual primary

`root `[`#`]`cat /proc/drbd`

    version: 8.4.3 (api:1/proto:86-101)
    built-in

     1: cs:Connected ro:Primary/Primary ds:UpToDate/UpToDate C r-----
        ns:0 nr:535088 dw:535088 dr:928 al:0 bm:131068 lo:0 pe:0 ua:0 ap:0 ep:1 wo:f oos:0

We can now mount it the OCFS2 cluster on both node.

`root `[`#`]`mount /ocfs2cluster/ `

## [Adding both DRBD and OCFS2 on system boot]

Let us start both DRBD and OCFS2 when system boot up.

`root `[`#`]`rc-update add drbd`

`root `[`#`]`rd-update add ocfs2`

## [Manual Split Brain Recovery]

Summary from ^[\[2\]](#cite_note-ManualSplitBrinaRecovery-2)^ Under certain condition, Split Brain will happen and cannot be recover automatically by system. And we have to manually recovery the DRBD disk.

### [][Split Brain Victim, Choose a node upon which the changes will be discarded]

We will disconnect this node, make it secondary and connect it back to the drbd array and we will discard all the differences so that it will sync with the latest version from other node.

`root `[`#`]`drbdadm disconnect r0 `

`root `[`#`]`drbdadm secondary r0 `

`root `[`#`]`drbdadm connect --discard-my-data r0 `

### [][Split Brain Survivor, Choose The node upon which we have the latest version of files]

We just connect this back to the drbd array so the secondary will sync from here.

`root `[`#`]`drbdadm connect r0 `

### [Result]

Sync should happen and we should have our array back. What if that don\'t happen.

Troubleshooting and error recovery^[\[3\]](#cite_note-TroubleshootingandErrorRecovery-3)^

## [See also]

-   [DRBD](https://wiki.gentoo.org/wiki/DRBD "DRBD")

## [References]

1.  [[[↑](#cite_ref-drbdManual_1-0)] [[The DRBD User's Guide Ver 8.4](http://www.drbd.org/users-guide/drbd-users-guide.html), The DRBD User's Guide]]
2.  [[[↑](#cite_ref-ManualSplitBrinaRecovery_2-0)] [[Manual Split Brain Recovery Ver 8.4](http://www.drbd.org/users-guide/s-resolve-split-brain.html)]]
3.  [[[↑](#cite_ref-TroubleshootingandErrorRecovery_3-0)] [[Troubleshooting and error recovery Ver 8.4](http://www.drbd.org/users-guide/ch-troubleshooting.html)]]