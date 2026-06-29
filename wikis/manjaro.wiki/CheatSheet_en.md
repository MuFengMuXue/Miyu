[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-CheatSheet&language=en&action=page&filter= "Special:Translate")

Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=CheatSheet/de "Spickzettel (96% translated)") • ‎[English](//wiki.manjaro.org/index.php?title=CheatSheet "CheatSheet (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=CheatSheet/tr "Hile Sayfası (12% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=CheatSheet/ru "Шпаргалка (100% translated)")

# [Commands CheatSheet for Manjaro]

## Contents

-   [[1] [Commands CheatSheet for Manjaro]](#Commands_CheatSheet_for_Manjaro)
    -   [[1.1] [Locating and Installing Packages]](#Locating_and_Installing_Packages)
        -   [[1.1.1] [Using Pamac CLI]](#Using_Pamac_CLI)
        -   [[1.1.2] [Using native pacman]](#Using_native_pacman)
    -   [[1.2] [Maintenance]](#Maintenance)
    -   [[1.3] [AUR]](#AUR)
    -   [[1.4] [Access rights]](#Access_rights)
    -   [[1.5] [Files and Directories]](#Files_and_Directories)
    -   [[1.6] [Network]](#Network)
    -   [[1.7] [System and Screen]](#System_and_Screen)
-   [[2] [See Also]](#See_Also)

### [Locating and Installing Packages]

#### [Using Pamac CLI]

Install packages

[user \$ ][ pamac install \[PackageName\] [COPY TO CLIPBOARD]]

\
Uninstall packages

[user \$ ][ pamac remove \[PackageName\] [COPY TO CLIPBOARD]]

\
Search for a package

[user \$ ][ pamac search \[PackageName\] [COPY TO CLIPBOARD]]

\
Update installed packages

[user \$ ][ pamac upgrade [COPY TO CLIPBOARD]]

\
Check for updates

[user \$ ][ pamac checkupdates [COPY TO CLIPBOARD]]

\

#### [Using native pacman]

Install packages

[user \$ ][ sudo pacman -Syu \[PackageName\] [COPY TO CLIPBOARD]]

\
Uninstall packages

[user \$ ][ sudo pacman -Rns \[PackageName\] [COPY TO CLIPBOARD]]

\
Search for a package

[user \$ ][ pacman -Ss \[PackageName\] [COPY TO CLIPBOARD]]

\
Update installed packages

[user \$ ][ sudo pacman -Syu [COPY TO CLIPBOARD]]

\
Check for updates

[user \$ ][ sudo pacman -Syu [COPY TO CLIPBOARD]]

\

### [Maintenance]

Generates a random mirrorlist for the users and sort them by their current access time.

[user \$ ][ sudo pacman-mirrors \--fasttrack [COPY TO CLIPBOARD]]

\
Generate cache list

[user \$ ][ du -sh \~/.cache/\* [COPY TO CLIPBOARD]]

\
Purge files not accessed in 100 days

[user \$ ][ find \~/.cache/ -type f -atime +100 -delete [COPY TO CLIPBOARD]]

\
Report journal current size

[user \$ ][ journalctl \--disk-usage [COPY TO CLIPBOARD]]

\
Remove but recent entries by size or time

[user \$ ][ journalctl \--vacuum-size=50M [COPY TO CLIPBOARD]]

\

[user \$ ][ journalctl \--vacuum-time=2weeks [COPY TO CLIPBOARD]]

\
Check for orphaned packages

[user \$ ][ pamac list -o [COPY TO CLIPBOARD]]

\
Remove all orphans

[user \$ ][ pamac remove -o [COPY TO CLIPBOARD]]

\
Remove all packages except the latest 3 versions

[user \$ ][ pamac clean \--keep 3 [COPY TO CLIPBOARD]]

\

### [AUR]

Search for package

[user \$ ][ pamac search -a \[PackageName\] [COPY TO CLIPBOARD]]

\
Build the package

[user \$ ][ pamac build \[PackageName\] [COPY TO CLIPBOARD]]

\

### [Access rights]

Execute command as root

[user \$ ][ sudo \[command\] [COPY TO CLIPBOARD]]

\
Empty password cache

[user \$ ][ sudo -k [COPY TO CLIPBOARD]]

\
Change user password

[user \$ ][ passwd username [COPY TO CLIPBOARD]]

\
Change owner and group of file

[user \$ ][ chown \[owner\]:\[group\] -c \[file\] [COPY TO CLIPBOARD]]

\
Change file permissions

[user \$ ][ chmod \[permissions\] -c \[file\] [COPY TO CLIPBOARD]]

\

Set permissions in octal mode: 4(read) 2(write) 1(execute)

Example: 755 read-write-execute for owner and read-execute for group and others

Display files and permissions \[of directory\]

[user \$ ][ ls -lh \[dir\] [COPY TO CLIPBOARD]]

\

### [Files and Directories]

Change the working directory

[user \$ ][ cd \[dir\] [COPY TO CLIPBOARD]]

\
Change to parent directory

[user \$ ][ cd .. [COPY TO CLIPBOARD]]

\
List directory contents

[user \$ ][ ls -l [COPY TO CLIPBOARD]]

\
List also hidden files

[user \$ ][ ls -la [COPY TO CLIPBOARD]]

\
Copy file

[user \$ ][ cp \[file\] \[target\] [COPY TO CLIPBOARD]]

\
Copy directory **recursively**

[user \$ ][ cp -r \[directory\] \[target\] [COPY TO CLIPBOARD]]

\
Move or rename file/directory

[user \$ ][ mv \[source\] \[target\] [COPY TO CLIPBOARD]]

\
Remove directory **recursively**

[user \$ ][ rm -r \[dir\] [COPY TO CLIPBOARD]]

\
Create symbolic link

[user \$ ][ ln -s \[target\] \[link\] [COPY TO CLIPBOARD]]

\
Mount filesystem

[user \$ ][ mount -t \[type\] \[/dev/sdx9\] \[mountpoint\] [COPY TO CLIPBOARD]]

\
Mount ISO image

[user \$ ][ mount -o loop \[iso\] \[mountpoint\] [COPY TO CLIPBOARD]]

\
Home directory of user

[user \$ ][ cd /home/\$USER [COPY TO CLIPBOARD]]

\

[user \$ ][ cd \~ [COPY TO CLIPBOARD]]

\
Directory with global configurations

[user \$ ][ cd /etc [COPY TO CLIPBOARD]]

\

### [Network]

Display network information

[user \$ ][ nmcli [COPY TO CLIPBOARD]]

\
List wireless access points

[user \$ ][ nmcli c [COPY TO CLIPBOARD]]

\
Enable firewall \[package Community: ufw\]

[user \$ ][ ufw enable [COPY TO CLIPBOARD]]

\
Allow/deny all incoming traffic

[user \$ ][ ufw default \[allow/deny\] [COPY TO CLIPBOARD]]

\
Displays firewall status and rules

[user \$ ][ ufw status [COPY TO CLIPBOARD]]

\
Allows/deny incoming traffic on the specified port

[user \$ ][ ufw \[allow/deny\] \[port\] [COPY TO CLIPBOARD]]

\
Allows/deny incoming traffic from specified IP address

[user \$ ][ ufw \[allow/deny\] from \[ip\] [COPY TO CLIPBOARD]]

\

### [System and Screen]

Display kernel version

[user \$ ][ uname -r [COPY TO CLIPBOARD]]

\
Display long kernel version

[user \$ ][ uname -a [COPY TO CLIPBOARD]]

\
Report file system disk space usage

[user \$ ][ df \[/\] \[/home\] [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo btrfs filesystem usage -h \[/\] [COPY TO CLIPBOARD]]

\
Display system tasks

[user \$ ][ top [COPY TO CLIPBOARD]]

\

[user \$ ][ htop [COPY TO CLIPBOARD]]

\
Display system information

[user \$ ][ inxi -zv8 [COPY TO CLIPBOARD]]

\
or long form

[user \$ ][ inxi \--filter \--verbosity=8 [COPY TO CLIPBOARD]]

\
Display system information in a \`chroot\` environment:

[user \$ ][ inxi -zv8c0 [COPY TO CLIPBOARD]]

\
Display a tree of processes

[user \$ ][ pstree [COPY TO CLIPBOARD]]

\

Switch to tty

-   [Ctrl]+[Alt]+[F1]
-   [Ctrl]+[Alt]+[F2]
-   [Ctrl]+[Alt]+[F3]
-   [Ctrl]+[Alt]+[F4]
-   [Ctrl]+[Alt]+[F5]
-   [Ctrl]+[Alt]+[F6]

Switch to the X session

-   [Ctrl]+[Alt]+[F7]

Start a unit

[user \$ ][ systemctl start unit [COPY TO CLIPBOARD]]

\
Stop a unit

[user \$ ][ systemctl stop unit [COPY TO CLIPBOARD]]

\
Check status of a unit

[user \$ ][ systemctl status unit [COPY TO CLIPBOARD]]

\
Enable a unit

[user \$ ][ systemctl enable unit [COPY TO CLIPBOARD]]

\
Disable a unit

[user \$ ][ systemctl disable unit [COPY TO CLIPBOARD]]

\
Restart a unit

[user \$ ][ systemctl restart unit [COPY TO CLIPBOARD]]

\
Shut down the system

[user \$ ][ poweroff [COPY TO CLIPBOARD]]

\
Restart the system

[user \$ ][ reboot [COPY TO CLIPBOARD]]

\

\

# [See Also]

[Original forum post](https://forum.manjaro.org/t/manjaro-cli-cheat-sheet/101305)