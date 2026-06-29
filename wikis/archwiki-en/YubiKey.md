# YubiKey

The YubiKey is a small USB security token. Depending on the model, it can:

* Act as a smartcard using the CCID protocol, allowing storage of both PGP and PIV secret keys.
* Handle Universal 2nd Factor (U2F) requests.
* Store and query approximately 30 Initiative for Open Authentication (OATH) credentials.
* Handle challenge-response requests, in either the Yubico OTP mode or the HMAC-SHA1 mode.
* Generate one-time passwords (OTPs) with Yubico's AES-based standard.
* "Type" a static password up to 63 characters.

While offering many features, newer versions of the YubiKey are not released as open source. Alternatives are the Solo, TKey or Nitrokey.

## Installation
## Management tools
*
::
::
*
*
::

## Authentication tools
*
*
*

## Udev rules
 (and, by extension, ) include udev rules to allows non-root users to access some of the functionality, such as OTP. Users of the other clients will need to add the following rules:

{{hc|/etc/udev/rules.d/51-yubikey.rules|2=
ACTION=="addchange", ATTRS{idVendor}=="1050", ATTRS{idProduct}=="0010011001110114011604010403040504070410", ENV{ID_SECURITY_TOKEN}="1"
}}

## Inputs
The YubiKey takes inputs in the form of API calls over USB and button presses.

The button is very sensitive. Depending on the context, touching it does one of these things:

* Trigger a static password or one-time password (OTP) (Short press for slot 1, long press for slot 2). This is the default behavior, and easy to trigger inadvertently.
* Confirm / allow a function or access. The LED will illuminate to prompt the user.
* Insert / eject the smartcard

## Outputs
The YubiKey transforms these inputs into outputs:

* Keystrokes (emulating a USB keyboard), used to type static passwords and OTPs. (Note that static passwords are vulnerable to keyloggers.)
* The built-in LED:
** Blinks once when plugged in, useful for troubleshooting.
** Blinks steadily when a button press is required to permit an API response.
* API responses over USB. This is used for:
** Challenge-Response requests (calculated using either Yubico OTP mode or HMAC-SHA1 mode)
** U2F Challenge-Response requests
** CCID Smartcard related requests

## USB connection modes
Depending on the YubiKey model, the device provides up to three different USB interfaces. Two of the interfaces implement the USB HID (Human Interface Device) device class; the third is a smart card interface (CCID). All three can be enabled or disabled independently, allowing control of their associated protocols.

The following table shows which protocols use which interfaces:

{| class="wikitable"
! Protocol !! Interface
|-
|OTP || Keyboard HID
|-
|FIDO || Other HID
|-
|PIV || CCID
|-
|OpenPGP || CCID
|-
|OATH || CCID
|}

 uses the term "modes", named OTP, FIDO, and CCID.

## Get enabled modes
For YubiKey prior to version 5:

For YubiKey version 5:

## Set modes
All modes are enabled from the factory. To change them:

 $ ykman mode 'MODE

*  can be a string, such as , or a shortened form .
*  can be a mode-number, which encodes several enabled modes.

Here is a table of mode-numbers, if you care to use them:

{| class="wikitable"
|0||OTP device only.
|-
|1||CCID device only.
|-
|2||OTP/CCID composite device.
|-
|3||U2F device only.
|-
|4||OTP/U2F composite device.
|-
|5||U2F/CCID composite device.
|-
|6||OTP/U2F/CCID composite device.
|-
|81||CCID device only, with touch-eject.
|}

Options:

*  - The button will insert and eject the smart card. This only works if the mode is CCID only; FIDO and OTP must be disabled.
*  - Automatically eject the smart card after some time. Same restrictions as .
*  - Set the challenge-response timeout.

For more information, see .

## One-time password
This feature has a somewhat misleading name, because it also encompasses the static password and challenge-response functions.

2 slots are provided for this feature, accessible by short and long button presses respectively. Each can be configured with one of the following:

* Yubico OTP
* OATH-HOTP
* OATH-TOTP
* Challenge-response
* Static Password

Each function has several configuration options provided at the time of creation, but once set they cannot be read back. It is possible to swap slots 1 and 2, with .

## Factory configuration
On a new YubiKey, Yubico OTP is preconfigured on slot 1. This initial AES symmetric key is stored in the YubiKey and on the Yubico Authentication server. This allows validating against YubiCloud, allowing the use of Yubico OTP in combination with the Yubico Forum website for instance or on https://demo.yubico.com).

## Yubico OTP
The [https://developers.yubico.com/OTP/ Yubico OTP is based on symmetric cryptography. More specifically, each YubiKey contains a 128-bit AES key unique to that device, which is also stored on a validation server. When asked for a password, the YubiKey will create a token by concatenating different fields such as the ID of the key, a counter, and a random number, and encrypting the result.

This OTP is sent to the target system, which passes it to a validation server. The validation server (also in posession of the secret key) decrypts it and verifies the information inside. The result is returned to the target system, which can then decide whether to grant access.

## Configuration and usage
Generate a new key in slot 2, and upload it to YubiCloud (opens in a browser):

 $ ykman otp yubiotp --generate-key --upload 2

For more information, see .

## Security risks
## AES key compromise
As you can imagine, the AES key should be kept secret. It cannot be retrieved from the YubiKey itself (or it should not, at least not with software). It is also present in the validation server, so the security of this server is very important.

## Validation requests/responses tampering
Since the target system relies on a validation server, a possible attack would be to impersonate it. To prevent this, the target system needs to authenticate the validation server, either using HMAC or HTTPS.

## Challenge-response
A challenge is sent to the YubiKey, which calculates a response based on some secret. The same challenge always results in the same response. Without the secret this calculation is not feasible, even with many challenge-response pairs.

This can be used for

* True 2-factor authentication: The user is provided a challenge, they must provide the correct response in addition to a password. Both parties must have the secret key.
* "Semi" 2-factor authentication: the challenge acts as a password, and the server stores the correct response. This is not an OTP, and if anyone can obtain the response they will gain access, but it is simpler as the server does not need the secret key.

There are two Challenge-Response algorithms:

* HMAC-SHA1
* Yubico OTP

You can set them up with a GUI using the , or with the following instructions:

## HMAC-SHA1 algorithm
Set up slot 2 in challenge response mode with a generated key:

 $ ykman otp chalresp --generate 2

You can omit the  flag in order to provide a key, see . A main advantage of providing a key is that it can be used to setup a second device as a backup. The command  generates a suitable key, for example.

## Yubico OTP algorithm
 Does not appear to support setting the chal-yubico algorithm, but you can use . Generate a random key in slot 2:

 $ ykpersonalize -2 -ochal-resp -ochal-yubico

For more information, see .

## Sending a challenge
To send a challenge and get a response, the  command can be used. For example,

returns a 40-byte SHA1-hash unique to the programmed slot 2. A different challenge produces another unique response.

## Static password
You can either generate a static password:

 $ ykman otp static --generate slot

or provide one:

 $ ykman otp static slot password

You have several options; you can set the length and character set of the generated password, and whether or not to send an Enter keystroke. See  for more.

## Emulated USB keyboard limitations, or "Why does my password look so weak?"
In order for the YubiKey to work with most keyboard layouts, passwords are by default limited to the ModHex alphabet (), digits , and . These characters use the same scan codes across a very large number of keyboard layouts, ensuring compatibility with most computers.

Yubico has provided a whitepaper on the subject.

## OATH
The YubiKey offers 2 OATH implementations:

; OATH API: Newer method, can store approximately 30 credentials depending on the model. (YubiKey 4, NEO, and newer)
; OTP slot: Older method, both OTP slots can store a single credential. (All models which support challenge-response)

## OATH API
If you prefer a GUI, you can use .

 can add codes in the URI format with . Here is a one-liner that will add a credential from an image of a QR code:

 $ zbarimg qr_code.png --quiet --raw | xargs ykman oath accounts uri

You can also do things manually. Program a TOTP key, requiring a button touch to generate a code:

 $ ykman oath accounts add --touch name secret

Program an HOTP key:

 $ ykman oath accounts add --oath-type HOTP name secret

List credentials:

 $ ykman oath accounts list

Generate codes:

 $ ykman oath accounts code query

To see all available subcommands see . To see information about each, use .

## OTP slot implementation
Program an HOTP in slot 2:

 $ ykman otp hotp 2 key

Program a TOTP:

 $ ykman otp chalresp --totp slot key

Generate an HOTP:

 $ ykman otp calculate slot

Generate a TOTP:

 $ ykman otp calculate --totp slot

See also:  and https://developers.yubico.com/OATH/

## U2F
Universal 2nd Factor (U2F) with a YubiKey is very simple, requiring no configuration for the key itself. Note that this mode is also referred to as 'FIDO' in some documentation and utilities. You have a few limited management options through the  utility:

* Set a PIN:
* delete individual credentials:
* Reset all credentials and PIN:

To use U2F for authentication, see the instructions in U2F.

Also see WebAuthn.

## CCID smartcard
CCID (Chip Card Interface Device) is a USB standard device class for use by USB devices that act as smart card readers or with security tokens that connect directly via USB, like the YubiKey. HID (Human Interface Device) and CCID are both USB device classes, i.e. they are in the same category of USB specifications. HID is a specification for computer peripherals, like keyboards. The YubiKey works like a USB (HID) keyboard when used in the OTP and FIDO modes, but switches to the CCID protocol when using the PIV application, or as an OpenPGP device.

CCID mode should be enabled by default on all YubiKeys shipped since November 2015 Enable at least the CCID mode. Please see #Get enabled modes.

## PIV
Starting with the YubiKey NEO, the YubiKeys contain a PIV (Personal Identity Verification) application on the chip. PIV is a US government standard (FIPS 201) that specifies how a token using RSA or ECC (Elliptic Curve Cryptography) is used for personal electronic identification. The YubiKey NEO only supports RSA encryption, later models (YubiKey 4 and 5) support both RSA and ECC. The exact algorithms supported depends on the firmware. For example, only YubiKeys with firmware 5.7 and up support RSA 3072, RSA 4096, Ed25519, and X25519 keys [https://developers.yubico.com/PIV/Introduction/YubiKey_and_PIV.html. The distinguishing characteristic of a PIV token is that it is built to protect private keys and operate on-chip. A private key never leaves the token after it has been installed on it. Optionally, the private key can even be generated on-chip with the aid of an on-chip random number generator. If generated on-chip, the private key is never handled outside of the chip, and there is no way to recover it from the token. When using the PIV mechanism, the YubiKey functions as a CCID device.

## OpenPGP smartcards
The YubiKey can act as a standard OpenPGP smartcard; see GnuPG#Smartcards for instructions on how to set up and use it with GnuPG. Yubico also provides some documentation in https://developers.yubico.com/PGP/.

If you do not want to use the other features (U2F and OTP), the button can be configured to insert and eject it, and an auto-eject timeout can be set as well. See #USB connection modes for more.

The default user pin is  and the default admin pin is . The default PUK is also . Remember to change all 3.

## Use cases
This section details how to use your YubiKey for various authentication purposes. It is by no means an exhaustive list.

## Full disk encryption with LUKS
You have several options:

* Challenge-Response: the response to some challenge is used as a LUKS key. The challenge can act as a password for true 2-factor authentication, or stored in plain-text for one-factor authentication.
* GnuPG: Uses the yubikey's PGP smartcard functionality. Offers strong 2-factor authentication without needing a huge passphrase.
* FIDO HMAC Secret: If your YubiKey supports U2F, it can be configured to return a symmetric secret.

## Common prerequisites
* A bootable LUKS encrypted system, using the  mkinitcpio hook, with at least one free keyslot.
** With the exception of , the  hook is not supported by any of these tools.
* Backed up LUKS header (Optional, though advisable)

## Challenge-response
See 's official documentation for complete instructions. Broadly:

# Install .
# Configure .
# Enroll the disk:
# Add the  mkinitcpio hook before the  hook.
# Regenerate the initramfs.

:

There are a few variations available:

* 2FA: default behavior. You must provide the challenge as a password when enrolling the device, and upon boot.
* 1FA: Set  in . Note that this is stored in plaintext. Consider disabling non-root read permissions to this file.
* NFC support (Experimental)
* Suspend & Resume support (Experimental) Automatically lock encrypted volumes on suspend, unlock them on resume.

You must regenerate the initramfs for any configuration changes to take effect.

## systemd-based initramfs
Users of the  hook may install  or  and follow the instruction in the project documentation. The procedure is broadly similar to .

## GnuPG encrypted keyfile
One tool to accomplish this is initramfs-scencrypt; see its docs for complete instructions. Note that as of October 2022 this package is not in the AUR and is not thoroughly tested, though the GitHub repository offers a PKGBUILD.

The dm-crypt pages offer a few alternatives, though they are mostly links to old forum posts.

## HMAC secret extension of FIDO2 protocol
Yet another way of using YubiKey for full disk encryption is to utilize HMAC Secret Extension to retrieve the LUKS password from YubiKey. This can be protected by a passphrase. This functionality requires at least YubiKey 5 with firmware 5.2.3+.
For a passphrase protected solution, install  and follow instructions available in project documentation.
For single factor (optionally PIN-protected) solution and starting with systemd 248, it is possible to use your FIDO2 key as LUKS2 keyslot. Instructions available in the author's blog post.

## KeePass
KeePass can be configured for YubiKey support; see the YubiKey section for instructions.

## SSH keys
## CCID
If your YubiKey supports CCID smartcards, you can use it as a hardware-backed SSH key, either based on GPG or PIV keys. Yubico offers good documentation:
* An overview of both possibilities, giving their advantages and disadvantages
* Instructions for PGP authentication
* Instructions for PIV authentication through user certificates
* Instructions for PIV authentication through #PKCS11

:

## U2F
You may also use the U2F feature of the YubiKey to create hardware-backed SSH keys. See SSH keys#FIDO/U2F for instructions.

## PIV
 stores the SSH key as PIV token. See https://github.com/FiloSottile/yubikey-agent#readme for a setup guide.

## Linux user authentication with PAM
PAM, and therefore anything which uses PAM for user authentication, can be configured to use a YubiKey as a factor of its user authentication process. This includes sudo, su, ssh, screen lockers, display managers, and nearly every other instance where a Linux system needs to authenticate a user. Its flexible configuration allows you to set whichever authentication requirements fit your needs, for the entire system, a specific application, or for groups of applications. For example, you could accept the YubiKey as an alternative to a password for local sessions, while requiring both for remote sessions. In addition to the Arch Wiki, You are encouraged to read  and  to understand how it works and how to configure it.

There are several modules available which integrate YubiKey-supported protocols into PAM:

*  - Supports #U2F via the FIDO2 standard. If you are not sure which method to use, this one is a good choice.
** Universal 2nd Factor#Authentication for user sessions
** Yubico's official docs, including a list of supported module parameters.
** Man Pages: ,
*  - Supports #OATH one-time passwords (either HOTP or TOTP)
** pam_oath
*  - Supports #Yubico OTP and challenge-response OTPs. Note that Yubico OTP mode requires a network connection to a validation server, while challenge-response mode does not.
** Yubico's official docs
**  - Take note of the  parameter, used to set challenge-response mode.
::

PAM configuration is beyond the scope of this article, but for a brief overview:

* Create file(s) containing authorized keys, either in users' home directories or centrally.
* Add a line in the appropriate place in the appropriate PAM configuration file which follows this format:
    auth [module_name.so arguments
*  for multifactor,  for single factor.
*  - Example: . See a list of installed modules:
* Module configuration arguments are for things like the location of the keyfile, or which method the module should use for authentication.

## SSH notes
* Yubico has provided additional guidance. It is written for an old version of Ubuntu, but much of it still applies to an updated Arch system.
* If you are configuring a distant server to use YubiKey, you should open at least one additional, rescue SSH session, so that you are not locked out if the configuration fails.
* Check that  contains the following settings. The  shipped with  has these set correctly by default.
    ChallengeResponseAuthentication no
    UsePAM yes

## Browser/web integration
Many web services are beginning to support FIDO hardware tokens. See the U2F and WebAuthn pages for more information, but usually the only thing you need to do is to install  and try it.

## Tips and tricks
## Executing actions on insertion/removal of YubiKey device
For example, you want to perform an action when you pull your YubiKey out of the USB slot, create the following:

{{hc|/etc/udev/rules.d/80-yubikey-actions.rules|2=
ACTION=="remove", ENV{ID_VENDOR}=="Yubico", ENV{ID_VENDOR_ID}=="1050", ENV{ID_MODEL_ID}=="0010|0111|0112|0113|0114|0115|0116|0401|0402|0403|0404|0405|0406|0407|0410", RUN+="/usr/local/bin/script args"

}}

Please note, most keys are covered within this example but it may not work for all versions of YubiKey. You will have to look at the output of lsusb to get the vendor and model ID's, along with the description of the device or you could use udevadm to get information. Of course, to execute a script on insertion, you would change the action to 'add' instead of remove.

## Start Yubico Authenticator on insertion
The authenticator is a long-running GUI process. If run directly in a udev rule, the process would block udev's processing. If forked, udev would unconditionally kill the process after the event handling finishes. Thus you cannot start the authenticator from udev rules. However, systemd.device may be used to handle this case.

Similar to above, create:

{{hc|/etc/udev/rules.d/80-yubikey-actions.rules|2=
ENV{ID_VENDOR}=="Yubico", ENV{ID_VENDOR_ID}=="1050", ENV{ID_MODEL_ID}=="0010|0111|0112|0113|0114|0115|0116|0401|0402|0403|0404|0405|0406|0407|0410", SYMLINK+="yubikey", TAG+="systemd"

}}

Then create a new systemd user unit:

and enable it. systemctl would warn that it is added as a dependency to a non-existent unit . But it is okay. Such unit will start existing once the YubiKey is plugged in.

## Maintenance / upgrades
## Installing the OATH Applet for a YubiKey NEO
These steps will allow you to install the OATH applet onto your YubiKey NEO. This allows the use of Yubico Authenticator in the Google Play Store.

{{Note|1=These steps are only for NEOs with a firmware version  80E88013D7C000C400BE00C700CA00CA00B400BE00CE00D200D500D700B000DB00C700DF00BEFFFF00BE00E400AC00AE00AE00DB00E700A
A00EA00ED00ED00ED00BE00EF00F100F400F100F700FA00FF00BE00F700AA01010103010700CA00C400B400AA00F700B400AA00B600C7010C
010C00AA0140012001B0056810B0013005600000056810E0011006B4B44304B44404B44106B44B4405B443400343B002410636810E06B4B44
407326810B004B43103441003334002B102B404B3B403BB4003B440076820A4100221024405B4341008B44600000231066820A100
Wrapped command --> 84E88013DFC000C400BE00C700CA00CA00B400BE00CE00D200D500D700B000DB00C700DF00BEFFFF00BE00E400AC00AE00AE00DB00E700A
A00EA00ED00ED00ED00BE00EF00F100F400F100F700FA00FF00BE00F700AA01010103010700CA00C400B400AA00F700B400AA00B600C7010C
010C00AA0140012001B0056810B0013005600000056810E0011006B4B44304B44404B44106B44B4405B443400343B002410636810E06B4B44
407326810B004B43103441003334002B102B404B3B403BB4003B440076820A4100221024405B4341008B44600000231066820A15D848CB77
27D0EDA00
Response  80E60C002107A000000527210108A00000052721010108A000000527210101010003C901000000
Wrapped command --> 84E60C002907A000000527210108A00000052721010108A000000527210101010003C9010000B4648127914A4C7C00
Response  /sys/bus/usb/drivers/DRIVER/unbind

## Error: could not be locally signed or gpg: No default secret key: No public key
Occurs when attempting to sign keys on a non-standard keyring while a YubiKey is plugged in, e.g. as Pacman does in . The solution is to remove the offending YubiKey and start over.

## YubiKey disappears and reappears in Yubico Authenticator
This happens when the CCID driver is not installed. You may need to install the  package.

## YubiKey core error: timeout
You are probably using the wrong slot. Try the other one.

## gpg: no such device
gpg (scdaemon) tries to acquire exclusive access to the yubikey. It needs to be configured to use PSCS and use shared access.https://blog.apdu.fr/posts/2024/12/gnupg-and-pcsc-conflicts-episode-3/[https://github.com/LudovicRousseau/PCSC/issues/65

Your configuration file should contain:

For old versions of GnuPG, the  option is not available. Only keep  and restart  as a workaround.
