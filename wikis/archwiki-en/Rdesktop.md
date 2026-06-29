# Rdesktop

rdesktop is a free, open source client for Microsoft's proprietary RDP protocol released under the GNU General Public License.  Use rdesktop to connect to Windows RDP server to remotely administrate the Windows box.

As of July 2008, rdesktop implements a large subset of the RDP 5 protocol, including:

* Bitmap caching
* File system, audio, serial port and printer port redirection
* Mappings for most international keyboards
* Stream compression and encryption
* Automatic authentication
* Smartcard support
* RemoteApp like support called "seamless" mode via SeamlessRDP

Still unimplemented are:

* Remote Assistance requests
* USB device redirection

Support for the additional features available in RDP 5.1 and RDP 6 (including multi-head display spanning and window composition) also have not yet been implemented.

## Installation
Install the  package.

## Usage
For a complete listing of options see .  Here is a typical line:

 $ rdesktop -g 1440x900 -P -z -x l -r sound:off -u windowsuser 98.180.102.33:3389

Reading from left to right:

{| class="wikitable"
|         || Sets the resolution of the display to 1440x900
|-
|                  || Enables bitmap caching/speeds up xfers.
|-
|                  || Enables RDP datastream compression
|-
|                || Uses the "lan" quality experience level, see
|-
|        || Redirects sound generated on the server to null
|-
|      || This defines the username to use when logging into the Windows box
|-
|  || This is the IP address and port number of the target machine
|}

## Tips and tricks
## Automatic scaling of geometry
In order to automatically scale the geometry to fit the screen, one can use the  command line option. Either by using percentage:

 $ rdesktop -g 100% -P -z 98.180.102.33:3389

or with numerical values:

 {{bc|-g $(xrandr -q  awk '/Screen 0/ {print int($8/1.28) $9 int($10/1.2)}'  sed 's/,//g')}}

## Remote desktop using NetBIOS names instead of using IP address
If you do not know the IP address of a Windows computer in a network, you have to enable wins support. To do so, you have to install samba. To enable wins in samba add the following line:

Then you have to install winbind, then edit the  and add the "wins" to the list of hosts.

Restart  and  services and test your success by pinging a Windows NetBIOS host.

## Supplying missing cursors
See Cursor themes#Supplying missing cursors.

## Troubleshooting
## Failed to initialize NLA
When trying to remote desktop into a Windows 10 or Windows 11 host, you might get this error:

 Failed to initialize NLA, do you have correct Kerberos TGT initialized ?
 Failed to connect, CredSSP required by server (check if server has disabled old TLS versions, if yes use -V option)

If you own or have admin access to the host, you can work around this issue by allowing clients to connect without NLA. Search  for instructions. Note that this might introduce security issues on a public-facing host, so use this with caution.
