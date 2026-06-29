# Yggdrasil

Yggdrasil is an early-stage implementation of a fully end-to-end encrypted IPv6 network. It is lightweight, self-arranging, supported on multiple platforms, and allows pretty much any IPv6-capable application to communicate securely with other Yggdrasil nodes.

This article describes how to set up and use Yggdrasil.

## Installation
Install the  package.

## Running
Start/enable .

This will create a  network interface and make available two new IPv6 network interfaces. The important one starts with  which is what your machine will be known as in the Yggdrasil network. This IP address is using a reserved part of the IPv6 standard. This avoids any conflicts with the wider Internet.

To test this works you can run:

 # yggdrasilctl getself

## Configuration
You can create default configuration file  by running , also it will be created and used by running  first time. By default your Yggdrasil instance will not have any peers and thus you are running a standalone service. Editing the  file, which uses the JSON format, allows one to add peers and after restarting the service your node can both reach the wider network, as well as others can find your node.

More details about the configuration is available in the upstream documentation.

To peer with the wider network, start with the public-peers documentation.

## Local firewall
In todays networking practices a common Linux installation is not exposed directly to the Internet. Only servers will typically have a public IP address. As a result our ssh or similar services are not able to be attacked by anyone and everyone.

It is important to realize that running Yggdrasil and peering it to the wider Yggdrasil network changes this. Services that listen on all network connections will become reachable by anyone that connects to this network. You might want configure them to not listen on the Yggdrasil network or quickly hide running services with a couple of firewall rules.

Start/enable  to make this take effect.
