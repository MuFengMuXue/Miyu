# Mail server

A mail server consists of multiple components. A mail transfer agent (MTA) receives and sends emails via SMTP. Received and accepted emails are then passed to a mail delivery agent (MDA), which stores the mail in a mailbox (usually in mbox or Maildir format). If you want users to be able to remotely access their mail using email clients (MUA), you need to run a POP3 and/or IMAP server.

## Software
Below is a table containing all mail servers with the features they support.

{| class="wikitable sortable"
! rowspan="2"| Name
! colspan="2"| Mail transfer agent
! colspan="2"| Mail delivery agent
! rowspan="2"| Sendmail
! rowspan="2"| Mailing list
! rowspan="2"| JMAP
! rowspan="2"| Notes
|-
! Sending !! Receiving
! POP3 !! IMAP
|-
! dma
|  ||
|  ||
|
|
|
| Does not support email domains; limited MTA receiving (see Use Google SMTP)
|-
! Exim
|  ||
|  ||
|
|
|
|
|-
! OpenSMTPD
|  ||
|  ||
|
|
|
|
|-
! Postfix
|  ||
|  ||
|
|
|
|
|-
! Courier
|  ||
|  ||
|
|
|
| Includes a web client
|-
! Cyrus IMAP
|  ||
|  ||
|
|
|
| Can be installed from
|-
! Dovecot
|  ||
|  ||
|
|
| , requested
|
|-
! UW IMAP
|  using  ||
|  ||
|   has same capabilities
|
|
| Project is abandoned
|-
! msmtp
|  ||
|  ||
|  msmtp has same capabilities
|
|
|
|-
! Sendmail
|  ||
|  ||
|
|
|
| Sendmail implementation is deprecated
|-
! sSMTP
|  ||
|  ||
|
|
|
|
|-
! fdm
|  ||
|  ||
|
|
|
| Can also fetch mail from standard input (stdin)
|-
! Procmail
|  ||
|  ||
|
|
|
| Only reads mail through standard input (stdin), upstream is unmaintained
|-
! Maildrop
|  ||
|  ||
|
|
|
| Only supports receiving emails over standard input (stdin)
|-
! Stalwart
|  ||
|  ||
|
|
|
|
|}

## Ports
{| class="wikitable"
! Purpose !! Port !! Protocol !! Encryption
|-
| Accept mail from other MTAs. || 25 || SMTP || STARTTLS
|-
|rowspan=2| Accept submissions from MUAs. || 587 || SMTP || STARTTLS
|-
| 465 || SMTPS || implicit TLS
|-
|rowspan=4| Let MUAs access mail.
| 110 || POP3 || STARTTLS
|-
| 995 || POP3S || Implicit TLS
|-
| 143 || IMAP || STARTTLS
|-
| 993 || IMAPS || implicit TLS
|}

## MX record
Hosting a mail server requires a domain name with an MX record pointing to the domain name of your mail transfer agent.
The domain name used as the value of the MX record must map to at least one address record (A, AAAA) and must not have a CNAME record to conform with RFC 2181, otherwise you may not get mail from some mail servers. Configuring DNS records is usually done from the configuration interface of your domain name registrar.

## Authentication
There are various email authentication techniques.

## Sender Policy Framework
From Wikipedia:
:Sender Policy Framework (SPF) is an email validation protocol designed to detect and block email spoofing by providing a mechanism to allow receiving mail exchangers to verify that incoming mail from a domain comes from an IP Address authorized by that domain's administrators.

To allow other mail exchangers to validate mails apparently sent from your domain, you need to set a DNS TXT record as explained in the Wikipedia article (there is also an online wizard). To validate incoming mail using SPF you need to configure your mail transfer agent to use a SPF implementation. There are several SPF implementations available: ,  and .

{|class="wikitable sortable"
|+ SPF validation support
! Courier
| , built-in
|-
! Postfix
|
|-
! Sendmail
|
|-
! Exim
|
|-
! OpenSMTPD
|
|}

The following websites let you validate your SPF record:

* SPF Record Checker
* SPF Email test

## Sender Rewriting Scheme
The Sender Rewriting Scheme (SRS) is a secure scheme to allow forwardable bounces for server-side forwarded emails without breaking the Sender Policy Framework.

For Postfix, see Postfix#Sender Rewriting Scheme.

## DKIM
DomainKeys Identified Mail (DKIM) is a domain-level email authentication method designed to detect email spoofing.

Available DKIM implementations are OpenDKIM and .

## ARC
ARC is an experimental Standard, the Authenticated Received Chain (ARC) email authentication system. It allows an intermediate mail server like a mailing list or forwarding service to sign an email's original authentication results. ARC is implemented by Google, Microsoft, ProtonMail, Fastmail, and others.

Available ARC implementations are  (as a module of rspamd), and OpenARC (standalone).

## Testing
There are several options to help you test DNS records, deliver ability, and encryption support.

## Dedicated tools
*

## Dedicated websites
There are several handy web sites that can help you testing.

* https://mxtoolbox.com/
* https://ismyemailworking.com/
* https://www.mail-tester.com/ (3 free tries only!)
* https://www.checktls.com/
* https://pingability.com/zoneinfo.jsp
* https://www.mailhardener.com/tools/

## Tips and tricks
## Removing IP addresses from emails
Most mail servers can be configured to strip users' IP addresses and user agents from outgoing mail.

## Scanning emails for viruses
See ClamAV for email antivirus scanning.

## Spam filtering
See SpamAssassin for filtering of spam emails.

## Webmail
See Roundcube and Squirrelmail for setting up of a webmail.
