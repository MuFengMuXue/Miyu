# Flatpak

From the project README:

:Flatpak is a system for building, distributing and running sandboxed desktop applications on Linux.

From :

:Flatpak is a tool for managing applications and the runtimes they use. In the Flatpak model, applications can be built and distributed independently from the host system they are used on, and they are isolated from the host system ('sandboxed') to some degree, at runtime.
:Flatpak uses OSTree to distribute and deploy data. The repositories it uses are OSTree repositories and can be manipulated with the ostree utility. Installed runtimes and applications are OSTree checkouts.

## Installation
Install the  package. If you want to build Flatpaks, install  too.

To complete setup, restart your system, see link

## Desktop integration
For Flatpak applications to interact with your desktop (i.e. allow applications to open URLs, share your screen and more), make sure to set up the xdg-desktop-portal. Depending on the implementation for your desktop, there is a confirmation dialog before the application is able to access some portals.

## Application management
*
*
*

## Permission management
*
*
*

## Managing repositories
See also Basic commands.

## Add a repository
To add a remote Flatpak repository do:

 $ flatpak remote-add name location

where name is the name for the new remote, and location is the path or URL for the repository.

The installation of Flatpak will, by default, add the official Flathub repository as a system-wide installation. To add the official repository with a per-user configuration:

 $ flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo

## Delete a repository
To delete a remote Flatpak repository do:

 $ flatpak remote-delete name

where name is the name of the remote repository to be deleted.

## List repositories
To list all the added repositories do:

 $ flatpak remotes

## Set repository priorities
To change the default priority of Flathub repo to 3:

 $ flatpak remote-modify --prio=3 flathub

## Change the repository subset
To select verified subset of Flathub repo:

 $ flatpak remote-modify --subset=verified flathub

Refer to the documentation for the desired Flatpak repository to find the available subsets and their descriptions.

## Managing runtimes and applications
## Search for a remote runtime or application
You can proceed to search for a package with , e.g. to look for the package  with the  remote configured:

## List all available runtimes and applications
To list all available runtimes and applications in a remote repository named remote do:

 $ flatpak remote-ls remote

## Install a runtime or application
To install a runtime or application do:

 $ flatpak install remote name

where remote is the name of the remote repository, and name is the name of the application or runtime to install.

To install an application from a .flatpak file do:

 $ flatpak install name.flatpak

## List installed runtimes and applications
To list installed runtimes and applications do:

 $ flatpak list

## Run applications
Binaries are available in , which is automatically added to $PATH by . You may have to re-login to apply the change.

Flatpak applications can also be run with the command line:

 $ flatpak run name

## Update a runtime or application
List runtimes and applications that have updates available:

 $ flatpak remote-ls --updates

To update a runtime or application named name do:

 $ flatpak update name

To update all applications and runtimes:

 $ flatpak update

## Automatic updates via systemd
To update your system runtimes and applications automatically, create the following files:

Afterwards, do a daemon-reload and enable/start the  unit.

## Uninstall a runtime or application
To uninstall a runtime or application named name do:

 $ flatpak uninstall name

To delete app data from  and from the permission store while uninstalling, use:

 $ flatpak uninstall --delete-data name

## Downgrade a runtime or application
To downgrade a runtime or application, first look for the associated commit ID:

 $ flatpak remote-info --log remote name

Where remote is the repository (such as ), and name is the name of the application or runtime. Then, deploy the commit:

 $ flatpak update --commit=commit name

where commit is the commit for the desired version, and name is as before.

This procedure can also be used to selectively upgrade a package to a desired version that is not the latest version.

To exclude  from updating this package, see #Prevent updates to a runtime or application.

## Prevent updates to a runtime or application
To prevent automatic and manual updates to a runtime or application, use the  command:

 $ flatpak mask name

This also prevents selective upgrades and downgrades.

To reverse the mask and re-enable updates, use :

 $ flatpak mask --remove name

## Add Flatpak .desktop files to your menu
Flatpak expects window managers to respect the XDG_DATA_DIRS environment variable to discover applications. This variable is set by the script . Updating the environment may require restarting the session. If the launcher does not support , you can edit the list of directories scanned and add these to it:

 ~/.local/share/flatpak/exports/share/applications
 /var/lib/flatpak/exports/share/applications

This is known to be necessary in Awesome.

## View sandbox permissions of application
Flatpak applications come with predefined sandbox rules which define the resources and file system paths the application is allowed to access.
To view the specific application permissions do:

 $ flatpak info --show-permissions name

The reference of the sandbox permission names can be found on official Flatpak documentation.

## Override sandbox permissions of applications
If you find the predefined permissions of the application too lax or too restrictive you can change to anything you want using  command.
For example:

 $ flatpak override --nofilesystem=home name

This will prevent the application access to your home folder.

Every type of permission, such as device, filesystem or socket, has a command line option that allows that particular permission and a separate option that denies permission. For example, in case of device access  allows access,  denies the permission to access device.

