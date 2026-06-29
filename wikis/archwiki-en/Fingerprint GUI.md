# Fingerprint GUI

Fingerprint GUI is a program that provides an interface and drivers for fingerprint readers. The package includes drivers from the open-source project fprint as well as proprietary drivers not included in fprint.

## Installation
Install .

The package includes an installation guide in HTML at .

If you are using GNOME or KDE follow the instructions pacman gives and remove the following files:

If you are using a window manager, you may need an authentication agent. The package includes an authentication agent . If your window manager is fully XDG compliant, this agent will autostart. An agent is only needed when enrolling fingers, not when identifying.

## Registering fingerprints
After installation, test if your hardware is recognized and correctly working by launching the configuration utility:

 $ fingerprint-gui -d

The  is for debugging, and simply creates a verbose log of events. If you are comfortable without the debug info, you may safely omit the flag.

If your device is not recognized, you might need to reboot in order for udev to set the correct permissions for the device. You may need to add your user to the scanner group.

To start registering your fingerprints with the configuration utility, select the tab "Finger", select a finger and choose "next".

## Authentication
Once your fingerprints have been registered, you may notice that in the setup procedure that the "test" section does not yet work. This is because the necessary authentication has not been approved in the appropriate  files.

As an example of how to set up fingerprint authetication for a given service, we will first start with sudo. Open  in your  text editor and insert the following bold text:

Keep in mind that your 'sudo' file may contain more entries.

Some users may not have (or want to have) sudo installed on their systems. In this case, it is still possible to use your fingerprint to authenticate su. This can be done just like the sudo example, of course instead adding an entry to . Again, add the following bold text.

One may also configure such things as GDM, SDDM, LightDM and the Gnome-Screensaver. Again, if more information or instruction is needed, please refer to the included manual. The Package Maintainer's Manual might provide further information that cannot be obtained by the included manual.

## Verification
Now that the necessary authentication has been added to pam, you may wish the confirm the functionality of your setup. The easiest way to do this is to, again, launch the fingerprint-gui. Rather than go through the steps (as your fingerprints should already be established), click directly on the Settings tab. From here you may select the function you wish to test (ie. sudo, su, gdm, etc).

There is also an included utility to simply confirm that your registered fingerprints are recognized. This can be done by simply running:

 $ fingerprint-identifier

and following the onscreen instructions.

## Exporting
If you wish to save your user's fingerprint data to a file, simply use the Export button in the Settings tab. A file Fingerprints.tar.gz" will be created in the desired directory. The saved file appears to be of little use, however, as an "Import" function has not yet been discovered (as of May 2018).

## Password
In some cases, using your fingerprint to log into the system may inhibit certain other functions of the desktop environment. For example, GNOME Keyring is dependent on your password, as it is used to encrypt the data in your keyring. To overcome this, Fingerprint GUI contains a feature that allows you to store your encrypted password on removable media (USB). You may then use the key to decrypt your keychain by authenticating your fingerprint while the removable media is plugged in.

The manual indicates that to use this function, mount your USB drive and ensure that you have write access to it. Under the "Password" tab of Fingerprint GUI, indicate the appropriate path to your device where it says "Save to directory" (ie. if using gvfs it should be under ). Enter your password and re-enter it and select "save". This will create a hidden directory on your removable media  and create a file . On the local machine, this will also create the file .

## Known issues
## Device is not recognized
If your device (for example , which can be found on recent Thinkpads) is not recognized while it is recognized by the CLI (fprint), it is because currently the Fingerprint GUI is based on an old version. See https://github.com/RogueScholar/fingerprint-gui/issues/5 for details.
