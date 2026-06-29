# Ventoy

Ventoy is a free and open source tool to create drives that allow you to select and boot any EFI, IMG, ISO, VHD(x), or WIM files stored on a rewritable partition on the drive.

Most types of operating systems are supported (Windows/WinPE/Linux/ChromeOS/Unix/VMware/Xen...), see the full list.

## Installation
Install the  package.

## Known issues
Ventoy might contain backdoors or other malicious code:

* The author(s?) long refused to react on questions about the source code for the precompiled code inside their git repository.
* They long refused to react on questions about the security risks.
* When an answer was finally given, it boiled down to a simple "There is no reason to assume that we would have placed malware inside."
* Again after a really long time the authors finally mentioned what other source code they used to generate some−but not all−of the pre-compiled code. They did not mention the build methods and refused to prove that this really was the used source code.
* The real identities of the authors is unknown.

See Wikipedia:Ventoy#Concerns over software security and validity of open source claim for more information.

For alternatives, take a look at the Multiboot USB drive#Automated tools.

## Usage
There are three utilities for setting up the media:

# , which is a shell script to be run from the command line.
# , which is a graphical application.  or a similar application is needed to escalate to root if the application is not started with root permissions.
# Opening  with a web browser.

The same utilities can be used for upgrading the Ventoy installation on the drive.

Ventoy creates two partitions on the drive. Their default names are Ventoy and VTOYEFI. The Ventoy partition is to store the bootable images (iso files), and any other data. VTOYEFI is for the Ventoy binaries.

To add images from which you can boot, mount the first partition and copy the images over.

## Use without installing
If you just want to create a multi-boot drive, you can simply download the pre-built executable at the GitHub releases page. You need  to be installed because a vfat partition is created by using mkfs.vfat. After verifying the sha256sum and unpacking, you can display the included CLI'shelp page by running the shell script without any arguments:

 # ./ventoy-VERSION/Ventoy2Disk.sh

You can afterwards upgrade the drive for future versions by following a similar procedure. Downloading a NEWER-VERSION, verifying the sha256sum, unpacking, running

 # ./ventoy-NEWER-VERSION/Ventoy2Disk.sh

and following the on screen help message.

As an alternative to the shell script mentioned here, a GTK/qt[https://www.ventoy.net/en/doc_linux_gui.html, and a webUIare also included.

## Tips and tricks
## What version is already installed?
With  utility mentioned earlier, start, and do not approve, an upgrade process (). It will inform from which version it intends to upgrade, before asking for confirmation.

## Checking files integrity
As described in [https://www.ventoy.net/en/doc_checksum.html upstream documentation, a built-in checksum utility allows verification of the integrity of the files on the disk.
