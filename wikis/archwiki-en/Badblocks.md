# Badblocks

badblocks is a program to test storage devices for bad blocks.

Modern HDDs and SSDs include firmware that will automatically detect, attempt to correct, and report errors. However, firmware becomes aware of a corrupted sector only upon an attempt to read or write to it. Badblocks may be used to test the entire device at once. It operates by sequentially attempting to read and optionally write to and read back every sector on a drive, and report errors. Consequently, the firmware will react to any detected failures in this process.

## Installation
Install the  package.

See  for the usage.

## Storage device fidelity
Due to natural manufacturing defects, every new drive generally has some bad sectors. However as part of manufacturing these sectors are scanned for, detected, and reported to the firmware of the drive. Sectors such as this will not be visible to end users, a new drive should always report zero bad sectors. As part of normal usage, drives will degrade over time developing more bad sectors. Drive firmware automatically monitors and attempts to correct for this and a small number of bad blocks on older drives is expected. An increasing number of bad blocks generally indicates a failing drive, and more than a few on a drive still within warranty generally indicates a defective drive, both of which should be replaced.

## Comparisons with other programs
Many storage device manufacturers have their own test programs for drives. Their standards as well as firmware specific quirks are normally built in to the program, and can be more accurate for drive health than badblocks. Furthermore, they can take much less time to scan drive than badblocks. However, some tools do not always report full tests results and simply report a pass or failure, making them less useful for precise information.

## Testing
## Read-only test
Read-only tests attempt to read every single sector on the specified drive. The operation is non-destructive and may be safely executed on live systems. It is similar to an extended S.M.A.R.T. self-test, however unlike the self-test badblocks will proceed even after encountering an error, identifying all errors on the device.

## Write-mode test
Write tests are a more intensive but fully destructive test, in which a pattern is written to the entire disk and then read back after a pass. As the pattern is written to every accessible block, contents of the device are lost. The default is an extensive test with four passes using four different patterns: 0xaa (10101010), 0x55 (01010101), 0xff (11111111) and 0x00 (00000000). For some devices this will take a couple of days to complete.

Options:
: : do a destructive write test
: : show progress
: : be "verbose" and output bad sectors detected to stdout

Additional options you might consider:
: : specify the block size of the hard disk which can significantly improve testing time. ( as the root user). For drives larger than two terabytes,  is required for the test to proceed properly
: : run through the extensive four pass test number of sequent iterations
: : print bad sectors to output-file instead of stdout
: : Specify a pattern. See below.

## Define specific test pattern
From the manpage: "The test_pattern may either be a numeric value between 0 and  ULONG_MAX-1  inclusive ===== Random pattern =====

Badblocks can be made to repeatedly write a single "random pattern" with the  option.

## Read-write test (non-destructive)
This test is designed for devices with data already on them. A non-destructive read-write test makes a backup of the original content of a sector before testing with a single random pattern and then restoring the content from the backup. This is a single pass test and is useful as a general maintenance test.

The  option signifies a non-destructive read-write test.

## Have filesystem incorporate bad sectors
To not use bad sectors, they have to be known by the filesystem.

## During filesystem check
Incorporating bad sectors can be done using the filesystem check utility (fsck). fsck can be told to use badblocks during a check.  To do a read-write (non-destructive) test and have the bad sectors made known to the filesystem, run:

 # fsck -vcck /dev/device-PARTITION

The  option tells run  in non-destructive test mode, the  tells  to show its output, and the  option preserves old bad sectors that were detected.

To do a read-only test (not recommended):

 # fsck -vck /dev/device-PARTITION

## Before filesystem creation
Alternately, this can be done before filesystem creation.

If badblocks is run without the  option, bad sectors will only be printed to stdout.

Example output for read errors in the beginning of the disk:

For comfortably passing badblocks error output to the filesystem, it has to be written to a file.

Then (re-)create the file system with the information:

 # mke2fs -t filesystem-type -l /root/badblocks.txt /dev/device

## Ext4
From the  manual page:
:Note that the block numbers in the bad block list must be generated using the same block size as used by mke2fs. As a result, the  option to mke2fs is a much simpler and less error-prone method of checking a disk for bad blocks before formatting it.

