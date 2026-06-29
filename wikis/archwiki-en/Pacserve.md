# Pacserve

Pacserve allows to easily share pacman packages between computers. This is very useful if you have a slow internet connection and multiple machines running Arch Linux.

## Installation
Install .

Finally start/enable .

In case you use iptables, you will probably want to start  too. For other firewalls open TCP port  and UDP port . The UDP port can be limited to multicast traffic only.

## Configuration
The  can configured by editing  in . Run  to see the available options.

## Avahi
To announce and discover Pacserve using mDNS add the option  to  in .

## Standalone usage
Instead of pacman, use the pacsrv wrapper to perform an update, install packages and so on. It will automatically download all packages from the LAN, if someone hosts them with pacserve there. Otherwise it will just download them from the internet mirrors, as usually. For example:

 # pacsrv -Syu
 # pacsrv -S openssh

## Configure Pacman to use Pacserve
If you are always running the pacserve daemon and want pacman to use it without the wrapper, insert the following line (before any other  lines) in each repository in .

 Include = /etc/pacman.d/pacserve

Here is an example for the Xyne repository:

Alternatively (for official mirrors only), you may insert the  line at the top of the Pacman mirrorlist file or let pacman.conf-insert_pacserve generate a  file for you.

## Troubleshooting
## Problems if using external downloaders in pacman.conf
If you are using an external downloader such as wget, pacsrv may return errors when downloading. To work around these errors, simply quote the url and output formatting strings ( resp. ) using single quotes:

 XferCommand = /usr/bin/wget --timeout=6 --passive-ftp -c -O '%o' '%u'

## Machines do not see each other
Peers detection relies on version of .
TCP multicast frames coming from a different version of the service are discarded.
In this case, running  as root will warn about such unrecognized frames.
Upgrade this package first then restart the .
