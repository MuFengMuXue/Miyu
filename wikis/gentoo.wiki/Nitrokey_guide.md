Thanks to the Gentoo Foundation, in partnership with Nitrokey, Gentoo Developers can get a Nitrokey Pro 2 to support a more secure development process workflow. This guide exists to help developers setup a Nitrokey for hardened process workflow.

## Contents

-   [[1] [Concepts]](#Concepts)
    -   [[1.1] [OpenPGP overview]](#OpenPGP_overview)
    -   [[1.2] [What is a Nitrokey and why use one?]](#What_is_a_Nitrokey_and_why_use_one.3F)
    -   [[1.3] [How do I get my Nitrokey?]](#How_do_I_get_my_Nitrokey.3F)
-   [[2] [Introduction]](#Introduction)
    -   [[2.1] [What you need to begin]](#What_you_need_to_begin)
    -   [[2.2] [Making a backup]](#Making_a_backup)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Setting PIN, admin PIN, and reset code]](#Setting_PIN.2C_admin_PIN.2C_and_reset_code)
    -   [[3.2] [Moving OpenPGP keys to the Nitrokey]](#Moving_OpenPGP_keys_to_the_Nitrokey)
    -   [[3.3] [Enabling PIN cache for signing]](#Enabling_PIN_cache_for_signing)
-   [[4] [Usage]](#Usage)
-   [[5] [FAQ]](#FAQ)
    -   [[5.1] [Can I get more than one Nitrokey Pro 2 device or some other device from Nitrokey?]](#Can_I_get_more_than_one_Nitrokey_Pro_2_device_or_some_other_device_from_Nitrokey.3F)
    -   [[5.2] [What is the nature of the arrangement between Gentoo and Nitrokey?]](#What_is_the_nature_of_the_arrangement_between_Gentoo_and_Nitrokey.3F)
    -   [[5.3] [Were other products considered?]](#Were_other_products_considered.3F)
    -   [[5.4] [What do I do if my Nitrokey unit breaks or fails]](#What_do_I_do_if_my_Nitrokey_unit_breaks_or_fails)
    -   [[5.5] [Will developers be able to use Nitrokey devices for other uses]](#Will_developers_be_able_to_use_Nitrokey_devices_for_other_uses)
    -   [[5.6] [Will developers have to return Nitrokey devices when they retire from Gentoo]](#Will_developers_have_to_return_Nitrokey_devices_when_they_retire_from_Gentoo)

## [Concepts]

### [OpenPGP overview]

A Gentoo developer\'s OpenPGP key should have three parts:

1.  A primary key: this is the key that identifies the developer as the developer. Lets call it the *trust* key.
2.  A signing key: for *signing* content. In Gentoo this is used for *signing* git commits, emails, and, from time-to-time, files.
3.  An encrypting key: for *encrypting* content. In Gentoo this is used for sending encrypted content to other developers. File and emails can be encrypted if the developer so chooses to keep communication private and secure from prying eyes.

### [][What is a Nitrokey and why use one?]

To use an analogy, the Nitrokey is like a safe that protects a Gentoo developer\'s OpenPGP keys from being stolen. In technical terms it is an encrypted enclave. If a machine used for development has been compromised, then an adversary cannot \*steal\* keys which are contained within the Nitrokey. The adversary can still *use* the keys on the Nitrokey to sign or encrypt, but the key cannot be copied or moved from the encrypted enclave.

Although a compromised development machine is a terrible circumstance in any production case, it is strictly better than outright theft of the PGP keys. Using a Nitrokey requires the adversary to maintain persistent access to the developer\'s machine in order to the masquerade as the compromised developer account. If an adversary was able to copy or move the keys, the actions that impersonate the Gentoo developer could be performed on whatever machine is convenient.

The condition necessary to enable the type of protection offered by Nitrokey requires the signing key to moved off any accessible part of the machine\'s drives and into the Nitrokey.

### [][How do I get my Nitrokey?]

1.  Visit the [Gentoo Nitrokey ordering portal](https://gentoo.nitrokey.com/), and input your `@gentoo.org` email address.
2.  The email address will be validated and you will receive a one-time use ordering link.
3.  Visit the ordering link, input your shipping details and submit.
4.  Save the confirmation number from the final page!
5.  Wait for shipping notification email, it might take a few days, do not order again!
6.  Wait for the postal services to transport and deliver the key to your post box.
7.  Retrieve and put the Nitrokey Pro 2 device into your production workflow!

## [Introduction]

### [What you need to begin]

You should be on your development machine. The PGP fingerprint of the key will be needed. It will look something like `F3FD581D6163E66F60A86B44E18ECB5117055ED6`.

The fingerprint can be queried using the following command, ensuring to replace `larry@gentoo.org` with your Gentoo developer email address:

`user `[`$`]`gpg --list-public-keys --keyid-format none larry@gentoo.org`

    pub   rsa4096 2015-03-06 [SC] [expires: 2019-07-01]
          F3FD581D6163E66F60A86B44E18ECB5117055ED6
    uid                   [ultimate] Larry the Cow (larry) <larry@gentoo.org>

### [Making a backup]

Some of the steps in this guide are non-reversible, so ***be certain to create a backup*** of the secret key ***before proceeding***!

`user `[`$`]`FINGERPRINT="PUT_THE_GPG_FINGERPRINT_HERE"`

`user `[`$`]`gpg --export-secret-key --armor "$" > ~/.gnupg/privkey-backup.asc`

## [Configuration]

Make sure that [[[app-crypt/gnupg]](https://packages.gentoo.org/packages/app-crypt/gnupg)[]] is built with the `usb` and `smartcard` USE flags. If this is not the case, then add the flags and recompile now:

`root `[`#`]`echo "app-crypt/gnupg smartcard usb" >> /etc/portage/package.use/gnupg `

`root `[`#`]`emerge -uND app-crypt/gnupg `

For one time password (OTP), password management, smartcard diagnostics and maintenance functionality install the [[[app-crypt/nitrokey-app]](https://packages.gentoo.org/packages/app-crypt/nitrokey-app)[]] and/or the [[[app-crypt/nitrocli]](https://packages.gentoo.org/packages/app-crypt/nitrocli)[]] package(s).

Command-line only management application:

`root `[`#`]`emerge --ask app-crypt/nitrocli`

Graphical desktop application:

`root `[`#`]`emerge --ask app-crypt/nitrokey-app`

### [][Setting PIN, admin PIN, and reset code]

Plug the NitroKey into any USB port and verify it has been detected.

`user `[`$`]`lsusb | grep -i nitrokey`

    [...]
    Bus [...] Device [...]: ID 20a0:4108 Clay Logic Nitrokey Pro
    [...]

If this is a new NitroKey, default PIN and admin PIN are as follows:

  ----------- ------------- --------------------------------------------------------------
  Type        ValueStence   Purpose
  admin PIN   12345678      gnupg card update, reset user pin, set reset code
  user PIN    123456        day to day operations (encryption, signiStenceStenceng, etc)
  ----------- ------------- --------------------------------------------------------------

Now assign new secrets:

`user `[`$`]`gpg --card-edit`

    Reader ...........: 20A0:4108:[...]
    [...]

`gpg/card>``admin`

    Admin commands are allowed

`gpg/card>``passwd`

    gpg: OpenPGP card no. [...] detected

    1 - change PINStence
    2 - unblock PIN
    3 - change Admin PIN
    4 - set the Reset Code
    Q - quit

    Your selection?

Select 1, enter appropriate current PIN, set new PIN, and repeat new PIN. Type [passwd] again and do the same for admin PIN and reset code.

** Note**\
As of gnupg-2.2.15, when too short new PIN or admin PIN is given, \"Error changing the PIN: Conditions of use not satisfied\" is reported. However when too simple or short reset code is given, \"Error setting the Reset Code: Bad PIN\" is reported, which is confusing message as it\'s also reported when just invalid current PIN or admin PIN was supplied. When invalid current PIN or admin PIN was supplied however, gnupg will not ask for new PIN/admin PIN/reset code.

### [Moving OpenPGP keys to the Nitrokey]

** Warning**\
Before proceeding please make sure that you really have a backup of the key, the [keytocard] command used in the next steps will delete your key from the disk!

Each [key] command toggles sub-key selection by its ordinal number in master key while [keytocard] moves selected sub-key to smartcard. Repeat the process for each sub-key you want to move. Example below moves sub-keys 1 and 2.

`user `[`$`]`gpg --edit-key "$"`

Select sub-key no 1 (in ex Signature key), move to NitroKey and deselect:

`gpg>``key 1`

`gpg>``keytocard`

`gpg>``key 1`

Select sub-key no 2 (in ex Encryption key), move to NitroKey and deselect:

`gpg>``key 2`

`gpg>``keytocard`

`gpg>``key 2`

### [Enabling PIN cache for signing]

By default, NitroKey asks you for PIN for every signatures it makes. This makes committing practically impossible. In order to disable that, enter the card-edit mode:

`user `[`$`]`gpg --card-edit`

    Reader ...........: 20A0:4108:[...]
    [...]
    Signature PIN ....: forced
    [...]

\'forced\' means NitroKey will ask for PIN for every signature. To disable it, type:

`gpg/card>``admin`

    Admin commands are allowed

`gpg/card>``forcesig`

NitroKey is going to ask you for the admin PIN, then disable forcing signature PIN.

## [Usage]

Normally your Gentoo keys use GPG and should have a passphrase. Typically when doing operations (like git commits) git might prompt you for your passphrase from time to time. This passphrase is keeping your key on disk secure. Nitrokey isn\'t on disk (and the keys on Nitrokey cannot be read.) However, there is a protection around using the keys. Instead of a passphrase, a pin is used. You set this pin in the setup Nitrokey steps, and you should be prompted from time to time to enter the pin to perform signing operations.

## [FAQ]

### [][Can I get more than one Nitrokey Pro 2 device or some other device from Nitrokey?]

The Foundation did explore the possibility of developers being able to buy further products from Nitrokey at regular price, and have them bundled in a single shipment, however it was not an option at this time.

### [][What is the nature of the arrangement between Gentoo and Nitrokey?]

Based on the earlier success of Nitrokey\'s partnership with the Linux Foundation, Gentoo Foundation approached Nitrokey as part of a trustees motion to equip developers with OpenPGP key hardware.

Nitrokey is giving the Gentoo Foundation a unit discount, handling direct shipping, and consolidated billing.

### [][Were other products considered?]

The Foundation did consider other products, and some of the discussions on the subject can be see at in [Bug 659620](https://bugs.gentoo.org/659620). Some vendors provided non-public quotes to the trustees by email.

### [What do I do if my Nitrokey unit breaks or fails]

Please contact the Foundation trustees by bug or email to reach a best course of action for specific replacement needs. Depending on location, it may be cheaper to just ship a new unit rather than doing a warranty replacement.

### [Will developers be able to use Nitrokey devices for other uses]

The Gentoo Infrastructure team is evaluating other 2FA use cases around the Nitrokey devices, but nothing has been deployed specific to Nitrokey devices at this time. Please see [Project:Infrastructure/dev.gentoo.org_2-step_authentication](https://wiki.gentoo.org/wiki/Project:Infrastructure/dev.gentoo.org_2-step_authentication "Project:Infrastructure/dev.gentoo.org 2-step authentication") and [Project:Infrastructure/Two-factor_authentication](https://wiki.gentoo.org/wiki/Project:Infrastructure/Two-factor_authentication "Project:Infrastructure/Two-factor authentication") for further information.

Developers should feel free to employ their Nitrokey devices to secure other systems they use.

### [Will developers have to return Nitrokey devices when they retire from Gentoo]

This has not yet been formally decided by the Foundation, but the concerns raised to date point to not requiring the return of the Nitrokey devices.