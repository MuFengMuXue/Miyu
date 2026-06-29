# Trash management

To prevent accidental deletion of files, you can use a trash can. To ensure compatibility between multiple applications, you can use software (CLI, GUI or Library) that follows the FreeDesktop.org's Trash specification.

## Tools
Most GUI file managers, such as GNOME Files and Dolphin, natively support moving files into the trash and managing its content.

Electron Applications need  to use the trash.

## Command line
*  provides a  command, see  in . The  package is required to fully support trash management, e.g. .
*  provides a  command that can be used as  to move  to the trash.
*
*
*
*
*
*
*
*

## Automatic cleaning
*
* Dolphin can automatically remove files older than a give number of days, and warn you or remove older or bigger files if the trash can goes above a size threshold. See official documentation.
* GNOME can automatically remove older files, see official documentation.
*

## Troubleshooting
## Unable to find or create trash directory
## External drives
 might not be set correctly. Note that  must be replaced by your own user id by .

Make sure that the root directory of the drive contains {{ic|~/.Trash-1000/{expunged,files,info} }} and set relevant read permissions for the directory and sub-directory.
