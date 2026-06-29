[badblocks] is a small program for stress testing [block devices](https://en.wikipedia.org/wiki/Block_device#Block_devices "wikipedia:Block device"). Similar to [memtest86+], badblocks reads and writes small patterns of bytes to block devices.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Test a drive]](#Test_a_drive)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Emerge]

badblocks comes as part of the [[[sys-fs/e2fsprogs]](https://packages.gentoo.org/packages/sys-fs/e2fsprogs)[]] package and should be available as part of the default system profile.

## [Usage]

### [Invocation]

`user `[`$`]`badblocks`

    Usage: /sbin/badblocks [-b block_size] [-i input_file] [-o output_file] [-svwnf]
           [-c blocks_at_once] [-d delay_factor_between_reads] [-e max_bad_blocks]
           [-p num_passes] [-t test_pattern [-t test_pattern [...]]]
           device [last_block [first_block]]

### [Test a drive]

To test a drive with visual progress use the `-s` and `-w` options followed by the path to the block device. -b flag is added as a precaution and to support large drives.

** Warning**\
All data on the device will be completely overwritten and destroyed; be sure to create backups as needed to preserve data that should be saved!

`root `[`#`]`` badblocks -s -w -b `blockdev --getbsz /dev/<device>` /dev/<device> ``

Replace `<device>` in the command above with the block device that is to be tested. badblocks should run through a series of four tests and return output similar to the following:

    Testing with pattern 0xaa: done
    Reading and comparing: done
    Testing with pattern 0x55: done
    Reading and comparing: done
    Testing with pattern 0xff: done
    Reading and comparing: done
    Testing with pattern 0x00: done
    Reading and comparing: done

badblocks also supports a non-destructive read-write mode when using the `-n` option instead of `-w`. Users are advised to create backups nonetheless.

## [See also]

-   [Memtest86+](https://wiki.gentoo.org/wiki/Memtest86%2B "Memtest86+") --- memory test software based on the commercially available (from Passmark) [memtest86](https://www.memtest86.com/) program.

## [External resources]

-   [badblocks on Arch wiki](https://wiki.archlinux.org/index.php/badblocks)