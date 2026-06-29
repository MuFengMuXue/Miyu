# Trac

From the project web page:
:Trac is an enhanced wiki and issue tracking system for software development projects. Trac uses a minimalistic approach to web-based software project management. Our mission is to help developers write great software while staying out of the way. Trac should impose as little as possible on a team's established development process and policies.

## Installation
Install the  package. Configuration is done on a per-environment basis. See below on how to create an environment. Detailed instructions can be found at https://trac.edgewall.org/wiki/TracGuide.

## Configuration
## Create and initialize an environment
Initialize an environment

 # cd /srv/
 # mkdir tracenv
 # trac-admin /srv/tracenv initenv

The environment configuration can be found at .

## Configure the systemd unit
Edit  using a drop-in file  point to your new environment. The  entry should look something like this:

 ExecStart=/usr/bin/tracd -b localhost -p 8080 /srv/tracenv

## Webinterface
Start/enable the service and you can view the web interface at  using a web browser.

## Trac user
It is a good idea to create a dedicated user for the trac service. Once that user is created, you can create the environment using that user:

 # cd /srv/
 # mkdir tracenv
 # chown trac:trac tracenv
 trac-admin /srv/tracenv initenv

Extend the unit file to make sure it is started as the  user:

 [Service
 User=trac
 Group=trac

## Users and permissions within trac
(This section refers to creating users within the trac environment rather than GNU/Linux users.)

Next, you will want to add users and give permissions to those users. To add users, see https://trac.edgewall.org/wiki/TracStandalone#UsingAuthentication (you will have to change your  file to refer to the authentication mechanism you choose). To grant permissions to users, run the following on the trac server:

 # trac-admin /srv/tracenv permission add  TRAC_ADMIN
