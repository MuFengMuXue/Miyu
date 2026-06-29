# Privoxy

Privoxy is a filtering proxy for the HTTP protocol, frequently used in combination with Tor. Privoxy is a web proxy with advanced filtering capabilities for protecting privacy, filtering web page content, managing cookies, controlling access, and removing ads, banners, pop-ups, etc. It supports both stand-alone systems and multi-user networks.

## Installation and setup
Install the  package.

When Privoxy is used in conjunction with Tor the two applications need to exchange information through a chain, which requires the specification of forwarding rules.

Finally, if you plan to make Privoxy available to other computers in your network, just add the following to :
 listen-address For example:
 listen-address 192.168.1.1:8118

## i2p
To forward .i2p sites through the I2P router, add the following to :
 forward .i2p localhost:4444

## Forwarding through tor
Edit your  file and add this line at the end (be sure to include the . at the end
 forward-socks5 / localhost:9050 .

This example uses the default port used by Tor. If you changed the port number modify the example accordingly. The same basic example is valid for other targets. If you plan on chaining to another proxy specify the method (here SOCKS5) and the port to suit your needs. Refer to section 5 of the manual inside  for a complete list of options and examples.

The above will forward all browser traffic through Tor. To only forward .onion sites through Tor, use this instead:
 forward-socks4a .onion localhost:9050 .

## Ad Blocking with Privoxy
Using an ad blocking extension in a web browser can increase page load time. Additionally, extensions like AdBlock Plus are not supported by all browsers. A useful alternative is to install system-wide ad blocking by setting a proxy address in your preferred browser.

You can use adblock plus filters. The [https://github.com/Andrwe/privoxy-blocklist privoxy blocklist script automatically downloads adblock plus filters, converts them to a privoxy friendly format, and edits privoxy's configuration file to include those filters:
# Run the script once to create
# Edit  to uncomment the line  and the two lines below it.
# Run the script again to download and install the blocklists.
# Restart privoxy.

To block tracking via embedded Facebook "Like" button, Twitter "follow", and Google Plus "+1", edit  and add these lines to the end:
 {+block-as-image{Facebook "like" and similar tracking URLs.}}
 www.facebook.com/(extern|plugins)/(login_status|like(box)?|activity|fan)\.php
 platform.twitter.com/widgets/follow_button?
 plusone.google.com

## Usage
Start and enable .

Configure your program to use Privoxy. The default address is:
 localhost:8118

For Firefox, go to:
 Preferences > General > Network Settings > Settings

For Chromium you can use:

 $ chromium --proxy-server="localhost:8118"

Alternatively you can set  environment variable, which is respected by Firefox, Chromium and other applications:
 http_proxy="http://localhost:8118"

Privoxy can be tested by accessing either http://config.privoxy.org or http://p.p.
