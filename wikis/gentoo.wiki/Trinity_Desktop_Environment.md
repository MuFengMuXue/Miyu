**Resources**

[[]][Home](https://trinitydesktop.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Trinity_Desktop_Environment "wikipedia:Trinity Desktop Environment")

[[]][Ebuild repository](https://mirror.git.trinitydesktop.org/gitea/TDE/tde-packaging-gentoo)

The **Trinity Desktop Environment** (**TDE**) is a free and open-source desktop environment forked from [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") 3.5. Due to the fact it is forked from an old version of KDE (which is itself a resource-heavy desktop environment) it is considered light-medium weight by today\'s standards.

\

** Note**\
Please don\'t report bugs to the Gentoo bugzilla, instead report issues at the [upstream repository](https://mirror.git.trinitydesktop.org/gitea/TDE/tde-packaging-gentoo/issues).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Installing TDE]](#Installing_TDE)
        -   [[1.1.1] [Profiles]](#Profiles)
        -   [[1.1.2] [Enabling the Overlay]](#Enabling_the_Overlay)
        -   [[1.1.3] [Emerge]](#Emerge)
    -   [[1.2] [Display Manager]](#Display_Manager)
        -   [[1.2.1] [TDM]](#TDM)
        -   [[1.2.2] [Emerge]](#Emerge_2)
        -   [[1.2.3] [Boot Service]](#Boot_Service)
        -   [[1.2.4] [systemd]](#systemd)
        -   [[1.2.5] [LightDM]](#LightDM)
    -   [[1.3] [Pipewire]](#Pipewire)
        -   [[1.3.1] [elogind]](#elogind)
        -   [[1.3.2] [Emerge]](#Emerge_3)
        -   [[1.3.3] [gentoo-pipewire-launcher]](#gentoo-pipewire-launcher)
        -   [[1.3.4] [pavucontrol]](#pavucontrol)

## [Installation]

### [Installing TDE]

#### [Profiles]

It is highly recommended to run a desktop profile when running a [Desktop Environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment"), using **[amd64]** as an example this can be done by running:

`root `[`#`]`eselect profile set default/linux/amd64/23.0/desktop`

`root `[`#`]`emerge -vauDU @world`

#### [Enabling the Overlay]

TDE is packaged in the trinity-official overlay. To enable this overlay:

`root `[`#`]`eselect repository add trinity-official git `[`https://mirror.git.trinitydesktop.org/gitea/TDE/tde-packaging-gentoo.git`](https://mirror.git.trinitydesktop.org/gitea/TDE/tde-packaging-gentoo.git)

To add this overlay manually:

[FILE] **`/etc/portage/repos.conf/tde.conf`**

    [trinity-official]
    location = /var/db/repos/trinity-official
    sync-type = git
    sync-uri = https://mirror.git.trinitydesktop.org/gitea/TDE/tde-packaging-gentoo.git
    auto-sync = yes

Sync the overlay with emaint:

`root `[`#`]`emaint sync -r trinity-official`

The packages on the overlay are keyworded under the unstable \~amd64 keyword, so users on a stable system should unmask the packages on the repository.

[FILE] **`/etc/portage/package.accept_keywords/trinity-official`**

    */*::trinity-official ~amd64

#### [Emerge]

To install the Trinity Desktop Environment meta package run the following command:

`root `[`#`]`emerge --ask trinity-base/tdebase-meta`

### [Display Manager]

#### [TDM]

Trinity Desktop Environment has a matching display manager called TDM.

#### [Emerge]

To install the Trinity Display Manager package run the following command:

`root `[`#`]`emerge --ask trinity-base/tdm`

Change your Display manager to \"tdm.\" An example for **display-manager-init** users:

[FILE] **`/etc/conf.d/display-manager`**

    DISPLAYMANAGER="tdm"

#### [Boot Service]

To start TDM on boot, add display-manager to the default runlevel:

`root `[`#`]`rc-update add display-manager default`

To start TDM now:

`root `[`#`]`rc-service display-manager start`

#### [systemd]

To start TDM on boot, run the following:

`root `[`#`]`systemctl enable tdm.service`

And start the service:

`root `[`#`]`systemctl start tdm.service`

#### [LightDM]

Users not wishing to use TDM may instead install LightDM.

To install LightDM, run the following command:

`root `[`#`]`emerge --ask x11-misc/lightdm`

Enable the LightDM service.

`root `[`#`]`systemctl enable lightdm`

To start LightDM now:

`root `[`#`]`systemctl start lightdm`

### [Pipewire]

Trinity Desktop Environment does not pull in a sound server, so we will have to enable one ourselves.

#### [elogind]

First, ensure elogind is enabled:

`root `[`#`]`rc-update add elogind boot`

#### [Emerge]

Enable the pulseaudio and pipewire USE flags globally:

[FILE] **`/etc/portage/make.conf`**

    USE="pulseaudio pipewire"

Then, emerge PipeWire:

`root `[`#`]`emerge --ask media-video/pipewire`

#### [gentoo-pipewire-launcher]

Add gentoo-pipewire-launcher to your xprofile:

[FILE] **`~/.xprofile`**

    gentoo-pipewire-launcher &

#### [pavucontrol]

Trinity\'s default sound server application is unable to use pipewire, so you will want something like pavucontrol:

`root `[`#`]`emerge --ask media-sound/pavucontrol`

Reboot, and you should have sound.