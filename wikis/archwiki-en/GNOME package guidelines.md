# GNOME package guidelines

The GNOME packages on Arch Linux follow a certain schema.

## Source URL
GNOME packages normally follow two source URL scheme: a released tarball stored in GNOME's FTP server and a specific commit in the software's Git repository

## Using released tarball
When downloading a released tarball, you can get it from https://download.gnome.org using the following source array:

 source=("https://download.gnome.org/sources/$pkgname/${pkgver%.*}/$pkgname-$pkgver.tar.xz")

where {{ic|${pkgver%.*} }} returns the major.minor package version, by removing the suffix of  (which is the micro package version). E.g., if pkgver=3.28.0 then {{ic|${pkgver%.*} }} would return 3.28.

## Using a commit from Git repository
Another common practice is to use as source a specific commit from a GNOME software's source code git repository. It does not classify as a VCS package because Pacman's feature of setting specific commit (see ) makes PKGBUILD not follow latest development commits neither update the  field, using the source from the specified commit hash instead.

See a template below:
{{hc|1=PKGBUILD|2=
url="https://gitlab.gnome.org/GNOME/$pkgname"
makedepends=(git)
_commit=hash_of_a_commit  # tags/X.Y.Z
source=("git+${url}.git#commit=$_commit")
md5sums=('SKIP')

pkgver() {
  cd $pkgname
  git describe --tags | sed 's/-/+/g'
}
}}

Replace  with the Git commit hash desired, and replace the  statement to fit the needs of the package you are packaging (see VCS package guidelines#Git).

Please notice that since the source is downloaded with git, then  must be in makedepends and checksums must be set to , just like it would happen with any other VCS package. Using  function is highly recommended, so it sets  accordingly for the commit hash provided.

## Meson and GNU build systems
Historically GNOME used GNU Build System to build its applications. While there some currently active applications and many inactive applications that still use GNU Build System, most of currently active GNOME applications migrated to Meson Build System.

See Meson package guidelines for instructions that fits the packaging needs of most GNOME applications.

## GSettings schemas
GSettings are the current schemas used by GNOME applications, and can be accessed/read/edited using the GUI tool  or the CLI tool gsettings (provided by , which is most likely already installed as dependency). GSettings used to require some attention of the packager, but nowadays no intervention is required.

Some observations:
* Applications that use GSettings normally depends on GTK ( or later), so GSettings-related dependencies are normally already satisfied.
*  flag in  used to be required to avoid recompiling GSettings database on  function, but this no longer applies to GNOME applications for some time now, mainly in applications using Meson as build system.

## GConf schemas
Most GNOME packages migrated from GConf schemas to #GSettings schemas, but you may cross with an old and obsolete GNOME package to installs these GConf schemas. In these cases,  must be added to depends array.

Gconf schemas get installed in the system GConf database, which has to be avoided. Some packages provide a  flag for , which hardly ever works. However, gconftool-2 has a variable called  which you can set to tell gconftool-2 to not update any databases.

When creating packages that install GConf schema files, use

 make GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR="${pkgdir}" install

in the PKGBUILD's  function.

## ScrollKeeper documentation
GNOME applications do not use ScrollKeeper nowadays, but you might come across with a GTK2-based application with that documentation.

Since GNOME 2.20 there is no need to run any command for ScrollKeeper, as  reads its OMF files directly. scrollkeeper-update is a dummy these days. The only requirement is to include  to makedepends array.

You can disable documentation generation using  flag from .

## GTK icon cache
Many graphical GNOME applications install icons in the system, and those icons are included in an icon cache via the gtk-update-icon-cache tool. Every time an icon is added or remove, this tool is used to update the cache.

## .desktop files
Many packages install Freedesktop.org-compatible  files and register MimeType entries in them. These information is stored in a database that has to be updated on every addition or removal. This is the function of the update-desktop-database tool.

## AppStream and metainfo files
As many others, most GNOME applications adheres the Freedesktop.org's AppStream specification and provide a metainfo file so that a description of the application is shown in application centers, like  or Flathub.

GNOME applications usually validate metainfo files if appstream-util tool when  is called in check() function.  If  is not installed, this will simply prevent this particular validation from being executed (i.e. no error will interrupt the build process).

You can identify that appstream-util is used by the application using two methods:
* The first method is to look in the source code for appstream-util by running  or looking at  file;
* The other method is to read the build process looking for

Add  to checkdepends array to validate metainfo file.
