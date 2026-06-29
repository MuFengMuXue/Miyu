# OfflineIMAP

OfflineIMAP is a Python utility to sync mail from IMAP servers. It does not work with the POP3 protocol or mbox, and is usually paired with a MUA such as Mutt.

## Installation
Install the  package.

## Configuration
Offlineimap is distributed with two default configuration files, which are both located in .  contains every setting and is thoroughly documented. Alternatively,  is not commented and only contains a small number of settings; see: #Minimal.

Copy one of the default configuration files to  or .

## Minimal
The following file is a commented version of .

## Selective folder synchronization
For synchronizing only certain folders, you can use a folderfilter in the remote section of the account in . For example, the following configuration will only synchronize the folders  and :

For more options, see the official documentation.

## Custom port
Some IMAP servers might require you to connect on a custom port, instead of the default 993 port. To do so, add a remoteport option to the remote section in :

## Usage
Before running offlineimap, create any parent directories that were allocated to local repositories:

 $ mkdir ~/mail

Now, run the program:

 $ offlineimap

Mail accounts will now be synced. If anything goes wrong, take a closer look at the error messages. OfflineIMAP is usually very verbose about problems; partly because the developers did not bother with taking away tracebacks from the final product.

## Tips and tricks
## Running offlineimap in the background
Most other mail transfer agents assume that the user will be using the tool as a daemon by making the program sync periodically by default. In offlineimap, there are a few settings that control backgrounded tasks.

Confusingly, they are spread thin all-over the configuration file:

To start the daemon automatically on login, start/enable the systemd/User service  using the  flag.

In case you have more than one account configured, it is advised to use  instead of increasing maxsyncaccounts parameterSimply start/enable .

## systemd timer
Alternatively, it is possible to manage OfflineIMAP completely using systemd-user timers, start/enable  with the  flag.

This timer by default runs OfflineIMAP every 15 minutes. This can be easily changed by creating a drop-in snippet. For example, the following modifies the timer to check every 5 minutes:

For more robust solution it is possible to set a watchdog which will kill OfflineIMAP in case of freeze:

## Automatic mailbox generation for mutt
Mutt cannot be simply pointed to an IMAP or maildir directory and be expected to guess which subdirectories happen to be the mailboxes, yet offlineimap can generate a muttrc fragment containing the mailboxes that it syncs.

Then add the following lines to .

 is the name you have given to your IMAP account in .

## Gmail configuration
This remote repository is configured specifically for &#71;mail support, substituting folder names in uppercase for lowercase, among other small additions. Keep in mind that this configuration does not sync the All Mail folder, since it is usually unnecessary and skipping it prevents bandwidth costs:

