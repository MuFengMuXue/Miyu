** Warning**\
This page is no longer actively maintained and is kept for historical purposes only. emul-linux-x86 packages are gone, and there is no longer a need for an explicit *porting*. Instead, multilib support on additional packages can be enabled as necessary.

**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

\

## Contents

-   [[1] [Some information]](#Some_information)
-   [[2] [Legend]](#Legend)
-   [[3] [Emul-\* packages porting status]](#Emul-.2A_packages_porting_status)
    -   [[3.1] [emul-linux-x86-baselibs]](#emul-linux-x86-baselibs)
    -   [[3.2] [~~emul-linux-x86-compat~~]](#emul-linux-x86-compat)
    -   [[3.3] [emul-linux-x86-cpplibs]](#emul-linux-x86-cpplibs)
    -   [[3.4] [emul-linux-x86-db]](#emul-linux-x86-db)
    -   [[3.5] [~~emul-linux-x86-glibc-errno-compat~~]](#emul-linux-x86-glibc-errno-compat)
    -   [[3.6] [emul-linux-x86-gstplugins]](#emul-linux-x86-gstplugins)
    -   [[3.7] [emul-linux-x86-gtklibs]](#emul-linux-x86-gtklibs)
    -   [[3.8] [emul-linux-x86-gtkmmlibs]](#emul-linux-x86-gtkmmlibs)
    -   [[3.9] [emul-linux-x86-java]](#emul-linux-x86-java)
    -   [[3.10] [emul-linux-x86-jna]](#emul-linux-x86-jna)
    -   [[3.11] [emul-linux-x86-medialibs]](#emul-linux-x86-medialibs)
    -   [[3.12] [emul-linux-x86-motif]](#emul-linux-x86-motif)
    -   [[3.13] [emul-linux-x86-opengl]](#emul-linux-x86-opengl)
    -   [[3.14] [emul-linux-x86-qtlibs]](#emul-linux-x86-qtlibs)
    -   [[3.15] [emul-linux-x86-sdl]](#emul-linux-x86-sdl)
    -   [[3.16] [emul-linux-x86-soundlibs]](#emul-linux-x86-soundlibs)
    -   [[3.17] [emul-linux-x86-xlibs]](#emul-linux-x86-xlibs)
-   [[4] [Other packages porting status]](#Other_packages_porting_status)
    -   [[4.1] [Source packages]](#Source_packages)
    -   [[4.2] [Binary packages]](#Binary_packages)
-   [[5] [Profile fixing status]](#Profile_fixing_status)

### [Some information]

List of packages included in actual emul packages: [\[1\]](http://www.gentoo.org/proj/en/base/amd64/emul/emul-linux-x86-20140508.xml)

gx86 mulitilib tracker bug: [[[bug #454644]](https://bugs.gentoo.org/show_bug.cgi?id=454644)[]]

## [Legend]

  -------------- ---------------------------------------------------
  Text           Meaning
  DONE           Package is ported and available in testing/stable
  DONE           Package is ported but still masked
  IN PROGRESS    There is an open bug
  TODO           Not ported, no open bug
  -------------- ---------------------------------------------------

## [][Emul-\* packages porting status]

### [emul-linux-x86-baselibs]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                          Status   Notes
  [[[app-admin/gamin]](https://packages.gentoo.org/packages/app-admin/gamin)[]]                              DONE     was not really part of emul libs
  [[[app-arch/bzip2]](https://packages.gentoo.org/packages/app-arch/bzip2)[]]                                 DONE     \>=emul-linux-x86-baselibs-20130224-r1
  [[[app-crypt/mit-krb5]](https://packages.gentoo.org/packages/app-crypt/mit-krb5)[]]                     DONE     [[[bug #505004]](https://bugs.gentoo.org/show_bug.cgi?id=505004)[]]
  [[[app-text/libpaper]](https://packages.gentoo.org/packages/app-text/libpaper)[]]                        DONE     \>=emul-linux-x86-baselibs-20130224-r11
  [[[dev-db/sqlite]](https://packages.gentoo.org/packages/dev-db/sqlite)[]]                                    DONE     \>=emul-linux-x86-baselibs-20130224-r14
  [[[dev-lang/perl]](https://packages.gentoo.org/packages/dev-lang/perl)[]]                                    TODO
  [[[dev-lang/python]](https://packages.gentoo.org/packages/dev-lang/python)[]]                              TODO
  [[[dev-libs/dbus-glib]](https://packages.gentoo.org/packages/dev-libs/dbus-glib)[]]                     DONE     \>=emul-linux-x86-baselibs-20131008-r14
  [[[dev-libs/elfutils]](https://packages.gentoo.org/packages/dev-libs/elfutils)[]]                        DONE     \>=emul-linux-x86-baselibs-20130224-r12
  [[[dev-libs/expat]](https://packages.gentoo.org/packages/dev-libs/expat)[]]                                 DONE     \>=emul-linux-x86-baselibs-20130224-r7
  [[[dev-libs/glib]](https://packages.gentoo.org/packages/dev-libs/glib)[]]                                    DONE     \>=emul-linux-x86-baselibs-20130224-r10
  [[[dev-libs/gmp]](https://packages.gentoo.org/packages/dev-libs/gmp)[]]                                       DONE     \>=emul-linux-x86-baselibs-20131008-r2
  [[[dev-libs/json-c]](https://packages.gentoo.org/packages/dev-libs/json-c)[]]                              DONE     \>=emul-linux-x86-baselibs-20131008-r14
  [[[dev-libs/libffi]](https://packages.gentoo.org/packages/dev-libs/libffi)[]]                              DONE     \>=emul-linux-x86-baselibs-20130224-r2
  [[[dev-libs/libgcrypt]](https://packages.gentoo.org/packages/dev-libs/libgcrypt)[]]                     DONE     \>=emul-linux-x86-baselibs-20131008-r20
  [[[dev-libs/libgpg-error]](https://packages.gentoo.org/packages/dev-libs/libgpg-error)[]]            DONE     \>=emul-linux-x86-baselibs-20131008-r14
  [[[dev-libs/libnl]](https://packages.gentoo.org/packages/dev-libs/libnl)[]]                                 DONE
  [[[dev-libs/libpcre]](https://packages.gentoo.org/packages/dev-libs/libpcre)[]]                           DONE     \>=emul-linux-x86-baselibs-20131008-r3
  [[[dev-libs/libtasn1]](https://packages.gentoo.org/packages/dev-libs/libtasn1)[]]                        DONE     \>=emul-linux-x86-baselibs-20131008-r17
  [[[dev-libs/libusb]](https://packages.gentoo.org/packages/dev-libs/libusb)[]]                              DONE     \>=emul-linux-x86-baselibs-20130224-r8
  [[[dev-libs/libxml2]](https://packages.gentoo.org/packages/dev-libs/libxml2)[]]                           DONE     \>=emul-linux-x86-baselibs-20131008-r14
  [[[dev-libs/libxslt]](https://packages.gentoo.org/packages/dev-libs/libxslt)[]]                           DONE     \>=emul-linux-x86-baselibs-20131008-r21
  [[[dev-libs/lzo]](https://packages.gentoo.org/packages/dev-libs/lzo)[]]                                       DONE     \>=emul-linux-x86-baselibs-20131008-r20
  [[[dev-libs/nettle]](https://packages.gentoo.org/packages/dev-libs/nettle)[]]                              DONE     \>=emul-linux-x86-baselibs-20131008-r17
  [[[dev-libs/nspr]](https://packages.gentoo.org/packages/dev-libs/nspr)[]]                                    DONE     \>=emul-linux-x86-baselibs-20140508-r14
  [[[dev-libs/nss]](https://packages.gentoo.org/packages/dev-libs/nss)[]]                                       DONE     \>=emul-linux-x86-baselibs-20140508-r14
  [[[dev-libs/openssl]](https://packages.gentoo.org/packages/dev-libs/openssl)[]]:0                         DONE     [[[bug #488418]](https://bugs.gentoo.org/show_bug.cgi?id=488418)[]]
  [[[dev-libs/openssl]](https://packages.gentoo.org/packages/dev-libs/openssl)[]]:0.9.8                     Done     \>=emul-linux-x86-baselibs-20140508-r5
  [[[dev-libs/udis86]](https://packages.gentoo.org/packages/dev-libs/udis86)[]]                              DONE     \>=emul-linux-x86-baselibs-20130224-r2
  [[[media-libs/giflib]](https://packages.gentoo.org/packages/media-libs/giflib)[]]                        DONE     \>=emul-linux-x86-baselibs-20140406-r2
  [[[media-libs/lcms]](https://packages.gentoo.org/packages/media-libs/lcms)[]]:2                            DONE     \>=emul-linux-x86-baselibs-20130224-r11
  [[[media-libs/lcms]](https://packages.gentoo.org/packages/media-libs/lcms)[]]:0                            DONE
  [[[media-libs/libart_lgpl]](https://packages.gentoo.org/packages/media-libs/libart_lgpl)[]]         DONE
  [[[media-libs/libmng]](https://packages.gentoo.org/packages/media-libs/libmng)[]]                        DONE     [[[bug #496380]](https://bugs.gentoo.org/show_bug.cgi?id=496380)[]]
  [[[media-libs/libpng]](https://packages.gentoo.org/packages/media-libs/libpng)[]]:1.2                    DONE     \>=emul-linux-x86-baselibs-20130224-r4
  [[[media-libs/libpng]](https://packages.gentoo.org/packages/media-libs/libpng)[]]                        DONE     \>=emul-linux-x86-baselibs-20130224-r2
  [[[media-libs/tiff]](https://packages.gentoo.org/packages/media-libs/tiff)[]]:0                            DONE     \>=emul-linux-x86-baselibs-20130224-r10
  [[[media-libs/tiff]](https://packages.gentoo.org/packages/media-libs/tiff)[]]:3                            DONE     \>=emul-linux-x86-baselibs-20130224-r11
  [[[net-dialup/capi4k-utils]](https://packages.gentoo.org/packages/net-dialup/capi4k-utils)[]]      TODO
  [[[net-dns/libidn]](https://packages.gentoo.org/packages/net-dns/libidn)[]]                                 DONE
  [[[net-libs/gnutls]](https://packages.gentoo.org/packages/net-libs/gnutls)[]]                              DONE     [[[bug #493166]](https://bugs.gentoo.org/show_bug.cgi?id=493166)[]]
  [[[net-libs/libgssglue]](https://packages.gentoo.org/packages/net-libs/libgssglue)[]]                  TODO
  [[[net-libs/libsoup]](https://packages.gentoo.org/packages/net-libs/libsoup)[]]                           DONE
  [[[net-libs/libtirpc]](https://packages.gentoo.org/packages/net-libs/libtirpc)[]]                        DONE
  [[[net-libs/neon]](https://packages.gentoo.org/packages/net-libs/neon)[]]                                    DONE
  [[[net-misc/curl]](https://packages.gentoo.org/packages/net-misc/curl)[]]                                    DONE
  [[[net-nds/openldap]](https://packages.gentoo.org/packages/net-nds/openldap)[]]                           DONE     [[[bug #493174]](https://bugs.gentoo.org/show_bug.cgi?id=493174)[]]
  [[[net-print/cups]](https://packages.gentoo.org/packages/net-print/cups)[]]                                 DONE     [[[bug #493172]](https://bugs.gentoo.org/show_bug.cgi?id=493172)[]]
  [[[sys-apps/acl]](https://packages.gentoo.org/packages/sys-apps/acl)[]]                                       DONE     [[[bug #496964]](https://bugs.gentoo.org/show_bug.cgi?id=496964)[]]
  [[[sys-apps/attr]](https://packages.gentoo.org/packages/sys-apps/attr)[]]                                    DONE     \>=emul-linux-x86-baselibs-20130224-r10
  [[[sys-apps/dbus]](https://packages.gentoo.org/packages/sys-apps/dbus)[]]                                    DONE     \>=emul-linux-x86-baselibs-20130224-r5
  [[[sys-apps/file]](https://packages.gentoo.org/packages/sys-apps/file)[]]                                    DONE     \>=emul-linux-x86-baselibs-20131008-r22
  [[[sys-apps/keyutils]](https://packages.gentoo.org/packages/sys-apps/keyutils)[]]                        DONE     [[[bug #505006]](https://bugs.gentoo.org/show_bug.cgi?id=505006)[]]
  [[[sys-apps/pciutils]](https://packages.gentoo.org/packages/sys-apps/pciutils)[]]                        TODO
  [[[sys-apps/tcp-wrappers]](https://packages.gentoo.org/packages/sys-apps/tcp-wrappers)[]]            DONE     \>=emul-linux-x86-baselibs-20130224-r5
  [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]                  DONE     [[[bug #490968]](https://bugs.gentoo.org/show_bug.cgi?id=490968)[]]
  [[[sys-auth/nss-mdns]](https://packages.gentoo.org/packages/sys-auth/nss-mdns)[]]                        DONE
  [[[sys-auth/nss_ldap]](https://packages.gentoo.org/packages/sys-auth/nss_ldap)[]]                        DONE
  [[[sys-auth/pam_ldap]](https://packages.gentoo.org/packages/sys-auth/pam_ldap)[]]                        DONE
  [[[sys-devel/binutils]](https://packages.gentoo.org/packages/sys-devel/binutils)[]]                     TODO
  [[[sys-devel/gettext]](https://packages.gentoo.org/packages/sys-devel/gettext)[]]                        DONE     \>=emul-linux-x86-baselibs-20131008-r14
  [[[sys-devel/libperl]](https://packages.gentoo.org/packages/sys-devel/libperl)[]]                        TODO
  [[[sys-devel/libtool]](https://packages.gentoo.org/packages/sys-devel/libtool)[]]                        DONE     [[[bug #499390]](https://bugs.gentoo.org/show_bug.cgi?id=499390)[]]
  [[[sys-devel/llvm]](https://packages.gentoo.org/packages/sys-devel/llvm)[]]                                 DONE     \>=emul-linux-x86-baselibs-20130224-r3
  [[[sys-fs/e2fsprogs]](https://packages.gentoo.org/packages/sys-fs/e2fsprogs)[]]                           TODO
  [[[sys-libs/cracklib]](https://packages.gentoo.org/packages/sys-libs/cracklib)[]]                        DONE
  [[[sys-libs/db]](https://packages.gentoo.org/packages/sys-libs/db)[]]                                          DONE
  [[[sys-libs/e2fsprogs-libs]](https://packages.gentoo.org/packages/sys-libs/e2fsprogs-libs)[]]      DONE     \>=emul-linux-x86-baselibs-20130224-r13
  [[[sys-libs/gdbm]](https://packages.gentoo.org/packages/sys-libs/gdbm)[]]                                    DONE     \>=emul-linux-x86-baselibs-20130224-r5
  [[[sys-libs/gpm]](https://packages.gentoo.org/packages/sys-libs/gpm)[]]                                       DONE     \>=emul-linux-x86-baselibs-20130224-r13
  [[[sys-libs/libavc1394]](https://packages.gentoo.org/packages/sys-libs/libavc1394)[]]                  DONE     \>=emul-linux-x86-baselibs-20130224-r5
  [[[sys-libs/libraw1394]](https://packages.gentoo.org/packages/sys-libs/libraw1394)[]]                  DONE     \>=emul-linux-x86-baselibs-20130224-r5
  [[[sys-libs/ncurses]](https://packages.gentoo.org/packages/sys-libs/ncurses)[]]                           DONE     \>=emul-linux-x86-baselibs-20130224-r13
  [[[sys-libs/pam]](https://packages.gentoo.org/packages/sys-libs/pam)[]]                                       DONE
  [[[sys-libs/pwdb]](https://packages.gentoo.org/packages/sys-libs/pwdb)[]]                                    TODO
  [[[sys-libs/readline]](https://packages.gentoo.org/packages/sys-libs/readline)[]]                        DONE     \>=emul-linux-x86-baselibs-20131008-r14
  [[[sys-libs/slang]](https://packages.gentoo.org/packages/sys-libs/slang)[]]                                 DONE     \>=emul-linux-x86-baselibs-20140406-r2
  [[[sys-libs/talloc]](https://packages.gentoo.org/packages/sys-libs/talloc)[]]                              DONE     [[[bug #491222]](https://bugs.gentoo.org/show_bug.cgi?id=491222)[]]
  [[[sys-libs/zlib]](https://packages.gentoo.org/packages/sys-libs/zlib)[]]                                    DONE     \>=emul-linux-x86-baselibs-20130224-r1
  [[[virtual/jpeg]](https://packages.gentoo.org/packages/virtual/jpeg)[]]                                       DONE     \>=emul-linux-x86-baselibs-20130224-r5
  [[[media-libs/jpeg]](https://packages.gentoo.org/packages/media-libs/jpeg)[]]:62                           DONE     \>=emul-linux-x86-baselibs-20130224-r5
  [[[media-libs/libjpeg-turbo]](https://packages.gentoo.org/packages/media-libs/libjpeg-turbo)[]]   DONE     \>=emul-linux-x86-baselibs-20130224-r4
  [[[virtual/udev]](https://packages.gentoo.org/packages/virtual/udev)[]]                                       DONE     \>=emul-linux-x86-baselibs-20130224-r9
  [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]                           DONE
  [[[sys-fs/eudev]](https://packages.gentoo.org/packages/sys-fs/eudev)[]]                                       DONE
  [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]]                                          DONE
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [~~emul-linux-x86-compat~~]

-   Package removed as of 2014-10-14, [[[bug #517932]](https://bugs.gentoo.org/show_bug.cgi?id=517932)[]].

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ---------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                 Status   Notes
  [[[sys-libs/lib-compat]](https://packages.gentoo.org/packages/sys-libs/lib-compat)[]]         DONE     Binary package, 32-bit only
  [[[sys-libs/libstdc++-v3]](https://packages.gentoo.org/packages/sys-libs/libstdc++-v3)[]]   DONE     Already builds the 32-bit x86 version with USE=multilib
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ---------------------------------------------------------

### [emul-linux-x86-cpplibs]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                        Status   Notes
  [[[dev-libs/boost]](https://packages.gentoo.org/packages/dev-libs/boost)[]]               DONE     [[[bug #512884]](https://bugs.gentoo.org/show_bug.cgi?id=512884)[]]
  [[[dev-libs/libsigc++]](https://packages.gentoo.org/packages/dev-libs/libsigc++)[]]   TODO
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [emul-linux-x86-db]

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                               Status   Notes
  [[[dev-db/myodbc]](https://packages.gentoo.org/packages/dev-db/myodbc)[]]         DONE     done with \>=dev-db/myodbc-5.2.7-r1
  [[[dev-db/mysql]](https://packages.gentoo.org/packages/dev-db/mysql)[]]            DONE     done with \>=virtual/mysql-5.6-r2
  [[[dev-db/unixODBC]](https://packages.gentoo.org/packages/dev-db/unixODBC)[]]   DONE     [[[bug #510868]](https://bugs.gentoo.org/show_bug.cgi?id=510868)[]] \>=emul-linux-x86-db-20140508-r1
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [~~emul-linux-x86-glibc-errno-compat~~]

-   Not an emul package, only keyworded for **[\~x86]**.
-   Package removed as of 2014-09-07, [[[bug #503208]](https://bugs.gentoo.org/show_bug.cgi?id=503208)[]].

### [emul-linux-x86-gstplugins]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------
  Package                                                                                                                                                                                                                                                                                                                                                                                                                              Status   Notes
  [[[media-libs/gst-plugins-bad]](https://packages.gentoo.org/packages/media-libs/gst-plugins-bad)[]]                                 DONE
  [[[media-libs/gst-plugins-good]](https://packages.gentoo.org/packages/media-libs/gst-plugins-good)[]]                              DONE
  [[[media-libs/gst-plugins-ugly]](https://packages.gentoo.org/packages/media-libs/gst-plugins-ugly)[]]                              DONE
  [[[media-plugins/gst-plugins-a52dec]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-a52dec)[]]               DONE
  [[[media-plugins/gst-plugins-alsa]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-alsa)[]]                     DONE
  [[[media-plugins/gst-plugins-annodex]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-annodex)[]]            DONE
  [[[media-plugins/gst-plugins-cdio]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-cdio)[]]                     DONE
  [[[media-plugins/gst-plugins-cdparanoia]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-cdparanoia)[]]   DONE
  [[[media-plugins/gst-plugins-dts]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-dts)[]]                        DONE
  [[[media-plugins/gst-plugins-dv]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-dv)[]]                           DONE
  [[[media-plugins/gst-plugins-dvb]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-dvb)[]]                        DONE
  [[[media-plugins/gst-plugins-dvdread]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-dvdread)[]]            DONE
  [[[media-plugins/gst-plugins-faac]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-faac)[]]                     DONE
  [[[media-plugins/gst-plugins-faad]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-faad)[]]                     DONE
  [[[media-plugins/gst-plugins-ffmpeg]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-ffmpeg)[]]               DONE
  [[[media-plugins/gst-plugins-flac]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-flac)[]]                     DONE
  [[[media-plugins/gst-plugins-gconf]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-gconf)[]]                  DONE
  [[[media-plugins/gst-plugins-gio]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-gio)[]]                        DONE
  [[[media-plugins/gst-plugins-gnomevfs]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-gnomevfs)[]]         DONE
  [[[media-plugins/gst-plugins-jpeg]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-jpeg)[]]                     DONE
  [[[media-plugins/gst-plugins-ladspa]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-ladspa)[]]               DONE
  [[[media-plugins/gst-plugins-lame]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-lame)[]]                     DONE
  [[[media-plugins/gst-plugins-libmms]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-libmms)[]]               DONE
  [[[media-plugins/gst-plugins-libpng]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-libpng)[]]               DONE
  [[[media-plugins/gst-plugins-libvisual]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-libvisual)[]]      DONE
  [[[media-plugins/gst-plugins-mad]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-mad)[]]                        DONE
  [[[media-plugins/gst-plugins-meta]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-meta)[]]                     DONE
  [[[media-plugins/gst-plugins-mimic]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-mimic)[]]                  DONE
  [[[media-plugins/gst-plugins-modplug]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-modplug)[]]            DONE
  [[[media-plugins/gst-plugins-mpeg2dec]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-mpeg2dec)[]]         DONE
  [[[media-plugins/gst-plugins-mplex]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-mplex)[]]                  DONE
  [[[media-plugins/gst-plugins-musepack]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-musepack)[]]         DONE
  [[[media-plugins/gst-plugins-neon]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-neon)[]]                     DONE
  [[[media-plugins/gst-plugins-ofa]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-ofa)[]]                        DONE
  [[[media-plugins/gst-plugins-ogg]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-ogg)[]]                        DONE
  [[[media-plugins/gst-plugins-oss]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-oss)[]]                        DONE
  [[[media-plugins/gst-plugins-pango]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-pango)[]]                  DONE
  [[[media-plugins/gst-plugins-pulse]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-pulse)[]]                  DONE
  [[[media-plugins/gst-plugins-raw1394]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-raw1394)[]]            DONE
  [[[media-plugins/gst-plugins-resindvd]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-resindvd)[]]         DONE
  [[[media-plugins/gst-plugins-shout2]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-shout2)[]]               DONE
  [[[media-plugins/gst-plugins-sidplay]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-sidplay)[]]            DONE
  [[[media-plugins/gst-plugins-soup]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-soup)[]]                     DONE
  [[[media-plugins/gst-plugins-speex]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-speex)[]]                  DONE
  [[[media-plugins/gst-plugins-taglib]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-taglib)[]]               DONE
  [[[media-plugins/gst-plugins-theora]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-theora)[]]               DONE
  [[[media-plugins/gst-plugins-twolame]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-twolame)[]]            DONE
  [[[media-plugins/gst-plugins-v4l2]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-v4l2)[]]                     DONE
  [[[media-plugins/gst-plugins-vorbis]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-vorbis)[]]               DONE
  [[[media-plugins/gst-plugins-vp8]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-vp8)[]]                        DONE
  [[[media-plugins/gst-plugins-wavpack]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-wavpack)[]]            DONE
  [[[media-plugins/gst-plugins-x]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-x)[]]                              DONE
  [[[media-plugins/gst-plugins-x264]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-x264)[]]                     DONE
  [[[media-plugins/gst-plugins-ximagesrc]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-ximagesrc)[]]      DONE
  [[[media-plugins/gst-plugins-xvid]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-xvid)[]]                     DONE
  [[[media-plugins/gst-plugins-xvideo]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-xvideo)[]]               DONE
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------

### [emul-linux-x86-gtklibs]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                            Status   Notes
  [[[dev-libs/atk]](https://packages.gentoo.org/packages/dev-libs/atk)[]]                                                         DONE     [[[bug #488608]](https://bugs.gentoo.org/show_bug.cgi?id=488608)[]]
  [[[dev-libs/libIDL]](https://packages.gentoo.org/packages/dev-libs/libIDL)[]]                                                TODO
  [[[gnome-base/gconf]](https://packages.gentoo.org/packages/gnome-base/gconf)[]]                                             DONE
  [[[gnome-base/gnome-vfs]](https://packages.gentoo.org/packages/gnome-base/gnome-vfs)[]]                                 DONE
  [[[gnome-base/libglade]](https://packages.gentoo.org/packages/gnome-base/libglade)[]]                                    DONE
  [[[gnome-base/orbit]](https://packages.gentoo.org/packages/gnome-base/orbit)[]]                                             TODO
  [[[media-gfx/graphite2]](https://packages.gentoo.org/packages/media-gfx/graphite2)[]]                                    DONE     [[[bug #488860]](https://bugs.gentoo.org/show_bug.cgi?id=488860)[]]
  [[[media-libs/harfbuzz]](https://packages.gentoo.org/packages/media-libs/harfbuzz)[]]                                    DONE     [[[bug #488864]](https://bugs.gentoo.org/show_bug.cgi?id=488864)[]]
  [[[media-libs/imlib]](https://packages.gentoo.org/packages/media-libs/imlib)[]]                                             DONE     \>=emul-linux-x86-gtklibs-20140406-r1
  [[[x11-libs/cairo]](https://packages.gentoo.org/packages/x11-libs/cairo)[]]                                                   DONE     \>=emul-linux-x86-gtklibs-20131008-r2
  [[[x11-libs/gdk-pixbuf]](https://packages.gentoo.org/packages/x11-libs/gdk-pixbuf)[]]                                    DONE     \>=emul-linux-x86-gtklibs-20131008-r3
  [[[x11-libs/gtk+]](https://packages.gentoo.org/packages/x11-libs/gtk+)[]]                                                      DONE     [[[bug #489000]](https://bugs.gentoo.org/show_bug.cgi?id=489000)[]]
  [[[x11-libs/libnotify]](https://packages.gentoo.org/packages/x11-libs/libnotify)[]]                                       DONE
  [[[x11-libs/pango]](https://packages.gentoo.org/packages/x11-libs/pango)[]]                                                   DONE     \>=emul-linux-x86-gtklibs-20131008-r4
  [[[x11-libs/pangox-compat]](https://packages.gentoo.org/packages/x11-libs/pangox-compat)[]]                           DONE     [[[bug #488870]](https://bugs.gentoo.org/show_bug.cgi?id=488870)[]]
  [[[x11-libs/pixman]](https://packages.gentoo.org/packages/x11-libs/pixman)[]]                                                DONE     \>=emul-linux-x86-gtklibs-20131008-r1
  [[[x11-themes/gtk-engines]](https://packages.gentoo.org/packages/x11-themes/gtk-engines)[]]                           DONE
  [[[x11-themes/gtk-engines-murrine]](https://packages.gentoo.org/packages/x11-themes/gtk-engines-murrine)[]]   DONE
  [[[x11-themes/gtk-engines-xfce]](https://packages.gentoo.org/packages/x11-themes/gtk-engines-xfce)[]]            DONE
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [emul-linux-x86-gtkmmlibs]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------
  Package                                                                                                                                                                                                                                                                                                                                                                        Status   Notes
  [[[dev-cpp/atkmm]](https://packages.gentoo.org/packages/dev-cpp/atkmm)[]]                  TODO
  [[[dev-cpp/cairomm]](https://packages.gentoo.org/packages/dev-cpp/cairomm)[]]            TODO
  [[[dev-cpp/glibmm]](https://packages.gentoo.org/packages/dev-cpp/glibmm)[]]               TODO
  [[[dev-cpp/gtkmm]](https://packages.gentoo.org/packages/dev-cpp/gtkmm)[]]                  TODO
  [[[dev-cpp/libglademm]](https://packages.gentoo.org/packages/dev-cpp/libglademm)[]]   TODO
  [[[dev-cpp/pangomm]](https://packages.gentoo.org/packages/dev-cpp/pangomm)[]]            TODO
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------

### [emul-linux-x86-java]

### [emul-linux-x86-jna]

-   Tracker [[[bug #474464]](https://bugs.gentoo.org/show_bug.cgi?id=474464)[]]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------
  Package                                                                                                                                                                                                                                                                                                                                                      Status   Notes
  [[[dev-java/jna]](https://packages.gentoo.org/packages/dev-java/jna)[]]   TODO
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------

### [emul-linux-x86-medialibs]

-   [[[dev-libs/DirectFB]](https://packages.gentoo.org/packages/dev-libs/DirectFB)[]] doesn\'t need to be ported, see [[[bug #484248]](https://bugs.gentoo.org/show_bug.cgi?id=484248)[]]

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                   Status   Notes
  [[[app-misc/lirc]](https://packages.gentoo.org/packages/app-misc/lirc)[]]                                             TODO
  [[[dev-libs/fribidi]](https://packages.gentoo.org/packages/dev-libs/fribidi)[]]                                    DONE     \>=emul-linux-x86-medialibs-20130224-r11
  [[[dev-libs/libcdio]](https://packages.gentoo.org/packages/dev-libs/libcdio)[]]                                    DONE     \>=emul-linux-x86-medialibs-20130224-r11
  [[[dev-libs/liboil]](https://packages.gentoo.org/packages/dev-libs/liboil)[]]                                       DONE     \>=emul-linux-x86-medialibs-20130224-r10
  [[[media-gfx/sane-backends]](https://packages.gentoo.org/packages/media-gfx/sane-backends)[]]               DONE     [[[bug #493168]](https://bugs.gentoo.org/show_bug.cgi?id=493168)[]]
  [[[media-libs/a52dec]](https://packages.gentoo.org/packages/media-libs/a52dec)[]]                                 DONE     \>=emul-linux-x86-medialibs-20130224-r9
  [[[media-libs/faac]](https://packages.gentoo.org/packages/media-libs/faac)[]]                                       DONE     \>=emul-linux-x86-medialibs-20130224-r2
  [[[media-libs/faad2]](https://packages.gentoo.org/packages/media-libs/faad2)[]]                                    DONE     \>=emul-linux-x86-medialibs-20130224-r2
  [[[media-libs/gst-plugins-base]](https://packages.gentoo.org/packages/media-libs/gst-plugins-base)[]]   DONE
  [[[media-libs/gstreamer]](https://packages.gentoo.org/packages/media-libs/gstreamer)[]]                        DONE     [[[bug #493176]](https://bugs.gentoo.org/show_bug.cgi?id=493176)[]]
  [[[media-libs/libcuefile]](https://packages.gentoo.org/packages/media-libs/libcuefile)[]]                     DONE     \>=emul-linux-x86-medialibs-20130224-r3
  [[[media-libs/libdca]](https://packages.gentoo.org/packages/media-libs/libdca)[]]                                 DONE     \>=emul-linux-x86-medialibs-20130224-r4
  [[[media-libs/libdv]](https://packages.gentoo.org/packages/media-libs/libdv)[]]                                    DONE     \>=emul-linux-x86-medialibs-20130224-r13
  [[[media-libs/libdvdnav]](https://packages.gentoo.org/packages/media-libs/libdvdnav)[]]                        DONE     \>=emul-linux-x86-medialibs-20130224-r5
  [[[media-libs/libdvdread]](https://packages.gentoo.org/packages/media-libs/libdvdread)[]]                     DONE     \>=emul-linux-x86-medialibs-20130224-r5
  [[[media-libs/libgphoto2]](https://packages.gentoo.org/packages/media-libs/libgphoto2)[]]                     DONE     [[[bug #493170]](https://bugs.gentoo.org/show_bug.cgi?id=493170)[]]
  [[[media-libs/libid3tag]](https://packages.gentoo.org/packages/media-libs/libid3tag)[]]                        DONE     \>=emul-linux-x86-medialibs-20130224-r7
  [[[media-libs/libiec61883]](https://packages.gentoo.org/packages/media-libs/libiec61883)[]]                  DONE     \>=emul-linux-x86-medialibs-20130224-r8
  [[[media-libs/libmad]](https://packages.gentoo.org/packages/media-libs/libmad)[]]                                 DONE     \>=emul-linux-x86-medialibs-20130224-r4
  [[[media-libs/libmimic]](https://packages.gentoo.org/packages/media-libs/libmimic)[]]                           DONE     \>=emul-linux-x86-medialibs-20130224-r9
  [[[media-libs/libmms]](https://packages.gentoo.org/packages/media-libs/libmms)[]]                                 DONE     \>=emul-linux-x86-medialibs-20130224-r9
  [[[media-libs/libmpeg2]](https://packages.gentoo.org/packages/media-libs/libmpeg2)[]]                           DONE     \>=emul-linux-x86-medialibs-20130224-r10
  [[[media-libs/libofa]](https://packages.gentoo.org/packages/media-libs/libofa)[]]                                 DONE
  [[[media-libs/libpostproc]](https://packages.gentoo.org/packages/media-libs/libpostproc)[]]                  DONE
  [[[media-libs/libreplaygain]](https://packages.gentoo.org/packages/media-libs/libreplaygain)[]]            DONE     \>=emul-linux-x86-medialibs-20130224-r3
  [[[media-libs/libshout]](https://packages.gentoo.org/packages/media-libs/libshout)[]]                           DONE     \>=emul-linux-x86-medialibs-20130224-r7
  [[[media-libs/libsidplay]](https://packages.gentoo.org/packages/media-libs/libsidplay)[]]                     DONE     \>=emul-linux-x86-medialibs-20130224-r7
  [[[media-libs/libtheora]](https://packages.gentoo.org/packages/media-libs/libtheora)[]]                        DONE     \>=emul-linux-x86-medialibs-20130224-r2
  [[[media-libs/libv4l]](https://packages.gentoo.org/packages/media-libs/libv4l)[]]                                 DONE     \>=emul-linux-x86-medialibs-20130224-r6
  [[[media-libs/libvisual]](https://packages.gentoo.org/packages/media-libs/libvisual)[]]                        DONE     \>=emul-linux-x86-medialibs-20130224-r10
  [[[media-libs/libvpx]](https://packages.gentoo.org/packages/media-libs/libvpx)[]]                                 DONE     \>=emul-linux-x86-medialibs-20130224-r2
  [[[media-libs/speex]](https://packages.gentoo.org/packages/media-libs/speex)[]]                                    DONE     \>=emul-linux-x86-medialibs-20130224-r4
  [[[media-libs/taglib]](https://packages.gentoo.org/packages/media-libs/taglib)[]]                                 DONE
  [[[media-libs/x264]](https://packages.gentoo.org/packages/media-libs/x264)[]]                                       DONE     \>=emul-linux-x86-medialibs-20130224-r8
  [[[media-libs/xvid]](https://packages.gentoo.org/packages/media-libs/xvid)[]]                                       DONE     \>=emul-linux-x86-medialibs-20130224-r2
  [[[media-sound/lame]](https://packages.gentoo.org/packages/media-sound/lame)[]]                                    DONE     \>=emul-linux-x86-medialibs-20130224-r2
  [[[media-video/mjpegtools]](https://packages.gentoo.org/packages/media-video/mjpegtools)[]]                  DONE
  [[[sys-libs/libieee1284]](https://packages.gentoo.org/packages/sys-libs/libieee1284)[]]                        DONE     \>=emul-linux-x86-medialibs-20130224-r10
  [[[virtual/ffmpeg]](https://packages.gentoo.org/packages/virtual/ffmpeg)[]]                                          DONE
  [[[media-video/libav]](https://packages.gentoo.org/packages/media-video/libav)[]]                                 DONE
  [[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]]                              DONE
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [emul-linux-x86-motif]

-   Tracker [[[bug #461916]](https://bugs.gentoo.org/show_bug.cgi?id=461916)[]]
-   emul-linux-x86-motif package is fully ported.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------
  Package                                                                                                                                                                                                                                                                                                                                                            Status   Notes
  [[[x11-libs/motif]](https://packages.gentoo.org/packages/x11-libs/motif)[]]   DONE
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------

### [emul-linux-x86-opengl]

-   Tracker [[[bug #468102]](https://bugs.gentoo.org/show_bug.cgi?id=468102)[]]

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                           Status   Notes
  [[[media-libs/freeglut]](https://packages.gentoo.org/packages/media-libs/freeglut)[]]   DONE     \>=emul-linux-x86-opengl-20131008.ebuild
  [[[media-libs/glew]](https://packages.gentoo.org/packages/media-libs/glew)[]]               DONE     \>=emul-linux-x86-opengl-20131008.ebuild
  [[[media-libs/glu]](https://packages.gentoo.org/packages/media-libs/glu)[]]                  DONE     \>=emul-linux-x86-opengl-20131008.ebuild
  [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]]               DONE     \>=emul-linux-x86-opengl-20131008.ebuild
  [[[x11-libs/libdrm]](https://packages.gentoo.org/packages/x11-libs/libdrm)[]]               DONE     \>=emul-linux-x86-opengl-20131008.ebuild
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------

### [emul-linux-x86-qtlibs]

-   changed package category from x11-libs to dev-qt

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                              Status   Notes
  [[[media-libs/phonon]](https://packages.gentoo.org/packages/media-libs/phonon)[]]            TODO
  [[[dev-qt/qtcore]](https://packages.gentoo.org/packages/dev-qt/qtcore)[]]                        DONE     \>=dev-qt/qtcore-4.8.6
  [[[dev-qt/qtdbus]](https://packages.gentoo.org/packages/dev-qt/qtdbus)[]]                        DONE     \>=dev-qt/qtdbus-4.8.6
  [[[dev-qt/qtgui]](https://packages.gentoo.org/packages/dev-qt/qtgui)[]]                           DONE     \>=dev-qt/qtgui-4.8.6
  [[[dev-qt/qtopengl]](https://packages.gentoo.org/packages/dev-qt/qtopengl)[]]                  DONE     \>=dev-qt/qtopengl-4.8.6
  [[[dev-qt/qtscript]](https://packages.gentoo.org/packages/dev-qt/qtscript)[]]                  DONE     \>=dev-qt/qtscript-4.8.6
  [[[dev-qt/qtsql]](https://packages.gentoo.org/packages/dev-qt/qtsql)[]]                           DONE     \>=dev-qt/qtsql-4.8.6
  [[[dev-qt/qtsvg]](https://packages.gentoo.org/packages/dev-qt/qtsvg)[]]                           DONE     \>=dev-qt/qtsvg-4.8.6
  [[[dev-qt/qtwebkit]](https://packages.gentoo.org/packages/dev-qt/qtwebkit)[]]                  DONE     \>=dev-qt/qtwebkit-4.8.6
  [[[dev-qt/qtxmlpatterns]](https://packages.gentoo.org/packages/dev-qt/qtxmlpatterns)[]]   DONE     \>=dev-qt/qtxmlpatterns-4.8.6
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- -------------------------------

### [emul-linux-x86-sdl]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                              Status   Notes
  [[[media-libs/freealut]](https://packages.gentoo.org/packages/media-libs/freealut)[]]      DONE     \>=emul-linux-x86-sdl-20140406-r1
  [[[media-libs/libsdl]](https://packages.gentoo.org/packages/media-libs/libsdl)[]]            DONE     \>=emul-linux-x86-sdl-20140406-r1
  [[[media-libs/openal]](https://packages.gentoo.org/packages/media-libs/openal)[]]            DONE     [[[bug #484060]](https://bugs.gentoo.org/show_bug.cgi?id=484060)[]] \>=openal-1.15.1-r1
  [[[media-libs/sdl-image]](https://packages.gentoo.org/packages/media-libs/sdl-image)[]]   DONE     \>=emul-linux-x86-sdl-20140406-r1
  [[[media-libs/sdl-mixer]](https://packages.gentoo.org/packages/media-libs/sdl-mixer)[]]   DONE     \>=emul-linux-x86-sdl-20140406-r2
  [[[media-libs/sdl-net]](https://packages.gentoo.org/packages/media-libs/sdl-net)[]]         DONE     \>=emul-linux-x86-sdl-20140406-r1
  [[[media-libs/sdl-sound]](https://packages.gentoo.org/packages/media-libs/sdl-sound)[]]   DONE     \>=emul-linux-x86-sdl-20140406-r1
  [[[media-libs/sdl-ttf]](https://packages.gentoo.org/packages/media-libs/sdl-ttf)[]]         DONE     \>=emul-linux-x86-sdl-20140406-r1
  [[[media-libs/smpeg]](https://packages.gentoo.org/packages/media-libs/smpeg)[]]               DONE     \>=emul-linux-x86-sdl-20140406-r1
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [emul-linux-x86-soundlibs]

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                                                 Status   Notes
  [[[media-libs/alsa-lib]](https://packages.gentoo.org/packages/media-libs/alsa-lib)[]]                                                         DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-libs/alsa-oss]](https://packages.gentoo.org/packages/media-libs/alsa-oss)[]]                                                         DONE
  [[[media-libs/audiofile]](https://packages.gentoo.org/packages/media-libs/audiofile)[]]                                                      DONE     [[[bug #513780]](https://bugs.gentoo.org/show_bug.cgi?id=513780)[]] needs closing, \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-libs/flac]](https://packages.gentoo.org/packages/media-libs/flac)[]]                                                                     DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-libs/ladspa-sdk]](https://packages.gentoo.org/packages/media-libs/ladspa-sdk)[]]                                                   DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-libs/libao]](https://packages.gentoo.org/packages/media-libs/libao)[]]                                                                  DONE     \>=emul-linux-x86-soundlibs-20131008-r2
  [[[media-libs/libmikmod]](https://packages.gentoo.org/packages/media-libs/libmikmod)[]]                                                      DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-libs/libmodplug]](https://packages.gentoo.org/packages/media-libs/libmodplug)[]]                                                   DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-libs/libogg]](https://packages.gentoo.org/packages/media-libs/libogg)[]]                                                               DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-libs/libsamplerate]](https://packages.gentoo.org/packages/media-libs/libsamplerate)[]]                                          DONE     \>=emul-linux-x86-soundlibs-20130224-r7.ebuild
  [[[media-libs/libsndfile]](https://packages.gentoo.org/packages/media-libs/libsndfile)[]]                                                   DONE     \>=emul-linux-x86-soundlibs-20130224-r7.ebuild
  [[[media-libs/libvorbis]](https://packages.gentoo.org/packages/media-libs/libvorbis)[]]                                                      DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-libs/portaudio]](https://packages.gentoo.org/packages/media-libs/portaudio)[]]                                                      DONE     \>=emul-linux-x86-soundlibs-20130224-r9.ebuild
  [[[media-libs/webrtc-audio-processing]](https://packages.gentoo.org/packages/media-libs/webrtc-audio-processing)[]]            DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-plugins/alsa-plugins]](https://packages.gentoo.org/packages/media-plugins/alsa-plugins)[]]                                    DONE     [[[bug #488132]](https://bugs.gentoo.org/show_bug.cgi?id=488132)[]]
  [[[media-plugins/alsaequal]](https://packages.gentoo.org/packages/media-plugins/alsaequal)[]]                                             DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-plugins/caps-plugins]](https://packages.gentoo.org/packages/media-plugins/caps-plugins)[]]                                    DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-plugins/swh-plugins]](https://packages.gentoo.org/packages/media-plugins/swh-plugins)[]]                                       DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-sound/cdparanoia]](https://packages.gentoo.org/packages/media-sound/cdparanoia)[]]                                                DONE     \>=emul-linux-x86-soundlibs-20130224-r5.ebuild
  [[[media-sound/gsm]](https://packages.gentoo.org/packages/media-sound/gsm)[]]                                                                     DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  [[[media-sound/jack-audio-connection-kit]](https://packages.gentoo.org/packages/media-sound/jack-audio-connection-kit)[]]   DONE     \>=emul-linux-x86-soundlibs-20130224-r8.ebuild
  [[[media-sound/mpg123]](https://packages.gentoo.org/packages/media-sound/mpg123)[]]                                                            DONE     \>=emul-linux-x86-soundlibs-20130224-r10.ebuild
  [[[media-sound/musepack-tools]](https://packages.gentoo.org/packages/media-sound/musepack-tools)[]]                                    DONE     \>=emul-linux-x86-soundlibs-20130224-r6.ebuild
  [[[media-sound/pulseaudio]](https://packages.gentoo.org/packages/media-sound/pulseaudio)[]]                                                DONE     \>=emul-linux-x86-soundlibs-20131008-r2
  [[[media-sound/twolame]](https://packages.gentoo.org/packages/media-sound/twolame)[]]                                                         DONE     \>=emul-linux-x86-soundlibs-20130224-r7.ebuild
  [[[media-sound/wavpack]](https://packages.gentoo.org/packages/media-sound/wavpack)[]]                                                         DONE     \>=emul-linux-x86-soundlibs-20130224-r5.ebuild
  [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]]                                                            DONE
  [[[sci-libs/fftw]](https://packages.gentoo.org/packages/sci-libs/fftw)[]]                                                                           DONE     \>=emul-linux-x86-soundlibs-20130224-r4.ebuild
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [emul-linux-x86-xlibs]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- --------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                    Status   Notes
  [[[media-libs/fontconfig]](https://packages.gentoo.org/packages/media-libs/fontconfig)[]]      DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[media-libs/freetype]](https://packages.gentoo.org/packages/media-libs/freetype)[]]            DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libICE]](https://packages.gentoo.org/packages/x11-libs/libICE)[]]                        DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libpciaccess]](https://packages.gentoo.org/packages/x11-libs/libpciaccess)[]]      DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libSM]](https://packages.gentoo.org/packages/x11-libs/libSM)[]]                           DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libvdpau]](https://packages.gentoo.org/packages/x11-libs/libvdpau)[]]                  DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libX11]](https://packages.gentoo.org/packages/x11-libs/libX11)[]]                        DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXau]](https://packages.gentoo.org/packages/x11-libs/libXau)[]]                        DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXaw]](https://packages.gentoo.org/packages/x11-libs/libXaw)[]]                        DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libxcb]](https://packages.gentoo.org/packages/x11-libs/libxcb)[]]                        DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXcomposite]](https://packages.gentoo.org/packages/x11-libs/libXcomposite)[]]   DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXcursor]](https://packages.gentoo.org/packages/x11-libs/libXcursor)[]]            DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXdamage]](https://packages.gentoo.org/packages/x11-libs/libXdamage)[]]            DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXdmcp]](https://packages.gentoo.org/packages/x11-libs/libXdmcp)[]]                  DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXext]](https://packages.gentoo.org/packages/x11-libs/libXext)[]]                     DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXfixes]](https://packages.gentoo.org/packages/x11-libs/libXfixes)[]]               DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXft]](https://packages.gentoo.org/packages/x11-libs/libXft)[]]                        DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXi]](https://packages.gentoo.org/packages/x11-libs/libXi)[]]                           DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXinerama]](https://packages.gentoo.org/packages/x11-libs/libXinerama)[]]         DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXmu]](https://packages.gentoo.org/packages/x11-libs/libXmu)[]]                        DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXp]](https://packages.gentoo.org/packages/x11-libs/libXp)[]]                           DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXpm]](https://packages.gentoo.org/packages/x11-libs/libXpm)[]]                        DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXrandr]](https://packages.gentoo.org/packages/x11-libs/libXrandr)[]]               DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXrender]](https://packages.gentoo.org/packages/x11-libs/libXrender)[]]            DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXScrnSaver]](https://packages.gentoo.org/packages/x11-libs/libXScrnSaver)[]]   DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXt]](https://packages.gentoo.org/packages/x11-libs/libXt)[]]                           DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXtst]](https://packages.gentoo.org/packages/x11-libs/libXtst)[]]                     DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXv]](https://packages.gentoo.org/packages/x11-libs/libXv)[]]                           DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXvMC]](https://packages.gentoo.org/packages/x11-libs/libXvMC)[]]                     DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXxf86dga]](https://packages.gentoo.org/packages/x11-libs/libXxf86dga)[]]         DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  [[[x11-libs/libXxf86vm]](https://packages.gentoo.org/packages/x11-libs/libXxf86vm)[]]            DONE     \>=emul-linux-x86-xlibs-20130224-r2.ebuild
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- --------------------------------------------

## [Other packages porting status]

### [Source packages]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                                  Status         Notes
  [[[app-admin/elektra]](https://packages.gentoo.org/packages/app-admin/elektra)[]]                                                DONE
  [[[app-arch/xz-utils]](https://packages.gentoo.org/packages/app-arch/xz-utils)[]]                                                DONE           [[[bug #474940]](https://bugs.gentoo.org/show_bug.cgi?id=474940)[]]
  [[[app-benchmarks/cpuburn]](https://packages.gentoo.org/packages/app-benchmarks/cpuburn)[]]                                 DONE
  [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]]:18                                             DONE
  [[[app-emulation/wine]](https://packages.gentoo.org/packages/app-emulation/wine)[]]                                             DONE
  [[[dev-cpp/gtest]](https://packages.gentoo.org/packages/dev-cpp/gtest)[]]                                                            DONE           [[[bug #513780]](https://bugs.gentoo.org/show_bug.cgi?id=513780)[]] needs closing
  [[[dev-cpp/libxmlpp]](https://packages.gentoo.org/packages/dev-cpp/libxmlpp)[]]                                                   IN PROGRESS    [[[bug #469180]](https://bugs.gentoo.org/show_bug.cgi?id=469180)[]]
  [[[dev-cpp/tbb]](https://packages.gentoo.org/packages/dev-cpp/tbb)[]]                                                                  IN PROGRESS    [[[bug #545190]](https://bugs.gentoo.org/show_bug.cgi?id=545190)[]]
  [[[dev-db/oracle-instantclient-jdbc]](https://packages.gentoo.org/packages/dev-db/oracle-instantclient-jdbc)[]]   DONE           [[[bug #506228]](https://bugs.gentoo.org/show_bug.cgi?id=506228)[]]
  [[[dev-db/oracle-instantclient-odbc]](https://packages.gentoo.org/packages/dev-db/oracle-instantclient-odbc)[]]   DONE           [[[bug #506228]](https://bugs.gentoo.org/show_bug.cgi?id=506228)[]]
  [[[dev-lang/tcl]](https://packages.gentoo.org/packages/dev-lang/tcl)[]]                                                               DONE           [[[bug #496008]](https://bugs.gentoo.org/show_bug.cgi?id=496008)[]]
  [[[dev-libs/check]](https://packages.gentoo.org/packages/dev-libs/check)[]]                                                         DONE           [[[bug #473624]](https://bugs.gentoo.org/show_bug.cgi?id=473624)[]]
  [[[dev-libs/crypto++]](https://packages.gentoo.org/packages/dev-libs/crypto++)[]]                                                IN PROGRESS    [[[bug #534146]](https://bugs.gentoo.org/show_bug.cgi?id=534146)[]]
  [[[dev-libs/icu]](https://packages.gentoo.org/packages/dev-libs/icu)[]]                                                               DONE           [[[bug #480422]](https://bugs.gentoo.org/show_bug.cgi?id=480422)[]]
  [[[dev-libs/libappindicator]](https://packages.gentoo.org/packages/dev-libs/libappindicator)[]]                           IN PROGRESS    [[[bug #462764]](https://bugs.gentoo.org/show_bug.cgi?id=462764)[]]
  [[[dev-libs/libdbusmenu]](https://packages.gentoo.org/packages/dev-libs/libdbusmenu)[]]                                       IN PROGRESS    [[[bug #462764]](https://bugs.gentoo.org/show_bug.cgi?id=462764)[]]
  [[[dev-libs/libev]](https://packages.gentoo.org/packages/dev-libs/libev)[]]                                                         DONE           [[[bug #505010]](https://bugs.gentoo.org/show_bug.cgi?id=505010)[]]
  [[[dev-libs/libindicator]](https://packages.gentoo.org/packages/dev-libs/libindicator)[]]                                    IN PROGRESS    [[[bug #462764]](https://bugs.gentoo.org/show_bug.cgi?id=462764)[]]
  [[[dev-libs/libnsfb]](https://packages.gentoo.org/packages/dev-libs/libnsfb)[]]                                                   DONE
  [[[dev-libs/newt]](https://packages.gentoo.org/packages/dev-libs/newt)[]]                                                            IN PROGRESS    [[[bug #548484]](https://bugs.gentoo.org/show_bug.cgi?id=548484)[]]
  [[[dev-util/apitrace]](https://packages.gentoo.org/packages/dev-util/apitrace)[]]                                                DONE           gx86-multilib only since 4.0
  [[[games-emulation/nestra]](https://packages.gentoo.org/packages/games-emulation/nestra)[]]                                 DONE
  [[[games-emulation/zinc]](https://packages.gentoo.org/packages/games-emulation/zinc)[]]                                       DONE
  [[[games-emulation/zsnes]](https://packages.gentoo.org/packages/games-emulation/zsnes)[]]                                    DONE
  [[[games-fps/avp]](https://packages.gentoo.org/packages/games-fps/avp)[]]                                                            DONE
  [[[media-libs/allegro]](https://packages.gentoo.org/packages/media-libs/allegro)[]]                                             DONE
  [[[media-libs/FusionSound]](https://packages.gentoo.org/packages/media-libs/FusionSound)[]]                                 IN PROGRESS    [[[bug #484250]](https://bugs.gentoo.org/show_bug.cgi?id=484250)[]]
  [[[media-libs/libcanberra]](https://packages.gentoo.org/packages/media-libs/libcanberra)[]]                                 TODO           see [forum thread](https://forums.gentoo.org/viewtopic-t-1013876-highlight-libcanberra.html)
  [[[media-libs/libsdl2]](https://packages.gentoo.org/packages/media-libs/libsdl2)[]]                                             DONE
  [[[media-libs/nas]](https://packages.gentoo.org/packages/media-libs/nas)[]]                                                         DONE           [[[bug #463942]](https://bugs.gentoo.org/show_bug.cgi?id=463942)[]]
  [[[media-libs/oyranos]](https://packages.gentoo.org/packages/media-libs/oyranos)[]]                                             DONE
  [[[media-libs/sbc]](https://packages.gentoo.org/packages/media-libs/sbc)[]]                                                         DONE           [[[bug #488282]](https://bugs.gentoo.org/show_bug.cgi?id=488282)[]]
  [[[media-sound/lash]](https://packages.gentoo.org/packages/media-sound/lash)[]]                                                   DONE           [[[bug #463360]](https://bugs.gentoo.org/show_bug.cgi?id=463360)[]]
  [[[net-fs/samba]](https://packages.gentoo.org/packages/net-fs/samba)[]]:4                                                             IN PROGRESS    [[[bug #534432]](https://bugs.gentoo.org/show_bug.cgi?id=534432)[]] waits for multilib python
  [[[net-libs/libasyncns]](https://packages.gentoo.org/packages/net-libs/libasyncns)[]]                                          DONE           [[[bug #488278]](https://bugs.gentoo.org/show_bug.cgi?id=488278)[]]
  [[[net-libs/libdom]](https://packages.gentoo.org/packages/net-libs/libdom)[]]                                                      DONE
  [[[net-libs/libndp]](https://packages.gentoo.org/packages/net-libs/libndp)[]]                                                      IN PROGRESS    [[[bug #545284]](https://bugs.gentoo.org/show_bug.cgi?id=545284)[]]
  [[[net-libs/polarssl]](https://packages.gentoo.org/packages/net-libs/polarssl)[]]                                                DONE
  [[[sys-apps/libselinux]](https://packages.gentoo.org/packages/sys-apps/libselinux)[]]                                          DONE           [[[bug #480960]](https://bugs.gentoo.org/show_bug.cgi?id=480960)[]]
  [[[sys-apps/lm_sensors]](https://packages.gentoo.org/packages/sys-apps/lm_sensors)[]]                                          IN PROGRESS    [[[bug #529684]](https://bugs.gentoo.org/show_bug.cgi?id=529684)[]]
  [[[sys-auth/nss-pam-ldapd]](https://packages.gentoo.org/packages/sys-auth/nss-pam-ldapd)[]]                                 DONE           [[[bug #549278]](https://bugs.gentoo.org/show_bug.cgi?id=549278)[]]
  [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]]                                                            DONE
  [[[sys-cluster/mpich]](https://packages.gentoo.org/packages/sys-cluster/mpich)[]]                                                IN PROGRESS    [[[bug #541746]](https://bugs.gentoo.org/show_bug.cgi?id=541746)[]]
  [[[sys-devel/autogen]](https://packages.gentoo.org/packages/sys-devel/autogen)[]]                                                IN PROGRESS    [[[bug #499378]](https://bugs.gentoo.org/show_bug.cgi?id=499378)[]]
  [[[sys-libs/libcap]](https://packages.gentoo.org/packages/sys-libs/libcap)[]]                                                      DONE           [[[bug #488286]](https://bugs.gentoo.org/show_bug.cgi?id=488286)[]]
  [[[www-client/netsurf]](https://packages.gentoo.org/packages/www-client/netsurf)[]]                                             DONE
  [[[www-plugins/nspluginwrapper]](https://packages.gentoo.org/packages/www-plugins/nspluginwrapper)[]]                  DONE
  [[[x11-drivers/ati-drivers]](https://packages.gentoo.org/packages/x11-drivers/ati-drivers)[]]                              IN PROGRESS    [[[bug #485722]](https://bugs.gentoo.org/show_bug.cgi?id=485722)[]]
  [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]]                     IN PROGRESS    [[[bug #485724]](https://bugs.gentoo.org/show_bug.cgi?id=485724)[]]
  [[[x11-libs/libpciaccess]](https://packages.gentoo.org/packages/x11-libs/libpciaccess)[]]                                    DONE
  [[[x11-libs/libSM]](https://packages.gentoo.org/packages/x11-libs/libSM)[]]                                                         DONE           fixed in 1.2.2-r1
  [[[x11-libs/tslib]](https://packages.gentoo.org/packages/x11-libs/tslib)[]]                                                         DONE           [[[bug #484254]](https://bugs.gentoo.org/show_bug.cgi?id=484254)[]]
  [[[x11-misc/virtualgl]](https://packages.gentoo.org/packages/x11-misc/virtualgl)[]]                                             DONE
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Binary packages]

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                                                       Status   Notes
  [[[app-emulation/crossover-bin]](https://packages.gentoo.org/packages/app-emulation/crossover-bin)[]]                                       DONE     Some deps are pulled only on x86 but supposedly not needed for multilib?
  [[[app-emulation/crossover-office-bin]](https://packages.gentoo.org/packages/app-emulation/crossover-office-bin)[]]                  DONE
  [[[app-emulation/crossover-office-pro-bin]](https://packages.gentoo.org/packages/app-emulation/crossover-office-pro-bin)[]]      DONE
  [[[app-emulation/emul-linux-x86-java]](https://packages.gentoo.org/packages/app-emulation/emul-linux-x86-java)[]]                     DONE     Needs to be compared with oracle-jre-bin
  [[[app-i18n/atokx3]](https://packages.gentoo.org/packages/app-i18n/atokx3)[]]                                                                           DONE     partially migrated?
  [[[app-text/acroread]](https://packages.gentoo.org/packages/app-text/acroread)[]]                                                                     DONE
  [[[dev-lang/dmd-bin]](https://packages.gentoo.org/packages/dev-lang/dmd-bin)[]]                                                                        DONE     no dependencies needed
  [[[dev-lang/rebol-bin]](https://packages.gentoo.org/packages/dev-lang/rebol-bin)[]]                                                                  DONE     no dependencies needed
  [[[dev-util/android-sdk-update-manager]](https://packages.gentoo.org/packages/dev-util/android-sdk-update-manager)[]]               DONE
  [[[games-action/awesomenauts]](https://packages.gentoo.org/packages/games-action/awesomenauts)[]]                                             DONE
  [[[games-action/beathazardultra]](https://packages.gentoo.org/packages/games-action/beathazardultra)[]]                                    DONE
  [[[games-action/cs2d]](https://packages.gentoo.org/packages/games-action/cs2d)[]]                                                                     DONE
  [[[games-action/descent3]](https://packages.gentoo.org/packages/games-action/descent3)[]]                                                         DONE
  [[[games-action/descent3-demo]](https://packages.gentoo.org/packages/games-action/descent3-demo)[]]                                          DONE
  [[[games-action/heretic2]](https://packages.gentoo.org/packages/games-action/heretic2)[]]                                                         DONE
  [[[games-action/heretic2-demo]](https://packages.gentoo.org/packages/games-action/heretic2-demo)[]]                                          DONE
  [[[games-action/hotline-miami]](https://packages.gentoo.org/packages/games-action/hotline-miami)[]]                                          DONE
  [[[games-action/intrusion2]](https://packages.gentoo.org/packages/games-action/intrusion2)[]]                                                   DONE
  [[[games-action/lugaru]](https://packages.gentoo.org/packages/games-action/lugaru)[]]                                                               DONE     open-source nowadays
  [[[games-action/lugaru-demo]](https://packages.gentoo.org/packages/games-action/lugaru-demo)[]]                                                DONE
  [[[games-action/mutantstorm-demo]](https://packages.gentoo.org/packages/games-action/mutantstorm-demo)[]]                                 DONE
  [[[games-action/phobiaii]](https://packages.gentoo.org/packages/games-action/phobiaii)[]]                                                         DONE
  [[[games-action/rune]](https://packages.gentoo.org/packages/games-action/rune)[]]                                                                     DONE
  [[[games-action/shadowgrounds-bin]](https://packages.gentoo.org/packages/games-action/shadowgrounds-bin)[]]                              DONE
  [[[games-action/shadowgrounds-survivor-bin]](https://packages.gentoo.org/packages/games-action/shadowgrounds-survivor-bin)[]]   DONE
  [[[games-action/solar2]](https://packages.gentoo.org/packages/games-action/solar2)[]]                                                               DONE
  [[[games-action/spacetripper-demo]](https://packages.gentoo.org/packages/games-action/spacetripper-demo)[]]                              DONE
  [[[games-action/swordandsworcery]](https://packages.gentoo.org/packages/games-action/swordandsworcery)[]]                                 DONE
  [[[games-action/trine2]](https://packages.gentoo.org/packages/games-action/trine2)[]]                                                               DONE
  [[[games-arcade/aquaria]](https://packages.gentoo.org/packages/games-arcade/aquaria)[]]                                                            DONE
  [[[games-arcade/barbarian-bin]](https://packages.gentoo.org/packages/games-arcade/barbarian-bin)[]]                                          DONE
  [[[games-arcade/dynamitejack]](https://packages.gentoo.org/packages/games-arcade/dynamitejack)[]]                                             DONE
  [[[games-arcade/gish-demo]](https://packages.gentoo.org/packages/games-arcade/gish-demo)[]]                                                      DONE     version bumped, new version has native 64bit
  [[[games-arcade/jardinains]](https://packages.gentoo.org/packages/games-arcade/jardinains)[]]                                                   DONE
  [[[games-arcade/thinktanks-demo]](https://packages.gentoo.org/packages/games-arcade/thinktanks-demo)[]]                                    DONE
  [[[games-fps/doom3]](https://packages.gentoo.org/packages/games-fps/doom3)[]]                                                                           DONE
  [[[games-fps/doom3-demo]](https://packages.gentoo.org/packages/games-fps/doom3-demo)[]]                                                            DONE
  [[[games-fps/enemy-territory]](https://packages.gentoo.org/packages/games-fps/enemy-territory)[]]                                             DONE
  [[[games-fps/enemy-territory-truecombat]](https://packages.gentoo.org/packages/games-fps/enemy-territory-truecombat)[]]            DONE     only libstdc++ dep
  [[[games-fps/etqw-bin]](https://packages.gentoo.org/packages/games-fps/etqw-bin)[]]                                                                  DONE
  [[[games-fps/etqw-demo]](https://packages.gentoo.org/packages/games-fps/etqw-demo)[]]                                                               DONE
  [[[games-fps/glxquake-bin]](https://packages.gentoo.org/packages/games-fps/glxquake-bin)[]]                                                      DONE
  [[[games-fps/legends]](https://packages.gentoo.org/packages/games-fps/legends)[]]                                                                     DONE
  [[[games-fps/postal2]](https://packages.gentoo.org/packages/games-fps/postal2)[]]                                                                     DONE
  [[[games-fps/postal2mp-demo]](https://packages.gentoo.org/packages/games-fps/postal2mp-demo)[]]                                                DONE
  [[[games-fps/quake3-bin]](https://packages.gentoo.org/packages/games-fps/quake3-bin)[]]                                                            DONE
  [[[games-fps/quake3-demo]](https://packages.gentoo.org/packages/games-fps/quake3-demo)[]]                                                         DONE
  [[[games-fps/quake4-bin]](https://packages.gentoo.org/packages/games-fps/quake4-bin)[]]                                                            DONE
  [[[games-fps/quake4-demo]](https://packages.gentoo.org/packages/games-fps/quake4-demo)[]]                                                         DONE
  [[[games-fps/rtcw]](https://packages.gentoo.org/packages/games-fps/rtcw)[]]                                                                              DONE
  [[[games-fps/rtcwmp-demo]](https://packages.gentoo.org/packages/games-fps/rtcwmp-demo)[]]                                                         DONE
  [[[games-fps/rtcwsp-demo]](https://packages.gentoo.org/packages/games-fps/rtcwsp-demo)[]]                                                         DONE
  [[[games-fps/serious-sam-tfe]](https://packages.gentoo.org/packages/games-fps/serious-sam-tfe)[]]                                             DONE
  [[[games-fps/serious-sam-tse]](https://packages.gentoo.org/packages/games-fps/serious-sam-tse)[]]                                             DONE
  [[[games-fps/soldieroffortune]](https://packages.gentoo.org/packages/games-fps/soldieroffortune)[]]                                          DONE     needs testing with someone that has the CD to confirm it works
  [[[games-fps/soldieroffortune-demo]](https://packages.gentoo.org/packages/games-fps/soldieroffortune-demo)[]]                           DONE
  [[[games-fps/unreal]](https://packages.gentoo.org/packages/games-fps/unreal)[]]                                                                        DONE
  [[[games-fps/unreal-tournament]](https://packages.gentoo.org/packages/games-fps/unreal-tournament)[]]                                       DONE
  [[[games-fps/unreal-tournament-goty]](https://packages.gentoo.org/packages/games-fps/unreal-tournament-goty)[]]                        DONE
  [[[games-fps/ut2003]](https://packages.gentoo.org/packages/games-fps/ut2003)[]]                                                                        DONE
  [[[games-fps/ut2003-demo]](https://packages.gentoo.org/packages/games-fps/ut2003-demo)[]]                                                         DONE
  [[[games-fps/ut2004-demo]](https://packages.gentoo.org/packages/games-fps/ut2004-demo)[]]                                                         DONE
  [[[games-kids/crayon-physics]](https://packages.gentoo.org/packages/games-kids/crayon-physics)[]]                                             DONE     Waiting for qtlibs
  [[[games-misc/little-inferno]](https://packages.gentoo.org/packages/games-misc/little-inferno)[]]                                             DONE
  [[[games-puzzle/drod-bin]](https://packages.gentoo.org/packages/games-puzzle/drod-bin)[]]                                                         DONE
  [[[games-puzzle/hoh-bin]](https://packages.gentoo.org/packages/games-puzzle/hoh-bin)[]]                                                            DONE
  [[[games-roguelike/adom]](https://packages.gentoo.org/packages/games-roguelike/adom)[]]                                                            DONE
  [[[games-rpg/dear-esther]](https://packages.gentoo.org/packages/games-rpg/dear-esther)[]]                                                         DONE
  [[[games-rpg/dungeon-defenders]](https://packages.gentoo.org/packages/games-rpg/dungeon-defenders)[]]                                       DONE
  [[[games-rpg/eschalon-book-1-demo]](https://packages.gentoo.org/packages/games-rpg/eschalon-book-1-demo)[]]                              DONE
  [[[games-rpg/nwmouse]](https://packages.gentoo.org/packages/games-rpg/nwmouse)[]]                                                                     DONE
  [[[games-rpg/nwn]](https://packages.gentoo.org/packages/games-rpg/nwn)[]]                                                                                 DONE
  [[[games-rpg/nwn-data]](https://packages.gentoo.org/packages/games-rpg/nwn-data)[]]                                                                  DONE
  [[[games-rpg/penumbra-collection]](https://packages.gentoo.org/packages/games-rpg/penumbra-collection)[]]                                 DONE
  [[[games-rpg/rain-slick]](https://packages.gentoo.org/packages/games-rpg/rain-slick)[]]                                                            DONE
  [[[games-rpg/sacred-gold]](https://packages.gentoo.org/packages/games-rpg/sacred-gold)[]]                                                         DONE
  [[[games-server/etqw-ded]](https://packages.gentoo.org/packages/games-server/etqw-ded)[]]                                                         DONE     emul-linux-x86 dep removed (no matching native dep)
  [[[games-server/nwn-ded]](https://packages.gentoo.org/packages/games-server/nwn-ded)[]]                                                            DONE     no dependencies needed
  [[[games-server/ut2003-ded]](https://packages.gentoo.org/packages/games-server/ut2003-ded)[]]                                                   DONE     no dependencies needed
  [[[games-simulation/bcs-demo]](https://packages.gentoo.org/packages/games-simulation/bcs-demo)[]]                                             DONE
  [[[games-strategy/coldwar]](https://packages.gentoo.org/packages/games-strategy/coldwar)[]]                                                      DONE
  [[[games-strategy/coldwar-demo]](https://packages.gentoo.org/packages/games-strategy/coldwar-demo)[]]                                       DONE
  [[[games-strategy/darwinia]](https://packages.gentoo.org/packages/games-strategy/darwinia)[]]                                                   DONE
  [[[games-strategy/darwinia-demo]](https://packages.gentoo.org/packages/games-strategy/darwinia-demo)[]]                                    DONE
  [[[games-strategy/dominions2]](https://packages.gentoo.org/packages/games-strategy/dominions2)[]]                                             DONE
  [[[games-strategy/dominions2-demo]](https://packages.gentoo.org/packages/games-strategy/dominions2-demo)[]]                              DONE
  [[[games-strategy/gorky17-demo]](https://packages.gentoo.org/packages/games-strategy/gorky17-demo)[]]                                       DONE
  [[[games-strategy/heroes3-demo]](https://packages.gentoo.org/packages/games-strategy/heroes3-demo)[]]                                       DONE
  [[[games-strategy/knights-demo]](https://packages.gentoo.org/packages/games-strategy/knights-demo)[]]                                       DONE
  [[[games-strategy/majesty-demo]](https://packages.gentoo.org/packages/games-strategy/majesty-demo)[]]                                       DONE
  [[[games-strategy/savage-bin]](https://packages.gentoo.org/packages/games-strategy/savage-bin)[]]                                             DONE
  [[[games-strategy/spaz]](https://packages.gentoo.org/packages/games-strategy/spaz)[]]                                                               DONE
  [[[mail-client/novell-groupwise-client]](https://packages.gentoo.org/packages/mail-client/novell-groupwise-client)[]]               DONE     app-emulation/emul-linux-x86-java only
  [[[media-gfx/nvidia-cg-toolkit]](https://packages.gentoo.org/packages/media-gfx/nvidia-cg-toolkit)[]]                                       DONE
  [[[media-libs/fmod]](https://packages.gentoo.org/packages/media-libs/fmod)[]]                                                                           DONE     only affects \<4, new versions support amd64 natively
  [[[media-sound/aucdtect]](https://packages.gentoo.org/packages/media-sound/aucdtect)[]]                                                            DONE     no dependencies needed
  [[[media-sound/ventrilo-server-bin]](https://packages.gentoo.org/packages/media-sound/ventrilo-server-bin)[]]                           DONE     no dependencies needed
  [[[media-video/binkplayer]](https://packages.gentoo.org/packages/media-video/binkplayer)[]]                                                      DONE
  [[[media-video/makemkv]](https://packages.gentoo.org/packages/media-video/makemkv)[]]                                                               DONE
  [[[media-video/tsmuxer]](https://packages.gentoo.org/packages/media-video/tsmuxer)[]]                                                               DONE     Waits for multilib Qt4
  [[[net-im/skype]](https://packages.gentoo.org/packages/net-im/skype)[]]                                                                                    DONE     Waits for multilib Qt4
  [[[net-im/skypetab-ng]](https://packages.gentoo.org/packages/net-im/skypetab-ng)[]]                                                                  DONE     Waits for multilib qt4
  [[[net-misc/icaclient]](https://packages.gentoo.org/packages/net-misc/icaclient)[]]                                                                  DONE
  [[[net-misc/teamviewer]](https://packages.gentoo.org/packages/net-misc/teamviewer)[]]                                                               DONE
  [[[net-print/cndrvcups-lb]](https://packages.gentoo.org/packages/net-print/cndrvcups-lb)[]]                                                      DONE
  [[[sci-chemistry/cara-bin]](https://packages.gentoo.org/packages/sci-chemistry/cara-bin)[]]                                                      DONE
  [[[sci-chemistry/icm]](https://packages.gentoo.org/packages/sci-chemistry/icm)[]]                                                                     DONE
  [[[sci-chemistry/icm-browser]](https://packages.gentoo.org/packages/sci-chemistry/icm-browser)[]]                                             DONE     ldd shows many more dependencies
  [[[sci-chemistry/xdsstat-bin]](https://packages.gentoo.org/packages/sci-chemistry/xdsstat-bin)[]]                                             DONE
  [[[sci-electronics/eagle]](https://packages.gentoo.org/packages/sci-electronics/eagle)[]]                                                         DONE
  [[[sys-libs/lib-compat-loki]](https://packages.gentoo.org/packages/sys-libs/lib-compat-loki)[]]                                                DONE
  [[[www-plugins/adobe-flash]](https://packages.gentoo.org/packages/www-plugins/adobe-flash)[]]                                                   DONE     [[[bug #480918]](https://bugs.gentoo.org/show_bug.cgi?id=480918)[]]
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Profile fixing status]

Legend:

1.  ABI, DEFAULT_ABI --- whether the profile sets ABI and DEFAULT_ABI to a consistent value other than \'default\',
2.  MULTILIB_ABIS --- whether the profile sets MULTILIB_ABIS,
3.  IUSE_IMPLICIT --- whether the profile makes the native ABI flag implicit,
4.  use.force, use.mask --- whether the profile unmasks flags matching MULTILIB_ABIS and forces the flag for native ABI,
5.  def. ABI\_\* --- whether the profile sets default value of ABI\_\* flags for packages that don\'t use use.force.

  --------------------------------------------- ------------------ --------------- --------------- --------------------- --------------
  Profile                                       ABI, DEFAULT_ABI   MULTILIB_ABIS   IUSE_IMPLICIT   use.force, use.mask   def. ABI\_\*
  Main architecture profiles
  arch/amd64                                    Yes                Yes             Yes             Yes                   Yes
  arch/amd64/no-multilib                        inh.               Yes             inh.            Yes                   inh.
  arch/amd64/x32                                Yes                Yes             Yes             Yes                   Yes
  arch/amd64-fbsd                               Yes                Yes             Yes             Yes                   Yes
  arch/arm                                      Yes                Yes             No              No                    No
  arch/arm64                                    Yes                Yes             No              No                    No
  arch/mips                                     Yes                Yes             Yes             Yes                   Yes
  arch/mips/mips64/n32                          Yes                Yes             Yes             Yes                   Yes
  arch/mips/mips64/n64                          Yes                Yes             Yes             Yes                   Yes
  arch/mips/mips64/multilib/n32                 Yes                Yes             Yes             Yes                   Yes
  arch/mips/mips64/multilib/n64                 Yes                Yes             Yes             Yes                   Yes
  arch/mips/mips64/multilib/o32                 Yes                Yes             Yes             Yes                   Yes
  arch/mips/mipsel                              Yes                Yes             Yes             Yes                   Yes
  arch/mips/mipsel/mips64el/n32                 Yes                Yes             Yes             Yes                   Yes
  arch/mips/mipsel/mips64el/n64                 Yes                Yes             Yes             Yes                   Yes
  arch/mips/mipsel/mips64el/multilib/n32        Yes                Yes             Yes             Yes                   Yes
  arch/mips/mipsel/mips64el/multilib/n64        Yes                Yes             Yes             Yes                   Yes
  arch/mips/mipsel/mips64el/multilib/o32        Yes                Yes             Yes             Yes                   Yes
  arch/powerpc/ppc32                            Yes                Yes             Yes             Yes                   Yes
  arch/powerpc/ppc64                            Yes                Yes             Yes             Yes                   Yes
  arch/powerpc/ppc64/32ul                       Yes                Yes             Yes             Yes                   Yes
  arch/s390                                     Yes                Yes             Yes             Yes                   Yes
  arch/s390/s390x                               Yes                Yes             Yes             Yes                   Yes
  arch/sparc                                    Yes                Yes             No              No                    No
  arch/sparc-fbsd                               No                 No              No              No                    No
  arch/x86                                      Yes                Yes             Yes             Yes                   Yes
  arch/x86-fbsd                                 Yes                Yes             Yes             Yes                   Yes
  Non-multilib architectures
  arch/alpha                                    Yes
  arch/hppa                                     Yes
  arch/ia64                                     Yes
  arch/m68k                                     Yes
  arch/sh                                       Yes
  Profiles that do not inherit from arch tree
  hardened/linux/musl/amd64                     Yes                Yes             Yes             Yes                   No
  hardened/linux/musl/arm                       No                 No              No              No                    No
  hardened/linux/musl/mips                      Yes                Yes             Yes             Yes                   No
  hardened/linux/musl/mips/mipsel               Yes                Yes             Yes             Yes                   No
  hardened/linux/musl/x86                       Yes                Yes             Yes             Yes                   No
  hardened/linux/uclibc/amd64                   Yes                Yes             Yes             Yes                   No
  hardened/linux/uclibc/arm                     No                 No              No              No                    No
  hardened/linux/uclibc/mips                    Yes                Yes             Yes             Yes                   No
  hardened/linux/uclibc/mips/mipsel             Yes                Yes             Yes             Yes                   No
  hardened/linux/uclibc/ppc                     Yes                Yes             Yes             Yes                   No
  hardened/linux/uclibc/x86                     Yes                Yes             Yes             Yes                   No
  --------------------------------------------- ------------------ --------------- --------------- --------------------- --------------