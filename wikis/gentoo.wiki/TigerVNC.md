This page contains [[changes](https://wiki.gentoo.org/index.php?title=TigerVNC&oldid=1354226&diff=1399900)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/TigerVNC/hu "TigerVNC (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/TigerVNC/pl "TigerVNC (58% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/TigerVNC/ja "TigerVNC/ja (4% translated)")

**Resources**

[[]][Home](https://tigervnc.org/)

[[]][GitHub](https://github.com/TigerVNC/tigervnc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/TigerVNC "wikipedia:TigerVNC")

**TigerVNC** is a client/server software package allowing remote network access to graphical desktops.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [Additional Software]](#Additional_Software)
-   [[2] [User Session Configuration]](#User_Session_Configuration)
    -   [[2.1] [Localhost Session]](#Localhost_Session)
-   [[3] [Single Server Configuration]](#Single_Server_Configuration)
-   [[4] [Multiple Server Configuration]](#Multiple_Server_Configuration)
    -   [[4.1] [Displays]](#Displays)
    -   [[4.2] [Desktop environments]](#Desktop_environments)
-   [[5] [Configuration]](#Configuration)
    -   [[5.1] [Service]](#Service)
        -   [[5.1.1] [OpenRC]](#OpenRC)
        -   [[5.1.2] [systemd]](#systemd)
-   [[6] [Usage]](#Usage)
    -   [[6.1] [Connecting]](#Connecting)
        -   [[6.1.1] [Connect over ssh with high resolution]](#Connect_over_ssh_with_high_resolution)
-   [[7] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/tigervnc](https://packages.gentoo.org/packages/net-misc/tigervnc) [[]] [Remote desktop viewer display system]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+drm`](https://packages.gentoo.org/useflags/+drm)             Build with DRM support
  [`+opengl`](https://packages.gentoo.org/useflags/+opengl)       Add support for OpenGL (3D graphics)
  [`+server`](https://packages.gentoo.org/useflags/+server)       Build TigerVNC server
  [`+viewer`](https://packages.gentoo.org/useflags/+viewer)       Build TigerVNC viewer
  [`dri3`](https://packages.gentoo.org/useflags/dri3)             Build with DRI3 support
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)         Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`java`](https://packages.gentoo.org/useflags/java)             Build TigerVNC Java viewer
  [`nls`](https://packages.gentoo.org/useflags/nls)               Add Native Language Support (using gettext - GNU locale utilities)
  [`pwquality`](https://packages.gentoo.org/useflags/pwquality)   Use dev-libs/libpwquality for password quality checking in vncpasswd
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)       Enable dev-libs/wayland backend
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)     Add support for querying multi-monitor screen geometry through the Xinerama API
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-31 18:41] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/tigervnc`

#### [Additional Software]

The following package can be installed to integrate the VNC server into Xorg:

`root `[`#`]`emerge --ask net-misc/tigervnc-xorg-module`

## [User Session Configuration]

The easiest way to use TigerVNC as a server is to run the **x0vncserver** component with the user\'s X session:

[FILE] **`~/.xinitrc`**

    ...
    x0vncserver -PasswordFile ~/.config/tigervnc/passwd
    ...

The password file can be defined with:

`user `[`$`]`mkdir ~/.config/tigervnc `

`user `[`$`]`vncpasswd ~/.config/tigervnc/passwd `

`user `[`$`]`chmod 600 ~/.config/tigervnc/passwd`

### [Localhost Session]

A VNC server can be started on localhost instead of on the network, allowing it to be forwarded over SSH, this can be accomplished with:

[FILE] **`~/.xinitrc`**

    ...
    x0vncserver -PasswordFile ~/.config/tigervnc/passwd -localhost
    ...

A SSH connection can be made, forwarding `127.0.0.1:5900` on the destination machine to port *5900* on the client:

`user `[`$`]`ssh -L 5900:127.0.0.1:5900 larry@remoteMachine`

** Important**\
This ssh session must remain open for the VNC session to function.

## [Single Server Configuration]

This configuration allows remote control of the **entire** Xorg X11 server. [[[net-misc/tigervnc-xorg-module]](https://packages.gentoo.org/packages/net-misc/tigervnc-xorg-module)[]] is required.

Create the TigerVNC config file for Xorg X11:

`root `[`#`]`mkdir -p /etc/X11/xorg.conf.d`

[FILE] **`/etc/X11/xorg.conf.d/40-vnc.conf`**

    Section "Module"
        Load "vnc"
    EndSection
    Section "Screen"
        Identifier "Default Screen"
        Option "PasswordFile" "/etc/X11/vncpasswd"
    EndSection

Create /etc/X11/vncpasswd

`root `[`#`]`vncpasswd /etc/X11/vncpasswd`

## [Multiple Server Configuration]

** Important**\
Starting with version 1.12, tigervnc no longer supports starting servers as \'normal\' user. A global configuration with sessions is now required. The following can still be used to test configuration.

Login as \'normal\' user. The following steps can be taken for any user who wishes to configure the VNC server for remote connection.

Set a password:

`user `[`$`]`vncpasswd`

Start the server giving it an unused display number (for example :1 or :2):

`user `[`$`]`vncserver :N`

If desired, use a VNC client on either a local or remote machine to test the connection.

Once finished, kill the running vncserver by pressing C-c.

### [Displays]

** Note**\
Starting with 1.13.1-r3, the TigerVNC service for OpenRC got migrated to a one session per service model, similar to what systemd does. Otherwise, starting all TigerVNC sessions in the same OpenRC service had a major drawback: if one session crashed, it could not be restarted without killing all the others.

Setup the displays in the TigerVNC configuration file:

[FILE] **`/etc/tigervnc/vncserver.users`**

    :1=user
    :2=user2

Typically the value of `:0` will be used for the server\'s own X display. This is why the example above starts by using the `:1` display handle.

** Important**\
The conf.d steps below were only needed for OpenRC with \<net-misc/tigervnc-1.13.1-r3. The DISPLAYS variable is no longer used in newer versions.

Setup the displays for OpenRC. This step is not required for systemd. Substitute each \'`user`\' value below with the name of a user who will be running the VNC server on the machine:

[FILE] **`/etc/conf.d/tigervnc`**

    DISPLAYS="user:1 user2:2"

### [Desktop environments]

To setup the default desktop environment, add it to `session=` (or uncomment one from below):

[FILE] **`/etc/tigervnc/vncserver-config-defaults`**

    # session=gnome
    # securitytypes=vncauth,tlsvnc
    # geometry=2000x1200
    # localhost
    # alwaysshared

    # Other possible working sessions:
    #session=e16-session
    #session=enlightenment
    #session=fvwm
    #session=gnome-classic
    #session=gnome-custom-session
    #session=gnome
    #session=gnome-xorg
    #session=LXDE
    #session=lxqt
    #session=openbox
    #session=plasma
    #session=xfce
    #session=Xsession

Each user who will be running a VNC server can override this configuration by adding it to `~/.config/tigervnc/config`. There is a file `/etc/tigervnc/vncserver-config-mandatory` where the system administrator can override user\'s config. `~/.config/tigervnc/xstartup` is no longer supported and the current server ignores it.

** Important**\
If the session configuration doesn\'t get applied or the VNC server simply exits right away, see [Gentoo bug #936475](https://bugs.gentoo.org/936475) \-- you may need to install a [Display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager"), set `TIGERVNC_XSESSION_FILE`, or hack `/etc/X11/Sessions/Xsession`

## [Configuration]

### [Service]

#### [OpenRC]

This example assumes 2 displays, :1 and :2

Create one link for every display:

`root `[`#`]`ln -s tigervnc /etc/init.d/tigervnc.1 `

`root `[`#`]`ln -s tigervnc /etc/init.d/tigervnc.2 `

Start the server(s):

`root `[`#`]`rc-service tigervnc.1 start `

`root `[`#`]`rc-service tigervnc.2 start`

Start the server(s) at startup:

`root `[`#`]`rc-update add tigervnc.1 default `

`root `[`#`]`rc-update add tigervnc.2 default`

Even having only one display requires creating a symlink.

#### [systemd]

Start the server:

`root `[`#`]`systemctl enable vncserver@:<display>.service`

for each `:display` in `/etc/tigervnc/vncserver.users`

## [Usage]

### [Connecting]

`user `[`$`]`vncviewer server:1`

#### [Connect over ssh with high resolution]

`user `[`$`]`vncviewer -Fullcolor -QualityLevel 9 -via user@remotehost localhost:1 `

`user `[`$`]`vncviewer -Fullcolor -QualityLevel 9 -via user2@remotehost localhost:2 `

## [See also]

-   [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") --- the ubiquitous tool for logging into and working on remote machines securely.