# Ente server

Ente server is the server part that stores and serves encrypted blobs of data to ente (mobile) clients. The clients send/receive encrypted data, which then arrives at the Ente server and is stored/read via the local MinIO object storage service.

For example when the Ente photos client is used, the client encrypts the photos, which are then stored on this server. Later on the client can then lookup the encrypted photos, and decrypt them locally (end-to-end encryption). Since only the client, or anyone the client shares the photos with, have the encryption key, only they can decrypt the data and actually see the photos, the server will never be able to do this due to the lack of that key material.

## Installation
The  package is meant for self hosting in contrary to the by default provided dockerized Ente server. If a dockerized or hosted solution is required, see ente.io.

Start by installing the  package.

Note that since self hosted server space is often available in limited quantity, the  package added the ability to change the cleanup delay cleanup before old unlinked ente-server MinIO objects will be actually deleted. This can be configured via the  ente-server configuration parameter. The default upstream Ente server cleans these objects every  by default, but when replication is not required, this setting can be set to cleanup every  for example.

To get the Ente server running a working PostgreSQL database (to store Ente object meta data and user data) and MinIO bucket (to store encrypted object data) is required. Furthermore, a HTTPS proxy like Nginx is recommended to be used to access the Ente server. Lastly, the ente-cli tool can be used to easily upgrade ente-server account size limit and account expiry.

These required components are listed as optional dependencies and should preferably be installed as dependencies: Pacman#Installation reason

## Configuration
## MinIO setup
Edit the configuration file as follows:

Enable/start .

Create MinIO ente-server bucket with the mcli command (as the minio user):

 # cd /srv/minio/data
 mcli mb -p ente-server

## PostgreSQL setup
Initialize the database as the postgres user:

 [postgres$ initdb --locale en_US.UTF-8 -D '/var/lib/postgres/data' --data-checksums --auth=scram-sha-256 --pwprompt -c listen_addresses=''

PostgreSQL#Configure PostgreSQL to be accessible exclusively through UNIX Sockets, in case of an existing PostgreSQL setup:

Restrict socket access to PostgreSQL user or group by editing :

Add  to the  user group, then start/enable.

Create PostgreSQL database user and a database owned by this user (specify new password twice, then specify postgres password to store new account):

 createuser -P ente

Then specify postgres password to create new database:

 [postgres$ createdb -T template0 -O ente -E unicode ente-server

## Running ente-server
Add MinIO bucket details:

Add PostgreSQL details:

Generate new secret key values using the ente-server-gen-random-keys command and use these values as a replacement of the default values in the  configuration file.

Edit  to allow it to access to the IP address of your_public_domain.tld (by default the service only allows access from and to localhost):

Enable/start .

## Configuring Nginx proxy
Copy the example MinIO and Ente server Nginx config and the accompanying  HTTP(S) security header config files to the Nginx configuration directory:

 # cp -v /usr/lib/ente-server/ente-server-nginx.conf /etc/nginx/
 # cp -v /usr/lib/ente-server/http*security_headers.conf /etc/nginx/
 # cp -v /usr/lib/ente-server/minio-server-nginx.conf /etc/nginx/

Edit this example config, and replace your_public_domain.tld with your actual public domain name

Request a letsencrypt certificate (or a TLS certificate from another provider) if not already done so:

 # certbot certonly --email your_email --agree-tos --preferred-challenge http --webroot -w /var/lib/letsencrypt -d your_public_domain.tld

Append an  statement to the Nginx  config to include the ente-server config:

{{hc|/etc/nginx/nginx.conf|
http {
    include /etc/nginx/ente-server-nginx.conf
}
}}

Fix permissions:

 # chmod 644 /etc/nginx/ente-server-nginx.conf
 # chmod 644 /etc/nginx/http*security_headers.conf

Restart  to apply the changes.

## Configuring ente-server and ente-cli
Install  on the client with the  package.

Add the  configuration on the client:

Add a user account via the Ente photos mobile, desktop or web app on the client, using a custom endpoint.

In the photos mobile app, click 7 times on the main screen to enable developers mode, then define your custom Ente server API endpoint:

 URL: https://your_public_domain.tld

In the web app on the client:

When using the desktop app using the  package, make sure you export the  environment variable before building.

Follow the photos mobile, desktop or web app (http://localhost:3000) instructions to create a new user.

Obtain the OTP code:

* Via email:
** Configure the  section in
** Make sure the configured  server is working
** Wait for the mail to arrive and copy the OTP code
* Via the ente-server log:
:

Obtain the new users account ID:

 # psql -U ente ente-server -c 'select user_id from users order by user_id desc limit 1;'

Configure this user as the admin:

Restart  to activate the new admin privileges.

Configure this admin within  on the client:

## Increasing user storage and account expiry limit
Use ente-cli to increase storage limit with 100 TB and expiry with 100 years:

 $ ente admin update-subscription -u "user@domain.tld"

## (Optional) Copy and apply AppArmor profile
An AppArmor profile has been provided for those that wish to limit the access the ente-server binary has using AppArmor. Copy and apply this profile as follows (assuming that AppArmor has already been installed and enabled):

## (Optional) Configure Firewall
If a host firewall like iptables or nftables has been enabled and configured, make sure the following is allowed:

* Traffic on
* Traffic from your Ente (mobile) client to TCP port  to reach the Ente server via Nginx
* Traffic from your Ente (mobile) client to TCP port  to reach the MinIO server via Nginx

## Files
The  package contains the  man page that lists and explains all files that are installed by this package.
