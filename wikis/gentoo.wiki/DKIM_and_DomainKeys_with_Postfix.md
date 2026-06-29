** See also**\
For more Postfix setup information, see the [Complete Virtual Mail Server](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server "Complete Virtual Mail Server") series, in which this article is included.

## Contents

-   [[1] [DKIM]](#DKIM)
    -   [[1.1] [OpenDKIM]](#OpenDKIM)
    -   [[1.2] [DNS]](#DNS)
    -   [[1.3] [Postfix]](#Postfix)
    -   [[1.4] [Testing]](#Testing)
-   [[2] [SPF]](#SPF)

## [DKIM]

### [OpenDKIM]

For more information on DKIM, see its [Wikipedia](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail "wikipedia:DomainKeys Identified Mail") page.

First, install [[[mail-filter/opendkim]](https://packages.gentoo.org/packages/mail-filter/opendkim)[]]:

`root `[`#`]`emerge --ask opendkim`

Configure the package in order to generate the domain keys:

`root `[`#`]`emerge --ask --config opendkim`

The initial configuration file needs some modification as shown below. By default, OpenDKIM configures itself using an ipv4 socket, but if OpenDKIM is run on the same server as Postfix, a unix socket may be preferable. In the following example configuration file, the mail server is under the domain `example.com` and uses `mail-1` as its key selector.

If the mail server handles more (virtual) domains and the same single key is to be used for all the virtual hosts, `Domain` can be given as a comma-delimited list of domain names. More complex configurations, like separate key per domain, are possible, but are beyond the scope of this example.

Example config:

[FILE] **`/etc/opendkim/opendkim.conf`**

    Domain                  example.com
    Selector                mail-1
    KeyFile                 /var/lib/opendkim/mail-1.private
    Socket                  inet:8891@localhost
    UMask                   0117
    ReportAddress           postmaster@example.com
    PidFile                 /var/run/opendkim/opendkim.pid
    UserID                  opendkim

With this, OpenDKIM can be started and should be functional:

`root `[`#`]`/etc/init.d/opendkim start`

Add it to the default runlevel:

`root `[`#`]`rc-update add opendkim default`

### [DNS]

Mail and spam filters will verify the signed e-mails by using the key in the DNS system and thus, access to the DNS records is required. A TXT entry needs to be added for domain that is being used to send signed e-mail.

An example of how to add this information to bind is shown here. The public key for the domain is printed in the package configuration step, but can also be found in the example dns record in [/var/lib/opendkim/mail-1.txt] for the `mail-1` key selector:

[FILE] **`/var/lib/opendkim/mail-1.txt`**

    mail-1._domainkey.example.com. IN TXT "v=DKIM1; k=rsa; p=MIGaslkjD08u98adfaSDSDaasda898932asd...afDaDSD898sDSLSKDJLSDJSLDKJLDSKJ;"

** Note**\
The private key is written to [/var/lib/opendkim/mail-1.private] and should not be shared with anyone.

A restart or reload may be required to synchronize this new record to the secondary servers and propagate it through the DNS system. Only once the record is visible in the DNS system can the key be used. Keep this in mind in case testing fails: check the domain's TXT record.

### [Postfix]

Finally, Postfix needs to be informed of the change, depending on whether the inet or unix socket is being used, this has to be added to the Postfix configuration file. In the following example, only inet is shown. (For an example based on unix sockets, see [OpenDKIM](https://wiki.gentoo.org/wiki/OpenDKIM "OpenDKIM").)

[FILE] **`/etc/postfix/main.cf`**

    # OpenDKIM mail verification
    smtpd_milters = inet:localhost:8891
    non_smtpd_milters = $smtpd_milters

Double check that the port above matches the one from the OpenDKIM configuration file.

Ensure that both OpenDKIM and Postfix re-read their configuration files:

`root `[`#`]`/etc/init.d/opendkim restart `

`root `[`#`]`/etc/init.d/postfix restart `

### [Testing]

To test the DKIM setup, a blank email can be sent to `check-auth@verifier.port25.com`. An e-mail will be sent within 30 seconds with a test report.

## [SPF]

To activate SPF (Sender Policy Framework), just add the appropriate DNS entries. SPF works by looking up the given domain (example.com), and searching for DNS TXT entries that hold SPF information. This comes as a list of IP addresses that are allowed to send mail on behalf of the domain. If the IP of the sending server is **not** found in the SPF record, this counts as a violation of the SPF policy. Thus, it is important that to add ALL servers that are allowed to send mail on behalf of the domain:

[FILE] **`/var/bind/domain.tld.hosts`**

    @ IN TXT "v=spf1 mx ~all"

** Note**\
This is an example that should work if the MX record points to every mail server that is authorized to send mail for the setup. If necessary, add further parameters **before** the \"\~all\" part. \"\~all\" **MUST** always be the last part of the SPF record.

+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| Option name           | Description                                                                                                                                                                                                                                    | Example                                           |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| a                     | This allows every IP listed in an **a** record of the domain to send mail.                                                                                                                                                                     | \"v=spf1 a \~all\"                                |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| mx                    | This allows every IP listed in an **mx** record of the domain to send mail.                                                                                                                                                                    | \"v=spf1 mx \~all\"                               |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| /24                   | This syntax expands the chosen record to the given CIDR subnet (e.g. 192.168.0.1/24). This works with a, mx, ip4 and ip6 records.                                                                                                              | \"v=spf1 a/24 \~all\"                             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ip4                   | Allows one to manually specify an IPv4 address to be included as a valid origin.                                                                                                                                                               | \"v=spf1 ip4:192.168.0.1 \~all\"                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ip6                   | Allows one to manually specify an IPv6 address to be included as a valid origin.                                                                                                                                                               | \"v=spf1 ip6:0:0:0:0:0:0:0:1 \~all\"              |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| include:example.org   | This syntax allows to include other domains. This performs a lookup of the SPF record of included domains. If the included domain does not have a SPF record, the lookup will fail.                                                            | \"v=spf1 include:example.org \~all\"              |
|                       |                                                                                                                                                                                                                                                |                                                   |
|                       |                                                                                                                                                                                                                                                | **example.org\'s SPF record:** \"v=spf1 a \~all\" |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| redirect:example.org  | This allows to redirect to other domains. The SPF record of the specified domain will be used. If the target domain has no valid SPF record, an error will be returned. **There MUST NOT be any \"all\"-statement at the end of this record.** | \"v=spf1 redirect:example.org\"                   |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| -all                  | No mail will be allowed at all. This is obviously not wanted on a mail server, so you should not use this.                                                                                                                                     | \"v=spf1 -all\"                                   |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| \~all                 | If the preceding checks return true, allow. Otherwise, deny. This is the default and should be used in 99% of all cases. Do not use any other \"all\" statements unless you know what you are doing!                                           |                                                   |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| +all                  | This allows all ip addresses to send mail. **THIS IS CONSIDERED DANGEROUS! DO NOT ENABLE UNLESS YOU KNOW WHAT YOU ARE DOING!**                                                                                                                 | \"v=spf1 +all\"                                   |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+