# SOGo

SOGo provides a rich AJAX-based Web interface and supports multiple native clients through the use of standard protocols such as CalDAV, CardDAV and GroupDAV, as well as Microsoft ActiveSync. This article explains how to setup a groupware server using SOGo.

## Installation
## Considerations
SOGo can use many different sources for user authentication including, but not limited to, Active Directory, OpenLDAP, MySQL/MariaDB, PostgreSQL, and probably many others if you include PAM. This article will focus on using a centrally managed user database for both authentication, and to provide a global address list.

Additionally, either  or  must be used to store the users' calendars and address books. As of this writing, the SOGo documentation has a clear preference for MariaDB (or MySQL), but if you have an existing PostgreSQL installation, it might make sense to use it. Other SQL implementations might also be supported, but are not currently covered.

Finally, there are currently two versions of SOGo that are being actively maintained. SOGo-2.x is uses a look and feel that is similar to a desktop client, while SOGo-3.x uses a more modern interface, taking cues from Google using AngularJS. Instructions and configuration are interchangeable between the two versions.

## Prerequisites
Install  or .

* For a local database install MySQL or PostgreSQL.
* For a local mail server install Dovecot and Postfix.
* For a local web server install Apache HTTP Server or nginx.

## Initial web server configuration
## Apache
Install and configure  following instructions at Apache HTTP Server and configure for TLS connections.
Add SOGo to the Apache configuration appending the following lines at the end of the  file or VirtualHost entry:

 ...
 # Include SOGo configuration
 include conf/extra/SOGo.conf

If not done already, uncomment mod_xml2enc and the needed proxy modules mod_proxy{,_http,_html} in the :

 # cp /etc/httpd/conf/httpd.conf{,.bak}
 # sed /mod_xml2enc\.so/s/#//    -i /etc/httpd/conf/httpd.conf
 # sed /mod_proxy\.so/s/#//      -i /etc/httpd/conf/httpd.conf
 # sed /mod_proxy_http\.so/s/#// -i /etc/httpd/conf/httpd.conf
 # sed /mod_proxy_html\.so/s/#// -i /etc/httpd/conf/httpd.conf

Edit the  file and modify the following lines (replace mail.domain.tld with the appropriate hostname for you desired configuration):

 ...
## adjust the following to your configuration
  RequestHeader set "x-webobjects-server-port" "443"
  RequestHeader set "x-webobjects-server-name" "mail.domain.tld"
  RequestHeader set "x-webobjects-server-url" "https://mail.domain.tld"
...

