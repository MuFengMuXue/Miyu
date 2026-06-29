# Webmin

From the project home page:
:Webmin is a web-based interface for system administration for Unix. Using any modern web browser, you can setup user accounts, Apache, DNS, file sharing and much more. Webmin removes the need to manually edit Unix configuration files like , and lets you manage a system from the console or remotely. See the standard modules page for a list of all the functions built into Webmin, or check out the screenshots.

## Installation
Install the  package.

## Configuration
To allow access to Webmin from a remote computer, configure your firewall to allow access to TCP port 10000. You may want to configure your firewall to restrict access only from certain IP addresses.

## Change port
To change the port, edit the  variable in the  file.

To disable SSL and avoid  change:

## Bind to localhost (only)
To bind Webmin to  (only), add the following line into your  file.

## Usage
Start  or enable it if you wish to load webmin at boot.

In a web browser, enter the https address of the server with the port number 10000 to access Webmin:

 https://host:10000

You will need to enter the root password of the server running Webmin to use the Webmin interface and administer the server.
