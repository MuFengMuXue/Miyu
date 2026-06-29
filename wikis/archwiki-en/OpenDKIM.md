# OpenDKIM

OpenDKIM is an open source implementation of the DomainKeys Identified Mail (DKIM) sender authentication system.

DKIM is supported by most common mail providers, including Yahoo, Google and Outlook.com.

Basically, DKIM digitally signs all messages from the server to verify that the message actually was sent from the domain in question and is not forged or modified.

* The sender's mail server signs outgoing email with the private key.
* When the message arrives, the receiver (or their server) reads the public key from the domain’s TXT records and verifies the signature.

This ensures the message was sent from a server whose private key matches the domain's public key.

See RFC 6376 for more information.

## Installation
Install the  package.

## Configuration
The main configuration file for the signing service is .

* Copy/move the sample configuration file  to  and change the following options:

* Socket address is the one specified in . This is what  should contain:

* To generate a secret signing key, specify the domain used to send mails and a selector which is used to refer to the key. The selector may be any value. See the RFC for details, but alpha-numeric strings should be OK:

 $ opendkim-genkey -r -s myselector -d example.com

* Sometimes mails get reformatted on their way (e.g. tab exchanged for spaces), rendering the DKIM signature invalid. To prevent trivial reformatting in header and body destroying trust, there is Canonicalization, a policy stating how strict formatting is to be conserved. Available settings are simple for no reformatting allowed and relaxed for some reformatting allowed. For details see RFC 4871 3.4. These can be set individually for header and body:

This example allows some reformatting of the header but not in the message body. Default settings for openDKIM are simple/simple.

* Other configuration options are available. Make sure to read the documentation.
* Enable/start the .

## DNS Record
Add a DNS TXT record with the selector and public key. The correct record is generated with the private key and can be found in  in the same location as the private key.

Example:

 myselector._domainkey   IN	 TXT	"v=DKIM1; p=...................."

There are several other switches available for the record (see RFC 4871 3.6.1), the most interesting might be the  which enables testing mode, signaling a checking receiver that the mail must not be treated differently from an unsigned mail, regardless of the state of the signature.

Check that the DNS record has been correctly updated:

 $ host -t TXT myselector._domainkey.example.com

You may also check that the DKIM DNS record is properly formated using one of the DKIM Key checkers available on the web.

## Postfix integration
Either add the following lines to :

To integrate DKIM and DMARC use unix sockets instead, set the UMask to give the
group write access to the socket, and add the postfix user to the opendkim
group:

Or change smtpd options in :

## Sendmail integration
Edit the  file and add the following line, after the last line starting with :

Rebuild the  file with:

 # m4 /etc/mail/sendmail.mc > /etc/mail/sendmail.cf

And then restart the .

## Multiple domains
To provide mail server service to multiple virtual domains on the same server, modify the basic configuration as below:

Provide these directives:

Create the following two files to tell opendkim where to find the correct keys. You can use the same key for all the domains or generate a key for each domain. Make changes to match your settings. Add more lines as needed.  In the following example,  and  share the same key.

An extant  file tells opendkim who may use the keys. This is referenced by the  directive in the configuration file. Opendkim ignores this list of hosts when verifying incoming mail.

Because it is also referenced by the  directive, this same list of hosts is be considered "internal," and opendkim signs their outgoing mail. Remember to change  to the correct server IP address:

Change ownership of all files to opendkim:

 # chown -R opendkim:mail /etc/opendkim

Add a DNS TXT record with your selector and public key for each of the domains.

You can now restart opendkim.

## Security
The default configuration for the OpenDKIM daemon is less than ideal from a security point of view (all those are minor security issues):

* The OpenDKIM daemon does not need to run as  at all (the configuration suggested earlier will have OpenDKIM drop  privileges by itself, but systemd can do this too and much earlier).
* If your mail daemon is on the same host as the OpenDKIM daemon, there is no need for localhost tcp sockets and unix sockets may be used instead, allowing classic user/group access controls.
* OpenDKIM is using the  folder by default whereas it could use its own folder with additional access restrictions.

The following configuration files will fix most of those issues (assuming you are using Postfix) and drop some unnecessary options in the systemd service unit:

Edit  accordingly to make Postfix listen to this unix socket:

## Troubleshooting
## Error: "milter-reject: END-OF-MESSAGE from localhost"
Most likely the Postfix milter protocol is set wrong in :

 # Postfix ≥ 2.6
 milter_protocol = 6
 # 2.3 ≤ Postfix ≤ 2.5
 milter_protocol = 2

