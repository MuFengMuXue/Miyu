**Resources**

[[]][GitHub](https://github.com/mgorny/gemato)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/gemato)

Gemato (**Ge**ntoo **Ma**nifest **To**ol) is a stand-alone utility to verify and update [Manifest](https://wiki.gentoo.org/wiki/Repository_format/package/Manifest "Repository format/package/Manifest") files distributed in the Gentoo [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Verifying the Gentoo ebuild repository]](#Verifying_the_Gentoo_ebuild_repository)
-   [[3] [Removal]](#Removal)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/gemato](https://packages.gentoo.org/packages/app-portage/gemato) [[]] [Stand-alone Manifest generation & verification tool]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+gpg`](https://packages.gentoo.org/useflags/+gpg)               Install dependencies needed for OpenPGP signature verification support
  [`pretty-log`](https://packages.gentoo.org/useflags/pretty-log)   Pull dev-python/rich to enable pretty logs
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tools`](https://packages.gentoo.org/useflags/tools)             Install additional utilities (benchmarks, hash testing tools, fast Manifest generators) to /usr/share/gemato.
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 06:27] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Usage]

### [Invocation]

`user `[`$`]`gemato --help`

    usage: /usr/lib/python-exec/python3.7/gemato [-h]

                                                 ...

    Gentoo Manifest Tool

    positional arguments:

        verify              Verify one or more directories against Manifests
        update              Update the Manifest entries for one or more directory
                            trees
        create              Create a Manifest tree starting at the specified file
        hash                Generate hashes for specified file(s) and/or stdin
        openpgp-verify      Verify OpenPGP signatures embedded in specified
                            file(s) and/or stdin

    optional arguments:
      -h, --help            show this help message and exit

### [Verifying the Gentoo ebuild repository]

To manually verify the main ebuild repository:

`user `[`$`]`gemato verify -K /usr/share/openpgp-keys/gentoo-release.asc /var/db/repos/gentoo`

    INFO:root:Refreshing keys...
    INFO:root:Keys refreshed.
    INFO:root:Manifest timestamp: 2020-05-25 00:38:25 UTC
    INFO:root:Valid OpenPGP signature found:
    INFO:root:- primary key: DCD05B71EAB94199527F44ACDB6B8C1F96D8BF6D
    INFO:root:- subkey: E1D6ABB63BFCFB4BA02FDF1CEC590EEAC9189250
    INFO:root:- timestamp: 2020-05-25 00:38:25 UTC
    INFO:root:Verifying /var/db/repos/gentoo...
    INFO:root:/var/db/repos/gentoo verified in 36.65 seconds

If the command exits with \"verified\" message, then the repository integrity has been successfully confirmed as valid.

## [Removal]

Gemato should *never* be removed from the system since it is necessary for correct operation of Portage.

## [See also]

-   [Project:Portage/Repository verification](https://wiki.gentoo.org/wiki/Project:Portage/Repository_verification "Project:Portage/Repository verification") --- describes different methods used to ensure authenticity of the Gentoo ebuild repository.
-   [Portage Security](https://wiki.gentoo.org/wiki/Portage_Security "Portage Security") --- aims to answer the question *\"How can I dispel doubts regarding the security of the Gentoo ebuild repository on a system?\"*