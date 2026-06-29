# Mosh

Mosh is an alternative interactive SSH terminal. It has support for roaming and local echo. It also aims to improve responsiveness on intermittent, and high latency connections. To achieve the aim, Mosh uses UDP on the transport layer with AES-128 OCB mode encryption for the session. It employs the OpenSSH dependency for the initial authentication of the session. Hence, Mosh can be used as an add-on for an existing OpenSSH configuration.

## Installation
Install the  package.

The server and client can use different versions of Mosh, but some features are not available in older versions. For example, truecolor support requires that both the server and client use Mosh 1.4.0 or newer.

## Usage
Mosh sessions by default use the first available UDP port in the 60001-60999 range, so it should be accessible in the server.

To connect, run:

 $ mosh user@server-address

To send ssh options for connecting:

 $ mosh --ssh="ssh -p 2222" user@server-address

You can make options permanent by using the usual OpenSSH Client Configuration.
