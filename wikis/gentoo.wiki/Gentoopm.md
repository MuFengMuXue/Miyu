**Resources**

[[]][GitHub](https://github.com/projg2/gentoopm)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/gentoopm)

[[]][Bugs (upstream)](https://bugs.gentoo.org/)

**gentoopm** is a common interface to Gentoo package managers written in Python. It currently supports [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") and [pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore").

The project provides a [gentoopmq] tool providing basic lookups into the package manager data. Most importantly, it provides an IPython-friendly [gentoopmq shell] command that can be used to play with the API.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Example use]](#Example_use)
    -   [[2.1] [Check if www-client/firefox is installed]](#Check_if_www-client.2Ffirefox_is_installed)
    -   [[2.2] [Get names of all installed packages]](#Get_names_of_all_installed_packages)
    -   [[2.3] [Compare two versions of a package]](#Compare_two_versions_of_a_package)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/gentoopm](https://packages.gentoo.org/packages/app-portage/gentoopm) [[]] [A common interface to Gentoo package managers]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-21 18:40] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install gentoopm:

`root `[`#`]`emerge --ask app-portage/gentoopm`

## [Example use]

### [][Check if [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] is installed]

[CODE]

    import gentoopm

    pm = gentoopm.get_package_manager()
    if "www-client/firefox" in pm.installed:
        print("Firefox is installed!")

### [Get names of all installed packages]

[CODE]

    inst = frozenset(str(pkg.key) for pkg in pm.installed)
    print(*sorted(inst), sep="\n")

### [Compare two versions of a package]

[CODE]

    pkg1 = pm.Atom("=www-client/firefox-90")
    pkg2 = pm.Atom("=www-client/firefox-100")
    assert pkg1.version < pkg2.version