## Authentication-Results: "dkim=neutral (bad format) header.i=@example.com"
Most likely this was caused by the DNS TXT records for given selector split into three or more resource record (RR). The authenticator, when concating the records got wrong record value.

For example, given DNS TXT record for selector "default._domainkey.example.com" with the correct, expected value

 "v=DKIM1; k=rsa; s=email; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqrXzI8BMAv3rTYU9FA4F1m2aLyT7JF8qnhTuqWibR/X55ZxoUX8fceXkRbM03tgn+1UWo5mbNN5siLPDlNOKU6fWCmkCbroPXe0vpip72zkFCtYxO4NTQY0kVaKVyFpUbFbxN3oabYTmaty3eE2yQDDAmJeZiVyEE7K7E0vnW9KpiJypFPFoft52Dqr3BTB8197gHPEMXgeP5gYkjJxVEfJZiZVco6p41JUr0CzD2dPun6pSLOO8NCkx3bWNKsL1DA7CR6qX/o2oOsd821N+0tn+8oc6x0rnhetaR0442NAGzxna4jTkUe9jwAK4aU7nKQxqNn/wOw1K2qT7uhsVMwIDAQAB".

The authenticator on the other side receive the record split into three,

{{hc
|1=$ resolver -t TXT default._domainkey.example.com
|2== options: &{sqtype:TXT sqclass:IN nameserver:udp://127.0.0.1 insecure:false qname:default._domainkey.example.com qtype:16 qclass:1}
= resolv.conf: &{Domain:localhost Search:NameServers:[127.0.0.1 NDots:1 Timeout:5 Attempts:2 OptMisc:map> Lookup default._domainkey.example.com at 127.0.0.1:53
 Header: {ID:2136 IsQuery:false Op:0 IsAA:false IsTC:false IsRD:true IsRA:true RCode:0 QDCount:1 ANCount:3 NSCount:0 ARCount:0}
> Question: &{Name:default._domainkey.example.com Type:TXT}
> Status: OK
> Answer #1:
>> Resource record: {Name:default._domainkey.example.com Type:16 Class:1 TTL:1822 rdlen:143}
>> RDATA: YkjJxVEfJZiZVco6p41JUr0CzD2dPun6pSLOO8NCkx3bWNKsL1DA7CR6qX/o2oOsd821N+0tn+8oc6x0rnhetaR0442NAGzxna4jTkUe9jwAK4aU7nKQxqNn/wOw1K2qT7uhsVMwIDAQAB
> Answer #2:
>> Resource record: {Name:default._domainkey.example.com Type:16 Class:1 TTL:1822 rdlen:253}
>> RDATA: p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqrXzI8BMAv3rTYU9FA4F1m2aLyT7JF8qnhTuqWibR/X55ZxoUX8fceXkRbM03tgn+1UWo5mbNN5siLPDlNOKU6fWCmkCbroPXe0vpip72zkFCtYxO4NTQY0kVaKVyFpUbFbxN3oabYTmaty3eE2yQDDAmJeZiVyEE7K7E0vnW9KpiJypFPFoft52Dqr3BTB8197gHPEMXgeP5g
> Answer #3:
>> Resource record: {Name:default._domainkey.example.com Type:16 Class:1 TTL:1822 rdlen:26}
>> RDATA: v=DKIM1; k=rsa; s=email;
}}

When authenticator combine the record the value its got is,

 YkjJxVEfJZiZVco6p41JUr0CzD2dPun6pSLOO8NCkx3bWNKsL1DA7CR6qX/o2oOsd821N+0tn+8oc6x0rnhetaR0442NAGzxna4jTkUe9jwAK4aU7nKQxqNn/wOw1K2qT7uhsVMwIDAQABp=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqrXzI8BMAv3rTYU9FA4F1m2aLyT7JF8qnhTuqWibR/X55ZxoUX8fceXkRbM03tgn+1UWo5mbNN5siLPDlNOKU6fWCmkCbroPXe0vpip72zkFCtYxO4NTQY0kVaKVyFpUbFbxN3oabYTmaty3eE2yQDDAmJeZiVyEE7K7E0vnW9KpiJypFPFoft52Dqr3BTB8197gHPEMXgeP5gv=DKIM1; k=rsa; s=email;

Solution: Generate keys with 1024 bits length (or less than 2048 bits) to make it fit into 255 chars on DNS TXT record.

## Notes
While you are about to fight spam and increase people's trust in your server, you might want to take a look at Sender Policy Framework, which basically means adding a DNS Record stating which servers are authorized to send email for your domain.
