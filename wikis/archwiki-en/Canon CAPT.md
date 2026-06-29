# Canon CAPT

CAPT (Canon Advanced Printing Technology) is Canon's proprietary driver, supporting the Canon i-Sensys series of laser printers. For more information, see Setting up CAPT printers on Ubuntu.

## Installation
Install the  package.
It depends on 32-bit library packages and requires enabling multilib.

There is also an open source CAPT driver in early alpha stage not described here, available as .

## Configuration
Canon's driver uses a local daemon to communicate with the printer, and wraps that using a CUPS driver.

To configure the printer, follow the CUPS article, adding a CAPT printer and using a Printer URI of . Find the right model using , or check the table provided on the Ubuntu help page, which matches each supported printer with its corresponding PPD.

Next, register the printer with the CAPT driver itself via ccpdadmin. Replace  with the queue descriptive name and  with either the USB port (e.g. ) in case of a local printer or the IP address, prefixed by  (e.g. ), in case of a network printer:

 # ccpdadmin -p queue_name -o printer_address

For example, for a USB printer (in case of multiple USB-connected printers, read #Collisions with other printers):

 # ccpdadmin -p LBP6310 -o /dev/usb/lp0

Or for a network printer:

 # ccpdadmin -p LBP6310 -o net:192.168.1.100

Start/enable the CAPT daemon with .

To remove a printer:

 # ccpdadmin -x queue_name

## CAPT status monitor
## Local CUPS
The driver includes a status monitor which can be launched with

 $ captstatusui -P printer_model

e.g.

 $ captstatusui -P LBP6310

If you only want the status monitor to pop up when a problem occurs, simply append the  switch:

 $ captstatusui -P LBP6310 -e

## Remote CUPS
Unfortunately, a local installation of captstatusui will not detect CAPT printers on a remote CUPS server.

Remote print monitoring can be achieved, however, using SSH and X11 forwarding.

## Client configuration
* create a new SSH key  and copy the public key to the remote server
* create a file  with the following content, make it executable and place it in your autostart folder:

 #!/bin/sh
 ssh -T -Y -i ~/.ssh/capt remote_server_hostname_or_IP_address < /dev/null

## Server configuration
* create a new user
* append the following section to  and restart the SSH daemon or socket

 ...
 Match User capt
        X11Forwarding yes
        PermitTTY no
        ForceCommand captstatusui -P printer_model -e
        AuthenticationMethods publickey

e.g.

 ...
 Match User capt
        X11Forwarding yes
        PermitTTY no
        ForceCommand captstatusui -P LBP6310 -e
        AuthenticationMethods publickey

This can be extended to include multiple users (using a single, shared SSH key or each with a unique SSH key) by adding each user to a  group, then using a Match Group rule:

 ...
 Match Group capt
        X11Forwarding yes
        PermitTTY no
        ForceCommand captstatusui -P LBP6310 -e
        AuthenticationMethods publickey

## Troubleshooting
## Conflict with CUPS
To prevent CUPS from accessing our CAPT-only printer (and confusing the firmware with multiple setup requests over USB), a list of unsupported VID/PID pairs may be added into . A new file (e. g. ) may be created to prevent the list from getting overwritten by CUPS updates. See the issue on GitHub: Cups attempts to probe, configure unsupported Canon CAPT USB printers.

## Collisions with other printers
Other printers connected to the computer may create their own /dev/usb/lpN entries, possibly even before your Canon printer is enumerated and initialized, causing CAPT to access devices it shouldn't be touching. A symlink to the USB device can be created automatically by Udev based on the USB VID/PID and (optionally) the serial number reported in .

{{hc|/etc/udev/rules.d/50-canon.rules|
2=SUBSYSTEMS=="usb", ATTRS{idVendor}=="04a9", ATTRS{idProduct}=="271c", ATTRS{serial}=="0000A2BARL02", SYMLINK+="usb/lbp7010c"
}}

Then, add the symlinked path to CCPD:

 # ccpdadmin -p LBP7010C -o /dev/usb/lbp7010c

Source: Arch Forums: "/dev/usb/lp1" is used instead of "/dev/usb/lp0" for printers
