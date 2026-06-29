# Kernel live patching

Kernel Live Patching (KLP) allows quick fixes to the kernel space without rebooting the whole system.  Since version 4.0, related patches have been accepted so one can configure their kernel to enable this feature.  Generally, KLP is achieved by the following steps:
# Obtain the source tree of the running kernel
# Prepare the patch against the kernel
# Apply some tools (as follows) to help transform and load the patch

Some projects provide the live patching utilities before KLP was officially supported, such as Oracle's ksplice, SuSE's #kGraft, and Red Hat's #kpatch.  They implemented the KLP functionality in different ways.  The minimalistic functional set of patches that entered the mainstream kernel were derived from kpatch and kGraft.

## kpatch
## Installation
Install  for an appropriate kernel and  for userspace tools.

You can also manually build a kernel that supports kpatch usage, by enabling , , and .

## Usage
Once both packages are successfully built and after reboot, you may

 $ export ROOTDIR=some/dir/aur/linux-kpatch/src/linux-x-y
 $ cd $ROOTDIR

Assume that you have done some modifications and have a patch some.patch (against the source tree after a , not the vanilla kernel of version x.y) in the working directory. Launch the kpatch utility,

 $ kpatch-build -s $(pwd) -v $(pwd)/vmlinux some.patch

This command involves two kernel builds, the original one and the patched one, so it may take a period of time to complete.  After the build is over, there should be a kpatch-some.ko module in the same directory.  And then,

 # insmod kpatch-some.ko

should do the trick.

For further information, please check the manpages or [https://github.com/dynup/kpatch the GitHub repository.

## kGraft
KGraft has not been tested in Arch environment.
