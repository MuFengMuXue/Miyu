# Virtual user mail system with Postfix, Dovecot and Roundcube

This article describes how to set up a virtual user mail system, i.e. where the senders and recipients do not correspond to the Linux system users.

Roughly, the components used in this article are Postfix as the mail server, Dovecot as the IMAP server, Roundcube as the webmail interface and PostfixAdmin as the administration interface to manage it all.

In the end, the provided solution will allow you to use the best currently available security mechanisms, you will be able to send mails using SMTP and SMTPS and receive mails using POP3, POP3S, IMAP and IMAPS. Additionally, configuration will be easy thanks to PostfixAdmin and users will be able to login using Roundcube.

## Installation
Before you start, you must have both a working MySQL server as described in MySQL and a working Postfix server as described in Postfix.

Install the , , and  packages.

## Configuration
## User
For security reasons, a new user should be created to store the mails:
 # groupadd -g 5000 vmail
 # useradd -u 5000 -g vmail -s /usr/bin/nologin -d /home/vmail -m vmail
A gid and uid of 5000 is used in both cases so that we do not run into conflicts with regular users. All your mail will then be stored in . You could change the home directory to something like  but be careful to change this in any configuration below as well.

## Database
You will need to create an empty database and corresponding user. In this article, the user postfix_user will have read/write access to the database postfix_db using hunter2 as password. You are expected to create the database and user yourself, and give the user permission to use the database, as shown in the following code.

Now you can go to the PostfixAdmin's setup page, let PostfixAdmin create the needed tables and create the users in there.

## PostfixAdmin
See PostfixAdmin.

## SSL certificate
You will need a SSL certificate for all encrypted mail communications (SMTPS/IMAPS/POP3S). If you do not have one, create one:
 # cd /etc/ssl/private/
 # openssl req -new -x509 -nodes -newkey rsa:4096 -keyout vmail.key -out vmail.crt -days 1460 #days are optional
 # chmod 400 vmail.key
 # chmod 444 vmail.crt

Alternatively, create a free trusted certificate using Let's Encrypt. The private key will be in , the certificate in . Either change the configuration accordingly, or symlink the keys to :
 # ln -s /etc/letsencrypt/live/yourdomain/privkey.pem /etc/ssl/private/vmail.key
 # ln -s /etc/letsencrypt/live/yourdomain/fullchain.pem /etc/ssl/private/vmail.crt

## Postfix
Before you copy & paste the configuration below, check if  has already been set. If you leave more than one active, you will receive warnings during runtime.

Also follow Postfix#Secure SMTP (receiving) pointing to the files you created in #SSL certificate.

## Setting up Postfix
To  append:
 relay_domains = $mydestination
 virtual_alias_maps = proxy:mysql:/etc/postfix/virtual_alias_maps.cf
 virtual_mailbox_domains = proxy:mysql:/etc/postfix/virtual_mailbox_domains.cf
 virtual_mailbox_maps = proxy:mysql:/etc/postfix/virtual_mailbox_maps.cf
 virtual_mailbox_base = /home/vmail
 virtual_mailbox_limit = 512000000
 virtual_minimum_uid = 5000
 virtual_transport = virtual
 virtual_uid_maps = static:5000
 virtual_gid_maps = static:5000
 local_transport = virtual
 local_recipient_maps = $virtual_mailbox_maps
 transport_maps = lmdb:/etc/postfix/transport

 smtpd_sasl_auth_enable = yes
 smtpd_sasl_type = dovecot
 smtpd_sasl_path = /var/run/dovecot/auth-client
 smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination
 smtpd_relay_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination
 smtpd_sasl_security_options = noanonymous
 smtpd_sasl_tls_security_options = $smtpd_sasl_security_options
 smtpd_tls_security_level = may
 smtpd_tls_auth_only = yes
 smtpd_tls_received_header = yes
 smtpd_tls_cert_file = /etc/ssl/private/vmail.crt
 smtpd_tls_key_file = /etc/ssl/private/vmail.key
 smtpd_sasl_local_domain = $mydomain
 smtpd_tls_loglevel = 1
 smtp_tls_security_level = may
 smtp_tls_loglevel = 1

* In the configuration above  is a list of the domains that you want to receive mail for. This CANNOT contain the domain that is set in . That is why we left  to be localhost only.

*  will contain the information of virtual users and their mailbox locations. We are using a hash file to store the more permanent maps, and these will then override the forwards in the MySQL database.

*  is the base directory where the virtual mailboxes will be stored.

The  and  are the real system user IDs that the virtual mails will be owned by. This is for storage purposes.

