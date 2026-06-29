# Acme.sh

acme.sh is an ACME client written purely in shell script. It implements the full ACME protocol and supports, for example, IPv6 and wildcard certificates.

## Installation
Install the  package, and  if you want to use the standalone mode.

## Usage
The package does not provide man pages, but a wiki for usage. Executing  outputs a long list of commands and parameters.

There are three basic steps involved:

# Requesting a certificate to be issued.
# Installing the issued certificate, to make it useful.
# Maintaining the certificate over time.

as covered with below examples.

## Issuing a new cert
You can specify any domain with the  option.

The  script support different modes. Examples for modes and options to be specified are:

* Webroot mode:
* Standalone mode, by adding  if no web server is running (requires  installed):
* Nginx mode
* DNS mode:

The project's wiki lists more examples.

## Install the cert to Apache/Nginx etc
Nginx:

 $ acme.sh --install-cert -d example.com \
    --key-file         /path/to/keyfile/in/nginx/key.pem  \
    --fullchain-file /path/to/fullchain/nginx/cert.pem \
    --reloadcmd    "systemctl force-reload nginx"

Apache:

 $ acme.sh --install-cert -d example.com \
    --cert-file        /path/to/certfile/in/apache/cert.pem  \
    --key-file         /path/to/keyfile/in/apache/key.pem  \
    --fullchain-file /path/to/fullchain/certfile/apache/fullchain.pem \
    --reloadcmd    "systemctl force-reload httpd"

## Maintaining a cert
The certs will be renewed every 60 days. To run  regularly, a systemd timer may be set up.
