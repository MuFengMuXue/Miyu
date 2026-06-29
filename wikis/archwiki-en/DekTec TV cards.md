# DekTec TV cards

DekTec is a manufacturer of PC add-on cards, USB devices, IP converters and software for the professional digital-television market. Products are used for test and measurement, to build broadcast infrastructure or as OEM component integrated in your PC-based product.

## Installation
Install the  DKMS drivers for full support of all DekTec PC add-on cards.

Make sure to reboot the PC to load the newly installed dkms drivers.

## Check if drivers are installed and detected
To check if dkms drivers are installed, type:

 $ dkms status

To check if DekTec PCI/PCIe add-on card is detected, type:

 $ lspci -k | grep DekTec

To check if DekTec USB add-on card is detected (requires ), type:

 $ lsusb -t | grep DekTec

If  is installed, it is possible to list all type of DekTec add-on cards with:

 $ tsdektec -a

## Demodulator boards DtapiService daemon
The DtapiService is a Linux daemon that manages DekTec's range of demodulator boards. The following demodulators are supported:

;DTU-234: VSB/QAM-B receiver for USB
;DTU-235: DVB-T measurement receiver for USB
;DTU-236: QAM measurement receiver + ASI input for USB
;DTA-2131: Multi-standard VHF/UHF demodulator for PCI Express
;DTA-2135: Dual DVB-T receiver for PCI Express
;DTA-2136: Dual QAM-A/B/C receiver for PCI Express
;DTA-2137: Dual DVB-S/DVB-S2 receiver for PCI Express
;DTA-2138: DVB C2/T2 receiver for PCI Express
;DTA-2139: Twelve-channel QAM Receiver for PCI Express

Install the  and start/enable .

## Example usage
All mainstream DekTec Applications require a license and is exclusively developed for use on Microsoft Windows. A license can be purchased from DekTec or one of its distributors. There are also free utilities, such as  which can be installed with .

## Linux SDK solution
Linux SDK – SDK for DTA, DTU and DTE products provides developers with a driver and an API for using DekTec's
DVB/MPEG-2 PCI/PCIe and USB-2 devices in applications running under Linux.
All drivers are free to use except for DTAPITS and DtapiService.bin (self-extracting binary installer for DtapiService) which requires a license.

## SDK Examples
Install the  package.

AvFifo code examples for Linux, demonstrating the usage of the AvFifo API for receiving and transmitting SMPTE 2110 streams.

## External toolkits
Using TSDuck the MPEG Transport Stream Toolkit. TSDuck can be installed with  or . It is an extensible toolkit for MPEG transport streams and can be used in digital television systems for test, monitoring, integration, debug, lab, demo. With this tool, the development possibilities are essentially endless.

## FFmpeg Integration
Install the  package.

Unlock the power of FFmpeg for real-time streaming of SDI or SMPTE 2110 via DekTec devices. DekTec device support to the  and  command-line utilities, the FFmpeg libraries for custom application development and the new  file format for storage of raw SDI streams has been introduced since September 2023.
