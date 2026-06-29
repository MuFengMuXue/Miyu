# Msmtp

msmtp is a very simple and easy to use SMTP client with fairly complete sendmail compatibility.

## Installation
Install the  package. Additionally, install , which creates a sendmail alias to msmtp.

## Basic setup
Since msmtp version 1.8.6 you can place your user configuration either at  or . The following is an example of a msmtp configuration (the file is based on the per-user example file located at ; the system configuration file belongs at  and its corresponding example file is located at ).

The user configuration file must be explicitly readable/writeable by its owner or msmtp will fail:

 $ chmod 600 ~/.msmtprc

To avoid saving the password in plain text in the configuration file, use passwordeval to launch an external program, or see the #Password management section below.  This example using Gnu PG is commonly used to perform decryption of a password:

 echo -e "password\n" | gpg --encrypt -o .msmtp-gmail.gpg # enter id (email...)

## OAuth2 Setup
OAuth2 can be used to securely authenticate msmtp when basic username/password authentication is unsupported by the site configuration or otherwise undesirable.

## oama
msmtp alone lacks the ability to renew or authorize OAuth2 credentials. A comprehensive solution is using the oama utility which provides IMAP/SMTP clients with renewal capabilities and authorization of OAuth2 credentials.

To use oama, install  and configure msmtp to use it:

    # account at Google with oauth2 access
    account YOUR_EMAIL_NAME@gmail.com
    from YOUR_EMAIL_NAME@gmail.com
    user YOUR_EMAIL_NAME@gmail.com
    auth oauthbearer
    passwordeval oama access YOUR_EMAIL_NAME@gmail.com
    host smtp.gmail.com
    port 587
    tls on
    tls_trust_file /etc/ssl/certs/ca-certificates.crt

Access token renewal happens automatically in the background transparent to the user.

## Using the mail command
To send mails using the  command you must install the package , which also provides the  command. You will also need to provide a -compatible MTA, either by installing  (which symlinks  to ) or by editing  to set the sendmail path:

A  file will need to be in the home of every user who wants to send mail or alternatively the system wide  can be used.

msmtp also understands aliases. Add the following line to the defaults section of msmtprc or your local configuration file:

and create an aliases file in

## Test functionality
The account option () tells which account to use as sender:

 $ echo "hello there username." | msmtp -a default username@domain.com

Or, send both a subject and a body:

 $ printf "Subject: Test\n\nhello there username." | msmtp -a default username@domain.com

Or, with the addresses in a file:

 $ cat test.mail | msmtp -a default @domain.com

## Cronie default email client
To make Cronie use msmtp rather than sendmail, make sure  is installed, or edit the  systemd unit:

Then you must tell cronie or msmtp what your email address is. One way to accomplish this is by adding it to the msmtp configuration:

# Add to :
# Create :

Alternatively, you can add it directly to the crontab:

* Add a  line to the crontab:
* Add a  line to the crontab:
:The last part is necessary to prevent this error:

## Password management
Passwords for msmtp can be stored in plaintext, encrypted files, or a keyring.

## GNOME Keyring
Storing passwords in GNOME Keyring is supported natively in msmtp. Setup the keyring as described on the linked wiki page and install . Then, store a password by running:

 secret-tool store --label=msmtp host smtp.your.domain service smtp user yourusername

msmtp should now find the password automatically.

## GnuPG
The  directive may be omitted. In that case, if the account in question has  set to a legitimate value other than , invoking msmtp from an interactive shell will ask for the password before sending mail. msmtp will not prompt if it has been called by another type of application, such as Mutt. For such cases, the  parameter
can be used to call an external keyring tool like GnuPG.

To do this, set up GnuPG, including gpg-agent to avoid having to enter the password every time. Then, create an encrypted password file for msmtp, as follows. Create a secure directory with  permissions located on a tmpfs to avoid writing the unencrypted password to the disk. In that directory create a plain text file with the mail account password. Then, encrypt the file with your private key:

 $ gpg --default-recipient-self -e /path/to/plain/password

Remove the plain text file and move the encrypted file to the final location, e.g. . In  add:

Normally this is sufficient for a GUI password prompt to appear when, for example, sending a message from Mutt. If gpg prompt for the passphrase cannot be issued, then start the gpg-agent before. A simple hack to start the agent is to execute a external command in your muttrc using the backtick  syntax. For example, you can put something like the following in your muttrc:

Mutt will execute this when it starts, gpg-agent will cache your password, msmtp will be happy and you can send mail.

An alternative is to place passwords in , a file that can act as a common pool for msmtp, OfflineIMAP, and associated tools.

## pass
You may store your credentials inside of the pass password manager.

