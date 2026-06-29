# Sendmail

Sendmail is the classic mail transfer agent from the Unix world. This article builds upon Mail server.

The goal of this article is to setup Sendmail for local user accounts, without using MySQL or other databases, and also allowing the creation of mail-only accounts.

## Installation
Install the ,  and  packages.

## Adding users
Create a Linux user for each user that wants to receive email at username@your-domain.com. To add mail-only accounts, that is, users who can get email, but cannot have shell access or login on X, you can add them like this:
 # useradd -m -s /usr/bin/nologin username

## Configuration
## Obtain TLS certificate
To obtain a certificate, see OpenSSL#Usage.

## sendmail.cf
Create the file .
You can read all the options for configuring sendmail on the file .

Here is an example using auth over TLS. The example has comments explaing how it works. The comments start with .

Then process it with
 # m4 /etc/mail/sendmail.mc > /etc/mail/sendmail.cf

## local-host-names
Put your domains on the  file:

Make sure the domains are also resolved by your  file.

## access.db
Create the file   and put there the base addresses where you want to be able to relay mail. Lets suppose you have a vpn on , and you want to relay mails from any ip in that range:

Then process it with
 # makemap hash /etc/mail/access.db < /etc/mail/access

## aliases.db
Edit the file   and  uncomment the line  and change it to be like this:

You can add aliases for your usernames there, like:

Then process it with

 # newaliases

## virtusertable.db
Create your  file and put there aliases that includes domains (useful if your server is hosting several domains)

Then process it with
 # makemap hash /etc/mail/virtusertable.db < /etc/mail/virtusertable

## Start on boot
Enable/start the following units.

*
*
*

## SASL authentication
Add a user to the SASL database for SMTP authentication.
 # saslpasswd2 -c your-username

## Tips and tricks
## Forward all the mail of one domain to certain user
To forward all mail addressed to any user in the my-other.tld domain to your-username@your-domain.com:

Do not forget to process it again with

 # makemap hash /etc/mail/virtusertable.db < /etc/mail/virtusertable
