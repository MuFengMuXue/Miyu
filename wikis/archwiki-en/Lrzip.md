# Lrzip

Long Range ZIP (or Lzma RZIP) is a compression program optimised for large files, consisting mainly of an extended rzip step for long-distance redundancy reduction and a normal compressor (LZMA, LZO, gzip, bzip2, or ZPAQ) step. The larger the file and the more memory you have, the better the compression advantage this will provide, especially once the files are larger than 100MB. The advantage can be chosen to be either size (much smaller than bzip2) or speed (much faster than bzip2).

## Installation
Install the  package.

## Usage
## Compression
Compression of directories (recursive) requires lrztar, which first tars the directory, then compresses the single file just like tar does when users compress with gzip or xz ( and , respectively). Note that the compression algorithms are used after the rzip-like precompressing of the archive, instead of e.g. plain LZMA compression in normal "LZMA compressed archives".

This will produce an LZMA compressed archive  from a directory named :
 $ lrztar foo

This will produce an LZMA compressed archive  from a file named :
 $ lrzip bar

For extreme compression, add the  switch which enables ZPAQ but takes notably longer than LZMA:
 $ lrztar -z foo

For extremely fast compression and decompression, use the  switch for LZO:
 $ lrzip -l bar

By default, lrzip can use up to your available ram size to remember the file block history. If the file you compress is bigger than that, add the  switch to enable on disk mapping. Note that it will be considerably slower but will handle file of any size:

 $ lrzip -U bar

## Decompression
To completely extract an archived directory:
 $ lrzuntar foo.tar.lrz

To decompress  to :
 $ lrunzip bar.lrz

## Details
Lrzip uses an extended version of rzip, which does a first pass long distance redundancy reduction. The lrzip modifications make it scale according to memory size. The data is then either:

# Compressed by LZMA (default), which gives excellent compression at approximately twice the speed of bzip2 compression
# Compressed by a number of other compressors chosen for different reasons, in order of likelihood of usefulness:
## ZPAQ: Extreme compression up to 20% smaller than LZMA, but ultra slow at compression AND decompression.
## LZO: Extremely fast compression and decompression, which on most machines compresses faster than disk writing making it as fast (or even faster) than simply copying a large file.
## GZIP: Almost as fast as LZO, but with better compression.
## BZIP2: A defacto linux standard of sorts, but is the middle ground between LZMA and gzip and neither here nor there.
# Leaving it uncompressed and rzip prepared. This form improves substantially any compression performed on the resulting file in both size and speed (due to the nature of rzip preparation merging similar compressible blocks of data and creating a smaller file). By "improving" it will either speed up the very slow compressors with minor detriment to compression, or greatly increase the compression of simple compression algorithms.

The major disadvantages are:
# The main lrzip application only works on single files, so it requires the lrztar wrapper to fake a complete archiver.
# It requires a lot of memory to get the best performance out of (as much memory as the size of the data to compress; but see the sliding mmap below), and is not really usable (for compression) with less than 256MB. Decompression requires less ram and works on smaller ram machines. Sometimes swap may need to be enabled on these lower ram machines for the operating system to be happy.
# STDIN/STDOUT works fine on both compression and decompression, but larger files compressed in this manner will end up being less efficiently compressed.

The unique feature of lrzip is that it tries to make the most of the available ram in your system at all times for maximum benefit. It does this by default, choosing the largest sized window possible without running out of memory. It also has a unique "sliding mmap" feature which makes it possible to even use a compression window larger than your ramsize, if the file is that large. It does this (with the  option) by implementing one large mmap buffer as per normal, and a smaller moving buffer to track which part of the file is currently being examined, emulating a much larger single mmapped buffer. Unfortunately, this mode can be many times slower.
