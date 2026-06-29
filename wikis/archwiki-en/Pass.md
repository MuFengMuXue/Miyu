# Pass

From the official website:

:Password management should be simple and follow Unix philosophy. With pass, each password lives inside of a gpg encrypted file whose filename is the title of the website or resource that requires the password. These encrypted files may be organized into meaningful folder hierarchies, copied from computer to computer, and, in general, manipulated using standard command line file management utilities.

pass is a simple password manager for the command line. pass is a shell script that makes use of existing tools like GnuPG,  and Git.

## Installation
Install the  package.

An optional Qt GUI is available via the  package.

## Basic usage
To initialize the password store:

 $ pass init gpg-id_or_email

To create a new password, first provide a descriptive hierarchical name. In this example, this is archlinux.org/wiki/username:

 $ pass insert archlinux.org/wiki/username

To get a view of the password store do the following. Note the example output which shows the hierarchy we just created:

To generate a new random password for the above example, do the following, where  is the desired password length as a number:

 $ pass generate archlinux.org/wiki/username n

To retrieve a password, enter the gpg passphrase at the following prompt, again using the example name from above:

 $ pass archlinux.org/wiki/username

Users of Xorg with  installed can retrieve the password directly onto the clipboard temporarily (e.g., to paste into web forms). In a Wayland session, should use  instead. To do so, do the following (again with the same example hierarchical name from above):

 $ pass -c archlinux.org/wiki/username

pass comes with a dmenu wrapper to enable easy searching/copying. To use it, install the optional dependency  and run:

 $ passmenu

Then selecting an entry will copy its password to the clipboard. See  for customization options such as case-insensitivity. You may want to set this to a systemwide keybinding in order to easily access passwords from any application.

## Data organization
By default, the credential file created with  will only contain your password. However, it may not be enough since several applications ask for detail data like username, url, etc.
You can edit an existing file the way you want with command .
Below is the preferred organizational scheme provided by pass-project page. When using the option  or  with this scheme, only the password will be copied.

## Migrating to pass
There are multiple scripts listed on the pass-project page to import passwords from other programs

## Extensions
Since version 1.7, pass supports extensions developed by the community. These extensions extend the features of pass with the support of new commands.

*
*
*
*
*
*
*
*
*
*

## Advanced usage
Environment variables can be used to alter where pass looks to do store and git operations via:
 PASSWORD_STORE_DIR=/path/to/store

For more information on how this can be used to support multiple pass repositories see this link.
The following  example alias sends the second line of the named database to the clipboard before sending the first line five seconds thereafter and finally an OTP code five seconds after that. Assuming that a password occupies the first line and a username the second line and an OTP URI exists anywhere in the named database, the net effect is passing username > password > otp code for consecutive primary pasting into available (e.g. browser) entry fields:

 pw() {
 export PASSWORD_STORE_CLIP_TIME=8
 export PASSWORD_STORE_X_SELECTION=primary
 pass -c2 $1; sleep 5; pass -c $1; sleep 5; pass otp -c $1; exit
 }

## Multiple pass contexts (e.g. teaming)
One can use aliases to set up different pass contexts, which helps when collaborating with different teams. We have gotten this working in bash as follows:

Add aliases to your shell configuration file:

 alias passred="PASSWORD_STORE_DIR=~/.pass/red pass"
 alias passblue="PASSWORD_STORE_DIR=~/.pass/blue pass"

If using bash, add these for bash-completion to your  and make sure  is installed:

 source /usr/share/bash-completion/completions/pass
 _passred(){
     PASSWORD_STORE_DIR=~/.pass/red/ _pass
 }
 complete -o filenames -o nospace -F _passred passred
 _passblue(){
     PASSWORD_STORE_DIR=~/.pass/blue/ _pass
 }
 complete -o filenames -o nospace -F _passblue passblue

Or for zsh (source: )

 compdef _pass passred
 zstyle ':completion::complete:passred::' prefix "$HOME/.pass/red"
 passred() {
   PASSWORD_STORE_DIR=$HOME/.pass/red pass $@
 }
 compdef _pass passblue
 zstyle ':completion::complete:passblue::' prefix "$HOME/.pass/blue"
 passblue() {
   PASSWORD_STORE_DIR=$HOME/.pass/blue pass $@
 }

Now you can initialize into  and  and have two pass contexts with the  and  aliases. You can generalize this further into as many contexts as you like.

## Git integration
## Git helper usage
You can use  as a credentials helper for . Install the .
Details are described in the github README file.

## git configuration
Configure  as a git credentials helper by calling:
 $ git config --global credential.helper /usr/bin/pass-git-helper

## Mapping file
Create the file . It is used to map git remote hosts to your  database. The format is something like this:

You can use wildcards in the host part, as shown in the example.

## Password store layout
As usual with pass, the helper assumes that the password is contained in the first line of the passwordstore entry.
Additionally, if a second line is present, this line is interpreted as the username.

For this to work, you have to use  to create a multi line password store entry.

## Central Git server for pass in combination with GnuPG (SSH example)
You are able to setup a password management system by setting up a central Git server for pass. This allows you to synchronize your central password repository through multiple client environments.

## Install a bare Git repository for pass on the server
On the server run  to create a bare repository you can push to.

## Import authorized public SSH keys
See SSH keys#Copying the public key to the remote server

## On the client
This section assumes you have configured GnuPG and have a key pair to encrypt passwords.
On your local client ensure you have a local password store on the client, then enable management of local changes through Git, add your remote Git repository, and push your local pass history.

Create a local password store:

 $ pass init gpg_key_id

Enable management of local changes through Git:

 $ pass git init

Add the remote git repository as 'origin':

 $ pass git remote add origin user@server:~/.password-store

Push your local pass history:

 $ pass git push -u --all

Now you can use the standard Git commands, prefixed by . For example: , or . pass will automatically create commits when you use it to modify your password store.

## Troubleshooting
## Encryption failed: Unusable public key
The following error can occur when attempting to insert a new entry:

This occurs if the trust level of the GnuPG key is set to anything other than "ultimate". Edit the key used for  to set its trust level to "ultimate":

## Secret key expired
The following error can occur when your GPG key expires (e.g., after a year) and you try to add a new password:

To fix this, either extend the current GPG key's expiration date or switch to a new one (i.e., key rotation).

To switch to a new key and re-encrypt the store:

 $ pass init new_gpg-id_or_email
