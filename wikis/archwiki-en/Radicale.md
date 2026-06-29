# Radicale

Radicale is a server designed to support the CalDav and CardDav protocols. It operates either as a standalone package using its own internal http server or can be integrated with an existing webserver.

## Installation
Install the  package.

The package creates the  user and service as per the Radicale systemd instructions, along with the  data folder, so you can just enable .

## Configuration
The easiest thing is to follow the instructions at the Radicale website.

The main configuration file is located at

If this is setup on a remote / headless system, consider adding the  option to enable remote access to the built-in web interface.

Many of the configuration options can be changed on the command-line:

 $ radicale --help

## Authentication
By default, anyone can access the web interface and create address books or calendars, so authentication should be considered.

Authentication is controlled by  which can use Apache httpasswd formatted passwords (as well as plaintext & other options). If you are not planning to install Apache HTTP Server, you can just use , , or an online htpasswd generator to generate the  hashes.

## Non-default Storage Location
By default, the Radicale package comes configured to store data in . If you want to change this you can specify another location in the configuration file but you must also adjust the systemd configuration. The included  file sets  which means systemd will not allow the service read-write access to any area outside . To get around this create a drop-in file with the following contents:

You can now tell Radicale to use your chosen location by editing the config file as in the Radicale documentation:

Changing  in both files to your chosen location.

## Integration
## Web Servers
Radicale provides its own web server (initially restricted to  only, accessible at  with any username and password), but it can be integrated with HTTP webservers like Apache HTTP Server via Reverse Proxy or the WSGI interface.

## Client support
Since it uses the CalDav and CardDav protocols, it should support most clients, particularly the officially supported.

The following list may or may not be accurate:

* Thunderbird
** To add calendars, on the calendar view click on "New Calendar" -> On the network, in the location field add the root address radicale is listening to, for instance , not the address of a single calendar, and Thunderbird will automatically discover all the calendars shared by radicale
* GNOME/Evolution, Contacts and Calendar
* KOrganizer ()
* InfCloud (), CalDavZAP, CardDavMATE
* syncEvolution ()
* DAVx⁵, Infomaniak kSync, Simple Contacts Pro SE for Android (ICSx⁵ will also works for single calendars, but DAVx⁵ is highly recommended over it for full experience, as will automatically detect all calendars and addressbooks that radicale exposes).
* Mac OSX Calendar/Contacts
* Apple iOS
** Note that iOS requires a SSL in order to sync CalDAV/CarDAV (as of iOS14 self-signed SSL is sufficient for Radicale to integrate as an account) this can be created by following the instructions in OpenSSL#Generate a self-signed certificate with private key in a single command.
*** Note also that key sizes must be greater than 2048 bits [https://support.apple.com/en-au/HT210176
