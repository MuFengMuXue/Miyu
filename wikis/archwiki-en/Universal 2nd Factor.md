# Universal 2nd Factor

Universal 2nd Factor (U2F) is an open standard that strengthens and simplifies two-factor authentication (2FA) using specialized USB or NFC devices based on similar security technology found in smart cards.

While initially developed by Google and Yubico, with contribution from NXP Semiconductors, the standard is now hosted by the FIDO Alliance.

For all articles on U2F and U2F-devices see: Universal 2nd Factor.

WebAuthn is a more recent standard.

## Authentication for websites
U2F is supported by major sites like Google, Facebook, Twitter, or GitHub. Check out 2fa.directory or dongleauth.com to find other websites and links to setup documentation. For all browsers which support it, likely the only action required is to install . Yubico offers a demo page for testing.

## Firefox
Firefox/Tweaks#Fido U2F authentication

## Chromium/Chrome
Chromium/Tips and tricks#U2F authentication

## Authentication for user sessions
Yubico, the company creating the YubiKey, develops an U2F PAM module. It can be used to act as a second factor during login or replace the need for a password entirely.

## Installing the PAM module
The module is part of the package .

## Adding a key
Keys need to be added with the tool :

 $ mkdir ~/.config/Yubico
 $ pamu2fcfg -i pam://hostname > ~/.config/Yubico/u2f_keys

After entering your PIN, click the button of your U2F key to confirm the key.

If you own more than one key, append the next ones with

 $ pamu2fcfg -i pam://hostname -n >> ~/.config/Yubico/u2f_keys

## Passwordless sudo
Add

as the first line. Be sure to replace the  as mentioned above. Then create a new terminal and type . Your key's LED should flash and after clicking it the command is executed. The option  is set to provide indication of what to do, i.e. .

In order to make the token the only method of sudo (ie. no password fallback) you will need to comment out the other auth methods present. This is usually just the default system-auth include.

You should also change  to  in the above  line.

## GDM login
Add:

after the existing  lines. Please note the use of the  option which allows the rule to fail if the user did not configure a key. This way setups with multiple users where only some of them use a U2F key are supported.

Some multi-function security keys (ex. Trezor Model T) which can do U2F / PAM may not advertise the feature on system boot which is intentionally out of the CTAP 2.0 specificationWith multiple U2F keys present, this can result in two-minute long delays when used with GDM as pam-u2f does sequential lookups and will wait for the (Trezor) device to timeout before offering presence / touch with the secondary U2F key [https://github.com/Yubico/pam-u2f/issues/310. You could try adding the  option alongside  and finish any device specific login (ex. screen PIN) before GDM loads.

## SDDM/KDE
SDDM does not appear to support pam_u2f with initial user login. Autologin can be used instead, and then edit  to just control screen locking.

If you are using a U2F key with biometric authentication (e.g. Yubikey Bio) and want 1FA, use , commenting out the pam_fprintd.so line and placing your changes in its place. This avoids an unnecessary "unlock" button that gets displayed after authentication, rather than simply unlocking immediatelyhttps://www.reddit.com/r/kdeneon/comments/1bgh78z/using_face_login_without_unlock_button_appearing/.

For example:

## Other authentication methods
Enable the PAM module for other services like explained above. For example, to secure the screensaver of Cinnamon, edit .

For Polkit, copy the default configuration at  to  and make your changes there.

## Troubleshooting
If you managed to lock yourself out of the system, boot into recovery mode or from a USB pen drive. Then revert the changes in the PAM configuration and reboot.

In case the pam-u2f module silently fails, add debug keyword to the auth line in a file in .

## OpenSSH
OpenSSH ≥8.2 supports FIDO/U2F hardware tokens natively, see SSH keys#FIDO/U2F.

## Data-at-rest encryption with LUKS
Since version 248, systemd can be use to unlock a LUKS partition using a FIDO2 key.

First, you will need to setup your  file (see below), or customize your initramfs if you wish to unlock your root partition. The full procedure is similar to the use of a TPM chip for unlocking. See systemd-cryptenroll#Trusted Platform Module.

To register the key, you will need to use the systemd-cryptenroll utility. First, run the following command to list your detected keys:

 $ systemd-cryptenroll --fido2-device=list

Then you can register the key in a LUKS slot, specifying  value (or path to the FIDO2 device such as  if you have multiple):

 $ systemd-cryptenroll --fido2-device=auto /dev/sdX

## Non-root partitions
For a non-root data partition the crypttab would look like this:

This should also work if your encrypted partition is a logical volume managed under LVM:
