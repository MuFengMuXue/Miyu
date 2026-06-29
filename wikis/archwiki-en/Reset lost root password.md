# Reset lost root password

This guide will show you how to reset a forgotten root password. Several methods are listed to help you accomplish this.

## Using sudo
If you have installed sudo and have configured permissions for either the  group or a user whose password you recall, you can change the root password by running .

## Using the debug shell
# Append  to the kernel parameters.
# This will do a normal boot but start  which runs a root shell () on . Press  to access it.
# Use the passwd command to create a new password for the root user.
# When done, stop .

## Using bash as init
# Append the  kernel parameter to your boot loader's boot entry.
# Your root file system is mounted as read-only now, so remount it as read/write: .
# Use the passwd command to create a new password for the root user.
# Reboot by typing  and do not lose your password again!

## Using a LiveCD
With a LiveCD a couple methods are available: change root and use the  command, or erase the password field entry directly editing the password file. Any Linux capable LiveCD can be used, albeit to change root it must match your installed architecture type. Here we only describe how to reset your password with chroot, since manual editing the password file is significantly more risky.

## Change root
# Boot the LiveCD and mount the root partition of your main system.
# Use the  command to set the new password (you will not be prompted for an old one).
# Unmount the root partition.
# Reboot, and enter your new password.
