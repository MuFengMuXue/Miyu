# GnuPG

According to the official website:

:GnuPG is a complete and free implementation of the OpenPGP standard as defined by RFC 4880 (also known as PGP). GnuPG allows you to encrypt and sign your data and communications; it features a versatile key management system, along with access modules for all kinds of public key directories. GnuPG, also known as GPG, is a command line tool with features for easy integration with other applications. A wealth of frontend applications and libraries are available. GnuPG also provides support for S/MIME and Secure Shell (ssh).

## Installation
 should already be installed on your system as it is a dependency of .

This will also install , a collection of simple PIN or passphrase entry dialogs which GnuPG uses for passphrase entry. The shell script  determines which pinentry dialog is used, in the order described at #pinentry.

If you want to use a graphical frontend or program that integrates with GnuPG, see List of applications/Security#Encryption, signing, steganography.

## Configuration
## Home directory
The GnuPG home directory is where the GnuPG suite stores its keyrings and private keys, and reads configurations from. By default, the path used is . There are two ways to override this:

* Set the  environment variable.
* Use the  argument, e.g.  By default, the home directory has its permissions set to  and the files it contains have their permissions set to . Only the owner of the directory has permission to read, write, and access the files. This is for security purposes and should not be changed. In case this directory or any file inside it does not follow this security measure, you will get warnings about unsafe file and home directory permissions.

## Configuration files
All of GnuPG's behavior is configurable via command line arguments. For arguments you would like to be the default, you can add them to the respective configuration file:

