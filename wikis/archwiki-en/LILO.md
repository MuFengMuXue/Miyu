# LILO

The LInux LOader, or LILO for short, is a legacy multi-boot loader for Linux systems. In spite of being the standard choice over the course of several years, it has been slowly phased out. As of January 2016, LILO is no longer actively developed.

## Supported file systems
From upstream's readme:
: LILO does not know how to read a file system. Instead, the map installer asks the kernel for the physical location of files (e.g. the kernel image(s)) and records that information. This allows LILO to work with most file systems that are supported by Linux.

In practice, the development of LILO has stopped precisely because of some limitations to that approach, e.g. with Btrfs, GPT, RAID.

## Installation
LILO can be installed with the  package. LILO only works on BIOS systems.

Running the command  (as root) will install LILO to the MBR. Before running the lilo command you should edit  to ensure that the root entry points towards the root partition. If your root partition is on  then the root entry should look like this: . Remember to change the root line for both the 'arch' and the 'arch-fallback' entries.

## Install to partition or partitionless disk
Use the  flag to specify a partition or the whole disk (instead of the implied ) to install LILO to the volume boot record (VBR) instead of the MBR. See  and the answers by Hypnos on the Gentoo forum.

## Configuration
LILO is configured by editing the  file and running  afterwards to apply the new configuration.

As a reminder, consider that LILO needs to be run after every kernel upgrade, otherwise the system is likely to be left in an unbootable state.

More help on setting up LILO can be found in the LILO-mini-HOWTO.

## Sample setup
A typical LILO setup:

You can use  to determine what vga modes you can use.

## Using an image as background
First prepare the background image:

* Open it in GIMP.
* Scale it to 640x480.
* Change it to indexed mode (Image > Mode > Indexed).
* Select Create optimal palette and set it to 16 colours. Choose whatever dithering method suits you.
* Open the "Indexed Palette" dialog. Make note of which colours you want to use for menu text entries, the clock, etc. In your , you refer to the colours by index.
* Export the image as a bmp in your  directory. In Export dialog check option Do not write color space information

Now edit . There are a few options that can be set for your graphical menu. See  for more information.

* bitmap= Set this to the file that you saved above.
* bmp-colors=,,,,,
:These are the colours of the entries in the menu. They refer to the foreground, background, and shadow colours respectively, followed by the same for highlighted text. Do not use spaces. The values used are indices into the colour palette that you discovered in the previous step. If you choose, you can leave a value blank (but do not forget the comma). The default background is transparent, the default shadow is to have none.
* bmp-table=,,,,, This option specifies where the menu is placed. x and y are the character coordinates. You can also suffix them with a p to specify pixel coordinates.
* bmp-timer=,,,, This option specifies the coordinates and colour of the timer that counts down the timeout before booting a default entry. It uses colour indices for the colours, and character (or pixel) coordinates.

For example:

 bitmap=/boot/arch-lilo.bmp
 bmp-colors=1,0,8,3,8,1
 bmp-table=250p,150p,1,18
 bmp-timer=250p,350p,3,8,1

Save , run  as root, and reboot and see how it looks!

## Pacman hook
lilo needs to be run after every kernel update. You can use a pacman hook to automate it. See Pacman#Hooks or .

Make the directory  if it does not already exist.

## Troubleshooting
## Read write error message whilst booting
This error message is caused by a change in mkinitcpio which was in response to this systemd commit. The change causes partitions to be fsck'ed twice when mounted read only. To fix this error edit  and change the 'read only' line to 'read write' for both arch entries.

See this forum thread for more information.

## Devmapper not found error message after kernel upgrade
It is possible that running the  command after a kernel upgrade results in a devmapper not found error. If this is the case run  before running  after a kernel upgrade.
