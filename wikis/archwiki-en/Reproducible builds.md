# Reproducible builds

Arch Linux is currently working on making all packages reproducible. This lets users and researchers verify the distributed packages from Arch Linux.

## Verification builds
## Repository vs. rebuild
An experimental rebuilderd instance has been setup on our own infrastructure with the Reproducible status page. Rebuilderd rebuilds our repository packages and checks if they are bit for bit identical. If they are not reproducible there is either a bug in the tooling, the package is not reproducible or the package has not been built cleanly.

A list of known issues is located on /Status.

## Rebuild vs. another rebuild with variations
The Reproducible Builds project rebuilds Arch Linux packages and compares them with another rebuild in a different environment. The package status and environment variations are listed on the Reproducible status page.

## Helping out
## Tooling
Help out on fixing bugs and adding features for repro.

## Running a Rebuilder instance
Setting up rebuilderd to build Arch Linux packages helps to independently verify repository packages.

## Verifying packages with repro and finding issues
A great way to help out is to find an unreproducible package and figuring out how it can be made reproducible:

* Download an Arch Linux package or get one from the Arch Linux Archive.
* Run repro on the downloaded package or a package from your pacman cache. Ideally with  to get diffoscope output. For example, .
:
* Investigate if it is an issue with Arch Linux packaging or upstream, issues can be added on the status page. More information can be found on the Reproducible Builds website.

## Work on issues in the tests.reproducible-builds.org infrastructure
Arch users can help contribute to Reproducible Build issues by looking at the continuous reproducing environment (Reproducible status page). There are various issues which can be sorted out:

* Failed to build from source (FTBS): reproduce the build failure locally and create a bug report if the package cannot be built from a clean chroot ( or ).
* Failed to download sources, reproduce the issue () and create a bug report on the Arch GitLab.
* Failed to reproduce. Locally you can reproduce packages using . Note that not all variations can be used. For simple time related testing:

There might be various reasons for a package to not be reproducible, but before digging in take a look at the upstream repository or the reproducible status in Debian

* Failed to run tests, these failures are heavily on the testing environment. Most likely due to to  being set and Arch not supporting .

If you are interested in the code which runs the continuous reproducing environment, the first build code starts here on salsa.

## Known issues
## GPG verification
There is a possible rebuild scenario where GPG keys will not verify as the packager was removed from the keyring or revoked as we use the latest keyring and a package in the archive which we need might need be signed by a revoked key we are unable to verify it and the build will fail.

## Contact
* #archlinux-reproducible — Main channel for the progress of Reproducible Builds on Arch Linux
