This page contains [[changes](https://wiki.gentoo.org/index.php?title=DDE&diff=1429042)] which are not marked for translation.

\

[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=DDE&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

deepin-overlay repo hasn\'t had an update in 4 years (as of 2025-08).

**Resources**

[[]][Home](https://www.deepin.org/en/dde/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Deepin#DDE "wikipedia:Deepin")

[[]][Ebuild repository](https://github.com/zhtengw/deepin-overlay)

**Deepin Desktop Environment** is an elegant, easy to use and reliable domestic desktop environment released by Deepin Technology Co., Ltd. It is primarily written in Golang and Qt5. It was originally written for Deepin Linux, and is ported to Gentoo.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Add deepin overlay]](#Add_deepin_overlay)
        -   [[1.1.1] [Option 1: Install by eselect repository]](#Option_1:_Install_by_eselect_repository)
        -   [[1.1.2] [Option 2: Manually add repos.conf]](#Option_2:_Manually_add_repos.conf)
    -   [[1.2] [KEYWORDS]](#KEYWORDS)
    -   [[1.3] [Profile and USE flags]](#Profile_and_USE_flags)
        -   [[1.3.1] [OpenRC]](#OpenRC)
        -   [[1.3.2] [systemd]](#systemd)
    -   [[1.4] [Updating system]](#Updating_system)
-   [[2] [Emerging Deepin Desktop Environment]](#Emerging_Deepin_Desktop_Environment)
-   [[3] [Configuring and running DDE]](#Configuring_and_running_DDE)
    -   [[3.1] [Configuring lightdm greeter]](#Configuring_lightdm_greeter)
        -   [[3.1.1] [Optional: adding a normal user]](#Optional:_adding_a_normal_user)
    -   [[3.2] [Setting default services and running DDE]](#Setting_default_services_and_running_DDE)
        -   [[3.2.1] [OpenRC]](#OpenRC_2)
            -   [[3.2.1.1] [With display-manager]](#With_display-manager)
            -   [[3.2.1.2] [With the deprecated xdm init script]](#With_the_deprecated_xdm_init_script)
        -   [[3.2.2] [systemd]](#systemd_2)
-   [[4] [Removal]](#Removal)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [External resources]](#External_resources)

## [Prerequisites]

### [Add deepin overlay]

[DDE] currently resides in the [deepin](https://github.com/zhtengw/deepin-overlay) ebuild repository. There are three primary methods for installing repositories in Gentoo:

#### [Option 1: Install by eselect repository]

First emerge [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]]:

`root `[`#`]`emerge --ask --noreplace app-eselect/eselect-repository dev-vcs/git`

Then add the overlay and sync:

`root `[`#`]`eselect repository add deepin git https://github.com/zhtengw/deepin-overlay.git `

`root `[`#`]`emerge --sync deepin `

#### [Option 2: Manually add repos.conf]

Create a file in the [[/etc/portage/repos.conf/](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")] directory (create the [repos.conf] directory first if it does not exist) called [deepin.conf]. Fill the file\'s contents with the following code:

[FILE] **`/etc/portage/repos.conf/deepin.conf`**

    [deepin]
    location = /usr/local/overlay/deepin
    sync-type = git
    sync-uri = https://github.com/zhtengw/deepin-overlay.git
    auto-sync = yes

### [KEYWORDS]

For now, only the **[\~amd64]** and **[\~x86]** keywords are supported. So enabling testing global keyword will make it \'quick and easy\' for installing DDE.

[FILE] **`/etc/portage/make.conf`**

    ACCEPT_KEYWORDS="~amd64"

### [Profile and USE flags]

** Important**\
Read [relevant documentation](https://wiki.gentoo.org/wiki/Profile_(Portage)#Changing_profile "Profile (Portage)") before performing any profile changes.

#### [OpenRC]

Using the basic [desktop] profile:

`root `[`#`]`eselect profile set default/linux/amd64/23.0/desktop`

Add `elogind` USE flag in [/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf"), it\'s also recommended to disable support for other session trackers to avoid conflicts:

[FILE] **`/etc/portage/make.conf`**

    USE="elogind -systemd"

#### [systemd]

** Warning**\
Read the [[systemd]](https://wiki.gentoo.org/wiki/Systemd "Systemd") documentation before changing to a [systemd] profile.

Using the [systemd] profile:

`root `[`#`]`eselect profile set default/linux/amd64/23.0/systemd`

Ensure that `X` USE flag is included in the system\'s global [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

### [Updating system]

After setting, ensure everything is up-to-date and remerge \@world to make the changes take effect:

`root `[`#`]`emerge --sync `

`root `[`#`]`emerge --deep --with-bdeps=y --changed-use --update --ask --verbose @world `

## [Emerging Deepin Desktop Environment]

Set proper USE flags for [dde-base/dde-meta], as describe below:

  --------------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  USE flag        Default   Description
  `elogind`                 Use [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]] to make DDE runs under [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")
  `extra`                   Install extra applicaions developed by Deepin
  `grub`                    Install Deepin themes for [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]]
  `kwin`                    Use the WM based on kwin
  `manual`                  Install [dde-extra/deepin-manual] User Manual
  `multimedia`              Install Deepin multimedia suite
  `mutter`                  Use the WM based on mutter
  `plymouth`                Install Deepin themes for [[[sys-boot/plymouth]](https://packages.gentoo.org/packages/sys-boot/plymouth)[]]
  `policykit`     Yes       Enable PolicyKit authentication support
  `screensaver`             Install Deepin Screensaver module
  `systemd`                 Run with [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")
  `terminal`      Yes       Install [dde-extra/deepin-terminal] Terminal Emulator
  `turbo`                   Enable DTK Apps Turbo by [dde-extra/deepin-turbo]
  --------------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For example, to add deepin multimedia suit to the default set of installed applications, do:

`root `[`#`]`mkdir -pv /etc/portage/package.use `

`root `[`#`]`echo "dde-base/dde-meta multimedia" >> /etc/portage/package.use/deepin `

** Note**\
The above assumes that [/etc/portage/package.use] is a directory, which is now the default on the Gentoo minimal install image. If using a single file instead, simply append to [/etc/portage/package.use] instead of [/etc/portage/package.use/deepin] in the above.

Then emerge DDE:

`root `[`#`]`emerge --ask --verbose --keep-going dde-base/dde-meta`

## [Configuring and running DDE]

Assuming that you have setup [X11](https://wiki.gentoo.org/wiki/X11 "X11") properly, now going to configure DDE.

### [Configuring lightdm greeter]

There are two greeter we can choose \-- [lightdm-gtk-greeter] and [lightdm-deepin-greeter]. But [lightdm-deepin-greeter] cannot run without any normal user, so we use [lightdm-gtk-greeter] by default.

[FILE] **`/etc/lightdm/lightdm.conf`**

    [Seat:*]
    greeter-session=lightdm-gtk-greeter

#### [Optional: adding a normal user]

If there isn\'t any normal user able to login in to your system, [lightdm-deepin-greeter] won't work. Then adding one and setting password. For instance, to create a user called [aten] who is member of the wheel, users, and audio groups:

`root `[`#`]`useradd -m -G users,wheel,audio -s /bin/bash aten `

`root `[`#`]`passwd aten `

    Password: (Enter the password for aten)
    Re-enter password: (Re-enter the password to verify)

### [Setting default services and running DDE]

#### [OpenRC]

##### [With display-manager]

The configuration file should be modified to use LightDM:

[FILE] **`/etc/conf.d/display-manager`Set LightDM as the display manager**

    CHECKVT=7
    DISPLAYMANAGER="lightdm"

Set [dbus], [display-manager], [[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager")], and [[elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind")] to come up on boot, and disable [[dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd")] if enabled.

`root `[`#`]`rc-update add dbus default `

`root `[`#`]`rc-update add display-manager default `

`root `[`#`]`rc-update add NetworkManager default `

`root `[`#`]`rc-update del dhcpcd default `

`root `[`#`]`rc-update add elogind boot `

Start DDE:

`root `[`#`]`rc-service dhcpcd stop `

`root `[`#`]`rc-service NetworkManager start `

`root `[`#`]`rc-service elogind start `

`root `[`#`]`rc-service display-manager start`

##### [With the deprecated xdm init script]

Change the `DISPLAYMANGER` value in the [xdm] configuration file to use [lightdm](https://wiki.gentoo.org/wiki/Lightdm "Lightdm").

[FILE] **`/etc/conf.d/xdm`**

    DISPLAYMANAGER="lightdm"

Set [dbus], [xdm], [[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager")], and [[elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind")] to come up on boot, and disable [[dhcpcd](https://wiki.gentoo.org/wiki/Dhcpcd "Dhcpcd")] if enabled.

`root `[`#`]`rc-update add dbus default `

`root `[`#`]`rc-update add xdm default `

`root `[`#`]`rc-update add NetworkManager default `

`root `[`#`]`rc-update del dhcpcd default `

`root `[`#`]`rc-update add elogind boot `

Start DDE:

`root `[`#`]`rc-service dhcpcd stop `

`root `[`#`]`rc-service NetworkManager start `

`root `[`#`]`rc-service elogind start `

`root `[`#`]`rc-service xdm start`

#### [systemd]

Enable [[NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager")] and [[lightdm](https://wiki.gentoo.org/wiki/Lightdm "Lightdm")] to be started at boot time:

`root `[`#`]`systemctl enable NetworkManager `

`root `[`#`]`systemctl enable lightdm `

Start and login:

`root `[`#`]`systemctl start NetworkManager `

`root `[`#`]`systemctl start lightdm `

## [Removal]

To remove DDE, begin by deselecting it:

`root `[`#`]`emerge --deselect dde-base/dde-meta`

Then, clean the package and its dependencies:

`root `[`#`]`emerge --ask --depclean`

Finally, remove all of the project overlays. For example, if using [eselect repository]:

`root `[`#`]`eselect repository remove deepin`

## [Troubleshooting]

If you discover any issues, or if you want to contribute, just create a [new issue](https://github.com/zhtengw/deepin-overlay/issues/new) on the [deepin ebuild repository](https://github.com/zhtengw/deepin-overlay) Github project or contact the [maintainer](mailto:atenzd@gmail.com).

## [External resources]

-   [Description of deepin-overlay](https://github.com/zhtengw/deepin-overlay/blob/master/README.md)
-   [DDE Installation Guide in deepin-overlay Wiki](https://github.com/zhtengw/deepin-overlay/wiki/Installing-Deepin-Desktop-Environment)
-   [Desktop Applications List provided by deepin-overlay](https://github.com/zhtengw/deepin-overlay/wiki/Applications-From-Deepin-Team)