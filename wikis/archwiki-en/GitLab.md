# GitLab

From GitLab's homepage:

:GitLab offers git repository management, code reviews, issue tracking, activity feeds and wikis. Enterprises install GitLab on-premise and connect it with LDAP and Active Directory servers for secure authentication and authorization. A single GitLab server can handle more than 25,000 users but it is also possible to create a high availability setup with multiple active servers.

An example live version can be found at GitLab.com.

## Installation
GitLab requires Valkey and a database backend. If you plan to run it on the same machine, first install PostgreSQL.

Install the  package.

Finally, a web server has to be installed and configured. The configuration for GitLab will be discussed in the #Web server configuration section.

## Configuration
## Preliminary notes
GitLab is composed of multiple components, see the architecture overview page.

The  package installs GitLab's files in a manner that more closely follow standard Linux conventions:

{| class="wikitable"
! Description
! GitLab's Official
!
|----------------------------------------------------------
| Application Code
|
|
|----------------------------------------------------------
| Application Data
|
|
|----------------------------------------------------------
| User (Home Directory)
|  ()
|  ()
|----------------------------------------------------------
| Configuration File GitShell
|
|
|----------------------------------------------------------
| Configuration File GitLab
|
|
|----------------------------------------------------------
| Logs
|
|
|----------------------------------------------------------
| Unix socket files / PID files
|
|
|}

## GitLab
Edit  and setup at least the following parameters:

Hostname: In the  section set  - replacing  to  (no  or trailing slash) - into your fully qualified domain name.

Port:  can be confusing. This is not the port that the GitLab server (Puma) runs on; it is the port that users will initially access through in their browser. Basically, if you intend for users to visit  in their browser, without appending a port number to the domain name, leave  as . If you intend your users to type something like  into their browsers, then you would set  to . You will also have to configure your webserver to listen on that port.

Timezone (optional): The  parameter is optional, but may be useful to force the zone of GitLab applications.

Based on the table in #Preliminary notes above, the following paths have to be configured in . The GitLab FOSS repo has a full example which includes field descriptions:

*
*  section:
*  section (if enabled):
*  section (if enabled):
*  section (if enabled):
*  section (if enabled):
*  section (if enabled):
*  section (if enabled):
*  section (if enabled):
*  section (if enabled):
*  section (if enabled):

## Custom port for Puma
GitLab Puma is the main component which processes most of the user requests. By default, it listens on the  UNIX socket which can be changed in the  file.

To configure Puma to listen on a TCP port as well as UNIX socket:

If the Puma address is changed, the configuration of other components which communicate with Puma have to be updated as well:

* For GitLab Shell, update the  variable in  and  in the  section in .
:
* For GitLab Workhorse, edit the  and update the  option. See for details.

## Secret strings
Make sure that the files  and  files contain something. Their content should be kept secret because they are used for the generation of authentication tokens etc.

For example, random strings can be generated with the following commands:

 # hexdump -v -n 64 -e '1/1 "%02x"' /dev/urandom > /etc/webapps/gitlab/secret
 # chmod 640 /etc/webapps/gitlab/secret

 # hexdump -v -n 64 -e '1/1 "%02x"' /dev/urandom > /etc/webapps/gitlab-shell/secret
 # chmod 640 /etc/webapps/gitlab-shell/secret

