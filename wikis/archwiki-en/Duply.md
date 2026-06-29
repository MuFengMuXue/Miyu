# Duply

From duply.net:

:Duply is a frontend for the mighty duplicity magic. Duplicity is a python based shell application that makes encrypted incremental backups to remote storages.

## Installation
Duply can be installed with the  package.

## Usage
For an overview on how to use Duply, run .

The first thing to do is create a profile. Run  to create a profile named my_profile. Then configure the profile using the file .

Use  to make backups and  to restore after configuration is complete.

## Configuration
Set GPG_KEY to encrypt and sign the backup with a GPG key. Set the GPG_PW with the GPG passphrase. See #No GPG Passphrase for details on Duply prompting for the GPG passphrase. Set TARGET for the destination of the backup. Set SOURCE for the base location to backup. See the conf file for information on other Duply backup settings.

Example:

Now run  to backup everything in /tmp/important_files. The first time  the user will be prompted for the GPG passphrase so that the key can be exported for safe keeping. Afterwords, Duply should run without prompting for a passphrase.

To exclude files backed up, see the ~/.duply/my_profile/exclude file.

OR

Dupicity exclude requires  as to match the base directory.

## No GPG Passphrase
Because of a bug in the Duply, duplicity will prompt for a GPG passphrase even though it is available from the gpg-agent. Simply pressing return during the prompt will work as the passphrase is not needed to use the key (if the key is cached), or the  line can be added to the conf.

## Signing fails using GPG version 2.1.0 or later
Due to changes in recent versions of GPG, this message may occur during backup process:

 duply gpg: signing failed: Inappropriate ioctl for device

This can be fixed by uncommenting GPG_OPTS section of Duply's conf file and adding --pinentry-mode loopback argument into it:

## Backup configuration
It is important to backup the configuration for your profile so that the backup can be recovered. One way to do this automatically is to add a post script which tars the profile after a backup. For example:

Copy the *.tar.gz file to a secure storage location such as LastPass, KeePass, Bitwarden or an offline USB harddrive. Another option is to archive the profile on a piece of paper as QR code (). The configuration file should accessible even if access is lost to the computer being backed up because the whole point of the backup is that it can be recovered even if the computer is lost or destroyed.
