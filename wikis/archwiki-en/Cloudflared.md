# Cloudflared

Cloudflared may be used to run a local DNS over HTTPS server (DoH), i.e., a stub resolver.

## Installation
Install the  package.

## Usage
Run  to run a DNS over HTTPS proxy server.

Use the  and  options to specify the address and port cloudflared listens to. They default to  and  respectively. For a list of available command line options, see here.

You can create a systemd service file, for example:

After starting the service, you can test that it works by using  (provided by the  package):

 $ drill archlinux.org @127.0.0.1 -p 54

## Checking
Use 1.1.1.1/help to check if browser is using Cloudflare DoH.

## Endpoints
By default cloudflared uses  and , i.e. Cloudflare's DNS over HTTPS servers, as upstream endpoint URLs.

You can specify different upstream endpoint URLs with the  option.
