# Haveged

The haveged project is an attempt to provide an easy-to-use, unpredictable random number generator based upon an adaptation of the HAVEGE algorithm. Haveged was created to remedy low-entropy conditions in the Linux random device that can occur under some workloads, especially on headless servers.

## Installation
Install the  package.

Start and enable .

## List available entropy
If you are not sure, whether you need haveged, run:

 # cat /proc/sys/kernel/random/entropy_avail

This command shows you how much entropy your server has collected. If it is rather low (<1000), you should probably install haveged. Otherwise cryptographic applications will block until there is enough entropy available, which eg. could result in slow wlan speed, if your server is a Software access point.

You should use this command again to verify how much haveged boosted your entropy pool after the installation.

## Alternative
Unless you have a specific reason to not trust any hardware random number generator on your system, you should try to use them with the rng-tools first and if it turns out not to be enough (or if you do not have a hardware random number generator available), then use Haveged.

## Virtual machines
As discussed at Is it appropriate to use haveged as a source of entropy on virtual machines?, it can be contested whether haveged provides quality entropy within a virtual environment. Haveged relies on the rdtsc instruction, which may be virtualized within a virtual machine resulting in lower quantity entropy. On some hypervisors, it is possible to disable the virtualization of rdtsc, which would in theory allow haveged to provide higher quality entropy.
