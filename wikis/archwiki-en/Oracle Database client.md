# Oracle Database client

This document will explain how to install the Oracle database client under Arch Linux. The client is used to connect to Oracle databases running on other machines.

## Installation
Due to the way Oracle provides downloads of their software, the files cannot be retrieved automatically. You must download the necessary .zip files manually and place them in the same directory as the PKGBUILD from AUR, before running . You will need an Oracle account before you can log in and download the .zip files.

## Relevant packages
The packages to be installed from the AUR are:

*  - core Oracle client, required by all the other packages and any precompiled binaries using the native Oracle API
*  - C header files, required to compile software that accesses Oracle using the native API
*  - SQL*Plus command line utility
*  - UnixODBC connectivity
*  - Java connectivity
*  - Data Pump, SQL*Loader and Workload Replay Client

## Installation paths
When using the packages in the AUR, the TNSNAMES file should be saved as .  should be set automatically to  in any new shells opened after the install, courtesy of .

## gqlplus
After installing sqlplus, you might also want to install , a frontend to sqlplus that adds command history and tab completion.
