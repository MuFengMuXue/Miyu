# Tcplay

tcplay is a free, fully featured and stable TrueCrypt implementation including multiple keyfiles and cipher cascades.

Source: github project home

## Installation
Install the  package.

## Encrypting a file as a virtual volume
Invoke

 $ losetup -f

to find the first unused loopback device; in this example, .

Create a new container , 20M in size for instance, in the working
directory:

 # fallocate -l 20M foo.tc
 # losetup /dev/loop0 foo.tc
 # tcplay -c -d /dev/loop0 -a whirlpool -b AES-256-XTS

Enter a secure password for the volume, and confirm the query to overwrite
 with the new volume. tcplay will then write random data into the
volume. Map the volume and create a filesystem on it in order to mount

 # tcplay -m foo.tc -d /dev/loop0
 # mkfs.ext4 /dev/mapper/foo.tc
 # mount /dev/mapper/foo.tc /mnt/truecrypt/

To unset the container,

 # umount /mnt/truecrypt
 # dmsetup remove foo.tc
 # losetup -d /dev/loop0

## Mounting an existing container for a user
Consider  the first unused loop device,  the
TrueCrypt container,  the desired mount point. The
user  in this example has  and . The
steps for mounting the container as a virtual volume are:

# Associate loop device with the container
# Map the container to the loop device
# Mount the container in the filesystem

The following commands perform the above actions.

 # losetup /dev/loop0 foo.tc
 # tcplay -m foo.tc -d /dev/loop0
 # mount -o nodev,nosuid,uid=1000,gid=100 /dev/mapper/foo.tc /home/you/truecrypt/

Note, if the container uses ext4 or another filesystem that supports file ownership, the  and  parameters are not needed and will not work. Therefore the third command would be simply:

  # mount -o nodev,nosuid /dev/mapper/foo.tc /home/you/truecrypt/

To reverse them:

 # umount /home/you/truecrypt/
 # dmsetup remove foo.tc
 # losetup -d /dev/loop0

## Using tcplay-helper
The tcplay-helper script simplifies the process of creating, mounting and unmounting tc-play containers. The script is basic, but should work fine for most users wanting to work with simple secure tc-play containers.

The following command creates a 3Mb container called foo.tc.

 # tcplay-helper create foo.tc 3M

To mount the container file we can either mount it as root with the following command. The container will be mounted under /mnt/truecrypt/

 # tcplay-helper open foo.tc

Alternatively, we can supply a username to mount the container as.

 # tcplay-helper open foo.tc archie

Finally, to close the container this command does the trick.

 # tcplay-helper close foo.tc
