# OpenSMTPD

OpenSMTPD is a free mail transfer agent, developed as part of the OpenBSD project. This article builds upon Mail server.

## Installation
Install the  package.

## Configuration
OpenSMTPD is configured in . The main configuration file is ; see  for its documentation.

Make sure to test the configuration using:

 # smtpd -n

If you get a message that says —you are ready to start or restart . If not, work on any configuration errors and try again.

## Local mail
To have local mail working, for example for cron mails, it is enough to simply start .

The default configuration of OpenSMTPD is to do local retrieval and delivery of mail to Maildir, and also relay outgoing mail. See .

## Local mail only
To do only local mail, the following is enough:

## Hybrid : local mail and relay
These two lines in  :

configure OpenSMTPD to:

* send local email locally, without going through a relay (useful for cron & at mail notifications)
* use a relay to send a mail outside of localhost

Simply replace  by your ISP mail server, or another server at your convenience.

## Relay only
To send all local emails through a relay invoke procmail:

The aliases option is used for the local user mapping, for a simplified mapping you can use virtual aliases with a catch all:

## /var/spool/mail/
OpenSMTPD 6.6.3p1 changed the default local mail configuration to use maildir in  instead of  in  to avoid security issues.

To have your local mails go to the  instead, replace  with {{ic|action "local" maildir "/var/spool/mail/%{user.username}" alias }} in .

Alternatively, set the  environment variable, that is understood by most email clients, to point to . E.g.:

 export MAIL="${HOME}/Maildir/"

## Simple OpenSMTPD/maildir configuration
## TLS
To obtain a certificate, see OpenSSL#Usage.

## Create user accounts
* Create a user account on the mail server for each desired mailbox.

 # useradd -m roger
 # useradd -m shirley

* OpenSMTPD will deliver messages to the user account's maildir in
* Multiple SMTP email addresses can be routed to a given maildir if desired.

## Craft a simple smtpd.conf setup
A working configuration can be had in as little as nine lines:

{{hc|/etc/smtpd/smtpd.conf|
pki mx.domain.example cert         "/etc/smtpd/tls/smtpd.crt"
pki mx.domain.example key          "/etc/smtpd/tls/smtpd.key"

table creds file:/etc/smtpd/creds
table vdoms file:/etc/smtpd/vdoms
table vusers file:/etc/smtpd/vusers

listen on eth0 tls pki mx.domain.example
listen on eth0 port 465 smtps pki mx.domain.example auth
listen on eth0 port 587 tls-require pki mx.domain.example auth

action "receive" maildir "/var/spool/mail/%{user.username}" virtual
action "send" relay

match from any for domain  action "receive"
match for any action "send"
}}

## Create tables
For the domain table file; simply put one domain per line:

For the user table file; list one inbound SMTP email address per line and then map it to an maildir user account name, SMTP email address, or any combination of the two on the right, separated by commas.

For the creds table file; put the user name in the 1st column and the password hash in the 2nd column

## DKIM
To sign messages with DomainKeys Identified Mail (DKIM), install .

 supports RSA and Ed25519 keys. While RFC 8463 requires for verifiers to support Ed25519, not all of them do, so it may be best to use both Ed25519 and RSA.

## Create private keys for DKIM
Create a directory for storing the keys:

 # install -dm750 -g smtpd /etc/smtpd/dkim

Create private keys using OpenSSL.

Ed25519:

 # openssl genpkey -algorithm ed25519 -out /etc/smtpd/dkim/dkim_ed25519.key

RFC 8301 mandates support for RSA keys ranging from 1024 bits to 4096 bits, so create a 4096 bit RSA key:

 # openssl genrsa -out /etc/smtpd/dkim/dkim_rsa4096.key 4096

Change the file permissions so that filter-dkimsign, which runs with the  user and group permissions, can access it:

 # chown root:smtpd /etc/smtpd/dkim/dkim_*.key
 # chmod 640 /etc/smtpd/dkim/dkim_*.key

## Prepare DNS records
DKIM uses a TXT record with the domain name , e.g. . See Wikipedia:DomainKeys Identified Mail#Verification for more details. The following example will use  for the Ed25519 key and  for RSA.

Use the following commands to get DNS record values from the public keys# openssl pkey -in /etc/smtpd/dkim/dkim_ed25519.key -pubout | openssl asn1parse -offset 12 -noout -out /dev/stdout | openssl base64 | sed '1s/^/v=DKIM1;h=sha256;k=ed25519;p=/'
 # openssl pkey -in /etc/smtpd/dkim/dkim_rsa4096.key -pubout | sed '1s/.*/v=DKIM1;h=sha256;k=rsa;p=/;:nl;${s/-----.*//;q;};N;s/\n//g;b nl;'

Update you DNS records using these values.

## Configure filter-dkimsign
Define the filters in  and add the filter chain to all  directives. Replace  with your domain name and  and  with the  selectors matching with your DNS records.

{{hc|/etc/smtpd/smtpd.conf|
...
filter "dkimsign_ed25519" proc-exec "filter-dkimsign -t -a ed25519-sha256 -d mydomain.example -s selector1 -k /etc/smtpd/dkim/dkim_ed25519.key"
filter "dkimsign_rsa4096" proc-exec "filter-dkimsign -t -a rsa-sha256 -d mydomain.example -s selector2 -k /etc/smtpd/dkim/dkim_rsa4096.key"
filter "dkimsign" chain { "dkimsign_ed25519", "dkimsign_rsa4096" }
...
listen on mydomain.example port 465 smtps filter "dkimsign"
listen on socket filter "dkimsign"
...
}}

## Troubleshooting
## Console debugging
If you are having problems with mail delivery, try stopping the  and launching the daemon manually with the "do not daemonize" and "verbose output" options. Then watch the console for errors.

 # smtpd -dv

## Subsystem tracing
Add the  flag to get real-time subsystem tracing

 # smtpd -dv -T smtp

Alternately, use the  command if the daemon is already running. The trace output will appear in the console output above as well as the journalctl output for the smtpd.service. For example:

 # smtpctl trace expand && smtpctl trace lookup

...will trace both aliases/virtual/forward expansion and user/credentials lookups.

## Manual Submission port authentication
Encode username and password in base64

 $ printf '\0%s\0%s' 'username' 'password' | base64

Connect to submission port using  command, using one of the following commands:

* To connect via port 465 (implicit TLS):
* To connect via port 587 (STARTTLS):

Enter  followed by . Paste in the base64 string from step above after  response:

 250 HELP
 EHLO test.domain.example
 250-mx.hostname.example Hello test.domain.example [127.0.0.1, pleased to meet you
 250-8BITMIME
 250-ENHANCEDSTATUSCODES
 250-SIZE 36700160
 250-DSN
 250-AUTH PLAIN LOGIN
 250 HELP
 AUTH PLAIN
 334
 dXNlcm5hbWUAdXNlcm5hbWUAcGFzc3dvcmQ=
 235 2.0.0: Authentication succeeded

## "Helo command rejected: need fully-qualified hostname"
When sending email, if you get this kind of messages, set your FQDN in the file . Otherwise, the server name is derived from the local hostname returned by , either directly if it is a fully qualified domain name, or by retrieving the associated canonical name through .

## System users authentication failure
If you are using the system users and the authentication with valid credentials fails, you have to configure PAM:
