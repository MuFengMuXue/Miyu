**homed** support became available in Gentoo around 2021-02-01^[\[1\]](#cite_note-1)^.

The following article provides instructions to migrate home directories from their traditional structure into the encrypted by default, portable concept provided by systemd\'s homed. This article follows [the upstream guide](https://systemd.io/CONVERTING_TO_HOMED/) when possible. For continuity, it would be wise to read the upstream instructions before reading the instructions here.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [Systemd]](#Systemd)
    -   [[2.2] [NSS]](#NSS)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Inspecting users]](#Inspecting_users)
    -   [[3.3] [Creating new users]](#Creating_new_users)
-   [[4] [Converting traditional home directories to systemd homed]](#Converting_traditional_home_directories_to_systemd_homed)
    -   [[4.1] [Backup important data in /home]](#Backup_important_data_in_.2Fhome)
    -   [[4.2] [Collect UIDs of users to be migrated]](#Collect_UIDs_of_users_to_be_migrated)
    -   [[4.3] [Backup core files]](#Backup_core_files)
    -   [[4.4] [Backup /home directories]](#Backup_.2Fhome_directories)
    -   [[4.5] [Create homed directories]](#Create_homed_directories)
    -   [[4.6] [Move, then remove the files]](#Move.2C_then_remove_the_files)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Manual homed mount and repair]](#Manual_homed_mount_and_repair)
    -   [[5.2] [Moving a homed home directory to a new system]](#Moving_a_homed_home_directory_to_a_new_system)
    -   [[5.3] [Home directory fails to mount: not enough free space]](#Home_directory_fails_to_mount:_not_enough_free_space)
    -   [[5.4] [Image on partition or LVM volume remains absent]](#Image_on_partition_or_LVM_volume_remains_absent)
        -   [[5.4.1] [Example]](#Example)
        -   [[5.4.2] [Work-around]](#Work-around)
    -   [[5.5] [Home activation fails with error: *Value too large for defined data type*]](#Home_activation_fails_with_error:_Value_too_large_for_defined_data_type)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Installation]

### [Kernel]

[KERNEL] **Required kernel options**

     Device drivers --->
       [*] Block devices Search for <code>CONFIG_BLK_DEV</code> to find this item. --->
         [*] Loopback device support Search for <code>CONFIG_BLK_DEV_LOOP</code> to find this item.
       [*] Multiple devices driver support (RAID and LVM) Search for <code>CONFIG_MD</code> to find this item. --->
         [*] Device mapper support Search for <code>CONFIG_BLK_DEV_DM</code> to find this item.
         [*] Crypt target support Search for <code>CONFIG_DM_CRYPT</code> to find this item.
     [*] Cryptographic API Search for <code>CONFIG_CRYPTO</code> to find this item. --->
       Block ciphers --->
         [*] AES (Advanced Encryption Standard) Search for <code>CONFIG_CRYPTO_AES</code> to find this item.
       Length-preserving ciphers and modes --->
         [*] XTS (XOR Encrypt XOR with ciphertext stealing) Search for <code>CONFIG_CRYPTO_XTS</code> to find this item.
       Hashes, digests, and MACs --->
         [*] SHA-224 and SHA-256 Search for <code>CONFIG_CRYPTO_SHA256</code> to find this item.

[KERNEL] **Recommended for performance**

     [*] Cryptographic API Search for <code>CONFIG_CRYPTO</code> to find this item. --->
       Accelerated Cryptographic Algorithms for CPU (x86) --->
         [*] Ciphers: AES, modes: ECB, CBC, CTS, CTR, XCTR, XTS, GCM (AES-NI/VAES) Search for <code>CONFIG_CRYPTO_AES_NI_INTEL</code> to find this item.
         [*] Hash functions: SHA-224 and SHA-256 (SSSE3/AVX/AVX2/SHA-NI) Search for <code>CONFIG_CRYPTO_SHA256_SSSE3</code> to find this item.

### [USE flags]

Installation presumes [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] has already been installed and is presently running as the system and service manager.

Rebuild [[[sys-auth/pambase]](https://packages.gentoo.org/packages/sys-auth/pambase)[]] and [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] with `homed` support. systemd will also require the `cryptsetup` USE flag as well, since LUKS is needed. Alternatively, add `USE="cryptsetup homed"` in [/etc/portage/make.conf], which may help prevent additional USE flag maintenance in the future.

[FILE] **`/etc/portage/package.use/systemd-homed`Add homed support to pambase and systemd**

    sys-auth/pambase homed
    sys-apps/systemd cryptsetup homed

### [Emerge]

Update the [\@world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)") to account for the USE changes:

`root `[`#`]`emerge --ask --update --changed-use --deep @world`

Reload the systemd process for good measure:

`root `[`#`]`systemctl daemon-reexec`

## [Configuration]

### [Service]

#### [Systemd]

Enable the systemd-homed service:

`root `[`#`]`systemctl enable --now systemd-homed`

### [NSS]

Tell the Name Service Switch to use systemd for authenticating users.

[FILE] **`/etc/nsswitch.conf`**

    passwd:      files systemd
    shadow:      files systemd
    group:       files systemd

## [Usage]

### [Invocation]

`user `[`$`]`homectl --help`

    homectl [OPTIONS...] COMMAND ...

    Create, manipulate or inspect home directories.

    Commands:
      list                         List home areas
      activate USER…               Activate a home area
      deactivate USER…             Deactivate a home area
      inspect USER…                Inspect a home area
      authenticate USER…           Authenticate a home area
      create USER                  Create a home area
      remove USER…                 Remove a home area
      update USER                  Update a home area
      passwd USER                  Change password of a home area
      resize USER SIZE             Resize a home area
      lock USER…                   Temporarily lock an active home area
      unlock USER…                 Unlock a temporarily locked home area
      lock-all                     Lock all suitable home areas
      deactivate-all               Deactivate all active home areas
      rebalance                    Rebalance free space between home areas
      with USER [COMMAND…]         Run shell or command with access to a home area

    Options:
      -h --help                    Show this help
         --version                 Show package version
         --no-pager                Do not pipe output into a pager
         --no-legend               Do not show the headers and footers
         --no-ask-password         Do not ask for system passwords
      -H --host=[USER@]HOST        Operate on remote host
      -M --machine=CONTAINER       Operate on local container
         --identity=PATH           Read JSON identity from file
         --json=FORMAT             Output inspection data in JSON (takes one of
                                   pretty, short, off)
      -j                           Equivalent to --json=pretty (on TTY) or
                                   --json=short (otherwise)
         --export-format=          Strip JSON inspection data (full, stripped,
                                   minimal)
      -E                           When specified once equals -j --export-format=
                                   stripped, when specified twice equals
                                   -j --export-format=minimal

    General User Record Properties:
      -c --real-name=REALNAME      Real name for user
         --realm=REALM             Realm to create user in
         --email-address=EMAIL     Email address for user
         --location=LOCATION       Set location of user on earth
         --icon-name=NAME          Icon name for user
      -d --home-dir=PATH           Home directory
      -u --uid=UID                 Numeric UID for user
      -G --member-of=GROUP         Add user to group
         --skel=PATH               Skeleton directory to use
         --shell=PATH              Shell for account
         --setenv=VARIABLE[=VALUE] Set an environment variable at log-in
         --timezone=TIMEZONE       Set a time-zone
         --language=LOCALE         Set preferred language
         --ssh-authorized-keys=KEYS
                                   Specify SSH public keys
         --pkcs11-token-uri=URI    URI to PKCS#11 security token containing
                                   private key and matching X.509 certificate
         --fido2-device=PATH       Path to FIDO2 hidraw device with hmac-secret
                                   extension
         --fido2-with-client-pin=BOOL
                                   Whether to require entering a PIN to unlock the
                                   account
         --fido2-with-user-presence=BOOL
                                   Whether to require user presence to unlock the
                                   account
         --fido2-with-user-verification=BOOL
                                   Whether to require user verification to unlock
                                   the account
         --recovery-key=BOOL       Add a recovery key

    Account Management User  Record Properties:
         --locked=BOOL             Set locked account state
         --not-before=TIMESTAMP    Do not allow logins before
         --not-after=TIMESTAMP     Do not allow logins after
         --rate-limit-interval=SECS
                                   Login rate-limit interval in seconds
         --rate-limit-burst=NUMBER
                                   Login rate-limit attempts per interval

    Password Policy User Record Properties:
         --password-hint=HINT      Set Password hint
         --enforce-password-policy=BOOL
                                   Control whether to enforce system's password
                                   policy for this user
      -P                           Same as --enforce-password-password=no
         --password-change-now=BOOL
                                   Require the password to be changed on next login
         --password-change-min=TIME
                                   Require minimum time between password changes
         --password-change-max=TIME
                                   Require maximum time between password changes
         --password-change-warn=TIME
                                   How much time to warn before password expiry
         --password-change-inactive=TIME
                                   How much time to block password after expiry

    Resource Management User Record Properties:
         --disk-size=BYTES         Size to assign the user on disk
         --access-mode=MODE        User home directory access mode
         --umask=MODE              Umask for user when logging in
         --nice=NICE               Nice level for user
         --rlimit=LIMIT=VALUE[:VALUE]
                                   Set resource limits
         --tasks-max=MAX           Set maximum number of per-user tasks
         --memory-high=BYTES       Set high memory threshold in bytes
         --memory-max=BYTES        Set maximum memory limit
         --cpu-weight=WEIGHT       Set CPU weight
         --io-weight=WEIGHT        Set IO weight

    Storage User Record Properties:
         --storage=STORAGE         Storage type to use (luks, fscrypt, directory,
                                   subvolume, cifs)
         --image-path=PATH         Path to image file/directory
         --drop-caches=BOOL        Whether to automatically drop caches on logout

    LUKS Storage User Record Properties:
         --fs-type=TYPE            File system type to use in case of luks
                                   storage (btrfs, ext4, xfs)
         --luks-discard=BOOL       Whether to use 'discard' feature of file system
                                   when activated (mounted)
         --luks-offline-discard=BOOL
                                   Whether to trim file on logout
         --luks-cipher=CIPHER      Cipher to use for LUKS encryption
         --luks-cipher-mode=MODE   Cipher mode to use for LUKS encryption
         --luks-volume-key-size=BITS
                                   Volume key size to use for LUKS encryption
         --luks-pbkdf-type=TYPE    Password-based Key Derivation Function to use
         --luks-pbkdf-hash-algorithm=ALGORITHM
                                   PBKDF hash algorithm to use
         --luks-pbkdf-time-cost=SECS
                                   Time cost for PBKDF in seconds
         --luks-pbkdf-memory-cost=BYTES
                                   Memory cost for PBKDF in bytes
         --luks-pbkdf-parallel-threads=NUMBER
                                   Number of parallel threads for PKBDF
         --luks-sector-size=BYTES
                                   Sector size for LUKS encryption in bytes
         --luks-extra-mount-options=OPTIONS
                                   LUKS extra mount options
         --auto-resize-mode=MODE   Automatically grow/shrink home on login/logout
         --rebalance-weight=WEIGHT Weight while rebalancing

    Mounting User Record Properties:
         --nosuid=BOOL             Control the 'nosuid' flag of the home mount
         --nodev=BOOL              Control the 'nodev' flag of the home mount
         --noexec=BOOL             Control the 'noexec' flag of the home mount

    CIFS User Record Properties:
         --cifs-domain=DOMAIN      CIFS (Windows) domain
         --cifs-user-name=USER     CIFS (Windows) user name
         --cifs-service=SERVICE    CIFS (Windows) service to mount as home area
         --cifs-extra-mount-options=OPTIONS
                                   CIFS (Windows) extra mount options

    Login Behaviour User Record Properties:
         --stop-delay=SECS         How long to leave user services running after
                                   logout
         --kill-processes=BOOL     Whether to kill user processes when sessions
                                   terminate
         --auto-login=BOOL         Try to log this user in automatically

    See the homectl(1) man page for details.

### [Inspecting users]

`homectl(1)` can be used to see information about user accounts:

`user `[`$`]`homectl inspect larry`

       User name: larry
           State: active
     Disposition: regular
     Last Change: Mon 2024-03-18 02:25:37 GMT
     Last Passw.: Fri 2024-02-23 18:20:33 GMT
        Login OK: yes
     Password OK: yes
             UID: 60183
             GID: 60183 (larry)
     Aux. Groups: adm
                  larry
                  wheel
       Real Name: Larry The Cow
       Directory: /home/larry
         Storage: luks (strong encryption)
      Image Path: /home/larry.home
       Removable: no
           Shell: /bin/bash
     Access Mode: 0701
    LUKS Discard: online=no offline=yes
       LUKS UUID: 1cf006fb-daa8-45b3-b9f9-c539c210ee34
       Part UUID: 6ed84030-d48a-4e54-852d-db3092ef4a2b
         FS UUID: a337bb03-e09b-4864-880a-a9d90f1fb59c
     File System: btrfs
     LUKS Cipher: aes
     Cipher Mode: xts-plain64
      Volume Key: 256bit
     Mount Flags: nosuid nodev exec
       Disk Size: 1.1T
      Disk Usage: 18.2G (= 1.5%)
       Disk Free: 1.1T (= 98.5%)
      Disk Floor: 18.2G
    Disk Ceiling: 1.6T
      Good Auth.: 356
       Last Good: Tue 2024-03-19 21:12:23 GMT
       Bad Auth.: 517
        Last Bad: Tue 2024-03-19 21:11:45 GMT
        Next Try: anytime
     Auth. Limit: 30 attempts per 1min
       Rebalance: off
       Passwords: 1
      Local Sig.: yes
         Service: io.systemd.Home

### [Creating new users]

`homectl(1)` can be used to see create new user accounts. For a simple account `larry` using `/bin/bash` as the shell, and a home directory at `/home/larry`:

`root `[`#`]`homectl new larry`

## [Converting traditional home directories to systemd homed]

### [][Backup important data in /home]

As mentioned in the warning above, all important data in existing [/home] directories should have at *least one*, but *preferably two* local copies of the data in order to be well protected against the case of accidental data loss. This should be the case for each home directory to be migrated. The 3-2-1 backup rule applies here.

As an extra measure, there is a \'backup\' step below, but do not rely on that step for assurance of data safety.

### [Collect UIDs of users to be migrated]

Unless specifically assigned at user creation time, most single user Gentoo systems will have the primary user\'s ID set to a value of 1000. Verify the UID of the primary system user by using the following commands (according to upstream), substituting `larry` for the appropriate username as necessary:

`user `[`$`]`getent passwd larry`

    larry:x:1000:1000::/home/larry:/bin/bash

`user `[`$`]`getent group 1000`

    larry:x:1000:

Mult-user systems go beyond the scope of these instructions. For multi-user systems proceed with each UID as necessary and proceed with caution.

### [Backup core files]

Create backups of important core system files that will be modified:

`root `[`#`]`cp /etc/passwd /etc/passwd.bak `

`root `[`#`]`cp /etc/shadow /etc/shadow.bak `

`root `[`#`]`cp /etc/gshadow /etc/gshadow.bak `

`root `[`#`]`cp /etc/passwd /etc/passwd.bak `

### [][Backup /home directories]

Backup the user(s) home directories. Depending on the speed of the disk and the amount of data, this could take considerable time.

`root `[`#`]`cp --archive --recursive /home/larry /home/larry.saved`

### [Create homed directories]

To (re)create the home directory for each user to be migrated, simply enter the same username and password that each user account had before the migration. If there should be changes made to the *names* of usernames, password, or groups, then it is possible to make the changes now, however it may be unwise. The safest option is to leave the values the way they are and adjust using [homectl update] later.

`root `[`#`]`homectl create larry --uid=1000 --real-name="Larry the Cow" --member-of=wheel,audio,docker,kvm,video,plugdev,portage,users,vboxusers,libvirt`

    🔐 Please enter new password for user foobar:
    🔐 Please enter new password for user foobar (repeat):

### [][Move, then remove the files]

*Move* the old home directory files into the new home directory:

`root `[`#`]`homectl with larry -- rsync -aHAXv --remove-source-files /home/larry.saved/ .`

When the [rsync] command finishes, all files will be moved into the new home directory; only empty directories will be left inside the [/home/larry.saved] location. It can be finally removed with:

`user `[`$`]`rmdir /home/larry.saved`

If the command fails on a certain directory, then not all files have been moved properly. Re-run the above command until the remove command successfully completes the removal of all directories.

## [Troubleshooting]

There are various issues that homed can experience due to being an encrypted filesystem and not a traditional directory full of files.

### [Manual homed mount and repair]

In case a homed filesystem is marked as dirty, which can happen due to disk corruption, the filesystem can be manually mounted and fsck\'d. Using an alternate user account (typically root), use [homectl inspect \<username\>] in order to determine filesystem is dirty. Substitute `larry` in the above command with the appropriate username as necessary:

`root `[`#`]`losetup -fP /home/larry.home `

`root `[`#`]`cryptsetup open /dev/loop0p1 home-larry `

`root `[`#`]`btrfs check /dev/mapper/home-larry `

If the check completes successfully, then the device can be manually mounted:

`root `[`#`]`mount /dev/mapper/home-larry /mnt/rescue`

If everything works as expected, then the [/mnt/rescue] directory will contain the mounted home directory. Files can be moved out of the image, or removed as necessary.

### [Moving a homed home directory to a new system]

Once home directories are converted to the homed format, one of the advantages is their portability. They can be moved between computer systems.

Systemd-homed stores metadata on users and home directories in so called JSON User Records. These user records are signed with a cryptographic key pair to ensure the authenticity of the metadata. The private key is required whenever a user record needs to be updated (e.g. with homectl update) and the public key is required whenever a records needs to be validated, for example as part of the user\'s login process.^[\[2\]](#cite_note-systemd-homed-key-management-2)^ The following steps assume that the user home is moved to a target system without any existing systemd-homed users.

** Warning**\
Overwriting existing key files under [/var/lib/systemd/home] will break current systemd-homed users. If you need to move a systemd-homed user to a target system that already has other systemd-homed users, you need to export the JSON record of the user to be moved without its cryptographic signatures (i.e. `--export-format=minimal`) and use that export to recreate the user on the target system.^[\[3\]](#cite_note-3)^

1.  Copy the home directory file from the homed directory location ([/home] by default) on the old system to the homed directory location on the new system.
2.  Copy the [private.local] and [public.local] files found under the [/var/lib/systemd/home] directory on the old system to the new system.
3.  Restart the systemd-homed service on the *new* system.

    :::: cmd-box


    `root `[`#`]`systemctl restart systemd-homed`


    ::::
4.  Login on the new system.

** Note**\
Although moving home directories are portable with this approach, moving the [/var/lib/portage/world] file and Portage\'s configuration files under the [/etc/portage] directory may be needed to ensure all applications used and references in the moved users\' home directory are available on the new system. Examples include broken shell aliases, commands called in systemd-timers, etc. Depending on the selected profile, custom USE flag selections, and other factors, this may be as simple as copying the world file from the old system to the new system and re-emerging the [\@world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"), or it may be more complex.

### [Home directory fails to mount: not enough free space]

When using a underlying filesystem such as btrfs and experiencing mount issues after filling the home directory with too many files, then files will either need removed from the image or a larger partition/disk will be necessary.

Activate luks discard offline support:

`user `[`$`]`homectl update larry --luks-discard=true --luks-offline-discard=true`

Now attempt to activate the home directory:

`user `[`$`]`homectl activate larry`

If this does not work as expected, then try the [Manual homed mount and repair](#Manual_homed_mount_and_repair) section.

### [Image on partition or LVM volume remains absent]

Creating a home on a block device other than a whole device (like [/dev/sda]) is currently not officially supported.^[\[4\]](#cite_note-4)^ Homed relies on a GPT partition table with a single partition with the appropriate type UUID set for a Linux Home. [homectl create] will appear to work just fine on a partition or LVM volume. However, nested partition tables are not automatically probed and made available.

[Open systemd issue](https://github.com/systemd/systemd/issues/15273) for partition support.

#### [Example]

If a LVM volume and user are created like:

`root `[`#`]`lvcreate -L 20G -n test vg0`

`root `[`#`]`homectl create test --uid=1001 --storage=luks --image-path=/dev/vg0/test --fs-type=ext4`

When activating, there will be an error:

`root `[`#`]`homectl activate test`

    Home of user test is currently absent, please plug in the necessary storage device or backing file system.

The journal log will show:

`root `[`#`]`journalctl -u systemd-homed.service`

    Jan 26 13:30:45 rog systemd-homework[5051]: Watching /dev/disk/by-uuid
    Jan 26 13:30:45 rog systemd-homework[5051]: Device link /dev/disk/by-uuid/a72f39cf-9d6c-455d-b0dc-96f2aefdff45 still hasn't shown up, giving up.
    Jan 26 13:30:45 rog systemd-homework[5051]: Creation completed.
    Jan 26 13:30:45 rog systemd-homework[5051]: Image size is 20.0G, file system size is 19.9G, file system payload size is 19.4G, file system free is 19.4G.
    Jan 26 13:30:45 rog systemd-homed[1353]: test: changing state creating → absent

#### [Work-around]

[kpartx] can be used to probe for nested partitions and make them available:^[\[5\]](#cite_note-5)^

`root `[`#`]`kpartx -av /dev/vg0/test`

    add map vg0-test1 (253:10): 0 2091008 linear 253:9 2048

Now activation should work fine:

`root `[`#`]`homectl activate test`

    🔐 Please enter password for user test: **************

Boot persistence can be achieved by running [kpartx] as pre-start hook for homed:

[FILE] **`/etc/systemd/system/systemd-homed.service.d/override.conf`homed service override**

    [Service]
    ExecStartPre=/usr/bin/kpartx -av /dev/vg0/test

`ExecStartPre` can be specified multiple times, if more user volumes / partitions need to be probed.

### [Home activation fails with error: *Value too large for defined data type*]

It\'s possible this error is caused by incorrect file permissions of the user\'s [\~/.identity] file. This can happen when a systemd-homed user is recreated on a new system with a different UID and the file permissions have not been adjusted accordingly. Ensure that the owner and group of the identity file is the same as the the UID and GID of the systemd-homed user.

## [See also]

-   [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") --- a modern SysV-style init and [[rc](https://wiki.gentoo.org/wiki/Rc "Rc")] replacement for Linux systems.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.reddit.com/r/Gentoo/comments/labx84/systemdhomed_is_now_alive/](https://www.reddit.com/r/Gentoo/comments/labx84/systemdhomed_is_now_alive/)]]
2.  [[[↑](#cite_ref-systemd-homed-key-management_2-0)] [[systemd-homed.service - Key Management](https://www.freedesktop.org/software/systemd/man/latest/systemd-homed.service.html#Key%20Management)]]
3.  [[[↑](#cite_ref-3)] [[homectl - Options](https://www.freedesktop.org/software/systemd/man/latest/homectl.html#--export-format=FORMAT)]]
4.  [[[↑](#cite_ref-4)] [[Storage Mechanism: luks Home Directories](https://systemd.io/HOME_DIRECTORY/#storage-mechanism-luks-home-directories)]]
5.  [[[↑](#cite_ref-5)] [[Issue comment mentioning kpartx](https://github.com/systemd/systemd/issues/15273#issuecomment-621234363)]]