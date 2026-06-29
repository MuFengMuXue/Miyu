# Soundmodem

Written by Tom Sailer (HB9JNX/AE4WA) to allow a standard PC soundcard to act as a packet radio modem for use with the various AX.25 communication modes. The data rate can be as high as 9600 baud depending on the hardware and application.

## Installation
Install

## Usage
Execute soundmodem as root:

 # soundmodem

## Using soundmodem as a MKISS module
The permissions on the interface must be changed in order to make it user-readable:

 # chmod 666 /dev/soundmodem0
