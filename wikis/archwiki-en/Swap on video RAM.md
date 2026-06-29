# Swap on video RAM

In the unlikely case that you have very little RAM and a surplus of video RAM, you can use the latter as swap.

## MTD Kernel Subsystem
## Potential benefits
A graphics card with GDDRX SDRAM or DDR SDRAM may be used as swap by using the MTD subsystem of the kernel. Systems with dedicated graphics memory of 256 MB or greater which also have limited amounts of system memory (DDRX SDRAM) may benefit the most from this type of setup.

## Pre-setup
You have to load the modules specifying the PCI address ranges that correspond to the RAM on your video card.

To find the available memory ranges run the following command and look for the VGA compatible controller section (see the example below).

Of most potential benefit is a region that is prefetchable, 64-bit, and the largest in size.

A video card needs some of its memory to function, as such some calculations are needed. The offsets are easy to calculate as powers of 2. The card should use the beginning of the address range as a framebuffer for textures and such. However, if limited or as indicated in the beginning of this article, if two programs try to write to the same sectors, stability issues are likely to occur.

As an example: For a total of 256 MB of graphics memory, the formula is 2^28 (two to the twenty-eighth power). Approximately 64 MB could be left for graphics memory and as such the start range for the swap usage of graphics memory would be calculated with the formula 2^26.

Using the numbers above, you can take the difference and determine a reasonable range for usage as swap memory.
leaving 2^24 (32M) for the normal function (less will work fine)

## Setup
Configure the phram module (3.x kernels used the slram module):

Load the modules on boot:

Create a systemd service:

## Xorg driver config
To keep X stable, your video driver needs to be told to use less than the detected videoram.

The above example specifies that you use 32 MB of graphics memory.

## Troubleshooting
The following command may help you getting the used swap in the different spaces like disk partitions, flash disks and possibly this example of the swap on video ram

## FUSE filesystem
This method works on hardware with OpenCL support using a FUSE filesystem backing a swapfile. See General-purpose computing on graphics processing units for more information.

## Setup
First, install .
Then, create an empty directory as mount point (e.g ).

Now run the following commands to set up the vramfs and a swapfile.

 # vramfs /tmp/vram 256MB -f # Substitute 256M with your target vramfs size
 # mkswap -U clear --size 200M --file /tmp/vram/swapfile # Substitute 200 with your target swapspace size in MiB

Your Swap should now be ready. Run  to check.

See Swap#Swap file for more information.

## Setting swappiness
In the case of swap on VRAM, increasing swappiness may be a good idea. This is especially true when random I/O for the VRAM swapfile is significantly faster than random disk I/O, as the benefit of caching disk reads will outweigh the cost of swapping. For example, if your random disk I/O speed is the same as VRAM swap I/O, you should set swappiness to 100. If VRAM swap I/O is 2x faster than disk I/O, you should set swappiness to 133. See the kernel documentation for how to calculate the swappiness value correctly.

## Troubleshooting
## swapon: /tmp/vram/swapfile: skipping - it appears to have holes.
The swapfile created is not contiguous. A loop device can be set up to work around this issue.

 # cd /tmp/vram
 # LOOPDEV=$(losetup -f)
 # truncate -s 4G swapfile # replace 4G with target swapspace size, has to be smaller than the allocated vramfs
 # losetup $LOOPDEV swapfile
 # mkswap $LOOPDEV
 # swapon $LOOPDEV

## Complete system freeze under high memory pressure
Sometimes, under very high memory pressure, the  process itself may get swapped to the VRAM swap space. This causes a complete deadlock. A fix is to make the process unswappable via cgroups by launching it via a systemd file:
