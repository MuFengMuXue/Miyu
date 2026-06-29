# Smartcards

This page explains how to setup your system in order to use a smart card reader.

Smartcards are, generally speaking, an ISO-7810 ID-1 sized plastic card with a microcontroller and some memory embedded in them, and usually interface with a computer or other equipment through a electrical contact pad on the card. Through their design,  smartcards cannot be reprogrammed after their 'fuses' have been set after programming by the manufacturer. Because of this, the behaviour of a smartcard can not be altered afterwards. This in turn enables the microcontroller to be programmed in such a way that it does not allow external dumping of the internal memory, and therefore protecting the information such as private keys contained within the smartcard.

Smartcards can have cryptographic hardware modules embedded into their design, supporting one or more cryptographic algorithms.  This combined with their protected memory allows these cards to be used as a secure hardware element, and have been used for payment processing, system or user authentication and related uses for decades. Examples are, but are not limited to, payment cards (EMV), mobile telephony SIM-cards and public-private cryptography.

Please be aware that the term "Smartcard" generally does not include EEPROM-cards (so called memory cards) or protected EEPROM-cards (so called logic cards) such as SLE4442 cards. These cards either contain a straight EEPROM, or a very basic microcontroller without any cryptographic functionalities.

Dual-Interface cards provide both contactless (NFC) and contact-based communication interfaces. However, depending how the card has been programmed by the manufacturer or the user, not all services may be available through the contactless interface.

## Installation
Install  and .

Enable and start .

## FIDO2/U2F support
Javacard (such as J3R180) with FIDO2 applet installed can provide similar functions like a yubikey.

install . ( since  do not have pcsc support enabled )

The FIDO2 applet is suit for ecdsa-sk ssh keys and systemd-homed, also U2F.

## Configuration
## Mozilla Firefox
The browser needs to set the new security-related device.
Open the Security Devices page (reach it via Preferences > Privacy & Security > Certificates > Security Devices), then click Load and set the Module Name to CAC Module and module filename to .

## Chromium
Chromium uses NSS. Open a shell in your home directory and verify that the CAC Module is not already present:

If not, close any browser and add the module (an user interaction for confirmation is required):

Check for the correct execution of the command:

## Tips and tricks
## Scan for readers and cards
Install  and start the  utility, then connect the Smart card reader and finally insert a card.
If you see output like this, the smart card reader and also the card have been successfully recognized.

## OpenSC
The  package provides an optional set of libraries and utilities to work with smart cards using , including tools to discover and investigate card contents.

##
p11-kit is a framework that provides a way to load and enumerate PKCS#11 modules, and a standard configuration setup for installing PKCS#11 modules in such a way that they're discoverable.

It also provides a proxy to allow aggregating and managing multiple devices (which may each require different pkcs11 drivers) as one.

## p11tool
If using packages from the GnuTLS suite which utilize p11-kit, such as p11tool, the OpenSC driver might not properly load. This can be determined if you run  and you do not see your hardware token in the list.

In this case, you'll need to create a .module file to expose the pkcs11 module for your card to p11-kit, either in the user directory at , or in the system directory which can be looked up with  The  directive specifies the location of the pkcs11 module to expose:

If the card reader does not have a PIN pad, append the line(s) and set  in the opensc configuration file /etc/opensc.conf

## SafeNet eToken
Class of Tokens and SmartCards from ThalesGroup. Used by companies like Certisign.

Install the  to pkcs11 library installation.

## SafeNet eToken on Google Chrome
Module needs to be added to nssdb:

To confirm it's installed:

## Smargo/TV Card reader
When interfacing with a TV-card for live TV and recording (PVR/DVR), you may need to assign the smartcard reader to the  user group allowing decryption. When using a Smargo Smartreader consider the following udev rule:

{{hc|1=/etc/udev/rules.d/98-smargo.rules|2=
SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", GROUP="video", MODE="0666", SYMLINK+="smargo"
}}

Set  as the reader device when using softcam applications like OSCam.

## Troubleshooting
## Firefox can't access data
If the browser is not able to use the smart card data, probably it is not aware of the service which provides access to the device. This happens if you plug in the smart card reader after you open Firefox.
To solve this issue, simply restart Firefox.

## LIBUSB_ERROR_BUSY
PC/SC can conflict with GnuPG for access to smartcards. See Ludovic Rousseau's blog and GnuPG#GnuPG with pcscd (PCSC Lite).
