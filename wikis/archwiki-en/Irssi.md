# Irssi

Irssi is a modular, ncurses based IRC (Internet Relay Chat) client. It also supports SILC and ICB protocols via plugins.

## Installation
Install the  package.

Several scripts are available in the AUR under irssi-script, and in the Irssi script repository.

## Usage
For a detailed introduction see the official documentation.

A terminal multiplexer such as tmux or GNU Screen is recommended. It allows the user to easily disconnect and reconnect to a session, and scripts such as nicklist.pl depend on a secondary window. To start irssi, run:

 $ irssi

See also .

## Commands
Irssi commands start with a slash and are case-insensitive. Tab completion is supported. You can find out about them with the built-in  pages, which are also available online.

{| class="wikitable"
! Command
! Description
|-
| /help
| List all commands or describe a given command.
|-
| /network
| Manage your IRC networks.
|-
| /server
| Manage your IRC servers.
|-
| /connect
| Connect to a server or network.
|-
| /disconnect
| Closes the current connection to a server.
|-
|
| Changes the currently active window.  cycles to the next window,  to the previous window.
|-
| /window
| Manage your irssi windows.
|-
| /layout
| Save or delete your window configuration.
|-
| /statusbar
| Manage the statusbars.
|-
| /set
| View or change settings.
|-
| /alias
| Manage your aliases.
|}

## Configuration
Irssi installs its default configuration to , and copies it to  if not present. The default configuration contains several servers, chatnets, and channels. You can start irssi with an alternate configuration file using the  flag.

* You can use  to save your current configuration to the configuration file.
* You can save the location of your currently opened windows by entering

## Authenticating with SASL
Irssi supports the Simple Authentication and Security Layer (SASL).

You can add a network with SASL mechanism as follows:

 /SERVER ADD -auto -tls -tls_verify -network liberachat -port 6697 irc.libera.chat
 /NETWORK ADD -sasl_mechanism PLAIN -sasl_username username -sasl_password password liberachat

Restart Irssi, connect network and look for SASL authentication succeeded.

## Automatically connect to #archlinux on startup
Start Irssi and then type the following in it:

 /server add -auto -network liberachat irc.libera.chat

 can be substituted for any preferred word, such as the common abbreviation .

Ensure SASL is configured correctly. You may use NickServ manually with  instead of SASL, but this causes a race condition when automatically joining channels. If desired, authenticate using SSL certificates, instead of passwords with NickServ.

 /channel add -auto #archlinux liberachat
 /channel add -auto #archlinux-offtopic liberachat

## TLS Connection
## Client certificates
Libera Chat and OFTC support authentication using TLS certificates, providing an alternative to passwords. Follow their own guides on using CertFP: Libera.chat, OFTC. The instructions below are for a more general case and may not reflect practices suggested by these IRC networks.

## General instructions
To create a password-less certificate that is valid for 730 days (when requested to enter details like state or even Common Name (CN), you can fill anything you want):

 $ openssl req -newkey rsa:4096 -days 730 -x509 -keyout irssi.key -out irssi.crt -nodes
 $ cat irssi.crt irssi.key > ~/.irssi/irssi.pem
 $ chmod 600 ~/.irssi/irssi.pem
 $ rm irssi.crt irssi.key

Next, find out the corresponding fingerprint:

 $ openssl x509 -sha512 -fingerprint -noout -in ~/.irssi/irssi.pem | sed -e 's/^.*=//;s/://g;y/ABCDEF/abcdef/'

This will write the SHA512 fingerprint to stdout. If you need the SHA1 fingerprint, replace  with . The sed command is there to format the fingerprint correctly by removing unwanted text and characters.

Copy the fingerprint string as you will register it in Irssi shortly.

In irssi, disconnect from the network and add the client certificate and keys. Omit the  option if your certificate was built without a password:

 /disconnect liberachat
 /server add -ssl_cert ~/.irssi/irssi.pem  -ssl_pass irssi.pem_password -network liberachat irc.libera.chat 6697

Now connect (not ) and register your fingerprint

 /connect liberachat
 /msg NickServ identify YOUR_PASSWORD
 /msg NickServ cert add YOUR_FINGERPRINT

