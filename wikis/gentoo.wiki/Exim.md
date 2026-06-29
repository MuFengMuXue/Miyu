**Resources**

[[]][Home](http://www.exim.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Exim "wikipedia:Exim")

**Exim** is a powerful and the most popular [Mail Transfer Agent](https://wiki.gentoo.org/wiki/Category:Mail_Transfer_Agents "Category:Mail Transfer Agents") (MTA). It\'s reported to have a 57% market share^[\[1\]](#cite_note-MX_Survey_of_March_1st.2C_2019_on_SecuritySpace-1)^. Also, Exim is the default MTA for Debian / Ubuntu.

## Contents

-   [[1] [Pre-installation]](#Pre-installation)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Complete mailserver]](#Complete_mailserver)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Modern mail security (SPF/DKIM/DMARC)]](#Modern_mail_security_.28SPF.2FDKIM.2FDMARC.29)
    -   [[3.2] [Example for SPF, DKIM with SQLite and Maildir]](#Example_for_SPF.2C_DKIM_with_SQLite_and_Maildir)
    -   [[3.3] [Example for SpamAssasin, ClamAV with PostgreSQL and Maildir]](#Example_for_SpamAssasin.2C_ClamAV_with_PostgreSQL_and_Maildir)
-   [[4] [Testing Exim]](#Testing_Exim)
-   [[5] [References]](#References)

## [Pre-installation]

As only one MTA can be installed at the same time on a system, it might be required to remove an installed MTA. The package manager will report a block when another MTA is still installed. This block can resolved by manually deselecting the old mail server. For example, preparing to remove [[[mail-mta/ssmtp]](https://packages.gentoo.org/packages/mail-mta/ssmtp)[]] (which might have been installed as the default when a program requested a mail server to be installed) with this command:

`root `[`#`]`emerge --deselect mail-mta/ssmtp`

## [Installation]

### [USE flags]

### [USE flags for] [mail-mta/exim](https://packages.gentoo.org/packages/mail-mta/exim) [[]] [A highly configurable, drop-in replacement for sendmail]

  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+dane`](https://packages.gentoo.org/useflags/+dane)                 Adds support for DNS-based Authentication of Named Entities
  [`+dkim`](https://packages.gentoo.org/useflags/+dkim)                 Adds support for DomainKeys Identified Mail (DKIM)
  [`+dnsdb`](https://packages.gentoo.org/useflags/+dnsdb)               Adds support for a DNS search for a record whose domain name is the supplied query
  [`+prdr`](https://packages.gentoo.org/useflags/+prdr)                 Adds support for Per-Recipient Data Response
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)                   Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`+tdb`](https://packages.gentoo.org/useflags/+tdb)                   Use sys-libs/tdb for internal database storage (such as hints database)
  [`+tpda`](https://packages.gentoo.org/useflags/+tpda)                 Adds support for Transport Post-Delivery Actions
  [`arc`](https://packages.gentoo.org/useflags/arc)                     Adds support for Authenticated Receive Chain (ARC)
  [`berkdb`](https://packages.gentoo.org/useflags/berkdb)               Add support for sys-libs/db (Berkeley DB)
  [`dcc`](https://packages.gentoo.org/useflags/dcc)                     Adds support for Distributed Checksum Clearinghouse (DCC)
  [`dlfunc`](https://packages.gentoo.org/useflags/dlfunc)               Install local_scan.h header to compile separate dlfunc libraries
  [`dmarc`](https://packages.gentoo.org/useflags/dmarc)                 Adds support for DMARC
  [`doc`](https://packages.gentoo.org/useflags/doc)                     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`dovecot-sasl`](https://packages.gentoo.org/useflags/dovecot-sasl)   Adds support for Dovecot\'s authentication
  [`dsn`](https://packages.gentoo.org/useflags/dsn)                     Adds support for Delivery Status Notifications (DSN)
  [`gdbm`](https://packages.gentoo.org/useflags/gdbm)                   Add support for sys-libs/gdbm (GNU database libraries)
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)               Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`gsasl`](https://packages.gentoo.org/useflags/gsasl)                 Adds support for GNU SASL authentiction
  [`idn`](https://packages.gentoo.org/useflags/idn)                     Enable support for Internationalized Domain Names
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)                   Add support for IP version 6
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                   Add LDAP support (Lightweight Directory Access Protocol)
  [`lmtp`](https://packages.gentoo.org/useflags/lmtp)                   Adds support for lmtp
  [`maildir`](https://packages.gentoo.org/useflags/maildir)             Add support for maildir (\~/.maildir) style mail spools
  [`mbx`](https://packages.gentoo.org/useflags/mbx)                     Adds support for UW\'s mbx format
  [`mysql`](https://packages.gentoo.org/useflags/mysql)                 Add mySQL Database support
  [`nis`](https://packages.gentoo.org/useflags/nis)                     Support for NIS/YP services
  [`pam`](https://packages.gentoo.org/useflags/pam)                     Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`perl`](https://packages.gentoo.org/useflags/perl)                   Add optional support/bindings for the Perl language
  [`pkcs11`](https://packages.gentoo.org/useflags/pkcs11)               Require pkcs11 support in net-libs/gnutls with USE=gnutls
  [`postgres`](https://packages.gentoo.org/useflags/postgres)           Add support for the postgresql database
  [`proxy`](https://packages.gentoo.org/useflags/proxy)                 Add support for being behind a proxy, such as HAProxy
  [`radius`](https://packages.gentoo.org/useflags/radius)               Add support for RADIUS authentication
  [`redis`](https://packages.gentoo.org/useflags/redis)                 Adds support for querying dev-db/redis
  [`sasl`](https://packages.gentoo.org/useflags/sasl)                   Add support for the Simple Authentication and Security Layer
  [`selinux`](https://packages.gentoo.org/useflags/selinux)             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`socks5`](https://packages.gentoo.org/useflags/socks5)               Add support for the socks5 proxy
  [`spf`](https://packages.gentoo.org/useflags/spf)                     Adds support for Sender Policy Framework
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)               Add support for sqlite - embedded sql database
  [`srs`](https://packages.gentoo.org/useflags/srs)                     Adds support for Sender Rewriting Scheme
  [`syslog`](https://packages.gentoo.org/useflags/syslog)               Enable support for syslog
  [`tcpd`](https://packages.gentoo.org/useflags/tcpd)                   Add support for TCP wrappers
  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 15:44] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

For a typical install, install [[[mail-mta/exim]](https://packages.gentoo.org/packages/mail-mta/exim)[]] with the following use flags:

[FILE] **`/etc/portage/package.use/exim`**

    mail-mta/exim dkim exiscan-acl maildir prdr spf ssl syslog

To use dovecot as your POP/IMAP server and want to make exim use dovecot\'s authentication services, add a use flag for dovecot-sasl.

[FILE] **`/etc/portage/package.use/exim`**

    mail-mta/exim dovecot-sasl dkim exiscan-acl maildir prdr spf ssl syslog

To use a database to manage what mailboxes and what aliases exist, add a use flag for the database to use, e.g. postgres, sqlite, etc.

[FILE] **`/etc/portage/package.use/exim`**

    mail-mta/exim dkim exiscan-acl maildir prdr spf sqlite ssl syslog

### [Emerge]

Finally, install exim with:

`root `[`#`]`emerge --ask mail-mta/exim`

### [Complete mailserver]

For a complete mailserver, you\'ll typically also want to install a POP/IMAP server, such as [dovecot](https://wiki.gentoo.org/wiki/Simple_mail_server_with_webmail#dovecot_IMAP.2C_POP_.26_SASL "Simple mail server with webmail") or [courier-imap](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Courier-IMAP_to_Database "Complete Virtual Mail Server/Courier-IMAP to Database"). These so-called [MDAs](https://wiki.gentoo.org/index.php?title=Mail_Delivery_Agent&action=edit&redlink=1 "Mail Delivery Agent (page does not exist)") tightly integrate with Exim (your MTA) and possibly your database.

Also, you might want to install a webmail server, such as [Squirrelmail](https://wiki.gentoo.org/wiki/Simple_mail_server_with_webmail#SquirrelMail_webmail "Simple mail server with webmail") or [Roundcube](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Web_Access "Complete Virtual Mail Server/Web Access"), which will also integrate with your MTA, MDA and database.

## [Configuration]

The exim ebuild creates a small number of configuration files in /etc/exim, namelyː auth_conf.sub exim.conf exim.conf.exiscan-acl and system_filter.exim. Of these files, the main configuration file is /etc/exim/exim.conf.

This exim.conf file can include several sectionsː

-   General options, setting up parameters such as hostname and domains, hooking up ACL\'s, SSL/TLS settings, ports and logging.
-   ACL, where specific rules can be written for different phases of the SMTP protocol for incoming e-mail.
-   Routers, which determine based on the addresses of the e-mail to which exim-transport the message should be routed
-   Transports, for actually delivering e-mails (either remotely, or locally)
-   Retry, because we might not want to give up after the first attempt
-   Rewrite, in case we want to touch content of the e-mail or its headers
-   Authenticators, as we only want to send e-mails out into the world if it was submitted by someone we trust
-   Local_scan, in case \*really\* specific scanning hook-ups are needed

### [][Modern mail security (SPF/DKIM/DMARC)]

With the rise of security in computing, mail security is also improving. After a number of solutions have been tried, the mailserver community seems to have settled on the combination of SPF, DKIM and DMARC.

SPF:

-   SPF focuses on Envelope-From (aka Return-Path, MAIL FROM, Bounce address)
-   SPF authenticates the IP of the sending server against SPF sending server policy
-   SPF does not require alignment between Header-From and Envelope-From
-   SPF does not survive forwarding and indirect mail-flows
-   SPF does not tell the receiving server what it should do with messages that fail SPF

\
DKIM:

-   DKIM focuses on asymmetrical crypto and control over DNS records
-   DKIM crypto-proves the d= domain signed the e-mail
-   DKIM crypto-proves the integrity of headers and/or body
-   DKIM does not require alignment between Header-From and d= domain
-   DKIM may survive forwarding and indirect mail-flows depending on what parts were signed
-   DKIM does not tell the receiving server what it should do with messages that fail DKIM

\
DMARC:

-   DMARC requires alignment between Header-From and Envelope-From used by SPF and/or d= domain field in DKIM signature
-   DMARC ignores the difference in SPF between hard fail (-all) and soft fail (\~all) and treats both as fail
-   DMARC allows defining a policy that receivers can follow for messages that fail SPF and/or DKIM tests
-   DMARC allows reporting mailboxes to be defined

### [][Example for SPF, DKIM with SQLite and Maildir]

This configuration enables SPF and DKIM, but only adds warning headers, it doesn\'t quarantine or reject e-mails. Further it uses SQLite for managing what mailboxes and aliases exist, and stores mails in a special directory in Maildir format.

[FILE] **`/etc/exim/exim.conf`**

    # Explicitly set our HELO name
    primary_hostname = mailserver.example.com

    # Define domain lists
    domainlist local_domains = example.com : crossexample.net : @
    hostlist   relay_from_hosts = 127.0.0.1 : localhost

    # Connect access control lists to their hooks
    acl_smtp_connect = acl_check_connect
    acl_smtp_helo = acl_check_helo
    acl_smtp_mail = acl_check_mail_from
    acl_smtp_dkim = acl_check_dkim
    acl_smtp_rcpt = acl_check_rcpt
    acl_smtp_data = acl_check_data

    # Allow any client to use TLS
    tls_advertise_hosts = *

    # Specify the location of the Exim server's TLS certificate and private key
    tls_certificate = /etc/ssl/mailserver.example.com-signed.crt
    tls_privatekey = /etc/ssl/private/mailserver.example.com.key

    # Set modern ciphers (assuming gentoo default of exim with openssl)
    tls_require_ciphers = TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-256-GCM-SHA384:TLS13-AES-128-GCM-SHA256:EECDH+CHACHA20:EECDH+AESGCM:EECDH+AES
    tls_dhparam = /etc/ssl/private/dhparam.pem
    openssl_options = +no_sslv2 +no_sslv3

    # Support acting as smtp.example.com server for users outside our network
    daemon_smtp_ports = 25 : 587
    # tls_on_connect_ports = 465 (required for Microsoft clients)

    # Add our domain to 'unqualified addresses', instead of our server name
    qualify_domain = example.com

    # Perform rDNS lookups for incoming connections, so we can confirm their HELO
    host_lookup = *

    # Advertise PRDR to accept/reject multi-recipient mails per-user
    prdr_enable = true

    # Specify what should be logged.
    log_selector = +smtp_protocol_error +smtp_syntax_error \
            +tls_certificate_verified

    # Prevent clogging the queue when mail delivery and return-to-sender both fail
    ignore_bounce_errors_after = 2d
    timeout_frozen_after = 7d

    # If we don't set the following option, Exim will complain mildly
    keep_environment =

    ###################
    # ACL CONFIGURATION
    ###################
    begin acl

    # Work through the SMTP protocol

    # Trigger on an incoming connection
    acl_check_connect:

      # Record the current timestamp, in order to delay crappy senders
      warn
              set acl_m0  = $tod_epoch

      # Warn if reverse DNS lookup failed. Note: later we compare rDNS with HELO
      warn
              !verify     = reverse_host_lookup
              set acl_c1  = X-DNS-Warning: Couldn't lookup reverse DNS for $

      # Set up for finalisation: write to log
      warn
              condition   = $ }
              logwrite    = $acl_c1

      # On error: accept but stall (good actors tend to be patient)
      accept
              set acl_m0  = $ } }
              delay       = $ }s

    # Trigger on the HELO/EHLO of incoming connections.
    acl_check_helo:

      # Record the current timestamp, in order to delay crappy senders
      warn
              set acl_m0  = $tod_epoch

      # Warn if sender did not provide a HELO/EHLO greeting
      warn
              condition   = $ }
              set acl_c2  = X-HELO-Warning: Remote host $sender_host_address \
                            did not present HELO/EHLO greeting.

      # Warn if sender greeted with an IP address (technically correct, but crappy)
      warn
              condition   = $ }
              condition   = $ }
              set acl_c2  = X-HELO-Warning: Remote host $sender_host_address \
                            used IP address instead of hostname in HELO/EHLO

      # Warn if sender pretended to be us (they may think that would trick us)
      warn
              condition   = $ }
              condition   = $\
                             }
              set acl_c2  = X-HELO-Warning: Remote host $sender_host_address \
                            used our name in HELO/EHLO but it is not defined in \
                            our +local_domains

      # Warn if HELO verification fails, e.g. rDNS of IP != HELO domain
      warn
              condition   = $ }
              !verify     = helo
              set acl_c2  = X-HELO-Warning: Remote host $\
                                 }\
                            incorrectly presented itself as $sender_helo_name

      # Set up for finalisation: write to log
      warn
              condition   = $ }
              logwrite    = $acl_c2

      # On error: accept but stall (good actors tend to be patient)
      accept
              set acl_m0  = $ } }
              delay       = $ }s

    # Trigger on MAIL FROM: command. Here we perform SPF checks.
    acl_check_mail_from:

      # Skip SPF checks for all authenticated connections (probably MUAs)
      accept
              authenticated = *

      # Record the current timestamp, in order to delay crappy senders
      warn
              set acl_m0  = $tod_epoch

      # Query if we can find an SPF policy for the sending domain
      warn
              spf         = none:temperror:permerror
              set acl_c3  = X-SPF-Warning: can't find SPF policy for \
                            $sender_address_domain

      # Query if the sending domain has set a useful SPF policy
      warn
              condition   = $ }
              condition   = $ } } }
              set acl_c3  = X-SPF-Warning: $sender_address_domain allows +all in SPF policy

      # Query the SPF policy whether sender was authorized to deliver this message
      # Note: fail = '-all', softfail = '~all', neutral = '?all'
      warn
              spf         = fail:softfail:neutral
              condition   = $ }
              set acl_c3  = X-SPF-Warning: $sender_host_address is not allowed to \
                            send mail for $sender_address_domain

      # Add a SPF-Received: line to the message header (regardless of SPF status)
      warn
              add_header  = $spf_received

      # Set up for finalisation: add all headers and write to log
      warn
              condition   = $ }
              logwrite    = $acl_c3
              add_header  = $acl_c1
              add_header  = $acl_c2
              add_header  = $acl_c3

      # On error: accept but stall (good actors tend to be patient)
      accept
              set acl_m0  = $ }  } }
              delay       = $ }s

    # This access control list is used to process DKIM status.
    acl_check_dkim:

      # Skip DKIM checks for all authenticated connections (probably MUAs)
      accept
              authenticated = *

      # Record the current timestamp, in order to delay crappy senders
      warn
              set acl_m0  = $tod_epoch

      # Warn no DKIM
      warn
              dkim_status = none
              set acl_c4  = X-DKIM-Warning: No signature found

      # RFC 8301 requires 'permanently failed evaluation' for DKIM signatures signed with 'historic algorithms (currently, rsa-sha1)'
      # @SEE: https://www.exim.org/exim-html-current/doc/html/spec_html/ch-dkim_and_spf.html
      warn
              condition              = $ }
              condition              = $ }
              condition              = $ } }
              condition              = $ } \
                                         } } }
              set acl_c4             = X-DKIM-Warning: forced DKIM failure (weak hash or short key)
              set dkim_verify_status = fail
              set dkim_verify_reason = hash too weak or key too short

      # RFC6376 requires that verification fail if the From: header is not included in the signature
      # @SEE: https://www.exim.org/exim-html-current/doc/html/spec_html/ch-dkim_and_spf.html
      warn
              condition   = $ }
              condition   = $ }
              set acl_c4  = X-DKIM-Warning: From: header not included in the \
                            signature, this defies the purpose of DKIM

      # Warn invalid or failed signatures
      warn
              condition   = $ }
              dkim_status = fail:invalid
              set acl_c4  = X-DKIM-Warning: verifying signature of $dkim_cur_signer \
                            failed for $sender_address because $dkim_verify_reason

      # Add a DKIM-Received: line to the message header (regardless of DKIM status)
      warn
              add_header  = Received-DKIM: $dkim_verify_status $ }

      # Set up for finalisation: add header and write to log
      warn
              condition   = $ }
              add_header  = $acl_c4
              logwrite    = $acl_c4

      # On error: accept but stall (good actors tend to be patient)
      accept
              set acl_m0  = $ } }
              delay       = $ }s

    # Trigger on RCPT of incoming message.
    acl_check_rcpt:

      # Test empty sending host field to accept local SMTP (i.e. not over network)
      accept
              hosts         = :
              control       = dkim_disable_verify

      # Strange non-alphanumeric characters may indicate a user trying to trick us;
      # 1/2: incoming mail address may not begin with . or contain @ % ! / or |
      deny
              message    = Restricted characters in address
              domains    = +local_domains
              local_parts   = ^[.] : ^.*[@%!/|]

      # 2/2: outgoing mail address may not begin with . / or | and neither may it
      #      contain @ % ! or the sequence /../ (this is slightly looser than 1/2)
      deny
              message    = Restricted characters in address
              domains    = !+local_domains
              local_parts   = ^[./|] : ^.*[@%!] : ^.*/\\.\\./

      # Deny unless we have a route to deliver mail back to the sender address
      require
              verify        = sender

      # Skip other checks for all authenticated connections (probably MUAs), set
      # submission mode and assume MUAs send address in From: that includes @domain
      accept
              authenticated = *
              control    = submission/sender_retain
              control    = dkim_disable_verify
              add_header    = X-Authenticated-Sender: $
              set acl_c_authenticated = 1

      # Insist that a HELO/EHLO was accepted.
      require
              message    = nice hosts say HELO first
              condition     = $

      # Insist that any other recipient address is in one of our local domains
      require
              message       = relay not permitted
              domains       = +local_domains

      # Ensure we can deliver the message before we accept it
      require
              verify        = recipient

      # If it got through to this point, accept it without further checks
      accept

    # Message has been received, now we can check its contents (headers, body, etc)
    # Note: here we can invoke external virus or spam scanners, if available
    acl_check_data:

      # Deny if the message contains an overlong line, as per the standards
      deny
              message       = maximum allowed line length is 998 octets, \
                              got $max_received_linelength
              condition     = $ }

      # Deny if the headers contain badly-formed addresses.
      deny
              !verify       = header_syntax
              message       = header syntax
              logwrite      = header syntax ($acl_verify_message)

      # Deny if the message contains a virus. Before enabling this check, you
      # must install a virus scanner and set the av_scanner option above.
      # deny
      #         malware     = *
      #         message     = This message contains a virus ($malware_name).

      # Add headers to a message if it is judged to be spam. Before enabling this,
      # you must install SpamAssassin. You may also need to set the spamd_address
      # option above.
      # warn
      #         spam        = nobody
      #         add_header  = X-Spam_score: $spam_score\n\
      #                       X-Spam_score_int: $spam_score_int\n\
      #                       X-Spam_bar: $spam_bar\n\
      #                       X-Spam_report: $spam_report

      # Accept the message.
      accept
                logwrite    = Received message from $sender_address_domain

    #########
    # ROUTERS
    #########

    begin routers

    # ---
    # Routers that handle addresses in remote domains (! +local_domains).
    # ---

    # Route addresses by doing a DNS lookup on the domain name.
    # Domains that resolve to 0.0.0.0 or to loopback (127.0.0.0/8) are treated as
    # if they have no DNS entry: lookup fails, 'no_more' intervenes and the
    # address is handled as unrouteable.
    dnslookup:
      driver = dnslookup
      driver = dnslookup
      domains = ! +local_domains
      transport = remote_smtp
      ignore_target_hosts = 0.0.0.0 : 127.0.0.0/8
      no_more

    # ---
    # Routers that handle addresses in local domains ("domainlist local_domains").
    # ---
    # If none of these routers picks up the message, "Unknown user" is returned to
    # sender.

    # This section is heavily dependent on your setup, especially how you wish to
    # manage the 'local_parts', i.e. what aliases exist, what mailboxes exist and
    # where mailboxes are stored.
    # Traditionally answers to these questions were files that have existed since
    # dawn of Unix tradition, but nowadays it's typical to put this in a database.
    # If you already administer one or more databases, you can use it here as well.
    # But if you don't, you can consider sqlite or flat files, so you don't need to
    # learn about database-upgrades, etc. This example uses an sqlite database.

    # If recepient is an alias, redirect it to the appropriate mailbox
    aliases:
      debug_print = "Redir: virtual_aliases for $@$"
      driver = redirect
      domains = +local_domains
      local_part_suffix = -*
      local_part_suffix_optional
    # Change the following two lines to reflect your database setup
    #  condition = $ }' AND alias='$'; }  }
    #  data = /path/to/mailboxes/$/$' AND alias='$'; } }
      file_transport = redir_virtual_directory
      directory_transport = redir_virtual_directory

    # If recepient is a mailbox on its own, deliver the message.
    # This router treats local parts with suffixes introduced by "-" as if the
    # suffixes did not exist. E.g. xxxx-foo@your.domain will be treated
    # in the same way as xxxx@your.domain by this router.
    users:
      debug_print = "Acc: userid for $@$"
      driver = accept
      no_check_local_user
      domains = +local_domains
      local_part_suffix = -*
      local_part_suffix_optional
    # Change the following line to reflect your database setup
    #  condition = $ }' AND userid='$'; }  }
      transport = accept_virtual_directory
      cannot_route_message = Unknown user

    ############
    # TRANSPORTS
    ############
    # Transports can only be called by a router picking up the message

    begin transports

    # ---
    # Transport for delivering over SMTP (e.g. outgoing e-mail)
    # ---

    # Refuse messages with over-long lines as per standard
    # Note: the use of message_size_limit is a red herring.
    remote_smtp:
      driver = smtp
      message_size_limit = $  }
      dkim_domain = $
      dkim_selector = dkim
      dkim_private_key = /etc/ssl/private/dkim-mailserver.example.com.key
      dkim_canon=relaxed

    # ---
    # Transport for delivering to local mailbox
    # ---

    # This transport is used for local delivery to user mailboxes w/ Maildir
    accept_virtual_directory:
      driver = appendfile
      maildir_format
      user = vmail
      group = vmail
      mode = 0600
      directory = /path/to/mailboxes/$/$/
      delivery_date_add

    redir_virtual_directory:
      driver = appendfile
      maildir_format
      user = vmail
      group = vmail
      mode = 0600

    #######
    # RETRY
    #######

    begin retry

    # Because we're not going to give up after our first attempt
    # Address or Domain    Error       Retries
      *                    *           F,2h,15m; G,16h,1h,1.5; F,4d,6h

    ################
    # AUTHENTICATION
    ################

    begin authenticators

    # Authentication can be finicky to set up, but will also be needed by the
    # POP/IMAP server you will probably also be setting up. This example makes use
    # of dovecot to handle authentication for our SMTP clients.
    dovecot_login:
      driver = dovecot
      public_name = LOGIN
      server_socket = /var/run/dovecot/auth-client
      server_set_id = $auth1

    dovecot_plain:
      driver = dovecot
      public_name = PLAIN
      server_socket = /var/run/dovecot/auth-client
      server_set_id = $auth1

