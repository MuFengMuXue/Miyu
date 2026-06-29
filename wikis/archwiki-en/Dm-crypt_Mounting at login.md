# Dm-crypt/Mounting at login

It is possible to configure PAM and systemd to automatically mount a dm-crypt encrypted home partition when its owner logs in, and to unmount it when they log out.

This tutorial assumes you have already created your encrypted partition, as described in Dm-crypt/Encrypting a non-root file system.

## Unlocking at login
pam_exec can be used to unlock the device at login. Edit  and add the line below emphasized in bold after :

Then create the mentioned script.

Make the script executable.

## Mounting and unmounting automatically
systemd-logind maintains  for as long as at least one session is active for the user. It is started automatically after a first successful login and stopped after a logout from the last session. Hence, we can create and enable a  unit for the mapped volume and connect it to  in order to make it mount and unmount automatically:

## Locking after unmounting
After unmounting, the device will still be unlocked, and it will be possible to mount it without re-entering password (shutting down or rebooting will lock the partition because the key is wiped from RAM, but unmounting alone will not). You can create and enable a service that starts when the device gets unlocked () and dies after the device gets unmounted (), locking the device in the process ():
