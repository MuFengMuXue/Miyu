This page contains [[changes](https://wiki.gentoo.org/index.php?title=Mailfiltering_Gateway&oldid=1250890&diff=1318998)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Mailfiltering_Gateway/hu "Levélszűrő átjáró (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Mailfiltering_Gateway/ru "Почтовый шлюз с фильтрацией (98% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Mailfiltering_Gateway/ja "メールフィルタリング ゲートウェイ (33% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Mailfiltering_Gateway/ko "Mailfiltering Gateway/ko (98% translated)")

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (Use of [2nd person pronouns](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines#Avoid_first_and_second_person_writing "Gentoo Wiki:Guidelines")). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Mailfiltering_Gateway&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

This guide provides step-by-step instructions for installing spam fighting technologies for Postfix. Among them Amavisd-new using Spamassassin and ClamAV, greylisting, and SPF.

See the [Complete Virtual Mail Server](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server "Complete Virtual Mail Server") article for a full guide on setting up a well featured mail server.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [The big picture]](#The_big_picture)
    -   [[1.2] [Preparations]](#Preparations)
-   [[2] [Installing the programs needed]](#Installing_the_programs_needed)
    -   [[2.1] [Setting up DNS]](#Setting_up_DNS)
    -   [[2.2] [Opening the firewall]](#Opening_the_firewall)
    -   [[2.3] [Configuring Postfix]](#Configuring_Postfix)
    -   [[2.4] [Configuring Amavisd-new]](#Configuring_Amavisd-new)
    -   [[2.5] [Configuring ClamAV]](#Configuring_ClamAV)
    -   [[2.6] [Configuring Vipul\'s Razor]](#Configuring_Vipul.27s_Razor)
    -   [[2.7] [Configuring Distributed Checksum Clearinghouse (dcc)]](#Configuring_Distributed_Checksum_Clearinghouse_.28dcc.29)
    -   [[2.8] [Configuring Spamassassin]](#Configuring_Spamassassin)
-   [[3] [Every good rule has good exceptions as well]](#Every_good_rule_has_good_exceptions_as_well)
-   [[4] [Adding more rules]](#Adding_more_rules)
-   [[5] [Testing and finishing up]](#Testing_and_finishing_up)
    -   [[5.1] [Testing the setup]](#Testing_the_setup)
-   [[6] [Autolearning and sidelining emails]](#Autolearning_and_sidelining_emails)
    -   [[6.1] [Creating the spamtrap user]](#Creating_the_spamtrap_user)
    -   [[6.2] [Creating .procmailrc]](#Creating_.procmailrc)
    -   [[6.3] [Create mailfolders]](#Create_mailfolders)
    -   [[6.4] [Adding cron jobs]](#Adding_cron_jobs)
    -   [[6.5] [Modifying amavisd.conf]](#Modifying_amavisd.conf)
    -   [[6.6] [Cleaning up]](#Cleaning_up)
-   [[7] [Greylisting]](#Greylisting)
    -   [[7.1] [Introduction]](#Introduction_2)
    -   [[7.2] [Simple greylisting]](#Simple_greylisting)
    -   [[7.3] [Configuring greylisting]](#Configuring_greylisting)
    -   [[7.4] [Configuring improved greylisting with postgrey]](#Configuring_improved_greylisting_with_postgrey)
-   [[8] [SPF (Sender Policy Framework)]](#SPF_.28Sender_Policy_Framework.29)
    -   [[8.1] [Introduction]](#Introduction_3)
    -   [[8.2] [Preparations]](#Preparations_2)
-   [[9] [Configuring amavisd-new to use MySQL]](#Configuring_amavisd-new_to_use_MySQL)
    -   [[9.1] [Configuring MySQL]](#Configuring_MySQL)
    -   [[9.2] [Configuring amavisd to use MySQL]](#Configuring_amavisd_to_use_MySQL)
-   [[10] [Configuring Spamassassin to use MySQL]](#Configuring_Spamassassin_to_use_MySQL)
    -   [[10.1] [Configuring Spamassassin to use the MySQL backend]](#Configuring_Spamassassin_to_use_the_MySQL_backend)
-   [[11] [Troubleshooting]](#Troubleshooting)
    -   [[11.1] [Amavisd-new]](#Amavisd-new)
    -   [[11.2] [Spamassassin]](#Spamassassin)
    -   [[11.3] [Repeating tasks after installation]](#Repeating_tasks_after_installation)
    -   [[11.4] [Getting help]](#Getting_help)
-   [[12] [Resources]](#Resources)
    -   [[12.1] [For further information]](#For_further_information)
    -   [[12.2] [General resources]](#General_resources)

## [Introduction]

This guide describes step by step how to install a spam and virus filtering mail gateway. It is quite simple to adopt this to a single server solution.

### [The big picture]

This document describe how to setup a spam filtering mail gateway with multiple domains. This server is meant to run in front of the mail servers actually keeping the mail accounts i.e. Microsoft Exchange or Lotus Notes.

In this setup applications with good security records and readable configuration files have been chosen. The email MTA is postfix which has a good security record and is fairly easy to setup right. Postfix will listen normally on port 25 for incoming mail. Upon reception it will forward it to Amavisd-new on port 10024. Amavisd-new will then filter the mail through different filters before passing the mail back to Postfix on port 10025 which in turn will forward the mail to the next mail server.

Amavisd-new is a content filtering framework utilizing helper applications for virus filtering and spam filtering. In this setup we will be using two helper applications one ClamAV for filtering virus mails and Spamassassin for filtering spam. Spamassassin itself can function as yet another layer of content filtering framework and utilize the helper applications Vipul\'s Razor2 and DCC.

Unlike many other spam fighting technologies like RBLs and others Spamassassin does not simply accept or reject a given email based on one single test. It uses a lot of internal tests and external helper applications to calculate a spam score for every mail passed through. This score is based on the following tests:

-   Bayesian filtering
-   Static rules based on regular expressions
-   Distributed and collaborative networks:
    -   RBLs
    -   Razor2
    -   Pyzor
    -   DCC

The first part (chapters 1 to 4) of the guide will describe the basic setup of a mailfiltering gateway. The next chapters can be implemented individually with no dependence between each chapter. These chapters describe how to:

-   setup special IMAP folders for learning of the Bayesian filter and for delivery of false positives
-   setup greylisting with Postfix
-   setup Amavisd-new to use a MySQL backend for user preferences
-   setup Spamassassin to use a MySQL backend for AWL and Bayes data

** Note**\
The IMAP folders will be using the maildir format. Having each mail in a separate file makes handling much simpler. If you\'re using mbox I propose to give maildir a try. If you\'re not already using maildir emerge the necessary tools with `emerge courier-imap` .

A planned fifth part will contain various tips regarding performance and things you may want to know (running chrooted, postfix restrictions, etc.).

** Note**\
Delegating responsibility to third parties is not without risks. You have to know and trust these third parties. In this setup only the decision to quarantine virus mails are based on a single third party. Using Spamassassin\'s scoring system the decision to stop spam mails are not made by a single authority except perhaps Spamassassins own static rules.

** Warning**\
When rejecting spam mails at the MTA level you have to be very careful when selecting the RBL\'s you want to use, i.e. SpamCop is a bad RBL to use at the MTA level because you will experience false positives because sometimes their listing is just too aggressive. Further info at [Realtime Blackhole Lists Are Bad](http://www.geekcomix.com/cgi-bin/classnotes/wiki.pl?UNIX03/Realtime_Blackhole_Lists_Are_Bad) and [The Spam Problem: Moving Beyond RBLs](https://theory.whirlycott.com/~phil/antispam/rbl-bad/rbl-bad.html)

### [Preparations]

Before you start make sure that you have a working Postfix installation where you can send and receive mails also you need a backend mailserver. If you\'re not experienced with setting up Postfix it might quickly become too complicated if all should be set up at once. If you need help you can find it in the excellent [Complete Virtual Mail Server](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server "Complete Virtual Mail Server") in the Gentoo Wiki.

## [Installing the programs needed]

We start out by installing the most important programs: Amavisd-new, Spamassassin and ClamAV.

`root `[`#`]`echo "mail-filter/amavisd-new spamassassin clamav" >> /etc/portage/package.use`

`root `[`#`]`emerge amavisd-new`

`root `[`#`]`freshclam`

** Note**\
As previously mentioned you should already have a working `postfix` instance running on the box. Basically this shouldn\'t be much more than `emerge postfix` *and* have a basic understanding of how Postfix is working.

### [Setting up DNS]

** Note**\
If you\'re not setting up a gateway server but have the mailboxes on the same server you only have to create the MX-Record.

While the programs are emerging fire up another shell and create the needed DNS records.

Start out by creating a `MX` record for the mail gateway and an `A` record for the next destination.

[CODE] **Setting up DNS**

    (Create a MX record for the gateway server)
                    MX      10      mailgateway.mydomain.tld.
    (Create an A record for the gateway server)
    mailgateway     A       mgw.ip.add.here
    (Create an A record for the next hop mail server)
    mail            A       ms.ip.add.here

\

** Note**\
Some ADSL providers might block port 25 and force you to relay mail through one of their servers. Typically you have to create a secondary MX-Record like `MX 20 backup-mx.some-isp.tld`

\

### [Opening the firewall]

In addition to allowing normal mail traffic you have to allow a few services through your firewall to allow the network checks to communicate with the servers.

  ---------------------- ---------- ------
  Application            Protocol   Port
  DCC                    UDP        6277
  Razor(outgoing ping)   TCP        7
  Razor                  TCP        2703
  ---------------------- ---------- ------

Razor uses pings to discover what servers are closest to it.

### [Configuring Postfix]

First we have to tell `postfix` to listen on port 10025 and we remove most of the restrictions as they have already been applied by the `postfix` instance listening on port 25. Also we ensure that it will only listen for local connections on port 10025. To accomplish this we have to add the following at the end of [/etc/postfix/master.cf]

[CODE] **Changing the master.cf file**

    smtp-amavis     unix -        -       n     -       2  smtp
      -o smtp_data_done_timeout=1200
      -o smtp_send_xforward_command=yes
    #Equivalently when using lmtp:
    #lmtp-amavis    unix -        -       n     -       2  lmtp
    #   -o lmtp_data_done_timeout=1200
    #   -o lmtp_send_xforward_command=yes

    127.0.0.1:10025 inet n        -       n     -       -  smtpd
      -o content_filter=
      -o local_recipient_maps=
      -o relay_recipient_maps=
      -o smtpd_restriction_classes=
      -o smtpd_client_restrictions=
      -o smtpd_helo_restrictions=
      -o smtpd_sender_restrictions=
      -o smtpd_recipient_restrictions=permit_mynetworks,reject
      -o mynetworks=127.0.0.0/8
      -o strict_rfc821_envelopes=yes
      -o smtpd_error_sleep_time=0
      -o smtpd_soft_error_limit=1001
      -o smtpd_hard_error_limit=1000

    #If you want to use proxy filtering instead
    #smtp            inet n         -       n      -       8 smtpd
    # -o smtpd_proxy_filter=127.0.0.1:10024
    # -o smtpd_client_connection_count_limit=4
    #If you don't want to scan outgoing mail use this
    #10.0.0.2:smtp   inet n         -       n       -      - smtpd
    #-o content_filter=

** Note**\
The `smtp-amavis` line specifies that a maximum of two of these processes may run at any time. If you need a greater degree of concurrency tune this number to fit your needs. Remember that to match the number with `$max_servers` in [amavisd.conf] . Keep in mind that `amavisd-new` is quite memory-intensive and raising the amount of `amavisd-new` processes too high can easily lead to memory starvation and heavy swapping, which leads to drastically reduced performance.

** Note**\
If you want to reject spam early on in the process you can use the Before-Queue (proxy) method instead of the filter method. If you uncomment the three lines you will have to set `content_filter=` in [main.cf] . This is not recommended for high traffic servers as the number of concurrent connections are limited to the number of amavisd instances.

** Warning**\
The Before-Queue(proxy) method is still not properly tested.

** Note**\
If you, for any reason whatsoever, want to send mail from this box and don\'t want it scanned, add another postfix instance by uncommenting the last two lines and substitute with a proper IP.

The file [master.cf] tells the postfix master program how to run each individual postfix process. More info with `man 8 master` .

Next we need the main `postfix` instance listening on port 25 to filter the mail through `amavisd-new` listening on port 10024.

We also need to set the next hop destination for mail. Tell Postfix to filter all mail through an external content filter and enable explicit routing to let Postfix know where to forward the mail to.

[FILE] **`/etc/postfix/main.cf`**

    biff = no
    empty_address_recipient = MAILER-DAEMON
    queue_minfree = 120000000

    content_filter = smtp-amavis:[127.0.0.1]:10024
    #Equivalently when using lmtp:
    #content_filter = lmtp-amavis:[127.0.0.1]:10024

    # TRANSPORT MAP
    #
    # Insert text from sample-transport.cf if you need explicit routing.
    transport_maps = hash:/etc/postfix/transport

    relay_domains = $transport_maps

Postfix has a lot of options set in [main.cf] . For further explanation of the file please consult `man 5 postconf` or the same online [Postfix Configuration Parameters](http://www.postfix.org/postconf.5.html) .

The format of the [transport] file is the normal Postfix hash file. Mail to the domain on the left hand side is forwarded to the destination on the right hand side.

[FILE] **`/etc/postfix/transport`**

    mydomain.tld                          smtp:mail.mydomain.tld

After we have edited the file we need to run the `postmap` command. Postfix does not actually read this file so we have to convert it to the proper format with `postmap /etc/postfix/transport` . This creates the file [/etc/postfix/transport.db] . There is no need to reload Postfix as it will automatically pick up the changes.

** Note**\
If the next hop mail server is not listening on the standard SMTP port 25 you can tell postfix to use a given port number, like `smtp:mail.mydomain.tld:25000` .

If your first attempts to send mail result in messages bouncing, you\'ve likely made a configuration error somewhere. Try temporarily enabling `soft_bounce` while you work out your configuration issues. This prevents postfix from bouncing mails on delivery errors by treating them as temporary errors. It keeps mails in the mail queue until `soft_bounce` is disabled or removed.

`root `[`#`]`postconf -e "soft_bounce = yes" `

`root `[`#`]`/etc/init.d/postfix reload`

Once you\'ve finished creating a working configuration, be sure to disable or remove `soft_bounce` and reload postfix.

### [Configuring Amavisd-new]

Amavisd-new is used to handle all the filtering and allows you to easily glue together severel different technologies. Upon reception of a mail message it will extract the mail, filter it through some custom filters, handle white and black listing, filter the mail through various virus scanners and finally it will filter the mail using SpamAssassin.

Amavisd-new itself has a number of extra features:

-   it identifies dangerous file attachments and has policies to handle them
-   per-user, per-domain and system-wide policies for:
    -   whitelists
    -   blacklists
    -   spam score thresholds
    -   virus and spam policies

Apart from `postfix` and `freshclam` we will run all applications as the user `amavis` .

Edit the following lines in [/etc/amavisd.conf]

[FILE] **`/etc/amavisd.conf`**

    # (Insert the domains to be scanned)
    $mydomain = 'example.com';
    # (Bind only to loopback interface)
    $inet_socket_bind = '127.0.0.1';
    # (Forward to Postfix on port 10025)
    $forward_method = 'smtp:127.0.0.1:10025';
    $notify_method = $forward_method;
    # (Define the account to send virus alert emails)
    $virus_admin = "virusalert\@$mydomain";
    # (Always add spam headers)
    $sa_tag_level_deflt  = -100;
    # (Add spam detected header aka X-Spam-Status: Yes)
    $sa_tag2_level_deflt = 5;
    # (Trigger evasive action at this spam level)
    $sa_kill_level_deflt = $sa_tag2_level_deflt;
    # (Do not send delivery status notification to sender.  It does not affect
    # delivery of spam to recipient. To do that, use the kill_level)
    $sa_dsn_cutoff_level = 10;
    # Don't bounce messages left and right, quarantine
    # instead
    $final_virus_destiny      = D_DISCARD;  # (defaults to D_DISCARD)
    $final_banned_destiny     = D_DISCARD;  # (defaults to D_BOUNCE)
    $final_spam_destiny       = D_DISCARD;  # (defaults to D_BOUNCE)

** Note**\
With this line `$sa_tag2_level_deflt = 5;` you set the Spamassassin spam score to 5. This might be a bit low. As you might have noticed the Amavisd-new default is `6.3` . If you don\'t want to see a single spam mail in your mail folder choose `5` , but if you don\'t want to deal with false positives choose `6.3` .

Create a quarantine directory for the virus mails as we don\'t want these delivered to our users.

`root `[`#`]`mkdir /var/amavis/virusmails `

`root `[`#`]`chown amavis:amavis /var/amavis/virusmails `

`root `[`#`]`chmod 750 /var/amavis/virusmails`

** Note**\
Amavisd-new offers finer policy tuning by using policy banks.

### [Configuring ClamAV]

As virus scanner we use ClamAV as it has a fine detection rate comparable with commercial offerings, it is very fast and it is Open Source Software. We love log files, so make `clamd` log using `syslog` and turn on verbose logging. Also do not run `clamd` as `root` . Now edit [/etc/clamd.conf]

[FILE] **`/etc/clamd.conf`**

    # (Verbose logging with syslog)
    LogSyslog
    LogVerbose
    LogFacility LOG_MAIL
    # (Change pid file location)
    PidFile /var/run/amavis/clamd.pid
    # (Set the clamav socket)
    LocalSocket /var/amavis/clamd
    # (Close the connection when this limit is exceeded)
    StreamMaxLength 10M
    # (Don't run clamd as root)
    User amavis
    # (Newer versions require you to uncomment this)
    ScanMail
    ScanArchive

** Note**\
Also remember to remove the Example directive to make ClamAV work

ClamAV comes with the `freshclam` deamon dedicated to periodical checks of virus signature updates. Instead of updating virus signatures twice a day we will make `freshclam` update virus signatures every two hours.

[FILE] **`/etc/freshclam.conf`**

    # (Syslog logging)
    LogSyslog
    # (Verbose logging)
    LogVerbose
    # (Explicitly drop root privileges)
    DatabaseOwner clamav
    # (Check for updates every two hours. That is the official recommendation)
    Checks 12
    # (Use the mirror closest to you. Replace XY with your country code
    DatabaseMirror db.XY.clamav.net

Start `clamd` with `freshclam` using the init scripts by modifying [/etc/conf.d/clamd] .

[FILE] **`/etc/conf.d/clamd`**

    START_CLAMD=yes
    START_FRESHCLAM=yes
    CLAMD_NICELEVEL=3
    FRESHCLAM_NICELEVEL=19
    IONICE_LEVEL=2

At last modify [amavisd.conf] with the new location of the socket.

[FILE] **`/etc/amavisd.conf`**

    # (Uncomment the clamav scanner and modify socket location)
    ['ClamAV-clamd',
    \&ask_daemon, ["CONTSCAN \n", "/var/amavis/clamd"],
      qr/\bOK$/, qr/\bFOUND$/,
      qr/^.*?: (?!Infected Archive)(.*) FOUND$/ ],

** Warning**\
Do NOT modify the `$unix_socketname` unless you know what you\'re doing.

### [][Configuring Vipul\'s Razor]

Razor2 is a collaborative and distributed spam checksum network. Install it with `emerge razor` and create the needed configuration files. Do this as user `amavis` by running `su - amavis` followed `razor-admin -create` .

`root `[`#`]`emerge razor`

`root `[`#`]`su - amavis -s /bin/bash`

`user `[`$`]`razor-admin -create `

`user `[`$`]`exit`

### [][Configuring Distributed Checksum Clearinghouse (dcc)]

Like Razor2, dcc is a collaborative and distributed spam checksum network. Its philosopy is to count the number of recipients of a given mail identifying each mail with a fuzzy checksum.

`root `[`#`]`emerge dcc`

### [Configuring Spamassassin]

Amavis is using the Spamassassin Perl libraries directly so there is no need to start the service. Also this creates some confusion about the configuration as some Spamassassin settings are configured in [/etc/mail/spamassassin/local.cf] and overridden by options in [/etc/amavisd.conf] .

[FILE] **`/etc/mail/spamassassin/local.cf`**

    # Enable the Bayes system
    use_bayes               1

    # Enable all network checks
    skip_rbl_checks         0

    # Mail using languages used in these country codes will not be marked
    # as being possibly spam in a foreign language.
    # - danish english norwegian swedish
    ok_languages            da en no sv

    # Mail using locales used in these country codes will not be marked
    # as being possibly spam in a foreign language.
    ok_locales              en

    # Use a sensible bayes path
    bayes_path              /var/amavis/.maildir/bayes

\

** Note**\
With Spamassassin version 3.1 you have to enable DCC, Razor2 by uncommenting the corresponding lines in [v310.pre] .

** Note**\
You can find inspiration for your [local.cf] file by trying the [SpamAssassin Configuration Generator](http://www.yrex.com/spam/spamconfig.php) .

** Note**\
You might also want to switch the `ok_languages` and `ok_locales` .

## [Every good rule has good exceptions as well]

Once mail really starts passing through this mail gateway you will probably discover that the above setup is not perfect. Maybe some of your customers like to receive mails that others wouldn\'t. You can whitelist/blacklist envelope senders quite easily. Uncomment the following line in [amavisd.conf] .

[FILE] **`amavisd.conf`do sitewide scoring**

    read_hash("/var/amavis/sender_scores_sitewide"),

In the [sender_scores_sitewide] file you put complete email addresses or just the domian parts and then note a positive/negative score to add to the spam score.

[FILE] **`whitelist_sender`example**

    # (Whitelist all emails from the specific email address)
    postmaster@example.net                -3.0
    # (Whitelist all emails from the example.net excluding subdomains)
    .example.net                          1.0

\

** Note**\
See [/etc/amavisd.conf] for more examples.

** Note**\
Placing these addresses outside [amavisd.conf] is a cleaner and safer solution.

** Note**\
Alternatively it can be done in Spamassassin\'s configuration file [/etc/mail/spamassassin/local.cf] but I think it is cleaner to do it in [/etc/amavisd.conf] .

** Note**\
In a later chapter I will show how to implement per-user policies using MySQL.

While waiting for a better method you can add the following to [amavisd.conf] to bypass spam checks for `postmaster` and `abuse` mailboxes.

[CODE] **Bypass spam filters for all postmaster and abuse mails**

    map =1 } (qw(
            postmaster@
            abuse@
    ));

** Important**\
While we are at it we should *never* automatically discard mails to the `postmaster` or the `abuse` accounts. See [RFC 2142 MAILBOX NAMES FOR COMMON SERVICES, ROLES AND FUNCTIONS](http://www.ietf.org/rfc/rfc2142.txt) . Otherwise your domains might end up listed in some of the evil lists over at [rfc-ignorant.org](http://www.rfc-ignorant.org/) .

## [Adding more rules]

If you want to use more rules provided by the SARE Ninjas over at the [SpamAssassin Rules Emporium](http://www.rulesemporium.com/) you can easily add and update them using the `sa-update` mechanism included in Spamassassin.

A brief guide to using SARE rulesets with `sa-update` can be found [here](http://daryl.dostech.ca/sa-update/sare/sare-sa-update-howto.txt) .

## [Testing and finishing up]

### [Testing the setup]

Now before you start `freshclam` you can manually verify that it works.

`root `[`#`]`freshclam`

    ClamAV update process started at Sun May  2 09:13:41 2004
    Reading CVD header (main.cvd): OK
    Downloading main.cvd [*]
    main.cvd updated (version: 22, sigs: 20229, f-level: 1, builder: tkojm)
    Reading CVD header (daily.cvd): OK
    Downloading daily.cvd [*]
    daily.cvd updated (version: 298, sigs: 1141, f-level: 2, builder: diego)
    Database updated (21370 signatures) from database.clamav.net (193.1.219.100).

Now you have updated virus definitions and you know that [freshclam.conf] is working properly.

Test freshclam and amavisd from the cli and amavisd testmails. Start `clamd` and `amavis` with the following commands:

`root `[`#`]`/etc/init.d/clamd start `

`root `[`#`]`/etc/init.d/amavisd start `

`root `[`#`]`/etc/init.d/postfix reload`

If everything went well `postfix` should now be listening for mails on port 25 and for reinjected mails on port 10024. To verify this check your log file.

`root `[`#`]`tail -f /var/log/mail.log`

** Note**\
Depending on your log settings the correct path might be [/var/log/messages] .

Now if no strange messages appear in the log file it is time for a new test.

Use `netcat` to manually connect to `amavisd` on port 10024 and `postfix` on port 10025.

** Note**\
Netcat can be used as an advanced replacement for `telnet` . Install it with `emerge netcat` .

** Note**\
For some unknown reason you can not complete a manual mail injection to `amavisd` with netcat. Use `telnet` instead.

`root `[`#`]`nc localhost 10024`

    220 [127.0.0.1] ESMTP amavisd-new service ready

`root `[`#`]`nc localhost 10025`

    220 example.com ESMTP Postfix

\

** Note**\
If you want to see the complete output from amavisd-new start `amavisd debug-sa` as the `amavis` user and send a mail. For this to work you might have to change the default shell in [/etc/passwd] .

Add `amavisd` and `clamd` to the `default` runlevel.

`root `[`#`]`rc-update add clamd default `

`root `[`#`]`rc-update add amavisd default`

** Note**\
We do not add `spamd` to the default runlevel as `amavisd` uses the Spamassassin Perl libraries directly.

** Note**\
You might notice `Net::Server: Couldn't POSIX::setuid to ... []` lines in your log. According to [amavis chroot README](http://www.ijs.si/software/amavisd/README.chroot) , if the process UID remains 0 ( `root` ), the program will terminate, otherwise you can consider the message just as informative. This is because `POSIX::setuid()` returns a string `0 but true` .

** Important**\
If you enabled login for amavis remember to set back the login shell in [/etc/passwd] to `/bin/false` .

## [Autolearning and sidelining emails]

### [Creating the spamtrap user]

Create the spamtrap account and directories.

`root `[`#`]`useradd -m spamtrap `

`root `[`#`]`maildirmake /home/spamtrap/.maildir `

`root `[`#`]`chown -R spamtrap:spamtrap /home/spamtrap/.maildir`

Give the spamtrap user a sensible password.

`root `[`#`]`passwd spamtrap`

If you manually want to check some of the mails to ensure that you have no false positives you can use the following `procmail` recipe to sideline spam found into different mail folders.

### [Creating .procmailrc]

[FILE] **`/home/spamtrap/.procmailrc`**

    #Set some default variables
    MAILDIR=$HOME/.maildir

    SPAM_FOLDER=$MAILDIR/.spam-found/

    LIKELY_SPAM_FOLDER=$MAILDIR/.likely-spam-found/

    #Sort mails with a spamscore of 7+ to the spamfolder
    :0:
    * ^X-Spam-Status: Yes
    * ^X-Spam-Level: \*\*\*\*\*\*\*
    $SPAM_FOLDER

    #Sort mail with a spamscore between 5-7 to the likely spam folder
    :0:
    * ^X-Spam-Status: Yes
    $LIKELY_SPAM_FOLDER

    #Sort all other mails to the inbox
    :0
    *
    ./

** Warning**\
If your mail server is going to receive a lot of mail you should NOT use the likely-spam recipe. Instead set `$sa_tag2_level_deflt` high enough to avoid false positives and filter it directly to `$SPAM_FOLDER` .

** Note**\
If you haven\'t already installed `procmail` do it with `emerge procmail` .

Now make sure that Postfix uses `procmail` to deliver mail.

[FILE] **`/etc/postfix/main.cf`**

    mailbox_command = /usr/bin/procmail -a "DOMAIN"

### [Create mailfolders]

Now we will create shared folders for ham and spam.

`root `[`#`]`maildirmake /var/amavis/.maildir `

`root `[`#`]`maildirmake -S /var/amavis/.maildir/Bayes `

`root `[`#`]`maildirmake -s write -f spam /var/amavis/.maildir/Bayes `

`root `[`#`]`maildirmake -s write -f ham /var/amavis/.maildir/Bayes `

`root `[`#`]`maildirmake -s write -f redeliver /var/amavis/.maildir/Bayes`

Amavisd-new needs to be able to read these files as well as all mailusers. Therefore we add all the relevant users to the mailuser group along with amavis.

`root `[`#`]`groupadd mailusers `

`root `[`#`]`usermod -G mailusers spamtrap `

`root `[`#`]`chown -R amavis:mailusers /var/amavis/.maildir/ `

`root `[`#`]`chown amavis:mailusers /var/amavis/ `

`root `[`#`]`chmod -R 1733 /var/amavis/.maildir/Bayes/ `

`root `[`#`]`chmod g+rx /var/amavis/.maildir/ `

`root `[`#`]`chmod g+rx /var/amavis/.maildir/Bayes/`

** Warning**\
This grants members of the `mailusers` groups access to `amavis` mail.

This makes the spam and ham folders writable but not readable. This way users can safely submit their ham without anyone else being able to read it.

Then run the following command as the `spamtrap` user:

`user `[`$`]`maildirmake --add Bayes=/var/amavis/.maildir/Bayes $HOME/.maildir`

** Note**\
We have to give the group read permissions on the [Bayes] folder in order for the mail client to be able to see the subdirectories used by IMAP.

### [Adding cron jobs]

Now run `crontab -u amavis -e` to edit the amavis crontab to enable automatic learning of the Bayes filter every hour.

[FILE] **`crontab`for amavis user**

    #Auto learn
    0 * * * *          /usr/bin/sa-learn --spam /var/amavis/.maildir/Bayes/.spam/ \
                        > /dev/null 2>&1
    0 * * * *          /usr/bin/sa-learn --ham /var/amavis/.maildir/Bayes/.ham/ > \
                       /dev/null 2>&1

** Note**\
`amavis` has to be a member of the`cron` group to run crons.

** Note**\
It seems like the shared maildir folders will make `sa-learn` examine all messages twice. This should not be a problem. The output will also show that the maximum of messages learned from is half or less than the messages examined.

### [Modifying amavisd.conf]

Now modify amavis to redirect spam emails to the `spamtrap` account and keep spamheaders.

[FILE] **`/etc/amavisd.conf`**

    # (Define the account to send virus spam emails)
    $spam_quarantine_to = "spamtrap\@$myhostname";

### [Cleaning up]

We don\'t want to keep mail forever so we use `tmpwatch` to clean up regularily. Emerge it with `emerge tmpwatch` . Only `root` is able to run `tmpwatch` so we have to edit the `root` crontab.

[FILE] **`crontab`root user**

    # Clean up
    # Keep virusmails for a week (24*7 hours)
    15 0 * * *      /usr/sbin/tmpwatch -c -f -d --quiet 168 /var/amavis/virusmails/
    # Delete spam and ham learned after a week
    15 0 * * *      /usr/sbin/tmpwatch -c -f -d --quiet 168 /var/amavis/.maildir/Bayes/

## [Greylisting]

### [Introduction]

Greylisting is one of the newer weapons in the spam fighting arsenal. As the name implies it is much like whitelisting and blacklisting. Each time an unknown mailserver tries to deliver mail the mail is rejected with a *try again later* message. This means that mail gets delayed but also that stupid spam bots that do not implement the RFC protocol will drop the attempt to deliver the spam and never retry. With time spam bots will probably adjust, however it will give other technologies more time to identify the spam.

** Note**\
If your ISP blocks incoming traffic on port 25 and relays all mail to you through their own mail server greylisting will not work.

Postfix 2.1 come with a simple Perl greylisting policy server that implements such a scheme. However it suffers from unpredictable results when the partition holding the greylisting database run out of space. There exists an improved version that do not suffer this problem. First I will show how to install the builtin greylisting support that come with Postfix and then I will show how to configure the more robust replacement.

** Note**\
There are other greylisting policy servers for Postfix around (such as [Gld](http://www.gasmi.net/gld.html) , which is in Portage, and [SQLgrey](http://sqlgrey.sourceforge.net/) ). Some of them support database backends, auto whitelisting and other neat features.

### [Simple greylisting]

** Note**\
If you prefer to use the improved greylisting with postgrey you can safely skip this section.

We need the file [greylist.pl] but unfortunately the ebuild does not install it as default.

`root `[`#`]`cp /var/cache/distfiles/postfix-your-version-here.tar.gz /root/ `

`root `[`#`]`tar xzf postfix-your-version-here.tar.gz `

`root `[`#`]`cp postfix-2.1.0/examples/smtpd-policy/greylist.pl /usr/bin/`

Now we have the file in place we need to create the directory to hold the greylisting database:

`root `[`#`]`mkdir /var/mta `

`root `[`#`]`chown nobody /var/mta`

** Warning**\
Do not create the greylisting database directory on a partition that might run out of space. While postfix can recover from no-space-left situations for the mail queue and mail box situations, this is not the case with the greylisting database. If the file becomes corrupted you may not be able to receive mail at all until you delete the file by hand.

### [Configuring greylisting]

Now that we have all this ready all that is left is to add it to the postfix configuration. First we add the necessary information to the [master.cf] :

[CODE] **Modifying master.cf to use greylisting**

    policy-greylist  unix  -       n       n       -       -       spawn
       user=nobody argv=/usr/bin/perl /usr/bin/greylist.pl

The postfix spawn daemon normally kills its child processes after 1000 seconds but this is too short for the greylisting process so we have to increase the timelimit in [main.cf] :

[FILE] **`main.cf`use greylisting**

    policy-greylist_time_limit = 3600
    # (Under smtpd_recipient_restrictions add:)
    check_sender_access hash:/etc/postfix/sender_access
    # (Later on add:)
    restriction_classes = greylist
    greylist = check_policy_service unix:private/policy-greylist

** Warning**\
Be sure to specify `check_sender_access` AFTER `reject_unauth_destination` or else your system could become an open mail relay.

** Note**\
The greylist database gets polluted quickly with bogus addresses. It helps if you protect greylist lookups with other restrictions that reject unknown senders and/or recipients.

We don\'t want to use greylisting for all domains but only for those frequently abused by spammers. After all it will delay mail delivery. A list of frequently forged MAIL FROM domains can be found [online](http://www.monkeys.com/anti-spam/filtering/sender-domain-validate.in) . Add the domains you receive a lot of spam from to [/etc/postfix/sender_access] :

[CODE] **Format of sender_access**

    aol.com     greylist
    hotmail.com greylist
    bigfoot.com greylist

If you want a more extensive list:

`root `[`#`]`wget `[`http://www.monkeys.com/anti-spam/filtering/sender-domain-validate.in`](http://www.monkeys.com/anti-spam/filtering/sender-domain-validate.in)` `

`root `[`#`]`cat sender-domain-validate.in | sort | awk  > /etc/postfix/sender_access`

Now we only have to initialize the [sender_access] database:

`root `[`#`]`postmap /etc/postfix/sender_access`

Now the setup of simple greylisting is complete.

** Warning**\
I tried this on one box handling thousands of mails daily and the results were almost a complete disaster. After four days the box was bogged down with hundreds of old `greylist.pl` processes.

### [Configuring improved greylisting with postgrey]

You can install the enhanced greylisting policy server with a simple `emerge` :

`root `[`#`]`emerge postgrey`

After installing `postgrey` we have to edit [main.cf] . Changes are almost exactly like the built in greylisting.

[FILE] **`main.cf`use greylisting**

    # (Under smtpd_recipient_restrictions add:)
    check_sender_access hash:/etc/postfix/sender_access
    # (Later on add:)
    smtpd_restriction_classes = greylist
    greylist = check_policy_service inet:127.0.0.1:10030

** Note**\
The Postfix SMTPD_POLICY_README only uses `restriction_classes` but that does not appear to work.

** Note**\
If you want to greylist everything instead add `check_policy_service inet:127.0.0.1:10030` .

Finally, start the server and add it to the proper runlevel.

`root `[`#`]`/etc/init.d/postgrey start `

`root `[`#`]`rc-update add postgrey default`

** Note**\
Some people like to get their mail fast and thus greylisting is worthless. However if you employ a backup mail server you can safely setup greylisting on that server. My limited experiences tell me that it can stop up to a third of the spam received.

## [][SPF (Sender Policy Framework)]

### [Introduction]

SPF allows domain owners to state in their DNS records which IP addressess should be allowed to send mails from their domain. This will prevent spammers from spoofing the `Return-Path`.

** Note**\
If your ISP blocks incoming traffic on port 25 and relays all mail to you through their own mail server SPF will not work.

First domain owners have to create a special `TXT` DNS record. Then an SPF-enabled MTA can read this and if the mail originates from a server that is not described in the SPF record the mail can be rejected. An example entry could look like this:

[CODE] **Example SPF record**

    example.com.  IN TXT  "v=spf1 a mx ptr -all"

The `-all` means to reject all mail by default but allow mail from the `A`( `a` ), `MX`( `mx` ) and `PTR`( `ptr` ) DNS records. For more info consult further resources below.

** Note**\
If you relay outgoing mail through your ISP you will have to add: `include:yourisp.com` .

Spamassassin 3.0 has support for SPF, however it is not enabled by default and the new policy daemon in Postfix supports SPF so let\'s install SPF support for Postfix.

** Note**\
If you want to use SPF with Spamassassin instead simply `emergeÂ dev-perl/Mail-SPF-Query` and restart Amavisd-new.

### [Preparations]

First you have to install Postfix 2.1 as described above. When you have fetched the source grab the [spf.pl] with:

`root `[`#`]`cp postfix-<version>/examples/smtpd-policy/spf.pl /usr/local/bin/`

** Note**\
The [spf.pl] coming with Postfix is slightly buggy so find and uncomment the following line: `push @HANDLERS, "sender_permitted_from"; use Mail::SPF::Query;` . Furthermore in about line 199 substitute `comemnt` with `comment` . Alternatively you can download a [development version](http://spf.pobox.com/postfix-policyd.txt) .

This Perl script also needs some Perl libraries that are not in portage but it is still quite simple to install them:

`root `[`#`]`emerge Mail-SPF-Query Net-CIDR-Lite Sys-Hostname-Long`

Now that we have everything in place all we need is to configure Postfix to use this new policy.

[FILE] **`master.cf`use SPF**

    policy-spf  unix  -       n       n       -       -       spawn
       user=nobody argv=/usr/bin/perl /usr/local/bin/spf.pl

Now add the SPF check in [main.cf] . Properly configured SPF should do no harm so we could check SPF for all domains:

[FILE] **`main.cf`use SPF**

    # (Under smtpd_recipient_restrictions add:)
    check_policy_service unix:private/policy-spf

** Note**\
If you\'re experiencing problems with SPF, e.g. when using `fetchmail` , you might want to enable SPF for certain domains only.

## [Configuring amavisd-new to use MySQL]

### [Configuring MySQL]

** Note**\
This has not been tested on versions higher than 2.2. Feedback is welcome :)

For large domains the default values you can set in [amavisd.conf] might not suit all users. If you configure amavisd-new with MySQL support you can have individual settings for users or groups of users.

`user `[`$`]`mysql -u root -p mysql`

    Enter password:
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 78 to server version: 4.0.18-log

    Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

`mysql>``create database maildb;`

`mysql>``GRANT INSERT,UPDATE,DELETE,SELECT ON maildb.* TO 'mail'@'localhost' IDENTIFIED BY 'very_secret_password'; `

`mysql>``use maildb;`

Now that the database is created we\'ll need to create the necessary tables. You can cut and paste the following into the mysql prompt:

[CODE] **MySQL table layout**

    CREATE TABLE users (
        id         int unsigned NOT NULL auto_increment,
        priority   int          NOT NULL DEFAULT '7',  -- 0 is low priority
        policy_id  int unsigned NOT NULL DEFAULT '1',
        email      varchar(255) NOT NULL,
        fullname   varchar(255) DEFAULT NULL,    -- not used by amavisd-new
        local      char(1),     -- Y/N  (optional field, see note further down)
        PRIMARY KEY (id),
        KEY email (email)
        );
    CREATE UNIQUE INDEX users_idx_email ON users(email);

    # (any e-mail address, external or local, used as senders in wblist)
    CREATE TABLE mailaddr (
       id         int unsigned NOT NULL auto_increment,
       priority   int          NOT NULL DEFAULT '7',  -- 0 is low priority
       email      varchar(255) NOT NULL,
       PRIMARY KEY (id),
       KEY email (email)
       );
    CREATE UNIQUE INDEX mailaddr_idx_email ON mailaddr(email);

    # (-- per-recipient whitelist and/or blacklist,
    # -- puts sender and recipient in relation wb)
    # (white or blacklisted sender)
    CREATE TABLE wblist (
       rid        int unsigned NOT NULL,     -- recipient: users.id
       sid        int unsigned NOT NULL,     -- sender:    mailaddr.id
       wb         char(1) NOT NULL, -- W or Y / B or N / space=neutral
       PRIMARY KEY (rid,sid)
       );

    CREATE TABLE policy (
       id               int unsigned NOT NULL auto_increment,
       policy_name      varchar(32),     -- not used by amavisd-new
       virus_lover          char(1),     -- Y/N
       spam_lover           char(1),     -- Y/N  (optional field)
       banned_files_lover   char(1),     -- Y/N  (optional field)
       bad_header_lover     char(1),     -- Y/N  (optional field)
       bypass_virus_checks  char(1),     -- Y/N
       bypass_spam_checks   char(1),     -- Y/N
       bypass_banned_checks char(1),     -- Y/N  (optional field)
       bypass_header_checks char(1),     -- Y/N (optional field)
       spam_modifies_subj   char(1),     -- Y/N (optional field)
       spam_quarantine_to   varchar(64) DEFAULT NULL, -- (optional field)
       spam_tag_level  float,  -- higher score inserts spam info headers
       spam_tag2_level float DEFAULT NULL,  -- higher score inserts
                   -- 'declared spam' info header fields
       spam_kill_level float,  -- higher score activates evasive actions, e.g.
                   -- reject/drop, quarantine, ...
                   -- (subject to final_spam_destiny setting)
       PRIMARY KEY (id)
      );

** Note**\
If you have problems using copy/paste you might have to copy this somewhere else and clean out the unneeded characters.

** Note**\
Lookups trying to match email are done with raw (rfc2821-unquoted and unbracketed) addresses as a key, i.e.: `John "Funny" Smith@example.com`

** Note**\
Lookups are performed in the following order: `SQL` , `LDAP` , `hash` , `ACL` , `regexp` , `constant` . The first that returns a definitive answer (not `undef/NULL` ) stops the search.

If you wish to use whitelisting and blacklisting you must add the sender and receiver to `mailadr` after which you create the relation between the two e-mail addresses in `wblist` and state if it is whitelisting ( `W` ) or blacklisting ( `B` ).

Now that we have created the tables let\'s insert a test user and a test policy:

[CODE] **Create test user and test policy**

    INSERT INTO users
       SET
          id         =1,
          priority   =9,
          policy_id  =1,
          email      ="johndoe@example.com",
          fullname   ="John Doe",
          local      ="Y";

    INSERT INTO policy
       SET
          id                     =1,
          policy_name            ="Test policy 1",
          virus_lover            ="N",
          spam_lover             ="N",
          banned_files_lover     ="N",
          bad_header_lover       ="N",
          bypass_virus_checks    ="N",
          bypass_spam_checks     ="N",
          bypass_banned_checks   ="N",
          bypass_header_checks   ="N",
          spam_modifies_subj     ="N",
          spam_quarantine_to     =NULL,
          spam_tag_level         =-50.0,
          spam_tag2_level        =7.0,
          spam_kill_level        =10.0;

** Note**\
Copy this to somewhere else and adjust to suit your own environment.

** Note**\
`local` should be set to`Y` otherwise the mail will not be scanned for spam.

This inserts a test user and a Test policy. Adjust these examples to fit your needs. Further explanation of the configuration names can be found in [amavisd.conf] .

### [Configuring amavisd to use MySQL]

Now that MySQL is ready we need to tell amavis to use it:

[FILE] **`amavisd.conf`Update to use MySQL**

    @lookup_sql_dsn =
       ( ['DBI:mysql:maildb:host1', 'mail', 'very_secret_password']  );

    # (For clarity uncomment the default)
    $sql_select_policy = 'SELECT *,users.id FROM users,policy'.
       ' WHERE (users.policy_id=policy.id) AND (users.email IN (%k))'.
       ' ORDER BY users.priority DESC';

    # (If you want sender white/blacklisting)
       $sql_select_white_black_list = 'SELECT wb FROM wblist,mailaddr'.
         ' WHERE (wblist.rid=?) AND (wblist.sid=mailaddr.id)'.
         '   AND (mailaddr.email IN (%k))'.
         ' ORDER BY mailaddr.priority DESC';
    </pre>

## [Configuring Spamassassin to use MySQL]

As of Spamassassin 3.0 it is possible to store the Bayes and AWL data in a MySQL database. We will use MySQL as the backend as it can generally outperform other databases. Also, using MySQL for both sets of data makes system management much easier. Here I will show how to easily accomplish this.

First start out by creating the new MySQL user and then create the needed tables.

`root `[`#`]`mysql -u root -p mysql`

    Enter password:
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 78 to server version: 4.0.18-log

    Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

`mysql>``create database dbname;`

`mysql>``GRANT INSERT,UPDATE,DELETE,SELECT ON dbname.* TO 'dbuser'@'localhost' IDENTIFIED BY 'another_very_secret_password'; `

`mysql>``use dbname;`

Now that the database is created we\'ll create the necessary tables. You can cut and paste the following into the mysql prompt:

[CODE] **MySQL table layout**

    CREATE TABLE bayes_expire (
              id                    int(11)         NOT NULL default '0',
              runtime               int(11)         NOT NULL default '0',
              KEY bayes_expire_idx1 (id)
              ) TYPE=MyISAM;

          CREATE TABLE bayes_global_vars (
              variable              varchar(30)     NOT NULL default '',
              value                 varchar(200)    NOT NULL default '',
              PRIMARY KEY           (variable)
              ) TYPE=MyISAM;

          INSERT INTO bayes_global_vars VALUES ('VERSION','3');

          CREATE TABLE bayes_seen (
              id                    int(11)         NOT NULL default '0',
              msgid                 varchar(200) binary NOT NULL default '',
              flag                  char(1)         NOT NULL default '',
              PRIMARY KEY           (id,msgid)
              ) TYPE=MyISAM;

          CREATE TABLE bayes_token (
              id                    int(11)         NOT NULL default '0',
              token                 char(5)         NOT NULL default '',
              spam_count            int(11)         NOT NULL default '0',
              ham_count             int(11)         NOT NULL default '0',
              atime                 int(11)         NOT NULL default '0',
              PRIMARY KEY           (id, token),
              INDEX (id, atime)
              ) TYPE=MyISAM;

          CREATE TABLE bayes_vars (
              id                    int(11)         NOT NULL AUTO_INCREMENT,
              username              varchar(200)    NOT NULL default '',
              spam_count            int(11)         NOT NULL default '0',
              ham_count             int(11)         NOT NULL default '0',
              token_count           int(11)         NOT NULL default '0',
              last_expire           int(11)         NOT NULL default '0',
              last_atime_delta      int(11)         NOT NULL default '0',
              last_expire_reduce    int(11)         NOT NULL default '0',
              oldest_token_age      int(11)         NOT NULL default '2147483647',
              newest_token_age      int(11)         NOT NULL default '0',
              PRIMARY KEY           (id),
              UNIQUE bayes_vars_idx1 (username)
              ) TYPE=MyISAM;

          CREATE TABLE awl (
              username              varchar(100)    NOT NULL default '',
              email                 varchar(200)    NOT NULL default '',
              ip                    varchar(10)     NOT NULL default '',
              count                 int(11)         default '0',
              totscore              float           default '0',
              PRIMARY KEY           (username,email,ip)
              ) TYPE=MyISAM;

** Important**\
The `INSERT` line is needed otherwise Spamassassin will not work.

** Note**\
This is also available in the source tarball in the files [awl_mysql.sql] and [bayes_mysql.sql] .

### [Configuring Spamassassin to use the MySQL backend]

If you have an old Bayes database in the DBM database and want to keep it follow these instructions:

`root `[`#`]`su - amavis`

`user `[`$`]`sa-learn --sync `

`user `[`$`]`sa-learn --backup > backup.txt `

`user `[`$`]`sa-learn --restore backup.txt`

** Note**\
Note that the last step should only be performed after the MySQL database and [secrets.cf] have been updated.

Now give Spamassassin the required info:

[FILE] **`/etc/mail/spamassassin/secrets.cf`**

    # (Tell Spamassassin to use MySQL for bayes data
    bayes_store_module              Mail::SpamAssassin::BayesStore::SQL
    bayes_sql_dsn                   DBI:mysql:sa_bayes:localhost:3306
    bayes_sql_username              db_name
    bayes_sql_password              another_very_secret_password

    # (Tell Spamassassin to use MySQL for AWL data
    auto_whitelist_factory          Mail::SpamAssassin::SQLBasedAddrList
    user_awl_dsn                    DBI:mysql:sa_bayes:localhost:3306
    user_awl_sql_username           db_name
    user_awl_sql_password           another_very_secret_password

Next, change its permissions for proper security:

`root `[`#`]`chmod 400 /etc/mail/spamassassin/secrets.cf`

** Note**\
To create a very secret password use `emerge app-admin/makepasswd` and `makepasswd -chars=8`

Now all you have to do is `/etc/init.d/amavisd restart` .

## [Troubleshooting]

### [Amavisd-new]

To troubleshoot Amavisd-new start out by stopping it with `/etc/init.d/amavisd stop` and then start it manually in the foreground with `amavisd debug` and watch it for anomalies in the output.

### [Spamassassin]

To troubleshoot Spamassassin you can filter an email through it with `spamassassin -D < mail` . To ensure that the headers are intact you can move it from another machine with IMAP.

** Note**\
If you need to troubleshoot you have to enable login for the user `amavis` by changing the login shell in [/etc/passwd] to [/bin/bash] .

If you want you can make get the same information and more with Amavisd-new using `amavisd debug-sa` .

### [Repeating tasks after installation]

Some of the activities mentioned in this guide will need to be repeated after upgrades. For instance, the `chown -R amavis:mailusers` will need to be repeated after every update of amavisd-new.

Luckily, Gentoo provides you with the means to perform these steps automatically. In [Hooking in the Emerge Process](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Advanced#Hooking_in_the_emerge_process "Handbook:AMD64/Portage/Advanced"), the Gentoo Handbook explains how to execute tasks after installations of a particular package, like so:

[CODE] **Example bashrc snippet for running the mentioned chown**

    if [ "$" == "amavisd-new" ] &&
       [ "$" == "postinst" ];
    then
      chown -R amavis:mailusers /var/amavis/.maildir
    fi

### [Getting help]

If you need help a good place to go is the amavis-user mailing list. Before postting a question try searching the [Amavis User mailing list archives](http://marc.theaimsgroup.com/?l=amavis-user) . If you find no answer here you can subscribe to the [Amavis User mailing list](https://lists.sourceforge.net/lists/listinfo/amavis-user)

If your question is specific to SpamAssassin, DCC, Razor, or Postfix, please refer to their respective home pages listed below.

## [Resources]

### [For further information]

-   [Amavisd-new INSTALL](http://www.ijs.si/software/amavisd/INSTALL)
-   [Amavisd-new Postfix README](http://www.ijs.si/software/amavisd/README.postfix)
-   [Amavisd-new Policy bank documentation](http://www.ijs.si/software/amavisd/amavisd-new-docs.html#pbanks)
-   [Spamassassin SQL README](http://spamassassin.apache.org/full/3.0.x/dist/sql/README)
-   [Greylisting](http://www.greylisting.org)
-   [Postfix SMTPD_POLICY_README](http://www.postfix.org/FILTER_README.html)
-   [Blocking spammers with Postfix HELO controls](http://www.unixwiz.net/techtips/postfix-HELO.html)
-   [SPF Overview](http://www.linuxjournal.com/article.php?sid=7327)
-   [Jim Seymour\'s Postfix Anti-UCE Cheat Sheet](http://jimsun.linxnet.com/misc/postfix-anti-UCE.txt)

### [General resources]

-   [Spamassassin](http://www.spamassassin.org)
-   [Amavisd-new](http://www.ijs.si/software/amavisd/)
-   [Amavisd-new documentation bits and pieces](http://www.ijs.si/software/amavisd/amavisd-new-docs.html)
-   [Vipuls\'s Razor](http://razor.sourceforge.net/)
-   [Pyzor](http://pyzor.sourceforge.net/)
-   [Distributed Checksum Clearinghouse](http://www.rhyolite.com/anti-spam/dcc/)
-   [Maia Mailguard](http://www.renaissoft.com/projects/maia/)

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Sune Kloppenborg Jeppesen, Jens Hilligsøe, Joshua Saddler**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*