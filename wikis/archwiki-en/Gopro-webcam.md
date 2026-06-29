# Gopro-webcam

Currently there is no official support for using your GoPro 8 and 9 (the only versions that offer this feature natively) as a webcam on Linux. The web is full of incomplete tutorials for this topic. This page tries to simplify this effort.

## Installation
Install the  package.

## Usage
The following command starts the tool in the interactive mode and tries to identify the GoPro's device, find the interface and ultimately start the webcam mode:

 # gopro webcam

There are a couple of options you can also set. See the  option.

## Examples
Start the webcam at a resolution of 1080p and with the linear FOV and start FFmpeg to expose the device to the OS:

 # gopro webcam -a -r 1080 -f linear

Find a device that matches the pattern  and starts the webcam mode without asking for user input (it also starts  to expose the device to the OS):

 # gopro webcam -p enx -n -a

Use the provided device  and do not ask for user input (just start VLC to preview the output you will get from the Camera):

 # gopro webcam -d enxenx9245589250e7 -n -v

Use the provided IP  and automatically start  to expose the device to the OS (and do not ask for user input):

 # gopro webcam -i 172.27.187.52 -a -n

## Start on boot
In order to start the webcam on boot, enable .

If you would like to change the start parameters, edit .

## Start on plug in
gopro-webcam comes with a udev rule that will automatically start the  service when a GoPro Hero9 is plugged in, which may be undesirable to some users. The udev rule can be disabled as follows:

 # ln -s /dev/null /etc/udev/rules.d/60-gopro.rules

To have the udev rule work with a GoPro Hero8 Black instead, change  in  to .

## Troubleshooting
## Cannot find network device for GoPro
Double check that the USB connection mode is GoPro Connect and not MTP under Preferences > Connections > USB Connection. If that option does not exist, you likely need a firmware upgrade. Instructions can be found at https://gopro.com/en/us/update.
