# Hauppauge Nova-T Stick

The Hauppauge Nova-T Stick is an USB2.0 DVB-T tuner with an additional antenna port. It features:

* Microtune MT2060 tuner
* Dibcom DVB-T demodulator
* USB 2.0 controller
* Remote control

## Installation
Plug in your Nova-T Stick. You should see the following:

The stick has been recognized, but it is not working yet because the firmware was missing. Download the firmware file and copy it to .

Depending on your box number (e.g. 293) or device number (e.g. 70009), the kernel may require the firmware version to be . Either rename the firmware linked above or use a link.

Plug in the USB stick again, the result should look like this:

## Configuration
## User permissions
In order to have access to the USB stick, you will have to add yourself to the  user group.

## Getting channels
Install .

We need a initial scan file. This file is needed for scan to work properly. It provides a frequency that scan is going to use as a starting point from which it will proceed with its scan. These files are specific to your geographic location and have the form of , where cc is a two-letter country code. You will find scan files in the official dvb-apps repository.

If you cannot find a suitable initial scan file, then you can build your own with :

 $ w_scan -x > cc-Location

For example in Leipzig, Germany; you would look for a file called :

 $ scan de-Leipzig > leipzig.conf

After a few seconds, the scan should finish and all found channels will been written into .

## Usage
Various players such as , , MPlayer or VLC media player should be able to open the previously created  to watch TV.