If you are using your main password (which is customarily stored in the first line of your pass file) to login into your SMTP server, you can add the following to your :

If you are using Gmail, and have set up an app password, the following configuration will suit you better.
Save your app password inside your  password file, but with a  prefix:

Then add the following to your :
{{hc|~/.msmtprc|
passwordeval   "pass your_email_password_entry  awk '/^msmtp:/ { print $2; }'"
}}

In either case, trying to send an email with msmtp will trigger , which may ask you for your  master password if you have not entered it recently.

## Miscellaneous
## Using msmtp offline
Although msmtp is great, it requires that you be online to use it. This is not ideal for people on laptops with intermittent connections to the Internet or dialup users. Several scripts have been written to remedy this fact, collectively called msmtpqueue.

The scripts are installed under . You might want to copy the scripts to a convenient location on your computer, ( is a good choice).

Finally, change your MUA to use msmtp-enqueue.sh instead of msmtp when sending e-mail. By default, queued messages will be stored in . To change this location, change the  line in the scripts (or delete the line, and export the QUEUEDIR variable in  like so: ).

When you want to send any mail that you have created and queued up run:

 $ /usr/local/bin/msmtp-runqueue.sh

Adding  to your PATH can save you some keystrokes if you are doing it manually. The README file that comes with the scripts has some handy information, reading it is recommended.

## Vim syntax highlighting
The msmtp source distribution includes an  syntax-highlighting script for Vim, which is available at . The filetype is not detected automatically. The easiest way to enable it is by adding a modeline at the top or bottom of the file(s), i.e.:

 # vim:filetype=msmtp

## Send mail with PHP using msmtp
Look for  option in your  and edit like this:

 sendmail_path = "/usr/bin/msmtp -C /path/to/your/config -t"

Note that you can not use a user configuration file (ie: one under ~/) if you plan on using msmtp as a sendmail replacement with php or something similar.
In that case just create /etc/msmtprc, and remove your user configuration (or not if you plan on using it for something else). Also make sure it is readable by whatever you are using it with (php, django, etc...).

From the msmtp manual: Accounts defined in the user configuration file override accounts from the system configuration file. The user configuration file must have no more permissions than user read/write

So it is impossible to have a conf file under ~/ and have it still be readable by the php user.

To test it place this file in your php enabled server or using php-cli.

 will fail to send mails and logs the warning:  unless you set the permissions of your /etc/msmtprc to user read/write (600).

## Troubleshooting
## Issues with TLS
If you see one of the following messages:

 msmtp: TLS certificate verification failed: the certificate hasn't got a known issuer

 msmtp: TLS certificate verification failed: The certificate is NOT trusted. The certificate issuer is unknown.

It probably means your  parameter of the configuration file is not right.

Just follow the fine manual. It explains you how to find out the server certificate issuer of a given smtp server. Then you can explore the  directory to find out if by any chance, the certificate you need is there. If not, you will have to get the certificate on your own. If you are using your own certificate, you can make msmtp trust it by adding the following to your :

 tls_fingerprint

If the user have the certificate used by the server in a PEM file, he can find the fingerprint of the certificate stored  using :

 openssl x509 -in CERT.pem -inform PEM -fingerprint

If you are trying to send mail through Gmail and are receiving this error, have a look at this thread or just use the second Gmail example above.

If you are completely desperate, but are 100% sure you are communicating with the right server, you can always temporarily disable the cert check:

 $ msmtp --tls-certcheck off

If you see the following message:

 msmtp: TLS handshake failed: the operation timed out

You may be affected by this bug. Recompile with  (msmtp is compiled with GnuTLS by default).

## Server sent empty reply
If you get a "server sent empty reply" error, this probably means the mail server does not support STARTTLS over port 587, but requires TLS over port 465.

To let msmtp use TLS over port 465, add the following line to :

 tls_starttls off

## Zoho SMTP server
It can also happen on Zoho SMTP servers when the mail has no
blank line between mail headers and mail body (see Debian bug #917260). The solution to this is to add an extra space in between:

 "test-header\n\ntest-body"

## Issues with GSSAPI
If you get the following error

 GNU SASL: GSSAPI error in client while negotiating security context in gss_init_sec_context() in SASL library.  This is most likely due insufficient credentials or malicious interactions.

Try changing your auth setting to plain, instead of gssapi in your .msmtprc file https://bbs.archlinux.org/viewtopic.php?id=138727:

 auth plain

## Envelope not accepted
In the case of

 msmtp: envelope from address mail@server not accepted by the server
 msmtp: server message: 530 5.5.1 Authentication Required.
 msmtp: could not send mail (account default from /etc/msmtprc)

Try enabling authentication with

 auth on

or any other method.