## Create the file structure
Those new additional settings reference a lot of files that do not even exist yet. We will create them with the following steps.

If you were setting up your database with PostfixAdmin and created the database schema through PostfixAdmin, you can create the following files. Do not forget to change the password:

For alias domains functionality adjust the following files:

Run postmap on transport to generate its db:
 # postmap /etc/postfix/transport

## Dovecot
Instead of using the provided Dovecot example configuration file, we will create our own . Please note that the user and group here might be vmail instead of postfix!

{{hc|/etc/dovecot/dovecot.conf|
protocols = imap pop3
auth_mechanisms = plain
passdb {
    driver = sql
    args = /etc/dovecot/dovecot-sql.conf
}
userdb {
    driver = sql
    args = /etc/dovecot/dovecot-sql.conf
}

service auth {
    unix_listener auth-client {
        group = postfix
        mode = 0660
        user = postfix
    }
    user = root
}

mail_home = /home/vmail/%d/%n
mail_location = maildir:~

ssl_cert = :@localhost/';
// If you are not using dovecot specify another algorithm explicitly e.g 'sha256-crypt'
$config= 'dovecot';
// For dovecot salted passwords only (above must be set to 'dovecot')
// $config['password_algorithm_prefix' = 'true';
// $config= '/usr/bin/doveadm pw';
// $config['password_dovecotpw_method' = 'SHA512-CRYPT';
// $config= true;
$config['password_query' = 'UPDATE mailbox SET password=%P WHERE username=%u';
}}

Make sure this file is readable only by the  user and group since it contains sensitive information:

 # chown http:http /usr/share/webapps/roundcubemail/plugins/password/config.inc.php
 # chmod o-r /usr/share/webapps/roundcubemail/plugins/password/config.inc.php

## Fire it up
All necessary daemons should be started in order to test the configuration. Start both  and .

Now for testing purposes, create a domain and mail account in PostfixAdmin. Try to login to this account using Roundcube. Now send yourself a mail.

## Testing
Now lets see if Postfix is going to deliver mail for our test user.

## Error response
 451 4.3.0 :Temporary lookup failure
Maybe you have entered the wrong user/password for MySQL or the MySQL socket is not in the right place.

This error will also occur if you neglect to run newaliases at least once before starting postfix. MySQL is not required for local only usage of postfix.

 550 5.1.1 : Recipient address rejected: User unknown in virtual mailbox table.
Double check content of mysql_virtual_mailboxes.cf and check the main.cf for mydestination

## See that you have received a email
Now type .

You should see something like the following:

The key is the last entry. This is an actual email, if you see that, it is working.

## Optional Items
Although these items are not required, they definitely add more completeness to your setup

## Quota
To enable mailbox quota support by dovecot, do the following:
*First add the following lines to /etc/dovecot/dovecot.conf
 dict {
 	quotadict = mysql:/etc/dovecot/dovecot-dict-sql.conf.ext
 }
 service dict {
 	unix_listener dict {
 		group = vmail
 		mode = 0660
 		user = vmail
 	}
 	user = root
 }
 service quota-warning {
 	executable = script /usr/local/bin/quota-warning.sh
 	user = vmail
 	unix_listener quota-warning {
 		group = vmail
 		mode = 0660
 		user = vmail
 	}
 }
 mail_plugins=quota
 protocol pop3 {
 	 mail_plugins = quota
 	 pop3_client_workarounds = outlook-no-nuls oe-ns-eoh
 	 pop3_uidl_format = %08Xu%08Xv
 }
 protocol lda {
 	mail_plugins = quota
 	postmaster_address = postmaster@yourdomain.com
 }
 protocol imap {
 	mail_plugins = $mail_plugins imap_quota
 	mail_plugin_dir = /usr/lib/dovecot/modules
 }
 plugin {
        quota = dict:User quota::proxy::quotadict
        quota_rule2 = Trash:storage=+10%%
        quota_warning = storage=100%% quota-warning +100 %u
        quota_warning2 = storage=95%% quota-warning +95 %u
        quota_warning3 = storage=80%% quota-warning +80 %u
        quota_warning4 = -storage=100%% quota-warning -100 %u # user is no longer over quota
 }

*Create a new file /etc/dovecot/dovecot-dict-sql.conf.ext with the following code:
 connect = host=localhost dbname=yourdb user=youruser password=yourpassword
 map {
 	pattern = priv/quota/storage
 	table = quota2
 	username_field = username
 	value_field = bytes
 }
 map {
 	pattern = priv/quota/messages
 	table = quota2
 	username_field = username
 	value_field = messages
 }
*Create a warning script /usr/local/bin/quota-warning.sh and make sure it is executable. This warning script works with postfix lmtp configuration as well.

*Edit the user_query line and add iterat_query in dovecot-sql.conf as following:
  user_query = SELECT '/home/vmail/%d/%n' as home, 'maildir:/home/vmail/%d/%n' as mail, 5000 AS uid, 5000 AS gid, concat('*:bytes=', quota) AS quota_rule FROM mailbox WHERE username = '%u' AND active = '1'
  iterate_query = SELECT username AS user FROM mailbox
*Set up LDA as described above under SpamAssassin. If you are not using SpamAssassin, the pipe should look like this in /etc/postfix/master.cf :
  dovecot    unix  -       n       n       -       -       pipe
  flags=DRhu user=vmail:vmail argv=/usr/lib/dovecot/deliver -f ${sender} -d ${recipient}
As above activate it in Postfix main.cf
  virtual_transport = dovecot
*You can set up quota per each mailbox in postfixadmin. Make sure the relevant lines in config.inc.php look like this:
 $CONF= 'YES';
 $CONF['quota_multiplier' = '1024000';

Restart postfix and dovecot services. If things go well, you should be able to list all users' quota and usage by the this command:
 doveadm quota get -A
You should be able to see the quota in roundcube too.

## Autocreate and autosubscribe folders in Dovecot
To automatically create the "usual" mail hierarchy, modify your  as follows, editing to your specific needs.

{{bc|1=
namespace inbox {
  type = private
  separator = /
  prefix =
  inbox = yes
}
namespace inbox {
  mailbox Drafts {
    auto = subscribe
    special_use = \Drafts
  }
  mailbox Junk {
   auto = subscribe
   special_use = \Junk
 }
 mailbox Trash {
   auto = subscribe
   special_use = \Trash
 }
 mailbox Sent {
   auto = subscribe
   special_use = \Sent
 }
}
}}

## Dovecot public folder and global ACLs
In this section we enable IMAP namespace public folders combined with global and per-folder ACLs.

First, add the following lines to :

{{bc|1=
### ACLs
mail_plugins = acl
protocol imap {
  mail_plugins = $mail_plugins imap_acl
}
plugin {
 acl = vfile
 # With global ACL files in /etc/dovecot/dovecot-acls file (v2.2.11+):
 acl = vfile:/etc/dovecot/dovecot-acl
}

### Public Mailboxes
namespace {
 type = public
 separator = /
 prefix = public/
 location = maildir:/home/vmail/public:INDEXPVT=~/public
 subscriptions = no
 list = children
}
}}

Create the root directory  and the folders you want to publicly share, for example (the period is required!) .

Change the ownership of all files in the root directory:

 $ chown -R vmail:vmail /home/vmail/public

Finally, create and modify your global ACL file to allow users access to these folders:

In the above example, user  has access to, and can do anything to, all the public folders. Edit to fit your specific needs.

## Fighting Spam
To use SpamAssassin, you must set it up with a SQL database. Otherwise user scores and filter data will not be saved as users are virtual and do not have home directories where to save these.

As an alternative to SpamAssassin, consider . Out of the box, it delivers an amazing amount of spam reduction, greylisting, etc and includes a nifty webui. See also == Sidenotes ==

## Alternative vmail folder structure
Instead of having a directory structure like  you can have cleaner subdirectories (without the additional domain name) by replacing  and  with:

## Troubleshooting
## IMAP/POP3 client failing to receive mails
If you get similar errors, take a look into  or run  as root to find out more.

It may turn out that the Maildir  is just being created if there is at least one email waiting. Otherwise there would not be any need for the directory creation before.

## Roundcube not able to delete emails or view any 'standard' folders
Ensure that the Roundcube config.inc.php file contains the following:

## LMTP / Sieve
Is LMTP not connecting to sieve? Ensure that your server is not routing the messages locally. This can be set in :

## Are your emails sent to gmail users ending up in their junk/spam folders?
Google gmail (and most other large email providers) will send your emails straight into your recipients junk / spam folder if you have not implemented SPF / DKIM / DMARC policies. (Hint: Rspamd, via the link above, shows you how to set this up, and will DKIM sign your emails.)

## Sending and receiving mails broken, logs mentioning "transport_maps lookup failure" along with "unsupported dictionary type: hash"
[https://gitlab.archlinux.org/archlinux/packaging/packages/postfix/-/commit/2ebb2274ab0481a8c70c2fded9126a30b0f228d3 Postfix 3.9.0 removed support for the "hash" transport map type. To fix this, stop  and edit  by replacing all instances of  with . Then save the file, delete  and regenerate it with the new format using . After that, you can start .
