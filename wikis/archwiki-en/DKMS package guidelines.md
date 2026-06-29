# DKMS package guidelines

Here are some guidelines to follow when creating a DKMS package.

## Package name
DKMS packages are named by appending "-dkms" to the original package name.

The variable  is often used below  to describe the package name minus the "-dkms" suffix (e.g. {{ic|1=_pkgname="${pkgname%-*}"}})

## Dependencies
Add  to  array. This is important because this will provide tools and hooks that will rebuild the kernel driver provided by the -dkms package whenever the kernel is updated.

Do not include  – or any other Linux header package – to the PKGBUILD. These headers are already listed as optional dependencies of  and each kernel package has its own header package, so including header package dependency in the -dkms package is both unnecessarily redundant and restricting.

## Source location
The package should install the kernel module's source files into:

 /usr/src/PACKAGE_NAME-PACKAGE_VERSION

where  and  are the kernel module's name and version.

It is highly recommended to set  with the value of  (See #Package name), and  with .

## Patching
The sources can be patched either directly in the PKGBUILD or through .

If patching through , make sure to install the patches into  directory and to add a  for each patch to be applied, replacing  with a incremental value starting at . See  for more information.

## Module loading automatically in .install
Do not use .install file to load or unload modules. Leave it to the user, since there is a possibility a module may crash when loaded.

Also do not call dkms as it is automatically done via pacman hook provided by . This hook runs  and  leaving no manual task for the package maintainer.

## Example
Here is an example package that edits  according to the package name and version, and install module blacklist configuration file.

For other example of (real) packages, search -dkms in official repositories and -dkms in AUR.

## PKGBUILD
{{hc|PKGBUILD|2=
# Maintainer: foo
# Contributor: bar

_pkgbase=example
pkgname=example-dkms
pkgver=1
pkgrel=1
pkgdesc="The Example kernel modules (DKMS)"
arch=('x86_64')
url="https://www.example.org/"
license=('GPL2')
depends=('dkms')
conflicts=("${_pkgbase}")
install=${pkgname}.install
source=("${url}/files/tarball.tar.gz"
        'dkms.conf'
        "${pkgname}.conf"
        'linux-3.14.patch')
md5sums=(use 'updpkgsums)

prepare() {
  cd ${_pkgbase}-${pkgver}

  # Patch
  patch -p1 -i "${srcdir}"/linux-3.14.patch
}

package() {
  # Copy dkms.conf
  install -Dm644 dkms.conf "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/dkms.conf

  # Set name and version
  sed -e "s/@_PKGBASE@/${_pkgbase}/" \
      -e "s/@PKGVER@/${pkgver}/" \
      -i "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/dkms.conf

  # Copy sources (including Makefile)
  cp -r ${_pkgbase}/* "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/

  # Blacklists conflicting module
  install -Dm644 ${pkgname}.conf "${pkgdir}/usr/lib/modprobe.d/${pkgname}.conf"
}
}}

## dkms.conf
## .install
This example shows a message on post-install and post-upgrade that suggests unloading a conflicting module () and then loading this package's module () for immediate use, when the user do not want to reboot the system at this moment.

{{hc|example.install|
post_install() {
  cat<<EOF

Unload and load kernel modules:

  rmmod example-conflicting-module
  modprobe example

EOF
}

post_upgrade() {
  post_install
}
}}

## Module blacklist conf
When it is known that  conflicts with this package's  module, it should be blacklisted:
