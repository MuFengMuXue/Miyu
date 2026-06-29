**Resources**

[[]][Home](https://system76.com/cosmic/)

[[]][GitHub](https://github.com/pop-os/cosmic-epoch)

**COSMIC** is a desktop environment built by System76 in Rust.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Overlay]](#Overlay)
    -   [[1.2] [Unmasking unstable ebuilds]](#Unmasking_unstable_ebuilds)
    -   [[1.3] [Unmasking live ebuilds]](#Unmasking_live_ebuilds)
    -   [[1.4] [Emerging]](#Emerging)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Display Manager]](#Display_Manager)
        -   [[2.1.1] [systemd]](#systemd)
        -   [[2.1.2] [OpenRC]](#OpenRC)
        -   [[2.1.3] [Autologin]](#Autologin)
        -   [[2.1.4] [SDDM and other Display Managers]](#SDDM_and_other_Display_Managers)
-   [[3] [Optional: SDDM autologin to Cosmic]](#Optional:_SDDM_autologin_to_Cosmic)
    -   [[3.1] [Locale Management]](#Locale_Management)
        -   [[3.1.1] [Systemd]](#Systemd_2)
        -   [[3.1.2] [OpenRC]](#OpenRC_2)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Cosmic Session Does Not Start]](#Cosmic_Session_Does_Not_Start)
        -   [[4.1.1] [Check D-Bus services]](#Check_D-Bus_services)
        -   [[4.1.2] [Inspect runtime environment]](#Inspect_runtime_environment)
        -   [[4.1.3] [Verify services are running]](#Verify_services_are_running)
        -   [[4.1.4] [Check greeter user runtime directory]](#Check_greeter_user_runtime_directory)
        -   [[4.1.5] [Examine logs]](#Examine_logs)
-   [[5] [See also]](#See_also)

## [Installation]

** Note**\
On musl profiles, prefer building [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] from [source](https://wiki.gentoo.org/wiki/Rust "Rust") before attempting installation.

** Warning**\
While COSMIC can be ran on [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), it currently only fully supports [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").

### [Overlay]

The [fsvm88\'s cosmic-overlay](https://github.com/fsvm88/cosmic-overlay) provides all necessary packages.

It can be added with the following commands:

`root `[`#`]`eselect repository add cosmic-overlay git https://github.com/fsvm88/cosmic-overlay.git `

`root `[`#`]`emaint sync -r cosmic-overlay `

### [Unmasking unstable ebuilds]

For the latest tagged release, unmask the packages in [/etc/portage/package.accept_keywords/cosmic-de] (or whatever file is preferred):

[FILE] **`/etc/portage/package.accept_keywords/cosmic-de`Unmasking unstable ebuilds**

    cosmic-base/* ~amd64
    cosmic-de/* ~amd64

### [Unmasking live ebuilds]

To try out the latest commits from [master] branch, unmask the packages in [/etc/portage/package.accept_keywords/cosmic-de] (or whatever file is preferred):

[FILE] **`/etc/portage/package.accept_keywords/cosmic-de`Unmasking unstable ebuilds**

    # live ebuilds are masked via "missing" keywords
    cosmic-de/* **
    cosmic-base/* **

\

** Note**\
Do **not** mix unstable (alpha) releases with live ebuilds. This can cause ABI/API mismatches (for example \`cosmic-session\` built as alpha7 while \`xdg-desktop-portal-cosmic\` is 9999), resulting in Cosmic failing to start.

### [Emerging]

After unmasking the ebuilds, COSMIC can be installed by emerging the following packages.

`root `[`#`]`emerge --ask cosmic-meta pop-theme-meta`

** Note**\
COSMIC overlay ebuilds attempt to install [[[dev-util/dart-sass-bin]](https://packages.gentoo.org/packages/dev-util/dart-sass-bin)[]], which may conflict with the official [[[dev-ruby/sass]](https://packages.gentoo.org/packages/dev-ruby/sass)[]]. As per [this commit](https://github.com/fsvm88/cosmic-overlay/commit/18906ffd1a81b16647b62981430bb6a1d79f60e1), [[[gui-libs/adw-gtk3]](https://packages.gentoo.org/packages/gui-libs/adw-gtk3)[]] versions greater than or equal to 5.10 won\'t build with [[[dev-ruby/sass]](https://packages.gentoo.org/packages/dev-ruby/sass)[]]. Therefore, consider using [[[dev-util/dart-sass-bin]](https://packages.gentoo.org/packages/dev-util/dart-sass-bin)[]] from the COSMIC overlay.

\

## [Configuration]

### [Display Manager]

The most convenient way of login management while using COSMIC is using [greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd").

Configuration process for the [Display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") is a bit different on systems with and without systemd.

#### [systemd]

[greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd") needs to be installed:

`root `[`#`]`emerge --ask gui-libs/greetd`

cosmic-greeter, upower and acpid need to be enabled:

`root `[`#`]`systemctl enable cosmic-greeter.service cosmic-greeter-daemon.service upower.service acpid.socket`

#### [OpenRC]

First of all, [display-manager-init](https://wiki.gentoo.org/wiki/Display_manager "Display manager"), [greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd") and [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") need to be installed:

`root `[`#`]`emerge --ask gui-libs/display-manager-init gui-libs/greetd sys-auth/elogind`

[greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd") needs to be configured as a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager"). That can be achieved with the following configuration for openrc:

[FILE] **`/etc/conf.d/display-manager`greetd with cosmic-greeter**

    CHECKVT=7
    DISPLAYMANAGER="greetd"

Make sure that the following services are enabled:

For openrc users,

`root `[`#`]`rc-update add elogind boot`

`root `[`#`]`rc-update add display-manager default`

For systemd users,

`root `[`#`]`systemctl enable greetd.service`

At the end, [greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd") needs to be configured to run [cosmic-greeter] as a frontend. It\'s very important to run it as [cosmic-greeter] user.

[FILE] **`/etc/greetd/config.toml`greetd with cosmic-greeter**

    [terminal]
    vt = 7

    [default_session]
    command = "/usr/bin/dbus-run-session /usr/bin/cosmic-comp /usr/bin/cosmic-greeter >>/var/log/cosmic.log 2>&1"
    user = "cosmic-greeter"

After that, reboot the machine. If everything went well, a password prompt will appear and then COSMIC can be started.

Alternatively, logging can be configured to use system logger directly instead of writing to file

[FILE] **`/etc/greetd/config.toml`greetd with cosmic-greeter**

    [terminal]
    vt = 7

    [default_session]
    command = "/usr/bin/dbus-run-session /usr/bin/cosmic-comp /usr/bin/cosmic-greeter 2>&1 | /usr/bin/logger -t cosmic-greeter"
    user = "cosmic-greeter"

#### [Autologin]

Some users might want to autologin into Cosmic session. To do that, edit [greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd") configuration like this:

[FILE] **`/etc/greetd/config.toml`greetd autologin Cosmic**

    [terminal]
    vt = 7

    [default_session]
    command = "/usr/bin/dbus-run-session env XDG_SESSION_TYPE=wayland XDG_CURRENT_DESKTOP=COSMIC /usr/bin/start-cosmic 2>&1 | /usr/bin/logger -t cosmic-greeter"
    user = "your-username"

#### [SDDM and other Display Managers]

To make Cosmic launch from SDDM's session list, create or edit the following file:

[FILE] **`/usr/share/wayland-sessions/cosmic.desktop`Cosmic session for SDDM**

    [Desktop Entry]
    Name=Cosmic
    Comment=System76 COSMIC Desktop
    Exec=dbus-run-session env XDG_SESSION_TYPE=wayland XDG_CURRENT_DESKTOP=COSMIC start-cosmic
    Type=Application
    DesktopNames=COSMIC

## [Optional: SDDM autologin to Cosmic]

[FILE] **`/etc/sddm.conf.d/10-autologin.conf`SDDM autologin to Cosmic**

    [Autologin]
    User=your-username
    Session=cosmic.desktop

### [Locale Management]

In the COSMIC ecosystem, locales are managed via the COSMIC initial setup and COSMIC settings applications. In order for this to function, users should follow the directions in the following sections that are applicable to their system.

#### [Systemd]

Nothing special needs to be done for users of [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") because the required [localed] daemon should be running already.

#### [OpenRC]

In order to manage locales via [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), you must start and enable [openrc-settingsd]. This can be done by running,

`root `[`#`]`rc-update add openrc-settingsd default`

`root `[`#`]`rc-service openrc-settingsd start`

This is required in order to provide the [org.freedesktop.locale1] D-Bus interface which is used to actually set the locale.

## [Troubleshooting]

### [Cosmic Session Does Not Start]

In the event that the Cosmic session does not start, check if it actually launches by executing it directly in TTY:

`root `[`#`]`dbus-run-session -- env XDG_SESSION_TYPE=wayland XDG_CURRENT_DESKTOP=COSMIC start-cosmic`

#### [Check D-Bus services]

Inside a running Cosmic session, verify that System76 services are available:

`root `[`#`]`dbus-send --session --dest=org.freedesktop.DBus --type=method_call \ --print-reply /org/freedesktop/DBus org.freedesktop.DBus.ListNames \ | sed -n 's/.*string "\(com\.system76[^"]*\)".*/\1/p'`

\
You should see multiple \`com.system76.\*\` names such as \`com.system76.CosmicSettingsDaemon\`.

#### [Inspect runtime environment]

Ensure the session has the right variables:

`root `[`#`]`env | grep -E 'XDG_CURRENT_DESKTOP|XDG_SESSION_TYPE|XDG_RUNTIME_DIR|DBUS_SESSION_BUS_ADDRESS'`

Expected values are \`XDG_CURRENT_DESKTOP=COSMIC\` and \`XDG_SESSION_TYPE=wayland\`.

#### [Verify services are running]

On OpenRC systems:

`root `[`#`]`rc-service dbus status`

`root `[`#`]`rc-service elogind status`

On systemd systems:

`root `[`#`]`systemctl status dbus`

`root `[`#`]`systemctl status systemd-logind`

Both \`dbus\` and the login/session manager (\`elogind\` on OpenRC, \`systemd-logind\` on systemd) must be running for Cosmic to start properly.

#### [Check greeter user runtime directory]

If using \`greetd\`, confirm the \`cosmic-greeter\` user has a runtime directory:

`root `[`#`]`ls -ld /run/user/$(id -u cosmic-greeter)`

If missing, verify \`/etc/pam.d/greetd\` contains:

[FILE] **`/etc/pam.d/greetd`PAM config for greetd with elogind**

    auth      include  system-login
    account   include  system-login
    password  include  system-login
    session   include  system-login
    session   required pam_elogind.so

#### [Examine logs]

Check logs for errors if Cosmic immediately returns to the greeter:

`root `[`#`]`tail -n 200 /var/log/messages | grep -Ei 'cosmic-greeter|cosmic-comp|elogind|dbus|permission|denied'`

## [See also]

-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland
-   [Hyprland](https://wiki.gentoo.org/wiki/Hyprland "Hyprland") --- an open-source [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") written in C++.
-   [Plasma](https://wiki.gentoo.org/wiki/Plasma "Plasma") --- a free software community, producing a wide range of applications including the popular Plasma desktop environment.
-   [Gnome](https://wiki.gentoo.org/wiki/Gnome "Gnome") --- a feature-rich desktop environment provided by the [GNOME project](https://www.gnome.org).