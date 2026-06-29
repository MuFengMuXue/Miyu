## [FHS Summary]

-   /etc contains system configuration files.
-   /home contains user data ("My Documents") and user config files (E.G. if you have one computer with 2 users and user 1 sets their resolution to HD and user 2 sets it to UHD, that's where this kind of config is kept)
-   /root contains the home directory for the root user.
-   /lib contains shared libraries (known to you as DLLs) that the essential binaries (known to you as EXEs) in /bin and /sbin need to be able to run and where kernel modules are stored.
-   /usr contains the Unix System Resources and is intended to be a read-only directory that stores files that aren't required to boot the system. I.E. This is where sort and grep and assorted brethren / sistern live... In general, when you install additional software from Manjaro's repositories, its binaries, libraries and supporting files go here in their corresponding /usr/bin, /usr/sbin or /usr/lib directories.
-   /opt: contains "optional" software. In general, this is where games install themselves.
-   /run: This directory contains system information data describing the system since it was booted, so don't do funny stuff like mounting anything there in your /etc/fstab.
-   /media: This directory is for mounting external media that needs to be available to the system and where you should create additional directories for each external drive you want mounted concurrently. (so you can have your CD-ROM, DVD drive, Blu-ray drive, External hard disks 1 2 and 3 all mounted simultaneously) 😁