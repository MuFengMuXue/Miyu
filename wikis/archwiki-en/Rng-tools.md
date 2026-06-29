# Rng-tools

The rng-tools is a set of utilities related to random number generation in kernel. The main program is rngd, a daemon developed to check and feed random data from hardware device to kernel entropy pool.

This is mainly useful to increase the quantity of entropy in kernel to make  faster. By default,  is very slow since it only collects entropy from device drivers and other (slow) sources. rngd allows the use of faster entropy sources, mainly hardware random number generators (TRNG), present in modern hardware like recent AMD/Intel processors, Via Nano or even Raspberry Pi.

While Linux itself uses the result from TRNG in , if available, they are only used as a XOR after the entropy is collected by kernel. So , by default, is slow even if you do have a TRNG. rngd feeds  itself, increasing the available entropy by far.

## Installation
Install the  package.
Start and enable .

## Configuration
The configuration file is located in . There is only one option though, that is , the parameters to be passed to the daemon when running it with the included . The default parameter (, or blank) should work in the majority of cases.

By default, rngd will try to automatically detect your TRNG and use it. This is reported to work for Raspberry Pi and Intel Ivy Bridge CPU using the lastest versions of rng-tools. If this does not work, you may manually pass the device file used by your TRNG, as in the below example:

 RNGD_OPTS="-r /dev/my_hw_random_device"

By default rngd fills the entropy pool until at least 2048 bits of entropy are available. This is to avoid the TRNG to dominate the contents of the pool. You can override this setting if you really trust your TRNG. To do this, pass  to , for example (4096 is the maximum size of kernel's entropy pool by default, you should not pass a value greater than the maximum either). Doing so may increase the performance of  even further, at the expense of maybe lower random number quality. However, it should be noted that the default setting is already sufficient for the majority of user cases.

## Testing and usage
You may test if rngd is working before enabling its service by running:

 # rngd -f

A simple test to see if everything is working as it should is to run (in another terminal) the following dd command:

 $ dd if=/dev/random of=/dev/null bs=1024 count=1 iflag=fullblock

Without rngd, the above command will take lots of time to run. With rngd working properly, the result should be almost instantaneous:

 1+0 records in
 1+0 records out
 1024 bytes (1.0 kB, 1.0 KiB) copied, 0.0199623 s, 51.3 kB/s

A speed of around 50 kB/s in dds output shows that everything is working properly. For comparison, without rngd you probably would get 0.0 kB/s (since the speed is too low).

Another interesting test is to run rngtest, to check the data using FIPS 140-2 tests:

It is normal for any random number generator to fail in a small number of tests in 1000 passes, however if the number of failures is too great (like 10), probably there is something wrong.

After that, you can start/enable the .
