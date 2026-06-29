# GNOME/Keyring

GNOME Keyring is "a collection of components in GNOME that store secrets, passwords, keys, certificates and make them available to applications."

It provides org.freedesktop.secrets, an API that allows client applications to store secrets securely using a service running in the user's login session.

## Security
## Protection against malicious application
There was a security issue (known as CVE-2018-19358) reported in the past regarding the behaviour of the GNOME/Keyring API. Any application can easily read any secret if the keyring is unlocked. And, if a user is logged in, then the login/default collection is unlocked. Available D-Bus protection mechanisms (involving the busconfig and policy XML elements) are not used by default and would be easy to bypass anyway.

The GNOME project disagrees with this vulnerability report because, according to their stated security model, untrusted applications must not be allowed to communicate with the secret service.

Applications sandboxed via Flatpak only have filtered access to the session bus.

## Keyring is not locked when session is locked
When the session is locked, the keyring is not automatically locked.This means that the passwords remain in memory which opens the system up to a DMA attack.

## Installation
 is a member of the  group is thus usually present on systems running GNOME. The package can otherwise be installed on its own.  should also be installed to grant other applications access to your keyrings. Although  is deprecated (and superseded by libsecret), it may still be required by certain applications.

The gnome-keyring-daemon is automatically started via a systemd user service upon logging in. It can also be started upon request via a socket.

Extra utilities related to GNOME Keyring include:

*
*

## Manage using GUI
You can manage the contents of GNOME Keyring using Seahorse; install the  package.

