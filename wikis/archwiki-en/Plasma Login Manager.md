# Plasma Login Manager

From the Plasma Login Manager upstream page:

:Plasma Login provides a display manager for KDE Plasma, forked from SDDM and with a new front-end providing a greeter, wallpaper plugin integration and System Settings module (KCM).

## Installation
Install the  package.

Follow Display manager#Loading the display manager to start Plasma Login Manager at boot.

## Configuration
After installation, a new section called Login Screen is added to the System Settings app, allowing it to be configured graphically.

To modify it manually, create a configuration file in . Alternatively, drop configuration files in .

## Custom wallpaper plugins
The KCM (System Settings module) for Plasma Login Manager may fail to list third-party or custom wallpaper plugins, even if they are correctly installed to .

To use a custom wallpaper plugin in this case: manually specify the plugin ID in the configuration file. Identify the plugin ID (folder name in  or the  field in the plugin's  file). Edit the configuration file as follows:

Save the file and log out or reboot to verify the changes.

## Autologin
Plasma Login supports automatic login through its configuration file. For example:

This configuration causes a KDE Plasma session to be started for user  when the system is booted. Available session types can be found in  for X and in  for Wayland.

To automatically log in to KDE Plasma while simultaneously locking the session (e.g. to allow autostarted apps to warm up), see KDE#Lock screen.

## Passwordless login
It is possible to configure Plasma Login to allow logging into some accounts without a password. This differs from automatic login in that the user still has to choose which account to log into, and it differs from simply setting the account password to the empty string in that it only allows interactive users to log in (and not, for example, remote users logged in via SSH).

Plasma Login goes through PAM so you have to create a Plasma Login configuration file  for PAM:

In order to allow unlocking the KDE Plasma lock screen without a password, also create a KDE configuration file  for PAM:

You must then also be part of the  user group to be able to login interactively without entering your password.

## Unlock KDE Wallet automatically on login
See KDE Wallet#Unlock KDE Wallet automatically on login.

## User icon (avatar)
Plasma Login Manager will access user avatars from  by default.  You can use the Plasma System Settings > Users menu to create an avatar, or copy your existing  to the directory:

 # cp /home/user/.face.icon /var/lib/AccountsService/icons/user
