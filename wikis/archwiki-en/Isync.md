# Isync

isync is a command line application to synchronize mailboxes; it supports Maildir and IMAP4 mailboxes. New messages, message deletions and flag changes can be propagated both ways.

Synchronization is based on unique message identifiers (UIDs), so no identification conflicts can occur (as opposed to some other mail synchronizers).
Synchronization state is kept in one local text file per mailbox pair; multiple replicas of a mailbox can be maintained.

## Installing
Install the  package.

## Configuring
First, a main configuration file needs to be created, either as   in the user's  directory, or  in the user's home directory root. The package supplies an example  file. Another example for a Google-mail account is as follows:

It is possible to avoid the proprietary  (or ) folder categorization by using separate channels for each directory, and later merging them to a group:

As you can see, name-translations are possible this way as well.

## Usage
First make any folders that were specified as Maildirs:

 $ mkdir -p ~/.mail/gmail

Then to retrieve the mail for a specific channel run:

 $ mbsync gmail

or to retrieve the mail for all channels:

 $ mbsync -a

## Tips and tricks
## Using Path and/or Inbox on NTFS partitions
Since NTFS partitions will not accept a semicolon in a filename, you need to change your InfoDelimiter and your FieldDelimiter to something else, you can achieve this by globaly (outside any store or channel configuration) changing the later, like below:

## Importing EML emails
Importing emails in the EML format is achieved by copying the  files under the  directory of the desired Maildir directory.
For example, using .
The new emails should be detected during the subsequent run of .

## Calling mbsync automatically
## With a timer
If you want to automatically synchronize your mailboxes, isync can be started automatically with a systemd/User unit. The following service file can start the  command:

The following timer configures  to be started 2 minutes after boot, and then every 5 minutes:

Once those two files are created, reload systemd, then enable and start , adding the  flag to .

## Integration with notmuch or mu4e
If you want to run notmuch or mu/mu4e after automatically synchronizing your mails, it is preferable to modify the above  by adding a post-start hook, like below:

You can also index  by changing the  line to , or to  if you are running emacsclient and would like to index .

This modification assumes that you have already setup notmuch or mu/mu4e for your user. If the ExecStart command does not execute successfully, the ExecStartPost command will not execute, so be aware of this!

Trigger syncing immediately when making local changes (such as marking messages as read) by watching the  directory:

Systemd defaults ensure that the service will not trigger redundantly.

## With imapnotify
IMAP IDLE is a way to get push notifications to download new email, rather than polling the server intermittently. This has the advantage of saving bandwidth and delivering your mail as soon as it is available. Isync does not have native IDLE support, but we can use a program like imapnotify to call mbsync when you receive new email. For this example we will use the  package which is reported to work better with frequent network interruptions.

