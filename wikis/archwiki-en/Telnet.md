# Telnet

From Wikipedia:
:Telnet (short for "teletype network") is a client/server application protocol that provides access to virtual terminals of remote systems on local area networks or the Internet.

Today, telnet is rarely used due to security concerns and is often only used for legacy software and hardware, for information on how to mitigate the security issues see #Security concerns.

## Installation
Install the  package which includes a telnet client, a telnet server with systemd service and sockets.

To configure a telnet server with xinetd, install  as well.

## Configuration
To enable telnet server connections in systemd, enable  (if the telnet server should be started on every boot), and start  to test connectivity.

To enable telnet server connections in xinetd, edit , change  to  and restart the xinetd service.

Enable systemd xinetd service if you wish to start it at boot time.

## Testing the setup
Try opening a telnet connection to your server:
 $ telnet localhost

Try a root login to see if your configuration permits it and the security implications that implies.

## Tips and tricks
## Security concerns
Telnet is a plain text protocol which does not support TLS encryption. Data can be easily intercepted and modified therefore should not be used on production servers, or to transmit sensitive data.

There are attempts to mitigate said security concerns, see #Netkit and #Tunneling for mitigations.

## Netkit
You can use  which modifies the protocol to support TLS encryption.

## Tunneling
You can use a VPN or SSH to create an encrypted tunnel for the telnet traffic between two devices, or networks.
