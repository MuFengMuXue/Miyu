# IMac Unibody

Despite having Radeon rather than nVidia graphics, this iMac model suffers from a number of graphics-related problems. The problems I have encountered are:
* The screen becomes disabled/turned off when kernel mode setting kicks in.
* After resuming from suspend-to-RAM, the screen cannot be re-enabled even with the fix described below.
* The system produces an interface for controlling a nonexistent backlight in .

## Workaround for the KMS bug
During the initial installation process, it is simplest to add  to your kernel command line when booting from the installation media. I did not attempt to boot in BIOS mode, though I doubt it would make much difference with regards to the black screen. You will need to keep this parameter in your kernel command line until after you have installed a graphical environment, so when you install your desktop environment, be sure to also install . This will allow you to use software rendering and the high-resolution EFI framebuffer until you get the radeon problem sorted out. When you have gotten your graphical environment the way you want, install , and create the following script:

Note: if eDP-1 does not work, try just "eDP." If you can log into the graphical session blindly, you can then use SSH to see the exact name by running .

Make it executable.

Edit your display manager's configuration so that the script runs while the greeter is starting up. I use SDDM, so I configured it like this:

Note that you may need to first create this file by running .

Now, you should be able to remove the  parameter from your kernel command line and reboot with 3D acceleration supported.

## Workaround for suspend-and-resume
Currently, there is no solution to the suspend-and-resume issues although using Legacy boot instead of EFI is worth a try if possible.

## Workaround for the fake backlight control
Add  to your kernel command line and reboot. Your desktop environment should now be able to adjust the screen brightness properly. (Note that you will have to install the  package if you wish to adjust the brightness in Plasma.)

## Suggestions about the boot loader
Because Mac computers do not have a normal UEFI, I advise making your boot loader follow Apple's conventions as much as possible. This will allow you to make the Arch entry in the Option-key boot menu nice and pretty, as well as allowing you to set Arch as the default OS instead of macOS. Here are the rough steps to do this. Consider these instructions a supplement to—not a replacement for—the installation guide. They only detail the steps that deviate from the normal install process.

# Before installing Arch, create a 1 GiB partition in Disk Utility formatted as MacOS Extended (Journaled). Name it "ArchLinux-Boot".
# Run  from the macOS terminal. (Replace X and Y with the disk and partition numbers from .)
# Create a full-sized partition for the root filesystem and optionally a swap partition in Disk Utility as well. The filesystem does not matter for these, as they will be overwritten anyway.
# Boot into the install media (do not forget the workaround for graphics above)
# Use  to change the partition type codes on the root and swap partitions to the proper codes for Linux Filesystem (8300) and Linux Swap (8200).
# Format the partitions with your choice of filesystem.
# Mount your newly-formatted root filesystem on . Create the directories , , and .
# Mount the EFI system partition under
# Mount the HFS+ filesystem you created in Disk Utility under .
# Run . The first set of directories emulates a macOS installation so that it will be picked up by the firmware. The second two are for Linux-specific things, as you will see later.
# Bind-mount  to
# Generate the fstab file. You will probably need to correct the bind-mount fstab entries to use directories that make sense for the installed system rather than the live environment.
# Run  as specified in the main installation guide and chroot into the new system.
# Copy  to  and from there configure systemd-boot as though  were the EFI system partition.  should contain your vmlinuz and initramfs images.
# Create the file  (it should be an empty file). I'm not sure whether this is actually necessary for the firmware to detect the partition as bootable.
# Perform any other needed installation steps, then reboot into the installed system by holding down the option key when the iMac boots.

## iMac12,2 27" 2011
## Sound
The following setting should be used to handle headphone detection correctly:

## Brightness
To adjust the backlight, adjust the values in "radeon_bl1" rather than "acpi_video0."

You can check the maximum value allowed with:

 $ cat /sys/class/backlight/radeon_bl1/max_brightness

And you can set the current brightness with:

 # echo value > /sys/class/backlight/radeon_bl1/brightness

Alternatively, add  to the kernel command line.
