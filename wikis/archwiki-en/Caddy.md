# Caddy

Caddy is a HTTP/3 capable web server with automatic HTTPS.

## Installation
Install the  package.

## Plugins
If you need more than the base version of caddy, you can use  to customize your caddy server build. This is useful if you need the additional plugins for DNS challenge, etc.
Alternatively, if a pre-built package, with the plugins you require, is already available you may choose to install those from AUR, for example .

For a custom caddy server build you can use xcaddy to build caddy with the necessary plugin modules:

 $ xcaddy build [--output
    ...

For more information, see the xcaddy repository.

## Configuration
Caddy 2 supports various configuration formats, see config adapters (caddyfile, nginx, json, yaml, toml, among others).

Most commonly, Caddy is configured using a plain text file called Caddyfile. The  starts with (an optional global options block and) an address of the site to be served, and is followed by a number of directives.

A simple  hosting the site at :

 {
   http_port 2020
 }

 localhost:2020
 file_server

## Usage
 $ caddy help
 $ caddy help run

Caddy can be run by any user from the page's directory, and the  should be in the same directory:

 $ caddy run

Alternatively you may specify a custom :

 $ caddy run --config ../path/to/Caddyfile

## Troubleshooting
## Certificate error
If you are facing any issues related to SSL certificates (especially on non-public domains), it is probably because the running caddy instance does not have permission to add the certificate to the system's trust store. This seems to be the case when  is used to autostart caddy.

To fix this, run the following as root. You only have to run this once in a very long time (lifetime of the root certificate).

 # XDG_DATA_HOME=/var/lib caddy trust

If you are using admin API through socket use this instead :

 # XDG_DATA_HOME=/var/lib caddy trust --address unix//run/caddy/admin.socket
