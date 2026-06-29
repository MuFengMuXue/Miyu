# Dkfilter

Dkfilter is a DomainKeys filter for Postfix.

## What is it?
It is digital email signing/verification technology, which included into RFCs and already supported by many mail servers. (For example yahoo, google, etc).

## How it works?
Sender signs email with private key.

Receiver gets signed email, request public key from DNS and verify it.

So you can check who actualy sent this email.

See RFC 4870 for more information.

## Installation
Install the  package.

By default, you should add dkfilter user and group. If you do not want to do this, edit /etc/conf.d/dkfilter and change DKFILTER_USER and DKFILTER_GROUP.

## Generic configuration
* Generate key:

 $ openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out private.key
 $ openssl rsa -in private.key -pubout -out public.key

* Adjust .
* Add DNS record with your selector (see  in , you may choose random name) and key:

 server1._domainkey IN TXT "k=rsa; p=MHwwDQYJK ... OprwIDAQAB; t=y"

* Start/enable  and .

## Postfix integration
## Inbound filter
Inbound filter gets connection from port 10025 and output filtered data to port 10026. (Inbound filter does not remove any data, it just adds verification result into mail)

Add following into /etc/postfix/master.cf:

## Outbound filter
Outbound filter gets connection from port 10027 and output signed data to port 10028.

Add following into /etc/postfix/master.cf:
