Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/fr "Serveur de messagerie virtuel complet (100% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/it "Server Virtual Mail completo (13% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/hu "Complete Virtual Mail Server (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/ru "Полноценный виртуальный почтовый сервер (21% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/zh-cn "完整虚拟邮箱服务 (8% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/ja "完全な仮想メールサーバ (82% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/ko "Complete Virtual Mail Server/ko (11% translated)")

**Article status**

[[]]This article has some todo items:\

-   [ToDo subpage](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/ToDo "Complete Virtual Mail Server/ToDo")

The purpose of this guide is to **establish a virtual mail system** that can handle multiple domains with a variety of different interface options. This is not intended to be used by the average user who is looking for a mail client, this is a full-scale Mail Transfer Agent (MTA) intended for individuals who are hosting their own domains and/or need to provide support for virtual domains.

This guide uses [Postfix](https://wiki.gentoo.org/wiki/Postfix "Postfix") as the MTA.

By the end of this guide, an easy method to manage a mail server that supports the following features has passed the revue:

-   Web based system administration
-   Unlimited number of domains
-   Virtual mail users without the need for shell accounts
-   Domain (specific) user names
-   Mailbox quotas
-   Web access to email accounts
-   IMAP and (very optional) POP3 support
-   SMTP Authentication for secure relaying
-   SSL for transport layer security
-   Strong SPAM filtering
-   Anti-Virus filtering
-   Log Analysis

The real plus is that all of this is managed by a single database.

## Contents

-   [[1] [Getting started]](#Getting_started)
-   [[2] [Basic setup]](#Basic_setup)
-   [[3] [Enhanced setup]](#Enhanced_setup)
-   [[4] [Anti-Spam measures]](#Anti-Spam_measures)
-   [[5] [Log analyzer]](#Log_analyzer)
-   [[6] [Miscellaneous]](#Miscellaneous)

## [[] Getting started]

[System Setup and Packages](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/System_Setup_and_Packages "Complete Virtual Mail Server/System Setup and Packages")

This section outlines a system setup (a multi-server implementation) as well as the core packages that were used. This is a MUST READ before reading on any further (don\'t worry, it\'s short).

## [[] Basic setup]

[Linux \'vmail\' user](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Linux_vmail_user "Complete Virtual Mail Server/Linux vmail user")

Mailboxes are stored on a normal filesystem and thus needs a user and group for security.

[Admin Support Systems](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Admin_Support_Systems "Complete Virtual Mail Server/Admin Support Systems")

[[[www-apps/postfixadmin]](https://packages.gentoo.org/packages/www-apps/postfixadmin)[]] and [[[www-servers/apache]](https://packages.gentoo.org/packages/www-servers/apache)[]] were key tools in getting through testing and getting this to hang together. While the details of an Apache/PHP setup are not here, there is good information in here all the same.

[Linking Postfix to database backend](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Postfix_to_Database "Complete Virtual Mail Server/Postfix to Database")

[[[mail-mta/postfix]](https://packages.gentoo.org/packages/mail-mta/postfix)[]] will be coupled to a database backend allowing virtual users on multiple domains.

[Linking Dovecot to database backend](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Dovecot_to_Database "Complete Virtual Mail Server/Dovecot to Database")

    ** Important**\
    This setup is for the dovecot route. It is mutually exclusive with *Linking Courier-imap to database backend*.
    :::

<!-- -->

[Linking Courier-imap to database backend](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Courier-IMAP_to_Database "Complete Virtual Mail Server/Courier-IMAP to Database")

    ** Important**\
    This setup is for the courier route. It is mutually exclusive with *Linking Dovecot to database backend*.
    :::

## [[] Enhanced setup]

[SMTP Authentication - Dovecot route](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/SMTP_Auth_Dovecot "Complete Virtual Mail Server/SMTP Auth Dovecot")

    ** Important**\
    This setup is for the dovecot route. It is mutually exclusive with *SMTP Authentication - Courier route*.
    :::

<!-- -->

[SMTP Authentication - Courier route](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/SMTP_Authentication "Complete Virtual Mail Server/SMTP Authentication")

    ** Important**\
    This setup is for the courier route. It is mutually exclusive with *SMTP Authentication - Dovecot route*.
    :::

[Web Access](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Web_Access "Complete Virtual Mail Server/Web Access")

Now that a basic mailserver has been setup, web access can be both useful and helpful during testing.

[SSL Certificates](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/SSL_Certificates "Complete Virtual Mail Server/SSL Certificates")

Securing the mail server with SSL certificates.

[DKIM, SPF and DMARC](https://wiki.gentoo.org/wiki/Postfix/DKIM "Postfix/DKIM")

DKIM will sign all outgoing messages with verification keys to prevent ending up in the junk box. SPF will ensure that the only verified servers/IP addresses may send mail from a given domain. DMARC ensures that both DKIM and SPF are properly enforced.

[Refining the Setup](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/Postfix_additions "Complete Virtual Mail Server/Postfix additions")

Using default Postfix configuration options, the server gets some performance tweaks and security settings.

## [[] Anti-Spam measures]

[Amavisd, Spam-Assassin and ClamAV](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/amavisd_spamassassin_clamav "Complete Virtual Mail Server/amavisd spamassassin clamav")

Defending against spam using Amavis, Spam-assassin and ClamAV for virus protection.

## [[] Log analyzer]

[Logging mail traffic with AWStats](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/awstats "Complete Virtual Mail Server/awstats")

Always important is monitoring. To do so AWStats is used to get a useful overview of passed messages.

## [[] Miscellaneous]

[POP3 protocol](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/POP3 "Complete Virtual Mail Server/POP3")