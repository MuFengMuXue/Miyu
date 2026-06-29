This document details how to create a mail hosting system based upon netqmail, vpopmail, courier-imap, mysql, and horde\'s imp.

[] This article is a **work in progress**; treat its contents with caution - [Vapier](https://wiki.gentoo.org/wiki/User:Vapier "User:Vapier") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:Vapier&action=edit&redlink=1 "User talk:Vapier (page does not exist)") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/Vapier "Special:Contributions/Vapier")).

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [netqmail (talking to myself)]](#netqmail_.28talking_to_myself.29)
-   [[3] [vpopmail]](#vpopmail)
-   [[4] [Courier POP/IMAP]](#Courier_POP.2FIMAP)
-   [[5] [netqmail (talking to the world)]](#netqmail_.28talking_to_the_world.29)
-   [[6] [Horde / IMP Webmail Client]](#Horde_.2F_IMP_Webmail_Client)
-   [[7] [Extra packages]](#Extra_packages)
    -   [[7.1] [qmailadmin]](#qmailadmin)
    -   [[7.2] [qmHandle]](#qmHandle)
    -   [[7.3] [horde add ons]](#horde_add_ons)
    -   [[7.4] [ucspi-tcp]](#ucspi-tcp)
    -   [[7.5] [qmail-scanner]](#qmail-scanner)
    -   [[7.6] [SpamAssassin]](#SpamAssassin)
    -   [[7.7] [Clam AntiVirus]](#Clam_AntiVirus)
    -   [[7.8] [Spamdyke]](#Spamdyke)
-   [[8] [Final Notes]](#Final_Notes)

## [Introduction]

Whether you\'re providing e-mail for just system daemons, a single server, a domain, or for many virtual domains, netqmail can easily be setup to handle your needs. This guide will help you setup netqmail for all of these scenarios with a focus on remote access and encrypted communications the whole way through.

Specifically, the packages this guide will help you with are netqmail, courier-imap, vpopmail, and horde/imp. These core packages will also bring in daemontools, ucspi-tcp, mysql, apache, and mod_php. netqmail provides the core MTA functions, courier-imap provides remote retrieval services, vpopmail provides virtual domain management, and horde/imp provides webmail access.

Before emerging anything, you will need the following USE variables enabled. If you\'ve already emerged any of these packages, you may have to re-emerge them. `USE="maildir ssl imap mysql"` . Additionally, if you want to use horde/imp for your webmail then you will need `USE="nls"` before emerging mod_php.

\

** Note**\
This guide is written in steps. If at anytime you feel your setup is \'complete\', you do not need to continue.

The last step of course is to commit yourself to the netqmail system. There are many other packages with which you could build your e-mail system. Now is the time to research and decide that netqmail is for you. We have another [lovely guide](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server "Complete Virtual Mail Server") centered around virtual mail hosting that discusses mail server infrastructure. It\'s up to you to choose the best solution for yourself; it is up to us to show you how to use netqmail.

## [][netqmail (talking to myself)]

`root `[`#`]`emerge --ask mail-mta/netqmail`

** Important**\
This guide is designed around netqmail-1.05-r4 or later. Will it work with earlier versions? Maybe. Should you upgrade? Yes, if you want to be sure this guide will work.

** Warning**\
If you get a message like `the virtual/mta package conflicts with another package` then you need to make sure to unmerge the other MTA on your system. To figure out which package that is, just run `emerge netqmail -p` .

Emerging netqmail will also emerge ucspi-tcp and daemontools. You can read up on [ucspi-tcp](http://cr.yp.to/ucspi-tcp.html) and on [daemontools](http://cr.yp.to/daemontools.html) if you like. Basically, daemontools is responsible for managing netqmail as a service while ucspi-tcp is responsible for managing the incoming TCP connections to the netqmail service.

First we have a few post-install configuration steps.

`root `[`#`]`nano /var/qmail/control/servercert.cnf `

`root `[`#`]`emerge --config netqmail`

The design of netqmail has been completely around the focus of security. To this end, e-mail is never sent to the user \'root\'. So now you have to select a user on your machine to receive mail that would normally be destined for \'root\'. From now on in this guide, I will refer to that user as I have it in my setup, \'vapier\'.

`root `[`#`]`cd /var/qmail/alias `

`root `[`#`]`echo vapier > .qmail-root `

`root `[`#`]`echo vapier > .qmail-postmaster `

`root `[`#`]`echo vapier > .qmail-mailer-daemon`

Now we want to get the netqmail delivery service up and running.

`root `[`#`]`rc-update add svscan default `

`root `[`#`]`/etc/init.d/svscan start `

`root `[`#`]`cd /service `

`root `[`#`]`ln -s /var/qmail/supervise/qmail-send qmail-send`

We want to make sure netqmail is working correctly, so here\'s a quick test.

`root `[`#`]`emerge mutt`

`root `[`#`]`ssh vapier@localhost`

`vapier $``maildirmake .maildir `

`vapier $``qmail-inject root << EOF`\

test root e-mail!\
EOF

`vapier $``qmail-inject postmaster << EOF`\

test postmaster e-mail!\
EOF

`vapier $``qmail-inject vapier << EOF`\

test vapier e-mail!\
EOF

`vapier $``mutt`

You should now have 3 e-mails in your inbox.

And that\'s all! Now you have a mail system that will handle mail for your local machine and the system daemons/users who utilize it.

** Warning**\
If you don\'t receive any mail or you see weird errors in the log files (check [/var/log/qmail/] ) involving \'localhost.localhost\', then that means your domain/dns information is not setup properly. By default, netqmail utilizes the output of `hostname --fqdn` . If, on your machine, this returns \'localhost\', then check your [/etc/conf.d/hostname] , [/etc/hosts] , and your DNS to make sure everything is correct. Once you have, edit the configuration files in [/var/qmail/control/] . Use the example setups that follow if you need some more help.

`root `[`#`]`hostname --fqdn`

    wh0rd.org

`root `[`#`]`cat me`

    wh0rd.org

`root `[`#`]`cat defaultdomain`

    wh0rd.org

`root `[`#`]`cat plusdomain`

    wh0rd.org

`root `[`#`]`cat locals`

    wh0rd.org

`root `[`#`]`cat rcpthosts`

    wh0rd.org

Same but for a 3rd level domain:

`root `[`#`]`hostname --fqdn`

    mail.wh0rd.org

`root `[`#`]`cat me`

    mail.wh0rd.org

`root `[`#`]`cat defaultdomain`

    wh0rd.org

`root `[`#`]`cat plusdomain`

    wh0rd.org

`root `[`#`]`cat locals`

    mail.wh0rd.org

`root `[`#`]`cat rcpthosts`

    mail.wh0rd.org

## [vpopmail]

`root `[`#`]`emerge --ask vpopmail`

** Important**\
This guide is designed around vpopmail-5.4.6 or later. Will it work with earlier versions? Maybe. Should you upgrade? Yes, if you want to be sure this guide will work.

vpopmail takes a little bit more effort to setup than the previous packages. Since vpopmail runs off of mysql, we\'ll have to make sure that it\'s up and running first. Then we can setup the vpopmail database and move on. Before you do this step, you should make sure you\'ve already emerged and setup mysql properly. Note that the password I will use for the vpopmail database is \'vpoppw\', you however should pick a different one.

`root `[`#`]`rc-update add mysql default`

If you just emerged mysql for the first time, make sure you run the ebuild \<mysql.ebuild\> config command and follow the directions before starting the mysql server.

\

`root `[`#`]`/etc/init.d/mysql start `

`root `[`#`]`nano /etc/vpopmail.conf`

Change the password from \'secret\' to \'vpoppw\'.

`root `[`#`]`mysql -p << EOF`\

create database vpopmail;\
use mysql;\
grant select, insert, update, delete, create, drop on vpopmail.\* to vpopmail@localhost identified by \'vpoppw\';\
flush privileges;\

EOF

The following steps may or may not be needed, but we run them just to be sure.

`root `[`#`]`chown root:vpopmail /etc/vpopmail.conf `

`root `[`#`]`chmod 640 /etc/vpopmail.conf `

`root `[`#`]`chown root:vpopmail /var/vpopmail/bin/vchkpw `

`root `[`#`]`chmod 4711 /var/vpopmail/bin/vchkpw`

** Warning**\
If you experience permission problems with mysql/vpopmail, you may want to try restarting mysql. Just run `/etc/init.d/mysql restart` .

At this point in time, vpopmail is ready to roll. In this guide, we will be providing virtual hosting for the domain \'wh0rd.org\'. This means we need to tell vpopmail about this domain we want it to host for us. We\'ll also quickly add an user account for \'vapier\' while we\'re here.

You only have to do this if the vadddomain step below results in \"command not found\":

`root `[`#`]`source /etc/profile`

While debugging vpopmail, you may want to consult the logs:

`root `[`#`]`mysql -u vpopmail -p`

`mysql>``select * from vpopmail.vlog;`

`root `[`#`]`vadddomain wh0rd.org postpass`

Now quickly verify the domain is setup properly.

`root `[`#`]`` printf "postmaster@wh0rd.org\0postpass\0blah\0" | vchkpw `which id` 3<&0 ``

    uid=89(vpopmail) gid=89(vpopmail) groups=0(root)

If you don\'t see something similar to above, then permissions somewhere are incorrect.

`root `[`#`]`vadduser vapier@wh0rd.org vappw`

Every domain that vpopmail creates comes with a \'postmaster\' account. Here we told vpopmail that the password for the postmaster account is \'postpass\'. Before vpopmail can be truly useful, we\'ll need to be able to receive mail via courier and send mail via netqmail and SMTP.

## [][Courier POP/IMAP]

`root `[`#`]`emerge --ask net-mail/courier-imap`

\

** Important**\
You must emerge courier-imap after vpopmail. That way the authvchkpw module will be built.

** Important**\
This guide is designed around net-mail/courier-imap-3.0.7 or later. Will it work with earlier versions? Maybe. Should you upgrade? Yes, if you want to be sure this guide will work.

Now for the common post-install configuration steps. These steps are only needed if you wish to run SSL encrypted communications (which you should !). Otherwise you can skip to the last two steps in the two following code listings, removing the \'-ssl\' from the init script name each time.

\

`root `[`#`]`nano /etc/courier/authlib/authdaemonrc`

Set the authmodulelist variable to only contain \"authvchkpw\".

`root `[`#`]`cd /etc/courier-imap `

`root `[`#`]`nano pop3d.cnf`

Edit the \[ req_dn \] section.

`root `[`#`]`mkpop3dcert `

`root `[`#`]`rc-update add courier-pop3d-ssl default `

`root `[`#`]`/etc/init.d/courier-pop3d-ssl start`

`root `[`#`]`cd /etc/courier-imap `

`root `[`#`]`nano imapd.cnf`

Edit the \[ req_dn \] section.

`root `[`#`]`mkimapdcert `

`root `[`#`]`rc-update add courier-imapd-ssl default `

`root `[`#`]`/etc/init.d/courier-imapd-ssl start`

Your mail client should now be able to login to the host running courier and retrieve mail for the virtual host. In my case, I am now able to login with the username \'vapier@wh0rd.org\' and password \'vappw\'.

If you receive similar errors in the log files: imapd-ssl: LOGIN FAILED, user=vapier@wh0rd.org , ip=\[::ffff:123.123.123.123\] authdaemond: file not found

`root `[`#`]`nano /etc/courier/authlib/authdaemonrc`

Set the authmodulelist variable to only contain \"authmysql\".

`root `[`#`]`nano /etc/courier/authlib/authmysqlrc`

If the file doesn\'t exist, use authmysqlrc.dist as a template. Set the MYSQL_SERVER, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_SOCKET, MYSQL_PORT, MYSQL_DATABASE, DEFAULT_DOMAIN variables to your configuration. Make sure that you have this line \"MYSQL_CRYPT_PWFIELD crypt\"

Set the MYSQL_SELECT_CLAUSE variable (somewhere at the end of the file)

MYSQL_SELECT_CLAUSE SELECT CONCAT(pw_name, \'@\', pw_domain) AS username, pw_passwd AS cryptpw, *AS clearpw, \'89\' AS uid,\'89\' AS gid, pw_dir AS home, \'.maildir\' AS maildir, pw_shell AS quota, pw_gecos AS fullname, \'disablewebmail=0,disablepop3=0,disableimap=0\' AS options FROM vpopmail WHERE pw_name = \'\$(local_part)\' AND pw_domain = \'\$(domain)\'*

`root `[`#`]`/etc/init.d/courier-authlib restart`

For MS Outlook Clients, set the DHE key length \> 1024, or else Outlook won\'t connect to your IMAP server ([https://technet.microsoft.com/library/security/MS15-055](https://technet.microsoft.com/library/security/MS15-055)). On my example, I\'ve set it to 2048

`root `[`#`]`nano /usr/sbin/mkdhparams`

BITS=2048

`root `[`#`]`/usr/sbin/mkdhparams`

## [][netqmail (talking to the world)]

Let\'s get SMTP up and running while making sure we don\'t create another spam hole for people to abuse.

`root `[`#`]`cd /var/qmail/control/ `

`root `[`#`]`nano conf-smtpd`

Uncomment the SMTP-AUTH variables and set QMAIL_SMTP_CHECKPASSWORD to /var/vpopmail/bin/vchkpw.

`root `[`#`]`nano servercert.cnf`

Edit the \[ req_dn \] section.

`root `[`#`]`mkservercert `

`root `[`#`]`cd /service `

`root `[`#`]`ln -s /var/qmail/supervise/qmail-smtpd qmail-smtpd `

`root `[`#`]`/etc/init.d/svscan restart`

Assuming you haven\'t tweaked the netqmail control files at all, netqmail will now accept mail for the wh0rd.org virtual domain and for users of the local machine. Furthermore, netqmail will relay mail for anyone who sends via 127.0.0.1 and for anyone who is able to authenticate with vpopmail. When you setup your mail client to send mail, make sure you select options like \'Server requires authentication\'. In my case, I set the user as \'vapier@wh0rd.org\' and my password as \'vappw\'. The last detail is to make sure you tell your mail client to use SSL/TLS for SMTP communication. netqmail will not let you authenticate if the session is not encrypted.

If you receive the error message

imapd-ssl: Unexpected SSL connection shutdown.

Please try to increase the Softlimit

`root `[`#`]`nano /var/qmail/control/conf-common`

Change the SOFTLIMIT_OPTS line to SOFTLIMIT_OPTS=\"-m 32000000\"

`root `[`#`]`/etc/init.d/svscan restart`

## [][Horde / IMP Webmail Client]

Although there are plenty of webmail clients out there (and you\'re free to use any of them), I prefer the [IMP Webmail Client](http://www.horde.org/imp/) that is part of the Horde framework. The biggest reason is that Horde can simply provide Webmail access, or you can easily add other components to handle Address Books, Calendars, Tasks, etc\... If this hasn\'t convinced you yet, then perhaps you need to read up on [Horde](http://www.horde.org/) for yourself.

On to the good stuff! We need to emerge IMP now.

`root `[`#`]`emerge --ask horde-imp`

Now we setup IMP real quick.

`root `[`#`]`cd /var/www/localhost/htdocs/horde/imp/config/ `

`root `[`#`]`nano servers.php`

Edit the \$servers\[\'imap\'\] array:

[FILE] **`servers.php`Editing imap info**

    $servers['imap'] = array(
      'name' => 'wh0rd.org',
      'server' => 'localhost',
      'protocol' => 'imap/ssl/novalidate-cert',
      'port' => 993,
      'folders' => '',
      'namespace' => 'INBOX.',
      'maildomain' => 'wh0rd.org',
      'smtphost' => 'localhost',
      'realm' => '',
      'preferred' => ''
    );

Finally, we bring up apache so we can start using webmail.

`root `[`#`]`nano /etc/conf.d/apache2`

Uncomment APACHE2_OPTS=\"-D SSL -D PHP5\".

`root `[`#`]`rc-update add apache2 default `

`root `[`#`]`/etc/init.d/apache2 start`

** Warning**\
You should really look into forcing https on users of horde. This isn\'t a trivial issue, but you should look into it for the sake of security.

To test out the new IMP setup, launch a web browser and visit [http://localhost/horde/](http://localhost/horde/) (or change localhost with the server you\'re setting this up on). You should see the Horde welcome page where you can login. Again, in my setup, I simply login with \'vapier@wh0rd.org\' and \'vappw\' as my username and password.

At this point, Horde and IMP are all setup. You should, however, go back through the config directories and tweak each to your heart\'s content.

## [Extra packages]

### [qmailadmin]

The first package I would suggest you look into is [qmailadmin](http://www.inter7.com/qmailadmin.html) . It\'s a web based interface for managing virtual domains. Simply `emerge net-mail/qmailadmin` and then point your webbrowser to [http://localhost/cgi-bin/qmailadmin](http://localhost/cgi-bin/qmailadmin) in order to use it. Makes life a lot easier.

### [qmHandle]

If you run into problems with netqmail queues and have a hard time debugging the situation, you may want to look into [qmHandle](http://qmhandle.sourceforge.net/) . It\'s a simple perl program which allows you to view and manage the netqmail message queue. Again, all you need to do is `emerge net-mail/qmhandle` .

### [horde add ons]

I would highly recommend looking into the many other Horde applications. The [Turba](http://www.horde.org/turba/) , [Kronolith](http://www.horde.org/kronolith/) , and [Nag](http://www.horde.org/nag/) applications complement IMP very well for instance. Their configuration is similar to that of IMP, so you should have no trouble setting them up. Just remember to edit registry.php in the horde config directory so the new applications show up at the bottom of the horde website.

### [ucspi-tcp]

netqmail utilizes ucspi-tcp to handle the incoming connections for netqmail. If you wish to customize these filtering rules, then see the configuration files in [/etc/tcprules.d/] (older versions put files in [/etc] ). There you\'ll find two files for each service, the configuration file (i.e. tcp.qmail-smtp) and the compiled version of this file that ucspi-tcp uses (i.e. tcp.qmail-smtp.cdb). Whenever you update the configuration file, you\'ll have to rebuild the binary version of it. Just run `tcprules tcp.qmail-smtp.cdb tcp.qmail-smtp.tmp < tcp.qmail-smtp` . Every time a connection is made to the netqmail service, the compiled rules file is re-read, so there\'s no need to restart the service.

### [qmail-scanner]

If you wish to do content filtering on your mail server (spam and virus), then you\'ll need to use a different queuing program than the default one. One good program for doing so is [qmail-scanner](http://qmail-scanner.sourceforge.net/) . Just `emerge qmail-scanner` and edit the [/etc/tcprules.d/tcp.qmail-smtp] file.

** Important**\
The build process of qmail-scanner is quite ugly. In order to support packages, they must already be on your system. This means you will have to emerge SpamAssassin and/or Clam AntiVirus before you emerge qmail-scanner. See the relevant following sections for more information.

`root `[`#`]`cd /etc/tcprules.d/ `

`root `[`#`]`nano tcp.qmail-smtp`

Add QMAILQUEUE=\"/var/qmail/bin/qmail-scanner-queue\" to the catchall allow rule.

`root `[`#`]`tcprules tcp.qmail-smtp.cdb tcp.qmail-smtp.tmp < tcp.qmail-smtp`

See the following sections for setting up spam and virus filtering. You may want to set a few custom options by editing [/var/qmail/bin/qmail-scanner-queue.pl] .

### [SpamAssassin]

One of the best Open Source spam filters out there is [SpamAssassin](http://www.spamassassin.org/) . Just `emerge mail-filter/spamassassin` to install. The package comes in two flavors, a command line version and a client/server version. For servers that will be handling a small amount of mail, running with the command line version is OK, but for anyone whose server will be handling appreciative loads should utilize the client/server version.

`root `[`#`]`nano /etc/mail/spamassassin/local.cf`

At the bare minimum, add these options:

[FILE] **`local.cf`Minimum settings**

    required_hits 6
    skip_rbl_checks 1

`root `[`#`]`rc-update add spamd default `

`root `[`#`]`/etc/init.d/spamd start `

`root `[`#`]`nano /var/qmail/bin/qmail-scanner-queue.pl`

Make sure the \$spamc_binary variable is set to \'/usr/bin/spamc\'. If it is set to *, then see the note below.*

\

** Important**\
If you did not have SpamAssassin on your system before you emerged qmail-scanner, you will have to re-emerge qmail-scanner now. Its build process is pretty ugly and will only add in features for packages it detects on the system at build time.

At this point, incoming mail should be sent through qmail-scanner which will run it through SpamAssassin for you.

### [Clam AntiVirus]

Like SpamAssassin, [Clam AntiVirus](http://www.clamav.net/) comes in two flavors. I\'ll give you a quick run down on how to quickly setup the client/server version. First, just `emerge app-antivirus/clamav` .

`root `[`#`]`nano /etc/conf.d/clamd`

Set START_CLAMD=yes.

`root `[`#`]`nano /etc/clamav.conf`

Setup stuff the way you want it.

`root `[`#`]`rc-update add clamd default `

`root `[`#`]`/etc/init.d/clamd start `

`root `[`#`]`nano /var/qmail/bin/qmail-scanner-queue.pl`

Make sure the \$clamscan_binary variable is set to \'/usr/bin/clamscan\'. If it is set to *, then see the note below.*

`root `[`#`]`nano /var/qmail/control/conf-common`

If ClamAV reports memory problems or /var/log/qmail/qmail-send/current reports something like \"Can\'t load \'/usr/lib/perl5/5.8.5/x86_64-linux/auto/Sys/Syslog/Syslog.so\' for module Sys::Syslog: /usr/lib/perl5/5.8.5/x86_64-linux/auto/Sys/Syslog/Syslog.so: failed to map segment from shared object: Cannot allocate memory at /usr/lib/perl5/5.8.5/x86_64-linux/DynaLoader.pm line 230. \" try rasing the softlimit.

If /var/log/qmail/qmail-smtp/current reports clamdscan: corrupt or unknown clamd scanner error or memory/resource/perms problem - exit status 512/2 and ClamAV (/var/log/clamav/clamd.log) claims permission problems -\> WARNING: lstat() failed on: /var/spool/qscan/tmp/ . Check owner of /var/spool/qscan/tmp/ .

`root `[`#`]`ls -al /var/spool/qscan/tmp/ `

total 8 drwxr-x\-\-- 2 qscand root 4096 Jan 18 00:31 .

drwxr-xr-x 6 qscand qscand 4096 Jan 18 00:09 ..

check clamav User line

`root `[`#`]`vi /etc/clamd.conf`

adapt User line

in my case I replaced \"User clamav\" with \"User qscand\"

** Important**\
If you did not have Clam AntiVirus on your system before you emerged qmail-scanner, you will have to re-emerge qmail-scanner now. Its build process is pretty ugly and will only add in features for packages it detects on the system at build time.

At this point, incoming mail should be sent through qmail-scanner which will run it through Clam AntiVirus for you.

### [Spamdyke]

For greylisting, rdns checks, sender blacklists, whitelists, and many more features

`root `[`#`]`emerge spamdyke`

`root `[`#`]`vi /var/qmail/control/conf-smtpd `

add these two lines

SPAMDYKE_OPTIONS=\"\--hostname \'\$HOSTNAME\' \--config-file /etc/spamdyke/spamdyke.conf\"

QMAIL_SMTP_PRE=\"\$ /usr/bin/spamdyke \$SPAMDYKE_OPTIONS\"

`root `[`#`]`/etc/init.d/svscan restart`

`root `[`#`]`vi /etc/spamdyke/spamdyke.conf`

adapt your configuration with your needed features.

my example configuration:

`root `[`#`]`cat /etc/spamdyke/spamdyke.conf`

    # Configuration option for spamdyke
    tls-certificate-file=/var/qmail/control/clientcert.pem
    graylist-level=always-create-dir
    graylist-dir=/var/tmp/spamdyke/graylist
    reject-empty-rdns
    reject-unresolvable-rdns
    dns-blacklist-entry=zen.spamhaus.org
    local-domains-file=/var/qmail/control/rcpthosts
    log-level=verbose
    reject-missing-sender-mx

Check the spamdyke website for more information [http://www.spamdyke.org](http://www.spamdyke.org)

## [Final Notes]

I have no final notes other than if you experience any troubles with the guide, use the [talk page](https://wiki.gentoo.org/wiki/Talk:Virtual_mail_hosting_with_qmail "Talk:Virtual mail hosting with qmail") for this article. If you have some interesting bits you think would enhance this guide, by all means suggest them or make the changes. I love netqmail and would gladly add stuff that could possibly enhance a user\'s experience with the mta.

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **vapier, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*