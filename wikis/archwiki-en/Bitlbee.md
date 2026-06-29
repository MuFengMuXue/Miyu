# Bitlbee

Bitlbee is a "console-based IRC to IM chatting gateway". It allows the user to interact with popular chat networks such as XMPP/Jabber, Yahoo! Messenger, the Twitter microblogging network (plus all other Twitter API compatible services like identi.ca and status.net), and social networking chat networks like Facebook and StudiVZ within their IRC client.

The users' buddies appear as normal IRC users in a channel and conversations use the private message facility of IRC.

## Installation
Install the  package.

## Configuration
Various settings can be set using the  configuration file. The default configuration file is well commented and each setting has relevant explanations.

## Daemon
It is recommended to run the Bitlbee daemon without root permission. Uncomment the following line so Bitlbee can run as the "bitlbee" user, which was created when the package was installed.

 User = bitlbee

For daemon mode uncomment the following lines.

 DaemonInterface = 0.0.0.0
 DaemonPort = 6667

To only allow connections from localhost set the listen interface () to loopback.

 DaemonInterface = 127.0.0.1

Ensure that the configuration directory is writeable with the user you configured:

 # chown -R bitlbee:bitlbee /var/lib/bitlbee

By default the bitlbee service doesn't kill child processes when stopping/restarting, to avoid disconnecting clients. This is desirable for public servers but less desirable in private installations where the client is left running on an old version after a upgrade.

To properly terminate bitlbee processes, edit the unit:

Then enable/start the  unit.

Note that just starting the server does not log you into any of your chat accounts.

## Usage
Once Bitlbee is running connect to  using an IRC client. The control channel, , should already show you some basic information (if not, join it now). You can always type  to get help.

While in the control channel, enter:

 help quickstart

and follow the instructions.

Your friend might be requesting authorization to add you back, so just reply according to the control channel prompts.

To initiate a chat, simply open a new IRC private window:

 /msg friend hello!

## OTR
For OTR support you must have  installed. Upon account registration, bitlbee will generate your OTR keys, and it will use them transparently whenever you are negotiating with an OTR-capable contact.

## External services
## Telegram
To make Telegram work with bitlbee, you need a version compiled with  support –  for example, although there are patched or development versions also available.

Next, install  and restart .

In the control channel, , type the following commands:

 11:45:03  account add telegram
 11:45:03  Account successfully added
 11:45:06  account telegram on

After connecting a separate chat window will open, asking for the SMS code – enter it and Telegram will work with your setup.

## Twitter
In the control channel, , type the following commands:

 11:45:03  account add twitter
 11:45:03  Account successfully added
 11:45:06  account on
 11:45:06  Trying to get all accounts connected...
 11:45:06  twitter - Logging in: Requesting OAuth request token

In a private channel, , you will receive:

 11:45:07  To finish OAuth authentication, please visit http://api.twitter.com/oauth/authorize?oauth_token=xxxxxxxxx and respond with the resulting PIN code.

Click the link and authorize the BitlBee app on Twitter. You should now see:

 11:59:54  twitter - Logging in: Connecting to Twitter
 11:59:55  twitter - Logging in: Logged in

## Discord
Install the package .

In the control channel, , type the following commands:

  account add discord
  Account successfully added with tag discord
  account discord on
  discord - Logging in: Logged in
