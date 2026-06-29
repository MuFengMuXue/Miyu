# Immich

Immich is a high-performance self-hosted photo and video management solution that allows users to back-up, organize, search, and share personal media libraries. The project is actively developed and positions itself as a leading open-source, self-hosted Google Photos and iCloud (photo/videos only) alternative. See the official documentation for more.

Data sovereignty is a core principle: complete control of your photos and videos. Break free from proprietary (and potentially privacy-intrusive) services such as Google Photos.

Immich can be deployed on a live system or container by docker or by snap image. This article gives specific steps to deploy it on a live system.

## Installation
The main package to install is . Optionally,  enables Google-Photos-like intelligence including: the ability to use natural language search terms to find photos, facial recognition, and people group, duplicate detection, and optical character recognition (OCR).

## PostgreSQL setup
Immich uses PostgreSQL for database activities. Manual setup of the admin user and of the database is required. Below is a baseline example configuration, the steps of which have been summarized from PostgreSQL.

Initialize the database:

 initdb --locale=C.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data --data-checksums

Edit  by adding:

 shared_preload_libraries = 'vchord.so'

Start/enable the .

Interactively create the  user. For a typical install, answer  for the role name, then  for the remaining superuser/createdb/createrole prompts.

 [postgres$ createuser --interactive

Create the  database:

 createdb immich

Edit the password for the admin user, replacing  with your desired password:

## Reverse proxy setup
Immich requires a reverse proxy to handle TLS termination, load balancing, traffic flow, and other advanced features. While the project officially supports Nginx, Caddy, Apache, and , the AUR package provides a pre-configured nginx drop-in. To configure any of the other supported daemons, refer to the [https://docs.immich.app/administration/reverse-proxy/ documentation.

## Nginx setup
Edit  by inserting the following inside the {{ic|http {}}} block:

 include /etc/nginx/conf.d/*.conf;
 types_hash_max_size 4096;

Create a  directory and populate it with the package template:

 # mkdir /etc/nginx/conf.d
 # cp /usr/share/doc/immich/examples/nginx.conf /etc/nginx/conf.d/immich.conf

## Firewall configuration
By default the external tcp port 8080 will redirect to the immich default 2283. Update the firewall to allow 8080/tcp.

For example with ufw allowing traffic only from the LAN:

 # ufw allow from 192.168.1.0/24 to any port 8080 proto tcp

## Usage
Start and optionally enable the following services:  and . If the ML packages are installed, start .

To setup users, service defaults, trigger jobs, etc. browse to http://127.0.0.1:8080 or to http://immich.hostname:8080
