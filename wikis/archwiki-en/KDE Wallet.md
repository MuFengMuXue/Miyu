# KDE Wallet

KDE Wallet Manager is a tool to manage passwords on the KDE Plasma system. Using the KWallet subsystem allows a user to keep its own secrets, but also allows a user to access passwords stored by every application that integrates with KWallet.

A wallet (in the KDE's terminology, sometimes called vault or keyring) is an encrypted volume protected by a user-defined password where user and/or software can store secrets (often, credentials when the user checked "Remember the account" in an application). Those vaults can be created and used manually by the user or created and used automatically in the background by some software that integrates with the wallet subsystem (e.g. mail applications or games). Vaults are often decrypted automatically at the user login using a PAM module (see below).

Tips:
* If you only need to have a wallet available for applications using it, it is suggested to use the default name (i.e. ) and the same password as the user (for PAM).
* Wallets are stored as encrypted files using the  extension in the  directory by default.

## Installation
KDE Wallet is often shipped with the KDE Plasma desktop environment. The wallet subsystem can be manually installed with the  package.

Optionally install the  package for the wallet management tool. This tool can be used to graphically create and manage a KDE Wallet.

## Configuration
## Configure PAM on Plasma 6 (KF6)
Plasma 6 uses  as secret service API for .
Therefore PAM must explicitly point to the daemon.

Add to the relevant PAM files (e.g. , ,  depending on setup):

Without the  parameter,  falls back to default and tries to use .

Edit the PAM configuration corresponding to your situation:

* For SDDM, no further edits should be needed because the lines are already present in .
* For LightDM, no further edits should be needed because the lines are already present in  and .
* For GDM, edit  accordingly.
* For greetd, edit  accordingly.
* For unlocking on tty login (no display manager, or like ), edit  accordingly. You will need to specify the force_run parameter.

## Plasma 5 (KF5) – legacy
Older Plasma versions use  and do not require specifying the daemon.

## Unlock KDE Wallet automatically on login
To unlock KDE Wallet automatically on login, install  for the PAM compatible module. The chosen KWallet password must be the same as the current user password.

## Using SDDM autologin and LUKS encryption
When the system is encrypted using dm-crypt it is possible to automatically unlock KDE Wallet using the passphrase that decrypts the disk. When SDDM#Autologin is configured, the wallet can still be unlocked automatically. Edit  to add :

Then edit , and add:

## Tips and tricks
## Using the KDE Wallet to store ssh key passphrases
Install  package.

Set the  environment variable to  and  to  (prefer to use the askpass program instead of the TTY). To set it automatically on each login, create the following  file:

Restart your session (i.e. relogin) so that the environment variables take effect.

The first time you try to use an SSH key, you will get asked for its passphrase. Make sure to check the Remember password checkbox. Next time, the passphrase will be read from KDE Wallet.

## Using the KDE Wallet to store Git credentials
Git can delegate credential handling to a credential helper. By using  as a credential helper, the HTTP/HTTPS and SMTP passwords can be safely stored in the KDE Wallet.

Install the  package.

Configure Git by setting the  environment variable:

See  for alternatives and more details.

## Store GPG key passphrases
Native KDE windows can be used to prompt for GPG key passphrases and save them in KDE Wallet.

Configure  to use .

Enable the Secret Service interface. There are two ways to do this:
* Go to System Settings > KDE Wallet and enable Use KWallet for the Secret Service interface.
* Edit the KDE Wallet configuration file:

Close the wallet and reopen it to affect these changes. You can do this using  or by issuing commands to Qt D-Bus directly:

 $ qdbus org.kde.kwalletd6 /modules/kwalletd6 closeAllWallets
 $ qdbus org.kde.kwalletd6 /modules/kwalletd6 open kdewallet 0 $0

## KDE Wallet for Chromium and VSCode
Chromium-based browsers have built-in wallet integration. VSCode-based IDEs rely on the same Chromium oscrypt module for keyring detection.
To enable it, run the program with either the  or  or  argument.
[https://source.chromium.org/chromium/chromium/src/+/main:docs/linux/password_storage.md

To make the change persistent, see Chromium#Making flags persistent (Setting CHROMIUM_USER_FLAGS will not work).

## Query passwords from the terminal
Instead of storing passwords in plain text files, you can manually add new entries in your wallet and retrieve them with kwallet-query.

For example, if you want to log into the Docker Hub registry with Podman, which supports getting the passwords from stdin with the  flag, you can use the following command to login:

 $ kwallet-query -r folder_entry wallet_name -f folder_name | podman login docker.io -u dockerhub_username --password-stdin

This way, your password is not stored in any text file and neither is it stored in the terminal history file.

In order to run  outside of a graphical session (for instance as part of an unattended backup script), set the  environment variable:

 $ QT_QPA_PLATFORM=offscreen kwallet-query -r folder_entry wallet_name -f folder_name

## Unlocking KWallet automatically in a window manager
To unlock KWallet protected by the login password, it is necessary to start  in the autostart portion of your window manager's configuration file in addition to configuring PAM.

## Disable KWallet
In case you want to permanently disable kwallet:

## Automatic D-Bus activation
Most applications use  D-Bus service. KWallet does not provide a service file for it out of the box.

You can achieve automatic activation by creating such service file:
