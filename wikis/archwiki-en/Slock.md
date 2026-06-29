# Slock

Slock, or the "Simple X display locker", is a display locker for X that aims to be minimal, fast, and lightweight.== Installation ==

Install the  package.

## Configuration
Configuration is done by editing the  header file and then recompiling the package. After configuration you should create a package.

## Usage
Simply run  to lock the screen. You can also provide an argument to be run after the screen has been locked:

 $ slock cmd [arg ...

To unlock the screen, just type your password.

## Tips and tricks
## Lock on suspend
Create the following service which locks the screen.

Enable the  systemd unit for it to take effect for the username user.

## Block VT switching and prevent killing X
slock recommends blocking VT switching so that the screen lock cannot be bypassed. For the same reason, slock recommends preventing users from killing the X server. See Xorg#Block TTY access and Xorg#Prevent a user from killing X.
