# ZeroNet

ZeroNet gives access to "open, free and uncensorable websites, using Bitcoin cryptography and the BitTorrent network".

## Installation
Install the  package.

## Configuration
## Starting
To start ZeroNet start/enable .

## Tor
By default, ZeroNet uses clearnet and Tor if available. To enable Tor support you first need to install Tor. Then, give ZeroNet access to control Tor using the following instructions.

 # usermod -a -G tor zeronet

Append or edit the following options in :

You may also want to start/enable .

Check the Tor file permissions:

 # stat -c %a /var/lib/tor

This should print . if not, run

To force all ZeroNet connections through Tor, append to your  file

## Creating ZeroNet sites
All operations, including editing ZeroNet site files, should be done as user . Use  to specify the configuration file.  use  as data directory by default. For example:

 python zeronet.py --config_file /etc/zeronet.conf

All sites you create will have their initial data folder setup in . For more information on how to create a Zite, please follow the guidelines on the [https://zeronet.readthedocs.io/en/latest/using_zeronet/create_new_site/ ZeroNet FAQ.
