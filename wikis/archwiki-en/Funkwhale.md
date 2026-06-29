# Funkwhale

Quoting the main documentation page:
:Funkwhale is a self-hosted, modern, free and open-source music server, heavily inspired by Grooveshark.

Instances can be federated via the ActivityPub protocol.

## Installation
Funkwhale requires a reverse proxy (so nginx or Apache HTTP Server need to be installed.

It also needs a configured PostgreSQL database and a Redis cache server.
See #Configuration and the respective pages for information.

Install the  package.

## Manual install
Follow instructions at [https://docs.funkwhale.audio/installation/debian.html.
This will install all components in .

## Docker install
Follow instructions at == Configuration ==

The following sections assume  was installed,
for a manual installation the folders should be changed appropriately.

It also assumes that you are using Funkwhale on a local network.
See the official [https://docs.funkwhale.audio/index.html documentation for making it accessible outside,
especially for the certificates using Certbot.

## Host config
Make sure your  file is setup correctly.
The Funkwhale server is running on  with alias , but this can be changed.

Your  file should look something like the following,

## Configure nginx
The upstream template of the Nginx configuration file is provided in .
However, this file contains variables that need to be replaced by their value from the  file
(see section #Initialization on how to create this file):

 $ set -a && source /srv/funkwhale/config/env && set +a
 $ envsubst "`env | awk -F = '{printf \" $%s\", $$1}'`" \
     /etc/nginx/sites-available/funkwhale.conf

The paths to the certificates should also be modified accordingly.

Then enable the site:

 $ ln -s /etc/nginx/sites-available/funkwhale.conf /etc/nginx/sites-enabled/

And start the .

## Configure apache
A template Apache configuration file is provided in . It configures the Funkwhale instance to be accessible at .

The folder names should be change to fit your installation. More explanation on which lines need to be modified is provided in Copy the template to the apache configuration folder,

 $ cp /etc/webapps/funkwhale/apache-funkwhale.conf /etc/httpd/conf/extra/funkwhale.conf

Next, edit the Apache HTTP Server configuration file and add the following:

For the changes to be applied, you need to restart  (Apache).

## Configure PostgreSQL
Connect to the PostgreSQL command line using the  user to create the  user and the database.

The last three lines load the  and  extensions,
which are needed for funkwhale to work ( since version 0.20).

## Initialization
## Funkwhale user
Funkwhale should run as the  user. It is automatically created by the AUR package.
If you followed the manual installation, create it with

 # useradd -r -d /srv/funkwhale -m funkwhale -c "Funkwhale music server" -s /usr/bin/nologin

Create Funkwhale's data folders in ,
owned by the  user:

 # mkdir /srv/funkwhale
 # chown funkwhale:funkwhale /srv/funkwhale

Run the following commands as the  user.

Create sub-folders for API files and storage:

 [funkwhale$ cd /srv/funkwhale
 mkdir -p api data/static data/media data/music config

To work, Funkwhale needs several environment variables to be present, these should be defined in the environment file .
There is a template at , copy and modify it to fit your installation.

 [funkwhale$ cp /etc/webapps/funkwhale/env.template /srv/funkwhale/config/env

The  variable should correspond to the hostname in .
 needs also to match the address where the funkwhale instance will be reached.
You should generate a unique  and change the paths accordingly to your installation.

## Database setup
Use  to run the  command as  user.

Initialize the database before launching the application:

 funkwhale_manage migrate

Create a superuser for your Funkwhale instance:

 [funkwhale$ funkwhale_manage createsuperuser

Collect the static files for the webapp:

 funkwhale$ funkwhale_manage collectstatic

## Version upgrade
In case of an error, use the  script to run the  commands (it should be run as root).

## Usage
Upstream provides systemd services that are already installed.

To start the instance, just start .

This starts three services, you can check their status with:

 $ systemctl status funkwhale-\*

## Troubleshooting
See https://docs.funkwhale.audio/administrator/troubleshooting/index.html

## Proxy logs
Apache logs for funkwhale:

 $ tail -f /var/log/httpd/funkwhale/error.log
