# Documentation / Ch Checksumming

Data and metadata are checksummed by default. The checksum is calculated before writing and verified after reading the blocks from devices. The whole metadata block has an inline checksum stored in the b-tree node header. Each data block has a detached checksum stored in the checksum tree.

> [!NOTE]
> Since a data checksum is calculated just before submitting to the block device, btrfs has a strong requirement that the corresponding data block must not be modified until the writeback is finished.
>
> This requirement is met for a buffered write as btrfs has the full control on its page cache, but a direct write (`O_DIRECT`) bypasses page cache, and btrfs can not control the direct IO buffer (as it can be in user space memory). Thus it's possible that a user space program modifies its direct write buffer before the buffer is fully written back, and this can lead to a data checksum mismatch.
>
> To avoid this, kernel starting with version 6.14 will force a direct write to fall back to buffered, if the inode requires a data checksum. This will bring a small performance penalty. If you require true zero-copy direct writes, then set the `NODATASUM` flag for the inode and make sure the direct IO buffer is fully aligned to block size.

There are several checksum algorithms supported. The default and backward compatible algorithm is *crc32c*. Since kernel 5.5 there are three more with different characteristics and trade-offs regarding speed and strength. The following list may help you to decide which one to select.

CRC32C (32 bits digest)
Default, best backward compatibility. Very fast, modern CPUs have instruction-level support, not collision-resistant but still good error detection capabilities.

XXHASH (64 bits digest)
Can be used as CRC32C successor. Very fast, optimized for modern CPUs utilizing instruction pipelining, good collision resistance and error detection.

SHA256 (256 bits digest)
Cryptographic-strength hash. Relatively slow but with possible CPU instruction acceleration or specialized hardware cards. FIPS certified and in wide use.

BLAKE2b (256 bits digest)
Cryptographic-strength hash. Relatively fast, with possible CPU acceleration using SIMD extensions. Not standardized but based on BLAKE which was a SHA3 finalist, in wide use. The algorithm used is BLAKE2b-256 that's optimized for 64-bit platforms.

The *digest size* affects overall size of data block checksums stored in the filesystem. The metadata blocks have a fixed area up to 256 bits (32 bytes), so there's no increase. Each data block has a separate checksum stored, with additional overhead of the b-tree leaves.

Approximate relative performance of the algorithms, measured against CRC32C using implementations on a 11th gen 3.6GHz intel CPU:

<table>
<thead>
<tr>
<th>Digest</th>
<th>Cycles/4KiB</th>
<th>Ratio</th>
<th>Implementation</th>
</tr>
</thead>
<tbody>
<tr>
<td>CRC32C</td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>1.00</p>
</blockquote></td>
<td>CPU instruction, PCL combination</td>
</tr>
<tr>
<td>XXHASH</td>
<td><blockquote>
<p>870</p>
</blockquote></td>
<td><blockquote>
<p>1.9</p>
</blockquote></td>
<td>reference impl.</td>
</tr>
<tr>
<td>SHA256</td>
<td><blockquote>
<p>7600</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>libgcrypt</td>
</tr>
<tr>
<td>SHA256</td>
<td><blockquote>
<p>8500</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>openssl</td>
</tr>
<tr>
<td>SHA256</td>
<td><blockquote>
<p>8700</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>botan</td>
</tr>
<tr>
<td>SHA256</td>
<td><blockquote>
<p>32000</p>
</blockquote></td>
<td><blockquote>
<p>68</p>
</blockquote></td>
<td>builtin, CPU instruction</td>
</tr>
<tr>
<td>SHA256</td>
<td><blockquote>
<p>37000</p>
</blockquote></td>
<td><blockquote>
<p>78</p>
</blockquote></td>
<td>libsodium</td>
</tr>
<tr>
<td>SHA256</td>
<td><blockquote>
<p>78000</p>
</blockquote></td>
<td><blockquote>
<p>166</p>
</blockquote></td>
<td>builtin, reference impl.</td>
</tr>
<tr>
<td>BLAKE2b</td>
<td><blockquote>
<p>10000</p>
</blockquote></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
<td>builtin/AVX2</td>
</tr>
<tr>
<td>BLAKE2b</td>
<td><blockquote>
<p>10900</p>
</blockquote></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td>libgcrypt</td>
</tr>
<tr>
<td>BLAKE2b</td>
<td><blockquote>
<p>13500</p>
</blockquote></td>
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>builtin/SSE41</td>
</tr>
<tr>
<td>BLAKE2b</td>
<td><blockquote>
<p>13700</p>
</blockquote></td>
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>libsodium</td>
</tr>
<tr>
<td>BLAKE2b</td>
<td><blockquote>
<p>14100</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td>openssl</td>
</tr>
<tr>
<td>BLAKE2b</td>
<td><blockquote>
<p>14500</p>
</blockquote></td>
<td><blockquote>
<p>31</p>
</blockquote></td>
<td>kcapi</td>
</tr>
<tr>
<td>BLAKE2b</td>
<td><blockquote>
<p>14500</p>
</blockquote></td>
<td><blockquote>
<p>34</p>
</blockquote></td>
<td>builtin, reference impl.</td>
</tr>
</tbody>
</table>

Many kernels are configured with SHA256 as built-in and not as a module. Up to kernel v6.15 the accelerated versions are however provided by the modules and must be loaded explicitly (`modprobe sha256`) before mounting the filesystem to make use of them. You can check in `/sys/fs/btrfs/FSID/checksum` which one is used. If you see *sha256-generic*, then you may want to unmount and mount the filesystem again. Changing that on a mounted filesystem is not possible.

Since kernel v6.16 the accelerated implementation is always used if available.

Check the file `/proc/crypto`, when the implementation is built-in, you'd find:

``` none
name         : sha256
driver       : sha256-generic
module       : kernel
priority     : 100
...
```

While accelerated implementation is e.g.:

``` none
name         : sha256
driver       : sha256-avx2
module       : sha256_ssse3
priority     : 170
...
```
