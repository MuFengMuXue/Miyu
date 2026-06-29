** Warning**\
The methods described here rely on technologies that are susceptible to a variety of attacks (DNS poisoning, DHCP injection, MITM). Please read up on security concerns related to this method before implementing this. [Wikipedia](https://secure.wikimedia.org/wikipedia/en/wiki/Wpad#Security) lists some of them.

## Contents

-   [[1] [How it works]](#How_it_works)
    -   [[1.1] [The Proxy Auto Configuration (PAC) file]](#The_Proxy_Auto_Configuration_.28PAC.29_file)
    -   [[1.2] [Getting the PAC file to the client]](#Getting_the_PAC_file_to_the_client)
        -   [[1.2.1] [Web Proxy Auto-Discovery (WPAD)]](#Web_Proxy_Auto-Discovery_.28WPAD.29)
-   [[2] [Creating the PAC file]](#Creating_the_PAC_file)
-   [[3] [DHCP server configuration]](#DHCP_server_configuration)
-   [[4] [DNS server configuration]](#DNS_server_configuration)
-   [[5] [Serving the WPAD file]](#Serving_the_WPAD_file)
    -   [[5.1] [Apache setup]](#Apache_setup)
-   [[6] [Configuring clients]](#Configuring_clients)
-   [[7] [Next steps]](#Next_steps)

## [How it works]

Many web clients have the possibility to detect proxy settings for their current network automatically. This can be done via

-   DHCP
-   WPAD
-   manual URL configuration

Once the proxy autoconfiguration file is obtained, clients evaluate it to see how to connect to a proxy server.

### [][The Proxy Auto Configuration (PAC) file]

A PAC file is a simple javascript file clients can evaluate to get their configuration. For each request, the client executes the javascript, passing along the URL and host name it would like to make the request to. The script will return a proxy name to use for this server/URL, or DIRECT if there is no proxy for this host or protocol.

### [Getting the PAC file to the client]

In order to get to the PAC file, a client can use several options:

local file

remote file

DHCP

WPAD

The last two options are explained in this article, because once a client is set up it can work the same way regardless which network it is in.

#### [][Web Proxy Auto-Discovery (WPAD)]

WPAD works like this:

A client tries to figure out is domain name by stripping its own host name from the FQDN it got from DHCP (or wherever). It will then try to contact a HTTP server by the name of wpad.\<domain\>. If it can\'t find one, and the domain name has one ore more subdomains, it will strip the first subdomain and try again to find a server named wpad.\<domain\> up until the top-level domain is reached.

From those HTTP servers it will request a file called /wpad.dat which should be a PAC file like the one created above.

For example:

  ---------------------- ----------------------------------------------------------------------------------------------------------------------------------------
  Client Name:           laptop.office.corporate.example.org
  First Server tried:    [http://wpad.office.corporate.example.org/wpad.dat](http://wpad.office.corporate.example.org/wpad.dat)
  Second Server tried:   [http://wpad.corporate.example.org/wpad.dat](http://wpad.corporate.example.org/wpad.dat)
  Last Server tried      [http://wpad.example.org/wpad.dat](http://wpad.example.org/wpad.dat)
  ---------------------- ----------------------------------------------------------------------------------------------------------------------------------------

## [Creating the PAC file]

For details on which commands are supported in this file, see:

-   [http://www.proxypacfiles.com/proxypac/](http://www.proxypacfiles.com/proxypac/)
-   [http://findproxyforurl.com/](http://findproxyforurl.com/)

A simple PAC file looks like this:

[FILE] **`proxy.pac`**

    function FindProxyForURL(url, host)

** Important**\
Depending on the capabilities of the proxy used one might want to expand the section matching other protocols. Many only do HTTP.

The [pacparser](https://github.com/manugarg/pacparser) tool can be used to test that the PAC file is functioning correctly.

Example:

    /usr/bin/pactester -p proxy.pac -u http://www.gentoo.org -h gentoo.org
    PROXY proxy.example.org:8118; DIRECT

    /usr/bin/pactester -p proxy.pac -u rsync://rsync.gentoo.org -h gentoo.org
    DIRECT

If the return value of the script is DIRECT, the client won\'t use a proxy. The line \"PROXY proxy.example.org:8080; DIRECT\" will tell clients to first try to use the host proxy.example.org at port 8080 as a proxy, and if that fails, go direct. Multiple PROXY strings can be provided for redundancy or load balancing.

** Note**\
Clients will try to use the servers in order so for load balancing the javascript will have to shuffle the servers.

## [DHCP server configuration]

** Note**\
To only use WPAD this step is not strictly necessary but it might help with clients which are not capable to the WPAD method f.e. some mobile devices.

Some operating systems can use information provided via DHCP to obtain the proxy autoconfiguration file. Here is how to make the ISC dhcpd server ([[[net-misc/dhcp]](https://packages.gentoo.org/packages/net-misc/dhcp)[]]) serve this information:

In dhcpd.conf in the general section define a new option with code 252 and in the section for the network provide the value of the config server valid for that network.

[FILE] **`/etc/dhcp/dhcpd.conf`**

    # do windows-style proxy autoconfig:
    option local-proxy-config code 252 = text;
    ...
    subnet 192.168.0.0 netmask 255.255.255.0

** Note**\
The option can be called anything you want, but you have to give it code 252 and type text

## [DNS server configuration]

The responsible DNS Server must have records for the wpad.\<domain\> servers. How to set up an or configure a DNS server is out of scope here, but a simple modification to the records of ISC bind would look like this:

[FILE] **`/etc/bind/pri/example.org.zone`**

    server1    IN A     192.168.0.1
    server2    IN A     192.168.0.2
    www        IN CNAME server1.example.org.
    proxy      IN CNAME server2.example.org.
    ; proxy autoconfig server:
    wpad       IN CNAME server1.example.org.

** Note**\
Might also want to add an alias for the proxy server itself if there isn\'t one yet.

## [Serving the WPAD file]

Now that there is a PAC file and DNS points to the correct server, all that is left is actually serving the file to clients.

### [Apache setup]

To use [[[www-servers/apache]](https://packages.gentoo.org/packages/www-servers/apache)[]], configure a (virtual) host which will respond to the wpad server name, and serve out the PAC file.

[FILE] **`/etc/apache2/vhosts.d/00_server1.example.org.conf`**

    NameVirtualHost 192.168.0.1:80
    Listen 192.168.0.1:80
    NameVirtualHost 192.168.0.1:80

    <VirtualHost 192.168.0.1:80>
            ServerName server1.example.org
            ServerAlias wpad.example.org

            DocumentRoot "/var/www/example.org/htdocs"
            <Directory "/var/www/example.org/htdocs">
                    AllowOverride All
                    Options MultiViews FollowSymlinks SymLinksIfOwnerMatch IncludesNoExec
                    Options -Indexes
                    Order allow,deny
                    Allow from all
            </Directory>

            # serve proxy autoconfig correctly:
            <Files "wpad.dat)">
                    AddType application/x-ns-proxy-autoconfig dat
            </Files>
            <Files "proxy.pac">
                    AddType application/x-ns-proxy-autoconfig pac
            </Files>
    </VirtualHost>

Now all that is left is to copy our PAC file to [/var/www/example.org/htdocs/]. The author likes to call the file \'proxy.pac\' because that name is used in lots of documentation. Add a symbolic link called wpad.dat to satisfy the WPAD naming convention.

`root `[`#`]`ln -s proxy.pac wpad.dat`

** Important**\
The file MUST be accessible under the URL [http://wpad.example.org/wpad.dat](http://wpad.example.org/wpad.dat). Naming it it anything else or placing it deeper in the web server hierarchy is not allowed. There probably also shouldn\'t be fancy stuff like redirects or HTTPS.

## [Configuring clients]

+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Application               | Steps                                                                                                                                              | Screenshot                                                                                                                                                                                                                                                                                                                                                                                   | Documentation                                                                                                                                                                                    |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Firefox                   | In the Preferences Window, chose Advanced, go to the Network Tab, click the Settings\... button.                                                   | ::::::                                                                                                                                                                                                                                                                                                                                                                        | [Firefox Documentation](http://support.mozilla.org/en-US/kb/settings-network-updates-and-encryption?s=proxy&r=4&e=es&as=s#w_network-tab)                         |
|                           |                                                                                                                                                    | :::::                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | [![FFProxyAutoConfig.png](/images/thumb/8/8a/FFProxyAutoConfig.png/240px-FFProxyAutoConfig.png)](https://wiki.gentoo.org/wiki/File:FFProxyAutoConfig.png)         |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | :::: thumbcaption                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | ::: magnify                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | [](https://wiki.gentoo.org/wiki/File:FFProxyAutoConfig.png "Enlarge")                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | :::                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | ::::                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | :::::                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | ::::::                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                  |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Opera                     | Press Alt+P to bring up the Preferences, go to the Advanced Tab, chose Networking and click the Proxy Servers\... button.                          | ::::::                                                                                                                                                                                                                                                                                                                                                                        | [Opera Documentation](http://www.opera.com/support/kb/view/332/)                                                                                                 |
|                           |                                                                                                                                                    | :::::                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | [![OpProxyAutoConfig.png](/images/thumb/b/b9/OpProxyAutoConfig.png/240px-OpProxyAutoConfig.png)](https://wiki.gentoo.org/wiki/File:OpProxyAutoConfig.png)         |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | :::: thumbcaption                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | ::: magnify                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | [](https://wiki.gentoo.org/wiki/File:OpProxyAutoConfig.png "Enlarge")                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | :::                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | ::::                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | :::::                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | ::::::                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                  |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| KDE                       | In System Settings, search for proxy, the first section is the proxy settings.                                                                     | ::::::                                                                                                                                                                                                                                                                                                                                                                        | [KDE Documentation](http://docs.kde.org/cgi-bin/desktopdig/search.cgi?show=stable/en/kde-runtime/kcontrol/proxy/index.html&collection=en&include=stable&q=proxy) |
|                           |                                                                                                                                                    | :::::                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                  |
|                           | :::                                                                     | [![KDEProxyAutoConfig.png](/images/thumb/0/0a/KDEProxyAutoConfig.png/240px-KDEProxyAutoConfig.png)](https://wiki.gentoo.org/wiki/File:KDEProxyAutoConfig.png) |                                                                                                                                                                                                  |
|                           | ** Note**\                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                  |
|                           | This setup will be used for all KDE applications including those using protocols other than http:// so make sure you handle those in the PAC file. | :::: thumbcaption                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                  |
|                           | :::                                                                                                                                                | ::: magnify                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | [](https://wiki.gentoo.org/wiki/File:KDEProxyAutoConfig.png "Enlarge")                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | :::                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | ::::                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | :::::                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                  |
|                           |                                                                                                                                                    | ::::::                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                  |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GNOME                     | see link                                                                                                                                           | \-- no pic \--                                                                                                                                                                                                                                                                                                                                                                               | [GNOME Documentation](http://library.gnome.org/users/gnome-help/stable/net-proxy.html.en)                                                                        |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Windows/Internet Explorer | If you use the DHCP method Windows probably does the right thing automatically. Otherwise follow the link on the right                             | too much of a clickfest to provide a single screenshot.                                                                                                                                                                                                                                                                                                                                      | [Microsoft Documentation](http://support.microsoft.com/kb/135982)                                                                                                |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## [Next steps]

To finish the setup a proxy server would be needed. Some popular proxy servers are:

-   [[[net-proxy/squid]](https://packages.gentoo.org/packages/net-proxy/squid)[]]
-   [[[net-proxy/polipo]](https://packages.gentoo.org/packages/net-proxy/polipo)[]]
-   [[[net-proxy/privoxy]](https://packages.gentoo.org/packages/net-proxy/privoxy)[]]
-   [[[net-misc/tor]](https://packages.gentoo.org/packages/net-misc/tor)[]]