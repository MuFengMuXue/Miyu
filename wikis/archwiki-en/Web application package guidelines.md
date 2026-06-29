# Web application package guidelines

This page describes how to package web applications.

## Separate user
For security reasons, every web application should be run as a separate (unprivileged) user (i.e. ).

Refer to the , ,  and  man pages for details on how to create users and deal with ownership of files and folders for that user in a package.

## Directory structure
The layout follows the FHS.

* : The application's data directory holds the files of the web application. Files are owned by  and are therefore readonly to the application user and group .
* : The configuration directory of the application holds configuration files for the application (symlinked to the data directory). Files located here have to go to the backup array and are owned by the user and group .

:

* : The runtime directory of the application (owned by the user and group ). It can be used for sockets (e.g. in setups facilitating socket activation).
:

* : The cache directory of the application (owned by the user and group ). It (or subfolders in it) is symlinked to the data directory for applications requiring writable cache directories.
* : The persistent storage of the application (owned by the user and group ). It (or subfolders in it) is symlinked to the data directory for applications requiring persistent storage directories.
