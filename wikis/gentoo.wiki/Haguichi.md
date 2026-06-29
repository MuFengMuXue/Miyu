**Resources**

[[]][Home](https://www.haguichi.net)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Hamachi_(software) "wikipedia:Hamachi (software)")

Haguichi is a graphical front-end to [Hamachi](https://wiki.gentoo.org/wiki/Hamachi "Hamachi"), a VPN tunneling engine.

** Note**\
Currently no ebuild exist for haguichi, therefore this article provides instructions on manually building and installing the package.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Kernel configuration]](#Kernel_configuration)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [See also]](#See_also)

## [Installation]

## [Kernel configuration]

The kernel must support tunneling.

[KERNEL] **Enabling `CONFIG_TUN` in the kernel**

    Device Drivers -->
       Network device support -->
          <*> Universal TUN/TAP device driver support

### [Emerge]

First unmask and emerge Hamachi, the VPN engine:

`root `[`#`]`echo "net-vpn/logmein-hamachi ~amd64" >> /etc/portage/package.accept_keywords`

`root `[`#`]`emerge --ask net-vpn/logmein-hamachi`

Haguichi requires mono and gtk-sharp. Emerge them in one fell swoop:

`root `[`#`]`emerge --ask dev-lang/mono dev-dotnet/gtk-sharp dev-dotnet/notify-sharp dev-dotnet/gconf-sharp dev-dotnet/ndesk-dbus dev-dotnet/ndesk-dbus-glib`

Then nab the Haguichi tarball:

`user `[`$`]`wget http://launchpad.net/haguichi/1.0/1.0.20/+download/haguichi-1.0.20-clr4.0.tar.gz`

Untar the file, and go into the resulting directory:

`user `[`$`]`tar -xf haguichi*.tar.gz && cd haguichi*`

Then build and install the package:

`user `[`$`]`./configure --prefix=/usr && make && su -c 'make install'`

## [See also]

-   [Hamachi](https://wiki.gentoo.org/wiki/Hamachi "Hamachi") --- a cross platform VPN tunneling engine.