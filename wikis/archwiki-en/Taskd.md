# Taskd

taskd is a lightweight, secure server for Taskwarrior (). It allows users to intelligently synchronize their tasks between multiple clients, including between desktop and mobile ones.

## Server
## Installation
Install .

## Configuration
Once taskd is installed, you need to set it up. The first step is to

 $ export TASKDDATA/var/lib/taskd

otherwise you need to append  to every taskd command.

Next, edit the  file. The  line must either match the server's hostname or IP address, depending on how you connect.

Once the file is edited to your heart's content, change to the directory  and run . This will create self-signed certificates for your server.

Copy all generated  to . Note that at least the  and  must remain in the  folder for the user-certificate generation later on.

Then make sure only taskd can read the certificates and keys in :

Now you need to configure taskd. Use  or add the following to  directly:

Additionally you should change where taskd logs to, since the default is . This can be done by running

The last step is to set taskd's server name, which must be the same as the one used in the certificates:

 # taskd config --force server servername:port

Note that taskd has no default port and it must be set manually.

## Running
Start/enable .

## Adding a user in taskd
taskd organizes data into organizations and users, with each user being in an organization.

To add a user, run the following commands, substituting  and  as you wish.

Note the key the last command returns, the user will need it to synchronize.

Make sure new organization and user are readable by user .

 # chown -R taskd:taskd /var/lib/taskd/orgs

Return to  and run

 # ./generate.client username

This will return  and .

The ,  and  must be copied into to the user's Taskwarrior user data directory (default ).

## Client
## User configuration
Once the  files have been copied to a user's Taskwarrior data directory, their configuration file (default ) must be updated to point to the files and server:

Paths are relative to the directory in which  is executed, so paths should be relative to  or absolute.

The key in  is name of the created directory in  on the server which contains a config file with the chosen username:

Perform the initial synchronization and consent to sending your Taskwarrior data to the server:

 $ task sync init

Send local changes to the server:

 $ task sync

## Using the Android Taskwarrior app
Before you even download the android app, you need to create a folder. On your external storage (or if you only have an internal one, then there) create the folder  where "key" is the same as the key given when creating the user with . Then add the ,  and  files to that folder.

Create a new file in that folder called . It should look like this:

Now download the app and start it. When prompted to add a profile, choose the data folder that you just created. Taskwarrior should now sync and work as expected.

## Troubleshooting
## Unreachable Server
Should the server be unreachable but running, it bound itself to an IPv6 address. You can force IPv4 by adding  to .

If the server stalls on "Server starting", it may be failing to resolve the address you have specified in the  option. After a while the server will time out with "Name or service not known". In that case, try adding an external  entry aliasing that address to your external IP address (see Domain name resolution),

Restart taskd after attempting these, then check if your issue is fixed.

## "Bad Key"
If the server responds with a "Bad Key" error even though you just generated them, check the permissions of the created folders (everything in  and subfolders). taskd does not set its own uid / gid, so those folders must be manually chowned to taskd.

## taskd.service fails on boot
Taskd 1.1's systemd unit does not have the correct network target dependency so might fail at times on boot. The snippet below adds the correct dependencies, this was already fixed upstream.

## systemd hardening
Taskd is not sandboxed by default, the overrides below disallow taskd from writing in anything except  and .