So the recommended method is to use:

 # mkfs.ext4 -c /dev/device

Use  to do a read-write bad block test.

## Block size
First, find the file systems' block size.  For example for ext# filesystems:

 # dumpe2fs /dev/device-PARTITION | grep 'Block size'

Feed this to badblocks:

 # badblocks -b block size

## Finding bad sectors
You can use badblock to find bad sectors. Note that badblocks calls sectors "blocks". It supports a few scan modes. There is read-only mode (default) which is the least accurate. There is the destructive write-mode ( option) which is the most accurate but takes longer and will (obviously) destroy all data on the drive, thus making it quite useless for matching sectors up to files. There is finally the non-destructive read-write mode which is probably as accurate as the destructive mode, with the only real downside that it is probably the slowest. However, if a drive is known to be failing, then read-only mode is probably still the safest.

To do a verbose ( option), read-only scan, run one of these commands (with  being the drive letter and  being partition number you want to scan):

Whole disk scan:
 # badblocks -v /dev/sdx

Single partition scan:
 # badblocks -v /dev/sdxy

The downside to scanning the drive as a whole is that each filesystem is going to start its block count relative to the partition it is on. This means that if you have a bad block that happens to be on, let us say, the second partition, and that partition starts on block 1000, then you will have to subtract 1000 from your block number in order to get the number you want. So if a scan from the beginning of the disk results in block number 1005 being bad, then block 5 of the second partition is what you will actually be using.

Otherwise, if you have found bad blocks after doing a full scan, you can simply figure out which partitions they are on, and rescan those in order to get the block number, rather than do any block math.

Another thing to note is that badblocks defaults to 1024 byte blocks, so you will either have to change the default size with the  option in order to match your filesystem or manually convert the block number(s) later.

If you need to figure out where your partitions start and end, run fdisk. Make sure to note the block size fdisk is using so that you can convert the block counts to match your scan.

After all this, you should have the block number(s) of your bad block(s), relative to the partition they exist on.

## Interaction with remapping
HDD controllers with SMART are generally able to remap a bad sector. They still waste time retrying reads at a bad sector, but on a write they either manage to fix it (when the error is "soft", i.e. ECC failure) or remap it to a spare sector, as long as the spare is not depleted.

* In non-destructive RW mode, badblocks first attempt a read of a sector. As a result, both "soft" and "hard" bad sectors are considered bad and not further tested. You should see the pending count unchanged or go up in SMART.
* In destructive RW mode, badblocks does the writing first. As a result, a remap should be triggered and the sector should be "fixed" in terms of being accessible. You should see the pending sector count go down in SMART, while the reallocated count stays unchanged (if "soft") or goes up (if "hard"). badblocks will go on to test whether the sector faithfully retains the data, as it is originally designed to.

It is possible to force a write using the badblocks list from non-destructive testing. One would need to calculate the LBA ranges, use  to narrow it down to single sectors, and finally use  [https://serverfault.com/a/641135/ to trigger the write. You would be giving up on any possible future retries at this sector, but at least no more read hangs would occur.

## Alternatives
Since badblocks was originally written to verify floppy disks, its design is not construed for modern HDDs. With sizes such as 18 TB drives, even the regular tip to use  will not help anymore. Encrypting a bunch of zeroes is a great alternative:

# Span a crypto layer above the device:
# Fill the now opened decrypted layer with zeroes, which get written as encrypted data:
# Compare fresh zeroes with the decrypted layer:  If it just stops with a message about end of file, the drive is fine. This method is also way faster than badblocks even with a single pass. As the command does a full write, any bad sectors (as known to the disk controller) should also be eliminated.

On btrfs and ZFS, the designers have decided that a floppy-era bad block list is not needed any more. They are usually right as long as you write over the defects (see above). Reading will still hang from retrying. If you want to "isolate" the bad blocks like in the old days, use a lower-level solution by partitioning or LVM.

On modern spinning drives,  (see S.M.A.R.T.) performs a full read-only test. It will halt as soon as a failure is found and record it as a "LBA_of_first_error" data entry, which you can then overwrite with hdparm (see above). You can skip the failure with a follow up selective test.
