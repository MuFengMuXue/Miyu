# TLS-RPT, DANE and MTA-STS

There are two key elements in how we trust email. One is about validating the content and sender of the message which includes messsage encryption as well as DMARC (RFC 7489), DKIM (RFC 6376), SPF (RFC 7208) and ARC (RFC 8617). The other is about trust in the mail servers themselves and that is what this article addresses.

According to RFC 3207 publicly reachable email servers need to be reachable without TLS encryption. This leaves servers vulnerable to downgrade attacks to plaintext transmission. Furthermore, a certificate doesn't need to meet any requirements of validity in practice, as RFC 3207 specifies none. In order to protect against this, two technologies have emerged with more and more of the large email providers supporting them as well: DANE and MTA-STS. Either technology informs an email sender that TLS is available and plaintext should not be used for transmission. They also both validate the certificate presented in their own way. An additional protocol named TLS-RPT exists that allows for informing the operator of an email server about any problems relating to the TLS configuration and thus preventing emails not reaching their destination. This article explains how to deploy these three technologies.

Please be aware that MTA-STS and DANE should be deployed together if possible, instead of just having one of them. They are designed not to interfere with one another and the support for both varies with mail senders. As discussed later in the article, Postfix and Exim do not have MTA-STS support built-in. Any sender using either of these can only work with DANE unless some extra work is done (see below). Similarly, DANE requires DNSSEC and not every mail provider supports this extension. Currently, the largest email provider in the world, Google Mail, does not use DANE or DNSSEC and relies on MTA-STS exclusively.

When using MTA-STS a TLS certificate needs to be from a valid certification authority and be currently valid for the hostname of the email server. DANE on the other hand relies on leveraging DNSSEC to provide authenticity of the certificate. However, DANE needs a sender to use a DNSSEC validating DNS resolver and in the inbound direction, the domain to be enrolled with DNSSEC. This might not be possible with every DNS registrar. In such a situation, only MTA-STS can be used in the inbound direction, but it may still be used together with TLS-RPT. When combining both technologies, as is recommended, the certificate presented could be validated by either one, and thus needs to have a current DNS record for DANE and be signed by a trusted root CA.

The German national security standard BSI TR-03108 mandates the use of all three mechanisms in unison and this is generally considered good practice.

## Inbound
In this section, the inbound direction is discussed, that is to say the setup to enable other mail servers to send mails to your server.

## MTA-STS
Mail Transfer Agent - Strict Transport Security (MTA-STS) is a technology that allows mail servers to declare their ability to receive Transport Layer Security (TLS) connections. It also provides for specifying a policy that requests that sending SMTP servers should refuse to deliver, or not, if the receiving server does not provide a trusted server certificate.

MTA-STS works by publishing a DNS entry and hosting a policy file at .

The DNS entry is a  record published at . It is of the following form:

 v=STSv1; id=202408090200Z

The  field is the revision of MTA-STS that is deployed, this is 1 for now.  is an alphanumeric field with 1-32 characters. Every time it is increased, the MTA-STS policy is considered to have been changed. Good practice is to create a string representing the current date and updating it if any changes are made to the policy.

Finally the policy is a text file of the following kind:

There are three distinct modes:

;none: informs senders that there is no policy, and this effectively disables MTA-STS
;testing: means that the policy should be considered inactive, but TLS-RPT reports should still be made. This mode only makes sense if TLS-RPT has been configured.
;enforce: is the mode that tells senders to refuse connection to the server if no connection over TLS can be made.

 is the lifetime of the policy in seconds. This should be somewhere between several weeks, but less than 31557600 (roughly a year). The  field simply has to lists all  records for the domain.

## DANE
DANE is an abberviation of DNS-based Authentication of Named Entities. It is a security protocol that uses DNS to verify the authenticity of digital certificates associated with a domain name. It is designed as an alternative to certificate authorities (such as Letsencrypt) by utilizing the integrity of DNSSEC to ensure that a certificate indeed belongs to a domain name. While DANE is applicable to any certificate, in practice it is only used for email, or DANE SMTP. By design, the private keys and certificates can be self generated. While it is also fine to use CA provided certs its just not needed at all and they don't provide any significant benefit. One key goal of DANE is to protect against man in the middle attacks. DNSSEC, or Domain Name System Security Extensions, is what guarantees the integrity of the public key published via DNS and therefore DANE cannot be used without it.

This section is focussed on how to use DANE specifically with SMTP. How to create a DANE TLSA record with OpenSSL is a more comprehensive guide on everything relating to DANE.

The way DANE works is by leveraging DNSSEC to publish the hash of a certificate in DNS in the form of a special TLSA record. For email there are two usable options:

;DANE-TA: publishes the certificate of the certificate authority that signed the TLS certificate the email server uses. This would for example be the root certificate of Let's Encrypt, if that service is used.
;DANE-EE: works by publishing the hash of the certificate itself that is used by the email server.
It is possible to publish either the entire certificate or just the public key embedded in it. The latter option allows for reusing a key pair of a certificate and thus never having to change the DNS entry. When publishing the entire certificate, it is necessary to update the TLSA record every time a new certificate is issued by the certificate authority. This can happen quite regularly if ACME is used with for example Let's Encrypt.

A TLSA record consists out of three numeric fields and the certificate data. For example, it could look like this:

The record name is of the format . For SMTP, this would mean the port is 25 and protocol is TCP.

The numeric fields are as follows:

# The first field is the type of DANE that is being used, called the Certificate Usage Field. A value of 2 is DANE-TA, 3 means DANE-EE. The values 0 and 1 are unsuitable for email and should not be used.
# The second field, called Selector Field, indicates whether the full certificate Cert(0) or just the public key of the certificate SPKI(1) is being published.
# The third field is called Matching Type Field and indicates how the data is published. A value of 1 is an SHA2-256 hash. The other possible options are generally considered unsuitable for practical purposes and therefore are not discussed here.

Finally, the data field would be the SHA2-256 hash of the certificate or public key respectively. In order to compute this,  can be used.

In the case of DANE-EE,  would be the actual TLS certificate used by the email server. On the other hand, with DANE-TA, this would have to be any of the issuing CAs certificates.

Depending on the DNS provider, it may be possible to automate the publication of this record.  for example allows for publishing the record to the Cloudflare DNS service. Given the multitude of providers out there, it is not possible to give any specific instructions for this step.

There is also the  package for managing DNS servers that are using DNSSEC and  for creating and renewing Let's Encrypt certificates, creating and updating DANE TLSA records and for rolling the keys when certificates are renewed. For more information on these, see the documentation dns_tools docs and ssl-mgr docs.

## TLS-RPT
SMTP TLS Reporting (TLS-RPT) defined in RFC 8460 is a standard for reporting mail delivery problems related to TLS encryption failures and successful connections.

TLS-RPT works by publishing a DNS record informing senders where to send the reports about TLS functionality. There is only one type of reports, aggregate reports, which summarize how often a particular outcome, be it error or success, happened. It is formatted as an XML file for further processing.

A TLS-RPT record is a  record published at . The content has to start with a version indicator  followed by information on where the reports are to be sent. This could either be a mail address or an HTTPS service accepting POSTs. A complete record would look like this:

 indicates that aggregate reports are to be sent to this address,  specifies this should be done via mail.  would be the prefix for the HTTPS POST solution.

As the reports are XML formatted, it is recommended to process them in order to extract information. There are also numerous cloud service providers available that can receive and process these reports. There is also tls-rpt available in the   package which can generate human readable reports for both DMARC and TLS-RPT from the XML files. For more info on this please see dmarc_report Readme

## Outbound
Next, the outbound direction (i.e. when sending emails) is discussed. Unlike the inbound direction, where all three technologies are mostly independent of the mail transfer agent used, the steps for direction differ depending on which mail server is being used.

One thing in common for all MTAs is that it is necessary for sending TLS-RPT reports that all mail servers handling outgoing mail need to support the RFC 8689 extension, as TLS-RPT reports have to be sent with the header .

Additionally, a DNSSEC capable DNS resolver is required for resolving DANE and strongly recommended for MTA-STS, as it is otherwise possible to downgrade the connection. The following sections assume that DNSSEC is being used for DNS, and this is not repeated every time.

## Postfix
Postfix has long since supported DANE (as of Postfix 2.11), but MTA-STS and TLS-RPT rely on plugins.

## DANE
DANE is built-in to Postfix and requires only the following lines to be added to

## MTA-STS
In order to support MTA-STS, a plugin is needed to supply information on the TLS policy to Postfix through smtp_tls_policy_maps. There are two options available for this,  and .

Install the  and start or enable the . Then edit the  of Postfix to add the following lines

## TLS-RPT
Install . Adjust at least the following lines in  to fit your domain and organisation:

Afterwards, start or enable  and . Then, add the following lines to your Postfix :

## Exim
Exim only supports DANE and not MTA-STS or TLS-RPT. In order to activate DANE, edit  and add

 dns_dnssec_ok = 1

Furthermore, edit the  transport and add the following line to it

 hosts_try_dane = *

Further information on this topic can be found in the Exim documentation.

## Stalwart
Stalwart has all three of DANE, MTA-STS and TLS-RPT built-in already. Please see their documentation for instructions on how to enable and configure them.
