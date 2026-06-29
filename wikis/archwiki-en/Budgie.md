# Budgie

Budgie is a desktop environment, formerly a project within Solus, becoming independent under the newly formed Buddies of Budgie organization in January 2022. It uses GTK for widgets, and is written in C and Vala. As of Budgie 10.10, a huge leap to Wayland was made and Xorg support was instantaneously dropped.

## Installation
Install the  package group to install all first-party components of the desktop. The individual  package. Installed alongside as runtime dependencies are  for display configuration, and  for modification of system settings. The following packages are optional, but add additional functionality to the desktop:

* : Official implementation of desktop icons
* : Network management from within the panel
* : Bluetooth support

Extra applets developed by the Ubuntu Budgie team are available in the  package - be warned, however, that this package also modifies existing functionality and could cause issues.

## Configuring user directories
Follow the XDG user directories instructions to create the "well known" user directories like Desktop, Downloads, etc. Logout and log back in for the Budgie menu to detect changes to the configuration.

## File manager
Budgie does not come with a file manager, and one is not installed by default. GNOME/Files (previously Nautilus) works well, and others are available.

## Starting
Choose Budgie Desktop session from a display manager of choice, or modify xinitrc to include Budgie Desktop:

## Usage
You can see your notification backlog, set the system and application volume, view a calendar, and see any currently playing videos or music with the "Raven" sidebar. The "Notifications" section can be accessed quickly with  or by clicking on the Notifications applet in the panel, and the "Applets" section can be accessed quickly with . Raven can also be opened by clicking on the "Raven Trigger" applet in the panel, and will be opened to the previously selected pane.

## Theming
Budgie uses GTK for its UI elements, and is thus supported by many GTK themes. Budgie also ships a built-in theme that is only applied to its own elements, such as panels and Raven, which can be toggled in Budgie Desktop Settings.  Icon themes and cursor themes can be set in Budgie Desktop Settings as well.

## Customizing themes
Customizing GTK themes requires to build them from source. Each theme will have documentation on how to do so. For example, the Materia theme code can be found in their repository.

## Forking Materia
Materia comes with hacking and installation instructions. If the theme is already installed from the  package, it is recommended to rename the forked version just in case an edit breaks the UI:

## Making UI changes
The theme is written with Sass. For example, to make all windows have a square border (instead of rounded), change the  variable:

## Building and installing
The Sass compiler and the Meson builder are required. Both can be installed from  and  packages. The theme can be built and installed with:

 meson _build
 meson install -C _build

Once installed, the theme can be activated from Budge Desktop Settings.

## Configuration
Configuration of Budgie Desktop is done through the built-in Budgie Desktop Settings application, and changes to system settings are made through .

## Changing button layout
Window button layout can be changed using ,  or gsettings.

For example:

 $ gsettings set com.solus-project.budgie-wm button-layout 'close,minimize,maximize:appmenu'
 $ gsettings set com.solus-project.budgie-helper.workarounds fix-button-layout 'close,minimize,maximize:menu'

## Use a different window manager
Budgie does not support using a different window manager.
