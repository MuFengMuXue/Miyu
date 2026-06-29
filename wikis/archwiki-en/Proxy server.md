# Proxy server

According to Wikipedia:
:In computer networks, a proxy server is a server (a computer system or an application) that acts as an intermediary for requests from clients seeking resources from other servers.

Proxying can be applied in common Internet protocols such as HTTP or SOCKS.

## Environment variables
Some programs, such as wget and (used by pacman) CURL, use environment variables of the form  to determine the proxy for a given protocol (e.g. HTTP, FTP, ...).

Below is an example on how to set these variables in a shell:

Some programs look for the all caps version of the environment variables.

If the proxy environment variables are to be made available to all users and all applications, the above mentioned export commands may be added to a script, say  inside . The script has to be then made executable. This method is helpful while using a desktop environment like Xfce which does not provide an option for proxy configuration. For example, Chromium browser will make use of the variables set using this method while running XFCE.

Alternatively, there is a tool named  which claims to configure system-wide proxy settings easily. It also handles proxy configurations of other software like git, npm, Dropbox, etc.

Alternatively you can automate the toggling of the variables by adding a function to your :

{{bc|
function proxy_on() {
    export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"

    if (( $# > 0 )); then
        valid=$(echo $@ | sed -n 's/\(if  $valid != $@ ; then
            >&2 echo "Invalid address"
            return 1
        fi
        local proxy=$1
        export http_proxy="$proxy" \
               https_proxy=$proxy \
               ftp_proxy=$proxy \
               rsync_proxy=$proxy
        echo "Proxy environment variable set."
        return 0
    fi

    echo -n "username: "; read username
    if  $username != "" ; then
        echo -n "password: "
        read -es password
        local pre="$username:$password@"
    fi

    echo -n "server: "; read server
    echo -n "port: "; read port
    local proxy=$pre$server:$port
    export http_proxy="$proxy" \
           https_proxy=$proxy \
           ftp_proxy=$proxy \
           rsync_proxy=$proxy \
           HTTP_PROXY=$proxy \
           HTTPS_PROXY=$proxy \
           FTP_PROXY=$proxy \
           RSYNC_PROXY=$proxy
}

function proxy_off(){
    unset http_proxy https_proxy ftp_proxy rsync_proxy \
          HTTP_PROXY HTTPS_PROXY FTP_PROXY RSYNC_PROXY
    echo -e "Proxy environment variable removed."
}
}}

Omit username or password if they are not needed.

As an alternative, you may want to use the following script.
Change the strings , ,  and  to match your own data, then edit your  to include the edited functions. Any new bash window will have the new functions. In existing bash windows, type .
You may prefer to put function definitions in a separate file like  then add  to  instead of putting everything in . You may also want to change the name "myProxy" into something short and easy to write.

{{bc|
#!/bin/bash

assignProxy(){
   PROXY_ENV="http_proxy ftp_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY FTP_PROXY ALL_PROXY"
   for envar in $PROXY_ENV
   do
      export $envar=$1
   done
   for envar in "no_proxy NO_PROXY"
   do
      export $envar=$2
   done
}

clrProxy(){
    PROXY_ENV="http_proxy ftp_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY FTP_PROXY ALL_PROXY"
    for envar in $PROXY_ENV
    do
       unset $envar
    done
}

myProxy(){
   user=YourUserName
   read -p "Password: " -s pass &&  echo -e " "
   proxy_value="http://$user:$pass@ProxyServerAddress:Port"
   no_proxy_value="localhost,127.0.0.1,LocalAddress,LocalDomain.com"
   assignProxy $proxy_value $no_proxy_value
}
}}

## Keep proxy through sudo
If the proxy environment variables are set for the user only they will get lost when running commands with sudo (or when programs use sudo internally).

A way to prevent that is to add the following line to a sudo configuration file:

## Automation with network managers
* NetworkManager cannot change the environment variables.
* netctl could set-up these environment variables but they would not be seen by other applications as they are not child of netctl.

## About libproxy
 is an abstraction library which should be used by all applications that want to access a network resource. It still is in development but could lead to a unified and automated handling of proxies in GNU/Linux if widely adopted.

The role of libproxy is to read the proxy settings from different sources and make them available to applications which use the library. The interesting part with libproxy is that it offers an implementation of the Web Proxy Autodiscovery Protocol and an implementation of Proxy Auto-Config that goes with it.

The  binary takes URL(s) as argument(s) and returns the proxy/proxies that could be used to fetch this/these network resource(s).

{{Note|1=the version 0.4.11 does not support  because {{ic|1={ pkg-config 'mozjs185 >= 1.8.5'; } }} fails .}}

## Web proxy options
* Squid is a very popular caching/optimizing proxy.
* Privoxy is an anonymizing and ad-blocking proxy.
*  is a small, efficient HTTP/SSL proxy daemon.
* For a simple proxy, ssh with port forwarding can be used.

## Simple Proxy with SSH
Connect to a server (HOST) on which you have an account (USER) as follows

 $ ssh -D PORT USER@HOST

For PORT, choose some number which is not an IANA registered port. This specifies that traffic on the local PORT will be forwarded to the remote HOST. ssh will act as a SOCKS server. Software supporting SOCKS proxy servers can simply be configured to connect to PORT on localhost. See  OpenSSH#Forwarding other ports.

## HTTPS MITM proxies
When debugging HTTPS connections it is sometimes useful to intercept them outside of the browser. In order for the TLS MITM to work you need to trust a certificate authority of the proxy either in your browser or system-wide.

*
*
*
*
*

## Using a SOCKS proxy
There are two cases:

* the application you want to use handles SOCKS5 proxies (for example Firefox), then you just have to configure it to use the proxy.
* the application you want to use does not handle SOCKS proxies, then you can try to use , , or torsocks.

In Firefox, you can use the SOCKS proxy in the menu Preferences > Network > Settings. Choose Manual Proxy Configuration, and set the SOCKS Host (and only this one, make sure the other fields, such as HTTP Proxy or SSL Proxy are left empty). For example, if a SOCKS5 proxy is running on localhost port 8080, put  in the SOCKS Host field,  in the Port field, and validate.

If using proxychains-ng, the configuration takes place in . You may have to uncomment the last line (set by default to use Tor), and replace it with the parameters of the SOCKS proxy. For example, if you are using the same SOCKS5 proxy as above, you will have to replace the last line by:

 socks5 127.0.0.1 8080

Then, proxychains-ng can be launched with

 $ proxychains program

Where  can be any program already installed on your system (e.g. xterm, gnome-terminal, etc).

If using proxy-ns, the configuration takes place in . You may have to change the socks5_address. An example configuration using SOCKS5 proxy as above looks like this:

{{hc|/etc/proxy-ns/config.json|2=
{
  "tun_name": "tun0",
  "tun_ip": "10.0.0.1/24",
  "socks5_address": "127.0.0.1:8080",
  "fake_dns": true,
  "fake_network": "240.0.0.0/4",
  "dns_server": "9.9.9.9"
}
}}

Then, proxy-ns can be launched with:

 $ proxy-ns program

The usage is the same as proxychains.

If using tsocks, the configuration takes place in . See  for the options. An example minimum configuration looks like this:

## curl and pacman
You may set the  environment variable to let curl and pacman (which uses curl) use your socks5 proxy:

 $ export all_proxy="socks5://your.proxy:1080"

## Proxy settings on GNOME
Some programs like Chromium and Firefox can use the settings stored by GNOME. These settings can be modified through the gnome-control-center front end and also through gsettings.

 gsettings set org.gnome.system.proxy mode 'manual'
 gsettings set org.gnome.system.proxy.http host 'proxy.localdomain.com'
 gsettings set org.gnome.system.proxy.http port 8080
 gsettings set org.gnome.system.proxy.ftp host 'proxy.localdomain.com'
 gsettings set org.gnome.system.proxy.ftp port 8080
 gsettings set org.gnome.system.proxy.https host 'proxy.localdomain.com'
 gsettings set org.gnome.system.proxy.https port 8080
 gsettings set org.gnome.system.proxy.socks host 'proxy.localdomain.com'
 gsettings set org.gnome.system.proxy.socks port 8080
 gsettings set org.gnome.system.proxy ignore-hosts "['localhost', '127.0.0.0/8', '10.0.0.0/8', '192.168.0.0/16', '172.16.0.0/12' , '*.localdomain.com' "

As GNOME is often used with NetworkManager, see also NetworkManager#Proxy settings. It does not appear that NetworkManager supports fetching the configuration from the GNOME settings above without a GNOME desktop.

## Microsoft NTLM proxy
In a Windows network, NT LAN Manager (NTLM) is a suite of Microsoft security protocols which provides authentication, integrity, and confidentiality to users.

A local proxy stands between your applications and the NTLM proxy, adding NTLM authentication on-the-fly.

 (NTLM PROXY IP:PORT + CREDENTIALS + OTHER INFO) -----> (127.0.0.1:PORT)

Two options are available from AUR:
*
*

## Alpaca
 from AUR is a local HTTP proxy for command-line tools. It supports proxy auto-configuration (PAC) files and NTLM authentication.

## Usage
Alpaca can be launched interactively, which requires entering a password:

 $ alpaca -d MYDOMAIN -u me
 Password (for MYDOMAIN\me):

To launch alpaca non-interactively, a NTLM hash needs to be generated and exported as a variable:

 $ ./alpaca -d MYDOMAIN -u me -H
 Password (for MYDOMAIN\me):
 NTLM_CREDENTIALS="me@DOMAIN:00000000000000000000000000000000"; export NTLM_CREDENTIALS

Alpaca will by default listen on , this can be overridden using the  and  options.

Furthermore a proxy PAC url should be provided as a parameter of the  option.

## Running as a service
 includes the  systemd user service, which can be used to start alpaca automatically in a non-interactive way.

It requires the following environment variables to be set in :

 LISTEN_ADDRESS=localhost
 LISTEN_PORT=3128
 NTLM_CREDENTIALS="me@DOMAIN:00000000000000000000000000000000"
 PAC_URL="http://some.url/to/some-file.pac"

## Cntlm
 from the AUR can be configured with several "parent" proxies and Cntlm will try one after another until one works. All authenticated connections are cached and reused to achieve high efficiency.

## Configuration
Change settings in  as needed, except for the password. Then run:

 $ cntlm -H

This will generate encrypted password hashes according to your proxy hostname, username and password.

Edit  again and include all three generated hashes, then enable .

To test settings, run:

 $ cntlm -v

## Usage
Use  or  as a proxy adress.  matches the  parameter in , which by default is .
