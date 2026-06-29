Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Using_Samba_in_your_File_Manager/tr "Dosya Yöneticinizde Samba'yı Kullanmak (6% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Using_Samba_in_your_File_Manager/ru "Использование Samba в файловом менеджере (100% translated)")

## Contents

-   [[1] [Accessing SMB Shares from the File Manager]](#Accessing_SMB_Shares_from_the_File_Manager)
-   [[2] [Sharing Files from the File Manager]](#Sharing_Files_from_the_File_Manager)
    -   [[2.1] [Installation]](#Installation)
        -   [[2.1.1] [Nemo - Cinnamon]](#Nemo_-_Cinnamon)
        -   [[2.1.2] [Nautilus - Gnome/Budgie]](#Nautilus_-_Gnome.2FBudgie)
        -   [[2.1.3] [Caja - MATE]](#Caja_-_MATE)
        -   [[2.1.4] [Thunar - XFCE]](#Thunar_-_XFCE)
        -   [[2.1.5] [Dolphin - KDE/plasma]](#Dolphin_-_KDE.2Fplasma)
    -   [[2.2] [Finishing Up]](#Finishing_Up)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Protocol version]](#Protocol_version)
    -   [[3.2] [User Accounts]](#User_Accounts)
    -   [[3.3] [User Doesn\'t have Rights to Create Shares]](#User_Doesn.27t_have_Rights_to_Create_Shares)
    -   [[3.4] [Firewall]](#Firewall)
-   [[4] [See Also]](#See_Also)

# [Accessing SMB Shares from the File Manager]

Dolphin is capable of mounting smb file shares without needing any additional packages. All other file managers require installing the package `gvfs-smb`. This is present by default in most Manjaro editions but if you need to install it you can so with:

    pamac install gvfs-smb

\

# [Sharing Files from the File Manager]

The following will guide you through setting up user sharing with Samba so that you can use your file manager to share folders.

\

## [Installation]

Depending on which file manager you use there are different packages to install. Please reference the appropriate section for your file manager.

\
The `manjaro-settings-samba` package will install a basic config and enable the file sharing services. The whole process is nicely automated.

\

### [Nemo - Cinnamon]

    pamac install nemo-share manjaro-settings-samba

\

### [][Nautilus - Gnome/Budgie]

    pamac install nautilus-share manjaro-settings-samba

\

### [Caja - MATE]

    pamac install caja-share manjaro-settings-samba

\

### [Thunar - XFCE]

    pamac install thunar-shares-plugin-gtk3

\

### [][Dolphin - KDE/plasma]

    pamac install samba kdenetwork-filesharing manjaro-settings-samba

\

## [Finishing Up]

Once you have installed the required packages for your file manager you should **reboot** to start the services and let the group changes take effect.

\

# [Troubleshooting]

## [Protocol version]

Since samba 4.11.0 released on 2019-09-17, the very old Windows NT protocol is disabled by default because of serious security issues, so if you connect to:

-   a supported Windows version
-   a supported Linux Samba server
-   a supported NAS appliance

Please upgrade these to the latest version and disable the NT1 protocol on these servers if not done automatically.

If you connect to:

-   an unsupported Windows version
-   an unsupported NAS

Please turn off file sharing towards the Internet and know that malicious users on your LAN (unless isolated in a guest network) will be able to access all local NT1 shares with full control.

## [User Accounts]

If you are getting permission denied when connecting to a new share, one common cause of this is that samba does not have access to Linux user passwords by default. To remedy this, create a samba password for your user account:

    sudo smbpasswd -a theusername

\
This will create a password for the user.

\

## [][User Doesn\'t have Rights to Create Shares]

If you get an error that you don\'t have rights to create shares ensure that you user account has been added to the [group](//wiki.manjaro.org/index.php?title=System_Maintenance#Groups "System Maintenance") sambashare. After modifying groups it is required to logout for the changes to take effect.

\

## [Firewall]

If you are getting \"connection denied\" errors make sure you have allowed access through your firewall. See [the firewall wiki article](//wiki.manjaro.org/index.php?title=Firewalls "Firewalls") for more details.

# [See Also]

-   The [Samba Project](https://www.samba.org/)
-   The [Arch Wiki](https://wiki.archlinux.org/index.php/Samba) Samba Page