# QBittorrent

qBittorrent is an open source and cross-platform BitTorrent client written in C++, Qt and Python (optional search engine), using  library.

It is fast, stable and light, supports unicode and provides an integrated search engine. It comes with UPnP/NAT-PMP port forwarding, encryption, FAST extension and PeX support.

## Installation
There are two packages in official repositories to install qBittorrent with:

*
*

## Configuration
A configuration file is created at  upon running the program the first time.

## Autostart
## Running as the package-created qbt user
As of -5.0.4-3, an unprivilleged user, qbt, will be created upon installation. The package also ships with  in which this user is hardcoded.

To see the OTP to the WebGUI upon starting the daemon, review the output of: .

In order to prevent the legal disclaimer from being written to journalctl, edit:

## Running as any user
Another option is to run the  in which QBittorrent will run as the user defined.

## Search engine
The optional search engine may be enabled through the menu View > Search Engine, which opens the Search tab.

## Search plugins
Default trackers can be added/enabled in the Search tab by opening the tracker window with Search plugins... (bottom right) and pressing Check for updates. More unofficial search plugins can be found here.

## Web interface
## Default location
By default, qBittorrent will listen on all interfaces on port 8080. Thus it is accessible at .

## Default username & password
The default username is  and the default password for versions before 5.0.0 is . Versions 5.0.0 and above generate a random password visible in console until manually saved to prevent unauthorized access. See here for more information related to this change.

## Allow access without username & password
In a home environment, it is often desirable to allow access to the Web UI without having to input a username and password. This can be configured in the Web UI itself after logging in using the default username and password.

Alternatively, to avoid logging in for the first time, add this section:

The above configuration items will:

* Allow clients logging in from 192.168.1.0/24 to access the Web UI without having to enter a username and password.
* Disable UPnP for the Web UI, so that the Web UI will not be accessible from outside the network.

After that, reload .

## Reverse proxy configuration
## nginx
Refer to qbittorrent wiki

## Themes
## Unofficial themes
* How to use custom UI themes
* List of known qBittorrent themes

## Troubleshooting
## qBittorrent stopped downloading (after reopening)
Sometimes, the  component of the search engines does not terminate after closing . Doing so, it binds the corresponding port, if one was set. Thus, one has to manually terminate the  plugins:

 $ killall nova

## Unable to download I2P torrents
Most I2P specific torrent clients do not implement encryption due to I2P being already encrypted. This means if you have "Encryption Mode" set to "Require encryption" or  set to  in  then downloading will not work.
