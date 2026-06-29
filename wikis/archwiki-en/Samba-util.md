# Samba-util

## samba-util
## Introduction
samba-util is a graphical user interface (GUI) for managing Samba configuration on Linux systems.
It provides a visual front‑end for editing , managing Samba users and inspecting service status.
The application is built with the cross‑platform Avalonia framework and is available as both an AppImage and an AUR package.

## Features
* Graphical editor for .
* Creation, modification and removal of Samba shares.
* Management of Samba users through .
* Validation of filesystem permissions for shared directories.
* Service status inspection for  and .
* Log viewer for Samba‑related journal entries.
* Cross‑platform Avalonia‑based interface.

## Installation
## From AUR
The package is available as :

## AppImage
The AppImage can be downloaded from the project’s release page:

* https://github.com/mijocecr/samba-util/releases

Make it executable:

## Dependencies
The following packages are required for full functionality:

*  — provides , ,  and user management tools.
*  — provides , , , .
*  — desktop notifications.
*  — service management.

Optional dependencies:

*  — SMB integration in graphical file managers.
*  — mDNS name resolution.
*  — mDNS/zeroconf service discovery.

## Usage
When launched, the application reads the system configuration from .
The interface provides access to:

* Editing global and per‑share configuration.
* Creating and removing Samba shares.
* Managing Samba users:

* Inspecting the status of  and .
* Viewing logs related to Samba services.

Changes to  can be validated using .

## System integration
samba-util interacts with the standard  mechanisms for configuration and service control.
For details on Samba configuration, see:

* Samba
* Samba/Tips and tricks
* Samba/Configuring

## Troubleshooting
Issues encountered while using the application generally correspond to underlying Samba configuration or filesystem permissions.
Refer to:

*  for configuration validation.
*  for service logs.
* Samba for detailed configuration guidance.
