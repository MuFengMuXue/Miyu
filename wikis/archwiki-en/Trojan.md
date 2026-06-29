# Trojan

Trojan is a proxy server, client and protocol, designed to bypass the Great Firewall of China by imitating HTTPS. Trojan claims to be unidentifiable.

## Installation
Install one of the following options:

*  − the official Trojan implementation in C++, for which development has long been stalled.
*  − Go implementation with features such as multiplexing, AEAD and routing based on destination IP.
*  − Rust implementation with an emphasis on high performance and low memory usage.

## Configuration
Trojan cannot run without proper configuration. It uses JSON as its configuration format. All configuration work is done in . Detailed explanations of each field of the configuration file can be found on the GitHub repository.

Examples of configuration files are at .

## TLS certificate
You will need to provide a TLS certificate and private key for Trojan servers to work. You can either apply for a free certificate with some automation tools like Acme.sh from Let's Encrypt or generate a self-signed one as shown in OpenSSL#Generate a self-signed certificate. Then, set the , , and (not necessarily) fields in the configuration file accordingly. Note that you should pin the certificate by setting  on the client if you generate a self-signed certificate. Also, make sure that trojan on a server has enough permission to access the certificate and key file.

## TCP Fast Open
For TCP Fast Open on servers to work, you will need to turn it on in your OS:
 # echo 3 > /proc/sys/net/ipv4/tcp_fastopen

## Disguise
Trojan servers can be disguised as other services over TLS to prevent active probing. This can be done by, for example, running a web server with nginx and pointing  and  fields to the server address and port.

## Running
## systemd services
Trojan can be controlled with  and . For example, start/enable the  instance to run Trojan with the  configuration file. Trojan can be similarly ran with  by starting/enabling .

## Manually
Trojan can also start in a shell, by running:
 $ trojan /etc/trojan/config.json

You can replace  with any other configuration files. Note that Trojan outputs its log to stderr, so you will have to redirect it to a file if you want to keep the log.
