# Status

## Overview

For a list of features by the kernel version of their introduction, please see `/Feature-by-version`.

The table below is an overview of the stability status of the features that BTRFS supports. While a feature may be functionally safe and reliable, it does not necessarily mean that it is suitable for all use cases or workloads, for example performance. Combination of features can vary in performance, the table does not cover all possibilities.

**The table is based on the latest released linux kernel: 7.0**

Since kernel version 6.12 there's a config option *CONFIG_BTRFS_EXPERIMENTAL* that enables features that are in development and do not have stabilized interface or have known problems. See the `list below<status-experimental-features>`.

The columns for each feature reflect the status of the implementation in following ways:

*Stability* - completeness of the implementation, use case coverage
*Performance* - how much it could be improved until the inherent limits are hit
*Notes* - short description of the known issues, or other information related to status

*Legend:*

- **OK**: should be safe to use, no known major deficiencies
- **mostly OK**: safe for general use, there are some known problems that do not affect majority of users
- **Unstable**: do not use for other then testing purposes, known severe problems, missing implementation of some core parts

Please open a github issue \<https://github.com/kdave/btrfs-progs/issues if:

- there's a known missing entry
- a particular feature combination that has a different status and is worth mentioning separately
- you know of a bug that lowers the feature status

| Feature | Stability | Performance | Notes |
|----|----|----|----|
| `Subvolumes, snapshots<Subvolumes>` | OK | OK |  |
| `Compression<Compression>` | OK |  |  |
| `Checksumming algorithms<Checksumming>` | OK | OK |  |
| `Defragmentation<Defragmentation>` | mostly OK |  | extents get unshared (see below) |
| `Autodefrag <Administration:mount-option-autodefrag>` | OK |  |  |
| `Discard (synchronous)<Trim>` | OK |  | mounted with -o discard (has performance implications), also see fstrim |
| `Discard (asynchronous)<Trim>` | OK |  | mounted with -o discard=async (improved performance) |
| `Out-of-band dedupe<Deduplication>` | OK | mostly OK | (reflink), heavily referenced extents have a noticeable performance hit (see below) |
| `File range cloning<Reflink>` | OK | mostly OK | (reflink), heavily referenced extents have a noticeable performance hit (see below) |
| `Filesystem resize<Resize>` | OK | OK | shrink, grow |
| `Device replace<Volume-management>` | mostly OK | mostly OK | (see below) |
| `Auto-repair<Auto-repair>` | OK | OK | automatically repair from a correct spare copy if possible (DUP, RAID1, RAID10, RAID56) |
| `Scrub<Scrub>` | OK | OK |  |
| Scrub + RAID56 | mostly OK | mostly OK |  |
| `Degraded mount <Administration:mount-option-degraded>` | OK | n/a |  |
| `Balance<Balance>` | OK | OK | balance + qgroups can be slow when there are many snapshots |
| Dynamic block group reclaim | TBD | TBD | Tunable thresholds for automatic background block group reclaim. |
| `Send<Send-receive>` | OK | OK |  |
| `Receive<Send-receive>` | OK | OK |  |
| Offline UUID change | OK | OK |  |
| Metadata UUID change | OK | OK |  |
| Temporary FSID | 6.8 | 6.8 | Single devices with same FSID can be mounted repeatedly, getting a temporary UUID. |
| `Seeding<Seeding-device>` | OK | OK |  |
| `Quotas, qgroups<Qgroups>` | mostly OK | mostly OK | qgroups with many snapshots slows down balance |
| `Squota, simplified qgroups<Qgroups>` | 6.8 | 6.8 | simplified qgroup accounting, better performance, specific use case |
| `Swapfile<Swapfile>` | OK | n/a | with some limitations |
| nodatacow | OK | OK |  |
| Encoded io read/write | OK | OK | Special *ioctls* to read or write file extent data directly, the raw compressed bytes in particular. |
| `Subpage block size<Subpage>` | OK | OK | Also see `table below<status-subpage-block-size>` for compatibility. |
| `Zoned mode<Zoned-mode>` | mostly OK | mostly OK | Not yet feature complete but moderately stable, also see `table below<status-zoned>` for compatibility. |

