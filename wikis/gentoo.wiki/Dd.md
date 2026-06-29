**Resources**

[[]][Home](https://www.gnu.org/software/coreutils/)

[[]][Official documentation](https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/coreutils)

[[]][Wikipedia](https://en.wikipedia.org/wiki/dd_(Unix) "wikipedia:dd (Unix)")

[[]][Bugs (upstream)](https://debbugs.gnu.org/)

[[]][Man page](http://man7.org/linux/man-pages/man1/dd.1.html)

** Warning**\
There is a reason [dd] is sometimes humorously called *disk destroyer*! Incorrect use of the [dd] command can wipe any drive connected to the system. Always [backup](https://wiki.gentoo.org/wiki/Backup "Backup") any data you\'re not willing to lose before using the command.

[dd] is a utility used to copy raw data from a source into sink, where source and sink can be a block device, file, or piped input/output. Because of its flexibility [dd] can be used for a variety of purposes ranging from writing installation media to a backup and recovery tool of last resort.

The [dd] utility is [specified by the](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/dd.html) [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX") standard. On Gentoo, [dd] is provided by GNU coreutils, [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]], installed via the \@system set.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Examples]](#Examples)
    -   [[3.1] [Boot stick]](#Boot_stick)
    -   [[3.2] [Master boot record backup]](#Master_boot_record_backup)
    -   [[3.3] [Hard disk backup]](#Hard_disk_backup)
    -   [[3.4] [Input manipulation]](#Input_manipulation)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

In the event that coreutils goes missing:

`root `[`#`]`emerge --ask sys-apps/coreutils`

## [Usage]

By default [dd] takes input from [stdin], optionally manipulates the data, and writes to [stdout].

### [Invocation]

`user `[`$`]`dd --help`

    Usage: dd [OPERAND]...
      or:  dd OPTION
    Copy a file, converting and formatting according to the operands.

      bs=BYTES        read and write up to BYTES bytes at a time (default: 512);
                      overrides ibs and obs
      cbs=BYTES       convert BYTES bytes at a time
      conv=CONVS      convert the file as per the comma separated symbol list
      count=N         copy only N input blocks
      ibs=BYTES       read up to BYTES bytes at a time (default: 512)
      if=FILE         read from FILE instead of stdin
      iflag=FLAGS     read as per the comma separated symbol list
      obs=BYTES       write BYTES bytes at a time (default: 512)
      of=FILE         write to FILE instead of stdout
      oflag=FLAGS     write as per the comma separated symbol list
      seek=N          (or oseek=N) skip N obs-sized output blocks
      skip=N          (or iseek=N) skip N ibs-sized input blocks
      status=LEVEL    The LEVEL of information to print to stderr;
                      'none' suppresses everything but error messages,
                      'noxfer' suppresses the final transfer statistics,
                      'progress' shows periodic transfer statistics

    N and BYTES may be followed by the following multiplicative suffixes:
    c=1, w=2, b=512, kB=1000, K=1024, MB=1000*1000, M=1024*1024, xM=M,
    GB=1000*1000*1000, G=1024*1024*1024, and so on for T, P, E, Z, Y.
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.
    If N ends in 'B', it counts bytes not blocks.

    Each CONV symbol may be:

      ascii     from EBCDIC to ASCII
      ebcdic    from ASCII to EBCDIC
      ibm       from ASCII to alternate EBCDIC
      block     pad newline-terminated records with spaces to cbs-size
      unblock   replace trailing spaces in cbs-size records with newline
      lcase     change upper case to lower case
      ucase     change lower case to upper case
      sparse    try to seek rather than write all-NUL output blocks
      swab      swap every pair of input bytes
      sync      pad every input block with NULs to ibs-size; when used
                with block or unblock, pad with spaces rather than NULs
      excl      fail if the output file already exists
      nocreat   do not create the output file
      notrunc   do not truncate the output file
      noerror   continue after read errors
      fdatasync  physically write output file data before finishing
      fsync     likewise, but also write metadata

    Each FLAG symbol may be:

      append    append mode (makes sense only for output; conv=notrunc suggested)
      direct    use direct I/O for data
      directory  fail unless a directory
      dsync     use synchronized I/O for data
      sync      likewise, but also for metadata
      fullblock  accumulate full blocks of input (iflag only)
      nonblock  use non-blocking I/O
      noatime   do not update access time
      nocache   Request to drop cache.  See also oflag=sync
      noctty    do not assign controlling terminal from file
      nofollow  do not follow symlinks

    Sending a USR1 signal to a running 'dd' process makes it
    print I/O statistics to standard error and then resume copying.

    Options are:

          --help        display this help and exit
          --version     output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Report any translation bugs to <https://translationproject.org/team/>
    Full documentation <https://www.gnu.org/software/coreutils/dd>
    or available locally via: info '(coreutils) dd invocation'

\

## [Examples]

Some common tasks where [dd] is used:

### [Boot stick]

This should work with any live media as long as the memory stick [/dev/sdX] is large enough.

** Warning**\
Any data on the memory stick will be lost.

`root `[`#`]`dd if=/home/myLiveCD.iso of=/dev/sdX bs=8M status=progress && sync`

-   `if`: Defines the source.
-   `of`: Defines the sink.
-   `bs`: Defines the block size (amount of data read/written at a time). The default is 512 bytes but most modern devices can read/write much faster. It is possible to define different sizes for source and sink using `ibs` and `obs`.
-   `status`: Defines the level of status information printed.
-   [sync]: Synchronizes write caches to make the stick removal safe.

### [Master boot record backup]

To backup the master boot record (MBR), copy only the first 512 bytes:

`root `[`#`]`dd if=/dev/sdX of=/root/mbr.bin bs=512 count=1`

-   `count`: The number of blocks to copy.

** Note**\
This is the complete MBR with the partition layout.

### [Hard disk backup]

** Note**\
Using dd as a disk backup is generally not recommended except when a perfect image is needed. This will include unused space in the image making it larger than the data contained inside the image. The storage medium must be as large or larger than the source disk.

To backup a complete hard disk or partition, it is necessary to boot the computer with into a Live CD environment (such as the Gentoo Minimal or Gentoo Admin disk).

The following example will backup a computer drive on [/dev/sda] to an external USB drive. To be able to mount that USB drive read/write, this example will use its label:

`root `[`#`]`ls /dev/disk/by-label`

    'Gentoo\x20amd64\x20AdminCD\x2020201230T21'   MaxiTux

`root `[`#`]`mkdir /mnt/MaxiTux `

`root `[`#`]`mount /dev/disk/by-label/MaxiTux /mnt/MaxiTux `

Not every file system includes a label. Using UUID values or verified disk paths are alternatives.

To create a backup:

`root `[`#`]`dd if=/dev/sda conv=sync,noerror bs=64k status=progress > /mnt/MaxiTux/sda_backup.img`

To restore a backup:

`root `[`#`]`dd if=/mnt/MaxiTux/sda_backup.img bs=8192 conv=sync,noerror of=/dev/sda status=progress`

### [Input manipulation]

As an example, convert any upper case character in a file to lowercase and reverse the input per line, then pipe the output to [less] to display the file:

`user `[`$`]`dd if=/etc/portage/make.conf conv=swab,lcase,noerror | less`

-   `conv=swab`: Revert the input per line by swapping any input byte (writing backwards).
-   `conv=lcase`: Convert any upper case letter to lower case. To convert lower case to upper case use `conv=ucase`.
-   `conv=noerror`: Continue if a read error occurs.

## [See also]

-   [dcfldd](https://wiki.gentoo.org/wiki/Dcfldd "Dcfldd") --- an enhanced [[dd]] tool that includes additional features for forensics and security.
-   [ddrescue](https://wiki.gentoo.org/wiki/Ddrescue "Ddrescue") --- a tool provided by GNU to retrieve data from failing (block) storage devices like disk drives, CDROMs, or memory sticks, etc.
-   [pv](https://wiki.gentoo.org/wiki/Pv "Pv") --- a command line tool to view verbose information about data streamed/piped *through* it.