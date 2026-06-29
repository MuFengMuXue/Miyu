[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Mosquitto&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://mosquitto.org/)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/mosquitto)

[[]][GitHub](https://github.com/eclipse/mosquitto)

Mosquitto is an open source MQTT message broker provided by the Eclipse foundation.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [TLS (X509)]](#TLS_.28X509.29)
    -   [[2.3] [Service]](#Service)
        -   [[2.3.1] [OpenRC]](#OpenRC)
        -   [[2.3.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/mosquitto`

### [Additional software]

Libraries/ integration, e.g. Eclipse Paho.

## [Configuration]

### [Files]

-   [/etc/mosquitto/mosquitto.conf] - Global (system wide) configuration file.
-   [\~/.config/mosquitto_sub] - per user defaults for command mosquitto_sub
-   [\~/.config/mosquitto_pub] - per user defaults for command mosquitto_pub

** Warning**\
Force drop of root user and privileges by configuring *user mosquitto* in mosquitto.conf. Leaving this unconfigured runs the process as root.

** Warning**\
Do not enable PID file in mosquitto.conf as it conflicts with PID file of init script. Using *user* directive in combination with init-script\'s PID file crashes the service immediately. PID file created by init script is owned by root which *mosquitto* can not write.

** Warning**\
Secure the broker by either using a (self signed) X509 certificate for TLS or pre shared key TLS. Without TLS communication is unencrypted. Credentials are transferred as plain text. Also setup access control for topics and at least one authorization schema:

-   user/ password with mosquitto_passwd, set permission on the file so that only user mosquitto can read it: chmod 400
-   mutual TLS, listener forces all clients to provide a certificate
-   dynamic security plugin

Without any means of authorization and or access control anybody can publish to any topic. This affects the entire host if for example high message volume exhausts host resources.

Listeners:

-   have at least a single *listener* so remote connections are possible
-   specify the network interface with *bind_interface* to if only one out of many is allowed
-   configure multiple listeners with enabled per-listener-configuration to separate contexts or shard traffic

Security:

-   memory_limit to avoid resource exhaustion
-   message_size_limit so the broker rejects payloads being too large
-   persistent_client_expiration to allow cleaning stale clients

Monitoring

-   *log_dest*, preferrably /var/log/mosquitto.log, in conjunction with *log_type* and optionally *connection_messages*

### [][TLS (X509)]

This section illustrates basic steps:

1.  create a private key
2.  create a certificate signing request (CSR) for the private key
3.  signing the CSR as your own CA to yield a server certificate

For other options and how to let the system trust your own CA see [Certificates](https://wiki.gentoo.org/wiki/Certificates "Certificates") and [Certificates/Become your own CA](https://wiki.gentoo.org/wiki/Certificates/Become_your_own_CA "Certificates/Become your own CA").

First create a directory tls under Mosquitto\'s configuration and create a broker key. Shown here an elliptic curve key with non-NIST algorithm:

`root `[`#`]`cd /etc/mosquitto `

`root `[`#`]`mkdir tls `

`root `[`#`]`cd tls `

`root `[`#`]`openssl genpkey -algorithm ED25519 >broker.key `

`root `[`#`]`chown mosquitto:mosquitto broker.key`

Certificates have limited validity and need to be re-created. It is much easier to do this with a configuration file (no alternative names/ certificate for the MQTT broker only):

[FILE] **`/etc/mosquitto/tls/openssl-25519.conf`**

    [req]
    distinguished_name = yourserver_mosquitto
    req_extensions = v3_req
    prompt = no
    [yourserver_mosquitto]
    C = DE
    CN = mqtt.yourserver.net
    [v3_req]
    keyUsage = keyEncipherment, dataEncipherment
    extendedKeyUsage = serverAuth

Create the CSR:

`root `[`#`]`openssl req -new -out mosquitto_yourserver.csr -key broker.key -config openssl-25519.conf`

With your own root/ intermediate CA issue a certificate valid for 365 days:

`user `[`$`]`openssl x509 -req -in mosquitto_yourserver.csr -days 365 -out broker-yourserver.crt -CA root.cer -CAkey root.key -sha256 -CAcreateserial`

Finally store *broker-yourserver.crt* in */etc/mosquitto/tls* and configure *mosquitto.conf* accordingly:

[FILE] **`/etc/mosquitto/mosquitto.conf`**

    #A listener on default TLS port
    # Broker runs as this user
    user=mosquitto

    listener 8883

    certfile=/etc/mosquitto/tls/broker-yourserver.crt

    keyfile=/etc/mosquitto/tls/broker.key

Finally secure all files by revoking permissions/ limiting access to user mosquitto only:

`root `[`#`]`chown -R mosquitto:mosquitto /etc/mosquitto/tls `

`root `[`#`]`chmod 400 /etc/mosquitto/tls/*`

Improvements:

-   broker key with password, requires unlocking upon start/ restart
-   monitoring of certificate expiration, e.g. [Icinga2](https://wiki.gentoo.org/wiki/Icinga2 "Icinga2")
-   use key management, e.g. an external device or partition that is only available when starting the service

### [Service]

#### [OpenRC]

`root `[`#`]`/etc/init.d/mosquitto start`

#### [systemd]

`root `[`#`]`systemctl start mosquitto`

## [Usage]

The package provides the broker and tools to directly interact with it. The following command subscribes to a topic *announce/info* on a given host with port 8883 -- assuming the broker was configured with a TLS listener (process runs until stopped):

`user `[`$`]`mosquitto_sub -h mqtt.example.com -p 8883 -u mqtt-consumer-12 -P secret -t announce/info`

To publish the message *This broker is up and running* to the same topic on the same host with a different user:

`user `[`$`]`mosquitto_pub -h mqtt.example.com -p 8883 -u mqtt-publisher -P othersecret -t announce/info -m 'This broker is up and running'`

This message now shows up in the output of the first command.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-misc/mosquitto`