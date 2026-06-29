**Resources**

[[]][Home](https://buddiesofbudgie.org)

[[]][GitHub](https://github.com/BuddiesOfBudgie/budgie-desktop)

[[]][Bugs (upstream)](https://github.com/BuddiesOfBudgie/budgie-desktop/issues)

**Budgie** is a feature-rich, modern desktop designed to keep out the way of the user. [Buddies of Budgie](https://buddiesofbudgie.org) was founded to provide a home for the Budgie Desktop, an open source modern desktop environment built to provide you immediate access to the things you need. It focuses on simplicity and elegance.

** Note**\
The Budgie desktop environment is not currently available in the main [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), there is however a Budgie ebuild repository available: [https://gitlab.com/SarahMia/sarahmiaoverlay](https://gitlab.com/SarahMia/sarahmiaoverlay).

Please report bugs [upstream](https://github.com/BuddiesOfBudgie/) and provide sufficient details (how to reproduce, info, logs, errors, etc).

Since latest release of budgie dekstop 10.10 budgie desktop will now only work on wayland. 10.9.3 is still available on the repository for those who prefer to use budgie-desktop on X11-Xorg. It is advised during installation to check which version is being installed to prevent confusion and issues.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Overlay]](#Overlay)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Migration from Budgie Desktop 10.9.3 to Budgie Desktop 10.10+]](#Migration_from_Budgie_Desktop_10.9.3_to_Budgie_Desktop_10.10.2B)
-   [[3] [Display Manager]](#Display_Manager)
-   [[4] [Personalize]](#Personalize)
    -   [[4.1] [Budgie Settings]](#Budgie_Settings)
    -   [[4.2] [File Manager]](#File_Manager)
    -   [[4.3] [Styling / Themes]](#Styling_.2F_Themes)

## [Installation]

#### [Overlay]

To be able to enable the overlay install the app-eselect/eselect-repository and dev-vcs/git packages.

`root `[`#`]`emerge --ask app-eselect/eselect-repository dev-vcs/git`

In order to be able to install the Budgie desktop on Gentoo enable the overlay created by SarahMia:

`root `[`#`]`eselect repository enable SarahMiaOverlay`

Also sync the overlay using:

`root `[`#`]`emerge --sync SarahMiaOverlay`

#### [USE flags]

The [[[budgie-base/budgie-meta]](https://packages.gentoo.org/packages/budgie-base/budgie-meta)[]] package provides the full Budgie desktop, configurable with 1 USE flag:

Minimal makes budgie-base/budgie-meta only install essential packages for the desktop to work. everything.

#### [Emerge]

The stable version is 10.9.3. This version will only work on X11-Xorg. For budgie-desktop-10.10.2 (and higher, which will only work on wayland), unstable keywords must be set beforehand:

[FILE] **`/etc/portage/package.accept_keywords/budgie-desktop`Allow latest versions to be installed**

    # Set to accept ~keywords for the entire repository to allow 10.10.X (wayland) to be installed.
    */*::SarahMiaOverlay

From here on one can install budgie desktop.

Install Budgie:

`root `[`#`]`emerge --ask budgie-base/budgie-meta`

Alternatively, If the user wants a very basic desktop, Install budgie-base/budgie-meta with the minimal USE flag.

[FILE] **`/etc/portage/package.use/budgie-meta`Change USE flags for budgie-base/budgie-meta**

    # Install's only budgie-desktop and budgie-control-center. (And for 10.9.3 also budgie-screensaver and budgie-desktop-view)
    budgie-base/budgie-meta minimal

If simply everything is wanted with all the applets you can install budgie-applets-meta.

`root `[`#`]`emerge --ask budgie-extra/budgie-applets-meta`

One can also specify what applets should be installed with the useflag BUDGIE_APPLETS. By default all will be installed with the exception of of a few. By setting

[FILE] **`/etc/portage/package.use/budgie`Set BUDGIE_APPLETS**

    */*::SarahMiaOverlay BUDGIE_APPLETS: app-launcher wallstreet show-weather

One can install any applet separately if wanted instead, but installing budgie-applets-meta is the recommended way.

The full list of applets can be found here: [https://gitlab.com/SarahMia/sarahmiaoverlay/-/wikis/Budgie-Applets](https://gitlab.com/SarahMia/sarahmiaoverlay/-/wikis/Budgie-Applets)

## [][Migration from Budgie Desktop 10.9.3 to Budgie Desktop 10.10+]

Due to the way Budgie Desktop works internally there is now a big wall between the 2. Most applets e.g. now have a version that work only with 1 or the other. While upgrading (or downgrading) in itself is actually very simple there is a chance you may run into issues. To be on the safe side it is best to first check how the upgrade looks like:

Check for any potential issues:

`root `[`#`]`emerge --ask --deep --update --ask --verbose --newuse budgie-meta budgie-applets-meta`

It is likely you see a lot of conflicts in regard to budgie-desktop. To safely resolve this unmerging budgie desktop is needed:

`root `[`#`]`emerge --ask --unmerge budgie-desktop`

Now the regular should work without any issues:

`root `[`#`]`emerge --ask --deep --update --ask --verbose --newuse budgie-meta budgie-applets-meta`

If one is in an active budgie desktop session it is recommended to fully logout and log back in once the migration is finished.

The same goes for downgrading back to 10.9.3. For regular updates of 10.10 to any higher version should work fine without any issues.

To see more information please check [https://gitlab.com/SarahMia/sarahmiaoverlay/-/wikis/Upgrading](https://gitlab.com/SarahMia/sarahmiaoverlay/-/wikis/Upgrading) and [https://gitlab.com/SarahMia/sarahmiaoverlay/-/wikis/Troubleshooting](https://gitlab.com/SarahMia/sarahmiaoverlay/-/wikis/Troubleshooting) for any other issues one may have.

## [Display Manager]

The recommended display manager to use with Budgie is LightDM, but any other will work. For instructions follow:

-   [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM"): Follow for instructions with enabling LightDM.
-   [Display_manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager"): Follow for instructions with enabling other display managers.

## [Personalize]

Budgie-desktop by itself comes pretty empty. You can install any application you want. Since Budgie Desktop uses GTK3 and 4 the preferences goes to GTK applications but the user is free to run any others.

### [Budgie Settings]

All settings can be found in Budgie Desktop Settings and Budgie System Settings. If budgie-extras is installed with the associated applets (by default all are) then there are additional settings available in Previews Control (for alt tabbing), Wallstreet Control (for rotating wallpapers) and Window Shuffler Control (for tiling and window placement support).

### [File Manager]

Budgie-desktop by itself comes without a file manager. You are free to install one yourself of your choice. Nautilus and Nemo are most used for Budgie Desktop and also fit the best.

### [][Styling / Themes]

Budgie Desktop 10.10.X will come with Materia theme installed (as dependency). One can select that in the settings or use any other theme if wanted such as ark and vertex e.g. For Budgie-Desktop 10.9.3 there is no default theme installed. For that one could install materia theme themselves (or any other if wanted):

`root `[`#`]`emerge --ask x11-themes/materia-theme`

The user can download a theme from another place such as [https://www.gnome-look.org/](https://www.gnome-look.org/). If done then place the theme directory in [\~/.local/share/themes/] (If the directory does not exist, please create the directory.

To style any Gnome application place the contents of the libadwaita (or the gtk-4.0 if it doesn\'t exist) directory thats inside the theme directory in [\~/.config/gtk-4.0/]

Downloaded icon and cursor themes can be placed in [\~/.icons]. If the directory does not exist please create it.

The themes can then be selected in Budgie Desktop Settings under the Style category. GNOME applications should be auto styled after they are restarted. Backgrounds are changed in Budgie System Settings.