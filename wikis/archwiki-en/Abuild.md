# Abuild

The abuild tooling provides necessary scripts to build and maintain Alpine Linux packages.

It can be used to maintain and build Alpine packages (in an Alpine clean chroot) from an Arch Linux system, without requiring to rely on a separate Alpine installation, such as a container or a VM.

Due to technical differences between Alpine and Arch Linux (e.g. in terms of package manager, init system and C library implementation), building Alpine packages on an Arch system outside of an Alpine clean chroot is not possible. As such, when building Alpine packages on an Arch system, only  is relevant to use.

## Installation
Install the  package.

The  package provides additional tools like  and  that may also be of interest (see #Usage).

## Configuration
abuild subcommands that are not about building packages should be usable right out of the box (e.g. generating / updating checksums, fetch sources, cleaning temporary directories, ... see the ).

To be able to build Alpine packages in an Alpine clean chroot, you need to generate a public / private rsa key pair with the abuild-keygen tool and add your user to the  user group (which is created when installing the  package):

 $ abuild-keygen -a -i

One can optionally edit the  configuration file to their liking and requirements. For instance, the paths used to store downloaded sources ( by default) and built packages ( by default) can be customized by modifying the  and  parameters respectively in that configuration file.

The  and  parameters are used by  when creating new aports for the APKBUILD's "Contributor:" and "Maintainer:" comments, respectively.

## Usage
A basic packaging workflow example using the abuild and atools tooling would start by creating a new port for a package and entering its directory:

 $ newapkbuild package_name && cd package_name

The next step would be editing the APKBUILD, then  running the apkbuild linter (provided by the  package):

 $ apkbuild-lint APKBUILD

One could then run the apkbuild fixer to attempt to automatically fix potential warnings raised by apkbuild-lint (provided by the  package):

 $ apkbuild-fixer APKBUILD

Afterwards, generate / upgrade checksum for the source(s) contained in the APKBUILD source array:

 $ abuild checksum

Finally, build the package in an Alpine clean chroot:

 $ abuild rootbld

See Alpine Linux Wiki's "Abuild and Helpers" page for more details and usage examples.
