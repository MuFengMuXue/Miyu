This guide is for getting basic mail server working in small amount of time. You can always add more features later. This guide uses postfix MTA, dovecot IMAP, POP, SASL and SquirrelMail webmail.

## Contents

-   [[1] [Postfix MTA]](#Postfix_MTA)
-   [[2] [dovecot IMAP, POP & SASL]](#dovecot_IMAP.2C_POP_.26_SASL)
-   [[3] [SquirrelMail webmail]](#SquirrelMail_webmail)
-   [[4] [Troubleshooting]](#Troubleshooting)

## [Postfix MTA]

Install [[[mail-mta/postfix]](https://packages.gentoo.org/packages/mail-mta/postfix)[]]. Enable *dovecot-sasl*, *ipv6*, *pam*, *berkdb* and *ssl* USE flags. See also the [Postfix](https://wiki.gentoo.org/wiki/Postfix "Postfix") article.

`root `[`#`]`emerge --ask postfix`

If this is a new install, the previous command should uninstall [[[mail-mta/ssmtp]](https://packages.gentoo.org/packages/mail-mta/ssmtp)[]]. If it fails to uninstall [[[mail-mta/ssmtp]](https://packages.gentoo.org/packages/mail-mta/ssmtp)[]], you need to manually uninstall it, because it blocks Postfix:

`root `[`#`]`emerge --ask -C ssmtp`

\
Configure Postfix.

[FILE] **`/etc/postfix/main.cf`**

    # basic config
    myhostname = example.com
    mydomain = example.com
    myorigin = example.com
    inet_interfaces = all
    mynetworks_style = host
    mydestination = $myhostname, localhost, $mydomain, mail.$mydomain, www.$mydomain
    home_mailbox = .maildir/

    # sasl config
    smtpd_sasl_type = dovecot
    smtpd_sasl_path = private/auth
    smtpd_sasl_auth_enable = yes
    smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination

Edit aliases to redirect root mails to webmaster:

[FILE] **`/etc/mail/aliases`**

    ...
    root: webmaster
    ...

Generate aliases database:

`root `[`#`]`newaliases`

Redirect root mails to webmaster:

[FILE] **`/root/.forward`**

    ...
    webmaster@localhost
    ...

Check for errors:

`root `[`#`]`postfix check`

Start Postfix:

`root `[`#`]`/etc/init.d/postfix start`

Check [/var/log/mail.log] for errors:

`root `[`#`]`cat /var/log/mail.log`

## [][dovecot IMAP, POP & SASL]

Install [[[net-mail/dovecot]](https://packages.gentoo.org/packages/net-mail/dovecot)[]]. Enable USE flags : bzip2 ipv6 maildir pam ssl zlib

`root `[`#`]`emerge --ask dovecot`

Configure dovecot:

[FILE] **`/etc/dovecot/dovecot.conf`**

    protocols = imap pop3

    # sasl config
    service auth
    }

Start dovecot:

`root `[`#`]`/etc/init.d/dovecot start`

## [SquirrelMail webmail]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Simple_mail_server_with_webmail&action=edit).

Change dir to webserver root:

`user `[`$`]`cd /home/webmaster/htdocs`

Unpack squirrelmail:

`user `[`$`]`tar xjf squirrelmail-webmail-1.4.22.tar.bz2`

Configure squirrelmail:

`user `[`$`]`cd squirrelmail-webmail-1.4.22/config `

`user `[`$`]`cp config_default.php config.php`

[FILE] **`config.php`**

    $data_dir = '/home/webmaster/.squirrelmail/data/';
    $attachment_dir = '/home/webmaster/.squirrelmail/attach/';
    $domain = 'example.com';

Create data dirs and set permissions:

`user `[`$`]`mkdir -p /home/webmaster/.squirrelmail/data/ `

`user `[`$`]`mkdir -p /home/webmaster/.squirrelmail/attach/`

`root `[`#`]`chown -R webmaster:lighttpd /home/webmaster/.squirrelmail/`

`user `[`$`]`chmod -R 770 /home/webmaster/.squirrelmail/`

Debug squirrelmail by opening url: [http://example.com/squirrelmail-webmail-1.4.22/src/configtest.php](http://example.com/squirrelmail-webmail-1.4.22/src/configtest.php)

You can access webmail by opening url: [http://example.com/squirrelmail-webmail-1.4.22/](http://example.com/squirrelmail-webmail-1.4.22/).

Everything should be working now.

## [Troubleshooting]

Check your error log (mine is /var/log/messages).

If you get this error and can\'t login to squirrelmail: \"auth: Fatal: sql: driver not set in configuration file /etc/dovecot/dovecot-sql.conf.ext\"

then try these changes and restart dovecot:

[FILE] **`/etc/dovecot/conf.d/10-auth.conf`**

    # Ensure that this line is commented out:
    #!include auth-sql.conf.ext