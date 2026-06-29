Other languages:

[English] • ‎[español](//wiki.manjaro.org/index.php?title=System_Maintenance/es "Mantenimiento del Sistema (14% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-System+Maintenance&language=fr&task=view "Start translation for this language") • ‎[русский](//wiki.manjaro.org/index.php?title=System_Maintenance/ru "Обслуживание системы (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Home Cache]](#Home_Cache)
-   [[3] [Journal and Logs]](#Journal_and_Logs)
    -   [[3.1] [Systemd Journal]](#Systemd_Journal)
    -   [[3.2] [System logs at /var/log/\*]](#System_logs_at_.2Fvar.2Flog.2F.2A)
-   [[4] [Packages and Updates]](#Packages_and_Updates)
    -   [[4.1] [Keeping your System Updated]](#Keeping_your_System_Updated)
    -   [[4.2] [Avoiding Partial Updates]](#Avoiding_Partial_Updates)
    -   [[4.3] [Removing Orphans]](#Removing_Orphans)
    -   [[4.4] [Package Cache]](#Package_Cache)
    -   [[4.5] [Pacnew and Pacsave files]](#Pacnew_and_Pacsave_files)
-   [[5] [Time and Date]](#Time_and_Date)
-   [[6] [See Also]](#See_Also)

# [Overview]

This article contains tips and best practices for keeping your system in optimal condition.

\

# [Home Cache]

The hidden `.cache` folder in your home directory is used by many parts of your system. This includes downloads, thumbnails, desktop resources, and more.\
While it is generally safe to remove everything in your `~/.cache` folder, it may be more advisable to inspect its contents and selectively remove items instead.\

To generate a sorted list of contents and sizes:

[user \$ ][ du -sh \~/.cache/\* [COPY TO CLIPBOARD]]

\

To automatically purge all `.cache` files that have not been accessed in 100 days:

[user \$ ][ find \~/.cache/ -type f -atime +100 -delete [COPY TO CLIPBOARD]]

\

# [Journal and Logs]

Log files & the systemd journal do the same thing in different ways. They keep a record of everything that happens on your system.\
For more information and tips on automated maintenance please see the dedicated page [Limit the size of .log files & the journal](//wiki.manjaro.org/index.php?title=Limit_the_size_of_.log_files_%26_the_journal "Limit the size of .log files & the journal")

## [Systemd Journal]

The journal keeps logs of system activity. This can be important for troubleshooting, but sometimes the log size can grow rather large.

To report the current size:

[user \$ ][ journalctl \--disk-usage [COPY TO CLIPBOARD]]

\

To remove all but the most recent entries by size or time:

[user \$ ][ journalctl \--vacuum-size=50M [COPY TO CLIPBOARD]]

\

[user \$ ][ journalctl \--vacuum-time=2weeks [COPY TO CLIPBOARD]]

\

To set a maximum size for the journal you can uncomment and edit the following line in `/etc/systemd/journald.conf`:

    SystemMaxUse=50M

## [][System logs at /var/log/\*]

While most things use the newer systemd journal (journalctl), there is still some software that uses the older /var/log/ directory.\
For more information and some tips on maintaining it, please see the relevant section of [this page](//wiki.manjaro.org/index.php?title=Limit_the_size_of_.log_files_%26_the_journal#Managing_.2Fvar.2Flog.2F.2A_files "Limit the size of .log files & the journal").

\

# [Packages and Updates]

## [Keeping your System Updated]

On a rolling release distribution it is essential to keep your system fully updated. Manjaro provides a few ways to keep your system updated.

-   You can use the GUI tool [Pamac](//wiki.manjaro.org/index.php?title=Pamac "Pamac") directly or via the update notifier
-   You can use the GUI tool [Octopi](//wiki.manjaro.org/index.php?title=Octopi "Octopi") directly or via the update notifier
-   You can use the [Pamac CLI](//wiki.manjaro.org/index.php?title=Pamac#Updating_the_System "Pamac")
-   You can use the [Pacman CLI](//wiki.manjaro.org/index.php?title=Pacman_Overview#Installing_Updates "Pacman Overview")

## [Avoiding Partial Updates]

**danger**

------------------------------------------------------------------------

Partial updates are not supported under any circumstances

It is of critical importance to ensure you don\'t end up in a state where your system is partially upgraded.\
It is not uncommon for systems in partially updated state to end up in a critical failure state.\
Here are some rules to help you avoid this undesired situation.

-   Don't update the local package database (metadata) without also updating the system
-   You may install a single package using `pacman -S ` but this may yield a 404 error if your metadata is not current
-   Don\'t use `pacman -Sy`, `pacman -Syy`, `pacman -Syuw` as this will update the metadata but not sync the packages to your system
-   Always sync metadata and packages together `pacman -Syu`
-   Don\'t add packages to pacman\'s or pamac\'s ignore list
-   If you just want to check to see what updates are available use the command `checkupdates`. This provides a safe way to check for upgrades to installed packages without pulling metadata at the same time
-   When [switching branches](//wiki.manjaro.org/index.php?title=Switching_Branches "Switching Branches") or [switching mirrors](//wiki.manjaro.org/index.php?title=Pacman-mirrors "Pacman-mirrors") always sync your systems metadata and packages using `pamac update` or `pacman -Syu`
-   If you get 404 in connection with a branch switch you may force sync metadata by doubling the **y** argument `pacman -Syyu`

## [Removing Orphans]

As packages are added, built and removed it is not uncommon to have unneeded dependencies, also called orphans, building up over time. While orphans are not harmful, they take up space on the disk and consume network bandwidth as they are continually updated. Luckily, there are a couple of easy ways to view and remove orphans.

To use pamac follow [this guide](//wiki.manjaro.org/index.php?title=Pamac#Dealing_with_Orphaned_Packages "Pamac").

To use pacman follow [this guide](//wiki.manjaro.org/index.php?title=Pacman_Overview#Viewing_and_Removing_Orphans "Pacman Overview").

## [Package Cache]

By default both pamac and pacman keep a cache of downloaded packages on the system. This can be helpful if you need to copy or downgrade a package.\
But the cache can grow to include dozens of each package resulting in gigabytes of space.

To use pamac follow [this guide](//wiki.manjaro.org/index.php?title=Pamac#Cleaning_the_Cache "Pamac").

To use pacman follow [this guide](//wiki.manjaro.org/index.php?title=Pacman_Overview#Cleaning_the_Cache "Pacman Overview").

## [Pacnew and Pacsave files]

A .pacnew file may be created during a package upgrade to avoid overwriting a file which already exists. A .pacsave file may be created during a package removal, or by a package installation of a package that was removed. These files require manual intervention from the user and it is good practice to handle them regularly. The program `pacdiff` can help manage this process. For example, here is what it looks like when the `/etc/default/grub` grub file has changed:

    DIFFPROG=meld pacdiff -s
    ==> pacnew file found for /etc/default/grub
    :: (V)iew, (S)kip, (R)emove pacnew, (O)verwrite with pacnew, (Q)uit: [v/s/r/o/q]

-   `V` shows the differences between the two files
-   `S` skips to the next change and allows you to deal with it later or manually
-   `R` keeps your existing file and delete the new file
-   `O` overwrites the existing file with the new file
-   `Q` quits the process without making further changes

Unfortunately, there is no perfect road map for how to deal with these files. If you keep the original config file, and the syntax has changed, the program may stop working or fail to use the existing config. If you remove the original file and use the new file without any changes, all your configuration settings can be overwritten. Sometimes, you need to combine pieces from the new and old files to make everything to work. In these situations it is better to integrate the files manually.

For more detailed information, please see review the Arch Wiki [linked below](#See_Also).

\

# [Time and Date]

[![Msm-time-date.png](/images/thumb/f/f4/Msm-time-date.png/350px-Msm-time-date.png)](//wiki.manjaro.org/index.php?title=File:Msm-time-date.png)

[](//wiki.manjaro.org/index.php?title=File:Msm-time-date.png "Enlarge")

Keeping the system time accurate may seem unimportant but certain network related services may malfunction if the time is out of sync.

The easiest way to ensure the time is being properly synchronized is the GUI tool included in **Manjaro Settings Manager** which is pictured to the left. Simply check the box next to \"Set time and date automatically\".

An alternative is to use systemd via the systemd-timesyncd service. This can be easily enabled with one of these commands:

[user \$ ][ timedatectl set-ntp true [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo systemctl enable \--now systemd-timesyncd [COPY TO CLIPBOARD]]

\

# [See Also]

-   The Arch Wiki guide on [System Maintenance](https://wiki.archlinux.org/index.php/System_maintenance)
-   The Arch Wiki guide on [Pacnew and Pacsave](https://wiki.archlinux.org/index.php/Pacman/Pacnew_and_Pacsave) files
-   The [Pacman wiki article](//wiki.manjaro.org/index.php?title=Pacman_Overview "Pacman Overview")
-   The [Pamac wiki article](//wiki.manjaro.org/index.php?title=Pamac "Pamac")

\