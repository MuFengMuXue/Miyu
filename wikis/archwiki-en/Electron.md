# Electron

Electron is an application developed by GitHub to build cross platform desktop apps using web technologies. They are rendered using the Chromium browser engine and back end is using the Node.js runtime environment.

## Installation
Install the  package for the latest version.

Some applications require older electron versions. You can install previous versions in parallel with latest. The corresponding packages are suffixed with version number, for example .

## Tips and tricks
## Configuration files
The  command reads command-line flags from  files, where XX is the Electron version, or falls back to  if the former is not present. ( defaults to  if not set.)

Lines starting with a hash  are treated as comments and ignored, but other lines are passed as CLI arguments to the actual Electron binary, one per line (lines are not split on whitespace!), before the options passed to the  command itself.

This can be useful, for example, to #Enable Wayland globally.

Example:

## Determine the version of Electron an application uses
If installed through your package manager, you can query the package's dependencies to see if it depends on e.g. , meaning it uses Electron 38.
(If it depends on : this package is designed to always provide the latest version of Electron; to learn which version this currently is, query that package's dependencies.)

It is also possible to determine the version of Electron from a running application by using its developer tools; see === Secret Service API ===

Electron provides the [https://www.electronjs.org/docs/latest/api/safe-storage#safestoragegetselectedstoragebackend-linux safestorage API to interact with a keyring compatible with the FreeDesktop.org's Secret Service API. Example of supported keyrings are GNOME/Keyring through GNOME libsecret, KDE Wallet and KeePass.

The backend can be chosen on the command-line with the  flag when running an Electron application. As an example, running  (built with Electron) to interact with  or KeePass:

 $ electron-desktop --password-store="gnome-libsecret"

## Turn any website to application
Sometimes you need to use a specific web site, but use it as an application. With  you can turn any website to an electron application.

## Enable Wayland
See Wayland#Electron.

## Troubleshooting
Since Electron is based on Chromium, Chromium#Troubleshooting may help
