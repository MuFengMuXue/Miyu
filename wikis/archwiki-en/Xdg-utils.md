# Xdg-utils

xdg-utils provides the official utilities for managing XDG MIME Applications.

*  - Install desktop menu items
*  - copies desktop entries to the user's desktop
*  - Compose a new email in the user's preferred email client, potentially with subject and other info filled in
*  - Install icon resources
*  - Query and install MIME types and associations
*  - Open a file or URI in the user's preferred application
*  - Enable, disable, or suspend the screensaver
*  - Get or set the default web browser and URL handlers

## Installation
Install the  package.

## Usage
## Environment variables
xdg-utils attempts to integrate with your desktop environment by invoking the specialized programs it provides, where applicable. The evaluation of the current environment is as follows * If the standardized XDG_CURRENT_DESKTOP environment variable is set to a recognized desktop environment, the corresponding value is used.
* If any classic fallbacks or environment-specific variables, such as KDE's , are present, then the corresponding value is used.
* If the legacy DESKTOP_SESSION environment variable is set to a recognized desktop environment, the corresponding value is used.

During this process, if any match is found, the DE variable is internally overwritten with the detected desktop environment's normalized value. Hence,  is both a legacy environment variable, and an internal state variable for xdg-utils. As an example, if  is , xdg-utils will internally set  to . If no match is found, then any pre-existing  value will be used, in such a way that  is equivalent to  being unset, and having . This implementation detail is worth noting because it has the consequence that a pre-set  is ignored if a desktop environment is otherwise detected.

Values of the variables that xdg-utils recognizes are:
{| class="wikitable"
! Desktop Environment !!  !!  !!
|-
|  || 1 ||  ||
|-
| Cinnamon || ,  ||  ||
|-
| Deepin || , , 1 ||  ||
|-
| Enlightenment || 1||  ||
|-
| GNOME || 2 ||  ||
|-
| GNOME Flashback || , 2 ||  ||
|-
| KDE Plasma ||  ||  ||
|-
| LXDE ||  ||  ||
|-
| LXQt ||  ||  ||
|-
| MATE ||  ||  ||
|-
| Xfce ||  ||  || , ,
|}

# This is not an environment [https://specifications.freedesktop.org/menu-spec/latest/onlyshowin-registry.html registered with freedesktop.org.
# GNOME variations, including the GNOME Classic mode, are all regarded as the same by xdg-utils.

Note that this is only a list of what the scripts provided by  are capable of detecting. The scripts will still perform generic, environment-agnostic actions under the following conditions:
* The generic routine was asked for, via  or .
* Environment detection failed. All relevant environment variables were unrecognized or unset, and the classic fallbacks did not reveal anything.
* Environment-specific actions were performed, but failed, e.g. due to a missing program.

## xdg-mime
 is a script for directly querying and modifying default MIME applications. It is used within other scripts, such as xdg-open, and is also a useful troubleshooting tool.

Determine a file's MIME type:

Determine the default application for a MIME type:

Change the default application for a MIME type:
 $ xdg-mime default feh.desktop image/jpeg

To set a file manager as the default file manager (for ex -Thunar) type:
 $ xdg-mime default thunar.desktop inode/directory

Debug default application for MIME type:

When it is necessary to determine the MIME type of a file, xdg-mime attempts to use the right program for the desktop environment:
{| class="wikitable"
! Desktop Environment !! Program !! Package
|-
| Cinnamon
|rowspan="6"|
|rowspan="6"|
|-
| GNOME
|-
| GNOME Flashback
|-
| LXDE
|-
| MATE
|-
| Xfce
|-
| Deepin
|rowspan="3"
|rowspan="3"
|-
| Enlightenment
|-
| LXQt
|-
| KDE Plasma ||  ||
|-
|}

In the generic case, xdg-mime will:
* Delegate to mimetype if present. Requires the  package to be installed.
* Delegate to  if present.

## xdg-open
 is a resource opener used by many applications, implementing the XDG MIME Applications standard while integrating with the system's desktop environment as much as possible.

If a desktop environment was detected, its provided handler will be invoked https://gitlab.freedesktop.org/xdg/xdg-utils/-/blob/master/scripts/xdg-open.in:
{| class="wikitable"
! Desktop Environment !! Program !! Package
|-
| Cinnamon
|rowspan="4"|
|rowspan="4"|
|-
| GNOME
|-
| GNOME Flashback
|-
| MATE
|-
| Deepin ||  ||
|-
| Enlightenment ||  ||
|-
| KDE Plasma || 1 ||
|-
| LXDE ||  ||
|-
| LXQt ||  ||
|-
| Xfce || 2 ||
|}

# If  is unset, then  from  will be used instead. KDE Plasma should set this variable under any condition, though.
#  from  will also be tried.

In the generic case, xdg-open will:
* Query #xdg-mime for the default desktop entry associated with the resource, parse the desktop entry, and execute its command.
* Delegate to run-mailcap if present. Requires the  package to be installed.
* Delegate to mimeopen if present. Requires the  package to be installed.

Since xdg-mime relies on  package to implement the XDG MIME Applications standard, if you are not using a desktop environment, you should either install , or consider a different resource opener.

## xdg-settings
See .

Shortcut to open all web MIME types with a single application:
 $ xdg-settings set default-web-browser firefox.desktop

Shortcut for setting the default application for a URL scheme:
 $ xdg-settings set default-url-scheme-handler irc xchat.desktop

## Tips and tricks
## URL scheme handlers
To set the default application for a URL scheme you may also need to change the default application for the  MIME types:

 $ xdg-mime default firefox.desktop x-scheme-handler/https x-scheme-handler/http
