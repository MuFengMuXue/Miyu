Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Pacman_troubleshooting/tr "Pacman'de sorun giderme (5% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Pacman_troubleshooting/es "Solución de Problemas en Pacman (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Pacman_troubleshooting/fr "Dépannage de Pacman (96% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Pacman_troubleshooting/ru "Устранение неисправностей Pacman (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Pacman_troubleshooting/zh-cn "Pacman 故障排除 (8% translated)")

## Contents

-   [[1] [Software Installation]](#Software_Installation)
    -   [[1.1] [\"Unrecognized archive format\" Error]](#.22Unrecognized_archive_format.22_Error)
    -   [[1.2] [\"Unable to lock database\" Error]](#.22Unable_to_lock_database.22_Error)
    -   [[1.3] [Errors about Keys]](#Errors_about_Keys)
    -   [[1.4] [Conflicting files - *FILENAME* exists in filesystem]](#Conflicting_files_-_FILENAME_exists_in_filesystem)
    -   [[1.5] [\"Configuration file\...not recognized\" Error]](#.22Configuration_file...not_recognized.22_Error)
    -   [[1.6] [\"GPGME error: No data\" Error]](#.22GPGME_error:_No_data.22_Error)
        -   [[1.6.1] [Option 1: Basic Resolution]](#Option_1:_Basic_Resolution)
        -   [[1.6.2] [Option 2: Comprehensive Resolution]](#Option_2:_Comprehensive_Resolution)
    -   [[1.7] [\"keyserver refresh failed: No dirmngr\" Error]](#.22keyserver_refresh_failed:_No_dirmngr.22_Error)
-   [[2] [See Also]](#See_Also)

# [Software Installation]

Various issues relating to the download and installation of software packages from the Manjaro repositories are dealt with here.

## [][\"Unrecognized archive format\" Error]

It has ocurred more than once, an update is issuing these messages in a seemingly never ending stream. [Pacman could not open file: sync files](https://forum.manjaro.org/t/pacman-could-not-open-file-sync-files/20046)

    error: could not open file /var/lib/pacman/sync/core.db: Unrecognized archive format
    error: could not open file /var/lib/pacman/sync/extra.db: Unrecognized archive format
    error: could not open file /var/lib/pacman/sync/community.db: Unrecognized archive format
    error: could not open file /var/lib/pacman/sync/multilib.db: Unrecognized archive format

The error relates to content of the db files. The error happens when pacman receives markup from the mirror instead of the database archives.

While it sometimes is possible to fix the issue simply by deleting the files and the running a pacman update it far from every time.

**Run pacman-mirrors to refresh your mirrorlist**

[user \$ ][ sudo pacman-mirrors -c Global [COPY TO CLIPBOARD]]

\

**Download the databases and update the system**

[user \$ ][ sudo pacman -Syu [COPY TO CLIPBOARD]]

\

## [][\"Unable to lock database\" Error]

When downloading and installing software from the repositories, a special database lock file will be created in order to ensure that the current installation process is the only one running at that time. Otherwise, attempting to install multiple files from multiple sources simultaneously may corrupt the downloaded files, cause file conflicts - or worse still - damage your system. Once the installation has been completed, the lock file will then be automatically deleted. This error may therefore occur due to two possible reasons:

-   Another installation is still taking place and has not yet finished, or
-   A previous installation attempt had not finished properly (e.g. due to being aborted early)

It is therefore wise to first check to ensure that another installation is not (or had not been) in process at the time of the error. When satisfied that this is not the case, then the database lock file can be manually deleted. To do so, open up the terminal and enter the following command:

[user \$ ][ sudo rm /var/lib/pacman/db.lck [COPY TO CLIPBOARD]]

\

Once done, you should now be able to successfully re-attempt your intended installation.

## [Errors about Keys]

We all have our own unique signatures which are used to authenticate who we are and to prevent fraudulent or even malicious activities by others. This is also the case with software packages available from the software repositories. They all contain encrypted codes (signature keys) unique to their developers to ensure that they are authentic and not malicious in nature.

During the installation process, once any software packages have been downloaded, your system will first check their signature keys to ensure that they are authentic prior to actually installing them. If a signature key cannot be verified for any reason, then the installation process will be aborted. This problem will usually occur due to:

-   one or more signature keys contained in your system\'s database being revoked, changed, corrupted, or out of date
-   one or more software packages not having been signed off properly when placed in a repository

Where a package has not been signed off properly before being placed in a repository, it will be the responsibility of the developer(s) to correct this. However, as this problem will be more than likely due to a problem with your system\'s verification of a signiture key, this can be solved in three easy steps. Working net connection is required. Once you have opened your terminal:

\

**Warning**

------------------------------------------------------------------------

The following commands only work, when your system time is set correctly!

\

**Info**

------------------------------------------------------------------------

Retrieving the latest keyring packages can be done by browsing a current mirrors pool folder. E.g. from **[https://mirror.easyname.at/manjaro/pool](https://mirror.easyname.at/manjaro/pool)** - using the **overlay** for Manjaro keyring and **sync** for Arch keyring and downloading them to your system. Do not download **.sig** files.

\

**Info**

------------------------------------------------------------------------

Those running ARM can find the **archlinuxarm-keyring** and **manjaro-arm-keyring** in the **sync-arm** and **overlay-arm** folders respectively.

**Download the new keyring packages** Before you download ensure no keyring packages is in the current folder.

[user \$ ][ rm manjaro-keyring\* archlinux-keyring\* [COPY TO CLIPBOARD]]

\

Use either your browser or curl to download. Using curl assumes you know the correct package name as located with the mirror. Replace **YYYYMMDD-R** as available from the mirror.

[user \$ ][ curl -O https://mirror.easyname.at/manjaro/pool/overlay/manjaro-keyring-YYYYMMDD-R-any.pkg.tar.zst [COPY TO CLIPBOARD]]

\

[user \$ ][ curl -O https://mirror.easyname.at/manjaro/pool/sync/archlinux-keyring-YYYYMMDD-R-any.pkg.tar.zst [COPY TO CLIPBOARD]]

\

**Remove the dysfunctional keyrings** by entering this command:

[user \$ ][ sudo rm -r /etc/pacman.d/gnupg [COPY TO CLIPBOARD]]

\

**Initialize the pacman keyring**:

[user \$ ][ sudo pacman-key \--init [COPY TO CLIPBOARD]]

\

**Install the downloaded packages** Assuming the files is the current folder and using wildcard so you don\'t have to deal with dates and versions - remove the packages after successful installation

[user \$ ][ sudo pacman -U manjaro-keyring\*.pkg.tar.zst archlinux-keyring\*.pkg.tar.zst [COPY TO CLIPBOARD]]

\

**Populate the keyrings** - (optional as the install process will do that)

[user \$ ][ sudo pacman-key \--populate manjaro archlinux [COPY TO CLIPBOARD]]

\

**Clear out the software packages downloaded during the aborted installation** (optional):

**Warning**

------------------------------------------------------------------------

The command clears the pacman cache completely, and one will not be able to downgrade to a previous version of a package if required. Instead packages that are causing signing errors can be removed individually when upgrading.

[user \$ ][ sudo pacman -Sc [COPY TO CLIPBOARD]]

\

After that try running **sudo pacman -Syu** to see if the errors were resolved.

## [Conflicting files - *FILENAME* exists in filesystem]

**If you cant can\'t install or update a package because of an error like this:**

    error: could not prepare transaction
    error: failed to commit transaction (conflicting files)
    libname: /insert/file/name/here exists in filesystem
    Errors occurred, no packages were upgraded.

Then the package manager, pacman, has detected an unexpected file that already exists on the disk.

**Why is this happening?**

By design pacman will **not** overwrite files that already exist. This is a design feature, not a flaw - package managers are designed to keep track of installed files.

This issue normally happens because you\'ve manually added, copied, or created a file. It can also happen when you install software using a downloaded executable, run a make install, or use a third-party package system such as conda. It also occurs when you install an AUR package which installs files that conflict with a repo package.

When using a third-party installer you should always specify an alternative installation location, such as under your home directory, or under /opt or /usr/local/. Never install directly under / or /usr.

**How can I fix this?**

The first step is to identify which, if any, package owns the file. This can be easily done with:

[user \$ ][ pacman -Qo /path/to/file [COPY TO CLIPBOARD]]

\

If this identifies a conflicting package you can decide to remove it with pacman -R. If no package is identified you can delete the file (or move it to a backup location).

**Where can I read more?**

This post was inspired by (and adapted from):

[https://wiki.archlinux.org/title/Pacman#%22Failed_to_commit_transaction\_(conflicting_files)%22_error](https://wiki.archlinux.org/title/Pacman#%22Failed_to_commit_transaction_(conflicting_files)%22_error)

The above post also has links to further reading.

## [][\"Configuration file\...not recognized\" Error]

Manjaro\'s package manager - **[pacman](//wiki.manjaro.org/index.php?title=Pacman "Pacman")** - uses a file called *mirrorlist* to tell it the internet addresses of the Manjaro servers in order to download updates and software applications from them. This error will therefore occur if one or more server addresses contained in the mirrorlist file have not been listed properly, resulting in pacman being unable to connect to them. Another tell-tale sign is that this problem will also be encountered immediately after:

-   Installing Manjaro and editing the mirrorlist file during installation, or
-   Editing the mirrorlist file at a later time.

See the [Change to a Different Download Server](//wiki.manjaro.org/index.php?title=Change_to_a_Different_Download_Server "Change to a Different Download Server") guide for more detailed information on how to correctly select and enable another Manjaro server for downloading.

\

## [][\"GPGME error: No data\" Error]

**Warning**

------------------------------------------------------------------------

This section duplicates information from [Pacman_troubleshooting#Errors_about_Keys](//wiki.manjaro.org/index.php?title=Pacman_troubleshooting#Errors_about_Keys "Pacman troubleshooting") consider removing duplicated information

The most likely cause of this issue is that an error or corruption has been detected by *pacman* in one or more software packages being downloaded. Package signatures and checksums are used to verify the validity of downloaded software, and should they fail, the installation attempt will be aborted to protect your system until the matter is resolved.

\

### [Option 1: Basic Resolution]

To resolve this issue, first follow the basic procedure provided below. If this does not work, then there is a more comprehensive procedure available.

\
1. Download the package databases and update your system:

[user \$ ][ sudo pacman -Syu [COPY TO CLIPBOARD]]

\

2\. Clear out the software packages downloaded during the aborted installation by entering the command:

[user \$ ][ sudo pacman -Sc [COPY TO CLIPBOARD]]

\

3\. Re-attempt the aborted download.

### [Option 2: Comprehensive Resolution]

If the basic proceedure still does not resolve the matter, further steps are available:

1\. Resynchronise with the Manjaro servers to ensure that everything is up to date by entering the command:

[user \$ ][ sudo pacman -Sy [COPY TO CLIPBOARD]]

\

2\. Refresh and update the signature keys by entering the command:

[user \$ ][ sudo pacman-key \--refresh-keys [COPY TO CLIPBOARD]]

\

3\. Reload the signature keys by entering the command:

[user \$ ][ sudo pacman-key \--populate archlinux manjaro [COPY TO CLIPBOARD]]

\

4\. Clear out the software packages downloaded during the aborted installation by entering the command:

[user \$ ][ sudo pacman -Sc [COPY TO CLIPBOARD]]

\

5\. Re-attempt the aborted download.

If the error still persists, then it is recommended to **[Change to a Different Download Server](//wiki.manjaro.org/index.php?title=Change_to_a_Different_Download_Server "Change to a Different Download Server")**.

## [][\"keyserver refresh failed: No dirmngr\" Error]

Try running the following command:

[user \$ ][ sudo dirmngr \</dev/null [COPY TO CLIPBOARD]]

\

# [See Also]

-   **[Change to a Different Download Server](//wiki.manjaro.org/index.php?title=Change_to_a_Different_Download_Server "Change to a Different Download Server")**
-   **[Reference Guide for pacman-mirrors](//wiki.manjaro.org/index.php?title=Pacman-mirrors "Pacman-mirrors")**
-   **[Arch wiki for more comprehensive troubleshooting](https://wiki.archlinux.org/index.php/Pacman#Troubleshooting)**