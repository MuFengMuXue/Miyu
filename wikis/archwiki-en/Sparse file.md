# Sparse file

According to Wikipedia, a sparse file is a type of file that attempts to use file system space more efficiently when blocks allocated to a file are mostly empty. This is achieved by writing brief information (metadata) representing the empty blocks to disk instead of the actual "empty" space which makes up the block, using less disk space. The full block size is written to disk as the actual size only when the block contains "real" (non-empty) data.

When reading sparse files, the file system transparently converts metadata representing empty blocks into "real" blocks filled with zero bytes at runtime. The application is unaware of this conversion.

Most modern file systems support sparse files, including most Unix variants and NTFS, but notably not Apple's HFS+. Sparse files are commonly used for disk images (not to be confused with sparse images), database snapshots, log files and in scientific applications.

The advantage of sparse files is that storage is only allocated when actually needed: disk space is saved, and large files can be created even if there is insufficient free space on the file system.

Disadvantages are that sparse files may become fragmented; file system free space reports may be misleading; filling up file systems containing sparse files can have unexpected effects; and copying a sparse file with a program that does not explicitly support them may copy the entire file, including the empty blocks which are not on explicitly stored on the disk, which wastes the benefits of the sparse property of a file.

## Creating sparse files
The truncate utility can create sparse files. This command creates a 512&nbsp;MiB sparse file:

 $ truncate -s 512M file.img

The dd utility can also be used, for example:

 $ dd if=/dev/zero of=file.img bs=1 count=0 seek=512M

Sparse files have different apparent file sizes (the maximum size to which they may expand) and actual file sizes (how much space is allocated for data on disk).  To check a file's apparent size, just run:

and, to check the actual size of a file on disk:

As you can see, although the apparent size of the file is 512 MiB, its "actual" size is really zero—that's because due to the nature and beauty of sparse files, it will "expand" arbitrarily to minimize the space required to store its contents.

## Making existing files sparse
The fallocate utility can make existing files sparse on supported file systems:

 $ fallocate -d copy.img
 $ du -h copy.img
 0       copy.img

## Making existing files non-sparse
The following command creates a non-sparse copy of a (sparse) file:

 $ cp file.img copy.img --sparse=never
 $ du -h copy.img
 512M    copy.img

## Creating a filesystem in a sparse file
Now that we have created a sparse file, it is time to format it with a filesystem. For example, ext4:

 $ mkfs.ext4 file.img

We can now check its size to see how a filesystem has affected it:

As you may have expected, formatting it with a filesystem has increased its actual size, but left its apparent size the same.  Now we can create a directory which we will use to mount our file:

 # mount --mkdir -o loop file.img mountpoint

Tada! We now have both a file and a folder into which we may store almost 512 MiB worth of information!

## Mounting a file at boot
To mount a sparse image automatically at boot, add an entry to your fstab:

 /path/to/file.img  /path/to/mountpoint  ext4  loop,defaults  0  0

## Detecting sparse files
Since sparse files occupy less blocks than the apparent file size would require, they can be detected by comparing the two sizes. This is not a bulletproof method if the filesystem uses compression, extended attributes take up the difference in space, file is internally fragmented, has indirect blocks, and similar. Still, the standard way to check is:

 $ ls -ls sparse-file.bin

If a file size is greater than the allocated size in the first column a file is sparse. The same can be achieved with  by comparing:

 $ du sparse-file.bin
 $ du --apparent-size sparse-file.bin

A step further is to print sparsiness value with find:

 $ find sparse-file.bin -printf '%S\t%p\n'

A sparse file has a sparsiness value of less than one whereas normal files have exactly one or just slightly above. The above command can be easily extended to list sparse files in a desired path:

 $ find path/ -type f -printf '%S\t%p\n' | gawk '$1 > folder/file1

 $ cat folder/file1
 This is a test to see if it works...

## Growing a file
Should you ever need to grow a file, you may do the following:

 # umount folder

This will increase its size to 1 GiB and leave its information intact. Next, we need to increase the size of its filesystem:

 $ e2fsck -f file.img

...and, remount it:

 # mount -o loop file.img folder

Checking its size gives us:

...and to check for consistency:

## Tools
*
*
