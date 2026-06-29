# Pam autologin

pam_autologin automatically logs in a user. Unlike other autologin methods, this module saves the password and uses it in the normal authentication process. The password can then be used by pam_mount, to mount an encrypted home directory, or by GNOME/Keyring, to unlock the login keyring.

## Installation
Install the  package.

To enable the module for a specific application, edit its configuration in , for example:

The autologin line should be the first module in the  section to allow it to set the username and password. If another module comes first and needs the username, it will prompt you for it.

Autologin will only occur once on each TTY, because when you log out, you most likely intend to log in to another account. The module will search the , ,  paths for logins on its TTY since the last boot. To autologin every time, you can specify the  option:

 auth required pam_autologin.so always

If the login process is run by a PAM-based application, such as a display manager, or a getty/login combination like , then no further configuration is needed. The plain agetty, however, is not a PAM application, and will always prompt for a username anyway. To enable autologin for it, you need to give getty the  option to launch login right away, by adding a drop-in file for systemd's :

{{hc|/etc/systemd/system/getty@.service.d/override.conf|2=
ExecStart=
ExecStart=-/sbin/agetty --skip-login --noreset --noclear - ${TERM}
}}

## Configuration
Tell the autologin module to save the next login by creating its configuration file:

 # touch /etc/security/autologin.conf

Reboot, and you should see a message telling you that the next login will be saved. Log in normally. Reboot again and you should be logged in automatically.

When you want to stop autologin, remove the configuration file:

 # shred -u /etc/security/autologin.conf

Use the shred utility to zero out the file before unlinking it. The file contains your username and password and they can otherwise end up in your unallocated storage area, where some hacker could potentially find them. Although the file is obfuscated with a random key, the key must be stored in the file itself to allow the autologin module to read it automatically, and so can only obfuscate, not protect.

## Security
Autologin is frequently and undeservedly derided as insecure, so a few observations on the subject seem warranted. To decide whether it is insecure for you, you must ask "secure from what?" For the vast majority of users there are only two kind of threats to be concerned about: malware and theft.

Malware and various remote hacking threats come in through bugs in programs running under user privileges, usually the web browser. The login information saved by this module is only readable by root, so malware would first require a privilege escalation vulnerability. Malware running under root privileges can already get your password by recording your login with a keylogger, so autologin will not decrease your security in this situation.

Theft is the other common threat, and the one where autologin does indeed allow the thief full access to everything. How big of a concern theft is for you can vary. If you are using a desktop at home, the chances of it being stolen are negligible in most places. Burglaries are uncommon outside the big cities. You are especially safe if you work at home; burglars dislike dealing with people. Enable autologin on the desktop and you are pretty much as secure as you were without it, and the convenience of not typing your password may well outweigh any remaining concerns.

Laptops, on the other hand, are much more likely to be stolen. Anytime you leave it unattended in public it's unsurprising to find it gone when you return. Using autologin on a laptop would usually not be a good idea, but a laptop is not always used in public. If you only use your laptop at home, it is no more vulnerable to theft than a desktop would be, and using autologin on it would be just as safe. If you use your laptop outside the home, but infrequently, then you could just disable autologin before leaving the house. This way you can still keep everything encrypted, while still having the convenience of autologin when in a safe location.

Under most circumstances, other than on laptops carried in public, using pam_autologin is quite safe and there is little reason to be afraid to do so.
