# NTPsec

The NTP is an unencrypted UDP based protocol and has been abused for attacks in the past. There have been several attempts to provide replacements, however the difficult nature of the protocol and its usage make this quite challenging. While the NTP provides capabilities for encryption, they have been proven to be unreliable. With NTPsec a 'secure' replacement is possible.

## Installation
You can install NTPsec via the  package.

It is necessary to import a new GPG key to your keyring with:

## Starting the service
Normally start/enable the .

## Enable NTS
NTS is a method for using TLS/SSL to authenticate NTP traffic on the net

Append the keyword  to the end of your server lines. Do this only for servers that speak NTS. If the server uses a port other than  for NTS key exchange, you also need to specify the port number.

For example:

Here is an unofficial list of NTP servers supporting NTS.
