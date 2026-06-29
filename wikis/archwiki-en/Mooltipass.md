# Mooltipass

The Mooltipass is an open hardware and open
software, hardware password keeper in which users store their credentials for
authenticating against web application, PAM session, and password protected applications.

The device can be used with any USB compatible system that supports
HID class devices.

As a daily based user, one is able to interact directly with the device
by using a clickable scroll-wheel or is free to use one of the available
browser extensions/applications.

## Introduction
The team behind Mooltipass was faced with the great complexity of
password based authentication which require a strict policy including:
* A unique password for every usage;
* A hardly-guessable password;

In order to combine security of such policy and usability people came
with software password managers like KeePass. Unfortunately, such
solution implies that all credentials remains in computer memory, so
it could eventually be stolen by a malicious software.

Mooltipass is an external device, on which credential are stored
encrypted using AES-CTR
and a key of 256 bits stored on an pin-locked smartcard.
When plugged, the Mooltipass emulates an HID device and will act like a
keyboard to send your credentials information to the targeted
application.
Even if an attacker is able to sniff at some point the communication
between the device and the host it is likely that they will not be able to
gather all credentials nor to inject their own data.

## Password storing
The smartcard previously introduced is used to identify an user. Note
that multiple user must have different smartcards, but can use the
same mooltipass.

Credentials are stored on the device flash memory with the following
information: domain, username, password, comments.

The following list limits of the storing capabilities:
* The flash memory is of 8Mb;
* One password can be up to 32 characters long;

## Firmware upgrade
The upgrade of the firmware is made with a signed bundle.
Every device gets a dedicated AES key fused into the board by the
main developer.

## Additional features
In addition, the mooltipass benefits from the
ATMega32u4
and exposes a custom Random Number Generator that is used to
generate random passwords.

## Udev rules
 provide udev rules that allow access to the
device for every classical user from a session or using libusb.

## Usage
Mooltipass has been designed to be easy to use for everyone. The main
way of interacting with it is through browser application and/or
extension.

## Chromium
Chromium was the first target for Mooltipass, the team created an extension (available from the Web Store) that
detects login forms on web page and selects the right credential for you
on the device. The user only has to check on the Mooltipass screen
that the request is legitimate and to approve/deny using the hardware
scroll-wheel.

See Chromium/Tips and tricks#U2F authentication for Webauthn support.

## Firefox
Like Chromium, Firefox users can use a Mooltipass extension for easy interaction between websites and credentials stored on the device.

## Moolticute
 is an effort to build a cross-platform application that
could interact with the mooltipass outside of a browser. The
application is based on C++/Qt and provide both a daemon that will
handle every operation with the device and an GUI application, that
could replace the chrome app.

## mc-cli
For scripting purpose there is  which allow one to
interact with the Mooltipass through moolticuted from the command line.

## mc-agent
 benefit from the filesystem support of Mooltipass
so users are able to store their (unencrypted) SSH keys. mc-agent
implement an SSH agent that allows to load the key from the device.

## Mooltipy
Last client implementation is
mooltipy that implement both
some CLI tools and an Python module that could be used for scripting.
