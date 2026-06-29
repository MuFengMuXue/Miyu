# Postfix

Postfix is a mail transfer agent that according to its website:
:attempts to be fast, easy to administer, and secure, while at the same time being sendmail compatible enough to not upset existing users. Thus, the outside has a sendmail-ish flavor, but the inside is completely different.

This article builds upon Mail server. The goal of this article is to setup Postfix and explain what the basic configuration files do. There are instructions for setting up local system user-only delivery and a link to a guide for virtual user delivery.

## Installation
Install the  package.

## Configuration
See Postfix Basic Configuration. Configuration files are in  by default. The two most important files are:

* , defines what Postfix services are enabled and how clients connect to them, see
* , the main configuration file, see

Configuration changes need a  reload or run  in order to take effect.

## Aliases
See .

You can specify aliases (also known as forwarders) in .

You should map all mail addressed to root to another account since it is not a good idea to read mail as root.

Uncomment the following line, and change  to a real account.
 root: you

Once you have finished editing  you must run the postalias command:
  # postalias /etc/postfix/aliases
For later changes you can use:
  # newaliases

## Local mail
To only deliver mail to local system users (that are in ) update  to reflect the following configuration. Uncomment, change, or add the following lines:

 myhostname = localhost
 mydomain = localdomain
 mydestination = $myhostname, localhost.$mydomain, localhost
 inet_interfaces = $myhostname, localhost
 mynetworks_style = host
 default_transport = error: outside mail is not deliverable

All other settings may remain unchanged. After setting up the above configuration file, you may wish to set up some #Aliases and then #Start Postfix.

## Virtual mail
Virtual mail is mail that does not map to a user account ().

## Virtual aliases
Virtual aliases are used to rewrite the destination addresses for all local, virtual and remote destinations. This can be used to rewrite the destination address for a single recipient, or an entire domain.

## Virtual address aliases
Set up a virtual alias for a single address.

Enable the virtual alias table:

Populate the virtual alias table:

Rebuild the index file:

 # postmap /etc/postfix/virtual

Restart .

## Check configuration
Run the  command. It should output anything that you might have done wrong in a configuration file.

To see all of your configs, type . To see how you differ from the defaults, try .

## Start Postfix
Start/enable the .

## TLS
For more information, see Postfix TLS Support.

## Secure SMTP (sending)
By default, Postfix/sendmail will not send email encrypted to other SMTP servers. To use TLS when available, add the following line to :

To enforce TLS (and fail when the remote server does not support it), change  to .  Note, however, that this violates RFC:2487 if the SMTP server is publicly referenced.

## Secure SMTP (receiving)
By default, Postfix will not accept secure mail.

You need to obtain a certificate. Point Postfix to your TLS certificates by adding the following lines to :

