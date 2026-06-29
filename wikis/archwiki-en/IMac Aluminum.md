# IMac Aluminum

From Wikipedia:
: In August 2007, Apple introduced a complete redesign of the iMac, featuring an aluminum, glass and plastic enclosure. There is only one visible screw on the entire computer, located at the base of the iMac for accessing the memory slots. It has a black, plastic backplate that is not user-removable.

## Deleting macOS
Keeping a small macOS partition allows you to do firmware updates.

You can also use an external USB or Firewire drive with which to boot OS X for the firmware updates, and possibly even via optical drive.

## Install additional boot loader
Apple computers have a built-in boot loader that can be accessed by holding down the  key when switched on. This allows you to boot from CD, HDD and via WiFi. If your iMac has a separate EFI system partition, this menu will also allow you to boot Arch Linux directly (follow these instructions: GRUB/Tips and tricks#GRUB standalone). This built-in boot loader sometimes has problems booting from USB, so it might be a good idea to  install rEFInd on your OS X partition. You will probably want to lower the timeout and make Linux the default option, for that you must edit the  file (See REFInd#Configuration).

After successfully installing Arch and Grub you may remove rEFInd (first make sure your stand-alone UEFI app shows up in the Apple boot loader). To change the default boot-option to Arch Linux, you need to bless the earlier created stand-alone UEFI app. It is best to rename the created  to , then run the following command from macOS, after mounting the EFI system partition:

 # bless --folder=/Volumes/EFI --file=/Volumes/EFI/efi/BOOT/BOOTX64.EFI --setBoot

When booting through the Apple boot loader (instead of rEFInd) you will be booting in full UEFI mode, instead of BIOS compatibility. This means you will probably need to boot your archlinux-fallback image the first time; and regenerate the initramfs to successfully switch from BIOS to UEFI.

## Partitioning & Filesystems
There are multiple ways to repartition the iMac drive, my favourite (probably because it is the easiest & being graphical it is most likely the safest) is to boot the Ubuntu 7.10 (or later) LiveCD & run GParted from the desktop menu.  I have shrunk the OS X, HFS+ partition, created Ext3, JFS & Linux Swap partition, deleted & moved partitions on the iMac using GParted & the Ubuntu LiveCD.  Great stuff!
The only present limitation that GParted has with the HFS+ file system, is that it can only shrink the HFS+ file system & can not enlarge it.  I'm sure it will not be too long & this limitation will not exist either.

Just a note on using GParted, or any other GUI type of partition management tool, it is generally accepted to be good safe practice to only Apply ONE process at a time.  What that means for those unfamiliar with GParted (& the other applications of it's ilk) is you can give it multiple instructions which it stores up until you hit the "Apply" button, after which it goes through the instructions one after the other.  If this does not make sense now, it very quickly will on using GParted.

My iMac partition scheme is as follows:

Partition...Filesystem......Size.........Mountpoint

sda1 ........ *FAT32* ....... 200Mb .... EFI system partition - While the ESP looks like a FAT32 volume, it is actually an EFI file system, which you want to know how to replace before you delete it.  This means do not delete it unless you are sure that you know what you are doing, as it may become essential to Apple firmware updates in the future.  Currently the ESP is empty & the firmware boots OS X directly!?  At least it is only 200Mb's wasted drive space, though more importantly it counts as one of the four partitions that can be seen by Apple's newly adopted GPT partitioning scheme.  More on GPT in the following paragraph.

sda2 ......... HFS+ ........... 50Gb ..... OS X - After thinning out OS X some & keeping tools I use plus iWork, CrossOver Games & Guild Wars, I have about 25Gb of free space to play with here, & for the odd game that may arrive in the future (Guild Wars 2). :D

sda3 ......... Ext3 ............ 15Gb ...... / - Arch - there is currently 12Gb free, it is a new install though.

sda4 ......... JFS .............. 30Gb ...... /home - that should be more than enough space for me there, & I can always resize with GParted.

sda5 ......... Linux Swap .... 2Gb ..... swap - rarely if ever used, but I have the space. It is questionable as to whether this partition needs to exist at all.

Having now used Arch on the iMac with 1GB of RAM for some months I deleted the /swap partition, as for my uses it was never needed.

sda6 ......... Ext3 ............ 200Gb ...... /thevoid - storage for video's music, unsafe backup, whatever...

## Accessing the Ext2/3 file system from OS X
I have been using the ExtFS for Mac from Paragon-Software, it is a commercial package that is simple to install, configure & auto mounts any Ext2/3 file system partitions in a read/write fashion when you boot up OS X, 10.4.11 or later on an Intel Mac.  It has been working superbly for me, to the point that I have reformatted my 200GB partition called /thevoid from JFS to Ext3 to give me access to it from OS X.  For anyone interested you can get a trial version on the Paragon-Software website.

There is also a free software application that is apparently somewhat outdated, but works with Ext2/3 & is working with OS X, 10.5, its name is ext2fsx.  I have not used ext2fsx so I cannot speak about it from experience.

## The GPT partitioning scheme that Apple uses
used to limit OS X, to only being able to use 4 partitions from which you could boot a system. If you have not allowed your older Mactel, Apple machines to upgrade for quite some time then their firmware is still suffering under this limitation (I'm told) & you should be aware of this fact.

Therefore you need to be sure to install your boot loader i.e. GRUB/Lilo, & any other partition that you may want OS X, to see (like a shared FAT32 data drive) on sda3 & sda4, Windows must also be on sda3 or sda4.

Partitions beyond Apple's (previously) imposed limit of 4 can still be created & used, e.g. Linux Swap, & other partitions, but they will not be accessible by OS X, or directly bootable, though I see no reason why a boot loader like GRUB positioned on sda3 or sda4 could not boot other OS's on partitions numbered greater than sda4.

This certainly does place limitations on what we can do if we do not allow our systems to accept the appropriate Apple online upgrades.

If you require more than this limited scheme will allow you, you could do away with OS X, & set up the drive on MBR only, using an external drive with OS X on it to update the firmware.

For those that DO accept the online upgrades from Apple, it would seem that you can now place GRUB, Lilo or any other boot loader in partitions beyond the 4th. I say "would seem", as I have been told this (& not read the technical documentation), not read it, & am not prepared to test it no "my" sacrosanct Arch machine. :)

The above section will be severely modified, when I have confirmed that Apple have indeed made these changes to their firmware.

So just to sum up, if you are using a machine with out of date firmware: & you have need to use sda3 & sda4, be sure to put any swap partitions on a partition number greater than sda4.  Also, it is worth considering not using a swap partition at all, as the only computers running Linux/BSD with 1 gigabyte of RAM that use their swap file are doing intensive specialized work such as video editing, sound recording/editing, 3D modelling...

## rEFIt Re-sync
When partitioning is finished you must restart the iMac & re-sync your partitions with rEFIt, which is quick & easy:  You choose to start the partitioning tool in the rEFIt boot-menu & follow the very simple instructions there.
rEFIt may prefer to have partitions in numerical order on the drive, i.e. sda1, sda2, sda3, sda4, sda5, sda6 ... & not shuffled.  This is unconfirmed, any feedback on the subject will be appreciated.

Then reboot & hold down the C key, or wait as I do for the rEFIt boot-menu to appear & choose to boot the Arch install CD.

This is not necessary when booting through EFI.

## Controlling the screen backlight and brightness
The iMac lacks physical buttons for controlling the backlight of the screen. Depending on the version/model of the computer and how Linux is booted, the brightness of the backlight may or may not be easily controllable. See Backlight for various options.

## backlight.c
Below is the C code for a little program that adjusts the brightness on many LCD Apple screens (I have been using it now for over 3 years).  It is easy to compile & setup using the following instructions.

The instructions follow:

Copy & paste the C code (found below these instructions) to your .  Save the code as a file, .

Now open a terminal in the directory where  is located.

Type the following in the Terminal:

 gcc -o backlight backlight.c

You now have a program called . It should adjust the brightness.

To change the brightness, you have to have direct access to video memory, which means that you have to be superuser (root).

Type , then your root password when prompted.

Now test the program by typing:

 ./backlight 10

in the terminal.

You can give it values from 1 to 15. Find a value you like.

Now enter the following in the Terminal:

 cp backlight /usr/local/bin/

Which copies the program to the standard location for user installed programs.

Next, to run it at startup. Still as root, edit . Add a line saying , where  is the number code you want for the brightness.

That should do it.

Source:

 /*
 * Apple Macbook Pro LCD backlight control
 *
 * Copyright (C) 2006 Nicolas Boichat
 * Copyright (C) 2006 Felipe Alfaro Solana
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
 *
 */

 #include
 #include
 #include

 void init()
 {
     if (ioperm(0xB2, 0xB3, 1) > 4;
     return t;
 }

 int calculate_new_value(const char *arg)
 {
     int val, new = atoi(arg);

     if (arg[0 == '+' || arg== '-')
         val = new + get_current_value();
     else
         val = new;

     if (val > 15)
         val = 15;
     else if (val  2)
     {
         printf("Usage:\n");
         printf("%s : read current value\n", argv[0);
         printf("%s value : write value argv[0);
         exit(1);
     }

     init();

     if (argc < 2)
     {
         printf("Current value : %d\n", get_current_value());
         exit(0);
     }

     if (argc == 2)
     {
         int value = calculate_new_value(argvoutb(0x04 | (value << 4), 0xB3);
         outb(0xBF, 0xB2);
         printf("new value: %d\n", value);
     }

     return 0;
 }

## Getting sound to work right
Sound does not always work nice out of the box using Linux on an iMac. For instance, the sound can appear "thin" or tinny with too much treble and too little base due to the built in subwoofer being muted by default or the OS may not detect that the headphones have been plugged in. The fixes are generally to load sound drivers with extra model flags specifying relevant iMac model by manipulating /etc/modprobe.d/sound.conf or /etc/modprobe.d/modprobe.conf, reload corresponding modules and use  to make sure all desired channels are not muted.

## The iMac 20" & 24" models
Add the following to /etc/modprobe.d/sound.conf

## The imac7,1 model
The option above may produces tiny sound on imac7,1. To have OSX like rich sound on imac 7,1, add following to /etc/modprobe.d/modprobe.conf

Using the above gives a workable alsamixer.  I have found that using VLC & its mixer is very helpful when watching DVD's. I have not tested the line out or mic, though I believe that they are working properly with this configuration.

## Troubleshooting
If you experience weird boot freeze just after boot loader (basically after Grub loaded Linux, which you can verify by appending  to the Linux command line), then you may fix the problem by resetting the PRAM (press  just after boot), and resetting the power management system (by unplugging your iMac for 15 seconds, then plugging it back, waiting 5 seconds, and then powering it up).
