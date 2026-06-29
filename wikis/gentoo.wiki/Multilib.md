Multilib is one of the solutions allowing users to run applications built for various [application binary interfaces](https://en.wikipedia.org/wiki/Application_binary_interface "wikipedia:Application binary interface") (ABIs) of the same architecture. The most common use of multilib is to run 32-bit applications on **[amd64]**.

The multilib systems use separate library directories for non-native ABIs. This allows having the same library installed in variants for each ABI, as necessary to satisfy the dependencies of programs built for the ABI in question.

## Contents

-   [[1] [Multilib library providers in Gentoo]](#Multilib_library_providers_in_Gentoo)
-   [[2] [Comparison of multilib approaches]](#Comparison_of_multilib_approaches)
-   [[3] [See also]](#See_also)
    -   [[3.1] [Documentation for developers]](#Documentation_for_developers)
    -   [[3.2] [Historical documentation]](#Historical_documentation)

## [Multilib library providers in Gentoo]

There are currently three ways of providing multilib libraries in Gentoo:

-   Using emul-linux-x86 packages (32-bit libraries for **[amd64]** only). (obsolete and removed)
-   Using the eclasses provided by the [gx86-multilib](https://wiki.gentoo.org/wiki/Gx86-multilib "Gx86-multilib") project. (Current implementation)
-   Using the multilib-portage fork.

## [Comparison of multilib approaches]

** Note**\
The table explains the current state as of 2013-11-16. It does not imply any limitations on further developments.

  ------------------------------------------ ------------------------------------------------------------- ----------------------------------------------------------------------------------------------- --------------------------------------------------------
                                             emul-linux                                                    [gx86-multilib](https://wiki.gentoo.org/wiki/Multilib/gx86-multilib "Multilib/gx86-multilib")   multilib-portage
  Supported ABIs                             x86 only                                                      any                                                                                             any
  Provision method                           binary packages                                               source build                                                                                    source build
  Method of introducing                      dedicated ebuilds                                             eclasses + changes in library ebuilds                                                           changes in package manager
  Inter-package dependencies                 explicit emul-linux package deps                              explicit USE dependencies                                                                       implicit
  Cost of introduction                       low (committing ebuilds)                                      medium (eclasses + changing a number of existing ebuilds                                        high (changing package managers and specification)
  Cost of adding libraries                   low (building a new package)                                  medium (changing the native library ebuild)                                                     none (implicit)
  Cost of maintenance                        medium (rebuilding the emul- set for new versions of libs)    low (bumping the ebuilds)                                                                       none (implicit)
  Cost of changing (fixing) implementation   low (rebuild the set)                                         medium (fixing eclasses and/or ebuilds)                                                         very high (needs new EAPI)
  Security implications                      security issues need to be handled separately                 handled along with the native version                                                           handled implicitly by the native version
  Supported libraries                        limited set with a single version of each                     limited set with free version choice                                                            any
  Support USE flags (choices)                very limited due to intra-library dependencies                USE flags common to native and multilib build                                                   USE flags common to native and multilib build
  Extra fetching                             binary packages                                               no                                                                                              no
  Extra build time                           no                                                            depending on build system limitations, some things may be built multiple times unnecessarily    the complete build process is run multiple times
  Extra dependencies                         no                                                            no                                                                                              every build-time tool need to become multilib as well
  ------------------------------------------ ------------------------------------------------------------- ----------------------------------------------------------------------------------------------- --------------------------------------------------------

## [See also]

### [Documentation for developers]

-   [Concepts](https://wiki.gentoo.org/wiki/Multilib/Concepts "Multilib/Concepts")
-   [Eclasses](https://wiki.gentoo.org/wiki/Multilib/Eclasses "Multilib/Eclasses")
    -   [multilib-build](https://wiki.gentoo.org/wiki/Multilib/multilib-build "Multilib/multilib-build")
    -   [multilib-minimal](https://wiki.gentoo.org/wiki/Multilib/multilib-minimal "Multilib/multilib-minimal")
    -   [cmake-multilib](https://wiki.gentoo.org/index.php?title=Multilib/cmake-multilib&action=edit&redlink=1 "Multilib/cmake-multilib (page does not exist)")
-   [Tips & tricks](https://wiki.gentoo.org/wiki/Multilib/Tips_%26_tricks "Multilib/Tips & tricks")
-   [Adding new ABIs](https://wiki.gentoo.org/wiki/Multilib/Adding_new_ABIs "Multilib/Adding new ABIs")

### [Historical documentation]

-   [Roadmap](https://wiki.gentoo.org/wiki/Multilib/RoadMap "Multilib/RoadMap")