There are two ways to accept secure mail. STARTTLS over SMTP (port 587 (also called "submission" port)) and SMTPS (port 465 (also called "submissions" port). The latter was previously deprecated but was reinstated by RFC:8314.

To enable STARTTLS over SMTP (port 587), uncomment the following lines in :

The  options remain commented because  are not defined in main.cf by default. If you do decide to set any of , uncomment those lines too.

To enable SMTPS (port 465), uncomment the following lines in :

The rationale surrounding the  lines is the same as above.

## Post-quantum TLS
As of Postfix 3.10 and OpenSSL 3.5.0, it is possible to offer post-quantum key exchanges for TLS. In order to do this, OpenSSL needs to be provided with a config file, as Postfix does not support the new keyshare syntax itself.

To enable this functionality, add the following to your configuration (see {{hc|/etc/postfix/main.cf|2=
tls_eecdh_auto_curves =
tls_ffdhe_auto_groups =
tls_config_file = ${config_directory}/openssl.cnf
tls_config_name = postfix
}}

Then you need to add an appropriate OpenSSL config:

This enables the new post-quantum secure X25519MLKEM768 as well as the previous defaults for traditional, non-quantum safe curves.

## Tips and tricks
## Blacklist incoming emails
Manually blacklisting incoming emails by sender address can easily be done with Postfix.

Create and open  file and append sender email address:

 user@example.com REJECT

Then use the  command to create a database:

 # postmap lmdb:blacklist_incoming

Add the following code before the first permit rule in :

 smtpd_recipient_restrictions = check_sender_access lmdb:/etc/postfix/blacklist_incoming

Finally restart .

## Hide the sender's IP and user agent in the Received header
This is a privacy concern mostly, if you use Thunderbird and send an email. The received header will contain your LAN and WAN IP and info about the email client you used.
(Original source: [https://askubuntu.com/questions/78163/when-sending-email-with-postfix-how-can-i-hide-the-senders-ip-and-username-in AskUbuntu)
What we want to do is remove the Received header from outgoing emails. This can be done by the following steps:

Add the following line to :

 smtp_header_checks = regexp:/etc/postfix/smtp_header_checks

Create  with this content:

 /^Received: .*/     IGNORE
 /^User-Agent: .*/   IGNORE

Finally, restart .

## Postfix in a chroot jail
Postfix is not put in a chroot jail by default. The Postfix documentation provides details about how to accomplish such a jail. The steps are outlined below and are based on the chroot-setup script provided in the Postfix source code.

First, go into the  file in the directory  and change all the chroot entries to 'yes' (y) except for the services , , , , and

Second, create two functions that will help us later with copying files over into the chroot jail (see last step)

 $ alias CP="cp -p"

 cond_copy() {
   # find files as per pattern in $1
   # if any, copy to directory $2
   dir=$(dirname "$1")
   pat=$(basename "$1")
   lr=$(find "$dir" -maxdepth 1 -name "$pat")
   if test ! -d "$2" ; then exit 1 ; fi
   if test "x$lr" != "x" ; then $CP $1 "$2" ; fi
 }

Next, make the new directories for the jail:

 $ set -e
 $ umask 022
 $ POSTFIX_DIR=${POSTFIX_DIR-/var/spool/postfix}
 $ cd ${POSTFIX_DIR}
 $ mkdir -p etc lib usr/lib/zoneinfo
 $ test -d /lib64 && mkdir -p lib64

Find the localtime file:

 $ lt=/etc/localtime
 $ if test ! -f $lt ; then lt=/usr/lib/zoneinfo/localtime ; fi
 $ if test ! -f $lt ; then lt=/usr/share/zoneinfo/localtime ; fi
 $ if test ! -f $lt ; then echo "cannot find localtime" ; exit 1 ; fi
 $ rm -f etc/localtime

Copy localtime and some other system files into the chroot's etc

 $ CP -f $lt /etc/services /etc/resolv.conf /etc/nsswitch.conf etc
 $ CP -f /etc/host.conf /etc/hosts /etc/passwd etc
 $ ln -s -f /etc/localtime usr/lib/zoneinfo

Make sure resolv.conf is owned by root:

 $ chown root /var/spool/postfix/etc/resolv.conf

Copy required libraries into the chroot using the previously created function

 $ cond_copy '/usr/lib/libnss_*.so*' lib
 $ cond_copy '/usr/lib/libresolv.so*' lib
 $ cond_copy '/usr/lib/libdb.so*' lib

And do not forget to reload Postfix.

## DANE (DNSSEC)
## Resource record
DANE supports several types of records, however not all of them are suitable in Postfix.

Certificate usage 0 is unsupported, 1 is mapped to 3 and 2 is optional, thus it is recommendet to publish a "3" record.
More on DANE#TLSA resource record.

## Configuration
Opportunistic DANE is configured this way:

To use per-domain policies, e.g. opportunistic DANE for example.org and mandatory DANE for example.com,
use something like this:

{{hc|/etc/postfix/main.cf|2=
indexed = ${default_database_type}:${config_directory}/

# Per-destination TLS policy
#
smtp_tls_policy_maps = ${indexed}tls_policy

# default_transport = smtp, but some destinations are special:
#
transport_maps = ${indexed}transport
}}

Full documentation is found [https://www.postfix.org/TLS_README.html#client_tls_dane here.

## Extras
*

## Postgrey
Postgrey can be used to enable greylisting for a Postfix mail server.

## Installation
Install the  package. To get it running quickly edit the Postfix configuration file and add these lines:

Then start/enable the  service. Afterwards, reload the  service. Now greylisting should be enabled.

## Configuration
Configuration is done by extending the unit .

## Whitelisting
To add automatic whitelisting (successful deliveries are whitelisted and do not have to wait any more), add the  option and replace  by a suitably small number (or leave it at its default of 5).

To add your own list of whitelisted clients in addition to the default ones, create the file  and enter one host or domain per line, then restart  so the changes take effect.

## Troubleshooting
If you specify  and the socket file is not created ensure you have removed the default  from the service file.

For a full documentation of possible options see .

## SpamAssassin
This section describes how to integrate SpamAssassin.

## SpamAssassin stand-alone generic setup
Edit  and add the content filter under smtp.

Also add the following service entry for SpamAssassin
{{bc|1=
spamassassin unix -     n       n       -       -       pipe
  flags=R user=spamd argv=/usr/bin/vendor_perl/spamc -e /usr/bin/sendmail -oi -f ${sender} ${recipient}
}}

Now you can start and enable .

## SpamAssassin combined with Dovecot LDA / Sieve (Mailfiltering)
Set up LDA and the Sieve-Plugin as described in Dovecot#Sieve. But ignore the last line .

Instead add a pipe in :

  dovecot   unix  -       n       n       -       -       pipe
        flags=DRhu user=vmail:vmail argv=/usr/bin/vendor_perl/spamc -u spamd -e /usr/lib/dovecot/dovecot-lda -f ${sender} -d ${recipient}

And activate it in :

  virtual_transport = dovecot

Alternately, if you do not want to use virtual transports you can use the mailbox_command. This runs with the local user and group, whereas the pipe runs with with the specified user using the  setting.

  mailbox_command = /usr/bin/vendor_perl/spamc -u spamd -e /usr/lib/dovecot/dovecot-lda -f "$SENDER" -a "$RECIPIENT"

## SpamAssassin combined with Dovecot LMTP / Sieve
Set up the LMTP and Sieve as described in Dovecot#Sieve.

Edit  and add:

  sieve_before = /etc/dovecot/sieve.before.d/
  sieve_extensions = +vnd.dovecot.filter
  sieve_plugins = sieve_extprograms
  sieve_filter_bin_dir = /etc/dovecot/sieve-filter
  sieve_filter_exec_timeout = 120s #this is often needed for the long running spamassassin scans, default is otherwise 10s

Create the directory and put spamassassin in as a binary that can be ran by dovecot:

  # mkdir /etc/dovecot/sieve-filter
  # ln -s /usr/bin/vendor_perl/spamc /etc/dovecot/sieve-filter/spamc

Create a new file,  which contains:

  require [ "vnd.dovecot.filter" ];
  filter "spamc" [ "-d", "127.0.0.1", "--no-safe-fallback" ];

Compile the sieve rules :

  # cd /etc/dovecot/sieve.before.d
  # sievec spamassassin.sieve

Finally, restart .

## Rule-based mail processing
With policy services one can easily finetune Postfix' behaviour of mail delivery.
 provides services to do so. This allows you to e.g. implement time-aware grey- and blacklisting of senders and receivers as well as SPF policy checking.

Policy services are standalone services and connected to Postfix like this:

Placing policy services at the end of the queue reduces load, as only legitimate mails are processed. Be sure to place it before the first permit statement to catch all incoming messages.

## Sender Policy Framework
To use the Sender Policy Framework with Postfix, you can install ,  or .

## With spf-engine or python-postfix-policyd-spf
Edit  to your needs. An extensively commented version can be found at .
Pay some extra attention to the HELO check policy, as standard settings strictly reject HELO failures.

In  file, add a timeout for the policyd:

Then add a transport

Lastly you need to add the policyd to the . To minimize load put it to the end of the restrictions but above any  DNSBL line:

Now reload the  service.

You can test your setup with the following:

## With postfix-policyd-spf-perl
Do the same process with postfix as with python-postfix-policyd-spf, but with the following differences:

Timeout for the policyd in  file:

Transport:

Add the policyd to the :

## Sender Rewriting Scheme
To use the Sender Rewriting Scheme with Postfix, install  and adjust the settings:

{{hc|/etc/postsrsd/postsrsd.conf|2=
domains = { "yourdomain.tld", "yournextdomain.tld", "yournextdomain.tld" }
unprivileged-user = "postsrsd"
}}

Enable and start the daemon, making sure it runs after reboot as well.
Then configure Postfix accordingly by tweaking the following lines:

Restart Postfix and start forwarding mail.

## Troubleshooting
## Warning: "database /etc/postfix/*.db is older than source file .."
If you get one or both warnings with journalctl:

 warning: database /etc/postfix/virtual.db is older than source file /etc/postfix/virtual
 warning: database /etc/postfix/transport.db is older than source file /etc/postfix/transport

Then you can fix it by using these commands, depending on the messages you get:

 postmap /etc/postfix/transport
 postmap /etc/postfix/virtual

And restart .

## Host or domain name not found. Name service error for name=...
If you get the following warning with journalctl:

 Host or domain name not found. Name service error for name=...

It could be that you are running Postfix in a  and  is missing. If so, you can fix this by:

 mkdir -p /var/spool/postfix/etc
 cp /etc/resolv.conf /var/spool/postfix/etc/resolv.conf

And restart .

## error: require command: unknown Sieve capability `vnd.dovecot.filter'
 spamassassin: line 1: error: require command: unknown Sieve capability `vnd.dovecot.filter'.
 spamassassin: line 2: error: unknown command 'filter' (only reported once at first occurrence).
 spamassassin: error: validation failed.
 sievec(root): Fatal: failed to compile sieve script 'spamassassin.sieve'

If you get this error when running  after following #SpamAssassin combined with Dovecot LMTP / Sieve, replace  with  in .

Restart .
