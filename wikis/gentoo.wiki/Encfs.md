[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Encfs&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://vgough.github.io/encfs/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/EncFS "wikipedia:EncFS")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/6347)

**EncFS** (**Enc**rypted **F**ile **S**ystem) is a userspace encryption method that creates an directory containing encrypted files with hashed filenames.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Deployment]](#Deployment)
    -   [[2.2] [Locking]](#Locking)
    -   [[2.3] [Unlocking]](#Unlocking)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Examples]](#Examples)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Kernel]

[KERNEL] **Enable FUSE**

    File systems  --->
        [*] FUSE (Filesystem in Userspace) support

** Note**\
When enabling a built-in (non-modular) feature or driver in the kernel remember a recompile will be needed and the new kernel loaded into memory (system reboot) before changes will take effect. This step should be completed *before* moving on to other sections in this article.

### [USE flags]

Cannot load package information. Is the atom *sys-fs/encfs* correct?

### [Emerge]

Install [[[sys-fs/encfs]](https://packages.gentoo.org/packages/sys-fs/encfs)[]]:

`root `[`#`]`emerge --ask sys-fs/encfs`

## [Configuration]

### [Deployment]

EncFS makes a hidden directory to store encrypted data then uses FUSE to mount a decrypted directory.

** Note**\
Make sure the [\~/] is empty or non-empty mount point error messages will be present.

`user `[`$`]`encfs ~/.encfs ~/encfs`

After running the command setup will ask if a [.encfs] directory should be made, press the [Y] key then press [Enter]. Another question will come up regarding setting up the encryption scheme, etc. Press [Enter] to accept defaults. Enter the password to the prompt twice to finish the set up process.

Once finished encrypted files can be fed to [\~/encfs]

### [Locking]

The [fusermount] command can be used to unmount FUSE file systems. To unmount the FUSE decrypted directory run:

`user `[`$`]`fusermount -u ~/encfs`

Remember that the files located in [\~/encfs] will not be available while it is unmounted.

### [Unlocking]

To mount the decrypted FUSE directory use the [encfs] command:

`user `[`$`]`encfs ~/.encfs ~/encfs`

Running this command will make encrypted files located in [\~/.encfs] available in the [\~/encfs] directory.

## [Usage]

### [Examples]

Running a simple [ls] on the [\~/encfs] directory while the decrypted FUSE file system is mounted will display all the files that were fed into the EncFS storage area:

`user `[`$`]`ls ~/encfs`

    foo bar

Running [ls] on the [\~/.encfs] directory will output hash encrypted filenames:

`user `[`$`]`ls ~/.encfs`

    OtyK9QEW3,1a1qnC5Um5tc-S  s9CN,iacV1bM5SxN1TOI8JB2

## [External resources]

[https://wiki.archlinux.org/index.php/EncFS](https://wiki.archlinux.org/index.php/EncFS) - EncFS on the Arch wiki.