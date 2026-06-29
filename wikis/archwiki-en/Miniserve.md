# Miniserve

miniserve is a small, self-contained cross-platform CLI tool that allows you to serve files and directories over HTTP.

## Installation
Install the  package.

## Usage
To serve a directory:

 $ miniserve /srv/http

Refer to  or  for additional options, such as custom index files, authentication,  interface binding, TLS, compressed folder download, and file upload capability.

## Configuration
## Temporary
miniserve does not use a configuration file. Instead, all options are passed via the CLI or set through environment variables. For example:

 $ MINISERVE_VERBOSE=true MINISERVE_PORT=8081 miniserve --enable-webdav /srv/http

This enables verbose logging, changes the port from the default 8080 to 8081, and starts miniserve with read-only WebDAV support.

## Permanent
A hardened systemd template unit file  is included with the package and can be customized via a drop-in file.

At first the path you wish to serve (e.g. ) must be escaped for a valid systemd unit name. Use  to format it correctly :

 is your desired path, translated into a valid instance name for the systemd unit.

Use the escaped path as the instance name to configure miniserve with your desired settings:

You might additionally have to override  and  if you plan on making miniserve directly available on a public interface.

Start and enable the unit with full instance name and inspect the journal.

## Testing
Upon startup, miniserve reports the bound interface and a list of available IP addresses:

A health check is implemented and should return "OK":

 $ curl http://127.0.0.1:8080/__miniserve_internal/healthcheck
