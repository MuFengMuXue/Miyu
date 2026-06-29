# Stubby

Stubby is an application that acts as a local DNS Privacy stub resolver (using DNS-over-TLS). Stubby encrypts DNS queries sent from a client machine (desktop or laptop) to a DNS Privacy resolver, increasing end user privacy.

## Installation
Install the  package.

## Configuration
To configure stubby, perform the following steps:

## Select resolver
Upon installation, Stubby has some default resolvers. They can be found and edited in . You can use the defaults, uncomment one of prewritten resolvers or find another resolver from this list.

Example of a valid resolver configuration:

When you get warn log complaining wrong tls_pubkey_pinset, the tls_pubkey_pinset value may be wrong and the  of the  can be generated with:

 $ openssl s_client -connect address_data:tls_port /dev/null | openssl x509 -pubkey -noout | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | openssl enc -base64

## Enable DNSSEC validation
Enable DNSSEC validation by uncommenting the following line in :

## Modify resolv.conf
After selecting a resolver, modify the resolv.conf file and replace the current set of resolver addresses with address for localhost:

Other programs may overwrite this setting; see resolv.conf#Overwriting of /etc/resolv.conf for details.

## Start systemd service
Finally, start/enable the .

## Tips and tricks
## Local DNS cache configuration
Stubby does not have a built-in DNS cache, therefore every single query is transmitted and resolved, which can slow down connections. Setting up a DNS cache requires installing and configuring a separate DNS cacher.

## Change port
In order to forward to a local DNS cache, Stubby should listen on a port different from the default , since the DNS cache itself needs to listen on  and query Stubby on a different port. Port number  is used as an example in this section.

Edit the value of  as follows:

## dnsmasq
Configure dnsmasq as a local DNS cache. The basic configuration to work with Stubby is the following:

Restart  to apply the changes.

## Other DNS cachers
For more DNS cachers, see DNSCrypt#Local DNS cache configuration. The configurations should be similar if not identical.
