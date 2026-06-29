[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

This article provides instructions on encrypting files in a home partition using the ext4 filesystem\'s built-in file based encryption.

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Basics]](#Basics)
-   [[3] [Decryption before login]](#Decryption_before_login)
    -   [[3.1] [systemd service]](#systemd_service)
    -   [[3.2] [systemd script]](#systemd_script)
    -   [[3.3] [PAM script]](#PAM_script)
    -   [[3.4] [Issues]](#Issues)

## [Overview]

[ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") file-system supports FBE (File Based Encryption).

Encrypting directories on an individual basis may be more suitable than full disk encryption (such as [DM-Crypt](https://wiki.gentoo.org/wiki/DM-Crypt "DM-Crypt")). Performance and the ability to exclude certain directories from encryption on the same filesystem.

Good example is scenario with multiple open-source project repositories with read-only access and or other \'public\' files are not required to be encrypted shared on filesystem with personal data.

Scenario described in this article will work correctly only with single user device.

## [Basics]

## [Decryption before login]

Let\'s assume, we want to encrypt our home directory. This approach brings need to enter password before GDM or other login manager is involved.

Since ext4 uses the kernel keyring, which is divided into **session** keyring (every time a user logs into console, X11, or Wayland) and **user** keyring (persistent for user, but only as user keep logged in).

Steps:

1.  (run from systemd service) wait for display manager loads itself - HACK
2.  (run from systemd service) then switch to VT 6 (since if we switch earlier than GDM loads itself, we lost focus with GDM fired up)
3.  (run from systemd shell script) ask password and save it to \@s (session)
4.  (run from systemd shell script)set permissions to allow link it to \@u (user keyring)
5.  (run from PAM) link from \@u (user keyring) to \@s (session keyring)

\

### [systemd service]

The systemd unit will need to run before login screens (haven\'t manage achieve with systemd FIXME). So, let\'s use tty6 for password prompt.

Since on regular desktop we don\'t usually use 6 VT\'s, let\'s modify [logind.conf] and reduce number of reserved VTs.

[FILE] **`/etc/systemd/logind.conf`**

    ...
    [Login]
    NAutoVTs=3
    ReserveVT=1
    ...

Create systemd service file:

[FILE] **`/etc/systemd/system/decrypt.service`**

    [Unit]
    Description=Decrypt
    Wants=multi-user.target

    [Service]
    Type=oneshot
    User=REPLACE_BY_YOUR_USERNAME
    ExecStartPre=/usr/bin/sleep 6
    ExecStartPre=/usr/bin/chvt 6
    ExecStart=/bin/bash /usr/local/sbin/decrypt.sh
    KeyringMode=inherit
    StandardInput=tty-force
    TTYPath=/dev/tty6
    TTYReset=yes
    TTYVHangup=yes
    TTYVTDisallocate=yes
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target

\

`root `[`#`]`systemctl enable decrypt`

### [systemd script]

Into script you have to fill number, which you\'ll get after you run [/usr/sbin/e4crypt add_key] under normal circumstances and then run [keyctl list \@s].

[FILE] **`/usr/local/sbin/decrypt.sh`**

    systemd-ask-password --timeout=0 | /usr/sbin/e4crypt add_key -k @us
    keyctl setperm `keyctl search @us logon ext4:OUTPUT_KEY_FROM_E4CRYPT_ADD_KEY` 0x3f3f3f3f

### [PAM script]

[FILE] **`/usr/local/bin/decrypt_link.sh`**

    #!/bin/sh
    sudo -u $PAM_USER /bin/keyctl link @us @s
    exit 0

Last thing, you need link from \@u (user keyring) to \@s (session keyring), because otherwise ext4 is not able to detect key (no idea why). For this case is best use [PAM](https://wiki.gentoo.org/wiki/PAM "PAM").

Search for files which include line with `pam_keyinit.so` (grep it) and put line right after

[CODE]

    session optional pam_exec.so /usr/local/bin/decrypt_link.sh

### [Issues]

-   When [e4crypt] is issued with `-k @u` (user keyring), the kernel is not able to decrypt content.