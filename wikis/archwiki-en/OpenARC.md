# OpenARC

OpenARC is an open source implementation of the experimental Authenticated Received Chain (ARC) email authentication system, designed to allow an intermediate mail server like a mailing list or forwarding service to sign an email's original authentication results.

ARC is supported by most common mail providers, including Microsoft, Google, Fastmail, and Proton Mail.

## The idea
DMARC allows a sender's domain to indicate that a message is protected by SPF and/or DKIM. DMARC also indicates what a receiving server should do if a check of the message's SPF and/or DKIM does not pass (the receiving server can reject the message, for example).

However, when an email is sent through a mailing list or mail forwarder, DKIM or SPF checks might fail due to those intermediary servers making changes to the message. To prevent this failing of legitimate messages, ARC was created.

ARC re-signs the message with ARC headers. These headers allow us to see who modified the message, and what the state of authentication was before the modifications by an intermediary server.

After changes to the message by an intermediary server, SPF and/or DKIM checks might fail (see above). However, if there is a valid ARC chain, then a receiving server can still pass the message, if it trusts the intermediary server(s), as the ARC chain will allow the receiving mail server to extract the (old) SPF and DKIM results, which will pass the check.

See RFC 8617 for more information.

## Installation
Install the  package.

## Configuration
The main configuration file for the signing service is .

* Create an empty configuration file , or copy/move the sample configuration file  to  and change or add the following options (See  for details):

* Socket address is the one specified in . This is what  should contain:

* To generate a secret signing key using OpenDKIM's opendkim-genkey, specify the domain used to send mails and a selector which is used to refer to the key. The selector may be any value. See the RFC for details, but alpha-numeric strings should be OK:

 # opendkim-genkey -D /etc/openarc/keys -r -s myselector -d example.com
 # chown -R openarc /etc/openarc/keys

Note that opendkim-keygen also generates a DNS zone file for your domain.

* Alternatively, you can also generate keys with just OpenSSL. Specify your domain instead of {YOURDOMAIN.COM}, and choose a 2048-bit key if you prefer.

First, create the private key:

 # openssl genrsa -out /etc/openarc/keys/{YOURDOMAIN.COM}.key 1024

Then, extract the public key from the private key you just generated:

 # openssl rsa -in /etc/openarc/keys/{YOURDOMAIN.COM}.key -pubout -out /etc/openarc/keys/{YOURDOMAIN.COM}.pub

Change the owner of the key files and restrict permissions:

 # chown -R openarc /etc/openarc/keys
 # chmod -R 600 /etc/openarc/keys/{yourkey}.key

Your Public key (for DNS):

 # cat /etc/openarc/keys/{YOURDOMAIN.COM}.pub

Now either create a DNS txt file for your locally hosted DNS in the following format:

 {YOURSELECTOR}._domainkey.{YOURDOMAIN.COM}.	IN TXT "v=DKIM1;k=rsa;p={YOUR-PUBLIC-KEY};"

Or, copy the Public key and paste it into your DNS txt file with the following format:
 ._domainkey..
 {YOUR-PUBLIC-KEY}

* If you want logging to syslog, enable it as follows:

* To tell OpenARC which headers to sign, configure them for example as follows:

* The PeerList contains a list of IP addresses, CIDR blocks, hostnames, or domain names, whose mail should be neither signed, nor verified by this filter. This can be used to exclude your local mail for example. This file needs to be created if it does not yet exist.

* Other configuration options are available. Make sure to read the documentation.
* Enable/start the .

## Postfix integration
To integrate ARC using unix sockets, add the postfix user to the openarc group and edit the OpenARC and Postfix configuration files as follows:

## Security
The default configuration for the OpenARC daemon is less than ideal from a security point of view (all those are minor security issues):

* The OpenARC daemon does not need to run as  at all (the configuration suggested earlier will have OpenARC drop  privileges by itself, but systemd can do this too and much earlier).
* If your mail daemon is on the same host as the OpenARC daemon, there is no need for localhost tcp sockets, and unix sockets may be used instead, allowing classic user/group access controls.
* OpenARC is using the  folder by default whereas it could use its own folder with additional access restrictions.

The following configuration files will fix most of those issues (assuming you are using Postfix) and drop some unnecessary options in the systemd service unit. First, create a missing directory:

 # mkdir /var/lib/openarc

Then:

Edit  accordingly to make Postfix listen to this unix socket:
