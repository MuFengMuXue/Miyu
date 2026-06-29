# Rosenpass

Rosenpass is an open-source post-quantum-secure key exchange protocol designed to secure WireGuard VPN connections against future quantum computing threats. Rosenpass runs in parallel to WireGuard, injecting its post-quantum-secure shared secret into WireGuard's pre-shared key interface. All VPN traffic still only goes through WireGuard, and the WireGuard binary and protocol remain untouched, keeping all security guarantees that WireGuard has on its own.

Rosenpass is written in Rust, the main development being coordinated on GitHub, and is published under the MIT and Apache 2 licenses.

## Installation
Install the  package, which provides Rosenpass and its helper tool rp.

## Testing
As a quick test that the installation succeeded, run both tools rosenpass and rp with the  command to show a short usage hint:

## Configuration
This section shows how to set up a Rosenpass-enhanced WireGuard connection between two peers. Technically, there is no difference between the two peers. However, for clarity, they are named  and .

## Preparing key pairs
Each peer needs to generate a key pair consisting of a secret and a public key.

## Generating secret keys for both peers
The following commands generate the secret keys and store them in newly created  and  directories:

 rp genkey server.rosenpass-secret

 [client$ rp genkey client.rosenpass-secret

## Extracting the public keys
The following commands compute the public keys and store them in newly created  and  directories:

 rp pubkey server.rosenpass-secret server.rosenpass-public

 [client$ rp pubkey client.rosenpass-secret client.rosenpass-public

## Copying each -public directory to the other peer
Both peers need the  directory of other peer, respectively, and it needs to be placed next to the  and  directories that already exist. If you have SSH access to both machines, you can use the following commands:

 scp -r server.rosenpass-public user@client:/path/to/directory

 [client$ scp -r client.rosenpass-public user@server:/path/to/directory

This completes the set-up of the key pairs.

## Launching the Rosenpass-enhanced WireGuard VPN
In the following two commands, replace  with the IP address under which the client can reach the server. This might be a publicly routable IP address, an IP address within your local network, or even the loopback address .

Equally, replace  by the name of the network device on which the server receives packets for the .

You can find information about the network device and IP addresses using the command:

 ip a

## Starting the VPN
Start the Rosenpass and WireGuard processes on both  and . This creates a WireGuard network interface named , which allows, in the next step, to assign an internal IP address, and to add a route for the internal network.

In the following two commands, remember to replace  with the IP address under which the  can reach the .

## Assigning IP addresses
In this example, we use addresses from the internal network  within the VPN. Feel free to try something else, but make sure to adapt IP addresses and networks in all commands where necessary.

 [server# ip a add 192.168.21.1 dev rosenpass0

 ip a add 192.168.21.2 dev rosenpass0

## Adding routes for the WireGuard network
Verify that the routing table containes an entry for the internal network . This can be done with the following command:

 $ ip route

Its output should contain a line about the  network, mentioning the interface :

If such a line is not present, a route can be added using:

 # ip route add 192.168.21.0/24 dev rosenpass0

Remember to verify and do this on both server and client.

## Configuring your firewall
Not sure if you are behind a firewall? You can skip this step and come back in case you cannot get a connection to work.

In this example, the server needs to be reachable on two ports:  for the Rosenpass connection, and  for the WireGuard connection. Port  is explicitly configured in the command used in the next step. The WireGuard port is implicitly set by the rp tool to the Rosenpass port number incremented by one,  in this example.

Configure your firewall(s) such that incoming UDP packets on ports  and  are allowed.

If you use Uncomplicated Firewall, you can use the following commands to add rules that allow the necessary incoming connections for this example setup. Remember to replace  with the IP address under which the client can reach the server, and  by the name of the network device on which the server receives packets for the .

The new firewall rules should look like this:

If you use nftables, you can use the following command to add a rule that satisfies Rosenpass' requirements. This command assumes that the appropriate firewall table and chain are called  and ; both are the standard names used in nftables' example configuration. Remember to replace  with the IP address under which the client can reach the server, and  by the name of the network device on which the server receives packets for the .

{{bc|
[server# nft add rule \
  inet filter input iif $DEVICE \
  udp dport { 9999, 10000 } \
  ip daddr $SERVERIP accept
}}

Make sure to save this rule such that it persists across reboots. One way is to add it to .

## Verifying your setup
## Testing the Rosenpass handshake
As a first test, check if Rosenpass manages to exchange a shared secret and to hand it over to WireGuard as pre-shared key (PSK).

On both the server and the client, you can run the following command to see which pre-shared key WireGuard is using for the connection. Be aware that this shows meant-to-be-secret cryptographic key material, and pay attention to who is able to see your computer's screen:

 # wg show rosenpass0 preshared-keys

The output should show one line consisting of two base64-encoded strings, separated by a space. The second string is the pre-shared key. This should be the same on both machines. Rosenpass changes it approximately every two minutes:

 q1ySvWXjsS2l0Apu2f9YZLw7pLT4+QXfIZVTpMBO01I=    (redacted)

Likewise on both server and client, you can display the state of the WireGuard connection:

 # wg show rosenpass0

On the client, you should see an output like this, where  matches the IP address configured earlier:

And on the server, you should see an output like this, with WireGuard listening port :

The displayed public key of the server should be listed as the ID of the peer on the client, and vice versa.

If you want to continuously watch the current state of the WireGuard tunnel and its pre-shared key, you can use the following command on both client and server; this can be useful during debugging, e.g., to see if both sides keep using the same pre-shared key and exchange it synchronously. This combines the two above commands repeats and them every 2 seconds:

 # watch 'wg show all; wg show all preshared-keys'

## Testing the WireGuard connection
You can test the WireGuard connection by pinging the server's internal IP address from the client peer and vice versa:

 ping 192.168.21.2

 [client$ ping 192.168.21.1

It is possible that the ping from server to client goes through only after the ping from client to server was started.

All done and the ping test works?

Rosenpass will now generate a new PSK key for WireGuard about every two minutes and keep the WireGuard VPN connection secure against post-quantum computer attacks.
