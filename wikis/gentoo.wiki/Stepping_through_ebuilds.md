This article discusses how to step through an [ebuild](https://devmanual.gentoo.org/ebuild-writing/index.html) within their [Local Overlay](https://wiki.gentoo.org/wiki/Ebuild_repository/Local_overlay "Ebuild repository/Local overlay"). When emerging a package, Portage executes `ebuild` which steps through a series of build phases that retrieve the the source code, configure and compile it into an installable package which it can then be merged into the system.

## [Phases]

**Clean**

Cleans up partially built packages.

**Manifest**

Rebuilds the package manifest (See [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") manifest).

**Prepare**

Collects and unpacks the source code into the work folder, `/var/tmp/portage/CATEGORY/PACKAGE/work`.

**Compile**

Compiles the source code into a binary.

**Install**

Generates a package from the build artifacts.

**Merge**

Merges (installs) the package onto the system.

See the ebuild man page, `man ebuild`, for a \"complete\" listing of these commands.

### [Debugging]

To resolve an issue with an ebuild, it is possible to step into the source before building it as follows:

    cd /var/db/repos/local/CATEGORY/PACKAGE
    ebuild /CATEGORY/PACKAGE clean prepare
    pushd /var/tmp/portage//CATEGORY/PACKAGE/work/
    # Resolve the issue
    popd
    # Attempt the build issue
    ebuild /CATEGORY/PACKAGE compile
    # Package the build
    ebuild /CATEGORY/PACKAGE install
    # Merge the build into ones system
    ebuild /CATEGORY/PACKAGE merge