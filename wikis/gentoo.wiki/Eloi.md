**Resources**

[[]][GitHub](https://github.com/mbaraa/eloi/)

**Eloi** is an ebuild searcher and installer ([eix](https://wiki.gentoo.org/wiki/Eix "Eix") with extra steps). Searches through all Gentoo\'s overlays provided by eselect repository and listed by Zugania\'s website.

Eloi can:

1.  Find and install an ebuild package from any overlay
2.  Enable ebuild overlays
3.  More in the future\...

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Go\'s Installer]](#Go.27s_Installer)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Update local repositories\' cache]](#Update_local_repositories.27_cache)
    -   [[2.2] [Find an ebuild]](#Find_an_ebuild)
    -   [[2.3] [Enable an overlay repository]](#Enable_an_overlay_repository)

## [Installation]

### [Emerge]

First, add the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") from here: [https://github.com/mbaraa/gentoo-overlay](https://github.com/mbaraa/gentoo-overlay).

Install **app-portage/eloi** using emerge:

`root `[`#`]`emerge --ask app-portage/eloi`

### [][Go\'s Installer]

`user `[`$`]`go install github.com/mbaraa/eloi@latest`

## [Usage]

### [][Update local repositories\' cache]

These cache files are stored in [/var/cache/eloi]:

`root `[`#`]`eloi --download`

### [Find an ebuild]

Using the `-S` or `--search` flag to find an ebuild, this will list all ebuilds that have `pulseaudio-equalizer` in their name, with other details, like version, overlay name, use flags, license:

`root `[`#`]`eloi -S pulseaudio-equalizer`

Or:

`root `[`#`]`eloi --search pulseaudio-equalizer`

### [Enable an overlay repository]

This can be done using the `--enable` flag:

`root `[`#`]`eloi --enable underworld`

Or by installing a package from a repository that\'s not enabled on the system, for now just search for a package and install it, and **Eloi** will add its corresponding repository!