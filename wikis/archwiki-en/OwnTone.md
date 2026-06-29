# OwnTone

OwnTone is a free and open-source DAAP (iTunes) and MPD media server with support for AirPlay 1 and 2 speakers (multiroom), Apple Remote (and compatibles), Chromecast, Spotify and internet radio.

OwnTone sends stream to multiple devices, but there are no multiple streams, because there are no multiple users or sessions.

## Installation
Install .

Start/enable the  systemd unit.

## Configuration
See the official documentation for detailed configuration options.

The configuration file is .

## Running as the owntone user
The default user in  is . However, this user is not set in the service file. Edit  and set the user:

If the service was started without the above changes, the user directory will be owned by . Change the owner of the directory if needed with:

 # chown owntone:owntone /var/lib/owntone

Once this is fixed,  will be able to create its configuration files.

## Example Firewall Configuration
Create application profile

Implied Environment for the following instructions:

* IPv4 LAN is  (change to match yours)
* IPv6 LAN is  (change to match yours)
* Apple Home Security is set to "Anyone On the Same Network"

Apply the following instructions with changes to match your environment.

Listening UDP ports are dynamic, so allow LAN UDP traffic on all ports:

Bonjour application profile might need to be added. The following may need to be added:

 ufw allow from 10.0.1.0/24 to 224.0.0.251 comment 'mDNS multicasts'
