# Tox

From the project home page: "Tox is a distributed, secure messenger with audio and video chat capabilities."

## Installation
In order to use Tox, you should install a Tox client. See List of applications/Internet#Tox clients.

## Proxy
To connect via Tor, first start it with:

 /usr/bin/tor

Then configure your Tox client. For example:

 $ toxic -t -p 127.0.0.1 9050

## Run a node
To be able to connect to others, Tox needs to connect to a [https://wiki.tox.chat/users/nodes DHT node first. All DHT nodes are connected to each other, and since everyone is connected to at least one DHT node, you can connect to others one way or the other.

The package  creates user tox-bootstrapd and includes  and a configuration file in .

Edit the configuration file and add appropriate nodes from Tox wiki or Node status page.

Enable and start  and check if it is running fine and port has been bound:
