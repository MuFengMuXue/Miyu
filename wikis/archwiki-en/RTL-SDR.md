# RTL-SDR

RTL-SDR is a set of tools that enables DVB-T USB dongles based on the Realtek RTL2832U chipset to be used as cheap software defined radios, given that the chip allows transferring raw I/Q samples from the tuner straight to the host device.

See the RTL-SDR wiki for exact technical specifications.

## Installation
The latest stable RTL-SDR version can be installed from .

udev rules are installed at  and set the proper permissions such that non-root users can access the device.

rngd claims rtlsdr devices by default - exclude it's use in  with

## Usage
Performing a simple test, and make sure the dongle works and that there are no lost samples:

 $ rtl_test

Raw samples can be captured directly to file (or fifo), for example to tune to 123.4MHz and capture 1.8M samples/sec:

 $ rtl_sdr capture.bin -s 1.8e6 -f 123.4e6

Tune to your favorite radio station and pipe to sox for audio:
 $ rtl_fm -f 102.7e6 -M wbfm -s 200000 -r 48000 - | aplay -r 48000 -f S16_LE

## Using on a headless server
To use an RTL SDR device over , add the user you are logging in as to the  user group.

Now, log out and back into a new  session. The groups that your user is a member of can be listed with the following:

 # groups

If the  group shows up, the current user should now be able to use any application that uses the RTL SDR USB device over .

Note that being a member of the  group is not necessary if you are logging into your system over a TTY or through a GUI login manager. In that case, the  piece of the  config file handles giving you access to the RTL SDR USB device. More details on this are available in .

## Applications
Some popular applications that use RTL-SDR:

*  - a popular SDR receiver with waterfall GUI for Linux
*  - complete suite for wireless protocol investigation with native support for many common SDR
*  - a lightweight ModeS (1090Mhz) decoder
*  - a decoder for various digital modes
*  - protocol aware receiver for multiple devices. Supports automatic packet interception and protocol analyzers for reverse engineering.
*  - Random number generator related utilities
*  - SDR receiver application with a number of features.

## Troubleshooting
When using certain tuners (like generic/unbranded "DVB" devices), the signal can get overloaded very easily even at low gain levels. This is an issue starting with version 2.0.1 of the official  package, which switched from a fork to the official Osmocom repository.
To fix this, the package must be downgraded to version 0.8.0-6, or alternatively use the  package which points to the fork repository which does not have this issue. Any applications which use the libraries from the rtl-sdr package must be re-built against the alternative package.
