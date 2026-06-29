**Resources**

[[]][Home](https://sourceforge.net/projects/phpvirtualbox/)

[[]][GitHub](https://github.com/phpvirtualbox/phpvirtualbox)

**phpVirtualBox** is a web-based administration utility for [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox").

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Verify VirtualBox installation]](#Verify_VirtualBox_installation)
    -   [[2.2] [Create SSL certificate]](#Create_SSL_certificate)
    -   [[2.3] [Configure Apache virtual host]](#Configure_Apache_virtual_host)
    -   [[2.4] [Configure phpVirtualBox installation]](#Configure_phpVirtualBox_installation)
-   [[3] [Verification]](#Verification)
-   [[4] [External resources]](#External_resources)

## [Installation]

Currently, [[[app-emulation/phpvirtualbox]](https://packages.gentoo.org/packages/app-emulation/phpvirtualbox)[]] has no stable version, so you need to add it to your package.accept_keywords file.

`root `[`#`]`emerge --ask app-emulation/phpvirtualbox`

## [Configuration]

phpVirtualBox does not need a VirtualBox installation to be present on the same box where phpVirtualBox is installed. phpVirtualBox can connect to other machines where your virtual machines are installed. phpVirtualBox requires a web-server to be present on your box, so we will demonstrate an Apache configuration using SSL certificate to encrypt your communication with the server.

### [Verify VirtualBox installation]

VirtualBox **must** be compiled with the `vboxwebsrv` USE flag on the host where the virtual machines are located.

[FILE] **`/etc/portage/package.use`**

    app-emulation/virtualbox vboxwebsrv

### [Create SSL certificate]

First, we create our shiny new SSL certificate

-   Create our **secret** private key

`root `[`#`]`openssl genrsa -des3 -out virtualbox-server.key 4096`

-   You probably want to remove your private key, otherwise apache will ask you for it every time you start it

`root `[`#`]`openssl rsa -in virtualbox-server.key -out virtualbox-server.key`

-   Create our new Certificate Singing Request (CSR)

`root `[`#`]`openssl req -new -key virtualbox-server.key -out virtualbox-key.csr`

-   Sign the CSR using our private key

`root `[`#`]`openssl x509 -req -days 365 -in virtualbox-key.csr -signkey virtualbox-server.key -out virtualbox-server.crt`

-   Place certificate and private key somewhere safe

`root `[`#`]`cp virtualbox-server. /etc/apache2/ssl-data/.`

### [Configure Apache virtual host]

Assuming you already have a working Apache installation, you need to create a new virtualhost for your phpVirtualBox installation. This entry should look like this:

[FILE] **`/etc/apache2/vhost.d/99-virtualbox.conf`phpVirtualBox vhost configuation**

    <VirtualHost *:443>
            ServerName phpvirtualbox.mydomain.example # Change this to your domain name
            DocumentRoot /usr/share/webapps/phpvirtualbox/4.1.7/htdocs/
            SSLEngine On
            SSLOptions  StrictRequire
            SSLProtocol all -SSLv2
            SSLCertificateFile /etc/apache2/ssl-data/virtualbox-server.crt
            SSLCertificateKeyFile /etc/apache2/ssl-data/virtualbox-server.key
            <Directory />
                    AllowOverride All
            </Directory>
            <Location />
                    Options Indexes FollowSymLinks
                    Order deny,allow
                    SSLRequireSSL
            </Location>
            ErrorLog /var/log/apache2/virtualbox_error.log
    </VirtualHost>

The previous configuration is just an example, your installation/configuration may be a lot different.

### [Configure phpVirtualBox installation]

The key file for your phpVirtualBox installation is the [config.php] file deriving from [config.php-example] file

`root `[`#`]`cd /usr/share/webapps/phpvirtualbox/4.1.7/htdocs `

`root `[`#`]`cp config.php-example config.php `

Edit this file and change the following variables

[FILE] **`/usr/share/webapps/phpvirtualbox/4.1.7/htdocs/config.php`PHPVirtualBox configuation**

    var $username = 'john'; # user who owns the virtual machines on the remote (or local) server
    var $password = 'mysecretpass';  #password for that user

    /* SOAP URL of vboxwebsrv (not phpVirtualBox's URL) */
    var $location = 'http://192.168.1.205:18083/'; # Where are the virtual machines? This can either be 'localhost' or the IP or the remote server where your virtual machines are installed

## [Verification]

-   Start the vboxwebsrv init service on the host where your virtual machines are located (in our case on 192.168.1.205)

`root `[`#`]`/etc/init.d/vboxwebsrv start`

-   Restart Apache on the host where your phpVirtualBox was installed

`root `[`#`]`/etc/init.d/apache2 restart`

-   Connect to phpVirtualBox installation

Open your browser and connect to your phpVirtualBox by typing:

    https://phpvirtualbox.mydomain.example

-   You should be able to login using the default credentials

<!-- -->

    user: admin
    pass: admin

## [External resources]

-   [phpVirtualBox Wiki](https://github.com/phpvirtualbox/phpvirtualbox/wiki)