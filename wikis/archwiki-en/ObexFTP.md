# ObexFTP

ObexFTP implements the OBEX protocol, used to transfer files. OBEX was adopted by the organization overseeing the Bluetooth standards and Android supports it since version 2.1.

## Installation
Install the  package.

For a Tcl/Tk front-end install .

## Usage
## Obex Object Push
To send a file, find out the channel of the OBEX Push service:

 $ sdptool search --bdaddr MAC_address OPUSH

Then send the file to that channel using the following command from http://dev.zuckschwerdt.org/openobex/wiki/ObexFtpExamples/#Obex-PUSH-over-Bluetooth:

 $ obexftp --nopath --noconn --uuid none --bluetooth MAC_address --channel channel --put file

## ObexFTP
If your device supports the Obex FTP service but you do not wish to mount the device you can transfer files to and from the device using the obexftp command.

To send a file to a device run the command:

 $ obexftp -b MAC_address -p /path/to/file

To retrieve a file from a device run the command:

 $ obexftp -b MAC_address -g filename

## ObexFS
Another option, rather than using KDE or Gnome Bluetooth packages, is ObexFS which allows for the mounting of phones which are treated like any other filesystem.

Mount supported phones by running:

 $ obexfs -b MAC_address mountpoint

Once you have finished, to unmount the device use the command:

 $ fusermount -u mountpoint

For more mounting options see http://dev.zuckschwerdt.org/openobex/wiki/ObexFs
