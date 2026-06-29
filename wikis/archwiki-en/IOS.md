# IOS

iOS is an operating system created by Apple Inc. for use in the iPhone series of smartphones. Although connecting iOS devices to Linux is not supported by Apple, the libimobiledevice project provides libraries and tools to connect and transfer data between iOS devices and Linux machines.

## Installation
Install the  and  packages.

## Connecting to a device
## Usbmux daemon
usbmuxd is responsible for performing the low-level connection to iOS devices. The usbmuxd package also includes an udev rule that automatically starts and stops the daemon whenever a device is connected or disconnected.

Connect the iOS device and verify that  is automatically started.

## Pairing
After connecting your iOS device and unlocking the screen, you should be presented with a "Trust This Computer?" popup on the device. Tap "Trust", then enter your device passcode to complete the pairing process.

If you do not see the popup, you can start the pairing process manually. Connect the device, unlock the screen and run:

If you have multiple iOS devices connected  parameter can be passed to target specific device.

You can verify the pairing has succeeded by running:

## Transferring data
After pairing, iOS exposes two different filesystems to the computer. One is the media filesystem, containing the device's photos, videos and music. The second filesystem is used for sharing files directly to certain apps. This is sometimes called "iTunes document sharing". [https://www.hadess.net/2010/12/house-arrest-or-just-document-sharing.html

## Using a graphical file manager
File managers which use GVFS can interact with iOS devices. To access the media filesystem, install . To access the app document filesystem, install .

Dolphin support for iOS devices is included in the  package, which is already a dependency for Dolphin. ==== Manual mounting ====

Install the  package. You can then run the following command to mount your iPhone's media filesystem:

 $ ifuse mountpoint

You can use this to access the device's photos inside .

To access an app's document filesystem, first you need to identify the app:

You can then mount an application's files using:

 $ ifuse --documents APPID mountpoint

Where APPID is the bundle identifier of the desired application, such as .

After you're done, unmount the filesystem:

 $ fusermount -u mountpoint

## Importing videos and pictures
Both photos and videos can typically be found in .

iOS tends to use formats that are not as well supported, but it can be configured to use formats with better compatibility.[https://support.apple.com/en-us/116944 Furthermore, you may wish to convert media that was already saved in one of the less compatible Apple formats.

## Backups
## Creating a backup
You can create a full backup of your iOS device using libimobiledevice by running the following command, where  is the folder you want the backup to be placed in:

 $ idevicebackup2 backup --full backup_to

You may need to authorize the backup request on your iOS device by entering your device passcode.

## Restoring a backup
A backup located in  can be restored by running:

 $ idevicebackup2 restore restore_from

## Accessing the contents of a backup
To access the contents of a backup,  provides the  and  subcommands. The list subcommand is broken.

However, other tools like this one can also be used to view and export contents of a backup.

## Restoring
 can be used to update (reinstall the operating system without touching user data) or restore (reinstall the operating system and erase user data) iOS devices.

## Troubleshooting
## ifuse fails to mount application directories
When using ifuse to mount application directories, you may run into the following error when trying to list the contents of the mountpoint:

 ".": Input/output error (os error 5)

This is a known issue that has been fixed in the current development version of libimobiledevice, but has not been released in a stable version yet. A workaround is to install .

## Device cannot be redirected to a virtual machine
If you use a Windows virtual machine to sync your device via USB, trying to redirect it may fail with a "device is in use by another application" message. This is due to  starting automatically when the device is connected. This can be solved by either stopping or masking .