## nginx
If using nginx for the web server, you will only configure on 443, SSL certificates must be in place prior to configuration.
Add the following to :

    server {
        listen 443;
        root /usr/lib/GNUstep/SOGo/WebServerResources/;
        server_name mail.domain.tld
        server_tokens off;
        client_max_body_size 100M;
        index  index.php index.html index.htm;
        autoindex off;
        ssl on;
        ssl_certificate path /path/to/your/certfile; #eg. /etc/ssl/certs/keyfile.crt
        ssl_certificate_key /path/to/your/keyfile; #eg /etc/ssl/private/keyfile.key
        ssl_session_cache shared:SSL:10m;
        #optional ssl_stapling on;
        #optional ssl_stapling_verify on;
        #optional ssl_trusted_certificate /etc/ssl/private/cacert-stapeling.pem;
        #optional resolver 8.8.4.4 8.8.8.8 valid=300s;
        #optionalresolver_timeout 10s;
        ssl_prefer_server_ciphers on;
        #optional ssl_dhparam /etc/ssl/certs/dhparam.pem;
        #optional add_header Strict-Transport-Security max-age=63072000;
        #optional add_header X-Frame-Options DENY;
        #optional add_header X-Content-Type-Options nosniff;
        location = / {
                rewrite ^ https://$server_name/SOGo;
                allow all;
        }
        location = /principals/ {
                rewrite ^ https://$server_name/SOGo/dav;
                allow all;
        }
        location ^~/SOGo {
                proxy_pass http://127.0.0.1:20000;
                proxy_redirect http://127.0.0.1:20000 default;
                # forward user's IP address
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $host;
                proxy_set_header x-webobjects-server-protocol HTTP/1.0;
                proxy_set_header x-webobjects-remote-host 127.0.0.1;
                proxy_set_header x-webobjects-server-name $server_name;
                proxy_set_header x-webobjects-server-url $scheme://$host;
                proxy_connect_timeout 90;
                proxy_send_timeout 90;
                proxy_read_timeout 90;
                proxy_buffer_size 4k;
                proxy_buffers 4 32k;
                proxy_busy_buffers_size 64k;
                proxy_temp_file_write_size 64k;
                client_max_body_size 50m;
                client_body_buffer_size 128k;
                break;
        }
        location /SOGo.woa/WebServerResources/ {
                alias /usr/lib/GNUstep/SOGo/WebServerResources/;
                allow all;
        }
        location /SOGo/WebServerResources/ {
                alias /usr/lib/GNUstep/SOGo/WebServerResources/;
                allow all;
        }
        location ^/SOGo/so/ControlPanel/Products/({
                alias /usr/lib/GNUstep/SOGo/$1.SOGo/Resources/$2;
        }
        location ^/SOGo/so/ControlPanel/Products/[^/*UI/Resources/.*\.(jpg|png|gif|css|js)$ {
                alias /usr/lib/GNUstep/SOGo/$1.SOGo/Resources/$2;
        }
    }

## Start and test web access
Create the state directory and start services:

 # mkdir /var/run/sogo
 # chown sogo:sogo /var/run/sogo
 # chown sogo:sogo /etc/sogo/sogo.conf
 # chmod 0644 /etc/sogo/sogo.conf

Then enable and start the  and either  or  services.

Open a browser and go to http://mail.domain.tld/SOGo/ for Apache, or https://mail.domain.tld/SOGo/ for nginx. Do not try to login just yet, just verify that you can connect and get the login screen as authentication sources have not been setup yet.

## SOGo database configuration
## MySQL/MariaDB
If you have not already done so, create the first MySQL/MariaDB database with the following command:

 # mysql_install_db --user=mysql --basedir=/usr/ --ldata=/var/lib/mysql/

Enable and start , then enter the MySQL shell as the root user:

 # mysql -u root

At the mysql prompt, enter the following commands (replace SogoPW with a secure password):

 CREATE DATABASE sogo;
 CREATE USER 'sogo'@'localhost' IDENTIFIED BY 'SogoPW';
 GRANT ALL PRIVILEGES ON `sogo`.* TO 'sogo'@'localhost' WITH GRANT OPTION;
 FLUSH PRIVILEGES;

## Migrating from a previous PostgreSQL configuration
If you had previously used PostgreSQL, you can migrate user data to MySQL/MariaDB using sogo-tool to backup and restore. Details are obviously site specific, but this example should work for most. Backup the full sogo-database with the following commands:

 # mkdir /root/sogo-backup
 # sogo-tool backup /root/sogo-backup ALL

Now stop the sogo daemon, stop postgresql (if not used for other purposes), and reconfigure sogo (/etc/sogo/sogo.conf) using both the sogo user and sogo database keeping the last path element (see example below).

To restore all user data, run the following commands:
 # for user in `ls -d /root/sogo-backup/*`
   do
       sogo-tool restore -f ALL /root/sogo-backup $(basename $user)
   done

Simply restart sogo to continue using the MySQL/MariaDB.

## PostgreSQL
If you have elected to use PostgreSQL over MySQL/MariaDB, the old instructions have been left for convenience. If this is a new installation, it is recommended that you use only MySQL/MariaDB for sogo/openchange data.

Initialize the default database and start PostgreSQL (be sure to replace en_US.UTF-8 with the correct locale for your installation):

 # mkdir -p /var/lib/postgres/data
 # chown -R postgres:postgres /var/lib/postgres
 # su - postgres -c "initdb --locale en_US.UTF-8 -D '/var/lib/postgres/data'"
Then start and enable  service.

Create the sogo user and the sogo DB for PostgreSQL (do not select a strong password for the sogo user, just use "sogo" for simplicity. This is temporary and will be changed later):

 # su - postgres
 $ createuser --no-superuser --no-createdb --no-createrole --encrypted --pwprompt sogo
 $ createdb -O sogo sogo

Edit the access configuration for the openchange DB:

 # cp /var/lib/postgres/data/pg_hba.conf{,.bak}
 # sed \
       's/D$/D\n\n#Configuration for OpenChange/' \
       -i /var/lib/postgres/data/pg_hba.conf
 # sed \
       's/ange$/ange\nhost\topenchange\topenchange\t127.0.0.1\/32\t\tmd5/' \
       -i /var/lib/postgres/data/pg_hba.conf
 # chown postgres:postgres /var/lib/postgres/data/pg_hba.conf{,.bak}

Restart the  service.

## Configuring user databases
## Active Directory
If using Active Directory for user authentication, whether using Samba (following the Samba/Active Directory domain controller article) or using a Microsoft server, the needed attributes for mail users are already present in the default schema. Users, however, need to have both mail and proxyAddresses attributes set. The proxyAddress attribute labeled SMTP (as opposed to smtp) is the default mail address. If using internal and external domains, you will need to set SMTP to the user's external address as this will be the SMTP from address and envelope sender in outgoing messages. Additionally, the mail attribute must also be set to the user's external email address.

For Samba, you can use the ldbedit command to edit users. In this example, we will modify the "Administrator" user and add aliases for postmaster, as well as internal and external email addresses. Replace vim in the following command with your preferred editor:

 # LDB_MODULES_PATH="/usr/lib/samba/ldb" ldbedit -e vim -H /var/lib/samba/private/sam.ldb '(samaccountname=administrator)'

It is important to change both the mail attribute (this is what will be used for group expansion and global address list functionality), and the primary SMTP address. The smtp entries for proxyAddresses act as aliases. Add the following attributes (again, substitute appropriate values for internal.domain.tld and domain.tld):

If using Microsoft's Active Directory Users and Computers MMC snap-in to edit users, you will need to enable "Show Advanced Features" from the Tools menu, and use the Attribute Editor tab.

Next, allow daemons to lookup users in the directory using LDAP. To do this, create an unprivileged user to use for LDAP lookups and optionally (recommended), set the password not to expire. If using Samba, execute the following commands. Be certain to set a suitably strong password:

 # samba-tool user create ldap --description="Unprivileged user for LDAP lookups"
 # samba-tool user setexpiry ldap --noexpiry

Finally, with Samba after 4.3.8 or 4.2.2, non-encrypted communication is disabled by default. Add the following configuration item to the global section of  if you are not in a position to enable TLS or StartTLS:

## MySQL/MariaDB
The following procedure is valid for mariadb 10.1.25-1 but should also work for MySQL.

# Ensure the sogo user is created in the database (see #MySQL/MariaDB).
# Ensure that there is a database named sogo with the database scheme utf8 (and not utf8mb4). This is necessary because the automatic creation of the sogo_sessions_folder table will fail with the following output:

  SQL: SELECT count(*) FROM sogo_sessions_folder;
  ERROR: Table 'sogo.sogo_sessions_folder' doesn't exist
  SQL: CREATE TABLE sogo_sessions_folder ( c_id VARCHAR(255) PRIMARY KEY, c_value VARCHAR(255) NOT NULL, c_creationdate INT NOT NULL, c_lastseen INT NOT NULL);
  ERROR: Specified key was too long; max key length is 767 bytes           /etc/postfix/ldap-group.cf

Append the following lines to the newly created  (in the #Filter secton):

 query_filter = (&(objectclass=group)(mail=%s))
 special_result_attribute = member
 leaf_result_attribute = mail

Set the permissions:

 # chmod 0600 /etc/postfix/ldap-{alias,group}.cf

Next test our lookup maps for users (groups have not yet been created) (substitute internal.domain.tld):

 # postmap -q administrator@domain.tld ldap:/etc/postfix/ldap-alias.cf
 # postmap -q administrator@internal.domain.tld ldap:/etc/postfix/ldap-alias.cf

The following output should be displayed for both commands:

 Administrator@internal.domain.tld

Append any other hosted domains to the first command below, add the maps, and then reload the Postfix configuration (again replacing domain values):

 # postconf -e virtual_mailbox_domains="domain.tld, internal.domain.tld"
 # postconf -e virtual_alias_maps="ldap:/etc/postfix/ldap-alias.cf, ldap:/etc/postfix/ldap-group.cf"
 # postfix reload

## Maria DB
To be added...

## OpenLDAP
To be added...

## PostgreSQL
To be added...

## SASL configuration
Modify the default smtpd instance:

 # postconf -e smtpd_sasl_type=dovecot
 # postconf -e smtpd_sasl_path=private/auth
 # postconf -e smtpd_sasl_auth_enable=yes
 # postconf -e smtpd_relay_restrictions="permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination"

## LMTP configuration
Use dovecot LMTP for delivery:

 # postconf -e virtual_transport=lmtp:unix:private/dovecot-lmtp

## TLS configuration
If you intend to use STARTTLS (as you should), enable the mail submission port and restrict to authenticated clients. Edit the following lines in :

 submission inet n       -       n       -       -       smtpd
   -o syslog_name=postfix/submission
   -o smtpd_tls_security_level=encrypt
   -o smtpd_sasl_auth_enable=yes
   -o smtpd_sasl_type=dovecot
   -o smtpd_sasl_path=private/auth
   -o smtpd_sasl_security_options=noanonymous
   -o smtpd_client_restrictions=permit_sasl_authenticated,reject
   -o smtpd_sender_login_maps=ldap:/etc/postfix/ldap-sender.cf
   -o smtpd_sender_restrictions=reject_sender_login_mismatch
   -o smtpd_recipient_restrictions=reject_non_fqdn_recipient,reject_unknown_recipient_domain,permit_sasl_authenticated,reject

Add SSL certificates. If you intend to put Postfix in a chroot jail (not discussed in this guide), these need to be placed in the Postfix configuration directory as opposed to the default /etc/ssl/private directory. Additionally, any intermediate certs should be concatenated with the public cert being first in the chain, and the key file should be owned by root with 0400 permission mode (replace mail.domain.tld):

 # postconf -e smtpd_tls_key_file=/etc/postfix/ssl/mail.domain.tld.key
 # postconf -e smtpd_tls_cert_file=/etc/postfix/ssl/mail.domain.tld.pem

Create a map to verify addresses to authenticated users .
 sed -e '/^query/d' \
     -e '/^result/d' \
     /etc/postfix/ldap-alias.cf > /etc/postfix/ldap-sender.cf

Now, edit the file and append the folowing lines:
 query_filter = (&(objectclass=person)(proxyAddresses=smtp:%s))
 leaf_result_attribute = proxyAddresses
 result_attribute = sAMAccountName

Set permissions:
 # chown root:root /etc/postfix/ldap-sender.cf
 # chmod 0640 /etc/postfix/ldap-sender.cf

If you would like to enable TLS on the default SMTP port, you should make it optional. If you make it required, you will not be able to receive mail from many hosts on the internet.

 # postconf -e smtpd_tls_security_level=may

Reload postfix to apply the configuration changes:

 # postfix reload

## Testing the Postfix SASL configuration
Begin by getting a base64 encoded version of the username and password (replace Administrator with a valid username and UserPass with your real password):

 $ echo -ne '\000Administrator\000UserPass' | openssl base64

You should receive output similar to the following:

 AEFkbWluaXN0cmF0b3IAVXNlclBhc3M=

Now, open an openssl session and test (commands you enter are in bold, replace server.internal.domain.tld with the real external FQDN and AEFkbWluaXN0cmF0b3IAVXNlclBhc3M= with the result of the previous command):

 $ '''openssl s_client -starttls smtp -crlf -connect server.internal.domain.tld:587
 Connecting to 127.0.1.1
 CONNECTED(00000003)'''
 ...
 ---
 read R BLOCK
 ehlo server.internal.domain.tld
 250-server.internal.domain.tld
 250-PIPELINING
 250-SIZE 10240000
 250-VRFY
 250-ETRN
 250-AUTH PLAIN LOGIN
 250-ENHANCEDSTATUSCODES
 250-8BITMIME
 250-DSN
 250-SMTPUTF8
 250 CHUNKING
 AUTH PLAIN AEFkbWluaXN0cmF0b3IAVXNlclBhc3M=
 235 2.7.0 Authentication successful
 quit
 221 2.0.0 Bye
 Connection closed by foreign host.

If anything other than a 235 message is returned, something is wrong and you should troubleshoot now rather than later.

## SOGo configuration
## Basic configuration
Create a suitable SOGo configuration file in  (replace items in bold with appropriate values). If using PostgreSQL, replace the "mysql:" lines with the appropriate "postgresql:" lines (as above):

 {
   /* Database Configuration */
   SOGoProfileURL = "mysql://sogo:SogoPW@localhost/sogo/sogo_user_profile";
   OCSFolderInfoURL = "mysql://sogo:SogoPW@localhost/sogo/sogo_folder_info";
   OCSSessionsFolderURL = "mysql://sogo:SogoPW@localhost/sogo/sogo_sessions_folder";

   /* Mail */
   SOGoDraftsFolderName = Drafts;
   SOGoSentFolderName = Sent;
   SOGoTrashFolderName = Trash;
   SOGoJunkFolderName = Junk;
   SOGoIMAPServer = server.internal.domain.tld;
   SOGoSieveServer = sieve://server.internal.domain.tld:4190;
   SOGoSMTPServer = smtp://server.internal.domain.tld;
   SOGoMailDomain = internal.domain.tld;
   SOGoMailingMechanism = smtp;
   SOGoForceExternalLoginWithEmail = NO;
   SOGoMailSpoolPath = /var/spool/sogo;
   NGImap4AuthMechanism = "plain";
   NGImap4ConnectionStringSeparator = "/";

   /* Notifications */
   SOGoAppointmentSendEMailNotifications = YES;
   SOGoACLsSendEMailNotifications = NO;
   SOGoFoldersSendEMailNotifications = NO;

   /* Authentication */
   SOGoPasswordChangeEnabled = YES;

   /* Web Interface */
   SOGoPageTitle = SOGo;
   SOGoVacationEnabled = YES;
   SOGoForwardEnabled = YES;
   SOGoSieveScriptsEnabled = YES;
   SOGoMailAuxiliaryUserAccountsEnabled = YES;
   SOGoTrustProxyAuthentication = NO;
   SOGoXSRFValidationEnabled = NO;

   /* General */
   SOGoLanguage = English;
   SOGoTimeZone = America/Chicago;
   SOGoCalendarDefaultRoles = (
       PublicDAndTViewer,
       ConfidentialDAndTViewer
   );
   SOGoSuperUsernames = (administrator);
   SxVMemLimit = 384;
   //WOPidFile = "/var/run/sogo/sogo.pid";
   SOGoMemcachedHost = "127.0.0.1";

   /* Debug */
   //SOGoDebugRequests = YES;
   //SoDebugBaseURL = YES;
   //ImapDebugEnabled = YES;
   //LDAPDebugEnabled = YES;
   //PGDebugEnabled = YES;
   //MySQL4DebugEnabled = YES;
   //SOGoUIxDebugEnabled = YES;
   //WODontZipResponse = YES;
   //WOLogFile = /var/log/sogo/sogo.log;

 }

Then issue the following commands:
 # chown sogo:sogo /etc/sogo/sogo.conf
 # chmod 0600 /etc/sogo/sogo.conf
 # mkdir /var/spool/sogo
 # chown sogo:sogo /var/spool/sogo
 # chmod 700 /var/spool/sogo

## SOGo user sources
## Active Directory
Modify the  file and add the LDAP user sources (and global address list). Place the following contents before the Web Interface section. If TLS is not configured for your Directory, exclude the "/????!StartTLS" strings at the end of the LDAP URIs:

   /* User Authentication */
   SOGoUserSources = (
    {
       type = ldap;
       CNFieldName = cn;
       UIDFieldName = sAMAccountName;
       IDFieldName = sAMAccountName;
       bindFields = (sAMAccountName);
       baseDN = "dc=internal,dc=domain,dc=tld";
       bindDN = "cn=ldap,cn=Users,dc=internal,dc=domain,dc=tld";
       bindPassword = "ldapPW";
       canAuthenticate = YES;
       displayName = "Active Directory";
       hostname = ldap://server.internal.domain.tld:389/????!StartTLS;
       id = directory;
       isAddressBook = NO;
     },
     {
       type = ldap;
       CNFieldName = cn;
       UIDFieldName = mail;
       IDFieldName = mail;
       baseDN = "dc=internal,dc=domain,dc=tld";
       bindDN = "cn=ldap,cn=Users,dc=internal,dc=domain,dc=tld";
       bindPassword = "ldapPW";
       hostname = ldap://server.internal.domain.tld:389/????!StartTLS;
       filter = "((NOT isCriticalSystemObject='TRUE') AND (mail=\'*\') AND (NOT objectClass=contact))";
       //Uncomment to list local users in WebUI without searching (small directories only)
       //listRequiresDot = NO;
       canAuthenticate = NO;
       displayName = "Shared Addressbook";
       hostname = ldap://server.internal.domain.tld:389/????!StartTLS;
       id = sambaShared;
       isAddressBook = YES;
     },
     {
       type = ldap;
       CNFieldName = cn;
       UIDFieldName = mail;
       IDFieldName = mail;
       baseDN = "dc=internal,dc=domain,dc=tld";
       bindDN = "cn=ldap,cn=Users,dc=internal,dc=domain,dc=tld";
       bindPassword = "ldapPW";
       filter = "((((objectClass=person) AND (objectClass=contact) AND ((uidNumber>=2000) OR (mail='*')))
                AND (NOT isCriticalSystemObject='TRUE') AND (NOT showInAdvancedViewOnly='TRUE') AND (NOT uid=Guest))
                OR (((objectClass=group) AND (gidNumber>=2000)) AND (NOT isCriticalSystemObject='TRUE')
                AND (NOT showInAdvancedViewOnly='TRUE')))";
       mapping = {
           displayname = ("cn");
       //Uncomment to list contacts in WebUI without searching (few contacts only)
       //listRequiresDot = NO;
       canAuthenticate = NO;
       displayName = "Shared Contacts";
       hostname = ldap://server.internal.domain.tld:389/????!StartTLS;
       id = sambaContacts;
       isAddressBook = YES;
       };
     }
   );

