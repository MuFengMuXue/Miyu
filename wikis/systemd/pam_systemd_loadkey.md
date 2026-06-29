## Name

pam_systemd_loadkey — Read password from kernel keyring and set it as PAM authtok

## Synopsis

`pam_systemd_loadkey.so`

## Description

**pam_systemd_loadkey** reads a NUL-separated password list from the kernel keyring, and sets the last password in the list as the PAM authtok, which can be used by e.g. pam_get_authtok(3).

The password list is supposed to be stored in the "user" keyring of the root user, by an earlier call to systemd-ask-password(1) with `--keyname=`. You can pass the keyname to **pam_systemd_loadkey** via the `keyname=` option.

## Options

The following options are understood:

`keyname=`  
Takes a string argument which sets the keyname to read. The default is "`cryptsetup`". During boot, systemd-cryptsetup@.service(8) stores a passphrase or PIN in the keyring. The LUKS2 volume key can also be used, via the `link-volume-key` option in crypttab(5).

**Table 1.  Possible values for `keyname`.**

| Value      | Description                |
|------------|----------------------------|
| cryptsetup | Passphrase or recovery key |
| fido2-pin  | Security token PIN         |
| luks2-pin  | LUKS2 token PIN            |
| tpm2-pin   | TPM2 PIN                   |

  

Added in version 255.

`debug`  
The module will log debugging information as it operates.

Added in version 255.

## Example

This module is intended to be used when you use LUKS with a passphrase, enable autologin in the display manager, and want to unlock Gnome Keyring / KDE KWallet automatically. So in total, you only enter one password during boot.

You need to set the password of your Gnome Keyring/KWallet to the same as your LUKS passphrase. Then add the following lines to your display manager's PAM config under `/etc/pam.d/` (e.g. `sddm-autologin`):

``` programlisting
-auth       optional    pam_systemd_loadkey.so
-auth       optional    pam_gnome_keyring.so
-session    optional    pam_gnome_keyring.so auto_start
-session    optional    pam_kwallet5.so auto_start
```

And add the following lines to your display manager's systemd service file, so it can access root's keyring:

``` programlisting
[Service]
KeyringMode=inherit
```

In this setup, early during the boot process, systemd-cryptsetup@.service(8) will ask for the passphrase and store it in the kernel keyring with the keyname "`cryptsetup`". Then when the display manager does the autologin, **pam_systemd_loadkey** will read the passphrase from the kernel keyring, set it as the PAM authtok, and then **pam_gnome_keyring** and **pam_kwallet5** will unlock with the same passphrase.
