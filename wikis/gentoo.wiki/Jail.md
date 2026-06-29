[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Jail&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://www.jmcresearch.com/projects/jail/)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/jail)

[[]][GitHub](https://github.com/spiculator/jail)

This guide will go through how to use the **jail** tool to set up a [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Create directories]](#Create_directories)
    -   [[2.2] [Add a new user account in the main system]](#Add_a_new_user_account_in_the_main_system)
    -   [[2.3] [Add a new user account in the chroot]](#Add_a_new_user_account_in_the_chroot)
    -   [[2.4] [Adding software]](#Adding_software)
    -   [[2.5] [Finishing touches]](#Finishing_touches)
-   [[3] [Activating jail]](#Activating_jail)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/jail`

## [Configuration]

### [Create directories]

Create the root directory for jail:

`root `[`#`]`mkjailenv /var/chroot`

    mkjailenv
    A component of Jail (version 1.9 for linux)
    http://www.gsyc.inf.uc3m.es/~assman/jail/
    Juan M. Casillas <assman@gsyc.inf.uc3m.es>

    Making chrooted environment into /var/jail
            Doing preinstall()
            Doing special_devices()
            Doing gen_template_password()
            Doing postinstall()
    Done.

### [Add a new user account in the main system]

This account should have the chroot as its home directory and the jail binary as the shell:

`root `[`#`]`useradd -g users --home /var/chroot --shell /usr/bin/jail larry`

### [Add a new user account in the chroot]

This account should have the same name as the account in the main system:

`root `[`#`]`addjailuser /var/chroot /home/larry /bin/bash larry`

    addjailuser
    A component of Jail (version 2.0 for linux)
    http://www.gsyc.inf.uc3m.es/~assman/jail/
    Juan M. Casillas <assman@gsyc.inf.uc3m.es>

    Adding user larry in chrooted environment /var/chroot
    Done

The home directory and shell paths in the above command refer to paths within the chroot.

### [Adding software]

Add the set of basic programs to the jail:

`root `[`#`]`addjailsw /var/chroot`

    A component of Jail (version 2.0 for linux)
    http://www.gsyc.inf.uc3m.es/~assman/jail/
    Juan M. Casillas <assman@gsyc.inf.uc3m.es>

    Guessing head args()
    Guessing sh args()
    Guessing vi args(-c q)
    Guessing pwd args()
    Guessing mv args()
    Guessing rmdir args()
    Guessing ls args()
    Guessing ln args()
    Guessing tail args()
    Guessing id args()
    Guessing mkdir args()
    Guessing touch args()
    Guessing grep args()
    Guessing cp args()
    Guessing rm args()
    Guessing more args()
    Guessing cat args()
    Warning: not allowed to overwrite /var/chroot//etc/passwd
    Warning: not allowed to overwrite /var/chroot//etc/group
    Warning: can't create /proc/meminfo from the /proc filesystem

    Done.

Next we need to also add the login shell:

`root `[`#`]`addjailsw /var/chroot -P /bin/bash --version`

It may be necessary to pass an argument (`--version` as in the above example) to help jail figure out the libraries that are necessary for the program to run in the jail.

The command `addjailsw -P` can be used to add any programs to the chroot.

### [Finishing touches]

Copy the shell startup scripts to the jail:

`root `[`#`]`mkdir -p /var/chroot/etc/bash `

`root `[`#`]`cp /etc/bash/bashrc /var/chroot/etc/bash `

`root `[`#`]`cp /etc/profile /var/chroot/etc `

`root `[`#`]`cp /etc/DIR_COLORS /var/chroot/etc `

## [Activating jail]

Everytime you switch to the larry user you will be logged into the jail:

`root `[`#`]`su - larry`

The first time you run this command it will probably fail, see below.

## [Troubleshooting]

If it is not possible to su into target jail system and the following error message appears:

    jail: execve() : No such file or directory

it means that the dynamic linker is missing. Copy it from the host lib64 directory -

`root `[`#`]` cp -L /lib64/ld-linux-x86-64.so.2 /var/chroot/lib64`

The -L switch is very important as ld-linux-x86-64.so.2 is actually a symlink that points to ld-2.25.so, which is the dynamic linker. The -L dereferences the symlink and copies the file that it points to instead of copying the symlink itself. The copied file inherits the name of the symlink.

## [External resources]

-   [http://www.jmcresearch.com/projects/jail/](http://www.jmcresearch.com/projects/jail/)