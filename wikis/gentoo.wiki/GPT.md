[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=GUID_Partition_Table&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

The **GUID Partition Table** (GPT) is a [partitioning](https://wiki.gentoo.org/wiki/Partition "Partition") scheme widely adopted in contemporary computers to organize and manage data on storage devices. Originally developed by Intel for the Itanium platform \"[IA64](https://wiki.gentoo.org/wiki/Project:IA64 "Project:IA64")\", GPT was designed to overcome limitations of the traditional [Master Boot Record](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record") (MBR) scheme and offers improved flexibility and scalability in handling storage on modern computing systems. The system firmware [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") demands GPT partitioning on bootable media.

Unlike the MBR, GPT employs a Globally Unique Identifier ([GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier "wikipedia:Universally unique identifier")) for each partition, allowing for a more extensive range of partitions and larger storage capacities. This modern approach is essential for accommodating the demands of today\'s data-intensive applications.

## Contents

-   [[1] [Structure and Features]](#Structure_and_Features)
-   [[2] [Compatibility and Adoption]](#Compatibility_and_Adoption)
-   [[3] [Implementation in Operating Systems]](#Implementation_in_Operating_Systems)
-   [[4] [See also]](#See_also)

### [Structure and Features]

Each partition is assigned a unique GUID, ensuring a globally distinct identifier across all systems. This design eliminates the limitations imposed by the MBR\'s maximum partition size and number of partitions, providing a solution for modern storage needs.

One notable feature of GPT is its inclusion of a Protective MBR. This ensures compatibility with legacy systems that may not fully support GPT, preventing accidental data loss or corruption when accessed by older software.

### [Compatibility and Adoption]

GPT is the standard for disk partitioning on modern computers, being compatible with both [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") (Basic Input/Output System) and [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") (Unified Extensible Firmware Interface) systems; the transition to GPT has been gradual but is now nearly ubiquitous.

### [Implementation in Operating Systems]

Major operating systems, including Linux, macOS, and Windows, include robust GPT support.

## [See also]

-   [Partition](https://wiki.gentoo.org/wiki/Partition "Partition") --- a means of splitting a block device up to sub-regions.