Install  and create a configuration file for each mail server you want to poll. Note that the file name format, including the .yaml, is necessary if you want to use the provided systemd service:
{{hc|~/.config/imapnotify/gmail.yaml|
{
  "host": "imap.gmail.com",
  "port": 993,
  "tls": true,
  "tlsOptions": {
    "rejectUnauthorized": false
  },
  "username": "username@gmail.com",
  "password": "",
    "passwordCmd": "pass gmail | head -n1",
  "onNewMail": "mbsync gmail",
  "onNewMailPost": "",
  "boxes": [ "INBOX" ]
}
}}
(You can view the full configuration options in the project's README.)

Start/enable the   user unit.

Note that IMAP IDLE only triggers when new mail arrives, not when there is undownloaded mail on the server. For example, if you receive 100 emails with your computer powered off, then turn on your computer, imapnotify will still not download new mail until you receive another email. For this reason you may want to run mbsync once when you log in.

## Using XOAUTH2
First install an XOAUTH2 SASL plugin, like .

For all OAuth2 helpers listed below, choose either one among them, you need to provide a  and optionally a  of your own or of a suitable FOSS registered application.

In order to get a  and , you will need an app registration with the provider. You should create your own app registration if possible, otherwise, for example due to missing rights, you can use existing app registrations, such as Thunderbird's (under ) or Evolution's, which are publicly available until dynamic client registration is supported.

Another option is to temporarily use an incognito browser window to create a free outlook.com account and use that to create the app registration.

## oama
oama is a utility which provides IMAP/SMTP clients with renewal capabilities and authorization of OAuth2 credentials. install  and configure it according to its README.
You can find configuration templates in .

Before you are able to use oama with your credentials you need to authorize OAuth2 access by running the command below:

 $ oama authorize service email

Where service is your email provider (e.g. google) and email is your email address.

After the authorization completed add  and  to the  section in the .

## oauth2token
Install  and follow its README to configure the account. It will be responsible for getting the current XOAUTH2 token using the account credentials every time mbsync needs to authenticate.

Finally, add  and , substituting  and  with the values you used for , to the  section in the .

## mutt_oauth2.py
 is known to work with Google and Microsoft accounts. Download  and follow its README for background and to configure the account.

In short, you will need to modify the  and  for your preferred encryption system directly in script's source or specify them on each subsequent renew invocation using flags. During authorization, add the  and  from an app registration with the provider (see #Using XOAUTH2). Then to initialize your tokens, you run and answer the questions in:

 $ mutt_oauth2.py userid@myschool.edu.tokens --verbose --authorize

Note that gmail only supports the  authflow while MS only supports the  authflow.

To subsequently receive your access token (the script automatically handles renewing of tokens), you can run:

 $ mutt_oauth2.py userid@myschool.edu.tokens

As the  and  options are not stored within the token file, you have to pass them separately if you do not want to hardcode your gpg key name in script's source:

 $ mutt_oauth2.py userid@myschool.edu.tokens --encryption-pipe 'gpg --encrypt --recipient '

Finally, add  and , with the correct paths if necessary, to the  section in the .

## oauth2ms
 can be used to fetch oauth2 tokens from the Microsoft identity endpoint.
Additionally, it can encode the token in the XOAUTH2 format to be used as authentication in IMAP mail servers.

Install  as indicated and create a config file  containing the .

Finally, add  and , or the full path to  if necessary, to the  section in .

## Integration with ProtonMail
Proton Mail solution for interfacing with conventional email clients is for the user to run a local IMAP/SMTP server that will communicate with ProtonMail servers -- it is known as ProtonMail Bridge and available in the  package.
Note that this software requires a running and working software implementing FreeDesktop.org's Secret Service API (e.g., GNOME Keyring or KeePassXC) and gpg-agent.

## Bridge installation and configuration
1. Run the bridge and login using ProtonMail credentials:

    $ protonmail-bridge-core --cli
    >>> login
    >>> info

2. To let IMAP clients accessing the local Bridge IMAP server, get the ProtonMail self-signed certificate:

    $ openssl s_client -starttls imap -connect 127.0.0.1:1143 -showcerts

3. Manually copy lines between   and  and put them inside a file, e.g., .

4. After checking that everything is working, stop the Bridge from the command-line and run it as a service:

    $ systemctl --user enable --now protonmail-bridge.service

## Isync configuration for interacting with Bridge
Configuring Isync to use ProtonMail Bridge as an IMAP server is possible using the following in your  configuration.
The following is a working example in a two-way sync between the local machine the ProtonMail account.

    IMAPStore proton-remote
    Port 1143
    Host 127.0.0.1
    User YOUR_EMAIL
    PassCmd YOUR_PASSWORD
    TLSType STARTTLS
    CertificateFile YOUR_CERTIFICATE_PATH

    MaildirStore proton-local
    SubFolders Verbatim
    Path ~/PATH/TO/MAILBOX/
    Inbox ~/PATH/TO/MAILBOX/Inbox

    Channel proton
    Far :proton-remote:
    Near :proton-local:
    Patterns * !Labels* !"All Mail"
    Create Both
    Expunge Both
    SyncState *

## Troubleshooting
## SSL error
If you get the following error:

Since google enforce SNI when you use TLS 1.3, ensure to run at least isync v1.3.0
See https://sourceforge.net/p/isync/isync/merge-requests/2/ for more details

If you get certificate related errors like:

you may need to retrieve the server's certificates manually in order for mbsync to correctly verify it.

## Step #1: Get the certificates
This will create a certificate file called  (e.g. ). Alternatively one can download get_certs.sh and run it:

If you wish to do this manually, you may enter:

and it will display output something like:

{{bc|
CONNECTED(00000003)
depth=1 C = US, O = Google Inc, CN = Google Internet Authority
verify error:num=20:unable to get local issuer certificate
verify return:0
---
Certificate chain
 0 s:/C=US/ST=California/L=Mountain View/O=Google Inc/CN=imap.gmail.com
   i:/C=US/O=Google Inc/CN=Google Internet Authority
-----BEGIN CERTIFICATE-----
MIIDgDCCAumgAwIBAgIKO3MmiwAAAABopTANBgkqhkiG9w0BAQUFADBGMQswCQYD
VQQGEwJVUzETMBEGA1UEChMKR29vZ2xlIEluYzEiMCAGA1UEAxMZR29vZ2xlIElu
dGVybmV0IEF1dGhvcml0eTAeFw0xMjA5MTIxMTU1NDlaFw0xMzA2MDcxOTQzMjda
MGgxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1N
b3VudGFpbiBWaWV3MRMwEQYDVQQKEwpHb29nbGUgSW5jMRcwFQYDVQQDEw5pbWFw
LmdtYWlsLmNvbTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEA2OmU9DjI+DFQ
ThqIN4vL6EqZbzH0ejLKcc+zhxsq9BU5hXohSJ1sS5FUU2vReDKk8fd+ZR3cWtpf
CTYAUSvdnz1ZFjESSzyUBmGRqByhoc0yqdfb61NosA4CDaO+z7DtAgKyecqnAJad
TPYYf9aLk/UgJuc6GseitjzFYonXi6ECAwEAAaOCAVEwggFNMB0GA1UdJQQWMBQG
CCsGAQUFBwMBBggrBgEFBQcDAjAdBgNVHQ4EFgQUFuLyTg2NcsyaEESytZbLbQan
YIowHwYDVR0jBBgwFoAUv8Aw6/VDET5nup6R+/xq2uNrEiQwWwYDVR0fBFQwUjBQ
oE6gTIZKaHR0cDovL3d3dy5nc3RhdGljLmNvbS9Hb29nbGVJbnRlcm5ldEF1dGhv
cml0eS9Hb29nbGVJbnRlcm5ldEF1dGhvcml0eS5jcmwwZgYIKwYBBQUHAQEEWjBY
MFYGCCsGAQUFBzAChkpodHRwOi8vd3d3LmdzdGF0aWMuY29tL0dvb2dsZUludGVy
bmV0QXV0aG9yaXR5L0dvb2dsZUludGVybmV0QXV0aG9yaXR5LmNydDAMBgNVHRMB
Af8EAjAAMBkGA1UdEQQSMBCCDmltYXAuZ21haWwuY29tMA0GCSqGSIb3DQEBBQUA
A4GBAC1LV7tM6pcyVJLcwdPml4DomtowsjTrqvy5ZFa3SMKANK0iZBgFu74O0THX
8SxP/vn4eAs0yRQxcT1ZuoishLGQl5NoimLaQ4BGQnzFQHDJendfaVKDl21GenJp
is72sIrAeprsVU8PbNsllUamWsIjKr3DH5xQdH54hDtzQojY
-----END CERTIFICATE-----
 1 s:/C=US/O=Google Inc/CN=Google Internet Authority
   i:/C=US/O=Equifax/OU=Equifax Secure Certificate Authority
-----BEGIN CERTIFICATE-----
MIICsDCCAhmgAwIBAgIDC2dxMA0GCSqGSIb3DQEBBQUAME4xCzAJBgNVBAYTAlVT
MRAwDgYDVQQKEwdFcXVpZmF4MS0wKwYDVQQLEyRFcXVpZmF4IFNlY3VyZSBDZXJ0
aWZpY2F0ZSBBdXRob3JpdHkwHhcNMDkwNjA4MjA0MzI3WhcNMTMwNjA3MTk0MzI3
WjBGMQswCQYDVQQGEwJVUzETMBEGA1UEChMKR29vZ2xlIEluYzEiMCAGA1UEAxMZ
R29vZ2xlIEludGVybmV0IEF1dGhvcml0eTCBnzANBgkqhkiG9w0BAQEFAAOBjQAw
gYkCgYEAye23pIucV+eEPkB9hPSP0XFjU5nneXQUr0SZMyCSjXvlKAy6rWxJfoNf
NFlOCnowzdDXxFdF7dWq1nMmzq0yE7jXDx07393cCDaob1FEm8rWIFJztyaHNWrb
qeXUWaUr/GcZOfqTGBhs3t0lig4zFEfC7wFQeeT9adGnwKziV28CAwEAAaOBozCB
oDAOBgNVHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFL/AMOv1QxE+Z7qekfv8atrjaxIk
MB8GA1UdIwQYMBaAFEjmaPkr0rKV10fYIyAQTzOYkJ/UMBIGA1UdEwEB/wQIMAYB
Af8CAQAwOgYDVR0fBDMwMTAvoC2gK4YpaHR0cDovL2NybC5nZW90cnVzdC5jb20v
Y3Jscy9zZWN1cmVjYS5jcmwwDQYJKoZIhvcNAQEFBQADgYEAuIojxkiWsRF8YHde
BZqrocb6ghwYB8TrgbCoZutJqOkM0ymt9e8kTP3kS8p/XmOrmSfLnzYhLLkQYGfN
0rTw8Ktx5YtaiScRhKqOv5nwnQkhClIZmloJ0pC3+gz4fniisIWvXEyZ2VxVKfml
UUIuOss4jHg7y/j7lYe8vJD5UDI=
-----END CERTIFICATE-----
---
Server certificate
subject=/C=US/ST=California/L=Mountain View/O=Google Inc/CN=imap.gmail.com
issuer=/C=US/O=Google Inc/CN=Google Internet Authority
---
No client certificate CA names sent
---
SSL handshake has read 2108 bytes and written 350 bytes
---
New, TLSv1/SSLv3, Cipher is ECDHE-RSA-RC4-SHA
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.1
    Cipher    : ECDHE-RSA-RC4-SHA
    Session-ID: 77136647F42633D82DEDFBB9EB62AB516547A3697D83BD1884726034613C1C09
    Session-ID-ctx:
    Master-Key: 635957FBA0762B10694560488905F73BDD2DB674C41970542ED079446F27234E2CA51CF26938B8CA56DF5BBC71E429A7
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 100800 (seconds)
    TLS session ticket:
    0000 - d6 5b a0 a7 10 0e 64 04-72 93 7c 9f 94 fa 07 57   .0010 - f1 8b 9d 24 8b 9d 1b f3-a8 b1 4d 2c a9 00 e1 82   ...$......M,....
    0020 - 00 83 1e 3f e5 f2 b2 2c-d2 a8 87 83 16 02 0d 1e   ...?...,........
    0030 - bf b6 c1 d6 75 21 04 e6-63 6b ab 5b ed 94 7a 30   ....u!..ck.[..z0
    0040 - 1a d0 aa 44 c2 04 9b 10-06 28 b5 7b a0 43 a6 0d   ...D.....(.{.C..
    0050 - 3b 4a 85 1f 2e 07 0a e1-32 9b bd 5d 65 41 4c e2   ;J......2..eAL.
    0060 - 7c d7 43 ec c4 18 77 53-b5 d4 84 b4 c9 bd 51 d6   |.C...wS......Q.
    0070 - 2d 4f 2e 10 a6 ed 38 c5-8e 9d f8 8b 8a 63 3f 7b   -O....8......c?{
    0080 - ee e6 b8 bf 7a f8 b8 e8-47 92 84 f1 9b 0c 63 30   ....z...G.....c0
    0090 - 76 d8 e1 44                                       v..D

    Start Time: 1352632558
    Timeout   : 300 (sec)
    Verify return code: 20 (unable to get local issuer certificate)
---
* OK Gimap ready for requests from 108.78.162.240 o67if11168976yhc.67
}}

Simply copy the first block that begins with  and ends with , paste into a file, and save with a .pem extension (this is necessary for the next step). Older instructions state that, with Gmail, both certificate blocks must be saved but on testing this was found to be unnecessary.

Now, copy the root issuer certificate to your local certificate folder. In this example (Gmail), the root issuer is Equifax Secure Certificate Authority. This certificate is included in the  package.

## Step #2: Setup mbsync
Configure mbsync to use that certificate:

## BAD Command with Exchange 2003
When connecting to an MS Exchange 2003 server, there could be problems when using pipelining (i.e. executing multiple imap commands concurrently).  Such an issue could look as follows:

{{hc|mbsync -V exchange|
>>> 9 SELECT "arch"^M
* 250 EXISTS
* 0 RECENT
* FLAGS (\Seen \Answered \Flagged \Deleted \Draft $MDNSent)
* OK (\Seen \Answered \Flagged \Deleted \Draft $MDNSent) Permanent flags
* OK 241 Is the first unseen message
* OK 4352 UIDVALIDITY value
9 OK SELECT completed.
>>> 10 UID FETCH 1:1000000000 (UID FLAGS)^M
* 1 FETCH (UID 1 FLAGS (\Seen \Answered))
* 2 FETCH (UID 2 FLAGS (\Seen \Answered))
...
* 249 FETCH (UID 696 FLAGS ())
* 250 FETCH (UID 697 FLAGS (\Seen))
10 OK FETCH completed.
>>> 11 APPEND "arch" (\Seen) {4878+}^M
(1 in progress) >>> 12 UID FETCH 697 (BODY.PEEK[)^M
(2 in progress) >>> 13 UID STORE 696 +FLAGS.SILENT (\Deleted)^M
12 BAD Command is not valid in this state.
}}

So command 9 is to select a new folder, command 10 checks the mail and commands 11, 12 and 13 run in parallel, writing/getting/flagging a mail.  In this case, the Exchange server would terminate the connection after the BAD return value and go on to the next channel.  (And if all went well in this channel, mbsync would return with 0.)  After setting

 PipelineDepth 1

in the IMAPStore config part of the Exchange, this problem did not occur any more.

## Emails on remote server have the wrong date
This fix works when syncing with fastmail, but it likely applies to other services as well.

If you move an email to a new folder using an email client, and mbsync causes the email to appear with the wrong date on the server, add this to your configuration file:

 CopyArrivalDate yes

For example, without this setting, moving an old email from Inbox to Archive using mu4e and then
syncing to fastmail with mbsync will cause the email to appear in Archive but with the date of
the sync.

mbsync uses mtime of email message when uploading from maildir to imap server. You can use fix_maildir_mail_mtime.py script to set mtime from email header.
