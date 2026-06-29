# Shadowsocks

Shadowsocks is a lightweight proxy. It is based on the SOCKS5 protocol, but additionally uses encryption, which improves security and helps to bypass firewalls.

## Installation
Install the  package.

## Alternative implementations
*  — written in Go.
*  — written in Python. No longer in development.
*  — written in C. No longer in development.
*  — written in Go. No longer in development.

## Configuration
Shadowsocks configuration is done with a JSON formatted file. See Configuration via Config File.

## Usage
## Client
## From the command line
The client is started with the  (shadowsocks-libev) or  (shadowsocks, shadowsocks-rust) command, see  for details:

 sslocal -b 127.0.0.1:1080 --server-url ss://

Or via config file:

 sslocal -c config.json

{{hc|config.json|
{
 "remarks": "Server name",
 "server": "111.111.111.111",
 "server_port": 804,
 "local_port": 1080,
 "method": "chacha20-ietf-poly1305",
 "password": "server_password"
}
}}

## Daemon management
The Shadowsocks client can be controlled with an instance of  (shadowsocks) or  (shadowsocks-libev) through systemctl. To use the configuration file , start and enable  or .

You may also be interested in running an instance of  or  after the network is up.

## Server
## From the command line
The server is started with the  (shadowsocks-libev) or  (shadowsocks, shadowserver-rust) command, see the  manual.

## Daemon management
The Shadowsocks server can be controlled with an instance of  (shadowsocks-rust) or  (shadowsocks). To use the configuration file , start and enable  or .

To bind Shadowsocks to a privileged port (less than ), the server should be started as user root:

## Tips and tricks
## Performance optimization
* Use common ports such as . The Great Firewall checks relatively few commonly used ports to reduce stress.
* Enable TCP Fast Open.
* Enable BBR.
* Install  to increase the speed of shadowsocks.
* Optimize kernel parameters, see Optimizing Shadowsocks.

## Encryption
See AEAD Ciphers.

Installing the  package will make encryption a little faster.

To use Salsa20 or ChaCha20 ciphers, install the  package.