## OAuth2 access tokens via oama
[https://github.com/pdobsan/oama oama () is a utility which provides IMAP/SMTP clients with renewal capabilities and authorization of OAuth2 credentials.

OfflineIMAP can call Python code from its configuration. So in the  section at the beginning, add the line:

And in the Python file, add this code to retrieve OAuth2 access tokens via oama:

And now back to the configuration file, in the repository section of a Gmail account, add the following:

## Password management
## .netrc
Add the following lines to your :

 machine hostname.tld
     login username
     password password

Do not forget to give the file appropriate rights like 600 or 700:

 $ chmod 600 ~/.netrc

## Using GPG
GNU Privacy Guard can be used for storing a password in an encrypted file. First set up GnuPG and then follow the steps in this section. It is assumed that you can use your GPG private key without entering a password all the time.

First type in the password for the email account in a plain text file. Do this in a secure directory with  permissions located on a tmpfs to avoid writing the unencrypted password to the disk. Then encrypt the file with GnuPG setting yourself as the recipient.

Remove the plain text file since it is no longer needed. Move the encrypted file to the final location, e.g. .

Now create a python function that will decrypt the password:

Load this file from  and specify the defined function:

## Using pass
pass is a simple password manager from the command line based on GPG.

First create a password for your email account(s):

 $ pass insert Mail/account

Now create a python function that will decrypt the password:

This is an example for a multi-account setup. You can customize the argument to pass as defined previously.

Load this file from  and specify the defined function:

## Gnome keyring
In configuration for remote repositories the remoteusereval/remotepasseval fields can be set to custom python code that evaluates to the username/password. The code can be a call to a function defined in a Python script pointed to by 'pythonfile' config field. Create  according to the subsection below and use it in the configuration:

## gkgetsecret.py
Ensure that , ,  and  are installed. Then create  with the following contents: gkgetsecret.py and set  in  as described above.

If you created a password using , you can retrieve it from its description. For instance, the password for a repository Work which is stored in gnome-keyring with the description Password for me@myworkemail.com can be retrieved by adding the following to :

 Work
 ...
 remotepasseval = get_pw_from_desc("Password for me@myworkemail.com")

For configurations where you wish to store the username as well, it is better if the password is created using secret-tool as this can be used to set attributes such as the username and repository name. Consider a password created with the following command:
 $ secret-tool store --label "Password for Work Email" username me@myworkemail.com repo Work

The username and password for this account can be retrieved by adding the following to :

 Work
 ...
 remoteusereval = get_val_from_attrs("username", "repo", "Work")
 remotepasseval = get_pw_from_attrs("repo", "Work")

## python-keyring
There is a general solution that should work for any keyring. Install  and then change  your ~/.offlineimaprc to say something like:

and somewhere in ~/offlineimap.py add .

Now all you have to do is set your password, either using python script like so:

or you can use keyring command provided by python-keyring package

 $ keyring --help
 $ keyring set host username
 Password for 'username' in 'host':
 $ keyring get host username
 password

and it will grab the password from your (kwallet/gnome-) keyring instead of having to keep it in plaintext or enter it each time.

## Emacs EasyPG
See https://www.emacswiki.org/emacs/OfflineIMAP#toc2

## KeePassXC with Freedesktop.org secret-service
Install , in KeepassXC settings enable Freedesktop.org secret-service integration, expose entries in Database Settings > Secret Service Integration and add additional attribute  with  in Edit Entry > Advanced settings. Now the command  should print the password in the console. Next create a python script:

An equivalent script which relies on  is:

{{hc| ~/.script.py|2=
#! /usr/bin/env python
import secretstorage
from contextlib import closing
def get_pass(title):
    with closing(secretstorage.dbus_init()) as conn:
        assert(secretstorage.check_service_availability(conn))
        collection = secretstorage.get_default_collection(conn)
        if collection.is_locked():
            collection.unlock()
        matches = collection.search_items({"Title": title})
        entry = next(matches)
        if entry.is_locked():
            entry.unlock()
        return(entry.get_secret())
}}

Load this file from  and specify the defined function:

## Troubleshooting
## Overriding UI and autorefresh settings
For the sake of troubleshooting, it is sometimes convenient to launch offlineimap with a more verbose UI, no background syncs and perhaps even a debug level:
 $ offlineimap [ -o ] [ -d  ] [ -u  ]
;-o
:Disable autorefresh, keepalive, etc.

;-d
:Where '''' is one of ,  or . Debugging imap and maildir are, by far, the most useful.

;-u
:Where '''' is one of , , ,  or . TTY.TTYUI is sufficient for debugging purposes.

## Folder could not be created
In version 6.5.3, offlineimap gained the ability to create folders in the remote repository, as described here.

This can lead to errors of the following form when using  on the remote repository:
 ERROR: Creating folder bar on repository foo-remote
   Folder 'bar'could not be created. Server responded: ('NO', ['[ALREADYEXISTS Duplicate folder name bar (Failure)'])

The solution is to provide an inverse  lambda for the local repository, e.g.

* For working out the correct inverse mapping. the output of  should help.
* After updating the mapping, it may be necessary to remove all of the folders under  for the affected accounts.

## SSL fingerprint does not match
 ERROR: Server SSL fingerprint 'keykeykey' for hostname 'example.com' does not match configured fingerprint. Please verify and set 'cert_fingerprint' accordingly if not set yet.

To solve this, add to  (in the same section as ) one of the following:
* either add , with the certificate fingerprint of the remote server. This checks whether the remote server certificate matches the given fingerprint.
* or add  with the path to the system CA certificates file. Needs  installed. This validates the remote ssl certificate chain against the Certification Authorities in that file.

## Copying message, connection closed
 ERROR: Copying message -2 email connection closed
 Folder sent email: ERROR: while syncing sent email connection closed

Cause of this can be creation of same message both locally and on server. This happens if your email provider automatically saves sent mails to same folder as your local client. If you encounter this, disable save of sent messages in your local client.
