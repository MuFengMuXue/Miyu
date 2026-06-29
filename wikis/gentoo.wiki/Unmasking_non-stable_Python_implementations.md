`PYTHON_TARGETS` and `PYTHON_SINGLE_TARGET` are [`USE_EXPAND`](https://wiki.gentoo.org/wiki/USE_EXPAND "USE EXPAND") variables controlling support for various Python implementations (versions) in packages. These essentially control what version of Python the package will reference during and after installation.

## [Enabling Python implementations]

The modern packages (using [-r1 suite eclasses](https://wiki.gentoo.org/wiki/Project:Python/Eclasses#-r1_eclasses "Project:Python/Eclasses")) use explicit USE flags aggregated in `PYTHON_TARGETS` and `PYTHON_SINGLE_TARGET` `USE_EXPAND` variables. The variables are defaulted in profiles and can be changed in [make.conf]. The flags may be adjusted per-package using [package.use] as well.

The `PYTHON_TARGETS` variable is used for packages that support enabling more than a single Python implementation. Therefore, the variable may contain any number of implementations.

The `PYTHON_SINGLE_TARGET` variable is used for packages that are built for a single implementation of choice only. It may contain only a single implementation. Due to technical limitations, the implementation specified as `PYTHON_SINGLE_TARGET` must also be included in `PYTHON_TARGETS` for the package in question.

The possible values are listed in the `PYTHON_COMPAT` column of the Python project\'s [implementations list](https://wiki.gentoo.org/wiki/Project:Python/Implementations "Project:Python/Implementations").

[FILE] **`/etc/portage/package.use`Examples of PYTHON_TARGETS/PYTHON_SINGLE_TARGET**

    # Enabling additional implementation in addition to the profile default
    */* PYTHON_TARGETS: python3_7
    # Replacing the profile default with specific implementation
    */* PYTHON_SINGLE_TARGET: -python3_6 python3_7
    # Build vim for python2.7 instead of the above
    # (note: -* in PYTHON_TARGETS is optional but it makes it possible to avoid extraneous deps
    app-editors/vim PYTHON_TARGETS: -* python2_7 PYTHON_SINGLE_TARGET: -* python2_7
    # Enable all Python implementation for Portage
    sys-apps/portage PYTHON_TARGETS: *

## [Unmasking non-stable implementation on a stable system]

If you\'d like to use an implementation that is not stable on your architecture on a stable system, you need to:

1.  Unmask the implementation using [/etc/portage/package.accept_keywords],
2.  Unmask the relevant USE flags using [/etc/portage/profile/use.stable.mask]. This also requires to set [/etc/portage/profile] to EAPI \>= 5.

[FILE] **`/etc/portage/package.accept_keywords`Unmasking Python 3.5**

    dev-lang/python:3.5

[FILE] **`/etc/portage/profile/use.stable.mask`Unmasking flags for Python 3.5**

    -python_targets_python3_5
    -python_single_target_python3_5

[FILE] **`/etc/portage/profile/eapi`Setting eapi 5**

    5