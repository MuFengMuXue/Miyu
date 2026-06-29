# Resilio Sync

Resilio Sync (formerly: BitTorrent Sync or BTSync) is a proprietary file sharing system that relies on the BitTorrent Peer-to-peer (P2P) protocol.

Instead of having a central server which archives every file, it uses peer-to-peer connections between the devices themselves therefore there is no limit on data storage and/or transfer speed. The user's data is exclusively stored on the devices with which the user chose to be in sync with, hence it is required to have at least two user devices, or "nodes" to be online. If many devices are connected simultaneously, files are shared between them in a mesh networking topology.

All traffic between devices is encrypted with AES-128 in counter mode, using a unique session key. This key is derived from a 'secret' which itself is a random 21 Byte key Base32-encoded. By handing over the 'secret', files and folders can be shared with other users. When a device adds a folder for synchronization, a secret is generated. From now on, every device that wants to synchronize that folder must know the secret key. The synchronization has no speed or size limits, as long as both devices have enough disk space.

## Installation
Install the  package, which includes systemd service definitions for managing the rslsync daemon. This package creates a default  for system/root operation. Make the desired changes (e.g. login id and password) to those files prior to enabling .

Alternatively, the bare .tar.gz packaged executable can be downloaded from the official website. The rest of this guide assumes that you are using the  package.

## Usage
The Linux client of Resilio Sync does not use a typical GUI, instead it sets up a WebUI server accessible at . Shared folders can also be configured statically in a configuration file, but doing so disables the WebGUI.

Once installed, you will first need to create a configuration file at , see #Configuration. You will also need to create the  directory. When that is done, start and (if you want it to start on boot) start/enable the user service  (i.e., with the  flag).

The service will run as the user invoking the command. Note that the above command is not run as root: doing so may lead to a cryptic error stating that D-Bus has refused the connection.

You can also run it as the  system user (without the  flag).

Configuration for this user is located at , and metadata is saved in  by default. You should review the configuration settings especially user and password, see below.

## Configuration
A sample configuration file can be created using:

 # rslsync --dump-sample-config > ~/.config/rslsync/rslsync.conf

You will probably want to change some of the settings, including:

* device_name
* storage_path
* webui/login
* webui/password

## Automatic configuration file creation
The  package provides a systemd user service called  which, if enabled, triggers when a user's  starts. Then a configuration file with default values will be created if it does not already exist.

The install script enables the service for all users by default. Although defeating most of its purpose,  can be disabled.

Individual users can then enable the  user unit.

 creates  if it does not exist, and guesses some default values of the settings:

* device_name:
* storage_path:
* webui/login:

The script also creates the  directory set in the configuration file if it does not exist. This is done independently from the creation of the configuration file.

## Troubleshooting
## Missing storage path
If you start the service but cannot reach the WebUI, check the unit status for the system-wide instance or the user unit.

A common error is . This is easily fixed by , or whatever your  is set to.

## Ignore some files/folders synchronization
If you don’t want Resilio Sync to track some files in your sync folder, please use .  is located in hidden  folder.

 is a UTF-8 encoded .txt file that allows you to specify single files, paths or rules for ignoring during the synchronization job. Each line of the  file represents a separate rule. All the files that fall under the ignore filter are not indexed and not counted in the "Size" column in Sync main view.

It supports '?' and '*' wildcard symbols.

Note that  is applied only to the folder where it is contained and will not work with the files that have already been synced. If you add indexed files to , they will be deleted on other syncing devices. In order to avoid this:

* Remove the folder from sync on all the devices.
* Modify  file on all of them so that it contains same info.
* Re-add the modified folders.

For further details, please refer to Ignoring files in Sync (IgnoreList)

## Error while loading shared libraries: libcrypt.so.1
If you receive the error message  starting rslsync with the binary or as a service, install the package .