### [][Example for SpamAssasin, ClamAV with PostgreSQL and Maildir]

This possibly outdated configuration uses SpamAssasin to filter spam, ClamAV to detect if e-mails contain virusses, PostgreSQL for managing what mailboxes exist, and stores mails in users\' home directories in Maildir format.

[FILE] **`/etc/exim/exim.conf`**

    # Domain list configuration, each domain must be separated by ":"
    domainlist local_domains = example.com:otherdomain.com:anotherdomain.com:@

    # On initial configuration we do not want to relay any other domain
    domainlist relay_to_domains =
    hostlist   relay_from_hosts = 127.0.0.1 : ::::1/128

    # ACL we want to be checked
    local_from_check = true

    acl_smtp_mail = acl_check_mail
    acl_smtp_rcpt = acl_check_rcpt
    acl_smtp_connect = acl_check_host
    acl_smtp_data = acl_check_data
    acl_smtp_helo = acl_check_helo

    # Postgresql Database connection
    hide pgsql_servers = localhost/db_maik/dbusername/dbpassword:

    # Set maximum parallel remote smtp
    remote_max_parallel = 24

    # Define clamav configuration
    av_scanner = clamd:127.0.0.1 3310

    # Spam configuration
    spamd_address = 127.0.0.1 783

    # Allow use of TLS, we can have files here.
    tls_advertise_hosts = *

    # Set the key and cert to use
    tls_certificate = /etc/ssl/mail/mycert.pem
    tls_privatekey = /etc/ssl/mail/myprivate.key

    # Our default qualify domain
    qualify_domain = example.com

    begin acl
    # Force authentication for send email
    acl_check_mail:
      warn  set acl_c_auth_deny = no
            set acl_c_deny_msg = Checking User

      accept sender_domains = !+local_domains:

      deny  sender_domains = +local_domains
            !authenticated = *
            set acl_c_auth_deny = yes
            set acl_c_deny_msg  = Authentication Needed for Send Mail
            message = Authentication Needed for Send Mail

      accept
    acl_check_rcpt:
      deny  condition = $acl_c_auth_deny
            message = $acl_c_deny_msg

      deny  hosts = :

      deny    message       = Restricted characters in address
              domains       = +local_domains
              local_parts   = ^[.] : ^.*[@%!/\|]

      deny    message       = Restricted characters in address
              domains       = !+local_domains
              local_parts   = ^[./|] : ^.*[@%!] : ^.*/\\.\\./

      accept  local_parts   = postmaster
              domains       = +local_domains

      require verify        = sender

      accept  authenticated = *
              control       = submission/sender_retain

      require message = relay not permitted
              domains = +local_domains : +relay_to_domains

      require verify = recipient

      accept

    # Verify the host against black lists
    acl_check_host:
        deny hosts    = !+relay_from_hosts
             message  = Host is listed in $dnslist_domain.
             dnslists = \
             cbl.abuseat.org : \
             virbl.dnsbl.bit.nl : \
             bl.spamcop.net : \
             sbl.spamhaus.org : \
             xbl.spamhaus.org

        accept

    # Check that the hello does not pretend to come from our servers
    acl_check_helo:
       accept hosts =  +relay_from_hosts

       deny condition = $ } } \
                              } } \
                              } } \
                              } } \
                            }  }

      accept
    # ACL fot data
    acl_check_data:
      deny    condition  = $ }

       deny    malware    = *
               message    = This message contains a virus ($malware_name).
       warn    spam       = nobody
               add_header = X-Spam_score: $spam_score\n\
                            X-Spam_score_int: $spam_score_int\n\
                            X-Spam_bar: $spam_bar\n\
                            X-Spam_report: $spam_report

       deny    message    = Mensaje clasificado como SPAM
               spam       = nobody:true
               condition  = $ }

    begin routers
    dnslookup:
      driver = dnslookup
      domains = ! +local_domains
      transport = remote_smtp
      ignore_target_hosts = 0.0.0.0 : 127.0.0.0/8 : ::::1/128
      no_more

    # Virtual aliases
    virtual_aliases:
      driver = redirect
      allow_fail
      allow_defer
      data = $lsearch }
      file_transport = address_file
      pipe_transport = address_pipe

    system_aliases:
      driver = redirect
      allow_fail
      allow_defer
      data = $lsearch }
    # user = exim
      file_transport = address_file
      pipe_transport = address_pipe

    userforward:
      driver = redirect
      check_local_user
    # local_part_suffix = +* : -*
    # local_part_suffix_optional
      file = $home/.forward
    # allow_filter
      no_verify
      no_expn
      check_ancestor
      file_transport = address_file
      pipe_transport = address_pipe
      reply_transport = address_reply

    localuser:
      driver = accept
      check_local_user
    # local_part_suffix = +* : -*
    # local_part_suffix_optional
      # Without dovecot
      #transport = local_delivery
      # With dovecot
      transport = dovecot_virtual_delivery
      cannot_route_message = Unknown user

    user_vacation:
      driver = accept
      check_local_user
      # do not reply to errors or lists
      condition = "$  }   } }   }"
      no_expn
      require_files = $' or    user_uid = '$@$'}fail}
      # do not reply to errors and bounces or lists
      senders = " ! ^.*-request@.*:\
                  ! ^owner-.*@.*:\
                  ! ^postmaster@.*:\
                  ! ^listmaster@.*:\
                  ! ^mailer-daemon@.*\
                  ! ^root@.*"
      transport = vacation_reply
      unseen
      user = $
      no_verify

    begin transports

    remote_smtp:
      driver = smtp
      delivery_date_add
      dkim_domain = $sender_address_domain
      dkim_selector = thisis
      dkim_private_key = /etc/ssl/exim/dkim.private.key
      dkim_canon = relaxed

    local_delivery:
      driver = appendfile
      directory = $' or user_uid = '$@$'}fail}
      maildir_format
      delivery_date_add
      envelope_to_add
      return_path_add

    dovecot_virtual_delivery:
            driver = pipe
            command = /usr/libexec/dovecot/dovecot-lda -d $local_part@$domain  -f $sender_address
            # v1.1+: command = /usr/local/libexec/dovecot/dovecot-lda -d $local_part@$domain  -f $sender_address -a    $original_local_part@$original_domain
            message_prefix =
            message_suffix =
            delivery_date_add
            envelope_to_add
            return_path_add
            log_output
            temp_errors = 64 : 69 : 70: 71 : 72 : 73 : 74 : 75 : 78
    address_pipe:
      driver = pipe
      return_output

    address_file:
      driver = appendfile
      delivery_date_add
      envelope_to_add
      return_path_add

    address_reply:
      driver = autoreply

    vacation_reply:
      driver = autoreply

    begin retry
    # Address or Domain    Error       Retries
    # -----------------    -----       -------

    *                      *           F,2h,15m; G,16h,1h,1.5; F,4d,6h

    begin rewrite

    # This rule allow to have more than one user with same email
    *@* "$fail}" Ffrw

    begin authenticators
    AUTH_CRAM_MD5=yes
    AUTH_SPA=yes

    CRAM:
      driver = cram_md5
      server_set_id = $auth1
      public_name = CRAM-MD5
      server_secret = $fail}
      #server_secret = $fail}
    SPA:
      driver = spa
      server_set_id = $auth1
      public_name = NTLM
      server_password = $fail}

## [Testing Exim]

Once the configuration file is ready we can test the the file with the following command:

`root `[`#`]`exim -bV`

If everything goes right we can now start exim

`root `[`#`]`/etc/init.d/exim start`

Now we must be able to test how exim will route some addresses

`root `[`#`]`exim -bt someuser`

`root `[`#`]`exim -bt bunnyfoofoo@gmail.com`

`root `[`#`]`exim -bt someuser@example.com`

Finally we can do the bunny test

`root `[`#`]`echo "test" | sendmail bunnyfoofoo@gmail.com`

## [References]

1.  [[[↑](#cite_ref-MX_Survey_of_March_1st.2C_2019_on_SecuritySpace_1-0)] [[Mail (MX) Server Survey](http://www.securityspace.com/s_survey/data/man.201902/mxsurvey.html), as stated in part of the Internet Research Reports by Canadian consulting firm E-Soft Inc., retrieved March 22, 2019]]