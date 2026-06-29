# Sudo

Sudo allows a system administrator to delegate authority to give certain users—or groups of users—the ability to run commands as root or another user while providing an audit trail of the commands and their arguments.

Sudo is an alternative to su for running commands as root. Unlike su, which launches a root shell that allows all further commands root access, sudo instead grants temporary privilege elevation to a single command. By enabling root privileges only when needed, sudo usage reduces the likelihood that a typo or a bug in an invoked command will ruin the system.

Sudo can also be used to run commands as other users; additionally, sudo logs all commands and failed access attempts to the journal for security auditing.

## Installation
Install the  package.

Alternatively, install the  package, which is a memory-safe implementation of sudo, albeit with some limitations.

## Usage
To begin using  as a non-privileged user, it must be properly configured. See #Configuration.

To use sudo, simply prefix a command and its arguments with  and a space:

 $ sudo cmd

For example, to use pacman:

 $ sudo pacman -Syu

See  for more information.

## Login shell
You cannot run every command as an other user simply by prepending sudo. In particular when using a redirection and command substitution, you must use a login shell, which can be easily accessed with  (one can omit  if the desired user is root).

In the following example command substitution would work in a full shell, but fails with prepending sudo:

## Permissive umask
Sudo will union the user's umask value with its own umask (which defaults to 0022). This prevents sudo from creating files with more open permissions than the user's umask allows. While this is a sane default if no custom umask is in use, this can lead to situations where a utility run by sudo may create files with different permissions than if run by root directly. If errors arise from this, sudo provides a means to fix the umask, even if the desired umask is more permissive than the umask that the user has specified:

This sets sudo's umask to root's default umask (0022) and overrides the default behavior, always using the indicated umask regardless of what umask the user as set.

## Tips and tricks
## Reduce the number of times you have to type a password
If you are annoyed that you have to re-enter your password every 5 minutes (default), you can change this by setting a longer value for  (in minutes):

If you are using sudo commands in a long script and you do not want to wait for user input when the timeout expires, it is possible to refresh the timeout by separately running  in a loop (whereas  revokes it immediately).

## Disable password prompt timeout
A common annoyance is a long-running process that runs on a background terminal somewhere that runs with normal permissions and elevates only when needed. This leads to a sudo password prompt which goes unnoticed and times out, at which point the process dies and the work done is lost or, at best, cached. Common advice is to enable passwordless sudo, or extend the timeout of sudo remembering a password. Both of these have negative security implications. The prompt timeout can also be disabled and since that does not serve any reasonable security purpose it should be the solution here:

## Passing aliases
The following is only relevant if the bash completion is not available (either full or reduced as described above): Aliases in Zsh and Bash are normally only expanded for the first word in a command. This means that your aliases will not normally get expanded when running the  command. One way to make the next word expand is to make an alias for sudo ending with a space. Add the following to your shell's configuration file:

 alias sudo='sudo '

 describes how this works:
: If the replacement text ends with a space, the next word in the shell input is always eligible for purposes of alias expansions.

As well as :
: If the last character of the alias value is a blank, then the next command word following the alias is also checked for alias expansion.

## Add terminal bell to the password prompt
To draw attention to a sudo prompt in a background terminal, users can simply make it echo a bell character:

Note the  is a literal bell character. E.g. in vim, insert using the sequence  . If  is mapped, e.g. for pasting, one can usually use  instead. In nano,  .

Another option is to set the  environment variable. For example, add the following to your shell configuration file:

 export SUDO_PROMPT=$'\apassword for %p: '

An alternative that allows keeping the localized prompt is to add an alias to your shell's configuration file:

 alias sudo='sudo -B'

## Disable per-terminal sudo
If you are annoyed by sudo's defaults that require you to enter your password every time you open a new terminal, change the  (which is  by default) to  so that all processes with the same parent process ID will share the 5 minutes timeout. This is particularly useful with a terminal multiplexer or tabbed graphical terminal emulators. An other option is to set it to .

## Environment variables
If you have a lot of environment variables, or you export your proxy settings via , when using sudo these variables do not get passed to the root account unless you run sudo with the / option.

 $ sudo -E pacman -Syu

The recommended way of preserving environment variables is to append them to :

## Root password
Users can configure sudo to ask for the root password instead of the user password by adding  (target user, defaults to root) or  to the Defaults line in :

To prevent exposing your root password to users, you can restrict this to a specific group:

## Disable root login
Users may wish to disable the root login. Without root, attackers must first guess a user name configured as a sudoer as well as the user password. See for example OpenSSH#Deny.

The account can be locked via :

 # passwd -l root

A similar command unlocks root.

 $ sudo passwd -u root

Alternatively, you can use the following command to delete the password and then lock the root account :

 $ sudo passwd -dl root

To enable root login again:

 $ sudo passwd root

Note that this merely disables password-based login. The user may still be able to login using another authentication token (e.g. an SSH key). To disable the account use:

 $ usermod --expiredate 1 root

In case of system emergency, the recovery prompt is going to ask you for a root password, making it impossible to log into recovery shell. To automatically unlock the root account in case of emergency add  environment variable to  using a drop-in file:

