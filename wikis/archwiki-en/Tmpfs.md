# Tmpfs

tmpfs is a temporary filesystem that resides in memory and/or swap partition(s). Mounting directories as tmpfs can be an effective way of speeding up accesses to their files, or to ensure that their contents are automatically cleared upon reboot.

## Usage
Some directories where  is commonly used are /tmp, /var/lock and /var/run. Do not use it on /var/tmp, because that directory is meant for temporary files that are preserved across reboots.

Arch uses a tmpfs  directory, with  and  simply existing as symlinks for compatibility. It is also used for  by the default systemd setup and does not require an entry in fstab unless a specific configuration is needed.

 2.2 and above expects tmpfs to be mounted at  for
POSIX shared memory. Mounting tmpfs at  is handled automatically by systemd and manual configuration in fstab is not necessary.

Generally, tasks and programs that run frequent read/write operations can benefit from using a tmpfs directory. Some applications can even receive a substantial gain by offloading some (or all) of their data onto the shared memory. For example, relocating the Firefox profile into RAM shows a significant improvement in performance.

## Examples
By default, a tmpfs partition has its maximum size set to half of the available RAM, however it is possible to overrule this value.
To explicitly set a maximum size, in this example to override the default  mount, use the  mount option:

To specify a more secure mounting, specify the following mount option:

See the  man page and Security#File systems for more information.

Reboot for the changes to take effect. Note that although it may be tempting to simply run  to make the changes effective immediately, this will make any files currently residing in these directories inaccessible (this is especially problematic for running programs with lockfiles, for example). However, if all of them are empty, it should be safe to run  instead of rebooting (or mount them individually).

After applying changes, verify that they took effect by looking at  and using :

The tmpfs can also be temporarily resized without the need to reboot, for example when a large compile job needs to run soon. In this case, run:

 # mount -o remount,size=4G /tmp
Or resize based on RAM:
 # mount -o remount,size=80% /tmp

## Disable automatic mount
Under systemd,  is automatically mounted as a tmpfs, if it is not already a dedicated mountpoint (either tmpfs or on-disk) in . To disable the automatic mount, mask the  systemd unit.

Files will no longer be stored in a tmpfs, but on the block device instead. The  contents will now be preserved between reboots (they are still cleaned up after 10 days though), which might not be the desired behavior. To regain the previous behavior and clean the  directory automatically when restarting, consider using :

## Troubleshooting
## Opening symlinks in tmpfs as root fails
Considering  is using tmpfs, change the current directory to , then create a file and create a symlink to that file in the same  directory.  Permission denied errors are to be expected when attempting to read the symlink due to  having the sticky bit set.

This behavior can be controlled via  or simply via sysctl: . See Sysctl#Configuration to make this permanent.

## Tips and tricks
## Allocate more memory to accommodate profiles in /run/user/xxxx
The standard way of controlling the size of tmpfs in  is the  directive in  (see  for more). By default, 10% of physical memory is used but one can increase it safely. Remember that tmpfs only consumes what is actually used; the number specified here is just a maximum allowed.
