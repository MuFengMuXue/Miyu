# JFS

The Journaled File System (JFS) is a journaling file system that was open-sourced by IBM in 1999 and support for which has been available in the Linux kernel since 2002.

This article introduces the reader to the JFS file system. In particular, procedures for implementation, maintenance and optimization will be presented along with background information on the file system itself and some cautionary notes on precarious implementations.

## Background
* In 1990, JFS1, (then simply called JFS), was released for AIX version 3.1. The filesystem was closely tied to its targeted hardware, IBM's AIX line of UNIX servers, being a proprietary design.
* In 1995, heavy development began on improving JFS, focusing on scalability and expanded features.
* In 1997, parallel development began on moving the improved JFS source back to AIX.
* In 1999, the improved JFS design was released for OS/2.
* In 2001, the improved filesystem (newly termed JFS2), was released for AIX 5L.
* The current GNU/Linux version is a port based on JFS for OS/2.

While it is difficult to make general comparisons between JFS and other file systems available on UNIX and UNIX-like operating systems, it is claimed that JFS uses less CPU resources than other GNU/Linux file systems With certain optimizations, JFS has also been claimed to be faster for certain file operations, as compared to other GNU/Linux file systems (see [https://www.redhat.com/archives/ext3-users/2005-July/msg00018.html,Benchmarks).

## GNU/Linux development team
The development of the GNU/Linux JFS port is headed by
* Dave Kleikamp (dave dot kleikamp at oracle dot com)
* HP: https://jfs.sourceforge.net/

## Technical features
JFS is a modern file system supporting many features, a few of which are listed here.
* fully 64-bit.
* dynamic space allocation for i-nodes, i.e. no running out of i-nodes on file systems with large number of small files.
* Directory structures designed for speed and efficiency:
** directories with eight or fewer entries have their contents storied inline within that directory's i-node.
** directories with more than eight entries have their contents stored in a B+ tree keyed on name.
* JFS utilizes extents for allocating blocks for large files.
* Support for extended attributes in addition to standard Unix-style permissions.
* Support for both internal and external logs (see below).
* Extremely Scalable; Consistent performance from minimum file size up to 4 petabytes.
* Algorithms designed for high performance on very large systems.
* Performance tuned for GNU/Linux.
* Designed from the ground up to provide Transaction/Log (not an add-on).
* Restarts after a system failure  man3_pkg_list

before attempting a forced fsck on a JFS root partition If  does indeed disappear, simply reinstall all the packages listed in man3_pkg_list.

As stated above, the reason for this issue is not clear at the moment; but it may have something to do with the fact that a forced fsck runs through higher phases of file system checks that only happen when a JFS log gets damaged in an improper dismounting of the partition.

## JFS losing files
In JFS; journal writes are indefinitely postponed until there is another trigger such as memory pressure or an unmount operation. This infinite write delay limits reliability, as a crash can result in data loss even for data that was written minutes or hours before.[https://www.usenix.org/events/usenix05/tech/general/full_papers/prabhakaran/prabhakaran.pdf

## Benchmarks
As benchmarks measuring file system performance tend to be focused at specific types of disk usage, it is difficult to decipher good general comparisons rating how well JFS performs against other files systems. As mentioned before, it has been noted that JFS has a tendency to use less CPU resources than other GNU/Linux file systems and (with the right optimizations) is faster than other GNU/Linux file systems for certain types of file operations. It has been noted that JFS slows down when working with many files, howeverIn the references are some links to benchmarks; but as always, it is best to test and see what works best for your own system and work load.

## Conclusions
JFS is a stable, feature-rich file system that has not been publicized as much as some of the other Linux file systems. With optimizations, JFS is stable, CPU efficient and fast. In particular, VMWare sessions stand to benefit enormously from a properly optimized and defragmented, underlying JFS file system.
