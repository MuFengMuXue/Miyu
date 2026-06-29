[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[[]][Home](https://www.dropbox.com/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/dropbox)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dropbox "wikipedia:Dropbox")

**Dropbox** is a closed source file synchronization and cloud service utility built from open and closed source software.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Adding to runlevel]](#Adding_to_runlevel)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [Systemd]](#Systemd)
        -   [[2.1.3] [service]](#service)
    -   [[2.2] [Xfce]](#Xfce)
        -   [[2.2.1] [Launcher]](#Launcher)
    -   [[2.3] [KDE]](#KDE)
        -   [[2.3.1] [KDE4]](#KDE4)
        -   [[2.3.2] [KDE Plasma 5]](#KDE_Plasma_5)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Dropbox complains about libappindicator]](#Dropbox_complains_about_libappindicator)
    -   [[3.2] [Dropbox says it\'s an old version]](#Dropbox_says_it.27s_an_old_version)
        -   [[3.2.1] [Step 1: Unmasking the later version]](#Step_1:_Unmasking_the_later_version)
            -   [[3.2.1.1] [x86]](#x86)
            -   [[3.2.1.2] [amd64]](#amd64)
        -   [[3.2.2] [Step 2: Dropbox not create the .dropbox-dist]](#Step_2:_Dropbox_not_create_the_.dropbox-dist)
        -   [[3.2.3] [Step 3: Dropbox does not start now]](#Step_3:_Dropbox_does_not_start_now)
    -   [[3.3] [Crash with nvidia-drivers]](#Crash_with_nvidia-drivers)
    -   [[3.4] [Don\'t show Dropbox icon on KDE/Plasma\'s systray]](#Don.27t_show_Dropbox_icon_on_KDE.2FPlasma.27s_systray)
    -   [[3.5] [ImportError: libffi.so.6: cannot open shared object file: No such file or directory]](#ImportError:_libffi.so.6:_cannot_open_shared_object_file:_No_such_file_or_directory)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/dropbox](https://packages.gentoo.org/packages/net-misc/dropbox) [[]] [Dropbox daemon (pretends to be GUI-less)]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)               Add support for X11
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-15 18:25] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Before you emerge, you must accept the license. To do this, create the file /etc/portage/package.license if it isn't already present and add the following line

[CODE] **Adding licensing for Dropbox**

    net-misc/dropbox CC-BY-ND-3.0 dropbox

Alternative: if the directory /etc/portage/package.license exists then, create a text-file using your favorite text editor and add the above line. Then:

`root `[`#`]`emerge --ask net-misc/dropbox`

## [Configuration]

Set the `DROPBOX_USERS` variable to the regular user name in [/etc/conf.d/dropbox]

`root `[`#`]`nano -w /etc/conf.d/dropbox`

`DROPBOX_USERS="user_name"`

### [Adding to runlevel]

#### [OpenRC]

[OpenRC] users can add the Dropbox init script to the default runlevel with the following:

`root `[`#`]`rc-update add dropbox default`

#### [Systemd]

[systemd] users have to pass a username as the instance identifier to enable it:

`root `[`#`]`systemctl enable dropbox@<user_name>`

Be sure to replace `<user_name>` in the example above with the appropriate local machine user name.

To display a tray-icon you have to define which display to use:

`root `[`#`]`systemctl edit dropbox@<user_name>`

[CODE] **Adding display for DropBox**

    [Service]
    Environment=DISPLAY=:0

#### [service]

Now as a regular user run the command line shown below:

`user `[`$`]`dropbox start`

Which will create these directories in the user\'s directory:

-   [Dropbox/]
-   [.dropbox-dist/]
-   [.dropbox/]

** Note**\
The command line above will also launch the Dropbox login window. Enter credentials or register an existing account to finish up the installation.

** Note**\
The instructions shown above will not result in a GUI launcher for Dropbox being integrated into the window manager or desktop environment, so it seems. At least, some users have reported with XFCE4. A Dropbox launcher may need to be created for each desktop environment.

### [Xfce]

#### [Launcher]

To create a Dropbox launcher for Xfce with the command as `dropbox start`,

Download an [icon](https://www.dropbox.com/sh/y30u5e1hnnqmv22/AADAMMM-gFutPWsm_tDDAR8ka/png?dl=0) and copy it into the [/opt/dropbox/images/hicolor/16x16/] directory.

[![Dropbox launcher screenshot.png](/images/1/12/Dropbox_launcher_screenshot.png)](https://wiki.gentoo.org/wiki/File:Dropbox_launcher_screenshot.png)

### [KDE]

[]  As of **2026-02-12**, the information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Dropbox&action=edit).

#### [KDE4]

Adding Dropbox ServiceMenu to Dolphin, which allows easy access to most of Dropbox features. It uses Dropbox CLI to generate a public url, and pyndexer to allow sharing directories in public folder.

Download [scripts](http://kde-apps.org/CONTENT/content-files/124416-DropboxServiceMenu-0.16.1.tar.gz) and unzip it.

`user `[`$`]`tar xvzf *DropboxServiceMenu*.tar.gz`

Then you can use install script, which generates all files that are required.

`user `[`$`]`./install-it.sh`

After installing, you must edit script because the original script-set no longer is in development (but it still works).

`user `[`$`]`nano ~/.kde4/share/kde4/services/ServiceMenus/dropbox-scripts/dropbox_menu.sh`

Find 37 line

`` dropbox_path=`$get_dropbox_folder.sh` ``

And change it to:

`dropbox_path="$HOME/Dropbox"`

Don\'t forget to add dropbox-daemon to autorun in systemsettings.

#### [KDE Plasma 5]

KDE Plasma removed support for the legacy Xembed-based systray applications. In order for the systray icon to appear, Plasma needs to be built with legacy systray support. Please refer to the [Plasma 5 page](https://wiki.gentoo.org/wiki/KDE/Plasma_5_upgrade#Missing_systray_icons "KDE/Plasma 5 upgrade") for details. Dropbox integration with Dolphin is provided by [[[kde-apps/dolphin-plugins-dropbox]](https://packages.gentoo.org/packages/kde-apps/dolphin-plugins-dropbox)[]] when the `dropbox` USE flag is enabled:

### [USE flags for] [kde-apps/dolphin-plugins-dropbox](https://packages.gentoo.org/packages/kde-apps/dolphin-plugins-dropbox) [[]] [Dolphin plugin for Dropbox service integration]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 20:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

`root `[`#`]`emerge --ask kde-apps/dolphin-plugins-dropbox`

## [Troubleshooting]

### [Dropbox complains about [libappindicator]]

Dropbox may show a warning message indicating that [libappindicator] cannot be found. This means that Dropbox auto-updated itself and broke the [libappindicator] symlink. This is explained in the following post-install message:

[CODE]

    Warning: while running, dropbox may attempt to autoupdate itself in
    your user's home directory.  To prevent this, run the following as
    each user who will run dropbox:

    install -dm0 ~/.dropbox-dist

    If you do allow dropbox to update/install to your user homedir, you
    will need to create some compat symlinks to keep the tray icon working:

    ln -sf /usr/$(get_libdir)/libayatana-appindicator3.so.1 ~/.dropbox-dist/dropbox-lnx.*/libappindicator3.so.1
    ln -sf libappindicator3.so.1 ~/.dropbox-dist/dropbox-lnx.*/libappindicator3.so

You may reinstall Dropbox if it auto-updated itself to follow the above instructions correctly.

### [][Dropbox says it\'s an old version]

When you start dropbox and return the error of it\'s an old version of dropbox, you can have some problems, between their version to some problems of dropbox, follow the following steps to help you to solve the problem:

#### [Step 1: Unmasking the later version]

unmask the latest version for your architecture, you can found the information in [[[net-misc/dropbox]](https://packages.gentoo.org/packages/net-misc/dropbox)[]]

##### [x86]

`root `[`#`]`echo -e "net-misc/dropbox ~x86" >> /etc/portage/package.accept_keywords`

##### [amd64]

`root `[`#`]`echo -e "net-misc/dropbox ~amd64" >> /etc/portage/package.accept_keywords`

#### [Step 2: Dropbox not create the .dropbox-dist]

Another problem is that dropbox does not install the dropboxd daemon, it\'s on [.dropbox-dist] folder of their user\'s home, for force to Dropbox to install it you must install the CLI version (don\'t uninstall nothing) and force the installation of the daemon.

`root `[`#`]`emerge --ask net-misc/dropbox-cli `

Creating the daemon\'s folder:

`user `[`$`]`dropbox-cli start -i`

Starting Dropbox:

`user `[`$`]`dropbox start`

if it continues to not start, follow the next step:

#### [Step 3: Dropbox does not start now]

At this time, you have a problem between the GL library installed by dropbox called [libGL.so.1], it conflicts with the already installed X driver, to solve the problem, remove it, its inside [\~/.dropbox-dist/dropbox-lnx./].

`user `[`$`]` rm ~/.dropbox-dist/dropbox-lnx.x86_64-3.10.11/libGL.so.1`

`user `[`$`]` dropbox start `

Sometimes it is also necessary to remove the DRM library from [\~/.dropbox-dist/dropbox-lnx./], continue to remove it aswell.

`user `[`$`]` rm ~/.dropbox-dist/dropbox-lnx.x86_64-3.10.11/libdrm.so.2`

`user `[`$`]` dropbox start `

### [Crash with nvidia-drivers]

When trying to launch Dropbox on a system with nVidia proprietary drivers ([[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]]) Dropbox wouldn\'t start. It turns out that the problem is related to a bundled [libGL.so.1] library inside the Dropbox installation.

In order to fix this it is necessary to remove this library and let Dropbox use the system-provided version. This is already done by the ebuild, however Dropbox is automatically updating itself into [\~/.dropbox-dist/] so it is necessary to also remove the library from there.

`user `[`$`]`rm ~/.dropbox-dist/dropbox-lnx.x86_64-3.8.8/libGL.so`

### [][Don\'t show Dropbox icon on KDE/Plasma\'s systray]

[]  As of **2019-10-18**, the information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Dropbox&action=edit).

Make sure that you have added the \"legacy-systray\" support and understand all issues mentioned in [Plasma 5 page](https://wiki.gentoo.org/wiki/KDE/Plasma_5_upgrade#Missing_systray_icons "KDE/Plasma 5 upgrade")

Resume of adding legacy-systray support for KDE/Plasma:

`root `[`#`]`echo "kde-plasma/plasma-desktop legacy-systray gtk2 gtk3 qt4" >> /etc/portage/package.use `

`root `[`#`]`emerge --ask dev-libs/sni-qt libappindicator:2 libappindicator:3 `

`root `[`#`]`emerge --ask --update --deep --verbose --tree --newuse kde-plasma/plasma-desktop `

If it does not work for you, make sure that you are on the latest version (**[\~x86]**, **[\~amd64]**,\...) and, have stopped the service, remove the following files and restart dropbox from the user\'s bash.

Stopping Dropbox:

`root `[`#`]`rc-service dropbox stop`

Deleting some files (make sure that your adding your Dropbox\'s Version on ) and restarting Dropbox:

`user `[`$`]`rm .dropbox-dist/dropbox-lnx./libQt5* `

`user `[`$`]`rm .dropbox-dist/dropbox-lnx./qt.conf `

`user `[`$`]`rm .dropbox-dist/dropbox-lnx./plugins/platforms/libqxcb.so `

`user `[`$`]`dropbox `

### [ImportError: libffi.so.6: cannot open shared object file: No such file or directory]

If you tried to start Dropbox after installing it and got the followingː

`user `[`$`]`dropbox start`

    dropbox: locating interpreter
    dropbox: logging to /tmp/dropbox-antifreeze-qeteiz
    dropbox: initializing
    dropbox: initializing python 3.5.4
    dropbox: setting program path '/opt/dropbox/dropbox'
    dropbox: setting home path '/opt/dropbox'
    dropbox: setting python path '/opt/dropbox:/opt/dropbox/python-packages-35.zip'
    dropbox: python initialized
    dropbox: running dropbox
    dropbox: setting args
    dropbox: applying overrides
    dropbox: running main script
    dropbox: load fq extension '/opt/dropbox/cryptography.hazmat.bindings._constant_time.cpython-35m-x86_64-linux-gnu.so'
    Traceback (most recent call last):
      File "dropbox/__init__.pyc", line 8, in <module>
      File "dropbox/overrides.pyc", line 517, in <module>
      File "dropbox/overrides.pyc", line 418, in __ssl_wrap_socket_internal_ca_certs
      File "dropbox/ssl/revoked_certs.pyc", line 9, in <module>
      File "cryptography/x509/__init__.pyc", line 9, in <module>
      File "cryptography/x509/base.pyc", line 16, in <module>
      File "cryptography/x509/extensions.pyc", line 18, in <module>
      File "cryptography/hazmat/primitives/constant_time.pyc", line 9, in <module>
      File "<_bootstrap_overrides>", line 153, in load_module
    ImportError: libffi.so.6: cannot open shared object file: No such file or directory
    !! dropbox: fatal python exception:
    ['Traceback (most recent call last):\n', '  File "dropbox/__init__.pyc", line 8, in <module>\n', '  File "dropbox/overrides.pyc", line 517, in <module>\n', '  File "dropbox/overrides.pyc", line 418, in __ssl_wrap_socket_internal_ca_certs\n', '  File "dropbox/ssl/revoked_certs.pyc", line 9, in <module>\n', '
    File "cryptography/x509/__init__.pyc", line 9, in <module>\n', '  File "cryptography/x509/base.pyc", line 16, in <module>\n', '  File "cryptography/x509/extensions.pyc", line 18, in <module>\n', '  File "cryptography/hazmat/primitives/constant_time.pyc", line 9, in <module>\n', '  File
    "<_bootstrap_overrides>", line 153, in load_module\n', 'ImportError: libffi.so.6: cannot open shared object file: No such file or directory\n'] (error 3)
    Aborted

Install the **net-misc/dropbox-58.3.88-r1** and above which does not have this problem:

`root `[`#`]`emerge --ask '>=net-misc/dropbox-58.3.88-r1'`

## [See also]

-   [SparkleShare](https://wiki.gentoo.org/wiki/SparkleShare "SparkleShare") --- a cross platform, free, open source, Dropbox-like, git-based collaboration and file sharing tool.
-   [Owncloud](https://wiki.gentoo.org/wiki/Owncloud "Owncloud") --- a free, open source, Dropbox-like file synchronization and cloud service.