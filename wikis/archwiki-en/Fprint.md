# Fprint

From the fprint homepage:

:The fprint project aims to plug a gap in the Linux desktop: support for consumer fingerprint reader devices.

The idea is to use the built-in fingerprint reader in some notebooks for login using PAM. This article will also explain how to use regular password for backup login method (solely fingerprint scanner is not recommended due to numerous reasons).

## Prerequisites
You can check if your device is supported by checking the list of supported devices or the list of unsupported devices. To check which one you have, type:

 $ lsusb

The lsusb tool is available inside the  package.

## Installation
Install the  package.  might also be needed.

Some devices require a different fork of , not (yet?) merged with the main libfprint:

*
*

This list is not exhaustive. See many more forks for other devices in the AUR.

## Configuration
Upstream recommends using S2Idle sleep instead of S3 but depending on your device, S3 might work as well.

## Login configuration
Add  as sufficient to the top of the auth section of :

This tries to use fingerprint login first, and if it fails or if it finds no fingerprint signatures in the given user's home directory, it proceeds to password login.

You can also modify other files in {{ic|/etc/pam.d/{login,gdm,lightdm}}} in the same way.

KDE already has fingerprint authentication configured in  so you do not need to edit that file. For a minimal working setup, which asks for your fingerprint first and requires password authentification if it fails on KDE Plasma, it suffices to change the following lines to :

 -auth      default=ignore   pam_systemd_home.so
 auth       default=ignore   pam_fprintd.so
 auth       default=bad     pam_unix.so          try_first_pass nullok

Adding  as sufficient to any configuration file in  when a fingerprint signature is present will only prompt for fingerprint authentication. This prevents the use of a password if you cannot  fingerprint authentication (due to the lack of a shell). In order to use either a password or a fingerprint in a graphical interface, add the following line to the top of any files required:

 auth		sufficient  	pam_unix.so try_first_pass likeauth nullok
 auth		sufficient  	pam_fprintd.so
 ...

This will prompt for a password; pressing  on a blank field will proceed to fingerprint authentication.

If you want to prompt for fingerprint and password input at the same time, you can use . This may be needed for some graphical programs which do not allow blank password input, such as Gnome's built-in polkit agent. To use this package, add the following lines to the top of any files required:

 auth		sufficient  	pam_fprintd_grosshack.so
 auth		sufficient  	pam_unix.so try_first_pass nullok
 ...

## Create fingerprint signature
You will need to have an authentication agent running before being able to enroll.

To add a signature for a finger, run:

 $ fprintd-enroll

or create a new signature for all fingers:

 $ fprintd-delete "$USER"
 $ for finger in {left,right}-{thumb,{index,middle,ring,little}-finger}; do fprintd-enroll -f "$finger" "$USER"; done

You will be asked to scan the given finger. Swipe your right index finger five times. After that, the signature is created in .

You can also enroll without an authentication agent:

 # fprintd-enroll user

To verify the newly created fingerprint, use:

 $ fprintd-verify

For more information, see .

## Restrict enrolling
By default every user is allowed to enroll new fingerprints without prompting for the password or the fingerprint. You can change this behavior using polkit rules.

There are two locations that contains the polkit configuration files:

*
*

In the following example only root can enroll fingerprints:

{{hc|/etc/polkit-1/rules.d/50-net.reactivated.fprint.device.enroll.rules|
polkit.addRule(function (action, subject) {
  if (action.id == "net.reactivated.fprint.device.enroll") {
    return subject.user == "root" ? polkit.Result.YES : polkit.Result.NO
  }
})}}

## Troubleshooting
## No devices available
If your supported device cannot be found or is claimed to be already open (in use), check the  logs in the journal.

You may find log entries like:

 fprintdCorrupted message received
 fprintd[2936592: Ignoring device due to initialization error: unsupported firmware version

Ensure your device's firmware is up to date with Fwupd.

## gdm hangs when revealing login prompt after suspend
This issue is described in libfprint repository. The developers answer is:

:My guess right now is that we are disconnecting the BT USB dongle while it is being initialised. Then everything gets stuck while btusb is trying to load the firmware (this has a 10s timeout, explaining the just under 10s hang that we are seeing). Disconnecting the bluetooth dongle like this is expected to happen when the rfkill switch is toggled, so that is normal. It just seems that the case where the device suddenly disconnects is not handled properly and times out.

The proposed fix is to create:

Or execute straight away:

 # rmmod btusb

Then it should not try to initialize the device.

## Unexpected error while suspending device
This issue is described in libfprint repository:
:You need to set your laptop to not suspend to RAM but to do s2idle. You might need to switch the BIOS into "Windows mode".

## Fingerprint authentication is not taking effect in the Polkit agent.
After adding fingerprint rules to Linux PAM, fingerprint recognition only works for SDDM and sudo, but not for polkit.

Copy the  file to  and change group name  to your user group.

 # cp /usr/share/polkit-1/rules.d/50-default.rules /etc/polkit-1/rules.d/

{{hc|/etc/polkit-1/rules.d/50-default.rules|
polkit.addAdminRule(function(action, subject) {
    return });
}}

## Debug
Use the following environment variable and command line flag:

 # G_MESSAGES_DEBUG=all /usr/lib/fprintd -t

## fprintd starts before fingerprint reader device is initialized after resuming from sleep
Create the following udev rule which enables [https://docs.kernel.org/driver-api/usb/persist.html USB device persistence, replacing the ID with the one for your fingerprint reader which you can find using :

{{hc|/etc/udev/rules.d/01-fingerprint.rules|
ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", ATTRS{idVendor}=="06cb", ATTRS{idProduct}=="00fc", ATTR{power/persist}="1", RUN="/usr/bin/chmod 444 %S%p/../power/persist"
}}

## Sleeping while fprintd is still running breaks fprintd
Fprintd waits 30 seconds after a successful login before quitting, so sleeping during that time period may cause fprintd to break. If that happens, create and enable the following systemd service:

## Enrolling works but verifying does not
Some touch-based fingerprint readers generate images too small for fprint's algorithm to work properly. A common workaround for those is swiping instead of touching the sensor, but the speed at which a good image is generated may vary. Some sensors require a slower swipe and some a faster one. Here are some tips regarding what a good image should look like.

If you want to practice with different speeds to see which generates a better image, try dumping the images with the script examples/img-capture and comparing it with the examples from above (you will need to compile libfprint from source).

See also https://gitlab.freedesktop.org/libfprint/libfprint/-/issues/174

## Unable to enroll as user
If you get an error like , ensure your authentication agent, which prompts the password of the user being enrolled, is properly functioning. However, this can be bypassed by running the command as root:

It is important to pass the name of a regular user, otherwise the fingerprint will be associated with the root user, which is counterproductive to most usecases.

If you get an "enroll-duplicate" error, that finger has already been enrolled as root.  You can either enroll a different finger or remove that finger from the root user with .

After this you should be able to run  as a regular user with no permission errors.
