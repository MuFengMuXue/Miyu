# Dm-integrity

The dm-integrity kernel device mapper target provides an additional layer with per-sector integrity information. In standalone mode it supports CRC (CRC-32, CRC-32C) or hash functions (xxHash64, SHA-1, SHA-256). It can also be used with dm-crypt to provide authenticated disk encryption with HMAC-SHA256. It uses journaling for guaranteeing write atomicity by default, which effectively halves the write speed.

## Usage
The main utility for standalone management is integritysetup, included in the  package. The dm-integrity layer can also be activated and managed with the
cryptsetup utility or with LVM. This section covers management in standalone mode.

## Format
The underlying device/partition/volume has to be formatted and the initial integrity metadata written, which takes some time. The integrity algorithm  can be one of , , ,  or .

 # integritysetup format -v --integrity algo /dev/device

## Open
A dm-integrity-protected volume is opened with:

 # integritysetup open -v --integrity algo /dev/device volname

Afterwards the volume can be accessed through .

## Close
After all contained filesystems are unmounted the volume is closed with:

 # integritysetup close -v volname

## /etc/integritytab
The  file can be set up to open specific volumes at system boot. See .
