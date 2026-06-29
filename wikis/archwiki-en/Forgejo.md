# Forgejo

Forgejo is a hard fork of Gitea managed by the non-profit organization Codeberg, lightweight code hosting solution written in Go and published under the GPLv3+ license.

## Installation
Install the  or  package.

Forgejo requires the use of a database backend, the following are supported:

* PostgreSQL
* MariaDB/MySQL
* SQLite

## Configuration
The user configuration file is located at .

See the Forgejo docs for more configuration examples.

If you are migrating from Gitea see the migration guide for Forgejo

## PostgreSQL
Install and configure PostgreSQL.

Choose between TCP or UNIX Socket, and jump to the corresponding section.

## With TCP socket
Create the new user while connecting to the server as  user (you will be prompted for a password for the new user):

 createuser -P forgejo

Create the Forgejo database, owned by  user:

 [postgres$ createdb -O forgejo forgejo

PostgreSQL#Configure PostgreSQL to be accessible from remote hosts

Verify it works:

 $ psql --host=ip_address --dbname=forgejo --username=forgejo --password

Configure Forgejo either through the first-run installer or update :

## With Unix socket
Create the new user while connecting to the server as  user:

 createuser forgejo

Create the Forgejo database, owned by  user:

 [postgres$ createdb -O forgejo forgejo

Setup the Unix socket by adding the following line to :

Restart .

Verify it works:

 psql --dbname=forgejo --username=forgejo

Configure Forgejo either through the first-run installer or update :

## MariaDB/MySQL
The following is an example of setting up MariaDB, setting your desired password:

Try connecting to the new database with the new user:

 $ mysql -u forgejo -p -D forgejo

Configure MariaDB either through the first-run installer or update :

## SQLite
No specific configuration needed for SQLite itself.

Configure SQLite either through the first-run installer or update :

## Usage
Start/enable , the webinterface should listen on .

When running Forgejo for the first time, it should redirect to .

## Tips and tricks
## Local Shell Client (forgejo)
Forgejo comes packages with a local shell administration tool. Binary is located in

More information can be found at https://forgejo.org/docs/latest/admin/command-line/

## Enable SSH Support
Make sure SSH is properly configured and running.

## Setup your domain
You might want to set , e.g.:

## Configure SSH
By default, Forgejo will run as the user ; this account will also be used for ssh repository access.
By default this user will be expired and you may encounter an error when authenticating: "Your account has expired; please contact your system administrator".

Use chage to remove the expiration condition, e.g. as follows:
 # chage -E -1 forgejo

For ssh access to work, you have to enable PAM. Alternatively, you might have to unlock service account.

If you use  in your SSH configuration, add  to it, e.g.:

Restart  if you use it (nothing to do if you use ).

## Disable HTTP protocol
By default, the ability to interact with repositories by HTTP protocol is enabled.
You may want to disable HTTP-support if using SSH, by setting  to  in  under the  section.

## Binding on restricted ports
If you use the built-in SSH server and want Forgejo to bind it on port 22, or if you want to bind Forgejo webserver directly on ports 80/443 (that is in a setup without proxy), you will need to add a drop-in systemd unit override:

## Enable Dark Theme
In the ui section, you can set the  to  for making the web interface use a dark background.

## Customize the appearance of Forgejo
See the Forgejo docs[https://forgejo.org/docs/latest/developer/customization/ for more detail.

The appearance of forgejo is highly customizable using Go templates.
First, create the  directory.
Templates can be overridden by editing files in .
The default templates can be found in the Forgejo source code under the  directory. For instance, to customize the home page, copy  from the source code to  and edit the template as desired.

In addition, the logo and favicon can be changed by creating the following files:  and

Forgejo needs to be restarted after any changes to these files.

## Configure reverse proxy
For additional information and examples, see the Reverse Proxies section on the Forgejo documentation website ==== nginx ====

The following is an example of using nginx as reverse proxy for Forgejo over unix socket (you need to provide the SSL certificate):

{{hc|/etc/nginx/servers-available/forgejo.conf|2=
server {
    listen 443 ssl;
    listen [:::443 ssl;
    http2 on;
    server_name git.domain.tld;

    ssl_certificate /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;

    location / {
        client_max_body_size 512M;
        proxy_pass http://unix:/run/forgejo/forgejo.socket;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
}}

Update the  and  section of :

## Apache HTTP Server
The following is an example of using the Apache HTTP Server as reverse proxy for Forgejo over unix socket.
To forward  to the Forgejo server, use

where  should be replaced by your domain name (this entry is only passed as a header to the proxy, and does not seem to matter for this setup).

To forward a subpath such as  to the Forgejo server, use

## Setup for custom data directory
As of now, you cannot use a custom path like  as your server home, since the shipped  unit file marks everything read-only.

To enable these custom paths, create a drop-in snippet with your server home directory as a new  directive:

Then do a daemon-reload and restart  for the changes to take effect.

## Troubleshooting
## Service failing with permission denied
If you manually create the  user with a usual home folder  the forgejo service will not start and output an error like :

 Sep 04 04:44:32 systemdforgejo.service: Failed with result 'exit-code'.
 Sep 04 04:44:32 systemd[1: forgejo.service: Main process exited, code=exited, status=200/CHDIR
 Sep 04 04:44:32 (forgejo)forgejo.service: Failed at step CHDIR spawning /usr/bin/forgejo: Permission denied
 Sep 04 04:44:32 (forgejo)[30727: forgejo.service: Changing to the requested working directory failed: Permission denied

The service needs the home folder of the user to be the main forgejo folder, the default being  a fix would be:

 $ usermod -d /var/lib/forgejo forgejo
