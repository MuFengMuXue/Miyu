# Pam usb

pam_usb (active fork of the original repo) provides hardware authentication for Linux using ordinary USB Flash Drives.

It works with any application supporting PAM, such as su and Display manager.

## Installation
Install the  package.

## Configuration
Setting up pam_usb requires the following, once pam_usb is installed:

# Set up devices and users
# Configuring PAM for system authentication

## Setting up Devices and Users
Once you have connected your USB device to the computer, use pamusb-conf to add it to the configuration file:

Note that  can be any arbitrary name you would like. Also, you can add as many devices as you want.

Next, configure users you want to be able to authenticate with pam_usb:

## Check the configuration
You can run  anytime to check if everything is correctly worked. This tool will simulate an authentication request (requires your device to be connected, otherwise it will fail).

## Setting up the PAM module
To add pam_usb into the system authentication process, we need to edit

The default PAM configuration file should include the following line:

Change it to:

The  keyword means that if pam_usb allows the authentication, then no password will be asked. If the authentication fails, then the default password-based authentication will be used as fallback.

If you change it to , it means that both the USB flash drive and the password will be required to grant access to the system.

Now you should be able to authenticate with the relevant USB device plugged-in.

## Enabling events management
pam_usb provides support for lock and unlock events that can trigger a user-defined list of commands along with custom environment variables. For instance, it can be used to instruct pam_usb to automatically lock the current session upon removal of a configured USB device, via the lock event.

There are two pre-requisites for the configured events to be triggered upon a configured USB device insertion/removal:

# The lock and/or unlock events configuration must be added to the pam_usb configuration file;
# The  must be running.

Both topics above are fully descibed in the pam_usb's wiki.

Here is an example of events configuration for a given user. Note that it also takes care of passing the DISPLAY and dbus environment details to the commands to be executed upon events. Both  and  elements content should be changed according to the target environment:

Note that although the  package installs pamusb-agent, it does not configure the system to either manage or start it automatically, this has to be taken care of manually post-installation as a service or simply as a session program, e.g. via Xfce Session and Startup 's Application Autostart control panel.

## Troubleshooting
## su fails to use pam_usb
If you set:

and  prompts for a password, and does not use pam_usb, add the same line at the beginning of . This may be required for other pam-aware applications as well.

## pamusb-check only works with elevated privileges (sudo)
To confirm that this is the same problem, run . Check that the output contains the line .

By default the  is only accessible to privileged users/processes. To use the device to elevate your privileges, the  needs to be accessible to you.

To solve this:
# Create a new group that will have access to the file .
# Add all users, who should be able to use the device, to the group with  e.g.
## Your own user.
## Any system users which will authenticate you, like for instance
## etc.
# Mount the device and navigate to it (The next steps assume the working directory is the root of the device).
# Change the ownership of the  directory and the  file to the  group.
#*
#* Any user added to the  group should work.
# Add permissions so that any one in the group can read, write and execute everything in the  directory.
#*

 should now work without elevated privileges.