### Block group profiles

| Feature | Stability | Performance | Notes |
|----|----|----|----|
| `Single (block group profile)<mkfs-section-profiles>` | OK | OK |  |
| `DUP (block group profile)<mkfs-section-profiles>` | OK | OK |  |
| `RAID0<mkfs-section-profiles>` | OK | OK |  |
| `RAID1<mkfs-section-profiles>` | OK | mostly OK | reading from mirrors in parallel can be optimized further (see below) |
| `RAID1C3<mkfs-section-profiles>` | OK | mostly OK | reading from mirrors in parallel can be optimized further (see below) |
| `RAID1C4<mkfs-section-profiles>` | OK | mostly OK | reading from mirrors in parallel can be optimized further (see below) |
| `RAID10<mkfs-section-profiles>` | OK | mostly OK | reading from mirrors in parallel can be optimized further (see below) |
| `RAID56<mkfs-section-profiles>` | unstable | n/a | (see below) |
| `Mixed block groups<mkfs-feature-mixed-bg>` | OK | OK |  |

### On-disk format

Features that are typically set at *mkfs* time (sometimes can be changed or converted later).

| Feature | Stability | Performance | Notes |
|----|----|----|----|
| `extended-refs<mkfs-feature-extended-refs>` | OK | OK | mkfs.btrfs default since 3.12 |
| `skinny-metadata<mkfs-feature-skinny-metadata>` | OK | OK | mkfs.btrfs default since 3.18 |
| `no-holes<mkfs-feature-no-holes>` | OK | OK | mkfs.btrfs default since 5.15 |
| `Free space tree<mkfs-feature-free-space-tree>` | OK | OK | mkfs.btrfs default since 5.15 |
| `Block group tree<mkfs-feature-block-group-tree>` | OK | OK |  |
| `Raid stripe tree<mkfs-feature-raid-stripe-tree>` | mostly OK | OK | not all profiles are supported and RST is behind CONFIGBTRFS_DEBUG/CONFIGBTRFS_EXPERIMENTAL build option |
| `Squota<Qgroups>` | OK | OK | Simplified tracking needs on-disk format update, but may work in a limited way without it. |
| `Remap tree tree<mkfs-feature-raid-stripe-tree>` | mostly OK | initial support in 7.0 | Another logical-to-logical layer mapping of block addresses to avoid unnecessary COW. CONFIGBTRFS_EXPERIMENTAL build option |

### Interoperability

Integration with other Linux features or external systems. `See also<Interoperability>`.

| Feature | Stability | Performance | Notes |
|----|----|----|----|
| `NFS<interop-nfs>` | OK | OK |  |
| `cgroups<interop-cgroups>` | OK | OK | IO controller |
| `io_uring<interop-io-uring>` | OK | OK | Can be combined with *Encoded read/write ioctls*. |
| `fsverity<interop-fsverity>` | OK | OK |  |
| `idmapped mount<interop-idmapped>` | OK | OK |  |
| `Samba<interop-samba>` | OK | OK | compression, server-side copies, snapshots |

## Subpage block size

Most commonly used page sizes are 4KiB, 16KiB and 64KiB. All combinations with a 4KiB sector size filesystems are supported. Some features are not compatible with subpage or require another feature to work. Since btrfs-progs 6.7 the default sector size is 4KiB as this allows cross-architecture compatibility. On x8664 the 2KiB *nodesize* is possible under debuggijng config, recommended only for testing.

| Feature | Status | Notes |
|----|----|----|
| Inline files | unsupported | The maxinline mount option value is ignored, as if mounted with maxinline=0 |
| Free space cache v1 | unsupported | Free space tree is mandatory, v1 makes some assumptions about page size |
| Compression | partial support | Only page-aligned ranges can be compressed |
| Sectorsize | supported | The list of supported sector sizes on a given version can be found in file `/sys/fs/btrfs/features/supported_sectorsizes` |

## Zoned mode

Features that completely incompatible with zoned mode are listed below. Compatible features may not be listed and are assumed to work as they are unaffected by the zoned device constraints. Since 7.0, the zone usage statistics are shown in the filesystem entry in `/proc/PID/mountstats`.

| Feature | Status | Notes |
|----|----|----|
| Boot | incompatible | The blocks where partition table is stored are used for super block |
| Mixed block groups | incompatible | Interleaving data and metadata would lead to out of order write |
| NODATACOW | incompatible | In-place overwrite |
| fallocate | incompatible | Preallocation of blocks would require an out of order write |
| Free space cache v1 | incompatible | Cache data are updated in a NODATACOW-way |
| Swapfile | incompatible | Swap blocks are written out of order |
| Offline UUID change | incompatible | Metadata blocks are updated in-place |
| Free space tree | supported |  |
| Block group tree | supported |  |
| Raid stripe tree | supported | Allows to use RAID in zoned mode |
| Filesystem resize | supported |  |
| Balance | supported |  |
| Metadata UUID change | supported |  |
| RAID0, RAID1\* | supported | requires raid-stripe-tree |
| RAID56 | not implemented | Will be supported once raid-stripe-tree support is implemented |
| discard | not implemented | May not be required at all due to automatic zone reclaim |
| subpage blocksize | not implemented | Missing support for compressed data |
| fsverity | TBD |  |
| seeding | TBD |  |

## Details that do not fit the tables

### Defrag

The data affected by the defragmentation process will be newly written and will consume new space, the links to the original extents will not be kept. See also `btrfs-filesystem` . Though autodefrag affects newly written data, it can read a few adjacent blocks (up to 64KiB) and write the contiguous extent to a new location. The adjacent blocks will be unshared. This happens on a smaller scale than the on-demand defrag and doesn't have the same impact.

### RAID1, RAID10

The simple redundancy RAID levels utilize different mirrors in a way that does not achieve the maximum performance. The logic can be improved so the reads will spread over the mirrors evenly or based on device congestion.

### RAID56

Please see <https://btrfs.readthedocs.io/en/latest/btrfs-man5.html#raid56-status-and-recommended-practices> .

### Device replace

Device *replace* and device *delete* insist on being able to read or reconstruct all data. If any read fails due to an IO error, the delete/replace operation is aborted and the administrator must remove or replace the damaged data before trying again.

## On-disk format

The filesystem disk format is stable. This means it is not expected to change unless there are very strong reasons to do so. If there is a format change, filesystems which implement the previous disk format will continue to be mountable and usable by newer kernels.

The core of the on-disk format that comprises building blocks of the filesystem:

- layout of the main data structures, e.g. superblock, b-tree nodes, b-tree keys, block headers
- the COW mechanism, based on the original design of Ohad Rodeh's paper "B-trees, Shadowing and Clones" (<http://sylab-srv.cs.fiu.edu/lib/exe/fetch.php?media=paperclub:shadow_btree.pdf>)

Newly introduced features build on top of the above and could add specific structures. If a backward compatibility is not possible to maintain, a bit in the filesystem superblock denotes that and the level of incompatibility (full, read-only mount possible).

## Experimental features

Until kernel 6.12 the *CONFIG_OPTION_DEBUG* was used to hide features that still need some work and should not be exposed to users in general. With the increasing number of such features or functionality this started to conflict with regular debugging features. Currently the following is behind the experimental option *CONFIG_BTRFS_EXPERIMENTAL*. Use with caution and if you find problems or have feedback please report that to the mailing list. [Current list in linux.git](https://elixir.bootlin.com/linux/latest/source/fs/btrfs/Kconfig#L87) may contain other entries not listed below in case they're not considered useful for users (e.g. internal).

| Feature | Version | Description |
|----|----|----|
| Raid stripe tree | ... | The RIAD5/6 block group is still not implemented and on-disk format is not finalized (last change was in 6.12). |
| Send stream protocol v3 | ... | The fs-verity stream command is implemented. More updates to the protocol specification are pending. |
| Read balancing | 6.13 | Spread IO read requests across available devices. A tunable is provided in sysfs. |
| Extent tree v2 | ... | Incomplete implementation. Standalone features are carved out and added separately. |
| Large folio support | ... |  |
| Shutdown ioctl | 6.19 | Will be available in 7.1 |
