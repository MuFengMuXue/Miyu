The option to encrypt the disk or a partition is usually performed during system installation.

But instead of encrypting the entire disk, there is the option to encrypt just the user\'s home directory. Maybe it doesn\'t offer the same level of security, but for some users it may be enough.

The encrypted home directory will not require any extra passwords besides the user login password, as is normally done. Even if someone has access to the system as root, and changes the user\'s password, they won\'t be able to access the encrypted files - it is necessary to know the original password.

** See also**\
For full information, see [ECryptfs](https://wiki.gentoo.org/wiki/ECryptfs "ECryptfs").

## [Procedure]

Install the necessary software. As this is masked software, it is necessary to unmask it, see the [unmasking a package](https://wiki.gentoo.org/wiki/Knowledge_Base:Unmasking_a_package "Knowledge Base:Unmasking a package") article on how to do that. The [[[suid]](https://packages.gentoo.org/useflags/suid)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag may need setting on [[[sys-fs/ecryptfs-utils]](https://packages.gentoo.org/packages/sys-fs/ecryptfs-utils)[]]. Then emerge [[[sys-fs/ecryptfs-utils]](https://packages.gentoo.org/packages/sys-fs/ecryptfs-utils)[]]:

`root `[`#`]`emerge --ask ecryptfs-utils`

Restart the computer. At the login screen, **do not** log in.

Open a new tty, for example: Ctrl + Alt + F2.

Log in with the root user.

Activate the module:

`root `[`#`]`modprobe ecryptfs`

Migrate user\'s home directory to an encrypted home directory. It will prompt for the user\'s password:

`root `[`#`]`ecryptfs-migrate-home -u <USERNAME>`

Switch to the daily user. It will prompt for the user\'s password again:

`root `[`#`]`su <USERNAME>`

Go to home folder:

`user `[`$`]`$ cd`

Run the mount wrapper script. Use the user password when prompted:

`user `[`$`]`ecryptfs-mount-private`

Unwrap an eCryptfs mount passphrase. Enter user password, again:

`user `[`$`]`ecryptfs-unwrap-passphrase`

Run the unmount wrapper script:

`user `[`$`]`ecryptfs-umount-private `

`user `[`$`]`exit`

If logging in as root again, in the home directory there will be a copy of user\'s directory followed by \".\" and some characters. It\'s a backup, to restore personal files if something goes wrong. When the whole process is done and it\'s working, that directory may be deleted.

## [Auto-mounting]

To allow the encrypted home directory to be mounted automatically on login, proceed as follows.

Make a backup of the \"/etc/pam.d/system-auth\":

`root `[`#`]`cp /etc/pam.d/system-auth /etc/pam.d/system-auth.ori`

Add two lines to the file.

`root `[`#`]`nano /etc/pam.d/system-auth`

Compare the differences, and see which lines have been added:

`user `[`$`]`diff -u /etc/pam.d/system-auth.ori /etc/pam.d/system-auth`

    --- /etc/pam.d/system-auth.ori  2022-08-21 19:02:30.070080014 -0300
    +++ /etc/pam.d/system-auth      2022-08-21 19:03:52.649811213 -0300
    @@ -2,6 +2,7 @@
     auth           requisite       pam_faillock.so preauth
     auth            [success=1 default=ignore]      pam_unix.so nullok  try_first_pass
     auth           [default=die]   pam_faillock.so authfail
    +auth           optional        pam_ecryptfs.so unwrap
     account                required        pam_unix.so
     account         required        pam_faillock.so
     password       required        pam_passwdqc.so config=/etc/security/passwdqc.conf
    @@ -9,3 +10,4 @@
     session                required        pam_limits.so
     session                required        pam_env.so
     session                required        pam_unix.so
    +session                optional        pam_ecryptfs.so unwrap

Save and exit. Restart and log in normally with username.