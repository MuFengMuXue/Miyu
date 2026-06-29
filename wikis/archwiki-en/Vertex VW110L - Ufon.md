# Vertex VW110L - Ufon

This article details the configuration and use of the Vertex VW110L modem for the U:Fon service.

## Installation
Install  and , then create the following override:

{{hc|/etc/udev/rules.d/40-usb_modeswitch.rules|2=
ATTR{idVendor}=="05c6", ATTR{idProduct}=="1000", RUN+=""
}}

Reload udev rules, then plug the Vertex modem in and wait for few second until the red LED on the edge of modem change color to blue.

You should be able to access .

Try screen or  to send AT commands to your modem.

## Usage
The modem can now receive AT commands, for example:

*  − signal strength (first number) - https://www.gprsmodems.co.uk/images/csq1.pdf
*  − modem info

## Configuration
To use with pppd, create:

and manage connection with  for connecting and  for disconnecting.
