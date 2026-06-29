# Amavis

From Amavis's site:

:amavisd-new is a high-performance interface between mailer (MTA) and content checkers: virus scanners, and/or SpamAssassin. It is written in Perl for maintainability, without paying a significant price for speed. It talks to MTA via (E)SMTP or LMTP, or by using helper programs. Best with Postfix, fine with dual-sendmail setup and Exim v4, works with sendmail/milter, or with any MTA as a SMTP relay.

## Installation and setup
In this setup it is assumed that you are using ClamAV as anti-virus scanner.

* Install . You would be wise to also install optdepends such as  and  so your filters can actually see inside compressed files.
* Install .

## Basic configuration
If your hostname is not a FQDN, you must set  and  accordingly in .

You can enable ClamAV support by commenting out the following lines (do not forget to put the same  as in ):

{{hc|/etc/amavisd/amavisd.conf|
# ### http://www.clamav.net/
\&ask_daemon, ["CONTSCAN {}\n", "/var/lib/clamav/clamd.sock",
   qr/\bOK$/m, qr/\bFOUND$/m,
   qr/^.*?: (?!Infected Archive)(.*) FOUND$/m ],
# # NOTE: run clamd under the same user as amavisd - or run it under its own
# #   uid such as clamav, add user clamav to the amavis group, and then add
# # NOTE: match socket name (LocalSocket) in clamav.conf to the socket name in
# #   this entry; when running chrooted one may prefer a socket under $MYHOME.
}}

Add a comment to this line to enable anti-virus scan:

 # @bypass_virus_check_maps = (1);  # controls running of anti-virus code

After that, add the  user to the  user group to avoid permission problems.

Finally restart the services:

* restart .
* start  and possibly enable it.

Check for errors with these commands:

 # systemctl status amavisd
 # journalctl -u amavisd

## Testing
To test the new configuration just telnet to the amavisd default listening port:

 $ telnet 127.0.0.1 10024

You should see something like:

Type :

Now just type  to exit.

## Integration with Postfix
## Quick start
To configure amavis for Postfix add the following to :

In this configuration we assume that postfix and Amavis are running on the same machine (i.e. ). If that is not the case edit  and the prevous Postfix entry accordingly.

Postfix will listen to port  so that Amavis can send back checked emails to that port.

You also have to add another other configuration in your  or  sections:

 -o content_filter=amavisfeed:Using this options implies that Postfix will send emails to Amavis on port , so that these can be checked. If mail passes the control then these are sent to port , as explained before.

We can now restart  and .

To check that Postfix is listening on port  do the same operations as the port  case.

## SpamAssassin support
Install

Spamassassin is integrated in Amavis so you do not have to start . To enable support for Spamassassin comment the following line in  like this:

 # @bypass_spam_checks_maps = (1);  # controls running of anti-spam code

Edit the SpamAssassin configuration based on your needs:

Before you restart the  service, run .

## Final test
To check that everything is working as intended:

* Send a normal email.
* Send an email with an [https://www.eicar.org/download-anti-malware-testfile/ EICAR test file as attachment.
* Send an email that would result as spam.
* Check both Postfix and Amavis logs.
