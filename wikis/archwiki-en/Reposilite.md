# Reposilite

From the project repository, reposilite is a:

:Lightweight and easy-to-use repository manager for Maven based artifacts in JVM ecosystem. This is simple, extensible and scalable self-hosted solution to replace managers like Nexus, Archiva or Artifactory, with reduced resources consumption.

## Installation
Install the  package. It can also be downloaded through Github Releases.

## Package contents
## Configuration
Configuration files are located in  :

*  : configuration variables used to run reposilite (allocated memory, user, working directory, configuration location)
*  : main reposilite configuration file

## Data directory
Reposilite data is stored in . This include default shared configuration database as well as repositories contents.

## Service files
The package contains the  systemd unit. It is not enabled by default.

## Usage
Reposilite does the majority of its configuration through the web interface. When you first install reposilite you will not have any user to login as (reposilite designates users as "tokens"). Before creating the first token, ensure that  is stopped.

Run the reposilite binary as root:

 # /usr/bin/reposilite

This will start the server and a CLI interface in the terminal; the next set of commands will be run from the CLI (we will use  to indicate that these command are run in the reposilite CLI):

 ! token-generate username m

Remember to replace username with the desired username, it is best to let reposilite generate you a secure token, but if you wish to use your own token, you can use the following command:

 ! token-generate --secret="your password" username m

Now that you have generated the username (if you let reposilite generate your token, make sure to copy this down securely, a password manager is recommended), you can stop the reposilite server using the following command:

 ! stop

Reposilite will then gracefully shutdown and detach from your terminal.

You can now start/enable  and you will be able to access the reposilite web interface over .
