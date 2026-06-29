# Keybase

From Wikipedia:
:Keybase is a key directory that maps social media identities to encryption keys (including, but not limited to PGP keys) in a publicly auditable manner. Keybase also offers an encrypted chat and cloud storage system, called Keybase Chat and the Keybase filesystem respectively. Files placed in the public portion of the filesystem are served from a public endpoint, as well as locally from a filesystem mounted by the Keybase client. Keybase supports publicly connecting Twitter, GitHub, Facebook, Reddit, and Hacker News identities to encryption keys, along with Bitcoin and Zcash wallet addresses.

## Installation
Keybase is provided by the  package. The KBFS filesystem and Keybase GUI can be additionally installed with the  and  packages. Alternatively,  is available on the AUR which includes everything in a single package. See also the install instructions on keybase.io.

## Signup / Login
If you installed the GUI via , it will walk you through signup. These instructions are for the CLI-only  package.

Keybase requires its service to be running so you can interact with it. Start the  user unit and enable it to run on boot.

Alternatively, run the keybase service manually:

 $ keybase service

To signup for a Keybase account use, and follow the on-screen prompts:

 $ keybase signup

If you already have a Keybase account you can login with:

 $ keybase login keybase_username

## GnuPG Keys
During the interactive signup if you already have any GnuPG key pairs on your keyring, Keybase will ask if you wish to use one of them.  If you do not have a key pair, you can generate one with:

 $ keybase pgp gen

This will interactively generate a key pair and securely upload the keys.

## Keybase Filesystem (KBFS)
KBFS uses FUSE to mount the remote cryptographic filesystem. It comes with the  package, or can be installed separately with .

Keybase allows users to store up to 250 GB of files in a cloud storage called the Keybase filesystem. The filesystem is divided into three parts: public files, private files, and team files. The filesystem is mounted to  by default if installed through .

To configure kbfs if installed via the  package, first ensure the keybase service is running (see instructions above). Then configure the desired mountpoint for the KBFS:

 $ keybase config set mountdir /path/to/kbfs

Now the  user unit can be started.

Enable this service to have the kbfs mounted on boot.

All files under  are automatically signed by the client. All files under  are both encrypted and signed before being uploaded, making them end-to-end encrypted. See the KBFS docs on keybase.io for more information and usage instructions.

## Troubleshooting
## Keybase GUI starts automatically
By default, keybase-gui add a desktop entry in your autostart. To disable it:

 $ keybase ctl autostart --disable

## Tray icon using AppIndicator GNOME Shell extension
You might find that no icon shows up when Keybase starts, if you are using the  extension. It seems that Electron needs the  to be installed, so that it can create and manage those icons.
