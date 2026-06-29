# OpenNTPD

OpenNTPD (part of the OpenBSD project) is a daemon that can be used to synchronize the system clock to internet time servers using the Network Time Protocol, and can also act as a time server itself if needed. It implements the Simple Network Time Protocol version 4, as described in RFC:5905, and the Network Time Protocol version 3, as described in RFC:1305.

## Installation
Install the  package.
The default configuration is actually usable if all you want is to sync the time of the local computer.

## Configuration
To configure OpenNTPD, you need to edit . See  for all available options.

## Client
To sync to a single particular server, edit the  directive.

The  directive works the same as the  directive. However, if the DNS name resolves to multiple IP address, all of them will be synced to. The default, , is working and should be acceptable in most cases. You can find the server's URL in your area at www.pool.ntp.org/zone/@.

Any number of  or  directives may be used.

## Server
If you want the computer you run OpenNTPD on to also be a time server, simply uncomment and edit the "listen" directive.

For example:

will listen on all interfaces, and

will only listen on the loopback interface.

Your time server will only begin to serve time after it has synchronized itself to a high resolution. This may take hours, or days, depending on the accuracy of your system.

## Usage
## Start OpenNTPD at boot
Enable .

## Making openntpd dependent upon network access
If you have intermittent network access (you roam around on a laptop, you use dial-up, etc.), it does not make sense to have  running as a system daemon on start up. Here are a few ways you can control  based on the presence of a network connection.

## Using NetworkManager dispatcher
OpenNTPD can be brought up/down along with a network connection through the use of NetworkManager's dispatcher scripts.

Install .

## Using dhclient hooks
Another possibility is to use dhclient hooks to start and stop openntpd.
When dhclient detects a change in state, it will run the following scripts:

*
*

See .

## Using dhcpcd hooks
See .

## Troubleshooting
## Error adjusting time
If you find your time set incorrectly and in the log, you see:

 openntpd adjtime failed: Invalid argument

Try:

 # ntpd -d

This is also how you would manually sync your system.

## constraint: failed to load constraint ca
OpenNTPD will fail to start on a system with AppArmor if HTTPS constraints are configured in . The journal will show .

This is because AppArmor's  profile does not have read access to LibreSSL's CA certificate file .The solution is to grant access with a local override:

{{hc|/etc/apparmor.d/local/usr.sbin.ntpd|
...
/etc/libressl/{,cert.pem} r,
}}

After editing, reload the AppArmor profile:

 # apparmor_parser -r /etc/apparmor.d/usr.sbin.ntpd