## Maria DB
For debugging purposes, edit the  to enable all debugging switches:

  /* Debug */
  SOGoDebugRequests = YES;
  SoDebugBaseURL = YES;
  ImapDebugEnabled = YES;
  LDAPDebugEnabled = YES;
  PGDebugEnabled = YES;
  MySQL4DebugEnabled = YES;
  SOGoUIxDebugEnabled = YES;
  WODontZipResponse = YES;
  WOLogFile = /var/log/sogo/sogo.log;

If problems occur, check by running  as root.

Further modify the  file to include SQL as a user source (change the password to the chosen password for the sogo mysql user):

   SOGoUserSources =
     (
       {
         type = sql;
         id = directory;
         viewURL = "mysql://sogo:yoursogopassword@127.0.0.1:3306/sogo/sogo_users";
         canAuthenticate = YES;
         isAddressBook = YES;
         userPasswordAlgorithm = md5;
       }
     );

Alternatively, a view can be used instead of the table directly. More information about which values are available for SOGoUserSources can be found here: https://sogo.nu/files/docs/SOGoInstallationGuide.html#_authentication_using_sql

## OpenLDAP
To be added...

## PostgreSQL
To be added...

## Completing configuration
Now enable and start the  service and restart the  service. Test by visiting http://server.internal.domain.tld/SOGo/ .

