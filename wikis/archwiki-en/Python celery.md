# Python celery

Quoting authors of the project:
:Celery is "an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well. (...) Tasks can execute asynchronously (in the background) or synchronously (wait until ready)."

## Installation
Install the package . As with most python-based packages you get a package compatible with Python 3.x.

Quoting Celery documentation: "Celery requires a solution to send and receive messages" - one of the options is  which also can be installed from official repositories.

## Configuration
## Celery
For configuration files, the directory  needs to be created with a configuration file named  where app is the name of your application. An example configuration file is provided within Celery documentation.

Start/enable the .

To run celery in a virtualenv, make a copy of  in  so you can customize it, and change the paths of the celery binary to the copy in your virtualenv.

## RabbitMQ
RabbitMQ stores its configuration within

You probably want to replace  with , RabbitMQ does not support Unix sockets.

For simple configurations, you may also want to add . Read more about environmental variables within RabbitMQ docs

Start/enable .

Follow RabbitMQ documentation and add your user and virtual host:

 $ cd /var/lib/rabbitmq
 rabbitmqctl add_user myuser mypassword
 [rabbitmq$ rabbitmqctl add_vhost myvhost
 rabbitmqctl set_user_tags myuser mytag
 [rabbitmq$ rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

Read the RabbitMQ admin guide to understand the above.

If issuing  results in  visit this blog post for more information how to fix the problem.

## Security
You may want to read a security section from relevant Celery documentation

## Example task
## Celery application
Follow Celery documentation to create a python sample task:

 - Use the same credentials/vhost you have created when configuring RabbitMQ

 - this parameter is optional since RabbitMQ is the default broker utilised by celery.

## Test run
While in the same directory as your  you can run:
 $ celery -A task worker --loglevel=info

Then from another console (but within same directory) create:

Run it:

 $ python call.py

First, the console should log some information suggesting worker was called:

 Received task: task.addTask task.add[f4aff99a-7477-44db-9f6e-7e0f9342cd4e succeeded in 0.0007182330009527504s: 8

## Prepare module for Celery service
Procedure below is slightly different than what you will find within Celery documentation

To make the  module as root, create first the  directory, a blank  and the following files should be created inside of it:

At this point if you issue  in your console you should be able to issue following without any error:
 >>> from test_task import celery

In  replace:
 CELERY_APP="proj"
with the following line:
 CELERY_APP="test_task"

Restart the .

## Run tasks periodically
Tasks can be ran periodicaly through Celery Beat, basic setup is described within relevant Celery documentation pages. An example:

If you want to specify  within your , then you need to add the  prefix to make celery recognise your scheduled tasks. After that you need to add the  parameters when you start the celery daemon. Further, the  directory must exist within the celery-relevant environment and be owned by the user that runs celery.
