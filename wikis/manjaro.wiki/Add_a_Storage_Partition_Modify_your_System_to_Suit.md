Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Add_a_Storage_Partition_%26_Modify_your_System_to_Suit/tr "Depolama Bölümü Ekleyin ve Sisteminizi Buna Göre Değiştirin (97% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Add_a_Storage_Partition_%26_Modify_your_System_to_Suit/es "Agregar una partición de almacenamiento y modificar su sistema para adaptarlo (3% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Add_a_Storage_Partition_%26_Modify_your_System_to_Suit/ru "Добавление раздела для хранения данных и изменение системы в соответствии с ним (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [The new partition layout]](#The_new_partition_layout)
-   [[2] [Manipulating the Partitions]](#Manipulating_the_Partitions)
-   [[3] [Modifying the system to suit these changes]](#Modifying_the_system_to_suit_these_changes)
-   [[4] [Configure the system to use new default storage directories]](#Configure_the_system_to_use_new_default_storage_directories)
-   [[5] [Creating a /swapfile]](#Creating_a_.2Fswapfile)

## [Introduction]

My storage system was OK when I initially devised it, as it happens, the years have gone by & it had become inefficient & a bit messy. So, time for a makeover. So I spent some hours reorganizing my partitions - 11 -\> 12 hours of GParted work. During this time I removed the /swap partition; enlarged my **/** partition, it still had \~2GB of free space which should have been fine for the way I use my system.

A **/swapfile** \[[\[1\]](https://wiki.manjaro.org/index.php/Swap#Using_a_Swapfile)\] is to replace the /swap partition (see the previous link for the simple how-to on how to create a /swapfile). My /swapfile was located in the **/** partition.

I also shrunk my /home partition as near as small as I could with the size of the data it was holding, so that I could then create a new partition where that data will reside in future.

I had to create a new partition, then reboot into Manjaro, where I moved all of my personal storage data over to the new partition. Then reboot the **GParted live CD** & shrink my /home down to 20GB, which is far larger than it needs to be in my new layout, but I have the disk space to spare, so why not? (I could always change it with GParted in the future if I had to.)

My system then needed to be configured to work with these changes as I will go into below.

### [The new partition layout]

    /boot      - 102MB  ext2  (half full)
    /          - 20GB  ext4  (carries the 4GB /swapfile & still has 5GB free)
    /home      - 20GB  ext4  (12GB free)
    /bdata     - 892GB  ext4

## [Manipulating the Partitions]

**Working with partitions**

------------------------------------------------------------------------

Modifying an existing partition table may cause loss of data. **Always** ensure adequate backup to external storage

Boot Manjaro from a live ISO and use Gparted to delete /swap & to modify the size of all (bar /boot) of the partitions on the 1TB (931.51GB formatted) drive. I had to, delete, shrink, move, expand, create (reboot & move my personal data across from /home to the new /bdata , then reboot GParted) shrink, expand.

As previously mentioned, this took 11 -\> 12 hours. The larger the partition & the more data involved the longer it takes to process a partition.

## [Modifying the system to suit these changes]

I had to comment out the call for mounting the /swap partition in /etc/fstab , change the path buttons in Worker (I\'m probably the only one reading this that uses the wonderful Worker, so, for all that statement is worth\...) to suit the new partition layout. For anyone doing the same thing you need to think about anything that you may have done that needs to be reconfigured to use these new paths (more on this later).

Then in the Terminal I used the blkid command to get the UUID of the new /bdata partition so I could add a call to it into the /etc/fstab :

    [handy@jarmano ~]$ blkid
    /dev/sda1: UUID="41c2c2b3-5ad8-43bc-9bf0-84d3b429127d" TYPE="ext2"
    /dev/sda2: LABEL="big.data" UUID="9fe95af9-529e-4f68-b83c-7fa9e7fb3ba1" TYPE="ext4"
    /dev/sda3: LABEL="my.system" UUID="6dfe5e6b-86b9-4301-b385-8cc3816ada8c" TYPE="ext4"
    /dev/sda4: LABEL="my.home" UUID="b993339d-dbb3-4fbd-adb4-e61baf43cd7f" TYPE="ext4"
    /dev/sdb1: LABEL="store" UUID="05e6f212-4003-430b-a7d9-a53d98fad0b5" TYPE="ext4" PARTUUID="8cb60e1f-8d16-4d9c-bccc-3a2cd5396836"

As you may have noticed, the new partition was given the /dev/sda2: spot (which once belonged to /swap)

I Copied the UUID for the new partition into /etc/fstab & created a call for this new partition, like so:

/etc/fstab

    ...
    UUID=9fe95af9-529e-4f68-b83c-7fa9e7fb3ba1 /data/bdata ext4 defaults      0       1
    ...

Then as root I made the directory /mnt/bdata , so that the new partition is accessible. You can do this in the Terminal like so (replace \<directory.name\> with the name you want to call your new partition:

[root \# ][ mkdir -p /data\<directory.name\> \ \" aria-disabled=\"false\"\>COPY TO CLIPBOARD]

\

Due to GParted doing its work with root permissions we need to change the ownership (owner:group) of the new partition, which we do by modifying the ownership of the directory name (that was created in the last command above) from root:root to \<user.name\>:users. To do that use the following Terminal command:

[root \# ][ chown \<user.name\>:users /data/\<new.partition\'s.name\> \:users /data/\<new.partition\'s.name\> \" aria-disabled=\"false\"\>COPY TO CLIPBOARD]

\

## [Configure the system to use new default storage directories]

Firstly, I had to check both the \~/.bash_profile & the /etc/profile files & modify the **PATH** variables where I had added paths that were now incorrect. Most users here won\'t have changed anything in these two files, though it is just too easy to do, to not check them for safeties sake. When looking at these files, check the PATH line for anything that relates to your moved storage directories. You probably won\'t have any differences unless you added them. These lines in my files follow, you will see where I have replaced the original paths with /mnt/bdata :

\~/.bash_profile

    PATH=$PATH:/mnt/bdata/scripts
    export PATH
    PATH=$PATH:~/games/ut2004
    export PATH
    PATH=$PATH:~/games/ut2004/System
    export PATH

/etc/profile

    # Set our default path
    PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/mnt/bdata/scripts:"
    export PATH

Then I needed to change the paths for what are considered to be the standard default /home/\<user\>/ storage directories - Downloads, Video, Music & so on. I had previously changed these paths, also, I don\'t want to use capital letters in the beginning of their names.

If you have more than one user account on your system, then it would be best to use & edit:

[user \$ ][ nano \~/.config/user-dirs.conf [COPY TO CLIPBOARD]]

\

If the above file doesn\'t exist, create it. Then copy mine (just below), editing it to suit your system/desires. Having only one user account on my Manjaro setup, I delete the previously mentioned file (if it existed anyway) & modify:

[root \# ][ nano /etc/xdg/user-dirs.defaults [COPY TO CLIPBOARD]]

\

As its settings, under these circumstances (not having a \~/.config/user-dirs.conf ) will be global. Mine edited file follows:

\~/.config/user-dirs.conf

    # Default settings for user directories customised by handy :->
    #
    # The values are relative pathnames from the home directory and
    # will be translated on a per-path-element basis into the users locale
    DESKTOP=desktop
    DOWNLOAD=/data/bdata/downloads
    DOCUMENTS=/data/bdata/documents
    MUSIC=/data/bdata/music
    PICTURES=/data/bdata/pictures
    VIDEOS=/data/bdata/videos

Once you have done this, check that you don\'t have new (likely empty) default directories in your \~/ that were created by the above file(s) on boot. Any such void files should be deleted after you have modified either the *user* based **\~/.config/user-dirs.conf** or the *root* based **/etc/xdg/user-dirs.defaults** files. **\~/.bashrc** may need some paths changed as well, depending on what you call from it.

I also had to tell qBittorent, Firefox (& the few other browsers I\'m testing) where their particular download directories had moved to. Any other applications that were set to save data into the documents, or any other directory that has moved (or been created as a default, in either of the two directories above) will need to have their config\'s modified too. & so it goes\...

## [][Creating a /swapfile]

Now, if you do choose to not have a /swap partition but you would still like to have swap space (which of course you can choose to easily have at any time in the future), then there is a very functional option available to you called a /swapfile.