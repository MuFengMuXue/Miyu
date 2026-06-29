Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Steam/es "Steam (22% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Steam/hu "Steam (83% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Steam/ru "Steam (37% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Steam/ja "Steam (86% translated)")

**Resources**

[[]][Home](https://store.steampowered.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Steam_(software) "wikipedia:Steam (software)")

**Steam** is a video game digital distribution service by Valve. Steam offers digital rights management (DRM), matchmaking servers, video streaming, and social networking services. It also provides the user with installation and automatic updating of games, and community features such as friends lists and groups, cloud saving, and in-game voice and chat functionality.

The Steam client is not open source software, therefore each user must accept the [Steam Subscriber Agreement](https://store.steampowered.com/subscriber_agreement/) before using the software, then typically accept [EULAs](https://en.wikipedia.org/wiki/End-user_license_agreement "wikipedia:End-user license agreement") or [Terms of Use](https://en.wikipedia.org/wiki/Terms_of_service "wikipedia:Terms of service") agreements for each particular title accessed through the Steam client.

Valve Corporation has collaborated with open source software organizations such as CodeWeavers ([Wine](https://wiki.gentoo.org/wiki/Wine "Wine"))^[\[1\]](#cite_note-1)^ in order to make closed source games possible to run on open source operating systems.

## Contents

-   [[1] [Game Compatibility]](#Game_Compatibility)
-   [[2] [Prerequisites]](#Prerequisites)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [File Descriptors Limit]](#File_Descriptors_Limit)
    -   [[2.3] [max_map_count]](#max_map_count)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Emerge (recommended)]](#Emerge_.28recommended.29)
        -   [[3.1.1] [Troubleshooting]](#Troubleshooting)
            -   [[3.1.1.1] [Migrate from flatpak to the emerge recommended install]](#Migrate_from_flatpak_to_the_emerge_recommended_install)
    -   [[3.2] [Flatpak]](#Flatpak)
    -   [[3.3] [Manual]](#Manual)
        -   [[3.3.1] [Dependencies]](#Dependencies)
        -   [[3.3.2] [USE flags]](#USE_flags)
        -   [[3.3.3] [Default installer]](#Default_installer)
        -   [[3.3.4] [Alternative installer]](#Alternative_installer)
-   [[4] [Chroot]](#Chroot)
    -   [[4.1] [Systemd and chroot]](#Systemd_and_chroot)
-   [[5] [Easy Anti Cheat Support]](#Easy_Anti_Cheat_Support)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Removing a manual installation]](#Removing_a_manual_installation)
    -   [[6.2] [Removing an external repository installation]](#Removing_an_external_repository_installation)
-   [[7] [Troubleshooting]](#Troubleshooting_2)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)
-   [[10] [References]](#References)

## [Game Compatibility]

With the popularization of the [Steam Deck](https://en.wikipedia.org/wiki/Steam_Deck "wikipedia:Steam Deck"), playing Steam games on Linux has grown considerably in recent years^[\[2\]](#cite_note-2)^. Game developers are increasingly incentivized to support Linux. Native Linux games can be identified with the SteamOS icon in the Store. For games without native support, Valve maintains [Proton](https://github.com/ValveSoftware/Proton/), built on [Wine](https://wiki.gentoo.org/wiki/Wine "Wine"), which integrates with the client and provides an easy-to-use compatibility layer for Windows-only games on a recent Linux OS. Users who prefer bleeding-edge versions over stability may consider an actively community-maintained fork of Proton called [GE-Proton](https://github.com/GloriousEggroll/proton-ge-custom).

** Important**\
Proton is open source and thus can be built from source, but it is highly recommended to use versions of Proton provided by the Steam client^[\[3\]](#cite_note-3)^. Proton can be enabled for each game through its properties under the Compatibility tab.

** Tip**\
Community-maintained [ProtonDB](https://www.protondb.com/) (similar to [Wine AppDB](https://appdb.winehq.org/)) monitors game compatibility with Steam Deck / Proton and similar emulation tools based on feedback from its users.

## [Prerequisites]

Steam provides 32-bit environment for most of supported games, so client itself requires a [multilib](https://wiki.gentoo.org/wiki/Multilib "Multilib") [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") on **[amd64]**. That is, during Gentoo installation, when choosing profiles the [no-multilib](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#No-multilib "Handbook:AMD64/Full/Installation") option was **not** selected. This prerequisite can be ignored if installing Steam in a [chroot](https://wiki.gentoo.org/wiki/Steam#Chroot "Steam").

The Steam browser is no longer supported on 32-bit Linux distributions, and is disabled when viewing the *Store*, *Community*, or *User Profile* tabs in the Steam client^[\[4\]](#cite_note-32bitonly-4)^, so only available architecture is **[amd64]**.

### [Kernel]

Steam expects that [/dev/shm], which requires kernel [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs") support, is mounted prior to being started. [/dev/shm] should be mounted automatically by [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") during boot, but can also be mounted explicitly via [/etc/fstab].

[FILE] **`/etc/fstab`**

    # To limit the size add e.g. size=1G to opts (recommended at least 2G, default is 50%)
    # Please note that lower setting may randomly crash Steam and/or games.

    #<fs>      <mountpoint>    <type> <opts>             <dump/pass>
    shm        /dev/shm        tmpfs        nodev,nosuid,noexec  0 0

The following kernel option has to be set, otherwise Steam may fail to start with the error message: \"The futex facility returned an unexpected error code.\"

[KERNEL] **Allow 32-bit time_t for Steam\'s 32-bit compatibility**

    General architecture-dependent options  --->
      [*] Provide system calls for 32-bit time_t Search for <code>CONFIG_COMPAT_32BIT_TIME</code> to find this item.

Enable user level driver support if controller support is desired.

[KERNEL] **Enable user level drivers for input**

    Device Drivers  --->
      Input device support  --->
        -*- Generic input layer (needed for keyboard, mouse, ...) Search for <code>CONFIG_INPUT</code> to find this item.
          [*] Miscellaneous devices Search for <code>CONFIG_INPUT_MISC</code> to find this item.  --->
            <*> User level driver support Search for <code>CONFIG_INPUT_UINPUT</code> to find this item.

Enable user namespace support in order to support launching games in Compatibility mode (i.e. with Proton):

[KERNEL] **Enable User namespace**

    General setup --->
        [*] Namespaces support Search for <code>CONFIG_NAMESPACES</code> to find this item. --->
            [*] User namespace Search for <code>CONFIG_USER_NS</code> to find this item.

Enable NTSYNC when using GE-Proton or Proton 11 or newer:

[KERNEL] **Enable NTSYNC**

    Device Drivers --->
        Misc devices --->
            [*] NT synchronization primitive emulation Search for <code>CONFIG_NTSYNC</code> to find this item.

### [File Descriptors Limit]

On non-systemd configurations the default PAM hard file descriptors limit of 4096 generates the following warning in the Proton debug log:

    WARNING: Low file descriptor limit: 4096 (see https://github.com/ValveSoftware/Proton/wiki/File-Descriptors)

The limit on the number of file descriptors that can be opened by a user logged on via PAM is controlled by the [pam_limits.so] module and the hard limit can be checked by a user at runtime with the [ulimit -Hn] command.

Proton will not produce the warning if the hard limit is increased to 524288 or higher.

Higher limit can be specified in the [/etc/security/limits.conf] file or in a configuration file in the [/etc/security/limits.d/] directory, for example:

[FILE] **`/etc/security/limits.d/26-steam-nofile.conf`**

    *               hard    nofile             524288

This config will allow all users and groups to use the new limit. To set the new limit to a particular user only, the `*` in the beginning can be replaced with a specific username.

### [max_map_count]

In Linux kernel the default [max_map_count](https://docs.kernel.org/admin-guide/sysctl/vm.html#max-map-count) limit of 65530 on the maximum number of memory map areas a process may have, generates the following warning in the Proton debug log:

    WARNING: Low /proc/sys/vm/max_map_count: 65530 will prevent some games from working

Proton will not produce the warning if the limit is increased to 1048576 or higher.

At runtime the limit can be changed with the following command:

`root `[`#`]`sysctl --write vm.max_map_count=1048576`

A configuration file in the [/etc/sysctl.d/] directory can be used to set the limit during boot time, for example:

[FILE] **`/etc/sysctl.d/steam.conf`**

    vm.max_map_count = 1048576

## [Installation]

The Steam installer downloads and installs the Steam client to the user\'s home directory. This prevents Portage from managing the Steam client updates or the software installed by it. The Steam client is solely responsible for managing software installation and updates.

** Important**\
The instructions throughout this page use the typical Steam installation directory [\~/.local/share/Steam].

### [][Emerge (recommended)]

The [steam-launcher] ebuild is available from the [steam-overlay](https://github.com/anyc/steam-overlay) repository, which is Gentoo\'s primary repository for the Steam client and Steam-based games. The steam-overlay repository can be added manually or with repository management tools like [eselect-repository].

Install [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]]:

`root `[`#`]`emerge --ask --noreplace app-eselect/eselect-repository dev-vcs/git`

Add the Steam repository:

`root `[`#`]`eselect repository enable steam-overlay`

Then sync with either specifically [emaint](https://wiki.gentoo.org/wiki/Emaint "Emaint"):

`root `[`#`]`emaint sync -r steam-overlay`

or

`root `[`#`]`emerge --sync`

Due to the Proton runtime built into Steam, 32-bit binaries of most dependencies are included within the Steam installation. Some system dependencies remain however, but Portage should prompt for them. These packages should be added to [/etc/portage/package.use/steam] with their `abi_x86_32` USE flag enabled. Some required changes include:

[FILE] **`/etc/portage/package.use/steam`**

    app-accessibility/at-spi2-core    abi_x86_32
    app-arch/bzip2                    abi_x86_32
    app-arch/lz4                      abi_x86_32
    app-arch/xz-utils                 abi_x86_32
    app-arch/zstd                     abi_x86_32
    app-crypt/p11-kit                 abi_x86_32
    dev-db/sqlite                     abi_x86_32
    dev-lang/rust                     abi_x86_32
    dev-lang/rust-bin                 abi_x86_32
    dev-libs/dbus-glib                abi_x86_32
    dev-libs/elfutils                 abi_x86_32
    dev-libs/expat                    abi_x86_32
    dev-libs/fribidi                  abi_x86_32
    dev-libs/glib                     abi_x86_32
    dev-libs/gmp                      abi_x86_32
    dev-libs/icu                      abi_x86_32
    dev-libs/json-glib                abi_x86_32
    dev-libs/leancrypto               abi_x86_32
    dev-libs/libevdev                 abi_x86_32
    dev-libs/libffi                   abi_x86_32
    dev-libs/libgcrypt                abi_x86_32
    dev-libs/libgpg-error             abi_x86_32
    dev-libs/libgudev                 abi_x86_32
    dev-libs/libgusb                  abi_x86_32
    dev-libs/libpcre2                 abi_x86_32
    dev-libs/libtasn1                 abi_x86_32
    dev-libs/libunistring             abi_x86_32
    dev-libs/libusb                   abi_x86_32
    dev-libs/libxml2                  abi_x86_32
    dev-libs/lzo                      abi_x86_32
    dev-libs/nettle                   abi_x86_32
    dev-libs/nspr                     abi_x86_32
    dev-libs/nss                      abi_x86_32
    dev-libs/openssl                  abi_x86_32
    dev-libs/wayland                  abi_x86_32
    dev-util/glslang                  abi_x86_32
    dev-util/spirv-tools              abi_x86_32
    dev-util/sysprof-capture          abi_x86_32
    dev-util/vulkan-utility-libraries abi_x86_32
    gnome-base/librsvg                abi_x86_32
    gui-libs/libdecor                 abi_x86_32
    llvm-core/clang                   abi_x86_32
    llvm-core/llvm                    abi_x86_32
    media-gfx/graphite2               abi_x86_32
    media-libs/alsa-lib               abi_x86_32
    media-libs/flac                   abi_x86_32
    media-libs/fontconfig             abi_x86_32
    media-libs/freetype               abi_x86_32
    media-libs/glu                    abi_x86_32
    media-libs/harfbuzz               abi_x86_32
    media-libs/lcms                   abi_x86_32
    media-libs/libdisplay-info        abi_x86_32
    media-libs/libepoxy               abi_x86_32
    media-libs/libglvnd               abi_x86_32
    media-libs/libjpeg-turbo          abi_x86_32
    media-libs/libogg                 abi_x86_32
    media-libs/libpng                 abi_x86_32
    media-libs/libpulse               abi_x86_32
    media-libs/libsdl2                abi_x86_32
    media-libs/libsndfile             abi_x86_32
    media-libs/libva                  abi_x86_32
    media-libs/libvorbis              abi_x86_32
    media-libs/libwebp                abi_x86_32
    media-libs/mesa                   abi_x86_32
    media-libs/openal                 abi_x86_32
    media-libs/opus                   abi_x86_32
    media-libs/tiff                   abi_x86_32
    media-libs/vulkan-layers          abi_x86_32
    media-libs/vulkan-loader          abi_x86_32 layers
    media-sound/lame                  abi_x86_32
    media-sound/mpg123-base           abi_x86_32
    media-video/pipewire              abi_x86_32
    net-dns/c-ares                    abi_x86_32
    net-dns/libidn2                   abi_x86_32
    net-libs/gnutls                   abi_x86_32
    net-libs/libasyncns               abi_x86_32
    net-libs/libndp                   abi_x86_32
    net-libs/libpsl                   abi_x86_32
    net-libs/nghttp2                  abi_x86_32
    net-libs/nghttp3                  abi_x86_32
    net-libs/ngtcp2                   abi_x86_32
    net-misc/curl                     abi_x86_32
    net-misc/networkmanager           abi_x86_32
    net-print/cups                    abi_x86_32
    sys-apps/dbus                     abi_x86_32
    sys-apps/lm-sensors               abi_x86_32
    sys-apps/systemd                  abi_x86_32
    sys-apps/systemd-utils            abi_x86_32
    sys-apps/util-linux               abi_x86_32
    sys-libs/gdbm                     abi_x86_32
    sys-libs/gpm                      abi_x86_32
    sys-libs/libcap                   abi_x86_32
    sys-libs/libudev-compat           abi_x86_32
    sys-libs/ncurses                  abi_x86_32
    sys-libs/pam                      abi_x86_32
    sys-libs/readline                 abi_x86_32
    sys-libs/zlib                     abi_x86_32
    virtual/glu                       abi_x86_32
    virtual/libelf                    abi_x86_32
    virtual/libiconv                  abi_x86_32
    virtual/libintl                   abi_x86_32
    virtual/libudev                   abi_x86_32
    virtual/libusb                    abi_x86_32
    virtual/opengl                    abi_x86_32
    virtual/zlib                      abi_x86_32
    x11-libs/cairo                    abi_x86_32
    x11-libs/extest                   abi_x86_32
    x11-libs/gdk-pixbuf               abi_x86_32
    x11-libs/gtk+                     abi_x86_32
    x11-libs/libdrm                   abi_x86_32
    x11-libs/libICE                   abi_x86_32
    x11-libs/libpciaccess             abi_x86_32
    x11-libs/libSM                    abi_x86_32
    x11-libs/libvdpau                 abi_x86_32
    x11-libs/libX11                   abi_x86_32
    x11-libs/libXau                   abi_x86_32
    x11-libs/libxcb                   abi_x86_32
    x11-libs/libXcomposite            abi_x86_32
    x11-libs/libXcursor               abi_x86_32
    x11-libs/libXdamage               abi_x86_32
    x11-libs/libXdmcp                 abi_x86_32
    x11-libs/libXext                  abi_x86_32
    x11-libs/libXfixes                abi_x86_32
    x11-libs/libXft                   abi_x86_32
    x11-libs/libXi                    abi_x86_32
    x11-libs/libXinerama              abi_x86_32
    x11-libs/libxkbcommon             abi_x86_32
    x11-libs/libXrandr                abi_x86_32
    x11-libs/libXrender               abi_x86_32
    x11-libs/libXScrnSaver            abi_x86_32
    x11-libs/libxshmfence             abi_x86_32
    x11-libs/libXtst                  abi_x86_32
    x11-libs/libXxf86vm               abi_x86_32
    x11-libs/pango                    abi_x86_32
    x11-libs/pixman                   abi_x86_32
    x11-libs/xcb-util-keysyms         abi_x86_32
    x11-misc/colord                   abi_x86_32

For users with an Nvidia card using the proprietary drivers, these packages should be added to [/etc/portage/package.use/steam] with their `abi_x86_32` USE flag enabled as well:

[FILE] **`/etc/portage/package.use/steam`**

    gui-libs/egl-gbm            abi_x86_32
    gui-libs/egl-wayland        abi_x86_32
    gui-libs/egl-wayland2       abi_x86_32
    gui-libs/egl-x11            abi_x86_32
    x11-drivers/nvidia-drivers  abi_x86_32

Add the steam overlay to [package.accept_keywords]:

[FILE] **`/etc/portage/package.accept_keywords/steam`**

    */*::steam-overlay
    games-util/game-device-udev-rules
    sys-libs/libudev-compat

Now read Steam\'s license terms located on /var/db/repos/steam-overlay/licenses/ValveSteamLicense and if you agree with them, then add it to portage:

[FILE] **`/etc/portage/package.license/steam`**

    games-util/steam-launcher ValveSteamLicense

The overlay enables the Steam runtime by default. If you\'d like to rely solely on Gentoo packages, then disable the `steamruntime` USE flag. Use the [esteam] utility later to scan your installed native Linux games for additional Gentoo packages required by them. Note that Gentoo packages do not cover the entirety of the runtime, so a small number of games may not work.

Once the repository has been added, install the [steam-launcher] ebuild:

** Important**\
Newer installed systems are likely to run into a circular dependencies due to Steam needing `ABI_X86_32` being set. This is easily resolved by following the first item in the [Steam](https://wiki.gentoo.org/wiki/Steam#Troubleshooting "Steam") troubleshooting section below.

`root `[`#`]`emerge --ask games-util/steam-launcher`

#### [Troubleshooting]

If Steam is failing to emerge due to [circular dependencies](https://wiki.gentoo.org/wiki/Portage/Help/Circular_dependencies "Portage/Help/Circular dependencies") with [ncurses] and [gpm], try:

`root `[`#`]`USE="-gpm" emerge --ask --oneshot sys-libs/ncurses `

`root `[`#`]`emerge --ask games-util/steam-launcher `

`root `[`#`]`emerge --ask --oneshot sys-libs/ncurses gpm `

If Steam is failing to emerge due to [circular dependencies](https://wiki.gentoo.org/wiki/Portage/Help/Circular_dependencies "Portage/Help/Circular dependencies") with [harfbuzz] and [freetype], try:

`root `[`#`]`USE="-harfbuzz" emerge --ask --oneshot media-libs/freetype media-libs/sdl2-ttf `

`root `[`#`]`emerge --ask games-util/steam-launcher `

`root `[`#`]`emerge --ask --oneshot media-libs/freetype media-libs/sdl2-ttf media-libs/harfbuzz `

** Tip**\
More information on circular dependencies and the reason they can occur can be found at [Portage/Help](https://wiki.gentoo.org/wiki/Portage/Help "Portage/Help")

On pure Wayland systems with a global `-X` use flag, installing `steam-launcher` may get blocked by `x11-libs/cairo`. In such a case, `dev-cpp/cairomm` will likely be installed without support for X as well, and an `X` use flag will need to be added to both.\
Furthermore, if your Wayland compositor does not support XWayland natively, `gui-apps/xwayland-satellite` is needed to run Steam.

If SteamUpdateUI fails to launch with \"An X error has occured\" it may indicate the user is not in the video group.

`root `[`#`]`gpasswd -a larry video`

##### [Migrate from flatpak to the emerge recommended install]

In order to migrate from flatpak to the recommended emerge method. The instructions for the emerge install must be followed, then the flatpak-packaged steam files must be moved to the default Gentoo filesystem location:

`user `[`$`]`mv ~/.var/app/com.valvesoftware.Steam/.local/share/Steam ~/.local/share/`

Some games store user data in [\~/.var/app/com.valvesoftware.Steam/.local/share/] for examples mods or screenshots. These directories also need to be moved for a complete migration. For example to move Euro Truck Simulator 2 user data :

`user `[`$`]`mv ~/.var/app/com.valvesoftware.Steam/.local/share/Euro\ Truck\ Simulator\ 2 ~/.local/share/`

Finally the flatpak can be uninstalled

`user `[`$`]`flatpak uninstall com.valvesoftware.Steam`

### [Flatpak]

A quite simple, fast, and clean method (e.g. 32-bit dependencies do not need to be compiled) of installing Steam is to use the [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak") package `com.valvesoftware.Steam` from [Flathub](https://flathub.org/apps/details/com.valvesoftware.Steam) (also installing necessary [udev rules](https://wiki.gentoo.org/wiki/Udev#Rules "Udev") for game controllers):

`root `[`#`]`USE="X" emerge --ask sys-apps/flatpak `

`root `[`#`]`emerge --ask games-util/game-device-udev-rules `

** Note**\
As explained at [Flatpak](https://wiki.gentoo.org/wiki/Flatpak#Installed_applications.27_desktop_entries_do_not_show_in_launchers "Flatpak"), rebooting the system is required for application icons to show up in the GUI menu.

Beside, Flatpak\'s first command below can also return an error about these directories:

[/var/lib/flatpak/exports/share]

[/home/user/.local/share/flatpak/exports/share]

They are \"*not in the search path set by the XDG_DATA_DIRS environment variable, so applications installed by Flatpak may not appear on the desktop until the session is restarted*\".

Creating them and adding them to XDG_DATA_DIRS doesn\'t works either.

`user `[`$`]`flatpak remote-add --if-not-exists flathub `[`https://dl.flathub.org/repo/flathub.flatpakrepo`](https://dl.flathub.org/repo/flathub.flatpakrepo)` `

`user `[`$`]`flatpak install flathub com.valvesoftware.Steam `

`user `[`$`]`flatpak run com.valvesoftware.Steam `

Steam will update itself and install its files in the [\~/.var/app/com.valvesoftware.Steam] directory.

### [Manual]

** Warning**\
Installing Steam manually is not recommended as various fixes are not applied automatically^[\[5\]](#cite_note-5)^. Please consider installing Steam through [emerge] instead as described above!

#### [Dependencies]

** Note**\
The following dependencies may be outdated and require verification. Some of the dependencies may be bundled by the Steam runtime, in which case the system libraries will *not* be used.

Create the following set of required Steam dependencies:

[FILE] **`/etc/portage/sets/steam`**

    # mandatory!
    dev-libs/glib:2
    dev-libs/libgcrypt
    dev-libs/nspr
    dev-libs/nss
    gnome-base/gconf
    gnome-extra/zenity
    media-libs/alsa-lib
    media-libs/fontconfig
    media-libs/freetype:2
    media-libs/libjpeg-turbo
    media-libs/libogg
    media-libs/libpng-compat:1.2
    media-libs/libsdl
    media-libs/libtheora
    media-libs/libvorbis
    media-libs/openal
    net-misc/curl
    net-print/cups
    sys-apps/dbus
    virtual/libusb:1
    virtual/opengl
    x11-libs/cairo
    x11-libs/gdk-pixbuf
    x11-libs/gtk+:2
    x11-libs/libX11
    x11-libs/libXScrnSaver
    x11-libs/libXext
    x11-libs/libXfixes
    x11-libs/libXi
    x11-libs/libXrandr
    x11-libs/libXrender
    x11-libs/pango
    x11-libs/pixman

    # optional
    media-sound/pulseaudio
    net-misc/networkmanager
    x11-misc/xdg-user-dirs

And then run:

`root `[`#`]`emerge --ask --noreplace @steam`

** Warning**\
Do not run [emerge \--unmerge \@steam] to remove Steam as it may make the system unusable. Instead use [emerge \--ask \--depclean \@steam] for this method.

#### [USE flags]

[] Some of the information in this section may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Steam&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

This section contains references to the [obsolete *sys-fs/udev* package](https://public-inbox.gentoo.org/gentoo-dev/ZL6xwI9xXAQmupbd@naomi/), so it would appear that this list is at least partially out of date. Could anyone who uses Steam and knows how to fix this please bring it up to date?

To enable the required USE flags for Steam dependencies under **[amd64]**, add the following file:

[FILE] **`/etc/portage/package.use/steam`**

    app-arch/bzip2 abi_x86_32
    app-arch/zstd abi_x86_32
    dev-db/sqlite abi_x86_32
    dev-libs/atk abi_x86_32
    dev-libs/expat abi_x86_32
    dev-libs/fribidi abi_x86_32
    dev-libs/glib abi_x86_32
    dev-libs/gmp abi_x86_32
    dev-libs/icu abi_x86_32
    dev-libs/libcroco abi_x86_32
    dev-libs/libffi abi_x86_32
    dev-libs/libpcre abi_x86_32
    dev-libs/libpthread-stubs abi_x86_32
    dev-libs/libtasn1 abi_x86_32
    dev-libs/libunistring abi_x86_32
    dev-libs/libxml2 abi_x86_32
    dev-libs/lzo abi_x86_32
    dev-libs/nettle abi_x86_32
    dev-libs/nspr abi_x86_32
    dev-libs/nss abi_x86_32
    dev-libs/openssl abi_x86_32
    dev-libs/wayland abi_x86_32
    dev-util/pkgconfig abi_x86_32
    dev-util/wayland-scanner abi_x86_32
    gnome-base/librsvg abi_x86_32
    llvm-core/llvm abi_x86_32
    media-gfx/graphite2 abi_x86_32
    media-libs/fontconfig abi_x86_32
    media-libs/freetype abi_x86_32
    media-libs/harfbuzz abi_x86_32
    media-libs/libpng abi_x86_32
    media-libs/mesa abi_x86_32
    media-libs/openal abi_x86_32
    media-libs/tiff abi_x86_32
    net-dns/libidn2 abi_x86_32
    net-libs/gnutls abi_x86_32
    net-misc/curl abi_x86_32
    net-nds/openldap abi_x86_32
    net-print/cups abi_x86_32
    sys-apps/attr abi_x86_32
    sys-apps/dbus abi_x86_32
    sys-apps/util-linux abi_x86_32
    sys-devel/gettext abi_x86_32
    sys-fs/udev abi_x86_32
    sys-libs/binutils-libs abi_x86_32
    sys-libs/gpm abi_x86_32
    sys-libs/ncurses abi_x86_32
    sys-libs/readline abi_x86_32
    sys-libs/zlib abi_x86_32
    virtual/libffi abi_x86_32
    virtual/libiconv abi_x86_32
    virtual/libudev abi_x86_32
    virtual/opengl abi_x86_32
    virtual/pkgconfig abi_x86_32
    x11-libs/cairo abi_x86_32
    x11-libs/gdk-pixbuf abi_x86_32
    x11-libs/gtk+:2 abi_x86_32
    x11-libs/libX11 abi_x86_32
    x11-libs/libXScrnSaver abi_x86_32
    x11-libs/libXau abi_x86_32
    x11-libs/libXcomposite abi_x86_32
    x11-libs/libXcursor abi_x86_32
    x11-libs/libXdamage abi_x86_32
    x11-libs/libXdmcp abi_x86_32
    x11-libs/libXext abi_x86_32
    x11-libs/libXfixes abi_x86_32
    x11-libs/libXft abi_x86_32
    x11-libs/libXi abi_x86_32
    x11-libs/libXinerama abi_x86_32
    x11-libs/libXrandr abi_x86_32
    x11-libs/libXrender abi_x86_32
    x11-libs/libXxf86vm abi_x86_32
    x11-libs/libdrm abi_x86_32
    x11-libs/libpciaccess abi_x86_32
    x11-libs/libxcb abi_x86_32
    x11-libs/libxshmfence abi_x86_32
    x11-libs/pango abi_x86_32
    x11-libs/pixman abi_x86_32
    x11-proto/damageproto abi_x86_32
    x11-proto/dri2proto abi_x86_32
    x11-proto/dri3proto abi_x86_32
    x11-proto/fixesproto abi_x86_32
    x11-proto/glproto abi_x86_32
    x11-proto/inputproto abi_x86_32
    x11-proto/kbproto abi_x86_32
    x11-proto/presentproto abi_x86_32
    x11-proto/xcb-proto abi_x86_32
    x11-proto/xextproto abi_x86_32
    x11-proto/xf86bigfontproto abi_x86_32
    x11-proto/xf86driproto abi_x86_32
    x11-proto/xf86vidmodeproto abi_x86_32
    x11-proto/xproto abi_x86_32

    # If using proprietary Nvidia drivers, include these as well
    media-libs/libglvnd abi_x86_32
    x11-drivers/nvidia-drivers abi_x86_32

Update the system:

`root `[`#`]`emerge --ask --changed-use --deep @world`

** Note**\
Users may receive an error citing circular dependencies due to gpm and ncurses. If this is the case, add `-gpm` to [[[sys-libs/ncurses]](https://packages.gentoo.org/packages/sys-libs/ncurses)[]] and update the [\@world] set once more.

#### [Default installer]

Fetch and extract the Steam installer:

`user `[`$`]`wget https://repo.steampowered.com/steam/pool/steam/s/steam/steam_1.0.0.78.tar.gz `

`user `[`$`]`tar -xvzpf steam_1.0.0.*.tar.gz `

Run the Steam installer:

`user `[`$`]`cd steam-launcher `

`user `[`$`]`./steam `

** Note**\
After invoking [./steam] a libGL error may appear. See [Steam/Client troubleshooting](https://wiki.gentoo.org/wiki/Steam/Client_troubleshooting#libGL_fails_to_load_driver "Steam/Client troubleshooting") for the resolution.

If the Steam client crashes, try running:

`user `[`$`]`./steam -textclient`

Running Steam with the `-textclient` option may be necessary each time the client wants to update.

Install the above Steam installer script:

`root `[`#`]`cp steam /usr/local/bin`

Steam can be started with:

`user `[`$`]`steam`

#### [Alternative installer]

The following installation method is almost identical to the [Default installer](https://wiki.gentoo.org/wiki/Steam#Default_installer "Steam") installation method, except that an alternative Steam installer script is used.

Fetch the Steam installer and extract the required files:

`user `[`$`]`wget https://repo.steampowered.com/steam/pool/steam/s/steam/steam_1.0.0.78.tar.gz `

`user `[`$`]`tar -xvzf steam_1.0.0.*.tar.gz steam-launcher/bootstraplinux_ubuntu12_32.tar.xz `

`user `[`$`]`tar -xvzf steam_1.0.0.*.tar.gz steam-launcher/steam.desktop `

Fetch and run [Julian Ospald\'s (hasufell)](https://gist.github.com/hasufell) Steam installer script:

`user `[`$`]`cd steam-launcher `

`user `[`$`]`wget https://gist.githubusercontent.com/hasufell/d02a93eccbe35be7a803/raw/987ea287dc81a60d2eb5fa1bb188eae0a5f1049f/steam `

`user `[`$`]`chmod +x steam `

`user `[`$`]`./steam `

If the installer script creates broken symbolic links when run with [Dash](https://wiki.gentoo.org/wiki/Dash "Dash"), run the installer script with [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") instead:

`user `[`$`]`bash ./steam`

## [[] Chroot]

Steam can be run in a 64-bit [multilib](https://wiki.gentoo.org/wiki/Multilib "Multilib") [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot") on **[amd64]**. The major advantage of a chroot is that Steam and its dependencies will be isolated from the root filesystem. The Steam browser is no longer supported on 32-bit Linux distributions, so only 64-bit chroot environment is available.^[\[4\]](#cite_note-32bitonly-4)^

Create the chroot directory:

`root `[`#`]`mkdir /usr/local/steam64 `

`root `[`#`]`cd /usr/local/steam64 `

Fetch and extract the stage3 tarball.

`root `[`#`]`wget https://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64-openrc/stage3-amd64-openrc-20250907T165007Z.tar.xz `

`root `[`#`]`tar xpvf stage3*.tar.xz --xattrs-include='*.*' --numeric-owner `

Copy DNS information and ensure it\'s world-readable:

`root `[`#`]`cp -L /etc/resolv.conf etc `

`root `[`#`]`chmod a+r etc/resolv.conf `

Create the ebuild repository directory:

`root `[`#`]`mkdir var/db/repos/gentoo `

Mount the necessary filesystems:

`root `[`#`]`mount -t proc /proc proc `

`root `[`#`]`mount -R /sys sys `

`root `[`#`]`mount -R /dev dev `

`root `[`#`]`mount -R /run run `

`root `[`#`]`mount -R /var/db/repos/gentoo var/db/repos/gentoo `

Chroot with [linux64] and update the environment. The use of [linux64] is not required on **[amd64]**, and it is only used here for consistency.

`root `[`#`]`linux64 chroot . `

`root `[`#`]`env-update && source /etc/profile `

`root `[`#`]`export PS1="(chroot) $PS1" `

The chroot should now be updated and configured accordingly. It is recommended to at least configure the [timezone](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Timezone "Handbook:AMD64/Installation/Base") and enable sound support by installing [[[media-libs/alsa-lib]](https://packages.gentoo.org/packages/media-libs/alsa-lib)[]].

Now create the Steam user with the same UID (usually 1000) as the local user. The local UID can be determined by running [id -u] as the local user, outside of the chroot. Using the same UID will simplify the process of granting access to the X server from inside the chroot.

`(chroot) root #``useradd -u <UID> -m -G audio,video steam `

Install Steam from one of the above installation methods. When complete, exit the chroot:

`(chroot) root #``exit `

Unmount the chroot directories:

`root `[`#`]`umount -l proc `

`root `[`#`]`umount -l sys `

`root `[`#`]`umount -l dev `

`root `[`#`]`umount -l run `

`root `[`#`]`umount -l var/db/repos/gentoo `

Install [xhost] to allow access to the X server from inside the chroot:

`root `[`#`]`emerge --ask --noreplace x11-apps/xhost`

Logout, and then login. This allows the [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or [xinit] to process [/etc/X11/xinit/xinitrc.d/00-xhost] and automatically grant all local connections to the X server from the local UID. This will not work if the Steam UID is different to that of the local UID. Either set the same UID when creating the Steam user, as was mentioned earlier, or if the Steam user already exists change the Steam UID with [usermod -u \<UID\> steam] to match the local UID.

Alternatively, run [xhost +local:] to allow all local connections to the X server from *any* local UID. This is a potential security risk as any user could access the X server without authentication. To revoke access run [xhost -local:]

Next, create the following wrapper script to setup the chroot, substitute to the Steam user, and start Steam. The wrapper script has two user defined variables: `chroot_bits` and `chroot_dir`. The `chroot_bits` variable must be set to `64` for a 64-bit chroot. The `chroot_dir` variable should be set to the location of the chroot directory.

[FILE] **`/usr/local/bin/steam-chroot`**

    #!/bin/sh

    # steam chroot bits
    chroot_bits="64"

    # steam chroot directory
    chroot_dir="/usr/local/steam64/"

    # check if chroot bits is valid
    if [ "$" = "32" ] ; then
      chroot_arch="linux32"
    elif [ "$" = "64" ] ; then
      chroot_arch="linux64"
    else
      printf "Invalid chroot bits value '%s'. Permitted values are '32' and '64'.\n" "$"
      exit 1
    fi

    # check if the chroot directory exists
    if [ ! -d "$" ] ; then
      printf "The chroot directory '%s' does not exist!\n" "$"
      exit 1
    fi

    # mount the chroot directories
    mount -v -t proc /proc "$proc"
    mount -vR /sys "$sys"
    mount --make-rslave "$sys"
    mount -vR /dev "$dev"
    mount --make-rslave "$dev"
    mount -vR /run "$run"
    mount --make-rslave "$run"
    mount -vR /var/db/repos/gentoo "$var/db/repos/gentoo"
    # the --make-rslave flags are needed for systemd support

    # chroot, substitute user, and start steam
    if [[ -n $( grep systemd /proc/1/comm ) ]]; then
      "$" unshare -m chroot "$" su -c 'steam' steam
    else
      "$" chroot "$" su -c 'steam' steam
    fi
    # unmount the chroot directories when steam exits
    umount -vl "$proc"
    umount -vl "$sys"
    umount -vl "$dev"
    umount -vl "$run"
    umount -vl "$var/db/repos/gentoo"

** Note**\
The wrapper script bind mounts [/run] so Steam can connect to [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") if it is running on the host. Steam will work even if D-Bus is not installed, but there will be non-fatal errors relating to Steam\'s bundled [[[dev-libs/libappindicator]](https://packages.gentoo.org/packages/dev-libs/libappindicator)[]]. Steam also needs D-Bus if the *Remember my password* option is selected at the Steam login dialog. Refer to [client troubleshooting](https://wiki.gentoo.org/wiki/Steam/Client_troubleshooting#Segfault_when_remember_my_password_is_selected "Steam/Client troubleshooting") for further details.

Make the wrapper script executable:

`root `[`#`]`chmod +x /usr/local/bin/steam-chroot`

Run the wrapper script as [root] to start Steam:

`root `[`#`]`steam-chroot`

### [Systemd and chroot]

When the host system is in systemd, raw chroot is not sufficient. Instead, `unshare -m chroot` has to be used. In fact the above wrapper script supports this case.

Explanation: With bare `chroot`, the Steam client does not run, complaining \"Steam now requires user namespaces to be enabled.\" For this Steam tests if `bwrap --bind / / true` succeeds. (This requires bwrap is set setuid.) Internally bwrap calls [pivot_root (2)](https://www.man7.org/linux/man-pages/man2/pivot_root.2.html), of which conditions with \"/\" are not met under systemd. With unshare the namespace gets separated, and things work.

## [Easy Anti Cheat Support]

Due to DT_HASH not being enabled by default since glibc 2.36 then the follow needs to be applied to allow EAC games to work

[FILE] **`/etc/portage/package.use/glibc`**

    sys-libs/glibc hash-sysv-compat

`root `[`#`]`emerge -1 sys-libs/glibc`

## [Removal]

### [Removing a manual installation]

Remove the Steam dependencies:

`root `[`#`]`emerge --deselect @steam`

`root `[`#`]`emerge --ask --depclean`

Remove the Steam executable and Portage configuration:

`root `[`#`]`rm /usr/bin/steam `

`root `[`#`]`rm /etc/portage/sets/steam `

`root `[`#`]`rm -rf /etc/portage/package.*/steam `

Remove the Steam directory from the user accountː

`user `[`$`]`rm -rf ~/.local/share/Steam`

### [Removing an external repository installation]

Remove the [steam-launcher] ebuild:

`root `[`#`]`emerge --ask --depclean --verbose games-util/steam-launcher`

## [Troubleshooting]

The most common game related issues are solved by enabling the `stack-realign` USE flag on the [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] package and re-emerge the [\@world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"). It is a good idea to perform this change as the first troubleshooting action item.

Some Steam and games specific troubleshooting available on [Steam/Client troubleshooting](https://wiki.gentoo.org/wiki/Steam/Client_troubleshooting "Steam/Client troubleshooting") and [Steam/Games troubleshooting](https://wiki.gentoo.org/wiki/Steam/Games_troubleshooting "Steam/Games troubleshooting") subpages.

If you want to play games through proton, don\'t forget to add the `vulkan` USE flag on the [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] package.

The best place to ask for help is the [Steam thread](https://forums.gentoo.org/viewtopic-t-930354.html) on the Gentoo Forums. If a solution to an issue is confirmed by others, add it to this page or the relevant troubleshooting subpage. Please do not remove content without [discussion](https://wiki.gentoo.org/wiki/Talk:Steam "Talk:Steam"), *unless* it is obviously wrong.

## [See also]

-   [Games](https://wiki.gentoo.org/wiki/Games "Games") --- a landing page for many of the games (especially open source variants) available in Gentoo\'s main ebuild repository.
-   [Steam Controller](https://wiki.gentoo.org/wiki/Steam_Controller "Steam Controller") --- a game controller developed by [Valve](https://en.wikipedia.org/wiki/Valve_Corporation "wikipedia:Valve Corporation").
-   [Steam/Client troubleshooting](https://wiki.gentoo.org/wiki/Steam/Client_troubleshooting "Steam/Client troubleshooting") --- provides troubleshooting details for the Steam client on Linux systems.
-   [Steam/Games troubleshooting](https://wiki.gentoo.org/wiki/Steam/Games_troubleshooting "Steam/Games troubleshooting") --- provides troubleshooting details for specific games running via Steam.

## [External resources]

-   [Gentoo Forums - Native Steam client and source game engine](https://forums.gentoo.org/viewtopic-t-930354.html)
-   [GitHub - Steam for Linux Client](https://github.com/ValveSoftware/steam-for-linux)
-   [Steam Community - Steam for Linux](https://steamcommunity.com/linux)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://steamcommunity.com/games/221410/announcements/detail/1696055855739350561](https://steamcommunity.com/games/221410/announcements/detail/1696055855739350561)]]
2.  [[[↑](#cite_ref-2)] [[https://www.gamingonlinux.com/steam-tracker/](https://www.gamingonlinux.com/steam-tracker/)]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/ValveSoftware/Proton#introduction](https://github.com/ValveSoftware/Proton#introduction)]]
4.  [[↑ ^[4.0](#cite_ref-32bitonly_4-0)^ ^[4.1](#cite_ref-32bitonly_4-1)^] [[32-bit Linux distributions are no longer supported by Steam, Steam Web Browser disabled](https://www.gamingonlinux.com/2016/12/32-bit-linux-distributions-are-no-longer-supported-by-steam-steam-web-browser-disabled/)]]
5.  [[[↑](#cite_ref-5)] [[Issues on 4.18.9-gentoo kernel](https://github.com/ValveSoftware/steam-for-linux/issues/5782#issuecomment-424020747), [Steam for Linux](https://github.com/ValveSoftware/steam-for-linux), September 24th, 2018. Retrieved on September 25th, 2018.]]