At this point, you can remove your password from the configuration file (if you saved it in there) and save your configuration with:

 /save

## Automatic logging
 /SET autolog ON
 /save

## Hide joins, parts, and quits
In order to ignore showing of joining, leaving and quiting of users for all channels type the following in irssi:

 /ignore * joins parts quits

See smartfilter to restrict join messages to active users.

## Mouse scrolling
To enable the mouse, type the following in irssi:

 /run scriptassist
 /script install mouse.pl

You may need to install  for the above to work.

To permanently enable it at startup:

 /script autorun mouse.pl

If the above does not work, you can manually load scripts from  or  with the following:

 /script load mouse.pl

## Tips and tricks
## HTTP Proxy
To use irssi behind a HTTP proxy, the following commands are required:

 /SET use_proxy ON
 /SET proxy_address
 /SET proxy_port
 /SET -clear proxy_string
 /SET proxy_string_after conn %s %d
 /EVAL SET proxy_string CONNECT %s:%d HTTP/1.0\n\n

irssi should then alter its configuration file correspondingly; if the proxy is not required, just set use_proxy to OFF.

Should the proxy require a password, try:

 /SET proxy_password your_pass

Otherwise:

 /SET -clear proxy_password

## Irssi with nicklist in tmux
The irssi plugin 'nicklist' offers to add a pane listing the users on the channel currently viewed. It has two methods to do this:

* screen, which simply adds the list to the right of irssi, but brings the disadvantage that the entire window gets redrawn every time irssi prints a line.

* fifo, which like the name suggests writes the list into a fifo that can then be continuously read with e. g. .

nicklist will use the more efficient fifo with:

 /NICKLIST FIFO

This fifo can be used in a tmux window split vertically with irssi in its left pane and the cat from above in a small one in its right. Since the pane is dependent on its creating tmux session's geometry, a subsequent session with a different one needs to recreate it (which also implies a switch in irssi windows to refill the fifo).

E.g., the following script first checks for a running irssi, presumed to have been run by a previous execution of itself. Unless found it creates a new tmux session, a window named after and running irssi and then the pane with cat. If however irssi was found it merely attaches to the session and recreates the cat pane.

{{bc|1=
#!/bin/sh

T3=$(pgrep -u "$USER" -x irssi)

irssi_nickpane() {
    tmux setw main-pane-width $(( $(tput cols) - 21));
    tmux splitw -v "cat ~/.irssi/nicklistfifo";
    tmux selectl main-vertical;
    tmux selectw -t irssi;
    tmux selectp -t 0;
}

irssi_repair() {
    tmux selectw -t irssi
    [ "$(tmux lsp  wc -l)" -gt 1 ] && tmux killp -a -t 0
    irssi_nickpane
}

if [ -z "$T3" ]; then
    tmux new-session -d -s main;
    tmux new-window -t main -n irssi irssi;
    irssi_nickpane ;
fi
    tmux attach-session -d -t main;
    irssi_repair ;
exit 0
}}

## Virtual hostname (vhost)
A vhost can be used to change your hostname when connected to an IRC-server, commonly viewed when joining/parting or doing a whois. This is most commonly done on a server that has a static IP address. Without a vhost it would commonly look like so when doing a 'whois':

 nick@123.456.78.90.isp.com

The result of a successful vhost could be like so if you have the domain example.com available:

 nick@example.com

Keep in mind that not every IRC-server supports the use of vhost. This might be individually set between the servers and not the network, so if you are experiencing issues with one server try another on the same network.

## Required preconfigurations
Irssi supports using a vhost as long as the required configurations has been set. This includes especially that your host supports reverse DNS lookup (rDNS) using pointer record (PTR). Additionally you should add an appropriate line to your  file.

To see if this is working, test with the  DNS lookup utility included in  like so (where ip is a normal IPv4 address):

 $ host ip

If this returns something in the lines of this then you know that your rDNS is working.

 ip.in-addr.arpa domain name pointer example.com

## Enabling the vhost
There are a couple of ways to connect to a server with a given hostname. One is using the 'server' command with a -host argument like so:

 /server -host example.com irc.libera.chat

Another way would be to set your hostname (vhost) with the 'set' command which will save your hostname to :

 /set hostname example.com
 /save
 /server irc.libera.chat
