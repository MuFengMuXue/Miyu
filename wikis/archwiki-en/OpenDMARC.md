# OpenDMARC

OpenDMARC is an open source implementation of the Domain-based Message Authentication, Reporting and Conformance (DMARC) specification.

DMARC is a policy for mail transfer, which is already supported by some common mail providers.
It depends on Sender Policy Framework and DKIM.
DMARC provides a policy for outgoing mail and checks incoming mails for compliance with that policy.
The policy is published via a DNS TXT record. It is explained in #DMARC Record. Validation is done in a daemon.
For more info see RFC:7489.

## Installation
Install the  package.

## Configuration
Main configuration file is

Change the following options:

Add the socket directory and make it accessible to the user the SMTP server run as (likely  or :

 # mkdir /run/opendmarc
 # chown opendmarc:postfix /run/opendmarc

To have this socket directory created automatically, create the file  with the following contents:

 D /run/opendmarc 0750 opendmarc postfix

To run the  as the SMTP server user (default is ) create :

 Group=
 Group=postfix

* Enable/start the .

## Postfix integration
Add the following lines to :

Make sure that the DMARC milter is declared after the DKIM milter.

## DMARC Record
To enable DMARC for a domain, add a new TXT record to its DNS zone.  Below is an example of a DMARC policy, processed one step after another.

First testing, no harm as (sub)policy is "none", but start to receive aggregated reports and failing reports (SPF and DKIM):
 _dmarc.example.com TXT v=DMARC1; rua=mailto:postmaster@example.com; ruf=mailto:forensic@example.com; adkim=s; fo=1

After a certain time, after analyzing these reports enable the policy, for example, for 10% of e-mail traffic.
 _dmarc.example.com TXT v=DMARC1; p=quarantine; rua=mailto:postmaster@example.com; ruf=mailto:forensic@example.com; adkim=s; fo=1; pct=10

Then slowly raise the percentage and finalize with policy 100% enabled and only failing reports:
 _dmarc.example.com TXT v=DMARC1; p=quarantine; ruf=mailto:forensic@example.com; adkim=s; fo=1

## DMARC options in detail
All fields are OPTIONAL unless "v" which is RECOMMENDED.

{| class="wikitable"
! Tag name !! Purpose !! Sample
|-
| v        || Protocol version || v=DMARC1
|-
| p        || Policy for organizational domain (default "none") || p=quarantine
|-
| sp       || Policy for subdomains (default value of "p" field) || sp=reject
|-
| rua      || Reporting URI of aggregate reports || rua=mailto:postmaster@example.com
|-
| ruf      || Reporting URI for forensic reports || ruf=mailto:forensic@example.com
|-
| adkim    || Alignment mode for DKIM (default "r") || adkim=s
|-
| aspf     || Alignment mode for SPF (default "r") || aspf=r
|-
| ri       || Reporting interval of aggregate reports (default "86400" ; often disregarded to default value) || ri=86400
|-
| fo       || Forensic report options (default "0") || fo=1
|-
| rf       || Reporting format. (default "afrf") || rf=afrf
|-
| pct      || Percentage of messages subjected to filtering (default 100) || pct=20
|}

The alignment modes for DKIM and SPF can be:
* "s" for strict: means "strict". Domains from From: shall match DKIM/SPF identifier.
* "r" for relaxed: means "relaxed". Organizational domains from From: and  DKIM/SPF shall match.
where the latter allows a subdomain in the "From" header while the former does not.

The domain policy (p) and subdomain policy (sp) might be one of:
* "none" (for monitor mode)get at
* "quarantine"
* "reject"

The forensic report options are:
* "0" to generate reports if all underlying authentication mechanisms (SPF and DKIM) fail to produce a DMARC pass result
* "1" to generate reports if any mechanisms (SPF or DKIM) fail
* "d" to generate report if the DKIM signature failed to verify
* "s" if SPF failed.

## Weblinks
* [https://dmarcian.com/dmarc-inspector/ DMARC Inspector
* IETF RFC 7489
*
