# HTTP tunneling

In networking, tunneling is using a protocol of higher level (in our case HTTP) to transport a lower level protocol (in our case TCP).

## Creating the tunnel
## Using corkscrew and HTTP CONNECT
To open the connection to the server running the SSH daemon, we will use the HTTP CONNECT method which allows a client to connect to a server through an HTTP proxy by sending an HTTP CONNECT request to this proxy.

For this, we will use corkscrew, a tool for tunneling SSH through HTTP proxies available as .

Opening an SSH connection is pretty simple:

 $ ssh user@server -o "ProxyCommand corkscrew proxy_ip_or_domain_name proxy_port destination_ip_or_domain_name destination_port"

but that just opens a shell. What we want is a SOCKS tunnel, so we do this:

 $ ssh -ND port user@server -o "ProxyCommand corkscrew proxy_ip_or_domain_name proxy_port destination_ip_or_domain_name destination_port"

which creates a SOCKS proxy on .

## Tunneling Git
Restrictive corporate firewalls typically block the port that git uses. However, git can be made to tunnel through HTTP proxies using utilities such as corkscrew. When git sees the environment variable  set, it will run the command in  and use the program's stdin and stdout, instead of a network socket.

Create a script:

Set

 export GIT_PROXY_COMMAND=/path/to/corkscrewtunnel.sh

Now, git should be able to tunnel successfully through the HTTP proxy.

## Using httptunnel
httptunnel, available as , creates a bidirectional virtual data connection tunneled in HTTP requests. The HTTP requests can be sent via an HTTP proxy if so desired. This can be useful for users behind restrictive firewalls. If WWW access is allowed through a HTTP proxy, it is possible to use httptunnel and, say, telnet or PPP to connect to a computer outside the firewall.

One limitation of httptunnel is it explicitly can not handle HTTPS.If you already have a web server listening on port 80, you are probably going to want to create a virtual host and tell your web server to proxy request to the hts server. This is not covered here.

If you do not have any web server listening on port 80, you can do:
*on the server:
 hts --forward-port localhost:22 80
*on the client:
 htc --forward-port 8888 example.net:80
 ssh -ND user@localhost -p 8888

You can now use  as a SOCKS proxy.

## Using proxytunnel
[https://proxytunnel.sourceforge.io/intro.php ProxyTunnel is:
: "a program that connects stdin and stdout to a server somewhere on the network, through a standard HTTP(S) proxy".

The proxy connection is used to tunnel another protocol, for example SSH through a HTTPS connection. It can be installed with the  package.

An example for using it with OpenSSH, to eventually connect to , is having the following content:

## Using openbsd-netcat
Install the  package.

To open a connection using the OpenBSD netcat version:

 $ ssh user@final_server -o "ProxyCommand=nc -X connect -x some_proxy:proxy_port %h %p"

The OpenBSD netcat also supports SOCKS tunneling. See  for more on the  option.

## Using the tunnel
See Proxy server#Using a SOCKS proxy.
