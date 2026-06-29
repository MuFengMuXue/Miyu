# Archiving and compression

The traditional Unix archiving and compression tools are separated according to the Unix philosophy:

* A file archiver combines several files into one archive file, e.g. tar.
* A compression tool compresses and decompresses data, e.g. gzip.

These tools are often used in sequence by firstly creating an archive file and then compressing it.

Of course there are also tools that do both, which tend to additionally offer encryption, error detection and recovery.

## Archiving only
{| class=wikitable
! Name !! Package !! Manuals !! Description
|-
| GNU tar ||  || , info || Core utility for manipulating the ubiquitous tar archives (tarballs).
|-
| libarchive ||  ||  || Implementation of tar and cpio that also offers a library. Used by pacman and mkinitcpio.
|-
| ar ||  || || Legacy Unix archiver before tar. Today only used for creating static library files.
|-
| GNU cpio ||  || . info || File archiver via stdin/stdout, supports cpio and tar formats.
|}

See also #Archiving only usage.

## Compression tools
## Compression only
These compression programs implement their own file format.

{| class=wikitable
! Name !! Package !! Manual !! Ext !! Tar ext !! Description !! Parallel implementations
|-
| bzip2 ||  ||  || .bz2, .bz || .tbz2, .tbz|| Uses the Burrows–Wheeler algorithm.|| ,
|-
| bzip3 ||  ||  || .bz3 || .tbz3 || Uses the Burrows–Wheeler algorithm.||
|-
| gzip ||  ||  || .gz, .z|| .tgz, .taz|| GNU zip, based on DEFLATE algorithm.|| ,  (part of ), ,
|-
| lrzip ||  ||  || .lrz || || Improved version of rzip, uses multiple algorithms. || Is multithreaded by default
|-
| LZ4 ||  ||  || .lz4 || || Written in C, focused on compression and decompression speed. ||  Is multithreaded by default. See https://lz4.org/ for alternatives.
|-
| lzip ||  ||  || .lz ||  || Uses LZMA. ||
|-
| lzop ||  ||  || .lzo || .tzo || Uses the LZO library ().||
|-
| xz ||  ||  || .xz, .lzma || .txz, .tlz|| Uses LZMA2. Default for GNU  and kernel archive files.|| Is multithreaded by default. An alternative is .
|-
| zstd ||  ||  || .zst || || Uses Zstandard algorithm. || is multithreaded
|-
|}

* Parallel implementations offer improved speeds by using multiple CPU cores.
* Tar extensions refers to compressed archives where  and the compression tool is used, e.g.  is .
* See also #Compression only usage.

## Archiving and compression
{| class=wikitable
! Name !! Packages !! Manuals !! Ext !! Description
|-
| 7-Zip ||  || Official manual || .7z || A file archiver with a high compression ratio.
|-
| DAR ||  ||  || .dar || Archiver to backup large live filesystems, takes care of hard links, extended attributes, sparse files and inode types.
|-
| GNU tar ||  || , info || .tar.compression-type || Supports passing the archive for compression to , , , , , , , , as well as any other custom compression program. See .
|-
| libarchive ||  ||  || .tar.compression-type || Has built-in compression options for bzip2, gzip, lrzip, lzma, lzop, lz4, zstd and xz.
|-
| RAR || ,  ||  || .rar || Both the format and the rar utility are proprietary.
|-
|t2sz||||  || .tar.zst .tzst || Tar archiving utility in C with member-aligned zstd-compression
|-
|tarlz||  ||  || .tar.lz .tlz || Tar archiving utility in C++ with member-aligned lzip compression
|-
| ZIP || ,  || ,  || .zip || Widely used outside of the Linux world.
|-
| Unarchiver ||  || ,  || many || Command-line tool of a Mac application, supports over 40 archive formats.
|-
| ZPAQ ||  ||  || .zpaq || A high compression ratio archiver written in C++, uses several algorithms.
|-
| LHa || ,  ||  || .lzh (on Amiga: .lha) || LZH/LHA archiver, supports the lh7-method.
|-
| WinAce ||  ||  || .ace || Both the ACE file format and the archiving tool are proprietary.
|}

See also #Archiving and compression usage.

## Feature charts
Some of the tools above are capable of handling multiple formats, allowing for fewer installed packages.

## Decompress
{| class="wikitable sortable"
! rowspan="2" | Name !! colspan="5" | File !! colspan="4" | Archive
|-
! gzip !! bzip2 !! LZMA !! xz !! zstd !! ZIP !! RAR !! 7z !! CAB
|-
|  ||  ||  ||  ||  ||  ||  ||   ||  ||
|-
|  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||   ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||  ||  ||  ||  ||
|}

#  can only decompress single member ZIP files.

## Usage comparison
## Archiving only usage
{| class=wikitable
! Name !! Create archive !! Extract archive !! List content
|-
|  ||  ||  ||
|-
|  ||  || {{ic|cpio -i -vd  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

## Archiving and compression usage
{| class=wikitable
! Name !! Compress !! Decompress !! Decompress to stdout !! List content
|-
| 7z ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
| ,  ||  ||  ||  ||
|-
|  ||  ||  ||  || minimal:  verbose:
|-
|}

## Convenience tools
See also Bash/Functions#Extract.

*
*
*
*
*
*
*
*

## Determining archive format
To extract an archive, its file format needs to be determined. If the file is properly named you can deduce its format from the file extension.

Otherwise you can use the  tool, see .

## Esoteric, rare or deprecated tools
{| class=wikitable
! Name !! Packages !! Ext !! Description
|-
| ARC ||  || .arc, .ark|| Was very popular during the early days of the dial-up BBS. Superseded by ZIP.
|-
| ARJ ||  || .arj|| An archiver used on DOS/Windows in mid-1990s. This is an open source clone.
|-
| Cabinet || ,  || .cab, .exe || A variety of installation technologies in Windows use the CAB format.
|-
| compress ||  || .Z || The de facto standard UNIX compression utility to success the Huffman-based  before gzip become a thing.
|-
| Inno Setup ||  || .exe || Installers created by Inno Setup.
|-
| PAR2 ||  || .par2|| Parity archiver for increased data integrity. See also Parchive.
|-
| shar ||  || .shar || Creates self-extracting archives that are valid shell scripts.
|-
| Zoo ||  || .zoo || Was mostly popular on the OpenVMS operating system before PKZIP became popular.
|}

## File system compression
Some file systems support on-the-fly compression of file data:

* Btrfs can be configured to compress individual files, directories, or entire volumes by default.
* On ZFS, compression can be enabled on pools or file systems.

## Device mapper compression
The open-sourced VDO project was integrated into the Linux kernel project, which provides a deduplication and compression device mapper layer in the interest of increasing storage efficiency. A userspace tools for managing VDO volumes is available in the AUR:

## Compression libraries
*
*
*
*

## Troubleshooting
## Garbled file names when extracted
See Character encoding#Troubleshooting.
