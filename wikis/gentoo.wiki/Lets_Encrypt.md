This page contains [[changes](https://wiki.gentoo.org/index.php?title=Let%27s_Encrypt&diff=1354356)] which are not marked for translation.

**Resources**

[[]][Home](https://letsencrypt.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Let%27s_Encrypt "wikipedia:Let's Encrypt")

[[]][GitHub](https://github.com/certbot/certbot)

[[]][Official documentation](https://letsencrypt.readthedocs.org/en/latest/)

[[]][[#letsencrypt](ircs://irc.libera.chat/#letsencrypt)] ([[webchat](https://web.libera.chat/#letsencrypt)])

[certbot], previously known as Let\'s Encrypt client, is a free, automated, and open [certificate](https://wiki.gentoo.org/wiki/Certificates "Certificates") authority client.

From the official website: \"Anyone who has gone through the trouble of setting up a secure website knows what a hassle getting and maintaining a certificate can be. Let's Encrypt automates away the pain and lets site operators turn on and manage HTTPS with simple commands.\"^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Preliminary]](#Preliminary)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [certbot]](#certbot)
        -   [[2.1.1] [USE flags]](#USE_flags)
        -   [[2.1.2] [Emerge]](#Emerge)
    -   [[2.2] [acme-tiny (optional)]](#acme-tiny_.28optional.29)
    -   [[2.3] [acme.sh (optional)]](#acme.sh_.28optional.29)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [certbot]](#certbot_2)
        -   [[3.1.1] [Automatic configuration for existing web server]](#Automatic_configuration_for_existing_web_server)
        -   [[3.1.2] [Automatic signing with temporary certbox webserver]](#Automatic_signing_with_temporary_certbox_webserver)
        -   [[3.1.3] [Manual certonly configuration]](#Manual_certonly_configuration)
    -   [[3.2] [acme-tiny]](#acme-tiny)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [certbot]](#certbot_3)
        -   [[4.1.1] [Invocation]](#Invocation)
        -   [[4.1.2] [Renewal]](#Renewal)
    -   [[4.2] [acmetiny]](#acmetiny)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Preliminary]

Point an external IP at HTTP (port 80/TCP) and HTTPS (port 443/TCP) at a web server and setup DNS for it. This is important. You have to prove you own the IP/domain. You could use dynamic DNS if necessary.

## [Installation]

** Tip**\
It is helpful to read the [official documentation](https://letsencrypt.readthedocs.org/en/latest/intro.html) and [official installation instructions (select Gentoo from the Operating System dropdown)](https://certbot.eff.org/) *before* proceeding with this article.

### [certbot]

#### [[] USE flags]

Let's Encrypt Certbot uses plugins to enhance its features. To simplify the maintenance of this modular approach, the [[[app-crypt/certbot]](https://packages.gentoo.org/packages/app-crypt/certbot)[]] ebuild uses USE flags to denote which plugins should be installed.

For example, to enable the `RFC 2136 DNS Authenticator` plugin:

[FILE] **`/etc/portage/package.use/certbot`**

    app-crypt/certbot certbot-dns-rfc2136

### [USE flags for] [app-crypt/certbot](https://packages.gentoo.org/packages/app-crypt/certbot) [[]] [Let\'s Encrypt client to automate deployment of X.509 certificates]

  ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`certbot-apache`](https://packages.gentoo.org/useflags/certbot-apache)                     Enable Apache plugin.
  [`certbot-dns-dnsimple`](https://packages.gentoo.org/useflags/certbot-dns-dnsimple)         Enable DNSimple Authenticator plugin.
  [`certbot-dns-dnsmadeeasy`](https://packages.gentoo.org/useflags/certbot-dns-dnsmadeeasy)   Enable DNS Made Easy DNS Authenticator plugin.
  [`certbot-dns-gehirn`](https://packages.gentoo.org/useflags/certbot-dns-gehirn)             Enable Gehirn Infrastructure Service DNS Authenticator plugin.
  [`certbot-dns-google`](https://packages.gentoo.org/useflags/certbot-dns-google)             Enable Google Cloud DNS Authenticator plugin.
  [`certbot-dns-linode`](https://packages.gentoo.org/useflags/certbot-dns-linode)             Enable Linode DNS Authenticator plugin plugin.
  [`certbot-dns-luadns`](https://packages.gentoo.org/useflags/certbot-dns-luadns)             Enable LuaDNS Authenticator plugin.
  [`certbot-dns-nsone`](https://packages.gentoo.org/useflags/certbot-dns-nsone)               Enable NS1 DNS Authenticator plugin.
  [`certbot-dns-ovh`](https://packages.gentoo.org/useflags/certbot-dns-ovh)                   Enable OVH DNS Authenticator plugin.
  [`certbot-dns-rfc2136`](https://packages.gentoo.org/useflags/certbot-dns-rfc2136)           Enable RFC 2136 DNS Authenticator plugin.
  [`certbot-dns-route53`](https://packages.gentoo.org/useflags/certbot-dns-route53)           Enable Route53 DNS Authenticator plugin.
  [`certbot-dns-sakuracloud`](https://packages.gentoo.org/useflags/certbot-dns-sakuracloud)   Enable Sakura Cloud DNS Authenticator plugin.
  [`certbot-nginx`](https://packages.gentoo.org/useflags/certbot-nginx)                       Enable Nginx plugin.
  [`doc`](https://packages.gentoo.org/useflags/doc)                                           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)                                         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-18 10:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [Emerge]

[certbot] is an easy-to-use automatic client that fetches and deploys SSL/TLS certificates for your web server. [certbot] can automatically configure your web server to start serving over HTTPS immediately.

`root `[`#`]`emerge --ask app-crypt/certbot`

[certbot] also supports numbers of DNS Authenticator plugins which automates the process of completing a dns-01 challenge (DNS01) by creating, and subsequently removing, TXT records. Starting from 3.2.0-r100, [[[app-crypt/certbot]](https://packages.gentoo.org/packages/app-crypt/certbot)[]] package includes almost all supported DNS plugins.

  -------------------------- ---------- --------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------
  Name                       Packaged   Description                                               Documentation                                                                                       Notes
  certbot-apache             Yes        Apache plugin.
  certbot-dns-cloudflare     No         Cloudflare DNS Authenticator plugin.                      [doc](https://certbot-dns-cloudflare.readthedocs.io/en/stable/)     Available in [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository.
  certbot-dns-digitalocean   No         DigitalOcean DNS Authenticator plugin.                    [doc](https://certbot-dns-digitalocean.readthedocs.io/en/stable/)
  certbot-dns-dnsimple       Yes        DNSimple DNS Authenticator plugin.                        [doc](https://certbot-dns-dnsimple.readthedocs.io/en/stable/)
  certbot-dns-dnsmadeeasy    Yes        DNS Made Easy DNS Authenticator plugin.                   [doc](https://certbot-dns-dnsmadeeasy.readthedocs.io/en/stable/)
  certbot-dns-gehirn         Yes        Gehirn Infrastructure Service DNS Authenticator plugin.   [doc](https://certbot-dns-gehirn.readthedocs.io/en/stable/)
  certbot-dns-google         Yes        Google Cloud DNS Authenticator plugin.                    [doc](https://certbot-dns-google.readthedocs.io/en/stable/)         Currently limited to architectures amd64, arm64 and x86.
  certbot-dns-linode         Yes        Linode DNS Authenticator plugin.                          [doc](https://certbot-dns-linode.readthedocs.io/en/stable/)
  certbot-dns-luadns         Yes        LuaDNS Authenticator plugin.                              [doc](https://certbot-dns-luadns.readthedocs.io/en/stable/)
  certbot-dns-nsone          Yes        NS1 DNS Authenticator plugin.                             [doc](https://certbot-dns-nsone.readthedocs.io/en/stable/)
  certbot-dns-ovh            Yes        OVH DNS Authenticator plugin.                             [doc](https://certbot-dns-ovh.readthedocs.io/en/stable/)
  certbot-dns-rfc2136        Yes        RFC 2136 DNS Authenticator plugin.                        [doc](https://certbot-dns-rfc2136.readthedocs.io/en/stable/)
  certbot-dns-route53        Yes        Amazon Web Services Route 53 DNS Authenticator plugin.    [doc](https://certbot-dns-route53.readthedocs.io/en/stable/)
  certbot-dns-sakuracloud    Yes        Sakura Cloud DNS Authenticator plugin.                    [doc](https://certbot-dns-sakuracloud.readthedocs.io/en/stable/)
  certbot-nginx              Yes        Nginx plugin.
  -------------------------- ---------- --------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------

### [][acme-tiny (optional)]

** Important**\
The package is masked by a missing keyword, to unmask it, follow the steps provided [here](https://wiki.gentoo.org/wiki/Knowledge_Base:Missing_keywords_and_keyword_requests#Resolution "Knowledge Base:Missing keywords and keyword requests").

[[[app-crypt/acme-tiny]](https://packages.gentoo.org/packages/app-crypt/acme-tiny)[]] is a short, auditable Python script which avoids a lot of the bloat included in the official certbot client:

`root `[`#`]`emerge --ask app-crypt/acme-tiny`

### [][acme.sh (optional)]

Another alternative available in Gentoo is the [[[app-crypt/acme-sh]](https://packages.gentoo.org/packages/app-crypt/acme-sh)[]] client:

`root `[`#`]`emerge --ask app-crypt/acme-sh`

## [Configuration]

### [certbot]

#### [Automatic configuration for existing web server]

Run certbot with the corresponding web server plugin and domain. Certbot automatically changes the vhost configuration. For example, for nginx:

`root `[`#`]`certbot --nginx -d example.com`

In order to use certbot with Apache web server, enable the additional plugin with its corresponding USE flag:

[FILE] **`/etc/portage/package.use/certbot`**

    app-crypt/certbot certbot-apache

`root `[`#`]`emerge --ask app-crypt/certbot`

#### [Automatic signing with temporary certbox webserver]

In this configuration certbot will start a wizard and then initiate up a temporary web server instance in order to generate signed certificates. Choose the second option in the list (`2`), and follow the wizard. When running an existing web server, first disable the web server before running this mode, then restart the web server when finished (click **\[Expand\]** below to see wizard output).

`root `[`#`]`rc-service nginx stop `

`root `[`#`]`certbot certonly`

    Saving debug log to /var/log/letsencrypt/letsencrypt.log

    How would you like to authenticate with the ACME CA?
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    1: Nginx Web Server plugin (nginx)
    2: Spin up a temporary webserver (standalone)
    3: Place files in webroot directory (webroot)
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Select the appropriate number [1-3] then [enter] (press 'c' to cancel): 2
    Plugins selected: Authenticator standalone, Installer None
    Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c'
    to cancel): example.letsencrypt.org
    Requesting a certificate for example.letsencrypt.org
    Performing the following challenges:
    http-01 challenge for example.letsencrypt.org
    Waiting for verification...
    Cleaning up challenges

    IMPORTANT NOTES:
     - Congratulations! Your certificate and chain have been saved at:
       /etc/letsencrypt/live/example.letsencrypt.org/fullchain.pem
       Your key file has been saved at:
       /etc/letsencrypt/live/example.letsencrypt.org/privkey.pem
       Your certificate will expire on 2021-07-17. To obtain a new or
       tweaked version of this certificate in the future, simply run
       certbot again. To non-interactively renew *all* of your
       certificates, run "certbot renew"
     - If you like Certbot, please consider supporting our work by:

       Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
       Donating to EFF:                    https://eff.org/donate-le

`root `[`#`]`rc-service nginx start`

#### [Manual certonly configuration]

Run certbot with the corresponding web-server plugin and domain, with the *certonly* option:

`root `[`#`]`certbot --nginx certonly -d example.com`

Configure your virtual host. For example, for nginx:

[FILE] **`/etc/nginx/vhost.d/example.vhost`vhost configuration**

    server
    server
    }

### [acme-tiny]

The documentation on [acme-tiny](https://github.com/diafygi/acme-tiny/) is the best place to look for the most up to date information, but has been summarized below:

Make a directory for challenges to be created in:

`root `[`#`]`mkdir /var/www/localhost/acme-challenge/`

Add this to the Apache http vhost; IE port 80 vhost:

[FILE] **`/etc/apache2/vhosts.d/00_default_vhost.conf`Challenge alias in Apache**

    Alias /.well-known/acme-challenge/ /var/www/localhost/acme-challenge/

    <Directory /var/www/localhost/acme-challenge/>
           AllowOverride None
           Require all granted
    </Directory>

Set these in the Apache https vhost; IE port 443 vhost:

[FILE] **`/etc/apache2/vhosts.d/00_default_ssl_vhost.conf`SSL certificate settings for Apache**

    SSLCertificateFile /var/lib/letsencrypt/chained.pem
    SSLCertificateKeyFile /var/lib/letsencrypt/domain.key

Make a directory to hold the various files related to LE:

`root `[`#`]`mkdir /var/lib/letsencrypt `

`root `[`#`]`cd /var/lib/letsencrypt `

Create an account key, domain key and a CSR (replace www.example.co.uk with your host name):

`root `[`#`]`openssl genrsa 4096 > account.key `

`root `[`#`]`openssl genrsa 4096 > domain.key `

`root `[`#`]`openssl req -new -sha256 -key domain.key -subj "/CN=www.example.co.uk" > domain.csr `

Register and create the certificate file:

** Important**\
acme-tiny **may fail** its own token availability check [\[1\]](https://github.com/diafygi/acme-tiny/blob/master/acme_tiny.py#L142), even though the token is actually available. If the problem occurs, the check should be disabled using the `--disable-check` flag.

`root `[`#`]`/usr/bin/acme-tiny --account-key ./account.key --csr ./domain.csr --acme-dir /var/www/localhost/acme-challenge/ > ./chained.pem `

Reload configs for webserver:

`root `[`#`]`service apache2 reload`

or

`root `[`#`]`service nginx reload`

or

`root `[`#`]`service lighttpd reload`

Sample renewal script:

[FILE] **`/usr/bin/local/renew-le-cert`LetsEncrypt Cert renew script**

    #!/bin/sh
    /usr/bin/acme-tiny --account-key /var/lib/letsencrypt/account.key --csr /var/lib/letsencrypt/domain.csr --acme-dir /var/www/localhost/acme-challenge/ > /var/lib/letsencrypt/chained.pem.tmp || exit
    mv /var/lib/letsencrypt/chained.pem.tmp /var/lib/letsencrypt/chained.pem
    service apache2 reload

Add a monthly cron job:

[FILE] **`CRONJOB`**

    # Renew Lets Encrypt certificate
    0 0 1 * * /usr/local/bin/renew-le-cert.sh 2>> /var/log/acme_tiny.log

## [Usage]

### [certbot]

#### [Invocation]

`user `[`$`]`certbot --help`

      certbot [SUBCOMMAND] [options] [-d DOMAIN] [-d DOMAIN] ...

    Certbot can obtain and install HTTPS/TLS/SSL certificates.  By default,
    it will attempt to use a webserver both for obtaining and installing the
    certificate. The most common SUBCOMMANDS and flags are:

    obtain, install, and renew certificates:
        (default) run   Obtain & install a certificate in your current webserver
        certonly        Obtain or renew a certificate, but do not install it
        renew           Renew all previously obtained certificates that are near
    expiry
        enhance         Add security enhancements to your existing configuration
       -d DOMAINS       Comma-separated list of domains to obtain a certificate for

      (the certbot apache plugin is not installed)
      --standalone      Run a standalone webserver for authentication
      (the certbot nginx plugin is not installed)
      --webroot         Place files in a server's webroot folder for authentication
      --manual          Obtain certificates interactively, or using shell script
    hooks

       -n               Run non-interactively
      --test-cert       Obtain a test certificate from a staging server
      --dry-run         Test "renew" or "certonly" without saving any certificates
    to disk

    manage certificates:
        certificates    Display information about certificates you have from Certbot
        revoke          Revoke a certificate (supply --cert-name or --cert-path)
        delete          Delete a certificate (supply --cert-name)
        reconfigure     Update a certificate's configuration (supply --cert-name)

    manage your account:
        register        Create an ACME account
        unregister      Deactivate an ACME account
        update_account  Update an ACME account
        show_account    Display account details
      --agree-tos       Agree to the ACME server's Subscriber Agreement
       -m EMAIL         Email address for important account notifications

    More detailed help:

      -h, --help [TOPIC]    print this message, or detailed help on a topic;
                            the available TOPICS are:

       all, automation, commands, paths, security, testing, or any of the
       subcommands or plugins (certonly, renew, install, register, nginx,
       apache, standalone, webroot, etc.)
      -h all                print a detailed help page including all topics
      --version             print the version number

#### [Renewal]

Let\'s encrypt certificates only last 90 days before expiry, thankfully it is easy to renew certificates: run [certbot renew] to automatically renew all certbot certificates on the system. It is recommended to run this in a [cron](https://wiki.gentoo.org/wiki/Cron "Cron") command, every 60 days.

To renew just a specific domain, run [certbot certonly \--force-renew -d example.com].

### [acmetiny]

For those that are not interested in using scripts or want to configure things manually the first time, the author of acme-tiny has provided a webpage that gives step by step instructions along with javascript to help walk you through setting up your certificates. The guide may be found on [Get HTTPS for Free](https://gethttpsforfree.com/) website.

## [See also]

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") --- an efficient, extensible [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers"). It is one of the most popular web servers used the Internet.
-   [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") --- a robust, small, high performance [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") and reverse proxy server.
-   [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") --- a fast and lightweight [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers").

## [External resources]

-   [Manual installation](https://letsencrypt.readthedocs.org/en/latest/using.html#installation) - In the event manual installation is preferred. Note: Portage will not track the installation if the Let\'s Encrypt is manually installed; this is *not* recommended by Gentoo developers.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://letsencrypt.org/getting-started/](https://letsencrypt.org/getting-started/)]]