# TeamTalk

From Wikipedia:TeamTalk:

:TeamTalk is a conferencing system which people use to communicate on the Internet using VoIP and video streaming.

## Installation
## Client
Install the  package.  It is the same package for the server.  But the client files will be under the pkgsrc/srcdir/client directory.  The client can be invoked by running ./run.sh.

## Server
Install the  package.

## Server configuration and startup
## Configuration
* Teamtalk comes with a configuration script in the server binary, .

Just execute  and follow the steps.  This makes the file in  initially.  Minor edits can be made to this file later.  The usernames/passwords and other configuration options are stored in plaintext, so you may want to  the configuration file with .  Also the connection by default is not SSL/TLS enabled.

Teamtalk also has a facebook capability, which allows the user to enter  into the username box on the client.  To configure this feature on the server, an option will show up to create a generic  user to authenticate using facebook's network creating a profile for each facebook user on teamtalk directly from facebook.  It will be created like a normal user and ACLs.  An internet connection with DNS is required (if only using a local lan server) to use facebook's auth challenge which will alleviate having to administrate users.  However, a username can be used over and over again with multiple connections to the server, but this can also be restricted per user.

To enable file sharing, it can be given a storage directory in the wizard.  It needs to be a directory that the  user has access to.  A quota seems to be enforced by the wizard, making disabling a quota more difficult.  This might actually be a benefit to keep down spamming and only using the server for temporary storage until everyone has received the file.  The file uploader can delete the file share when finished.

IPv6 support is available and needs to be a specified listening address, but if IPv6 is not being used can be simply ignored.

The IP port for teamtalk is , but is flexible to other port numbers/assignments and can also be changed through the wizard or manually edited configuration file.

## First startup
You will need to configure at least one user through the server wizard to be able to use the client.  Facebook functionality is enabled by creating a special facebook user through the wizard.  Then you can
* Start the  service.

* To find the privilege key:
There is not a privilege key like there is with TeamSpeak or Mumble.  You create users with the server wizard directly without using the client program.  An admin user can use the client program like in Mumble to assign ACLs.  By default, most users will be able to do most things that a common user will need to be able to do in a conference including creating temporary rooms, sharing video, files or desktops.  Desktop sharing does not appear to be working on Linux.

## Regular startup
* Simply enable the  service.

## Changing configuration options manually
* Most likely remember to restart the  service.  Using the client admin function is usually more preferable for user administration, but other options are configured through manual edits or the server wizard. Using the facebook login function may save administrative maintainence, but may not be desirable.  Reusing users may not be desirable either.
