# Apache HTTP Server/mod gnutls

From mod_gnutls wiki:
:mod_gnutls is an extension for ​Apache's httpd uses the ​GnuTLS library to provide HTTPS.
:It is similar to ​mod_ssl in purpose, but it supports some features and protocols that mod_ssl does not, and it does not use ​OpenSSL.

## Installation
Install , available in the Arch User Repository.

## Configure Apache
Add these lines to :

Make sure that the following line is commented in :

Make sure no vhost definitions include mod_ssl.

Create the file  with the following content:

Restart .

Check that Apache loaded correctly and answers on port 443.

Additional documentation of configuration directives is on the outoforder.cc mod_gnutls documentation page.

## Testing
You can test or verify your https configuration via SSL Labs analyze tool.
