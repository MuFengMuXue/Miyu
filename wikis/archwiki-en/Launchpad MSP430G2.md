# Launchpad MSP430G2

This page explains how to use Energia for the Launchpad MSP-EXP430G2 board.

## Installation
Install the  package.

## Configuration
Create a udev rule to allow regular users access to the device:

{{hc|/etc/udev/rules.d/10-launchpad.rules|2=
ACTION!="remove", SUBSYSTEM=="usb", ATTR{idVendor}=="0451", ATTR{idProduct}=="f432", MODE="0660", TAG+="uaccess"
}}

Add yourself to the  and  user groups.

Plug your launchpad and start energia.
