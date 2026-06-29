# Floppy disks

From Wikipedia:

:A floppy disk, also called a diskette, is a disk storage medium composed of a disk of thin and flexible magnetic storage medium, sealed in a rectangular plastic carrier lined with fabric that removes dust particles. Floppy disks are read and written by a floppy disk drive (FDD).

Common tasks with floppy disks are described below, with available tools to accomplish them.

## Installation
## Kernel module
Most of the floppy drives should be supported by stock kernel. The module  is used as a driver for floppy drives (for classical floppy controllers). USB floppy drives do not need this as they appear as standard USB mass storage devices.

The  module might not be loaded by default. In such case, it could be loaded with the following command:

 # modprobe floppy

## Packages
There are two packages in the Arch package repository related with floppy disks:

*
*

In addition, for low level formatting on USB attached floppy drives you will need .

## Common tasks
Here are the commands needed to perform the most common tasks. In all examples is assumed that  is the Linux device for the floppy drive. By default, all these tasks need to be performed as root. Note that USB based floppy drives will show up as  for some varying value of x.

## Low level format
When it comes to floppies (and some very early hard drives) it was possible to perform a "low level format". This would create various markers on the disk for sectors and tracks. This is performed on a level below file systems.

For USB based floppy drives use :

 # ufiformat /dev/sdx

Additional flags can be used to adjust which format to use, by default it uses the same as is already on the disk. Note that USB floppy drives in general only support very few formats (unlike traditional floppy controllers). Supported formats can be listed using

For classical floppy controllers on the motherboard  could perform this, which used to be part of , but is no longer included in the package by default and you would have to rebuild it yourself.

## File system creation
 # mkfs.fat /dev/fd0

## Mount
 # mount -t vfat /dev/fd0 /media/floppy

## Flux images
It is possible to read and write non-native floppy formats (such as Amiga disks on a PC floppy drive) using special hardware adapters that works on the magnetic level (commonly referred to as "flux images"). This is possible as the floppy controller handles most of the low level tasks rather than the drives directly. Note that these do not work with USB floppy drives. While the adapter itself connects to the (modern) PC using USB, it needs to connect to a classic floppy drive with a ribbon cable on the other side.

These adapters also require specialised software to control them. Depending on which such hardware adapter you have one of these packages may be relevant:

* : For the Greaseweazle open hardware project
* : For the FluxEngine open hardware project. Also some support for Greaseweazle.
* : For the proprietary Kryoflux adapter.
* : Open source software to visualise flux images.

## Troubleshooting
## Unable to get diskette geometry
In such case, is probably that the diskette is physically damaged.

## /dev/sg* family: No such file or directory
If the above error occurs, the  module may not be loaded. If it is, run this command to load the module.

 # modprobe sg
