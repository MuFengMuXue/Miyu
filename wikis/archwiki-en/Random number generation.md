# Random number generation

From wikipedia:Random number generation:
:A random number generator (RNG) is a computational or physical device designed to generate a sequence of numbers or symbols that lack any pattern, i.e. appear random.

Generation of random data is crucial for several applications like making cryptographic keys (e.g. for data-at-rest encryption), securely wiping disks, running encrypted Software access points.

## Kernel built-in RNG
The Linux kernel's built-in RNG produces cryptographically secure pseudorandom data.  It works by collecting entropy from various sources, such as hardware RNGs, interrupts, and CPU-based jitterentropy.  No single entropy source is relied on exclusively.  The entropy is extracted using the BLAKE2s cryptographic hash function and used to seed a set of ChaCha20 CRNGs (Cryptographic Random Number Generators) that provide the actual random data.  Entropy continues to be collected, and the CRNGs are periodically reseeded, as long as the kernel is running.

The Linux RNG provides three interfaces for userspace to get random data:

* The  system call
*
*

Historically,  was considered to provide stronger random numbers than .  However, the behavior of  and  has significantly converged over time, and on x86-64 systems they are now equivalent.  Since Arch Linux only supports x86-64,  and  are equivalent on Arch Linux.  (This is true because the presence of the RDTSC instruction on all x86-64 CPUs means that the CPU-based jitterentropy algorithm will always be able to generate entropy, not to mention that most x86-64 CPUs also support RDRAND.)

On other architectures (specifically, architectures that do not have a fast cycle counter), there is one remaining difference between the two:  blocks until the kernel has estimated that the CRNGs are properly initialized, whereas  does not.  Therefore, in the general case, users and applications should still follow the traditional guidance of using  when generating long-term cryptographic keys, or use  which by default behaves similarly to .

Note that because  no longer aims to provide true random data, but rather "just" cryptographically secure random data (which is sufficient for all real-world use cases), reading from it no longer causes the kernel's entropy pool to deplete.  Therefore,  should always contain 256, which is the size of a ChaCha20 key in bits.  Historical documentation that expected larger values in this file, or expected the user to take actions if the value was getting "too low", can be disregarded.

## Alternatives
Applications that do not need cryptographically secure random numbers can simply use a non-cryptographic random number generator, for example .

For applications that do need cryptographically secure random numbers, there generally is no need for anything other than the kernel's RNG.  Historically, the kernel's RNG was fairly slow and did not take advantage of as many entropy sources as it could have.  However, it has since been improved to provide ~400 MB/s throughput on x86-64 and to take advantage of more entropy sources.  Even for cases that need fairly high throughput random numbers, such as securely wiping a disk, simply reading from  works fine.

Cases where it could make sense to not use the kernel's RNG directly include:

* In rare cases, applications need cryptographically secure random numbers with a very high throughput, or with a very low latency where the overhead of a system call would not be tolerable.  A userspace CRNG can solve this problem.  Userspace CRNGs should be seeded from the kernel's RNG to ensure that they are at least as secure as the kernel's RNG, modulo considerations such as reseeding.

* Some applications work in domains where there is already a well-established API for generating cryptographically secure random numbers using a userspace CRNG.  For example, when an application is using OpenSSL, it may make sense to use OpenSSL's .  When an application is written in Java, it may make sense to use .  Usually, the userspace CRNGs underlying these APIs are automatically seeded using the kernel's RNG.

* If you would like to use additional entropy sources that are not already incorporated into the kernel's RNG, it might make sense to not use the kernel's RNG directly.  For example, Haveged can provide random data generated using jitterentropy.  If possible, additional entropy sources should not replace the kernel's RNG, but rather be used in conjunction with it by seeding a userspace CRNG from both the additional entropy source and the kernel's RNG.  It is also possible to write additional entropy to  to cause it to be incorporated into the kernel's RNG, though it may take up to 60 seconds for this to take effect due to the kernel's CRNG reseeding schedule.  Note: the kernel already uses RDSEED and other hardware random number generators as entropy sources.
