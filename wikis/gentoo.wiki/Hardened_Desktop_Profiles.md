**Profiles**

**[Profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")**

[Structure](https://wiki.gentoo.org/wiki/Portage/Profiles/Structure "Portage/Profiles/Structure")

[Custom profiles](https://wiki.gentoo.org/wiki/Portage/Profiles/Custom_profiles "Portage/Profiles/Custom profiles")

[Switching profiles](https://wiki.gentoo.org/wiki/Portage/Profiles/Switching_profiles "Portage/Profiles/Switching profiles")

**Customized profiles**

[Hardened desktop profiles]

[Hardened Plasma profile](https://wiki.gentoo.org/wiki/KDE/Hardened_KDE_Plasma_profile "KDE/Hardened KDE Plasma profile")

[Hardened GNOME profiles](https://wiki.gentoo.org/wiki/GNOME/Guide/Hardened_GNOME_Profiles "GNOME/Guide/Hardened GNOME Profiles")

[Clang desktop profile](https://wiki.gentoo.org/wiki/LLVM/Clang/Desktop_profile "LLVM/Clang/Desktop profile")

[LTO profile](https://wiki.gentoo.org/wiki/LTO/LTO_profile "LTO/LTO profile")

A lot of people ask about combining the hardened and desktop profiles. Here\'s how!

## Contents

-   [[1] [GNOME and KDE]](#GNOME_and_KDE)
-   [[2] [Create a local repository]](#Create_a_local_repository)
    -   [[2.1] [Set up the repository layout]](#Set_up_the_repository_layout)
-   [[3] [Create the profile]](#Create_the_profile)
    -   [[3.1] [profiles.desc]](#profiles.desc)
    -   [[3.2] [The profile itself]](#The_profile_itself)
        -   [[3.2.1] [hardened-desktop]](#hardened-desktop)
        -   [[3.2.2] [hardened-desktop-systemd]](#hardened-desktop-systemd)
        -   [[3.2.3] [hardened-desktop-split-usr]](#hardened-desktop-split-usr)
-   [[4] [Selecting the profile]](#Selecting_the_profile)

## [GNOME and KDE]

For these desktop environments, please see [GNOME/Guide/Hardened_GNOME_Profiles](https://wiki.gentoo.org/wiki/GNOME/Guide/Hardened_GNOME_Profiles "GNOME/Guide/Hardened GNOME Profiles") and [KDE/Hardened_KDE_Plasma_profile](https://wiki.gentoo.org/wiki/KDE/Hardened_KDE_Plasma_profile "KDE/Hardened KDE Plasma profile").

## [Create a local repository]

A [local repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") is needed for the custom profile to be created.

First, install [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]]:

`root `[`#`]`emerge --ask app-eselect/eselect-repository`

Create a local repository:

`root `[`#`]`eselect repository create local`

### [Set up the repository layout]

It\'s recommended to make use of a [Portage extension](https://wiki.gentoo.org/wiki/Repository_format/metadata/layout.conf#profile-formats "Repository format/metadata/layout.conf") for the repository as it simplifies configuration.

[FILE] **`/var/db/repos/local/metadata/layout.conf`**

    masters = gentoo
    thin-manifests = true

    # Needed for profiles parent with repo syntax
    profile-formats = portage-2

## [Create the profile]

### [profiles.desc]

[profiles.desc] provides a list of profiles for [eselect profile list] to consume:

[FILE] **`/var/db/repos/local/profiles/profiles.desc`**

    # Adjust the list below as needed, no need to make them all
    amd64 hardened-desktop stable
    amd64 hardened-desktop-systemd stable
    amd64 hardened-desktop-split-usr stable

### [The profile itself]

Create the following directories (adjust as needed):

-   [/var/db/repos/local/profiles/hardened-desktop]
-   [/var/db/repos/local/profiles/hardened-desktop-systemd]
-   [/var/db/repos/local/profiles/hardened-desktop-split-usr]

Use the following command:

`root `[`#`]`mkdir -p /var/db/repos/local/profiles/`

#### [hardened-desktop]

Create the following files:

[FILE] **`/var/db/repos/local/profiles/hardened-desktop/eapi`**

    8

[FILE] **`/var/db/repos/local/profiles/hardened-desktop/parent`**

    gentoo:default/linux/amd64/23.0/hardened
    gentoo:targets/desktop

#### [hardened-desktop-systemd]

Create the following files:

[FILE] **`/var/db/repos/local/profiles/hardened-desktop-systemd/eapi`**

    8

[FILE] **`/var/db/repos/local/profiles/hardened-desktop-systemd/parent`**

    gentoo:default/linux/amd64/23.0/hardened
    gentoo:targets/desktop
    gentoo:targets/systemd

#### [hardened-desktop-split-usr]

Create the following files:

[FILE] **`/var/db/repos/local/profiles/hardened-desktop-split-usr/eapi`**

    8

[FILE] **`/var/db/repos/local/profiles/hardened-desktop-split-usr/parent`**

    gentoo:default/linux/amd64/23.0/hardened
    gentoo:features/split-usr
    gentoo:targets/desktop

## [Selecting the profile]

The new profiles should now appear in [eselect profile list]. Enjoy!