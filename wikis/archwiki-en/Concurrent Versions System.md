# Concurrent Versions System

From https://www.nongnu.org/cvs/:
:Concurrent Versions System is a version control system, an important component of Source Configuration Management (SCM). Using it, you can record the history of sources files, and documents. It fills a similar role to the free software RCS, PRCS, and Aegis packages.

More recent alternatives are listed in Version control system.

## Client
If you want to connect to a cvs server, install  and follow instructions from the owners of that server. For example https://www.openbsd.org/anoncvs.html.

## Graphical front-ends
*

## Server
This is a quick guide on how to set up the latest CVS server.

## Installation
Install  and .

Create the cvs user group - members of this group will have write access to the repository:

 # groupadd cvs

Create the cvs user in the cvs group ( makes the home directory):

 # useradd -md /home/cvsroot -g cvs -p Insecure0 cvs

## Initialization
Initialize your CVS repository (as cvs):
 cvs% cvs -d /home/cvsroot init

The permissions on the directory (not the files inside, however) should be 2775 (drwxrwxr-x), but if not, run (as cvs):
 cvs% chmod 2775 /home/cvsroot

Add any users that you want to have local access to the repository to the group cvs by using the following two steps.
You can add pre-existing users to the cvs group with the command:
 # gpasswd -a username cvs

Make a xinetd configuration file:

{{hc|/etc/xinetd.d/cvspserver|service cvspserver
{
        port            = 2401
        socket_type     = stream
        protocol        = tcp
        wait            = no
        user            = root
        passenv         = /home/cvsroot
        server          = /usr/bin/cvs
        server_args     = -f --allow-root=/home/cvsroot pserver
}}}

Ensure you have the following line in  (add it if not):
 cvspserver 2401/tcp

Unset the  variable
 # unset HOME

And restart .

## Configuration
As the cvs user, create a  file in . To add entries in the file you can use htpasswd commands (present in the  package) as follows:

 htpasswd -b filename username password

then edit the file and add the group, for example:

 # Format is username:password:group

 anonymous::
 archie:HopefullySecure0:cvs
 other:Insecure0:cvs

Now create a  file in , which grants write privileges to the users you created in :

 archie
 other

Now create a  file in , which grants read privileges to the users you created in :

 anonymous

## Usage
You can test out the server using the following commands:
