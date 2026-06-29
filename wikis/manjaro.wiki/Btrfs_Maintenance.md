\

## Contents

-   [[1] [Btrfs Maintenance]](#Btrfs_Maintenance)
    -   [[1.1] [Btrfs needs no maintenance]](#Btrfs_needs_no_maintenance)
        -   [[1.1.1] [Every filesystem needs some maintenance]](#Every_filesystem_needs_some_maintenance)
    -   [[1.2] [Automatic maintenance]](#Automatic_maintenance)
        -   [[1.2.1] [Is the Volume in a clean state]](#Is_the_Volume_in_a_clean_state)
            -   [[1.2.1.1] [power down]](#power_down)
            -   [[1.2.1.2] [error]](#error)
            -   [[1.2.1.3] [clean]](#clean)
    -   [[1.3] [Manual Maintenance]](#Manual_Maintenance)
        -   [[1.3.1] [Usage]](#Usage)
            -   [[1.3.1.1] [check unallocated space]](#check_unallocated_space)
            -   [[1.3.1.2] [Clean up unused snapshots]](#Clean_up_unused_snapshots)
        -   [[1.3.2] [Balance your free disk space]](#Balance_your_free_disk_space)
        -   [[1.3.3] [scrub]](#scrub)
    -   [[1.4] [special cases]](#special_cases)
        -   [[1.4.1] [SSD]](#SSD)
            -   [[1.4.1.1] [Read rate degradation (unconfirmed)]](#Read_rate_degradation_.28unconfirmed.29)
        -   [[1.4.2] [Rotating disks]](#Rotating_disks)
            -   [[1.4.2.1] [Defragmentation (not recommended)]](#Defragmentation_.28not_recommended.29)
-   [[2] [See Also]](#See_Also)

# [Btrfs Maintenance]

## [Btrfs needs no maintenance]

This can even be true when:

-   You always keep 10% of your volume **unallocated**

**free or unallocated**

------------------------------------------------------------------------

I\'m not saying \"free\" because with btrfs, free means nothing. The value you need to pay most attention to is **unallocated** !

#### [Every filesystem needs some maintenance]

Some filesystems do an automatic chkfs at every XX. mount. Others need the user to do a chkfs manually. On most you have to watch not to fill them to 100%. Others reserve 5% for root. Some filesystems need to be defragmented. Others do not.

**Every filesystem has its own needs and tools !**

## [Automatic maintenance]

Btrfs does some maintenance automatically.

### [Is the Volume in a clean state]

At mount btrfs tests wehter the volume is in a clean state.

#### [power down]

Most file systems are not prepared for a sudden loss of power. If the computer suddenly loses power, transactions may not be written or only partially written to the volume. File systems that use journaling can often recover after a power failure.

Btrfs attempts to clean the volume by removing the last (uncompleted) action. This can result in losing the last changes you made before turning off. But you get a clean file system that doesn\'t need to be repaired.

#### [error]

If btrfs encounters an unrecoverable error, such as a checksum mismatch, the filesystem will be mounted **read-only**. (When using RAID2, such errors are auto-repaired)

#### [clean]

btrfs will mount the subvolume read-write.

## [Manual Maintenance]

From time to time it may be advisable to check the health of a btrfs volume.

**Note**

------------------------------------------------------------------------

Btrfs is used to perform all maintenance on **a normally running system**. The volume can be fully used. Shutting down during such an action is also unproblematic. Btrfs will keep running the action after the next launch until it completes.

\

### [Usage]

Check if the **unallocated** space on your volume is ok.

#### [check unallocated space]

[root \# ][ btrfs filesystem usage -h / [COPY TO CLIPBOARD]]

\

\

**Pay special attention to **unallocated** !**

------------------------------------------------------------------------

The commonly used term \"free\" is meaningless to btrfs users. Even if you have 50% of your volume \"free\", you can run out of storage space.

Try to leave **at least 10%** of your volume unallocated. If this got below 10%:

-   Expand the volume to double size (see: [Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs"))
-   Delete some unused data
-   Delete some old snapshots
-   Balance ([Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs"))

#### [Clean up unused snapshots]

From time to time it is necessary to check if you have snapshots that you no longer need but that are taking up valuable space on your volume.

### [Balance your free disk space]

If you have some \"free\" space on your volume, but the unallocated space is below 10% (or close to 10%), you can help btrfs to rebalance some parts.

[root \# ][ btrfs balance start -dusage=50 / [COPY TO CLIPBOARD]]

\

Btrfs looks for chunks that contain more than 50% free space. It will take 2 of them and then move everything into a new chunk. After that, a chunk is released. This continues until each chunk is at least 50% full.

This will give you some unallocated (free) chunks that help btrfs \*\*not\*\* to get out of space.

If you have less than 20% unallocated space, please do the following:

[root \# ][ btrfs balance start -dusage=75 / [COPY TO CLIPBOARD]]

\

Btrfs looks for chunks that are less than 75% full. It will take 4 of them and then move everything into 3 new chunks. After that, a chunk can be released. This continues until each chunk is at least 75% full.

If you still have less than 20% unallocated space, please do the following:

[root \# ][ btrfs balance start -dusage=90 / [COPY TO CLIPBOARD]]

\

### [scrub]

Check if everything is ok with the checksums and the readability of your data. **Only do this when in doubt**. This may take a long time as btrfs has to read ALL the data. Btrfs only scans the portion of your volume that actually contains data.

[root \# ][ btrfs scrub start -Bd / [COPY TO CLIPBOARD]]

\

\

**Want to watch how btrfs works ?**

------------------------------------------------------------------------

[user \$ ][ pamac install procps-ng [COPY TO CLIPBOARD]]

\

**After that inside a separate terminal:**

------------------------------------------------------------------------

[root \# ][ watch -n 60 btrfs filesystem usage -h / [COPY TO CLIPBOARD]]

\

## [special cases]

There seem to be some cases where additional maintenance is needed.

#### [SSD]

Btrfs is optimal for SSDs due to its CoW nature

##### [][Read rate degradation (unconfirmed)]

This isn\'t a problem with SSDs in general, it just seems to happen in a few rare cases. Updating the firmware should then solve the problem. One way to test the read speed with btrfs is to read out all the data (scrub). If your SSD seems to have this RRD issue, **balancing** will help so that all data is written to a new location. This can be done while the system is running! But please only **once** a year!

[root \# ][ btrfs balance start \--full-balance / [COPY TO CLIPBOARD]]

\

This will take a long time. You can shut down your PC at any time. Do not be surprised. The \"balance\" will restart after booting until done!

If you want your data to rotate:

[root \# ][ btrfs balance start -dlimit=10 / [COPY TO CLIPBOARD]]

\

This rewrites 10 chunks at a time. This can be used weekly if you find it necessary.

#### [Rotating disks]

On spinning disks, fragmentation can become an issue in some rare use cases. Then you can defragment your Btrfs volume.

##### [][Defragmentation (not recommended)]

This is NOT the same as defragmentation in older Windows file systems. Btrfs does NOT require defragmentation as normal maintenance. Only do this if you can measure a huge read performance loss because a specific file/database is fragmented!

**Defragment only these specific files**

------------------------------------------------------------------------

Defragmenting an entire Btrfs volume does not increase its speed, it just wears out the device

# [See Also]

[Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs") Learn basics about btrfs