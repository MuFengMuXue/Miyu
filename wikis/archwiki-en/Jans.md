# Jans

Janssen Project is an open source digital identity platform that provides an OAuth Authorization Server and a certified OpenID Connect Provider. It is an alternative to Keycloak.

## Jans Auth Server
A very complete Java OAuth Authorization Server and a certified OpenID Connect Provider.

## Installation
Install

## Configuration
Jans supports several Database backends LDAP, Couchbase. PostgreSQL, MySQL and Spanner.

Edit  and set  accordingly.

To create configuration, execute:
 # /usr/share/jans/bin/generate_config.sh auth example.org:8080

## LDAP
The best support is for OpenDJ, but you might be able to use OpenLDAP as well.

Update  with your LDAP settings:

 # sed -i "s|%(persistence_type)s|ldap|" /etc/jans/conf/jans.properties
 # sed -i "s|%(ldap_binddn)s|cn=Directory Manager|" /etc/jans/conf/jans-ldap.properties
 # sed -i "s|%(ldap_hostname)s:%(ldaps_port)s|127.0.0.1:1389|" /etc/jans/conf/jans-ldap.properties
 # sed -i "s|useSSL: true|useSSL: false|" /etc/jans/conf/jans-ldap.properties

 # sed -i "s|%(ldap_bind_encoded_pw)s|$(echo -n "YOUR_LDAP_PASSWORD_HERE" | openssl des-ede3-ecb -e -a -K $(cat "/etc/jans/conf/salt" | cut -d '=' -f 2 | xxd -p))|" /etc/jans/conf/jans-ldap.properties

Copy LDAP schema:
 # cp /usr/share/jans/schema-opendj/101-jans.ldif /var/lib/opendj/config/schema/

Load generated config in LDAP:

 #  opendj-ldapmodify -D "cn=Directory Manager" -p 1389 -w $PASSWORD /tmp/jansconfig/auth.ldif

## Web Server
## Jetty
Install

Add necessary modules:

 # java -jar /usr/share/jetty11/start.jar jetty.base=/etc/jetty11 --add-module=deploy,jsp,websocket-jakarta,logging-log4j2,http,console-capture

Install webapp:

 # ln -sf /etc/jans/jetty/start.d/jans.ini /etc/jetty11/start.d/jans.ini
 # ln -sf /etc/jans/jetty/webapps/jans-auth-server.xml /var/lib/jetty11/webapps/
 # ln -sf /etc/jans/jetty/webapps/agama_web_resources.xml /var/lib/jetty11/webapps/

Start/enable .

## Jans Config API
RESTful control plane for all Janssen components.

## Installation
Install

Available plugins:
*
*
*
*
*

## Configuration
Execute:
 # /usr/share/jans/bin/generate_config.sh config example.org:8080

## LDAP
 #  opendj-ldapmodify -D "cn=Directory Manager" -p 1389 -w $PASSWORD /tmp/jansconfig/config-api.ldif

## Web Server
## Jetty
Install webapp:

 # ln -sf /etc/jans/jetty/webapps/jans-config-api.xml /var/lib/jetty11/webapps/

## Jans SCIM
SCIM JSON/REST API for user management, including associated FIDO devices.

## Installation
Install  and  for Jans Config API.

## Configuration
Execute:
 # /usr/share/jans/bin/generate_config.sh scim example.org:8080

## LDAP
 #  opendj-ldapmodify -D "cn=Directory Manager" -p 1389 -w $PASSWORD /tmp/jansconfig/scim.ldif

## Web Server
## Jetty
Install webapp:

 # ln -sf /etc/jans/jetty/webapps/jans-scim.xml /var/lib/jetty11/webapps/

## Jans Text UI ("TUI")
Command-line and interactive configuration tools to help you correctly call the Config API.

## Installation
Install

## Configuration
Execute:
 # /usr/share/jans/bin/generate_config.sh cli example.org:8080

## LDAP
 #  opendj-ldapmodify -D "cn=Directory Manager" -p 1389 -w $PASSWORD /tmp/jansconfig/cli.ldif

## Jans FIDO
Enables end-users to enroll and authenticate with passkeys and other FIDO authenticators.

## Installation
Install  and  for Jans Config API.

## Configuration
Execute:
 # /usr/share/jans/bin/generate_config.sh fido2 example.org:8080

## LDAP
 #  opendj-ldapmodify -D "cn=Directory Manager" -p 1389 -w $PASSWORD /tmp/jansconfig/fido2.ldif

## Web Server
## Jetty
Install webapp:

 # ln -sf /etc/jans/jetty/webapps/jans-fido2.xml /var/lib/jetty11/webapps/

## Jans LDAP Link
A group of components that provide synchronization services to update the Janssen User Store from an external authoritative LDAP data source.

## Installation
Install  and  for Jans Config API.

## Configuration
Execute:
 # /usr/share/jans/bin/generate_config.sh link

## LDAP
 #  opendj-ldapmodify -D "cn=Directory Manager" -p 1389 -w $PASSWORD /tmp/jansconfig/link.ldif

## Web Server
## Jetty
Install webapp:

 # ln -sf /etc/jans/jetty/webapps/jans-link.xml /var/lib/jetty11/webapps/

## Jans SAML
## Installation
Install  for Jans Config API.

## Configuration
Execute:
 # /usr/share/jans/bin/generate_config.sh saml keycloak.example.org

## LDAP
 #  opendj-ldapmodify -D "cn=Directory Manager" -p 1389 -w $PASSWORD /tmp/jansconfig/saml.ldif

## Jans Casa
Jans Casa is a self-service web portal for end-users to manage authentication and authorization preferences for their account in the Janssen server.

## Installation
Install .

## Configuration
Execute:
 # /usr/share/jans/bin/generate_config.sh casa example.org:8080

## LDAP
 #  opendj-ldapmodify -D "cn=Directory Manager" -p 1389 -w $PASSWORD /tmp/jansconfig/casa.ldif

## Web Server
## Jetty
Add necessary modules:

 # java -jar /usr/share/jetty11/start.jar jetty.base=/etc/jetty11 --add-module=deploy,jsp,websocket-jakarta,logging-log4j2,http,console-capture,cdi-decorate

Install webapp:

 # ln -sf /etc/jans/jetty/webapps/casa.xml /var/lib/jetty11/webapps/
 # ln -sf /etc/jans/jetty/webapps/jans-casa_web_resources.xml /var/lib/jetty11/webapps/
