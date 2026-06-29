# Hiawatha

Hiawatha is an open source web server with security, ease of use and lightweight as its three key features. It supports among others CGI, FastCGI, IPv6, URL rewriting and reverse proxy and has security features no other webserver has, like blocking SQL injections, XSS, CSRF and exploit attempts.

## Installation
Install the  package.

## Configuration
## Directory structure
First, to give an overview of the overall directory structure of Hiawatha, the hierarchy suggested by the default configuration is shown below:

*  - program configuration files
*  - website TLS certificate
*  - root for the default blank website associated with the IP address
*  - cache for http compression and uploads
*  - log files for the program and the default website
*  - website root
*  - website log files

## Basic webserver setup
The Hiawatha configuration file is . A configuration file example  is provided.

In the sample setup, there is one default website attached to the IP address of the domain, it is a dummy one directing to a blank html page. This is the page IP scanning robots and hackers will face.

Then, the working webservers are defined with  sections. Hiawatha can serve more than one webserver and each of these sections describes a different one. For initial testing purpose, you can create one  for my-domain and save in its root directory  a dummy  start file.

Next, enable and start  and point your browser to . At that stage you should be able to load the website start page.

For further details, see the official how to and the  manual page.

## CGI
Common Gateway Interface (CGI) scripts work with Hiawatha out of the box, the CGI module in the  section just needs to be enabled as follows:

{{hc|/etc/hiawatha/hiawatha.conf|2=
VirtualHost {
    ...
    ExecuteCGI = yes
}
}}

## Interpreters for CGI scripts
To use CGI scripts in your website, you have to specify the common script file extension and the location of the binary that can run them. This is indicated in the main body of the configuration file:

 CGIhandler = /usr/bin/php-cgi:php
 CGIhandler = /usr/bin/perl:pl
 CGIhandler = /usr/bin/python:py

For further details see the official HowTo.

## FastCGI
Install .

Hiawatha supports two different methods to send information to the FastCGI process: the webserver can communicate over either a Unix domain socket or a TCP connection. The communication type is defined in the  section via the field .

## Enable SSL/TLS
First, a X.509 SSL/TLS certificate is required to use TLS. If you do not have one, you can use a #Self-signed certificate or use one for free from #Let's Encrypt certificate authority.

The order of the items in the certificate file must be as follows:

For SSL/TLS support, the following  section that configures Hiawatha to use a certificate for HTTPS connections should be added:

{{hc|/etc/hiawatha/hiawatha.conf|2=
Binding {
    Port = 443
    TLScertFile = /etc/hiawatha/tls/serverkey.pem
}
}}

Once it is done, restart .

{{Tip|Hiawatha supports Server Name Indication, which allows to serve multiple certificates on the same IP address and hence multiple secure websites. To use this functionality, add a  setting inside the  block for each virtual host that has its own SSL/TLS certificate. The certificate specified in the  section is used whenever no virtual host has been defined for a website.

{{hc|/etc/hiawatha/hiawatha.conf|
VirtualHost {
    Hostname = www.website.org
    ...
    TLScertFile = website.pem
}
}}
}}

## Reverse proxy
Hiawatha's man pages suggest using the following:

 ReverseProxy [ http[ is the time in seconds Hiawatha tries to connect to the other webservice. Adding  enables keep-alive connections to the final webserver.

As an example, a webservice reverse proxy configuration which forwards requests from  to another local running web service on port  looks like (timout 10s):

{{hc|/etc/hiawatha/hiawatha.conf|
VirtualHost {
        Hostname = service.domain.net
        WebsiteRoot = /var/www/domain
        StartFile = index.html
        ReverseProxy .* http://127.0.0.1:8181/ 10
        RequireTLS = yes
}
}}

If a UNIX socket is needed instead:

 ReverseProxy .* /unix/socket 10

## Certificates
## Self-signed certificate
To get a local self-signed certificate for personal use, testing or web development, the procedure in OpenSSL#Generate a self-signed certificate to create both a private key and a self-signed certificate can be followed.

Make sure you did add the SSL bundle path to your  as stated in #Enable SSL/TLS.

As this solution does not use an official certificate authority (CA), a security exception will need to be added the first time the website is visited.

## Let's Encrypt certificate
## Configure
Hiawatha provides a script to obtain a Let’s Encrypt certificate in an automated fashion using the ACME v2 protocol.

A configuration file example  is provided in the directory . Two steps are needed to setup lefh:
# Copy the sample configuration file to the user's area , typically  if hiawatha is run as a system service.
# Edit the settings, in particular replace the value of  by the chosen email address, lefh will not run with the initial example email address.

## Obtain a certificate
The detailed instructions are described in  and the tool's configuration is defined in . In short, there are two steps to get a certificate:

#Register an account with the Let's Encrypt certificate authority (CA). An account key file will be created.
#Request a website certificate: www.my-domain.org must be the first hostname of a . Any following webserver's hostname will be used as an alternative hostname for the certificate. Note that wildcards can not be used in the hostname: even if Let's Encrypt accept this functionality, it can only be obtained via DNS challenge and this method is not supported by lefh.
The file  will be created.

If the above succeeds, you can switch from the ''testing to the production CA by changing the  setting in the configuration file and go through the two steps''' above again. Do not rush into production before making sure the test was successful: letsencrypt enforces rate limit for failed attempts and one may get temporarily banned.

## Auto renewal
The following command can be used to renew the certificate and restart the server upon renewal:

 # lefh renew restart

By default, the certificate will be renewed whenever it has less than 7 days to go and it will be written in the directory indicated in . The number of days before renewal can be controlled via the  setting.

A daily schedule of this script is appropriate as no action will be taken anyway before the threshold is reached.
This daily automation can be achieved using either cron or systemd/Timers:

## Automation with cron
In order to automate the renewal of the certificate, schedule a cronjob for the root user to run the command line above.

## Automation with a systemd timer
A systemd timer can be used for the repetition of the renewal process:

Start and enable .
