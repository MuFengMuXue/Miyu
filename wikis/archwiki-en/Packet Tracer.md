# Packet Tracer

Packet Tracer is a cross-platform visual network simulation tool for Cisco hardware on the CCNA level and can be used to prepare for the Cisco CCNA certification exam.

Packet Tracer is an integral part of the Cisco Networking Academy, and provides authoring, assessment, and collaboration capabilities.

## Installation
## Download source package tarball
 can not be installed using automated methods (e.g. AUR helper) because the software's tarball must be downloaded first before building the package.

So, first acquire the build files for  package.

## Download Packet Tracer deb package
* Log into Cisco Networking Academy (Skills For All / NetAcad) using your Cisco Account. Register an account if you do not have it.
* Once in the Networking Academy portal, download Cisco Packet Tracer 9.0.0.
* Place the .deb file inside the folder where 's build files are located — that is the same folder where the PKGBUILD file is found.

## Build and install
* Build the package; alternatively, build in a clean chroot.
* Install the package.

## Usage
The installation process will put a AppImage executable file as .

Please note that there will be no desktop file right after the installation. Packet Tracer will require a first run to accept the UELA via the command line:

 $ /usr/lib/packettracer/packettracer.AppImage

then you can find a desktop file or keep running it via the AppImage as above.

Executing packettracer requires FUSE for execution.

## Troubleshooting
## Crashes under Wayland
If Packet Tracer crashes when started in a Wayland session, try running it with the  environment variable set to . See Wayland#Qt for more details.

## Wrong UI Size
If Packet Tracer's UI is rendered incorrectly, try modifying the  environment variable, and then either reboot or logout.