## ActiveSync configuration
## Apache
To add ActiveSync support, simply uncomment the following lines in :

 ...
 ProxyPass /Microsoft-Server-ActiveSync \
  http://127.0.0.1:20000/SOGo/Microsoft-Server-ActiveSync \
  retry=60 connectiontimeout=5 timeout=3600
 ...

This will result in extended locking delays if you have more than a handful of users, so some tuning is required. You may notice that the above line was changed from 360 seconds to 3600 seconds (or one hour). This is because EAS devices need to keep their HTTP connections open for very long times (up to one hour). Because of this, you will need to tell SOGo (see below) to honor that timeout. Reload the  service before continuing.

## nginx
Add the following to your server definition for SOGo in :

 ...
         location ^~ /Microsoft-Server-ActiveSync {
                 proxy_pass http://127.0.0.1:20000/SOGo/Microsoft-Server-ActiveSync;
                 proxy_redirect http://127.0.0.1:20000/Microsoft-Server-ActiveSync /;
         }

         location ^~ /SOGo/Microsoft-Server-ActiveSync {
                 proxy_pass http://127.0.0.1:20000/SOGo/Microsoft-Server-ActiveSync;
                 proxy_redirect http://127.0.0.1:20000/SOGo/Microsoft-Server-ActiveSync /;
         }
 ...

Additional tuning may be required for the parameters in the SOGo section below (timeout, retry, and next host values, specifically).

## SOGo
As stated above for the listed HTTP servers, some tuning is required to use EAS. While the timeouts below (59 minutes) are appropriate for the HTTP session timeout set above, the number of workers is dependent on the number of simultaneous EAS clients you must support. In short, you will always need more workers than EAS clients to allow start of another worker for push operations. Additionally, the sync interval will allow you to reduce the load on the server so that less delay is generated, and this dependent on the total number of clients. The SOGo configuration guide, available at https://sogo.nu/files/docs/SOGoInstallationGuide.pdf, lists two example configurations. The 100 user with 10 EAS users example was chosen for this article. Append the following lines to  making sure that they are placed before the closing brace ("}") character:

   /* ActiveSync */
   WOWorkersCount = 15;
   WOWatchDogRequestTimeout = 59;
   SOGoMaximumPingInterval = 3540;
   SOGoMaximumSyncInterval = 3540;
   SOGoInternalSyncInterval = 30;

Finally, restart the  service.
