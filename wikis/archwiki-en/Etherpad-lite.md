# Etherpad-lite

Etherpad-Lite or just Etherpad, is a collaborative, multi-user web-editor based on Node.js with the ability to import/export various office file formats.

## Installation
Install the  package.

## Configuration
## Database
For testing purposes, the default database backend for Etherpad is the file-based DirtyDB. With that, you can run and test Etherpad-Lite without any further configuration.

If you want to use MySQL, PostgreSQL or SQLite, you can adjust those settings in the settings.json file. Further, you can set a password for the administrator interface on http://localhost:9001/admin, change port and listening address, etc.

At least, do not forget to set a sessionkey, e.g. generate with  and  and write it down to .

Your Etherpad installation can be extended with plugins listed at the administrator interface.

## Address
the default IP is , change it to 127.0.0.1 as assumed later.

## Starting
Enable the  unit. You can then access Etherpad-Lite on  or directly access a pad on

## Known issues
## Crashes on some Pads
https://github.com/ether/etherpad-lite/issues/2516#issuecomment-79659984