## kdesu
kdesu may be used under KDE to launch GUI applications with root privileges. It is possible that by default kdesu will try to use su even if the root account is disabled. Fortunately one can tell kdesu to use sudo instead of su. Create/edit the file :

 [super-user-command
 super-user-command=sudo

or use the following command:

 $ kwriteconfig6 --file kdesurc --group super-user-command --key super-user-command sudo

## Harden with sudo example
Let us say you create 3 users: admin, devel, and archie. The user "admin" is used for journalctl, systemctl, mount, kill, and iptables; "devel" is used for installing packages, and editing configuration files; and "archie" is the user you log in with. To let "archie" reboot, shutdown, and use netctl we would do the following:

Edit  and . Require user be in the wheel group, but do not put anyone in it.

Limit SSH login to the 'ssh' group. Only  will be part of this group.

 # groupadd -r ssh
 # gpasswd -a archie ssh
 # echo 'AllowGroups ssh' >> /etc/ssh/sshd_config

Restart .

Add users to other groups.

 # for g in power network ;do ;gpasswd -a archie $g ;done
 # for g in network power storage ;do ;gpasswd -a admin $g ;done

Set permissions on configuration files so  can edit them.

 # chown -R devel:root /etc/{http,openvpn,cups,zsh,vim,screenrc}

With this setup, you will almost never need to login as the root user.

 can connect to their home Wi-Fi.

 $ sudo netctl start home
 $ sudo poweroff

 can not use netctl as any other user.

 $ sudo -u admin -- netctl start home

When  needs to use journalctl or kill run away process they can switch to that user.

 $ sudo -i -u devel
 $ sudo -i -u admin

But  cannot switch to the root user.

 $ sudo -i -u root

If  want to start a GNU Screen session as admin they can do it like this:

 $ sudo -i -u admin
 chown admin:tty `echo $TTY`
 [admin$ screen

## Editing files
 provides the  command (equivalent to ). This is useful for editing files which can be edited by root only while still running the editor as a normal user, and using that user’s configuration.

To edit a file, set  to the name of the editor and pass the file name to . For example:

 $ SUDO_EDITOR=vim sudoedit /etc/file

See #Using visudo and  for ways to set the editor, but beware of possible security issues.

If multiple names are passed to , all files are opened in the editor in a single invocation. A feature useful for merging files:

 $ SUDO_EDITOR=vimdiff sudoedit /etc/file /etc/file.pacnew

## Enable insults
Users can enable the insults easter egg in sudo by adding the following line in the  file with .

Upon entering an incorrect password, this will replace  message with humorous insults.

## Enable password input feedback
By default, there is no visual feedback when you input a password. That is done on purpose for extra security. However, if you wish to have visual input, you can enable it by adding this line:

## Colored password prompt
To customize the password prompt with colors and/or bold fonts, set the  environment variable in your shell initialization file and use .

For example, to set the password prompt to display  in bold red, use this:

 export SUDO_PROMPT="$(tput setaf 1 bold)Password:$(tput sgr0) "

Or use different colors with the default message like so:

 export SUDO_PROMPT="$(tput setab 1 setaf 7 bold)sgr0) $(tput setaf 6)password for$(tput sgr0) $(tput setaf 5)%p$(tput sgr0): "

See more on Color output in console and Bash/Prompt customization

## Using U2F
U2F is great to use with sudo, as it can effectively eliminate the risk of shoulder surfing in public areas while still giving you conscious control to approve the prompt with a simple physical touch.

See Universal 2nd Factor#Passwordless sudo.

## Write to protected files
When using sudo, you may want to write to protected files. Using tee allows such a separation:

 $ input stream | sudo tee --option protected_file_1 protected_file_2...

when a simple / would not have worked.

## In Vim
A similar concept is useful when you forgot to start Vim with sudo when editing a file owned by an other user. In this case you can do the following inside Vim to save the file:

 :w !sudo tee %

You can add this to your  to make this trick easy-to-use with  mapping in command mode:

The  part explicitly throws away the standard output since we do not need to pass anything to another piped command.

More detailed explanation of how and why this works can be found in [https://stackoverflow.com/questions/2600783/how-does-the-vim-write-with-sudo-trick-work How does the vim “write with sudo” trick work? article on StackOverflow.

## Using sudo-rs without the sudo package
You can use sudo-rs as a standalone replacement for sudo, without requiring the  package.

Create  following 's default configuration.

Also create  for :

 # ln -s /etc/pam.d/sudo /etc/pam.d/sudo-i

sudo-rs supports both  and  and uses the latter if it exists. Create at least one of these. A valid minimal config could be this:

Optionally, you can replace  with  by symlinking it from a higher priority  directory:

 # ln -s /usr/bin/sudo-rs /usr/local/bin/sudo
 # ln -s /usr/bin/su-rs /usr/local/bin/su
 # ln -s /usr/bin/visudo-rs /usr/local/bin/visudo
 # ln -s /usr/bin/sudoedit-rs /usr/local/bin/sudoedit
