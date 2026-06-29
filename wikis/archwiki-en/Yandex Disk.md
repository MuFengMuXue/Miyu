# Yandex Disk

Yandex.Disk is a free cloud storage service created by Yandex that gives you access to your photos, videos and documents from any internet-enabled device.
The official Yandex.Disk console client lets you:

* synchronize files and folders with your Disk,
* get public links to files and folders,
* customize folder syncing.

## Installation
Install the  package. Note that it is a CLI client — there is no official GUI for it at the moment. For alternatives see #Unofficial clients.

To setup your proxy, user and local folder, enter

 $ yandex-disk setup

Syncing will start after completing this step, now you are ready to use Yandex.Disk.

## Commands
You can manage your folder using any file manager or console.

Full list of commands is available in  or using

 $ yandex-disk --help

Here are some examples of use:

*  — Launch the setup wizard.
*  — Launch the daemon and start syncing folders. The current sync status is recorded in the file .
*  — stop the daemon.
*  — show daemon status: sync status, errors, recently synced files, disk space status. If FILE is specified, the status for this file will be returned.
*  — receive OAuth token, encode and save it in a special file (by default ). If the options  or  are not specified, the password will be read from STDIN.
*  — sync the folder and log out (if the daemon is running, wait for syncing to finish).
*  — make the specified file/folder public and print the link to STDOUT. The item will be copied to the sync folder. Use the option  to rewrite existing items.
*  — removes public access to the file/folder.

## Unofficial clients
*
*
*