For all permission types commands consult the manual page:

Permission overrides can be reset to defaults with command:

 $ flatpak override --reset name

Flatseal is a GUI permissions manager which offers simple point-and-click permissions operations. In KDE Plasma, Flatpak Permissions Management KCM provides a similar GUI for the system settings application: System Settings > Applications > Flatpak Permission Settings.

## Creating a custom base runtime
You can create a custom Arch-based base runtime and base SDK for Flatpak using pacman. You can then use it for building and packaging applications. This is an alternative for personal use to the default  and  runtimes.

In addition to , you need to have installed  and for pacman hooks support also .

First, start by creating a directory for building the runtime and possibly applications.

 $ mkdir myflatpakbuilddir
 $ cd myflatpakbuilddir

You can then prepare a directory for building the runtime base platform. The files subdirectory will contain what will later be the  directory in the sandbox. Therefore you will need to create symbolic links so the default  etc. from Arch can still be accessed at the usual path.

 $ mkdir -p myruntime/files/var/lib/pacman
 $ touch myruntime/files/.ref
 $ ln -s /usr/usr/share myruntime/files/share
 $ ln -s /usr/usr/include myruntime/files/include
 $ ln -s /usr/usr/local myruntime/files/local

Make your host OS fonts available to the Arch runtime:

 $ mkdir -p myruntime/files/usr/share/fonts
 $ ln -s /run/host/fonts myruntime/files/usr/share/fonts/flatpakhostfonts

You need and may want to adapt your  before installing packages to the runtime. Copy  to your build directory and then make the following changes:

* Remove the  option so pacman will not complain about errors finding the root filesystem for checking disk space.
* Remove any undesired custom repositories and , ,  and  settings that are needed only for the host system.

Now install the packages for the runtime.

 $ fakechroot fakeroot pacman -Syu --root myruntime/files --dbpath myruntime/files/var/lib/pacman --config pacman.conf base
 $ mv pacman.conf myruntime/files/etc/pacman.conf

Set up the locales to be used by editing . Then regenerate the runtime’s locales.

 $ fakechroot chroot myruntime/files locale-gen

The base SDK can be created from the base runtime with added applications needed for building packages and running pacman.

 $ cp -r myruntime mysdk
 $ fakechroot fakeroot pacman -S --root mysdk/files --dbpath mysdk/files/var/lib/pacman --config mysdk/files/etc/pacman.conf base-devel fakeroot fakechroot --needed

Insert metadata about runtime and SDK.

Add base runtime and SDK to a local repository in the current directory. You may want to give them appropriate commit messages such as “My Arch base runtime” and “My Arch base SDK”.

 $ ostree init --mode archive-z2 --repo=.
 $ EDITOR="nano -w" ostree commit -b runtime/org.mydomain.BasePlatform/x86_64/2016-06-26 --tree=dir=myruntime
 $ EDITOR="nano -w" ostree commit -b runtime/org.mydomain.BaseSdk/x86_64/2016-06-26 --tree=dir=mysdk
 $ ostree summary -u

Install the runtime and SDK.

 $ flatpak remote-add --user --no-gpg-verify myarchos file://$(pwd)
 $ flatpak install --user myarchos org.mydomain.BasePlatform 2016-06-26
 $ flatpak install --user myarchos org.mydomain.BaseSdk 2016-06-26

## Creating apps with pacman
As an alternative to building applications the usual way, we can use pacman to create a containerized version of the regular Arch packages. Note that  is read-only when creating apps, so we can not use Arch’s packages when building an app. To create a real app with pacman, we can either

* use pacman to create a runtime containing all dependencies
* and compile the app ourselves as usual or perhaps using pacman with a custom PKGBUILD tailored to Flatpak which uses  for the  script,

or we can
* use pacman to create a runtime containing the app installed with pacman
* and create a dummy app to launch it.

For doing the latter, first create a runtime using pacman such as this one for . The runtime is first initialized and prepared for use with pacman.

 $ flatpak build-init -w geditruntime org.mydomain.geditruntime org.mydomain.BaseSdk org.mydomain.BasePlatform 2016-06-26
 $ flatpak build geditruntime sed -i "s/^#Server/Server/g" /etc/pacman.d/mirrorlist
 $ flatpak build geditruntime ln -s /usr/var/lib /var/lib
 $ flatpak build geditruntime fakeroot pacman-key --init
 $ flatpak build geditruntime fakeroot pacman-key --populate

Then the package is installed. The host’s network connection must be made available to pacman.

 $ flatpak build --share=network geditruntime fakechroot fakeroot pacman --root /usr -S gedit

You can test the installation before finishing the runtime (without proper sandboxing).

 $ flatpak build --socket=x11 geditruntime gedit

Now finish building the runtime and export it to a new local repository. pacman’s GnuPG keys have permissions that may interfere and need to be removed first.

 $ flatpak build geditruntime rm -r /etc/pacman.d/gnupg
 $ flatpak build-finish geditruntime
 $ sed -i "s/\geditruntime/metadata
 $ flatpak build-export -r geditrepo geditruntime