Also fill in (new) secret strings for  described in [https://gitlab.com/gitlab-org/gitlab-foss/-/blob/master/doc/development/application_secrets.md#secret-entries application_secrets.md:

## Valkey
In order to provide sufficient performance you will need a cache database. Install and configure a Valkey instance, being careful to the section dedicated to listening via a socket.

Add the  user to the  user group and update these configuration files:

## PostgreSQL database
A PostgreSQL database will be required before Gitlab can be run.

Login to PostgreSQL and create the  database along with its user. Remember to change  and  to the real values:

 # psql -d template1

Try connecting to the new database with the new user to verify it works:

 $ psql -d gitlabhq_production -U your_username_here -W

Open the new  and set the values for  and . For example:

For our purposes (unless you know what you are doing), you do not need to worry about configuring the other databases listed in . We only need to set up the production database to get GitLab working.

## Initialize Gitlab database
Start the Valkey server and the  before initializing the database.

Initialize the database and activate advanced features:

 $ cd /usr/share/webapps/gitlab
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:setup

You can set the Administrator/root password and email by supplying them in the  and  environment variables, respectively, as seen below. If you do not set the password (and it is set to the default one), do not expose GitLab to the public internet until the installation is done and you have logged into the server the first time. During the first login, you are forced to change the default password. An Enterprise Edition license may also be installed at this time by supplying a full path in the  environment variable.

 $ cd /usr/share/webapps/gitlab
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:setup GITLAB_ROOT_PASSWORD=yourpassword GITLAB_ROOT_EMAIL=youremail GITLAB_LICENSE_FILE=/path/to/license

Finally run the following commands to check your installation:

 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:env:info
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:check

## Adjust modifier bits
(The gitlab check will not pass if the user and group ownership is not configured properly)

 # chmod -R ug+rwX,o-rwx /var/lib/gitlab/repositories/
 # chmod -R ug-s /var/lib/gitlab/repositories
 # find /var/lib/gitlab/repositories/ -type d -print0 | xargs -0 chmod g+s

## Web server configuration
To access GitLab from an outside network, the upstream documentation recommends to use an established web server as a proxy. All queries from the web server to GitLab are processed by GitLab Workhorse, which decides how they should be processed. See for details.

## Nginx
See Nginx#Configuration for basic nginx configuration and Nginx#TLS for enabling HTTPS. The sample in this section also assumes that server blocks are managed with Nginx#Managing server entries.

Create and edit the configuration based on the following snippet. See the [https://gitlab.com/gitlab-org/gitlab-ce/tree/master/lib/support/nginx upstream GitLab repository for more examples.

{{hc|/etc/nginx/sites-available/gitlab|
upstream gitlab-workhorse {
  server unix:/run/gitlab/gitlab-workhorse.socket fail_timeout=0;
}

server {
  listen 80;                  # IPv4 HTTP
  #listen 443 ssl http2;      # uncomment to enable IPv4 HTTPS + HTTP/2
  #listen # uncomment to enable IPv6 HTTP
  #listen [:::443 ssl http2; # uncomment to enable IPv6 HTTPS + HTTP/2
  server_name example.com;

  access_log  /var/log/gitlab/nginx_access.log;
  error_log   /var/log/gitlab/nginx_error.log;

  #ssl_certificate ssl/example.com.crt;
  #ssl_certificate_key ssl/example.com.key;

  location ~ ^/(assets)/ {
    root /usr/share/webapps/gitlab/public;
    gzip_static on; # to serve pre-gzipped version
    expires max;
    add_header Cache-Control public;
  }

  location / {
      # unlimited upload size in nginx (so the setting in GitLab applies)
      client_max_body_size 0;

      # proxy timeout should match the timeout value set in /etc/webapps/gitlab/puma.rb
      proxy_read_timeout 60;
      proxy_connect_timeout 60;
      proxy_redirect off;

      proxy_set_header Host $http_host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;

      #proxy_set_header X-Forwarded-Ssl on;

      proxy_pass http://gitlab-workhorse;
  }

  error_page 404 /404.html;
  error_page 422 /422.html;
  error_page 500 /500.html;
  error_page 502 /502.html;
  error_page 503 /503.html;
  location ~ ^/(404|422|500|502|503)\.html$ {
    root /usr/share/webapps/gitlab/public;
    internal;
  }
}
}}

## Apache
Install and configure the Apache HTTP Server and Apache HTTP Server#TLS for enabling HTTPS. You can use these upstream recipes to get started with the configuration file for GitLab's virtual host.

Notice that the SSL virtual host needs a specific IP instead of generic. Also if you set a custom port for Puma, do not forget to set it at the  line.

The following Apache modules must also be loaded in the configuration file :

If an Apache configuration via unix socket for the  is desired, the following configuration is functional:

{{hc|/etc/httpd/conf/extra/gitlab.conf|

    ServerName SERVERNAME
    ServerAlias SERVERNAME
    DocumentRoot /usr/share/webapps/gitlab/public

        Options FollowSymlinks
        AllowOverride all
        Require all granted

        Alias / /usr/share/webapps/gitlab/public/

        Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains; preload"

    ProxyPreserveHost On
    SSLProxyEngine on
    AllowEncodedSlashes NoDecode

        ProxyPass unix:/run/gitlab/gitlab-workhorse.socket|http://127.0.0.1/ nocanon
        ProxyPassReverse unix:/run/gitlab/gitlab-workhorse.socket|http://127.0.0.1/

        ProxyPass unix:/run/gitlab/gitlab-workhorse.socket|ws://127.0.0.1/-/cable
        ProxyPassReverse unix:/run/gitlab/gitlab-workhorse.socket|ws://127.0.0.1/-/cable

    #
    RewriteEngine on
    RewriteCond %{DOCUMENT_ROOT}/%{REQUEST_FILENAME} !-f RewriteCond %{REQUEST_URI} ^/uploads/.*
    RewriteRule .* unix:/run/gitlab/gitlab-workhorse.socket|http://127.0.0.1%{REQUEST_URI} [P,QSA,NE
    RequestHeader set X_FORWARDED_PROTO 'https'
    RequestHeader set X-Forwarded-Ssl on
    #
    ErrorDocument 404 /404.html
    ErrorDocument 422 /422.html
    ErrorDocument 500 /500.html
    ErrorDocument 503 /deploy.html
    ErrorLog /var/log/httpd/gitlab.lan.info-error_log
    CustomLog /var/log/httpd/gitlab.lan.info-access_log common
Include /etc/letsencrypt/options-ssl-apache.conf
SSLCertificateFile /etc/letsencrypt/live/SERVERNAME/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/SERVERNAME/privkey.pem

    ServerName SERVERNAME
    Redirect / https://SERVERNAME
RewriteEngine on
RewriteCond %{SERVER_NAME} =SERVERNAME
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} }}

A working example with tcp network connection (certbot flavor) assuming that  contains  on the  line:

{{hc|/etc/httpd/conf/extra/gitlab.conf|

    ServerName SERVERNAME
    ServerAlias SERVERNAME
    DocumentRoot /usr/share/webapps/gitlab/public

        Options FollowSymlinks
        AllowOverride all
        Require all granted

        Alias / /usr/share/webapps/gitlab/public/

        Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains; preload"

    ProxyPreserveHost On
    SSLProxyEngine on
    AllowEncodedSlashes NoDecode

        ProxyPassReverse http://127.0.0.1:8181
        ProxyPassReverse http://SERVERNAME

        ProxyPassReverse http://127.0.0.1:8181
        ProxyPassReverse http://SERVERNAME

    #
    RewriteEngine on
    RewriteCond %{DOCUMENT_ROOT}/%{REQUEST_FILENAME} !-f [OR
    RewriteCond %{REQUEST_URI} ^/uploads/.*
    RewriteRule .* http://127.0.0.1:8181%{REQUEST_URI} RequestHeader set X_FORWARDED_PROTO 'https'
    RequestHeader set X-Forwarded-Ssl on
    #
    ErrorDocument 404 /404.html
    ErrorDocument 422 /422.html
    ErrorDocument 500 /500.html
    ErrorDocument 503 /deploy.html
    ErrorLog /var/log/httpd/gitlab.lan.info-error_log
    CustomLog /var/log/httpd/gitlab.lan.info-access_log common
Include /etc/letsencrypt/options-ssl-apache.conf
SSLCertificateFile /etc/letsencrypt/live/SERVERNAME/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/SERVERNAME/privkey.pem

    ServerName SERVERNAME
    Redirect / https://SERVERNAME
RewriteEngine on
RewriteCond %{SERVER_NAME} =SERVERNAME
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent

}}

## Node.js
You can easily set up an HTTPS proxy on port 443 to proxy traffic to the GitLab Workhorse using http-master for Node.js. http-master is built on top of node-http-proxy.

## HTTPS/SSL
## Change GitLab configs
Modify  so the URL to your GitLab site starts with . Modify  so that  setting is set to .

## Let's Encrypt
To validate your URL, the Let's Encrypt process will try to access your GitLab server via a URL such as . Hence, you need to make sure that requests to the  subdirectory are not proxied to GitLab Workhorse. This can be done easily with the Certbot's "webroot" method, see Certbot#Webroot for details.

## Firewall
If you want to give direct access to your Gitlab installation through an iptables firewall, you may need to adjust the port and the network address:

 # iptables -A tcp_inbound -p TCP -s 192.168.1.0/24 --destination-port 80 -j ACCEPT

If you are behind a router, do not forget to forward this port to the running GitLab server host, if you want to allow WAN access.

## Start and test GitLab
Make sure PostgreSQL and Valkey are running and setup correctly.

Then start/enable .

Now test your GitLab instance by visiting http://localhost or , where  is the port number on which your web server listens. You should be prompted to create a password:

See #Troubleshooting and log files inside the  directory for troubleshooting.

## Upgrade database on updates
## Manual method
After updating the  package, it is required to upgrade the database:
 $ cd /usr/share/webapps/gitlab
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake db:migrate

Afterwards, reload and restart , ,  and .

## Automatic method
You can create pacman hooks to automate database upgrades on GitLab package updates. Create the three following files, do not forget to make the shell script executable:

## Advanced configuration
## Basic SSH
After completing the basic installation, set up SSH access for users. Configuration for OpenSSH is described below. Other SSH clients and servers will require different modifications.

For tips on adding user SSH keys, the process is well-documented on the GitLab website. You can check the administrator logs at  to confirm user SSH keys are being submitted properly. Behind the scenes, GitLab adds these keys to its authorized_keys file in .

The common method of testing keys (e.g. ) requires a bit of extra configuration to work correctly. The user configured in  (by default ) must be added to the server's sshd configuration file, in addition to a handful of other changes:

If your  contains the  option, then the  user should be added to the list:

After updating the configuration file, restart the .

Test user SSH keys (optionally add -v to see extra information):

 $ ssh -T gitlab@your_server

## Custom SSH connection
If you are running SSH on a non-standard port, you must change the GitLab user's SSH config:

You also need to change the corresponding options (e.g. ssh_user, ssh_host, admin_uri) in the  file.

## Sending emails from GitLab
GitLab can send emails either using a local mail transfer agent (via sendmail) or using SMTP.

To use sendmail, edit  and comment out all lines. Then mail delivery should work without any further configuration in GitLab, assuming that the local mail transfer agent is configured properly.

To use SMTP, configure the options in  according to your mail server. For example, to send via Gmail:

{{hc|/etc/webapps/gitlab/smtp_settings.rb|
if Rails.env.production?
  Gitlab::Application.config.action_mailer.delivery_method = :smtp

  ActionMailer::Base.delivery_method = :smtp
  ActionMailer::Base.smtp_settings = {
    address:              'smtp.gmail.com',
    port:                 587,
    domain:               'gmail.com',
    user_name:            'username@gmail.com',
    password:             'application password',
    authentication:       'plain',
    enable_starttls_auto: true
  }
end
}}

## Useful tips
## Rake tasks
A number of setup/maintenance/etc tasks are available through rake. To list them, go to Gitlab's home directory:

 $ cd /usr/share/webapps/gitlab

and run:

## Backup and restore
Create a backup of the gitlab system:

 $ cd /usr/share/webapps/gitlab
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:backup:create

Restore the previously created backup file :

 $ cd /usr/share/webapps/gitlab
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:backup:restore BACKUP=1556571328_2019_04_29_11.10.2

## Enable fast SSH key lookup
Enable Fast SSH Key Lookup as explained in this page: https://docs.gitlab.com/ee/administration/operations/fast_ssh_key_lookup.html

In short, edit .

Revert all changes done following this wiki (or revert  from the  package) and only add:

 AuthorizedKeysCommand /var/lib/gitlab/gitlab-shell/bin/gitlab-shell-authorized-keys-check gitlab %u %k
 AuthorizedKeysCommandUser gitlab

Finally restart the .

## Rails console
Rails console can be used to interface directly with GitLab. See for details.

To access Rails console:

 $ cd /usr/share/webapps/gitlab
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rails console

From here you can troubleshoot problems or do administration tasks like [https://docs.gitlab.com/ee/security/reset_user_password.html#use-a-rails-console resetting user passwords.

## Troubleshooting
## HTTPS is not green (gravatar not using https)
Valkey caches gravatar images, so if you have visited your GitLab with http, then enabled https, gravatar will load up the non-secure images. You can clear the cache by doing

 $ cd /usr/share/webapps/gitlab
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake cache:clear

as the gitlab user.

## Errors after updating
After updating the package from the AUR, the database migrations and asset updates will sometimes fail. These steps may resolve the issue, if a simple reboot does not.

First, move to the gitlab installation directory.
 $ cd /usr/share/webapps/gitlab

If every gitlab page gives a 500 error, then the database migrations and the assets are probably stale. If not, skip this step.
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake db:migrate

If gitlab is constantly waiting for the deployment to finish, then the assets have probably not been recompiled.
 $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:assets:clean gitlab:assets:compile cache:clear

Finally, restart ,  and .

## GitLab Puma cannot access non-default repositories directory
If a custom repository storage directory is set in , disable the  parameter in the  (see systemd#Drop-in files and the relevant forum thread on gitlab.com).

## Failed to connect to Gitaly
Sometimes, the Gitaly service will not get started, leaving GitLab unable to connect to Gitaly. The solution is simple: start .

## CSS or styles issue
If you have any issues with styles and CSS not working, you may try to edit  and change:

  # Disable Rails's static asset server (Apache or nginx will already do this)
  config.public_file_server.enabled = false

to:

  # Disable Rails's static asset server (Apache or nginx will already do this)
  config.public_file_server.enabled = true

## The server does not support push options
If you get an error like  you might need to enable it for the GitLab Git user () on the server. This can be done in the gitconfig:

Alternatively one can set this with:

 $ sudo -u gitlab -H git config --global receive.advertisePushOptions true
