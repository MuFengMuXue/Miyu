[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Fstab+-+Use+SystemD+automount&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Fstab_-_Use_SystemD_automount "Fstab - Use SystemD automount (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Fstab_-_Use_SystemD_automount/tr "Fstab - SystemD automount'u kullan (43% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Fstab_-_Use_SystemD_automount/es "Fstab - usar el montaje automático de SystemD (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Fstab_-_Use_SystemD_automount/fr "Fstab - Utilisation du montage automatique SystemD (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Fstab_-_Use_SystemD_automount/ru "Fstab - использование автомонтирования SystemD (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Fstab_-_Use_SystemD_automount/zh-cn "Fstab - Use SystemD automount/zh-cn (5% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [A suitable problem example]](#A_suitable_problem_example)
-   [[3] [How do you do use it?]](#How_do_you_do_use_it.3F)
-   [[4] [Speed up your boot]](#Speed_up_your_boot)

### [Introduction]

I found a combination of systemd options (on the ArchWiki [\[1\]](https://wiki.archlinux.org/index.php/Systemd#Automount)) that can be used in the /etc/fstab when mounting storage devices \--be they internal, external, or network shares.

The magic (to me) that these mount options bring is that if a network share or an external drive that is being called via /etc/fstab is not present, they save your machine from hanging for a minute or two during the boot process.

A device called this way via /etc/fstab is mounted the first time data is attempted to be accessed from it. Only on this first mount is there any (minor) noticeable delay, when compared to having the device mounted the \"old\" way.

### [A suitable problem example]

I have a ReadyNAS Duo v1, which is connected to my LAN. These days I quite often turn it off as it doesn\'t need to run perpetually.

A problem that this causes is that if I forget to comment out the NFS share(s) that I\'m using from the /etc/fstab file, I have to wait for a minute or two during the boot process whilst the system repetitively tries to make a connection.

I attempted to get AutoFS [\[2\]](https://wiki.manjaro.org/index.php?title=Using_autofs_(automount)_with_NFS)to work for me. I got close but I just wasn\'t allowed to see the files on the NFS NAS share.

So then I found the following extremely simple & effective solution. (Wish I had of done this one first, as it would have saved me a couple of hours of a loosing battle!)

### [][How do you do use it?]

Add the following to the beginning of the options section in your /etc/fstab, the numbers at the end are a time limit for how long it should try to make a connection before giving up & moving on:

/etc/fstab

    noauto,x-systemd.automount,x-systemd.device-timeout=10

\
After I added the above to the following line in my fstab:

/etc/fstab

    192.168.1.15:/media-2 /mnt/NAS-media-2 nfs noauto,x-systemd.automount,x-systemd.device-timeout=10,timeo=14,hard,intr,noatime 0 0

\
I could boot Manjaro whilst the ReadyNAS\' Cat-6 network cable was unplugged, & there was NO noticeable delay. After the system was booted, I plugged the cable in & then called the NFS share /media-2 in Worker & it read the drive & listed the contents.

After that I unplugged the drive, which had Worker (my file manager of choice) looking for it as I hadn\'t changed out of the the media-2 directory. When I plugged the cable back in, it took \~10 seconds or so & then Worker automatically re-listed the contents or this very large partition that has well over 2000 directories, each holding multiple files.

### [Speed up your boot]

If you have a very large /home & the boot process is held up when a scheduled fsck takes place (really not a big problem if you are using ext4), you can add the **x-systemd.automount** section to the options section of the line in your fstab for /home like so:

/etc/fstab

    UUID=<id.number> /home noauto,x-systemd.automount,ext4 defaults 0 1

This will allow services that do not depend on /home to start while /home is checked by fsck. Mounting /home when it is first accessed, the kernel will buffer all file access to /home until it is ready.