* gpg checks  (user) and  (global) [https://dev.gnupg.org/T4788. Since gpg is the main entrypoint for GnuPG, most configuration of interest will be here. See GPG Options for possible options.
* dirmngr checks  and . dirmngr is a program internally invoked by  to access PGP keyservers See [https://www.gnupg.org/documentation/manuals/gnupg/Dirmngr-Options.html Dirmngr Options for possible options.

These two configuration files cover the common usecases, but there are more auxiliary programs in the GnuPG suite with their own options. See the GnuPG manual for a comprehensive list.

Create the desired file(s), and set their permissions to  as discussed in #Home directory.

Add to these files any long options you want. Do not write the two dashes, but simply the name of the option and required arguments. For example, to make GnuPG always use a keyring at a specific path, as if it was invoked as :

Other examples are found in #See also.

Additionally, pacman uses a different set of configuration files for package signature verification. See Pacman/Package signing for details.

## Default options for new users
If you want to setup some default options for new users, put configuration files in . When the new user is added in system, files from here will be copied to its GnuPG home directory. There is also a simple script called addgnupghome which you can use to create new GnuPG home directories for existing users:

 # addgnupghome user1 user2

This will add the respective  and  and copy the files from the skeleton directory to it. Users with existing GnuPG home directory are simply skipped.

## Usage
## Create a key pair
Generate a key pair by typing in a terminal:

 $ gpg --full-gen-key

Also add the  option to the command line to access more ciphers and in particular some newer elliptic curves like Curve448.

The command will prompt for answers to several questions. For general use most people will want:

* The default ECC (sign and encrypt) for signing and encryption keys.
* The default Curve 25519 to use Curve25519 and Ed25519.
* An expiration date: a period of one year is good enough for the average user. This way even if access is lost to the keyring, it will allow others to know that it is no longer valid. At a later stage, if necessary, the expiration date can be extended without having to re-issue a new key.
* Your name and email address. You can add multiple identities to the same key later (e.g., if you have multiple email addresses you want to associate with this key).
* no optional comment. Since the semantics of the comment field are not well-defined, it has limited value for identification.
* A secure passphrase, find some guidelines in Security#Choosing secure passwords.

## List keys
To list keys in your public key ring:

 $ gpg --list-keys

To list keys in your secret key ring:

 $ gpg --list-secret-keys

## Export your public key
GnuPG's main usage is to ensure confidentiality of exchanged messages via public-key cryptography. With it each user distributes the public key of their keyring, which can be used by others to encrypt messages to the user. The private key must always be kept private, otherwise confidentiality is broken. See Wikipedia:Public-key cryptography for examples about the message exchange.

So, in order for others to send encrypted messages to you, they need your public key.

To generate an ASCII version of a user's public key to file  (e.g. to distribute it by e-mail):

 $ gpg --export --armor --output public-key.asc user-id

Alternatively, or in addition, you can use a keyserver to share your key.

## Import a public key
In order to encrypt messages to others, as well as verify their signatures, you need their public key. To import a public key with file name  to your public key ring:

 $ gpg --import public-key.asc

Alternatively, try retrieving their public key via WKD (in case the domain of their email address supports it) or using a keyserver.

If you wish to import a key ID to install a specific Arch Linux package, see pacman/Package signing#Managing the keyring and Makepkg#Signature checking.

## Use a keyserver
## Sending keys
You can register your key with a public PGP key server, so that others can retrieve it without having to contact you directly:

 $ gpg --send-keys key-id

## Searching and receiving keys
To find out details of a key on the keyserver, without importing it, do:

 $ gpg --search-keys user-id

To import a key from a key server:

 $ gpg --receive-keys key-id

To refresh/update the keychain with the latest version from a key server:

 $ gpg --refresh-keys

## Key servers
See OpenPGP#Keyserver for a general overview of OpenPGP keyservers and their features.

An alternative key server can be specified with the  option in one of the configuration files, for instance:

A temporary use of another server is handy when the regular one does not work as it should. It can be achieved by, for example,

 $ gpg --keyserver hkps://keys.openpgp.org/ --search-keys user-id

## Web Key Directory
See OpenPGP#Web Key Directory for a general overview.

## Lookup certificates using WKD
When encrypting to an email address (e.g. ), if it is not already in the local keyring, GnuPG, by default, will retrieve the public OpenPGP key using the Web Key Directory protocol (i.e. GnuPG will download the key via HTTPS from the  web server). For example:

 $ gpg --recipient user@example.org --encrypt doc

To retrieve a public key and import it into your keyring, use the  or  options. The former will not do anything if the key already exists in the local keyring, while the later will always refresh the key. For example:

 $ gpg --locate-external-keys user@example.org

## Create a WKD
If you control the domain of your email address yourself and have a web server that provides HTTPS with a trusted TLS certificate, you can follow this guide to enable WKD for your domain.

## Encrypt and decrypt
## Asymmetric
You need to import a public key of a user before encrypting (option /) a file or message to that recipient (option /). Additionally you need to create a key pair if you have not already done so.

To encrypt a file with the name doc, use:

 $ gpg --recipient user-id --encrypt doc

To decrypt (option /) a file with the name doc.gpg encrypted with your public key, use:

 $ gpg --output doc --decrypt doc.gpg

gpg will prompt you for your passphrase and then decrypt and write the data from doc.gpg to doc. If you omit the / option, gpg will write the decrypted data to stdout.

## Symmetric
Symmetric encryption does not require the generation of a key pair and can be used to simply encrypt data with a passphrase. Simply use / to perform symmetric encryption:

 $ gpg -c doc

The following example:

* Encrypts  with a symmetric cipher using a passphrase
* Uses the AES-256 cipher algorithm to encrypt the data
* Uses the SHA-512 digest algorithm to mangle the passphrase and generate the encryption key
* Mangles the passphrase for 65536 iterations

 $ gpg -c --s2k-cipher-algo AES256 --s2k-digest-algo SHA512 --s2k-count 65536 doc

To decrypt a symmetrically encrypted  using a passphrase and output decrypted contents into the same directory as  do:

 $ gpg --output doc --decrypt doc.gpg

## Directory
Encrypting/decrypting a directory can be done with .

Encrypt:
 $ gpgtar -c -o dir.gpg dir

Decrypt:
 $ gpgtar -d dir.gpg

## Key maintenance
## Backup your private key
To backup your private key do the following:

 $ gpg --export-secret-keys --armor --output private-key.asc user-id

If the private key is protected by a passphrase, the exported key file will be protected by the same one.

GnuPG may ask you to enter the passphrase for the key. This is required, because the internal protection method of the secret key is different from the one specified by the OpenPGP protocol.To import the backup of your private key:

 $ gpg --import private-key.asc

## Backup your revocation certificate
Revocation certificates are automatically generated for newly generated keys. These are by default located in . The filename of the certificate is the fingerprint of the key it will revoke.
The revocation certificates can also be generated manually by the user later using:

 $ gpg --gen-revoke --armor --output revcert.asc user-id

This certificate can be used to revoke a key if it is ever lost or compromised. The backup will be useful if you have no longer access to the secret key and are therefore not able to generate a new revocation certificate with the above command. It is short enough to be printed out and typed in by hand if necessary.

## Edit your key
Running the  command will present a menu which enables you to do most of your key management related tasks.

Type  in the edit key sub menu to show the complete list of commands. Some useful ones:

 > passwd       # change the passphrase
 > clean        # compact any user ID that is no longer usable (e.g revoked or expired)
 > revkey       # revoke a key
 > addkey       # add a subkey to this key
 > expire       # change the key expiration time
 > adduid       # add additional names, comments, and email addresses
 > addphoto     # add photo to key (must be JPG, 240x288 recommended, enter full path to image when prompted)

## Exporting subkey
If you plan to use the same key across multiple devices, you may want to strip out your master key and only keep the bare minimum encryption subkey on less secure systems.

First, find out which subkey you want to export.

 $ gpg --list-secret-keys --with-subkey-fingerprint

Select only that subkey to export.

 $ gpg --armor --export-secret-subkeys --output /tmp/tmp.XXXXXXXXXX/subkey.asc subkey-id!

At this point you could stop, but it is most likely a good idea to change the passphrase as well. Import the key into a temporary folder.

 $ gpg --homedir /tmp/tmp.XXXXXXXXXX --import /tmp/tmp.XXXXXXXXXX/subkey.asc
 $ gpg --homedir /tmp/tmp.XXXXXXXXXX --edit-key user-id
 > passwd
 > save
 $ gpg --homedir /tmp/tmp.XXXXXXXXXX --armor --output /tmp/tmp.XXXXXXXXXX/subkey.altpass.asc --export-secret-subkeys subkey-id!

At this point, you can now use  on your other devices.

## Extending expiration date
It is good practice to set an expiration date on your subkeys, so that if you lose access to the key (e.g. you forget the passphrase) the key will not continue to be used indefinitely by others. When the key expires, it is relatively straight-forward to extend the expiration date:

 $ gpg --edit-key user-id
 > expire

You will be prompted for a new expiration date, as well as the passphrase for your secret key, which is used to sign the new expiration date.

Repeat this for any further subkeys that have expired:

 > key 1
 > expire

Finally, save the changes and quit:

 > save

Update it to a keyserver.

 $ gpg --keyserver keyserver.ubuntu.com --send-keys key-id

Alternatively, if you use this key on multiple computers, you can export the public key (with new signed expiration dates) and import it on those machines:

 $ gpg --export --output pubkey.gpg user-id
 $ gpg --import pubkey.gpg

There is no need to re-export your secret key or update your backups: the master secret key itself never expires, and the signature of the expiration date left on the public key and subkeys is all that is needed.

## Rotating subkeys
Alternatively, if you prefer to stop using subkeys entirely once they have expired, you can create new ones. Do this a few weeks in advance to allow others to update their keyring.

Create new subkey (repeat for both signing and encrypting key)

 $ gpg --edit-key user-id
 > addkey

And answer the following questions it asks (see #Create a key pair for suggested settings).

Save changes

 > save

Update it to a keyserver.

 $ gpg --keyserver pgp.mit.edu --send-keys user-id

You will also need to export a fresh copy of your secret keys for backup purposes. See #Backup your private key for details on how to do this.

## Revoke a key
Key revocation should be performed if the key is compromised, superseded, no longer used, or you forget your passphrase. This is done by merging the key with the revocation certificate of the key.

If you have no longer access to your keypair, first import a public key to import your own key.

Then, to revoke the key, import the file saved in #Backup your revocation certificate:

 $ gpg --import revcert.asc

Now the revocation needs to be made public. Use a keyserver to send the revoked key to a public PGP server if you used one in the past, otherwise, export the revoked key to a file and distribute it to your communication partners.

## Signatures
Signatures certify and timestamp documents. If the document is modified, verification of the signature will fail. Unlike encryption which uses the recipient public key to encrypt a document, signatures are created with the sender's private key. The recipient of a signed document then verifies the signature using the sender's public key.

## Create a signature
## Sign a file
To sign a file use the / flag:

 $ gpg --output doc.sig --sign doc

 contains both the compressed content of the original file  and the signature in a binary format, but the file is not encrypted. However, you can combine signing with encrypting.

## Clearsign a file or message
To sign a file without compressing it into binary format use:

 $ gpg --output doc.sig --clearsign doc

Here both the content of the original file  and the signature are stored in human-readable form in .

## Make a detached signature
To create a separate signature file to be distributed separately from the document or file itself, use the  flag:

 $ gpg --output doc.sig --detach-sig doc

Here the signature is stored in , but the contents of  are not stored in it. This method is often used in distributing software projects to allow users to verify that the program has not been modified by a third party.

## Verify a signature
To verify a signature use the  flag:

 $ gpg --verify doc.sig

where  is the signed file containing the signature you wish to verify.

If you are verifying a detached signature, both the signed data file and the signature file must be present when verifying. For example, to verify Arch Linux's latest iso you would do:

 $ gpg --verify archlinux-version.iso.sig

where  must be located in the same directory.

You can also specify the signed data file with a second argument:

 $ gpg --verify archlinux-version.iso.sig /path/to/archlinux-version.iso

If a file has been encrypted in addition to being signed, simply decrypt the file and its signature will also be verified.

## gpg-agent
gpg-agent is mostly used as daemon to request and cache the password for the keychain. This is useful if GnuPG is used from an external program like a mail client.  comes with systemd user sockets which are enabled by default. These sockets are , , , , and .

* The main  is used by gpg to connect to the gpg-agent daemon.
* The intended use for the  on a local system is to set up a Unix domain socket forwarding from a remote system. This enables to use gpg on the remote system without exposing the private keys to the remote system. See  for details.
* The  allows web browsers to access the gpg-agent daemon.
* The  can be used by SSH to cache SSH keys added by the ssh-add program. See #SSH agent for the necessary configuration.
* The  starts a GnuPG daemon handling connections to keyservers.

## Configuration
gpg-agent can be configured via  file. The configuration options are listed in . For example you can change cache ttl for unused keys:

## Reload the agent
After changing the configuration, reload the agent using gpg-connect-agent:

 $ gpg-connect-agent reloadagent /bye

The command should print .

However in some cases only the restart may not be sufficient, like when  has been added to the agent configuration.
In this case you firstly need to kill the ongoing gpg-agent process and then you can restart it as was explained above.

## pinentry
 can be configured via the  stanza to use a particular  user interface when prompting the user for a passphrase. For example:

There are other pinentry programs that you can choose from - see . You may need to install the relevant optional dependencies for your chosen pinentry program.

Remember to reload the agent after making changes to the configuration.

## Cache passwords
 and  defines how many seconds gpg-agent should cache the passwords. To enter a password once a session, set them to something very high, for instance:

For password caching in SSH emulation mode, set  and  instead, for example:

## Unattended passphrase
Starting with GnuPG 2.1.0 the use of gpg-agent and pinentry is required, which may break backwards compatibility for passphrases piped in from STDIN using the  commandline option. In order to have the same type of functionality as the older releases two things must be done:

First, edit the gpg-agent configuration to allow loopback pinentry mode:

Reload the agent if it is running to let the change take effect.

Second, either the application needs to be updated to include a commandline parameter to use loopback mode like so:

 $ gpg --pinentry-mode loopback ...

...or if this is not possible, add the option to the configuration:

## SSH agent
gpg-agent has OpenSSH agent emulation. If you already use the GnuPG suite, you might consider using its agent to also cache your SSH keys.  Additionally, some users may prefer the PIN entry dialog GnuPG agent provides as part of its passphrase management.

## Set SSH_AUTH_SOCK
Set the following variables to communicate with gpg-agent instead of the default ssh-agent.

{{bc|1=
SSH_AGENT_PID=""
SSH_AUTH_SOCK="${XDG_RUNTIME_DIR}/gnupg/S.gpg-agent.ssh"
}}

Alternatively, depend on Bash. This works for non-standard socket locations as well:

{{hc|~/.bashrc|2=
unset SSH_AGENT_PID
if [ "${gnupg_SSH_AUTH_SOCK_by:-0}" -ne $$ ; then
  export SSH_AUTH_SOCK="$(gpgconf --list-dirs agent-ssh-socket)"
fi
}}

## Configure pinentry to use the correct TTY
Also set the GPG_TTY and refresh the TTY in case user has switched into an X session as stated in . For example:

If you use multiple terminals simultaneously and want gpg-agent to ask for passphrase via pinentry-curses from the same terminal where the ssh command was run, add the following to the SSH configuration file. This will make the TTY to be refreshed every time an ssh command is run Note that GPG_TTY environment variable has to be set for this to work.

## Add SSH keys
Once gpg-agent is running you can use ssh-add to approve keys, following the same steps as for ssh-agent. The list of approved keys is stored in the  file.

Once your key is approved, you will get a pinentry dialog every time your passphrase is needed. For password caching see #Cache passwords.

## Using a PGP key for SSH authentication
You can also use your PGP key as an SSH key. This requires a key with the  capability (see #Custom capabilities). There are various benefits gained by using a PGP key for SSH authentication, including:

* Reduced key maintenance, as you will no longer need to maintain an SSH key.
* The ability to store the authentication key on a smartcard. GnuPG will automatically detect the key when the card is available, and add it to the agent (check with  or ). The comment for the key should be something like:  or .

To retrieve the public key part of your GPG/SSH key, run . If your key is authentication-capable but this command still fails with "Unusable public key", add a  suffix ([https://dev.gnupg.org/T2957).

Unless you have your GPG key on a keycard, you need to add your key to  to be recognized as a SSH key. If your key is on a keycard, its keygrip is added to  implicitly. If not, get the keygrip of your key this way:

Then edit  like this. Adding the keygrip is a one-time action; you will not need to edit the file again, unless you are adding additional keys.

## Forwarding gpg-agent and ssh-agent to remote
It is possible to forward one's gpg-agent to a remote machine by forwarding gpg sockets to the remote machine, as explained by the GnuPG wiki.

First, add the following line to  on the remote machine to enable automatic removal of stale sockets on connect. Without this, the socket(s) on the remote machine will need to removed manually before connecting with forwarding enabled for agent forwarding to work:

On the client, use the  SSH directive to forward traffic destined for a remote port, to a port on your local host. As described in , this directive's parameters are the listening socket path on the remote, and then the destination socket path on the local host. Your configuration should look something like this:

The first line configures gpg-agent forwarding:

* remote_agent_socket is the output of  on the remote host.
* local_agent_extra_socket is  on the local host.

The second line is optional. It configures ssh-agent forwarding:

* remote_agent_ssh_socket is  on the remote host.
* local_agent_ssh_socket is  on the local host.

So, with the default paths, it would be:

With this configuration in place, invoking  should automatically forward the gpg-agent to the remote, and allow the use of your gpg key(s) for both decryption/signing (and allows the use of ssh-agent with gpg if the second  line is included).

## Smartcards
GnuPG uses scdaemon as an interface to your smartcard reader, please refer to the man page  for details.

GnuPG's gpg-card tool can be used to configure scdaemon and serves as front-end for smartcard configuration, see  for details.

## GnuPG only setups
If you do not plan to use other cards but those based on GnuPG, you should check the  parameter in . The value '0' refers to the first available serial port reader and a value of '32768' (default) refers to the first USB reader.

## GnuPG with pcscd (PCSC Lite)
 is a daemon which handles access to smartcard (SCard API). In earlier versions, if GnuPG's scdaemon failed to connect to the smartcard directly (e.g. by using its integrated CCID support), it fell back and tried to find a smartcard using the PCSC Lite driver. Since version 2.4 however, you will have to add the  option in , to be able to use pcscd.

To use pscsd install  and . Then start and/or enable  . Alternatively start and/or enable  to activate the daemon when needed.

## Always use pcscd
If you are using any smartcard with an opensc driver (e.g.: ID cards from some countries) you should pay some attention to GnuPG configuration. Out of the box you might receive a message like this when using

 gpg: selecting openpgp failed: ec=6.108

By default, scdaemon will try to connect directly to the device. This connection will fail if the reader is being used by another process. For example: the pcscd daemon used by OpenSC. To cope with this situation we should use the same underlying driver as opensc so they can work well together. In order to point scdaemon to use pcscd you should remove  from , specify the location to  library and disable ccid so we make sure that we use pcscd:

Please check  if you do not use OpenSC.

## Shared access with pcscd
GnuPG  is the only popular  client that uses  flag when connecting to . Other clients like OpenSC PKCS#11 that are used by browsers and programs listed in Electronic identification are using  that allows simultaneous access to single smartcard.  will not give exclusive access to smartcard while there are other clients connected. This means that to use GnuPG smartcard features you must before have to close all your open browser windows or do some other inconvenient operations.

Starting from version 2.2.28 LTS and 2.3.0 you can enable shared access by modifying your  file and adding the line  to the end of it. Keep in mind that  describes this flag as a "somewhat dangerous option" due to "certain information being cached from the card".

## Multi applet smart cards
When using YubiKeys or other multi applet USB dongles with OpenSC PKCS#11 may run into problems where OpenSC switches your Yubikey from OpenPGP to PIV applet, breaking the .

You can hack around the problem by forcing OpenSC to also use the OpenPGP applet. Open  file, search for Yubikey and change the  line to . If  there is no such entry, use  provided by . Search for the Answer to Reset . Then create a new  block referencing your device ATR within the  block.

{{hc|/etc/opensc.conf|2=
app default {
    ...
    card_atr 12:23:34:45:67:89:ab:cd:... {
        name = "YubiKey Neo";
        driver = "openpgp"
    }
}
...
}}

After that you can test with  that the OpenPGP applet is selected by default. Other PKCS#11 clients like browsers may need to be restarted for that change to be applied.

## Using a smart card on a remote client
If for example you log into a machine via SSH or share a smart card to WSL via usbipd-win and try to use an attached device via pcscd, you will notice errors such as:

 gpg: selecting card failed: No such device
 gpg: OpenPGP card not available: No such device

This is due to Polkit restricting access to local clients. To fix this, you can add a rule to allow certain users in all cases. The below rule allows all users in the  group to access devices via :

{{hc|/etc/polkit-1/rules.d/99-pcscd.rules|2=
polkit.addRule(function(action, subject) {
    if (action.id == "org.debian.pcsc-lite.access_card" &&
        subject.isInGroup("wheel")) {
        return polkit.Result.YES;
    }
});
polkit.addRule(function(action, subject) {
    if (action.id == "org.debian.pcsc-lite.access_pcsc" &&
        subject.isInGroup("wheel")) {
        return polkit.Result.YES;
    }
});
}}

After creating the file, make sure to restart .

## OpenPGP compatibility
GnuPG started out as an implementation of the OpenPGP format. Currently, the project is based on RFC 4880 and does not support RFC 9580 (which supersedes RFC 4880).

However, beginning with version 2.4.0 (from December 2022) GnuPG has opted to roll out changes and extensions to the format outside of the IETF process (see draft-koch-librepgp).

Most of the GnuPG-proprietary formats (which diverge from the OpenPGP standard) carry "version 5" or "packet type 20" (these code points are not used in the IETF OpenPGP standard) and introduce incompatibilities:

* GnuPG's "version 5" keys use different fingerprints from v4 (longer, due to the use of SHA-256), but are also visually indistinguishable from v6 (RFC 9580) fingerprints.
* GnuPG's "version 5" signatures use a different calculation method with known design flaws.
* GnuPG's "type 20" symmetrically encrypted data packet format (OCB Encrypted Data Packet) is added, however it also has known design flaws. Support for this format is signalled with a "feature flag" which is aggressively enabled by default. See #Disable unsupported AEAD mechanism.
* GnuPG's Post-Quantum Cryptography formats again diverge from the upcoming IETF specification (see draft-ietf-openpgp-pqc) in arbitrary details that cause incompatibility.

External reviews have raised concerns about the soundness of the format extensions by GnuPG (see A Summary of Known Security Issues in LibrePGP).

See A Critique on "A Critique on the OpenPGP Updates" for a more in-depth discussion of concerns with regard to the GnuPG-specific format changes and "Comparison of RFC 9580 and LibrePGP" for a detailed technical comparison.

Arch Linux's position is to prefer compatibility with the OpenPGP standard.
To this end the patches from the FreePG project (jointly maintained by package maintainers from several Linux distributions) are applied to the  package.
This ensures the longterm compatibility with other OpenPGP implementations and avoids vendor lock-in by default.

## Disable unsupported AEAD mechanism
With  2.4,  generates keys, which advertise support for a GnuPG specific AEAD encryption mechanism (based on OCB). However, this flavor of AEAD is not supported by other OpenPGP implementations!

Although many downstreams attempt to remove this new default by patching the GnuPG sources, when using  the OCB based custom AEAD encryption mechanism is nonetheless set for the new key.

Whether GnuPG's custom AEAD is set for a key can be inspected with the help of  itself:

This mechanism can be disabled:

 $ gpg --expert --edit-key FINGERPRINT
 gpg> setpref AES256 AES192 AES SHA512 SHA384 SHA256 SHA224 ZLIB BZIP2 ZIP
 Set preference list to:
     Cipher: AES256, AES192, AES, 3DES
     AEAD:
     Digest: SHA512, SHA384, SHA256, SHA224, SHA1
     Compression: ZLIB, BZIP2, ZIP, Uncompressed
     Features: MDC, Keyserver no-modify
 Really update the preferences? (y/N) y

## Tips and tricks
## Different algorithm
You may want to use stronger algorithms:

In the latest version of GnuPG, the default algorithms used are SHA256 and AES, both of which are secure enough for most people. However, if you are using a version of GnuPG older than 2.1, or if you want an even higher level of security, then you should follow the above step.

## Encrypt a password
It can be useful to encrypt some password, so it will not be written in clear on a configuration file. A good example is your email password.

First create a file with your password. You need to leave one empty line after the password, otherwise gpg will return an error message when evaluating the file.

Then run:

 $ gpg -e -a -r user-id your_password_file

 is for encrypt,  for armor (ASCII output),  for recipient user ID.

You will be left with a new  file.

## Change trust model
By default GnuPG uses the Web of Trust as the trust model. You can change this to Trust on first use by adding  when adding a key or adding this option to your GnuPG configuration file. More details are in this email to the GnuPG list.

## Hide all recipient id's
By default the recipient's key ID is in the encrypted message. This can be removed at encryption time for a recipient by using . To remove it for all recipients add  to your configuration file. This helps to hide the receivers of the message and is a limited countermeasure against traffic analysis (i.e. using a little social engineering, anyone who is able to decrypt the message can check whether one of the other recipients is the one they suspect). On the receiving side, it may slow down the decryption process because all available secret keys must be tried (e.g. with ).

## Using caff for keysigning parties
To allow users to validate keys on the keyservers and in their keyrings (i.e. make sure they are from whom they claim to be), PGP/GPG uses the Web of Trust. Keysigning parties allow users to get together at a physical location to validate keys. The Zimmermann-Sassaman key-signing protocol is a way of making these very effective. Here you will find a how-to article.

For an easier process of signing keys and sending signatures to the owners after a keysigning party, you can use the tool caff. It can be installed from the AUR with the package .

To send the signatures to their owners you need a working MTA. If you do not have already one, install msmtp.

## Always show long ID's and fingerprints
To always show long key ID's add  to your configuration file. To always show full fingerprints of keys, add  to your configuration file.

## Custom capabilities
For further customization also possible to set custom capabilities to your keys. The following capabilities are available:

* Certify (only for primary keys) - allows the key to create certifications that the User IDs on other keys are correct.
* Sign - allows the key to create cryptographic signatures over data, that others can verify with the public key.
* Encrypt - allows anyone to encrypt data with the public key, that only the private key can decrypt.
* Authenticate - allows the key to authenticate with various non-GnuPG programs. The key can be used as e.g. an SSH key.

It is possible to specify the capabilities of the primary key, by running:

 $ gpg --full-generate-key --expert

And select an option that allows you to set your own capabilities.

Comparably, to specify custom capabilities for subkeys, add the  flag to , see #Edit your key for more information.

## Troubleshooting
## su
When using , you must have the proper permissions of the terminal device (e.g. ) in use. However, with su (or sudo), the ownership stays with the original user, not the new one. This means that pinentry will fail with a  error, even as root. If this happens when attempting to use ssh, an error like  will be returned. The fix is to change the permissions of the device at some point before the use of pinentry (i.e. using gpg with an agent). If doing gpg as root, simply change the ownership to root right before using gpg:

 # chown root $(tty)

and then change it back after su (or sudo) terminated.

## Agent complains end of file
If the pinentry program is , it needs a DBus session bus to run properly. See General troubleshooting#Session permissions for details.

Alternatively, you can use a variety of different options described in #pinentry.

## KGpg configuration permissions
There have been issues with  being able to access the  options. One issue might be a result of a deprecated options file, see the bug report.

## GNOME on Wayland overrides SSH agent socket
For Wayland sessions,  sets  to the standard gnome-keyring socket, . This overrides any value set elsewhere.

See GNOME/Keyring#Disabling on how to disable this behavior.

## mutt
Mutt might not use gpg-agent correctly, you need to set an environment variable  (the content does not matter) when running mutt. Be also sure to enable password caching correctly, see #Cache passwords.

See this forum thread.

## "Lost" keys, upgrading to gnupg version 2.1
When  fails to show keys that used to be there, and applications complain about missing or invalid keys, some keys may not have been migrated to the new format.

Please read GnuPG invalid packet workaround. Basically, it says that there is a bug with keys in the old  and  files, which have now been superseded by the new  file and the  subdirectory and files.  Your missing keys can be recovered with the following commands:

 $ cd
 $ cp -r .gnupg gnupgOLD
 $ gpg --export-ownertrust > otrust.txt
 $ gpg --import .gnupg/pubring.gpg
 $ gpg --import-ownertrust otrust.txt
 $ gpg --list-keys

## gpg hanged for all keyservers (when trying to receive keys)
If gpg hanged with a certain keyserver when trying to receive keys, you might need to kill dirmngr in order to get access to other keyservers which are actually working, otherwise it might keeping hanging for all of them.

## Smartcard not detected
Your user might not have the permission to access the smartcard which results in a  to be thrown, even though the card is correctly set up and inserted.

One possible solution is to add a new group  including the users who need access to the smartcard.

Then use udev rules, similar to the following:

{{hc|/etc/udev/rules.d/71-gnupg-ccid.rules|
ACTION=="add", SUBSYSTEM=="usb", ENV{ID_VENDOR_ID}=="1050", ENV{ID_MODEL_ID}=="0116|0111", MODE="660", GROUP="scard"
}}

One needs to adapt VENDOR and MODEL according to the  output, the above example is for a YubikeyNEO.

## server 'gpg-agent' is older than us (x < y)
This warning appears if  is upgraded and the old gpg-agent is still running. Restart the users  (i.e., use the  flag when restarting).

## IPC connect call failed
Make sure  and  are not running with  and the  folder has permission set to .

By default, the  package uses the directory  for sockets. GnuPG documentation states this is the preferred directory (not all file systems are supported for sockets). Validate that your  configuration specifies a path that has an appropriate file system. You can find your path settings for  by running .

Test that  starts successfully with .

## Mitigating Poisoned PGP Certificates
In June 2019, an unknown attacker spammed several high-profile PGP certificates with tens of thousands (or hundreds of thousands) of signatures (CVE-2019-13050) and uploaded these signatures to keyservers.
The existence of these poisoned certificates in a keyring causes gpg to hang with the following message:

 gpg: removing stale lockfile (created by 7055)

Possible mitigation involves removing the poisoned certificate as per this blog post.

## Invalid IPC response and Inappropriate ioctl for device
The default pinentry program is . If  is unavailable, pinentry falls back to  and causes signing to fail:

 gpg: signing failed: Inappropriate ioctl for device
 gpg: clear-sign failed: Inappropriate ioctl for device

You need to set the  environment variable for the pinentry programs  and .

 $ export GPG_TTY=$(tty)

## Keyblock resource does not exist
If you get an error like this when trying to import keys

 gpg: keyblock resource gnupg_home/pubring.kbx': No such file or directory

it is because GnuPG will not create its home directory if it does not yet exist. Simply create it manually

 $ mkdir -m 700 gnupg_home

## Subkey is created with Restricted capability
In some cases creating a subkey with a custom set of capabilities results in the subkey marked as "Restricted". This happens in the  command with option 7 or 8 ("set your own capabilities") when the capabilities are toggled in the interactive prompt. A workaround is to enter the desired capability set directly as a string instead of toggling individual capabilities, when prompted with the capability selection. For example, enter "=A" to create a subkey with only the Authentication capability.
