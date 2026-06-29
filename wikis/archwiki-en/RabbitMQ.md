# RabbitMQ

RabbitMQ is a messaging broker, an intermediary for messaging. It gives your applications a common platform to send and receive messages, and your messages a safe place to live until received.

## Installation
Install the  package.

## Configuration
No configuration should be needed. Simply start and/or enable .

Default configuration file location . See more about configuration on the official docs

## Enabling MQTT
RabbitMQ can act as MQTT server. For this functionality to work following plugin needs to be enabled:

 # rabbitmq-plugins enable rabbitmq_mqtt

RabbitMQ service needs to be restarted for this change to take effect.

Clients need to authenticate before they can post to topics. RabbitMQ segregates traffic via virtual hosts, you need to issue `configured_vhost_name:your_user_name` as user name in order to authenticate.

## Enabling HTTP admin
To enable the HTTP admin page:

 # rabbitmq-plugins enable rabbitmq_management

Then navigate to . Default credentials are

## Troubleshooting
## Service stop hangs for a minutes
Rabbitmq package install epmd (Erlang Port Mapping Daemons) as dependency. If you run rabbitmq server via systemd, it will start detached epmd process, that will not be stopped with . You can avoid this, if add  in  section. Do not forget to reload daemons.

## Changed hostname
If you have changed your hostname after you installed rabbitmq, it will no longer be able to start.
This is due to the  specified in .
Update it to reflect your new hostname, for example:

## Upgraded RabbitMQ to latest version and cannot start
This might cause your  to get the wrong .
For example, it might cause it to add another  part. In any case, this can be fixed by following #Changed hostname.

In case the service does not start with error:

 BOOT FAILED
 ===========
 [error  Error during startup:  {error,failed_to_initialize_feature_flags_registry}

It looks like this error is related to an incompatibility in the plugins folder after upgrade. One solution is to completely remove all trace of rabbitmq and reinstall:

 # pacman -Rn rabbitmq
 # rm -r /etc/rabbitmq
 # rm -r /var/lib/rabbitmq be unnecessary
 # pacman -S rabbitmq
 # systemctl start rabbitmq.service

After restart with latest version (4.0.5-3) they may still be issue because of missing variables. In this case add:

## Issues with rabbitmqctl and other command line tools
With latest version (4.0.5-3) it looks like  is not in , also see #Erlang cookie error.

## Erlang cookie error
Failure to authenticate might be caused by a wrong rabbitmq HOME setting:
 Authentication failed (rejected by the remote node), please check the Erlang cookie
 ...
 home dir: /root

Home can be set in the configuration file:

## can't establish TCP connection
If you see this error then make sure first entry with your host name within  contains the same IP address as specified within  (this error is common if you configure rabbitmq to bind to specific interface).

## Can't connect with pika Python client through localhost
Trying to connect through localhost with pika Python client, raises an exception:

 ...
 pika.exceptions.ProbableAccessDeniedError: (541, "INTERNAL_ERROR - access to vhost '/' refused for user 'guest': vhost '/' is down")

Default configuration file  of the package is:

Removing the username part of , and leaving the hostname of the machine (which should match the one shown in ), fixes the issue:
