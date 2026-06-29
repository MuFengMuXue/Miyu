# Gitea

Gitea is a community managed fork of Gogs, lightweight code hosting solution written in Go and published under the MIT license.

## Installation
Install the  or  package.

Gitea requires the use of a database backend, the following are supported:

* MariaDB/MySQL
* PostgreSQL
* SQLite
* MSSQL

## Configuration
The user configuration file is located at .

See the Gitea docs for more configuration examples.

## PostgreSQL
Install and configure PostgreSQL.

Choose between TCP or UNIX Socket, and jump to the corresponding section.

## With TCP socket
Create the new user while connecting to the server as  user (you will be prompted for a password for the new user):

 createuser -P gitea

Create the Gitea database, owned by  user:

 [postgres$ createdb -O gitea gitea

PostgreSQL#Configure PostgreSQL to be accessible from remote hosts

Verify it works:

 $ psql --host=ip_address --dbname=gitea --username=gitea --password

Configure Gitea either through the first-run installer or update :

## With Unix socket
Create the new user while connecting to the server as  user:

 createuser gitea

Create the Gitea database, owned by  user:

 [postgres$ createdb -O gitea gitea

Setup the Unix socket by adding the following line to :

Restart .

Verify it works:

 psql --dbname=gitea --username=gitea

Configure Gitea either through the first-run installer or update :

## MariaDB/MySQL
The following is an example of setting up MariaDB, setting your desired password:

Try connecting to the new database with the new user:

 $ mysql -u gitea -p -D gitea

Configure MariaDB either through the first-run installer or update :

## Usage
Start/enable , the webinterface should listen on .

When running Gitea for the first time, it should redirect to .

## Tips and tricks
## Local Shell Client (tea)
With  you can use the official cli-client of gitea.
More information can be found at https://gitea.com/gitea/tea

## Enable SSH Support
Make sure SSH is properly configured and running.

## Setup your domain
You might want to set , e.g.:

## Configure SSH
By default, Gitea will run as the user ; this account will also be used for ssh repository access.
By default this user will be expired and you may encounter an error when authenticating:
"Your account has expired; please contact your system administrator".

Use chage to remove the expiration condition, e.g. as follows:
 # chage -E -1 gitea

For ssh access to work, you have to enable PAM. Alternatively, you might have to unlock service account.

If you use  in your SSH configuration, add  to it, e.g.:

Restart  if you use it (nothing to do if you use ).

## Disable HTTP protocol
By default, the ability to interact with repositories by HTTP protocol is enabled.
You may want to disable HTTP-support if using SSH, by setting  to .

## Binding on restricted ports
If you use the built-in SSH server and want Gitea to bind it on port 22, or if you want to bind Gitea webserver directly on ports 80/443 (that is in a setup without proxy), you will need to add a drop-in systemd unit override:

## Enable Dark Theme
In the ui section, you can set the  to  for making the web interface use a dark background.

## Customize the appearance of Gitea
See the Gitea docs[https://docs.gitea.io/en-us/administration/customizing-gitea/ for more detail.

The appearance of gitea is highly customizable using Go templates.
First, create the  directory.
Templates can be overridden by editing files in .
The default templates can be found in the Gitea source code under the  directory. For instance, to customize the home page, copy  from the source code to  and edit the template as desired.

In addition, the logo and favicon can be changed by creating the following files:  and

Gitea needs to be restarted after any changes to these files.

## Configure reverse proxy
For additional information and examples, see the Reverse Proxies section on the Gitea documentation website ==== nginx ====

The following is an example of using nginx as reverse proxy for Gitea over unix socket (you need to provide the SSL certificate):

{{hc|/etc/nginx/servers-available/gitea.conf|2=
server {
    listen 443 ssl http2;
    listen [:::443 ssl http2;
    server_name git.domain.tld;

    ssl_certificate /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;

    location / {
        client_max_body_size 512M;
        proxy_pass http://unix:/run/gitea/gitea.socket;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
}}

Update the  and  section of :

## Apache HTTP Server
The following is an example of using the Apache HTTP Server as reverse proxy for Gitea over unix socket.
To forward  to the gitea server, use

where  should be replaced by your domain name (this entry is only passed as a header to the proxy, and does not seem to matter for this setup).

To forward a subpath such as  to the gitea server, use

## Setup for custom data directory
As of now, you cannot use a custom path like  as your server home, since the shipped  unit file marks everything read-only.

To enable these custom paths, create a drop-in snippet with your server home directory as a new  directive:

Then do a daemon-reload and restart  for the changes to take effect.

## Troubleshooting
## Database error on startup after upgrade to 1.5.0
A problem can appear after the upgrade to 1.5.0. The service will not start, and the following error is present in the logs:

To fix this problem, run the following command as the `root` user on your MySQL/MariaDB server

gitea should stop complaining about key size and startup properly.

## Service failing with permission denied
If you manually create the  user with a usual home folder  the gitea service will not start and output an error like :

 Sep 04 04:44:32 systemdgitea.service: Failed with result 'exit-code'.
 Sep 04 04:44:32 systemd[1: gitea.service: Main process exited, code=exited, status=200/CHDIR
 Sep 04 04:44:32 (gitea)gitea.service: Failed at step CHDIR spawning /usr/bin/gitea: Permission denied
 Sep 04 04:44:32 (gitea)[30727: gitea.service: Changing to the requested working directory failed: Permission denied

The service needs the home folder of the user to be the main gitea folder, the default being  a fix would be:

 $ usermod -d /var/lib/gitea gitea