Passwords for keyrings (e.g., the default keyring, "Login") can be changed and even removed. See [https://help.gnome.org/seahorse/keyring-create.html Create a new keyring and Update the keyring password in GNOME Help for more information.

## Using the keyring
The PAM module pam_gnome_keyring.so initialises GNOME Keyring partially, unlocking the login keyring in the process. The gnome-keyring-daemon is automatically started with a systemd user service.

## PAM step
When using a display manager, the keyring works out of the box for most cases. GDM, LightDM, LXDM, and SDDM already have the necessary PAM configuration. For a display manager that does not automatically unlock the keyring edit the appropriate file instead of  as mentioned below.

When using console-based login (ie, not using a Display Manager), edit :

Add  at the end of the  section and  at the end of the  section.

## SSH keys
GNOME Keyring can act as a wrapper around ssh-agent. In that mode, it will display a GUI password entry dialog each time you need to unlock an SSH key. The dialog includes a checkbox to remember the password you type, which, if selected, will allow fully passwordless use of that key in the future as long as your login keyring is unlocked.

The SSH functionality is disabled by default in gnome-keyring-daemon builds since version 1:46. It has been moved into , which is part of the  package.

## Setup gcr
Enable and start the  systemd user unit.

Once the unit starts, it will create the socket file .

Manual configuration of  environment variable is not necessary if  unit is active.  The value of  environment variable shall be set to  when user logs out and logs in.

## Using
You can run

 $ ssh-add -L

to list loaded SSH keys in the running agent. This can help ensure you started the appropriate service and set  correctly.

To permanently save a passphrase in the keyring, use ssh-askpass from the  package:

 $ /usr/lib/seahorse/ssh-askpass my_key

To manually add an SSH key from another directory:

 $ ssh-add ~/.private/id_rsa
 Enter passphrase for ~/.private/id_rsa:

To disable all manually added keys:

 $ ssh-add -D

## Disabling
If you wish to run an alternative SSH agent (e.g. ssh-agent directly or gpg-agent), it is a good idea to disable GNOME Keyring's ssh-agent wrapper. Doing so is not strictly necessary, since each agent listens on a different socket and  can be used to choose between them, but it can make debugging issues easier. Note that the GNOME implementation does not support many scripting features such BatchMode To disable gcr-ssh-agent, ensure  and  are both disabled and stopped in systemd.

## Tips and tricks
## Integration with applications
* Chromium

## Locking a keyring
 $ dbus-send --session --dest=org.freedesktop.secrets \
    --type=method_call  \
    /org/freedesktop/secrets \
    org.freedesktop.Secret.Service.Lock \
    array:objpath:/org/freedesktop/secrets/collection/login

This command performs a  D-Bus  method call to lock the login keyring. Alternatively, if you want to use a GUI, Seahorse can be used lock the keyring.

## Flushing passphrases
 $ gnome-keyring-daemon -r -d

This command starts gnome-keyring-daemon, shutting down previously running instances.

## Git integration
The GNOME keyring is useful in conjunction with Git when you are pushing over HTTPS. The  package needs to be installed for this functionality to be available.

Configure Git to use the libsecret helper:

 $ git config --global credential.helper /usr/lib/git-core/git-credential-libsecret

The next time you run , you will be asked to unlock your keyring if it is not already unlocked.

## GnuPG integration
Several applications which use GnuPG require a  to be set. Set the following to use GNOME 3 pinentry for GNOME Keyring to manage passphrase prompts.

Another option is to force loopback for GPG which should allow the passphrase to be entered in the application.

## Renaming a keyring
The display name for a keyring (i.e., the name that appears in Seahorse and from ) can be changed by [https://ttboj.wordpress.com/2013/01/27/renaming-a-gnome-keyring-for-seahorse-the-passwords-and-keyrings-application/ changing the value of display-name in the unencrypted keyring file. Keyrings will usually be stored in  with the .keyring file extension.

## Automatically change keyring password with user password
Append  to :

## Using gnome-keyring-daemon outside desktop environments (KDE, GNOME, XFCE, ...)
## Launching
If you are using sway, i3, or any window manager that does not execute

*
*

your window manager needs to execute the following commands during window manager startup. The commands do not need to be executed in any specific order.

or

This command passes environment variables from the window manager to session dbus. Without this, GUI prompts cannot be triggered over DBus. For example, this is required for seahorse password prompt.

This is required because session dbus is started before graphical environment is started. Thus, session dbus does not know about the graphical environment you are in. Someone or something has to teach session dbus about the graphical environment by passing environment variables describing the graphical environment to session dbus.

During login, PAM starts  which is responsible for keeping gnome-keyring unlocked with login password. If  is not connected to session dbus within a few minutes,  dies. If  is started against session dbus in a window manager,  is connected to session dbus. If your login session does not start  before  quits, you can also use any program that uses gnome-keyring or secret service API before  dies.

## GNOME Keyring XDG Portal
GNOME Keyring exposes an XDG Portal backend (for use with applications sandboxed through flatpak for example). In order for it to work outside of GNOME, one must configure it to be used.  There are a few ways to do this.

## Configuring user-level Secrets Portal
The method which avoids modifying system files is to configure  to be preferred as the  portal in .  For example, to configure sway to use  as the preferred portal to use for .

## Modifying gnome-keyring.portal
Another method is to add your desktop environment to the  configuration file by modifying the  key. For instance, to add sway:

See XDG Desktop Portal#Backends for more information about XDG Desktop Portal backends.

## Troubleshooting
## Passwords are not remembered
If you are prompted for a password after logging in and you find that your passwords are not saved, then you may need to create/set a default keyring. To do this using Seahorse (a.k.a. Passwords and Keys), see Create a new keyring and Change the default keyring in GNOME Help.

## Resetting the keyring
You will need to change your login keyring password if you receive the following error message: "The password you use to login to your computer no longer matches that of your login keyring".

Alternatively, you can remove the  and  files from . Be warned that this will permanently delete all saved keys. After removing the files, simply log out and log in again.

## Unable to locate daemon control file
The following error may appear in the journal after logging in:

 gkr-pam: unable to locate daemon control file

This message "can be safely ignored" if there are no other related issues === No such secret collection at path: / ===

If you try to add a new keyring with Seahorse you may receive this error due to the following reasons:

* The  directory does not exist. Create it if missing.
* A custom  is used. This may be solved by adding the following line [https://bbs.archlinux.org/viewtopic.php?pid=1640822#p1640822

## Terminal gives the message "discover_other_daemon: 1"
This is caused by gnome-keyring-daemon being started for the second time. Since a systemd service is delivered together with the daemon, you do not need to start it another way. So make sure to remove the start command from your , , ,  or similar. Alternatively you can disable the  and  user units.

## Improper initialization of the keyring
There are a few symptoms of this:

* Programs like SSH or Git hang while waiting for the keyring to provide a password, eventually timing out with errors such as "agent refused operation".
* Seahorse does not display any keyring, and manually creating a keyring named "login" does not appear to do anything.
* The following error message appears in seahorse's output:

To address this, do the following:

# Restart the  systemd user unit. This should properly initialize the login keyring.
# Restart the  systemd user unit if used. Other agents might also need restarting.

If this does not fix the issue, consider resetting the keyring.

## SSH agent is not available
Symptom :  returns "Error connecting to agent: Connection refused"

Ensure  user unit is enabled and started:

Ensure  socket and service user unit are enabled and started:

{{ic|$ systemctl --user enable gnome-keyring-daemon.{service,socket}}}
{{ic|$ systemctl --user start gnome-keyring-daemon.{service,socket}}}

## No Process Capabilities, Insecure Memory Might Get Used
If one sees the following error  it means the key-ring could get saved to a swap file/partition. This is a security concern as someone could read and extract the secrets without proper authorization. The solution is to tell the kernel not to do that, but  needs to have the proper permissions to do so.

Run the following command to give  the proper memory locking permissions:
 # setcap cap_ipc_lock=+ep /usr/bin/gnome-keyring-daemon
