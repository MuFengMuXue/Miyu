# Twister

Twister is an experimental peer-to-peer microblogging software.

## Installation
Install  and the  html interface.

## Configuration
Start/enable .

This will by default load both the twister-core daemon, and the twister-html gui.

Connect to http://user:pwd@127.0.0.1:28332/home.html

In the Network tab, wait until the daemon downloads the entire blockchain.

In the Login tab, create a new user. Wait a few seconds for the daemon to calculate the Proof-Of-Work to propagate your registration. You’ll be redirected to the Edit Profile tab: complete it. Wait a few minutes until your registration is accepted into a new block. The “Save” button will be disabled in the meantime.

The next time you enter the page, press "Login" and choose your newly created user to login.

## Graphical interface
The twister-html interface can be accessed at http://127.0.0.1:28332/home.html. It allows full configuration of Twister, and can be used to create and read posts.

## JSON/CLI Interface
Twisterd comes with a command line based utility, that can be used run and configure twister. However, this interface is an overlay on the JSON-RPC interface, and therefore is mostly useful for debugging and development. See the following page for the full documentation of this interface http://twister.net.co/?page_id=58.
