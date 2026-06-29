The **WD Black2** is a dual hybrid drive solution from Western Digital with a 120GB SSD coupled with a 1TB traditional rotating media on a single SATA device. Factory configuration of the drive allows a SATA host to only recognize the 120GB capacity per the SSD.

The 1TB media is \"unlocked\" via a Windows or MacOS installer tool available from Western Digital\'s product website. Although the **WD Black2** seems to be a device that does not work with Linux, the installer simply \"unlocks\" the upper 1TB and partitions the drive in 2 parts to distinguish between storage on the SSD and storage on the HDD. Once the HDD storage is unlocked, it may be used on any operating system. This article will explain how to use this drive under Gentoo Linux.

## Contents

-   [[1] [Unlocking the 1TB HDD]](#Unlocking_the_1TB_HDD)
-   [[2] [Partitioning the drive]](#Partitioning_the_drive)
    -   [[2.1] [Windows partitioning scheme]](#Windows_partitioning_scheme)
-   [[3] [Updating drive firmware from Linux]](#Updating_drive_firmware_from_Linux)
-   [[4] [Performance]](#Performance)
    -   [[4.1] [Random access]](#Random_access)
    -   [[4.2] [Sequential read]](#Sequential_read)
    -   [[4.3] [Old tests (INCORRECT)]](#Old_tests_.28INCORRECT.29)
        -   [[4.3.1] [hdparm]](#hdparm)
        -   [[4.3.2] [dd]](#dd)

## [Unlocking the 1TB HDD]

Unfortunately, physical access to a machine running Microsoft Windows is required for this step. If your drive already shows capacity of 1120GB in the BIOS, you may skip this section.

1.  Note that you should better check the drive sector count before enabling HDD, for example by connecting it to a Linux machine and checking dmesg (it will say something like \"\... xxxxxxxxx 512-byte sectors\"). You will use this number as your SSD-HDD partition boundary. In my case it was 234441648 sectors.
2.  Connect the **WD Black2** to a system with a free SATA port (impossible through USB cables, even those that support SMART i.e. scsi-to-ata translation) and boot into Microsoft Windows
    1.  Use a system that is already running Microsoft Windows and connect drive as a slave
    2.  OR install Microsoft Windows onto the drive from scratch.
3.  Run the WD Black2 installer which can be downloaded from the [product page](http://www.wdc.com/en/products/products.aspx?id=1190)
4.  Confirm that you are able to see 1120GB capacity in the BIOS

In fact WD utility only sends several VSC (Vendor-Specific Commands) to the drive. If you\'re familiar with disassembly you can try to discover these commands by looking into the official MacOS utility: it contains a small and simple command-line utility called xlba (WD_Black2_Configuration_Utility/WD Black2 Dual Drive Initialize.app/Contents/Resources/xlba in the package) - it\'s written in C++ and it\'s relatively easy to disassemble.

## [Partitioning the drive]

Once the drive is unlocked, it may technically be used on any system or configuration ~~as long as read/write commands do not cross over from the SSD to the HDD. This is why the tool available from Western Digital partitions the drive automatically, to protect itself from receiving a read/write command that would cross the boundary~~. NOTE [VitaliyFilippov](https://wiki.gentoo.org/index.php?title=User:VitaliyFilippov&action=edit&redlink=1 "User:VitaliyFilippov (page does not exist)") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:VitaliyFilippov&action=edit&redlink=1 "User talk:VitaliyFilippov (page does not exist)")) 09:51, 11 July 2015 (UTC): Although it\'s of course stupid to mix SSD and HDD in one partition, I didn\'t experience any issues when reading/writing across the boundary.

Use the SSD sector count from the previous step as the boundary between your SSD and HDD partitions. In my case the exact number of 512-byte SSD sectors was 234441648 and total drive size was 2187966778 sectors. If your numbers don\'t differ, just make sure your SSD partitions end with sector number 234441647, and that your HDD partitions begin with 234441648.

### [Windows partitioning scheme]

The partitioning scheme after running the installer may look something like this if setup as an MBR drive

`root `[`#`]`parted -a optimal /dev/sda`

    GNU Parted 2.3
    Using /dev/sdd
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) unit mib
    (parted) p
    Model: ATA WDC WD1001X06X-0 (scsi)
    Disk /dev/sdd: 1068343MiB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos

    Number  Start      End         Size       Type     File system  Flags
     1      1.00MiB    351MiB      350MiB     primary  ntfs         boot
     2      351MiB     114472MiB   114121MiB  primary  ntfs
     3      114474MiB  1068343MiB  953869MiB  primary

It seems the installer tool makes a boundary between partitions 2 (ending with 114472MiB) and 3 (starting with 114474MiB). It\'s not required in any way - the HDD partition may start exactly the next sector after the last SSD sector, but if you\'re getting some unexpected issue (unresponsive drive or so) you can also add some free space between SSD and HDD partitions. For example with a VERY big (\> 16 GB) boundary the partitioning scheme may look like the following:

`root `[`#`]`parted -a optimal /dev/sda`

    GNU Parted 2.3
    Using /dev/sdb
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) unit mib
    (parted) p
    Model: ATA WDC WD1001X06X-0 (scsi)
    Disk /dev/sdb: 1068343MiB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt

    Number  Start      End         Size       File system     Name          Flags
     1      1.00MiB    512MiB      511MiB     fat32           SP            boot
     2      513MiB     114472MiB   113959MiB  ext4            rootfs
     3      131072MiB  135168MiB   4096MiB    linux-swap(v1)  swap
     4      135169MiB  176129MiB   40960MiB   ext4            /var/tmp
     5      176130MiB  217090MiB   40960MiB   ext4            /var/db/repos/gentoo
     6      217090MiB  1068343MiB  851253MiB  ext4            /home

Here partitions 1 and 2 are located on the SSD while partitions 3-6 are on the HDD. The root file system and boot partitions are stored on the SSD for fast data read speeds. /var/tmp is a location that will see many writes on Gentoo due to compiling which can reduce the life of an SSD so it is stored on the HDD. Similarly, /var/db/repos/gentoo sees writes on emerge \--sync commands. Naturally /home and swap are stored on the HDD as they consist of data that is accessed slowly.

## [Updating drive firmware from Linux]

There is a firmware update 01.01A02 for this drive on the official site. However it\'s represented by either DOS or MacOS utilities. But the MacOS utility in fact contains a bootable Ubuntu Linux drive image and that\'s why it weighs \~700 mb. It\'s easily possible to extract the firmware update utility from that image, and it\'s only 2.5mb uncompressed and 1.1mb zip compressed: [http://yourcmc.ru/wiki/images/c/c0/Wd6098.zip](http://yourcmc.ru/wiki/images/c/c0/Wd6098.zip); it\'s a Linux x86-64 executable and must be run as root. It works without problem under Debian Stretch/Sid. Probably the most convenient way to upgrade the drive for Linux users :)

## [Performance]

### [Random access]

\'fio\' (Flexible I/O tester) may be used for getting much more correct benchmark results than using quick&dirty methods like \'hdparm\' or \'dd\'.

My method is to run the following command with \<buffer_size\> equal to \"4096-16384\" (4k-16k random read/write) and \"1048576\" (1M random read/write) on SSD and HDD partitions:

    fio -name iops -rw=randrw -numjobs 8 -filesize=512m -bs=<buffer_size> -runtime=20 -iodepth 64 -directory <mounted_partition_path> -direct 1

Testing results:

-   WD Black2 HDD:
    -   4-16 Kb: 0.46/1.57 Mb/s (read/write)
    -   1 Mb: 37/32 Mb/s
-   WD Black2 SSD:
    -   4-16 Kb: 13/43 Mb/s
    -   1 Mb: 64/51 Mb/s
-   For reference, normal 2.5\" SATA SSD Plextor PX-128M3:
    -   4-16 Kb: 23/78 Mb/s
    -   1 Mb: 128/114 Mb/s

Which means WD Black2\'s SSD is \~2x times slower than separate 2.5\" SSD (probably because it consists from only 2 flash memory chips), but it\'s still SSD and it\'s still much faster than HDD part during random access.

### [Sequential read]

It\'s easy to check sequential read speed by using \'dd\' utility:

    # test SSD part
    dd if=/dev/sda1 of=/dev/null bs=1048576 count=1000
    # test HDD beginning
    dd if=/dev/sda2 of=/dev/null bs=1048576 count=1000
    # test HDD end
    dd if=/dev/sda2 of=/dev/null bs=1048576 count=1000 skip=950000

Here I assume /dev/sda1 is the whole SSD (sectors 0 to 234441647), and /dev/sda2 is the whole HDD (sectors 234441648 to 2187966777).

By running these tests, I\'ve got the following results:

-   WD Black2 SSD: seq.read speed 133 Mb/s
-   WD Black2 HDD beginning: seq.read speed 110 Mb/s
-   WD Black2 HDD end: seq.read speed 57 Mb/s

Which again tells us that WD Black2 SSD is 2x times slower than my Plextor PX-128M3 (its seq.read speed is about 240-250 Mb/s).

Note that it\'s INCORRECT to check read/write speed by creating a temporary file in the target FS, unless you\'re using the O_DIRECT flag, because you\'ll be benchmarking Linux page cache and not the drive itself.

### [][Old tests (INCORRECT)]

#### [hdparm]

A very quick and dirty method to benchmark the drive can be used with [hdparm](https://wiki.gentoo.org/wiki/Hdparm "Hdparm"). Following the partitioning scheme above, the SSD and HDD is accessed as followed:

-   /dev/sda1 - SSD
-   /dev/sda2 - SSD
-   /dev/sda3 - HDD
-   /dev/sda4 - HDD
-   /dev/sda5 - HDD
-   /dev/sda6 - HDD

With that in mind, you can pass partitions to [hdparm](https://wiki.gentoo.org/wiki/Hdparm "Hdparm") to focus the I/O.

`root `[`#`]`hdparm -t /dev/sda1 /dev/sda2 /dev/sda3 /dev/sda4 /dev/sda5 /dev/sda6`

    /dev/sda1:
     Timing buffered disk reads: 510 MB in  1.39 seconds = 367.67 MB/sec

    /dev/sda2:
     Timing buffered disk reads: 1178 MB in  3.00 seconds = 392.38 MB/sec

    /dev/sda3:
     Timing buffered disk reads: 346 MB in  3.01 seconds = 115.10 MB/sec

    /dev/sda4:
     Timing buffered disk reads: 330 MB in  3.01 seconds = 109.57 MB/sec

    /dev/sda5:
     Timing buffered disk reads: 338 MB in  3.01 seconds = 112.46 MB/sec

    /dev/sda6:
     Timing buffered disk reads: 322 MB in  3.02 seconds = 106.67 MB/sec

#### [dd]

The utility [dd](https://wiki.gentoo.org/wiki/Dd "Dd") can be used to test reads/writes. Since /root is part of the SSD, I will use it as the directory for testing.

`root `[`#`]`cd /root`

Test writes:

`root `[`#`]`dd if=/dev/zero of=tempfile bs=1M count=1024 conv=fdatasync,notrunc`

    1024+0 records in
    1024+0 records out
    1073741824 bytes (1.1 GB) copied, 7.64504 s, 140 MB/s

Clear the buffer cache:

`root `[`#`]`echo 3 > /proc/sys/vm/drop_caches`

Test reads:

`root `[`#`]`dd if=tempfile of=/dev/null bs=1M count=1024`

    1024+0 records in
    1024+0 records out
    1073741824 bytes (1.1 GB) copied, 2.5181 s, 426 MB/s

Test cached reads by running it again:

`root `[`#`]`dd if=tempfile of=/dev/null bs=1M count=1024`

    1024+0 records in
    1024+0 records out
    1073741824 bytes (1.1 GB) copied, 0.146506 s, 7.3 GB/s

Delete tempfile:

`root `[`#`]`rm tempfile`