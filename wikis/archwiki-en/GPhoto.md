# GPhoto

Libgphoto2 is the core library designed to allow access to digital cameras by external (front-end) programs, such as digiKam and gPhoto2. List of officially supported cameras is available on the official website (though more may work).

This article documents the configuration of  to access digital cameras. Some digital cameras will mount as normal USB storage devices and may not require the use of libgphoto2.

## Installation
Install the  package, and optionally  to have a command line interface.

## Mount
*
*
*

## Frontend applications
*
*
*
*
*
*
*
*
*

## GPhoto2 usage
GPhoto2 is a command line client for libgphoto2. GPhoto2 allows access to the libgphoto2 library from a terminal or from a script shell to perform any camera operation that can be done. This is the main user interface.

GPhoto2 also provides convenient debugging features for camera driver developers.

Quick Commands
*
*
*
*
*
*
*
*  - sets the camera to the current time

For advanced file manipulation, use
*

## Example usage with GVfs
Auto detect the connected camera and list the required port:

Now open your favorite file manager and enter the address with the found port detail . File manager functionality#Mounting will use  to get the camera mounted and manageable with the file manager.

## Troubleshooting
## Permission issues
Users with a local session have permissions granted for cameras using ACLs. See General troubleshooting#Session permissions if it does not work.

## Claimed device
Your system might automatically mount the camera as a file system and then some gphoto2 commands output the error message "cannot claim device". In this case unmount the camera using your file browser or run:

 $ gio mount -s gphoto2
