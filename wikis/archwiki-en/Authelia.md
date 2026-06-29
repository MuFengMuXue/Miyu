# Authelia

Authelia is an open-source authentication and authorization server providing two-factor authentication and single sign-on (SSO) for applications via a web portal. It acts as a companion to reverse proxies like nginx, Caddy, Traefik, or HAproxy to enforce access control policies.

## Installation
Install the  package: it will create the  system user and group.

## Configuration
## Package-provided structure
The packages create  for configuration files and install tmpfiles.d configuration to manage permissions:

Place your main Authelia configuration at . See the Authelia documentation for configuration options.

## Recommended directory structure for file based storage
Authelia supports multiple options as storage provider and authentication backend. A simple dev setup could use sqlite3 for storage and a yaml file as user database. Such a file based setup does not support high availability scenarios. An RDBMS such as Postgresql and an LDAP server should be used in production scenarios to support high availability.

Following the Filesystem Hierarchy Standard, it is recommended to separate configuration from runtime application data should you want to use file based storage options for Authelia.

* Configuration (static):
* Application data (runtime state):

## Setting up the data directory
Create the data directory:

 # mkdir -p /var/lib/authelia
 # chown authelia:authelia /var/lib/authelia
 # chmod 0750 /var/lib/authelia

To use SQLite for storage, configure the database path in :

To use a file-based user database, you may also place it in :

## Securing with tmpfiles.d
To ensure proper permissions are maintained across reboots and during system updates, create a tmpfiles.d configuration for :

Apply the configuration immediately:

 # systemd-tmpfiles --create /etc/tmpfiles.d/authelia.conf

## Usage
Start/enable .

Check the service status:

 # systemctl status authelia

View logs:

 # journalctl -u authelia -f

## Troubleshooting
## Permission denied errors
If Authelia fails to start with permission errors, ensure:

# The  user has read access to configuration files
# The  user has read/write access to the data directory
# Directory permissions include the execute bit () for directories

Manually fix permissions:

 # chown -R authelia:authelia /etc/authelia /var/lib/authelia
 # chmod 0750 /etc/authelia /var/lib/authelia
 # chmod 0640 /etc/authelia/configuration.yml
 # chmod 0640 /var/lib/authelia/*

Then reapply tmpfiles configuration:

 # systemd-tmpfiles --create

## Configuration validation
Validate your configuration before starting the service:

 # authelia validate-config --config /etc/authelia/configuration.yml
