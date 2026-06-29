**Resources**

[[]][Home](http://netqmail.org)

[[]][Home](http://cr.yp.to/qmail.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Qmail "wikipedia:Qmail")

**qmail** is a fast, popular [Mail Transfer Agent](https://wiki.gentoo.org/wiki/Category:Mail_Transfer_Agents "Category:Mail Transfer Agents") (MTA).

## Contents

-   [[1] [Pre-installation]](#Pre-installation)
-   [[2] [Installation]](#Installation)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Setting up non-root account for mail]](#Setting_up_non-root_account_for_mail)
    -   [[3.2] [Fully Qualified Domain Name (FQDN)]](#Fully_Qualified_Domain_Name_.28FQDN.29)
    -   [[3.3] [Files for a 2nd level domain]](#Files_for_a_2nd_level_domain)
    -   [[3.4] [Files for a 3rd level domain]](#Files_for_a_3rd_level_domain)
    -   [[3.5] [Creating Properly Signed Certificates]](#Creating_Properly_Signed_Certificates)
    -   [[3.6] [Start qmail and add it to the default run level]](#Start_qmail_and_add_it_to_the_default_run_level)
-   [[4] [vpopmail]](#vpopmail)
-   [[5] [dovecot]](#dovecot)

## [Pre-installation]

As only one MTA can be installed at the same time on a system, it might be required to deselect an installed MTA. The package manager will report a block when another MTA is still installed. For example, a previously selected [[[mail-mta/ssmtp]](https://packages.gentoo.org/packages/mail-mta/ssmtp)[]] can be marked as removable with this command:

`root `[`#`]`emerge --deselect mail-mta/ssmtp`

## [Installation]

[[[mail-mta/netqmail]](https://packages.gentoo.org/packages/mail-mta/netqmail)[]] has several USE flags that may be desired for certain bigger setups. As this article aims at installing and configuring a *basic* netqmail setup, adding qmail plugin support with qmail-spp and ucspi-tcp support is necessary.

`root `[`#`]`echo "mail-mta/netqmail qmail-spp" >> /etc/portage/package.use `

`root `[`#`]`echo "sys-apps/ucspi-tcp qmail-spp" >> /etc/portage/package.use`

`root `[`#`]`emerge --ask netqmail`

## [Configuration]

The default 16 MiB of memory for qmail is a little sparse. Update the memory to 32 MiB to avoid memory related errors.

`root `[`#`]`sed -i 's/16000000/32000000/' /var/qmail/control/conf-common`

`root `[`#`]`emerge --ask --config netqmail`

#### [Setting up non-root account for mail]

The design of qmail has been completely around the focus of security. To this end, e-mail is never sent to the user *root*. Select a user on the machine to receive mail that would normally be destined for *root*. The remainder of this guide will that user as *myusername*.

[FILE] **`/var/qmail/alias/.qmail-root`qmail-root**

    myusername

[FILE] **`/var/qmail/alias/.qmail-postmaster`qmail-postmaster**

    myusername

[FILE] **`/var/qmail/alias/.qmail-mailer-daemon`qmail-mailer-daemon**

    myusername

Or to send this email elsewhere, simply put the full address in:

[FILE] **`/var/qmail/alias/.qmail-root`qmail-root**

    myusername@gmail.com

[FILE] **`/var/qmail/alias/.qmail-postmaster`qmail-postmaster**

    myusername@gmail.com

[FILE] **`/var/qmail/alias/.qmail-mailer-daemon`qmail-mailer-daemon**

    myusername@gmail.com

#### [][Fully Qualified Domain Name (FQDN)]

Though not entirely related, for an MTA to function properly, it is imperative that its hostname is set up correctly. Under Gentoo [/etc/conf.d/hostname] and [/etc/conf.d/net] are the files responsible for this. In this example, the mail server is named *foo* on the domain *example.com*.

[FILE] **`/etc/conf.d/net`Setup domain name**

    dns_domain_lo="example.com"

[FILE] **`/etc/conf.d/hostname`Setup hostname**

    hostname="foo"

** Note**\
Do not use *mail.example.com* just because it may be externally known as such. Use the actual name of the system.

Verifying that the FQDN is setup properly for the domain.

#### [Files for a 2nd level domain]

`user `[`$`]`cd /var/qmail/control/`

`user `[`$`]`hostname --fqdn`

domain.com

`user `[`$`]`cat me`

domain.com

`user `[`$`]`cat defaultdomain`

domain.com

`user `[`$`]`cat plusdomain`

domain.com

`user `[`$`]`cat locals`

domain.com

`user `[`$`]`cat rcpthosts`

domain.com

#### [Files for a 3rd level domain]

`user `[`$`]`cd /var/qmail/control/`

`user `[`$`]`hostname --fqdn`

foo.domain.com

`user `[`$`]`cat me`

foo.domain.com

`user `[`$`]`cat defaultdomain`

domain.com

`user `[`$`]`cat plusdomain`

domain.com

`user `[`$`]`cat locals`

domain.com

`user `[`$`]`cat rcpthosts`

foo.domain.com

### [Creating Properly Signed Certificates]

Move to the qmail control directory:

`root `[`#`]`cd /var/qmail/control/`

Upgrade the Cert Info to create a 2048bit key:

`root `[`#`]`sed -i 's/1024/2048/' /var/qmail/control/servercert.cnf`

Update the Cert Info with information pertinent to this host. CN is the fully qualified domain name ie. foo.domain.com:

[FILE] **`/var/qmail/control/servercert.cnf`Be certain this is the correct CN**

    CN=foo.domain.com

create the pem files and key:

`root `[`#`]`openssl req -new -nodes -out req.pem -config /var/qmail/control/servercert.cnf -keyout /var/qmail/control/servercert.pem`

Get the contents of the request pem file:

`root `[`#`]`cat /var/qmail/control/req.pem`

Send req.pem to a CA(ie godaddy/Starfield, Versign, etc.) to obtain signed_req.pem:

`root `[`#`]`cat myserver.domain.com.crt sf_bundle.crt >> servercert.pem `

`root `[`#`]`awk '/BEGIN PRIVATE KEY/,/END PRIVATE KEY/' servercert.pem > myserver.domain.com.key`

Alternatively, obtain a key from [Let\'s_Encrypt](https://wiki.gentoo.org/wiki/Let%27s_Encrypt "Let's Encrypt")

### [Start qmail and add it to the default run level]

Run the init scripts and setup supervisor links for qmail:

`root `[`#`]`ln -s /var/qmail/supervise/qmail-send /service/qmail-send `

`root `[`#`]`ln -s /var/qmail/supervise/qmail-smtpd /service/qmail-smtpd `

start and add netqmail to the default run level:

`root `[`#`]`/etc/init.d/svscan start `

`root `[`#`]`rc-update add svscan default `

## [vpopmail]

vpopmail will handle virtual domains, adding, deleting mail domains, accounts, storing passwords etc. vpopmail uses mysql in this setup. Please configure [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB") or [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") to follow these instructions.

First we need to tell qmail to use vpopmail when checking smtp passwords:

[FILE] **`/var/qmail/control/conf-smtpd`tell qmail to use vpopmail for auth**

    QMAIL_SMTP_CHECKPASSWORD="/var/vpopmail/bin/vchkpw"

Let\'s install and setup [[[net-mail/vpopmail]](https://packages.gentoo.org/packages/net-mail/vpopmail)[]]:

`root `[`#`]`echo 'net-mail/vpopmail clearpasswd mysql' >> /etc/portage/package.use`

`root `[`#`]`emerge --ask vpopmail`

Create the vpopmail database:

** Note**\
If the CREATE USER command return a syntax error at \"user\", then this is an older MySQL system. In that case, append \"identified by \'mypassword\'\" to the GRANT statement before the semicolon.

`root `[`#`]`mysql -u root -p`

    mysql> create database vpopmail;
    mysql> create user vpopmail@localhost identified by 'mypassword';
    mysql> grant select, insert, update, delete, create, drop on vpopmail.* to vpopmail@localhost;
    mysql> flush privileges;
    mysql> quit

Edit [/etc/vpopmail.conf] and update the mysql password for the vpopmail user:

[FILE] **`/etc/vpopmail.conf`set the vpopmail user password**

    # Read-only DB
    localhost|0|vpopmail|mypassword|vpopmail
    # Write DB
    localhost|0|vpopmail|mypassword|vpopmail

## [dovecot]

Finally add [[[net-mail/dovecot]](https://packages.gentoo.org/packages/net-mail/dovecot)[]] to talk to the email clients:

`root `[`#`]`echo "net-mail/dovecot vpopmail -mysql -pam" >> /etc/portage/package.use`

`root `[`#`]`emerge --ask dovecot`

Add vpopmail UID info to the default dovecot config:

`root `[`#`]`echo 'first_valid_uid = 89' >> /etc/dovecot/dovecot.conf `

`root `[`#`]`echo 'last_valid_uid = 89' >> /etc/dovecot/dovecot.conf `

Edit dovecot SSL configs to pass the SSL certificate to email clients when the login to get mail securely:

[FILE] **`/etc/dovecot/conf.d/10-ssl.conf`set the location of the certs**

    ssl_cert = </var/qmail/control/servercert.pem
    ssl_key = </var/qmail/control/myserver.domain.com.key

[FILE] **`/etc/dovecot/conf.d/10-auth.conf`edit the dovecot auth configs**

    disable_plaintext_auth = no
    auth_mechanisms = plain cram-md5

    #!include auth-system.conf.ext  comment this out, don't need it
    !include auth-vpopmail.conf.ext

[FILE] **`/etc/dovecot/conf.d/auth-vpopmail.conf.ext`comment out these two vpopmail lines**

    # [quota_template=<template>] - %q expands to Maildir++ quota
    #  args = quota_template=quota_rule=*:backend=%q}}

Start dovecot and add to the default runlevel:

`root `[`#`]`/etc/init.d/dovecot start `

`root `[`#`]`rc-update add dovecot default `