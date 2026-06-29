# Hylafax

From HylaFAX home page:
:HylaFAX is an enterprise-class system for sending and receiving facsimiles as well as for sending alpha-numeric pages. The software is designed around a client-server architecture. Fax modems may reside on a single machine on a network and clients can submit an outbound job from any other machine on the network. Client software is designed to be lightweight and easy to port. HylaFAX is designed to be very robust and reliable. The fax server is designed to guard against unexpected failures in the software, in the configuration, in the hardware and in general use. HylaFAX can support multiple modems and a heavy traffic load. If you expect to send more than a few facsimiles a day, then HylaFAX is the fax package for you!

## Installation
Install the  package.

It could be that you need a MTA installed like Postfix:

* After installation run  as the root user. Answer the questions and modify to your needs.
* Run  as the root user. It asks you for the device, leave out the  prefix; only enter eg. modem, ttyS0 or such things.
* Answer the other questions, important ones could be the ringtones, max pages, permissions on files or your the name that should be shown.
* Enable the service for the daemon. Assuming your modem is on ttyS0, the service would be .
* The package contains further services and systemd timers to start/enable for your usage. For example,  and .

Your received faxes will be saved in  and deleted after 30 days.  Your sent faxes will be saved in .

## Tips and tricks
## FaxDispatch
You can create a FaxDispatch file that will allow you to convert incoming faxes to pdf or other and direct where these are sent.  Examples are all over the Internet, but be aware that FaxDispatch does not go into , but rather into .

A simple FaxDispatch that converts to pdf and sends the fax to a particular address would be:

 FILETYPE=pdf
 SENDTO=myaddress@myemail.whatever

## Pagesize
HylaFAX defaults are made for North America settings. Pagesize of send faxes can be adjusted in  for A4 default setup please change the file to that:

## No dialtone error or if you are a laptop user
If you need a special number to get the Dialtone add this to:

 /var/spool/hylafax/etc/config.yourdevicename

Uncomment the  line, and change  to

## For laptop users it might be helpfull to deactivate the dialtone check
Uncomment the  line, and change  to

## Automatic fax printing
Add this to  at the end:

 /usr/bin/tiff2ps -a -h 11.1082 -w 7.8543 $FILE | /usr/bin/lpr -P yourprintername

This setup is for A4 pagesize, adjust -h and -w to your needs if you need an other size.

## Disabling MTA actions
Normally HylaFAX uses a MTA to receive faxes, if you do not need that change, your
.

Change  to

## Enable automatic printing of notifications
If you want notifications to be printed out and not mailed, change your

# Change  to  and at the end of that file.
# Comment this line:
# Add this as next line:

Remember to add your changed file to pacmans NoUpgrade list else your changes might get lost on update.

## Useful commands
For more options please read the manpages of each program.

## Frontends for HylaFAX
GNU/Linux Clients:

* Avantfax is a PHP56, MySQL enterprise class frontend to HylaFAX (by one of the HylaFAX developers David Mimms). Get it here: http://www.avantfax.com/download.php
* kfax is a nice application to view the received tiff files.
* KDE has a printer to send your document to fax, change it to use the HylaFAX backend.

Windows clients:

* WFHC is a nice HylaFAX client for Windows. Get it here: https://web.archive.org/web/20060830182240/http://www.uli-eckhardt.de/whfc/.
* SuSEfax is also a nice client for Windows. Get it here: https://web.archive.org/web/20050128145713/http://ftp.suse.com/pub/suse/discontinued/i386/SuSEFax_WIN32/.
