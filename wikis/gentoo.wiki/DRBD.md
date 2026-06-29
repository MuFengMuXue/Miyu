**Resources**

[[]][Home](https://www.linbit.com/en/drbd-community/drbd-download/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Distributed_Replicated_Block_Device "wikipedia:Distributed Replicated Block Device")

**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

\
**DRBD** (or **Distributed Replicated Block Device**) is a network block device that provides reliability when storing data across multiple network nodes.

From the kernel documentation:

> *DRBD is a shared-nothing, synchronously replicated block device. It is designed to serve as a building block for high availability clusters and in this context, is a \"drop-in\" replacement for shared storage. Simplistically, you could see it as a network RAID 1.*

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Errors]](#Errors)

## [Installation]

### [Kernel]

[KERNEL] **Enable CONFIG_BLK_DEV_DRBD in the kernel**

    Device Drivers --->  Block devices --->
    <*>   DRBD Distributed Replicated Block Device support

### [Emerge]

Install [[[sys-cluster/drbd-utils]](https://packages.gentoo.org/packages/sys-cluster/drbd-utils)[]]:

`root `[`#`]`emerge --ask sys-cluster/drbd-utils`

This package installs the userland utilities to interact with, and control DRBD. Also known as [drbdsetup] and [drbdadm].

## [Troubleshooting]

### [Errors]

    "ERROR: unknown cs for drbd0 : BrokenPipe, Update/DUnknown"

This error means connection state has a problem, link needs fixing, or drbd version updating. Upstream states \"we had some issues with discarding the first successful connection and getting in a connect/brokenpipe loop.\"

Run this command to extract useful information:

`root `[`#`]`cat /proc/drbd`