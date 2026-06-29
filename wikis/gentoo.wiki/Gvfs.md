[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=GVfs&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/gnome-base/gvfs)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GVfs "wikipedia:GVfs")

[[]][GitLab](https://gitlab.gnome.org/GNOME/gvfs)

[[]][Bugs (upstream)](https://gitlab.gnome.org/GNOME/gvfs/-/issues)

**GVfs** is a virtual file system for mounting local, and remote file systems.

## [Installation]

### [USE Flags]

### [USE flags for] [gnome-base/gvfs](https://packages.gentoo.org/packages/gnome-base/gvfs) [[]] [Virtual filesystem implementation for GIO]

  --------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+gcr`](https://packages.gentoo.org/useflags/+gcr)                                     Enables keystore handling using app-crypt/gcr
  [`+http`](https://packages.gentoo.org/useflags/+http)                                   Enable the HTTP/DAV backend using net-libs/libsoup
  [`+sftp`](https://packages.gentoo.org/useflags/+sftp)                                   Enable SFTP client support via virtual/openssh
  [`+udev`](https://packages.gentoo.org/useflags/+udev)                                   Enable udev base replacement code for cdda feature
  [`afp`](https://packages.gentoo.org/useflags/afp)                                       Enables support for accessing AFP (Apple Filing Protocol) network shares
  [`archive`](https://packages.gentoo.org/useflags/archive)                               Enables support for accessing files in archives transparently via app-arch/libarchive
  [`bluray`](https://packages.gentoo.org/useflags/bluray)                                 Enable playback of Blu-ray filesystems using media-libs/libbluray
  [`cdda`](https://packages.gentoo.org/useflags/cdda)                                     Add Compact Disk Digital Audio (Standard Audio CD) support
  [`cdr`](https://packages.gentoo.org/useflags/cdr)                                       Add support for CD writer hardware
  [`elogind`](https://packages.gentoo.org/useflags/elogind)                               Enable session tracking via sys-auth/elogind
  [`fuse`](https://packages.gentoo.org/useflags/fuse)                                     Enables fuse mount points in \$HOME/.gvfs for legacy application access
  [`gnome-online-accounts`](https://packages.gentoo.org/useflags/gnome-online-accounts)   Enable configuration panel for net-libs/gnome-online-accounts accounts
  [`google`](https://packages.gentoo.org/useflags/google)                                 Enables support for accessing Google accounts via dev-libs/libgdata
  [`gphoto2`](https://packages.gentoo.org/useflags/gphoto2)                               Add digital camera support
  [`ios`](https://packages.gentoo.org/useflags/ios)                                       Enable support for Apple\'s iDevice with iOS operating system (iPad, iPhone, iPod, etc)
  [`keyring`](https://packages.gentoo.org/useflags/keyring)                               Enable support for freedesktop.org Secret Service API password store
  [`mtp`](https://packages.gentoo.org/useflags/mtp)                                       Enable support for Media Transfer Protocol
  [`nfs`](https://packages.gentoo.org/useflags/nfs)                                       Enable NFS client support via net-fs/libnfs
  [`onedrive`](https://packages.gentoo.org/useflags/onedrive)                             Enable Onedrive backend via net-libs/msgraph
  [`policykit`](https://packages.gentoo.org/useflags/policykit)                           Enable PolicyKit (polkit) authentication support
  [`samba`](https://packages.gentoo.org/useflags/samba)                                   Add support for SAMBA (Windows File and Printer sharing)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                               Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`udisks`](https://packages.gentoo.org/useflags/udisks)                                 Enable storage management support (automounting, volume monitoring, etc)
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)                             Support for DNS Service Discovery (DNS-SD)
  --------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-16 12:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[gnome-base/gvfs]](https://packages.gentoo.org/packages/gnome-base/gvfs)[]]:

`root `[`#`]`emerge --ask gnome-base/gvfs`