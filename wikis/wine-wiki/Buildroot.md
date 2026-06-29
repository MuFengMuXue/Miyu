# Buildroot

[Buildroot](https://buildroot.org/) is a simple, efficient and
easy-to-use tool to generate embedded Linux systems through
cross-compilation. With a set of Makefiles and patches you can generate
any or all of a cross- toolchain, a rootfs, a kernel image and a
bootloader image.

Since 2015.05 it has support for stable Wine. It can easily be used to
test Wine on different architectures, just replace the Wine version with
the version you like and select needed packages.

## Usage

1.  [Get Buildroot](https://buildroot.org/download.html)
2.  Change to the root folder of the Buildroot source
3.  cp configs/qemu_x86_defconfig .config \# to get a basic x86
    configuration
4.  make menuconfig
5.  Toolchain → C library → glibc \# Wine needs glibc for now
6.  Target packages → Miscellaneous → wine
7.  Build options → Number of jobs to run simultaneously (0 for auto) \#
    Adjust number as needed, 1 for no multiprocess building
8.  Exit and say yes to save configuration
9.  make \# don't do a make -j2 here, adjust number above
10. Do the laundry and grab a coffee as it now downloads everything
    needed and even compiles a toolchain and a Kernel
11. In file board/qemu/x86/readme.txt you'll find how to run the result

You'll now have a bare Linux system with Wine installed, but you'll
notice that not everything is compiled in. The reason is that
dependencies are not selected automatically for Wine as this would
really be too much.

So you either select the packages yourself or use this configuration
file:

```
BR2_x86_core2=y
BR2_JLEVEL=1
BR2_OPTIMIZE_2=y
BR2_TOOLCHAIN_BUILDROOT_GLIBC=y
BR2_TOOLCHAIN_BUILDROOT_CXX=y
BR2_TARGET_GENERIC_GETTY_PORT="tty1"
BR2_PACKAGE_GST_PLUGINS_BASE=y
BR2_PACKAGE_MPG123=y
BR2_PACKAGE_MESA3D=y
BR2_PACKAGE_MESA3D_GALLIUM_DRIVER_SWRAST=y
BR2_PACKAGE_MESA3D_DRI_DRIVER_SWRAST=y
BR2_PACKAGE_XORG7=y
BR2_PACKAGE_XSERVER_XORG_SERVER=y
BR2_PACKAGE_XLIB_LIBXCOMPOSITE=y
BR2_PACKAGE_XAPP_XEYES=y
BR2_PACKAGE_DBUS=y
BR2_PACKAGE_SANE_BACKENDS=y
BR2_PACKAGE_ALSA_LIB=y
BR2_PACKAGE_OPENAL=y
BR2_PACKAGE_GNUTLS=y
BR2_PACKAGE_LCMS2=y
BR2_PACKAGE_LIBGLU=y
BR2_PACKAGE_LIBPNG=y
BR2_PACKAGE_TIFF=y
BR2_PACKAGE_LIBV4L=y
BR2_PACKAGE_LIBXSLT=y
BR2_PACKAGE_OPENLDAP=y
BR2_PACKAGE_NCURSES_WCHAR=y
BR2_PACKAGE_WINE=y
BR2_PACKAGE_NANO=y
BR2_PACKAGE_MESA3D_OSMESA_CLASSIC=y
BR2_PACKAGE_LIBPCAP=y
BR2_PACKAGE_PULSEAUDIO=y
BR2_PACKAGE_GSTREAMER1=y
BR2_PACKAGE_GST1_PLUGINS_BASE=y
BR2_PACKAGE_SDL2=y
BR2_PACKAGE_CUPS=y
BR2_PACKAGE_LIBKRB5=y
BR2_TARGET_ROOTFS_TAR_LZO=y
```

(copy that to .config and run "make menuconfig" or "make nconfig"
afterwards)

For qemu user space emulation you also don't need a Kernel, and maybe
you have a toolchain you could use instead of letting it build one, just
look around in menuconfig and adjust as needed.

## Changing the Wine Version

Everything Wine related is in package/wine/

So adjust WINE_VERSION in package/wine/wine.mk and update or delete
package/wine/wine.hash

Note that newer Wine has new or different dependencies, you need to
adjust wine.mk even more to get a proper build. For example following
block is used to turn tiff support on/off depending on the package being
selected, but it also ensures that libtiff is built before Wine, which
is very important:

```
ifeq ($(BR2_PACKAGE_TIFF),y)
WINE_CONF_OPTS += --with-tiff
WINE_DEPENDENCIES += tiff
else
WINE_CONF_OPTS += --without-tiff
endif
```

## See also

- [WineConf 2015](WineConf/WineConf-2015)