Then create a dummy app.

 $ flatpak build-init geditapp org.gnome.gedit org.mydomain.BaseSdk org.mydomain.geditruntime

Now finish the dummy app. You can fine-tune the app’s access permissions when sandboxed by giving additional options when finishing the build. For possible options see the Flatpak documentation and the [https://gitlab.gnome.org/GNOME/gnome-apps-nightly/tree/master GNOME manifest files. Alternatively, adapt  to your needs after finishing the build but before exporting. When the metadata file is complete, export the app to the repository.

 $ flatpak build-finish geditapp --socket=x11 other options --command=gedit
 $ flatpak build-export geditrepo geditapp

Install it along with the runtime.

 $ flatpak --user remote-add --no-gpg-verify geditrepo geditrepo
 $ flatpak install --user geditrepo org.mydomain.geditruntime
 $ flatpak install --user geditrepo org.gnome.gedit
 $ flatpak run org.gnome.gedit

## Troubleshooting
## Flatpak does not run on the linux-hardened kernel
The  kernel sets  to , so only privileged users can create new user namespaces.

One method to fix this is to install . This package provides a version of  with the  bit enabled, allowing bubblewrap elevate itself and create new namespaces.

Alternatively, set  to  using , allowing unprivileged users to create new user namespaces:

 # sysctl kernel.unprivileged_userns_clone=1

To make this change persist across reboots, add a configuration file to :

For more information, see the note in Bubblewrap#Installation.

## Failed to connect to Wayland display
If the application doesn't properly open and you get messages such as  on : This may be because some other setting such as  makes the Flatpak application choose Wayland while access to Wayland isn't whitelisted for this application.

This can be fixed by whitelisting access to  with e.g. Flatseal.

## xdg-desktop-portal is failing to start
If you are starting X with manually-configured run commands, ensure you are including all essential components of the reference `xinitrc`. One of which sources a script which runs an update of the environment used for D-Bus session services.

 systemctl --user import-environment DISPLAY XAUTHORITY
 if command -v dbus-update-activation-environment >/dev/null 2>&1; then
    dbus-update-activation-environment DISPLAY XAUTHORITY
 fi

## Flatpak applications not picking up the default system theme
There is no ideal way to apply system themes in Flatpak apps as mentioned in the Flatpak documentation [https://docs.flatpak.org/en/latest/desktop-integration.html?highlight=theme#theming. The easiest solution is using themes that are available in Flathub. However there is a workaround which can be used to apply themes to your Flatpak apps.  automates this workaround.

## "File not found" error when Open local HTML pages in Firefox
By default, the Flatpak version of Firefox will display a "File not found" error page when opening a local HTML. This is because permission must be granted to the app for accessing the folder containing the file.

However, note that when granting permission to access the entire Home folder, Firefox will then check for an existing profile in  and load it instead of those previously in use from the sandboxed folder . If your previous session's tabs and browsing history is missing after changing a permission (e.g. with Flatseal), either modify the permission to exclude access to , or consider copying the profile from  to .

## Links fail to open on wlroots-based compositors
Flatpak applications that attempt to open URIs make use of the  D-Bus interface exposed by xdg-desktop-portal. The xdg-desktop-portal-wlr backend does not support this call and therefore you will need an additional backend to fill the gap, for example .

## Applications do not use the correct cursor theme
There is no single standard to set the cursor properly. Some programs only need read access to the cursors directory, others also rely on other mechanisms. For GTK applications, ensure that  is installed.

Otherwise, the following overrides should work for most common desktop applications.

 $ flatpak -u override --filesystem=/usr/share/icons/:ro
 $ flatpak -u override --filesystem=/home/$USER/.icons/:ro
 $ flatpak -u override --filesystem=xdg-config/gtk-3.0:ro
 $ flatpak -u override --env=XCURSOR_PATH=~/.icons

In some cases you may also need to override the environment variables  and :

 $ flatpak -u override --env=XCURSOR_THEME=Adwaita
 $ flatpak -u override --env=XCURSOR_SIZE=24

See this discussion for additional details.

Apparently it is not possible anymore to enable access to applications to directories under . The following hints at this when launching a program:

One possible workaround would be to manually copy your icon theme from  to .

## Flatpak Qt applications do not use Gnome Adwaita dark theme
If you switched your theme to Adwaita-dark and Flatpak Qt applications still use the light version, install the required KStyle:

 # flatpak install flathub org.kde.KStyle.Adwaita

## Permission denied error when running Flatpak applications
Flatpak applications will not run if the mount point that contains the folder in which the application is stored, typically  for system wide installations, and  for user-specific installations, is mounted with the  option.

With  set you will get errors such as this:

 $ bwrap: execvp ldconfig: Permission denied
 $ error: ldconfig failed, exit status 256
