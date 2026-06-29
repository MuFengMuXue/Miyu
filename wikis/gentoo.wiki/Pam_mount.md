**Resources**

[[]][Home](http://pam-mount.sourceforge.net/)

The [**pam_mount.so**] PAM module allows systems to automatically mount file systems when a user logs on, and unmount file systems when the user logs off.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Mounting regular file systems]](#Mounting_regular_file_systems)
    -   [[3.2] [Mounting encrypted file systems (dm-crypt/LUKS)]](#Mounting_encrypted_file_systems_.28dm-crypt.2FLUKS.29)
    -   [[3.3] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

The [[[sys-auth/pam_mount]](https://packages.gentoo.org/packages/sys-auth/pam_mount)[]] package has a few USE flags that it supports:

### [USE flags for] [sys-auth/pam_mount](https://packages.gentoo.org/packages/sys-auth/pam_mount) [[]] [A PAM module that can mount volumes for a user session]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`crypt`](https://packages.gentoo.org/useflags/crypt)       Add support for encryption \-- using mcrypt or gpg where applicable
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)           Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-12 05:19] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To install the package, just emerge it:

`root `[`#`]`emerge --ask sys-auth/pam_mount`

## [Configuration]

No specific configuration is needed for the installation itself. The actual configuration entries are mentioned below under the [Usage](#Usage) section.

## [Usage]

### [Mounting regular file systems]

Edit the PAM configuration file in which the mount action has to be configured. Add the required call to [pam_mount.so] for `auth` and `session` as shown in the next example:

[FILE] **`/etc/pam.d/system-login`\"Enable pam_mount in the proper service\"**

    auth        required    pam_shells.so
    auth        required    pam_nologin.so
    auth        include     system-auth
    '''auth     optional    pam_mount.so'''

    account     required    pam_access.so
    account     required    pam_nologin.so
    account     include     system-auth

    password    include     system-auth

    session         optional        pam_loginuid.so
    session     required    pam_env.so
    session     optional    pam_lastlog.so silent
    session     include     system-auth
    session     optional    pam_ck_connector.so nox11
    session     optional    pam_motd.so motd=/etc/motd
    session     optional    pam_mail.so
    '''session      optional    pam_mount.so'''

Next, edit or create the following configuration file:

[FILE] **`/etc/security/pam_mount.conf.xml`\"Configure pam_mount\"**


      <volume user="your username" fstype="ext4" path="/dev/sdxn" mountpoint="/somewhere" option="fsck" />
      <debug enable="1" />
    </pam_mount>

This file will establish the file systems to mount when a particular user logs on. Of course, replace the example values with actual ones.

### [][Mounting encrypted file systems (dm-crypt/LUKS)]

One might want to mount devices encrypted with cryptsetup. At the moment it\'s managed by [pam_mount] automatically, just add `fstype="crypt"` to the configuration file:

[FILE] **`/etc/security/pam_mount.conf.xml`**


      <volume user="username" fstype="crypt" path="/dev/sdXN" mountpoint="/somewhere" option="fsck" />
      <debug enable="1" />
    </pam_mount>

For other kind of encrypted file systems specify the appropriate customization for mount programs.

[FILE] **`/etc/security/pam_mount.conf.xml`**

    <cryptmount>mount.crypt ...</cryptmount>
    <cryptumount>umount.crypt %(MNTPT)</cryptumount>

See [man pam_mount.conf] for details.

### [Unmerge]

Before removing the package, make sure that no PAM configuration file refers to the module anymore:

`user `[`$`]`grep pam_mount /etc/pam.d/*`

If no file refers to it anymore, then the package is safe to unmerge:

`root `[`#`]`emerge --ask --depclean --verbose sys-auth/pam_mount`

## [See also]

-   [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") --- allows (third party) services to provide an authentication module for their service which can then be used on PAM enabled systems.

## [[] External resources]

-   [pam_mount on ArchWiki](https://wiki.archlinux.org/title/Pam_mount)