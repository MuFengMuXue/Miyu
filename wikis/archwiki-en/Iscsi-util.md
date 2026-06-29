# Iscsi-util

## Introduction
iscsi-util is a graphical user interface (GUI) for managing iSCSI sessions on Linux.
It is built with the cross‑platform Avalonia framework and provides a simple alternative to using  directly.
The project offers a portable AppImage as well as an AUR package.

## Features
* Target discovery.
* Session management (login/logout).
* CHAP authentication support.
* Session parameter configuration.
* Cross‑platform Avalonia-based interface.
* Portable AppImage with no external dependencies.
* Integration with .

## Installation
## From AUR
The package is available as :

## AppImage
The AppImage can be downloaded from the project’s release page:

* https://github.com/mijocecr/iscsi-util/releases

Make it executable:

## Dependencies
*  — required for iSCSI discovery, login, logout and session management.
*  — required when running the non‑AppImage packaged version.
*  — provides lsblk, blkid, mount, umount and other essential tools.
*  — required for desktop notifications.
*  — ext2/3/4 filesystem support.
*  — XFS filesystem support.
*  — Btrfs filesystem support.
*  — F2FS filesystem support.
*  — NTFS filesystem support.
*  — exFAT filesystem support.

## Usage
When launched, the application automatically detects existing configuration under .
The main operations include:

* Discovering targets:

* Logging in to a target.
* Logging out.
* Configuring CHAP authentication.
* Viewing active sessions.

The application acts as a visual layer on top of these operations.

## System integration
iscsi-util can configure iSCSI nodes so that they are automatically logged in at boot using the standard  mechanisms.
For details on how automatic login works, see:

* iSCSI
* Open-iSCSI#Automatic_login

## Troubleshooting
* Ensure the  service is running:

* Verify network connectivity to the target.
* Check logs:
