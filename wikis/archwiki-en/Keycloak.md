# Keycloak

Keycloak is an identity management solution implemented in Java that can be used as an authentication backend for many different applications.

## Installation
Install the  package.

## Running
Start/enable . In the default configuration, it will start in standalone mode which is not recommended for production environments but will be used in this article for the sake of simplicity.

By default, Keycloak is available on http://127.0.0.1:8080/ and https://127.0.0.1:8443/.

## Creating an admin user
As per upstream instructions, you have two ways to create the initial Keycloak admin user one is connecting to keycloak through http://localhost:8080 and the second is to add environment variables for username and password for the first launch.

To do the latter, override the unit:

Reload the systemd daemon, then restart the .

Afterwards, make sure to delete the override and daemon-reload again, as Keycloak will refuse to start up with the environment variables defined when the account already exists.

## Configuration
The default standalone configuration can be found at .

Any changes you make to this file while the server is running will not take effect and may even be overwritten by the server. Either stop the service beforehand, use the command line scripting or use the web console of WildFly.

The ports used by the service can found in that file, albeit in a slightly unusual format:

## H2 configuration
Keycloak's  file is preconfigured with two h2 datasources. One is "ExampleDS", and can be safely removed. The other is "KeycloakDS" and is used to store Keycloak's configuration. ( refers to  in the Keycloak package)

Example configuration parts for the H2 file-based database:

{{hc|/etc/keycloak/standalone.xml|

                    jdbc:h2:mem:test;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
                    h2

                        sa
                        sa

                    jdbc:h2:${jboss.server.data.dir}/keycloak;AUTO_SERVER=TRUE
                    h2

                        sa
                        sa

                        org.h2.jdbcx.JdbcDataSource

   ...

}}

## PostgreSQL configuration
The official Arch Linux Keycloak package already comes with inbuilt PostgreSQL support.

Example configuration parts for PostgreSQL:

## Keycloak Prometheus metrics
Install the  package. To enable the metrics listener endpoint

  /opt/keycloak/bin/kcadm.sh config credentials --server http://localhost:8080/auth --realm master --user $KEYCLOAK_ADMIN --password $KEYCLOAK_PASS
  /opt/keycloak/bin/kcadm.sh update events/config -s "eventsEnabled=true" -s "adminEventsEnabled=true" -s "eventsListeners+=metrics-listener"

The config command creates a kcadm.config file in the .keycloak directory of the user who runs the command. As contains an access token, it is recommend to remove the file after

  rm /home/$USER/.keycloak/kcadm.config

After restarting the metrics are available via http://localhost:8080/auth/realms/master/metrics
