# XDG user directories

From freedesktop.org:
:xdg-user-dirs is a tool to help manage "well known" user directories like the desktop folder and the music folder. It also handles localization (i.e. translation) of the filenames.

:The way it works is that  is run very early in the login phase. This program reads a configuration file, and a set of default directories. It then creates localized versions of these directories in the user home directory and sets up a configuration file in  ( defaults to ) that applications can read to find these directories.

Most file managers indicate XDG user directories with special icons.

## Installation
Install .

## Creating default directories
Creating a full suite of localized default user directories within the  directory can be done automatically by running:

 $ xdg-user-dirs-update

When executed, it will also automatically:

* Create a local  configuration file: used by applications to find and use home directories specific to an account.
* Create a local  configuration file: used to set the language according to the locale in use.

The user service  will also be installed and enabled by default, in order to keep your directories up to date by running this command at the beginning of each login session.

## Creating custom directories
Both the local  and global  configuration files use the following environmental variable format to point to user directories:  An example configuration file may likely look like this (these are all the template directories):

As  will source the local configuration file to point to the appropriate user directories, it is therefore possible to specify custom folders.  For example, if a custom folder for the  variable has named  in  any application that uses this variable will use this directory.

Alternatively, it is also possible to specify custom folders using the command line.  For example, the following command will produce the same results as the above configuration file edit:

 $ xdg-user-dirs-update --set DOWNLOAD ~/Internet

## Querying configured directories
Once set, any user directory can be viewed with . For example, the following command will show the location of the  directory, which of course corresponds to the  variable in the local configuration file:

 $ xdg-user-dir TEMPLATES

{{warning| should not receive its argument from unchecked input, since it simply passes it to  without performing any sanity checks, in a line that looks like this:

 eval echo \${XDG_${1}_DIR:-$HOME}

This means that  facilitates arbitrary code execution from unsanitized input. Unless this unsafe implementation is fixed upstream,  should only ever be used with a hard-coded or strictly audited argument.}}
