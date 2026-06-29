[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Linux+Security&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Linux_Security "Linux Security (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Linux_Security/tr "Linux Güvenliği (2% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Linux_Security/ru "Безопасность Linux (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Users]](#Users)
-   [[3] [sudo]](#sudo)
    -   [[3.1] [sudo vs su]](#sudo_vs_su)
    -   [[3.2] [Why am I Asked for a Password]](#Why_am_I_Asked_for_a_Password)
-   [[4] [Changing Passwords]](#Changing_Passwords)
-   [[5] [Groups]](#Groups)
    -   [[5.1] [Primary Groups]](#Primary_Groups)
-   [[6] [File Permissions]](#File_Permissions)
    -   [[6.1] [Changing File Permissions]](#Changing_File_Permissions)
-   [[7] [Firewalls]](#Firewalls)
-   [[8] [File Integrity Monitoring]](#File_Integrity_Monitoring)
-   [[9] [Sandboxing]](#Sandboxing)

# [Overview]

System security is a complicated topic that individuals study for many years. It would be impractical to impart even a fraction of that knowledge in a Wiki article. What this page will attempt to do is provide a primer in the most basic elements of Linux security and identify common pitfalls for beginners

\

# [Users]

User accounts are used to log into the system and provide one of the basic building blocks for permissions. You could loosely categorize users into a few categories:

-   Regular user accounts like the one created for you during install.
-   Accounts used to run specific processes. These users are often named after the service they run. For example the `dbus` users is user to run the master dbus process.
-   The `root` account.

\
The root account is an administrator or superuser account. This account to everything in the system and be used with extreme care. In most cases, it shouldn\'t be used at all. Instead use `sudo`.

\

# [sudo]

The command `sudo` lets you run a command as the root user without actually switching to the root user. In many cases this is safer than using the root user directly as only a single command is being run as root. For example, your normal user account would not be able the file `/etc/fstab` because it is owned by root. However, you can edit it with sudo like this:

    sudo nano /etc/fstab

\
When you run this command, you will be asked for a password, this will be the password of your normal user account.\
For more information about editing configuration files owned as root see [this article on configuration files](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files "Viewing and editing configuration files").

\

## [sudo vs su]

While `sudo` and `su` look similar and both involve root access they are very different. `sudo` runs a single command as another user and requests the password of your normal user account. `su` lets you \*become\* root and requests the password of the root user. In general, it is usually safer to use sudo than to use su.

\

**Warning**

------------------------------------------------------------------------

Never run a graphical program as root or with sudo, it should only be used with command line programs

\

## [Why am I Asked for a Password]

Sometimes you will take an action in the terminal or through a GUI application and will get prompted for your password. This is because the action you are trying to take cannot be completed by you user and requires elevated rights. Whenever you get a password prompt like this it is important to pause and think if the action you are taking \*should\* be asking for elevated rights before entering your password.

\

**Note**

------------------------------------------------------------------------

Usually these password prompts will be looking for the password of your normal user account but occasionally they will need the password of the root account

\

# [Changing Passwords]

To change the password of the user account you are logged in as you can use the command:

    passwd

\
To change the password of a different user on the same system you can use sudo:

    sudo passwd USERNAME

\

# [Groups]

Users on a Linux system are commonly arranged in groups. A user group is a convenient way of assigning more users access to a common task like sound, media, printing and mounting of removable drives etc.

\
A list of the current groups can be seen on the system with the command:

    getent group | awk -F : ''

\
To see which groups a given user belongs to use the command

    groups USERNAME

\

## [Primary Groups]

A user can be a member of any number of groups but they have only one primary group. The primary group is the group used when files are created.

\

# [File Permissions]

At the most basic level, files are designated as **r**ead, **w**rite or e**x**ecute to the **u**ser(owner), the **g**roup and **o**ther. To understand how this works let\'s look at a real world example.

To get the permissions on the file we can use the command `ls -l`.

    ls -l /etc/fstab
    -rw-r--r-- 1 root root 539 Dec 26 23:07 /etc/fstab

\
That first group of letters and dashes indicate the permissions. It is 10 characters long and the dashes indicate a lack of permissions.

-   The first character \"-\", represents the file type, \"-\" indicates that it is a normal files.
-   The next three characters \"rw-\" indicate the permissions for the user or owner of the file. In this case reading and writing are allowed but not executing.
-   The next three characters \"rw-\" indicate the permissions for members of the group who owns the file. In this case reading and writing are allowed but not executing.
-   The next three characters \"r\--\" indicate the permissions for other users. In this case reading is allowed but not writing or executing.

\
From more detailed information on how file permissions are broken down take a look at [this Wikipedia article](https://en.wikipedia.org/wiki/File_system_permissions#Traditional_Unix_permissions)

\

## [Changing File Permissions]

The command `chmod` can be used to change permissions on a file or directory. It is probably easier to demonstrate than explain.

\
Add read rights to the user(owner) of the file

    chmod u+r filename

\
Remove execute rights to members of the group owner of filename

    chmod g-x filename

\
Set the rights for the other group to read only

    chmod o=r filename

\
Of course, in normal use you would combine everything like this:

    chmod u+rw,g=r,o-rwx filename

\
This adds read and write to the owner, set the group as read only and remove read, write and execute from other users

\
The chmod command can do a lot more than that. For more information take a look at [Wikipedia\'s chmod reference](https://en.wikipedia.org/wiki/Chmod)

\

# [Firewalls]

The [Firewalls](//wiki.manjaro.org/index.php?title=Firewalls "Firewalls") article has a full description of the Firewall solutions available on Manjaro.

\

# [File Integrity Monitoring]

Your first line of defense should always be security practices that prevent an intrusion such as firewalls, intrusion prevention systems and keeping your system patched and up-to-date. However, it is also useful to try to ensure that your system has not been compromised. One way to help with this is by using a file integrity monitoring solution. These solutions work by comparing the checksums or the files on your system to their previous versions and alerting about changes.

An open source tool which provides this service is [AIDE](https://aide.github.io/)(Advanced Intrusion Detection Environment. You can install it with the command:

    pamac install aide

\

# [Sandboxing]

A **Sandbox** is a security mechanism for separating running programs, usually in an effort to mitigate system failures or software vulnerabilities from spreading.

\
One method of sandboxing is using Firejail. Please the [Firejail Wiki page](//wiki.manjaro.org/index.php?title=Firejail "Firejail") for more information on installing and configuring Firejail.