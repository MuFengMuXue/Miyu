# Scripts / Desc / Xdg Settings

2009-2011

Mike

Mammarella

mdm@google.com

xdg-utils 1.1.0

xdg-settings

1

xdg-settings

get various settings from the desktop environment

xdg-settings

get

check

set

property

subproperty

value

xdg-settings

verb

default-web-browser

desktop-file.desktop

xdg-settings

verb

default-url-scheme-handler

scheme

desktop-file.desktop

xdg-settings

--help

--list

--manual

--version

# Description

xdg-settings gets various settings from the desktop environment. For instance, desktop environments often provide proxy configuration and default web browser settings. Using xdg-settings these parameters can be extracted for use by applications that do not use the desktop environment's libraries (which would use the settings natively).

xdg-settings is for use inside a desktop session only. It is not recommended to use xdg-settings as root.

# Verbs

get
Query the value of the given property and subproperty.

check
Test wheter the given value equals the value of the given property and subproperty. Returns `yes` or `no` on stdout. If this depends on multiple settings this may seem to conflict with the output of `get`.

set
Set the property and subproperty to the given value.

# Options

`--help`
Show command synopsis.

`--list`
List all properties xdg-settings knows about.

`--manual`
Show this manual page.

`--version`
Show the xdg-utils version information.

# Properties

When using xdg-settings to get, check or set a desktop setting, properties and possibly sub-properties are used to specify the setting to be changed.

Some properties (such as default-web-browser) fully describe the setting to be changed. Other properties (such as default-url-scheme-handler) require more information (in this case the actual scheme to set the default handler for) which must be provided in a sub-property.

# Exit Codes

An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned:

`1`
Error in command line syntax.

`2`
One of the files passed on the command line did not exist.

`3`
A required tool could not be found.

`4`
The action failed.

# See Also

`xdg-mime(1)`, `xdg-open(1)`, `xdg-utils-common(7)`, [MIME applications associations specification](http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/)

# Examples

Get the desktop file name of the current default web browser

            xdg-settings get default-web-browser


Check whether the default web browser is firefox.desktop, which can be false even if "get default-web-browser" says that is the current value (if only some of the underlying settings actually reflect that value)

            xdg-settings check default-web-browser firefox.desktop


Set the default web browser to google-chrome.desktop

            xdg-settings set default-web-browser google-chrome.desktop


Set the default mailto URL scheme handler to be evolution.desktop

            xdg-settings set default-url-scheme-handler mailto evolution.desktop
