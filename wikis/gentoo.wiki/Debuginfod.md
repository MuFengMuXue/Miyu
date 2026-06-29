**Resources**

[[]][Home](https://sourceware.org/elfutils/Debuginfod.html)

It is possible to use **debuginfod** to provide debug information to your binary package downstreams, and, consequently, to remove debug information from the binary package, saving disk space and bandwidth.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Build IDs]](#Build_IDs)
-   [[3] [Supporting changes]](#Supporting_changes)
-   [[4] [Overview]](#Overview)
-   [[5] [Server setup]](#Server_setup)
    -   [[5.1] [Build IDs]](#Build_IDs_2)
    -   [[5.2] [Configuration]](#Configuration)
-   [[6] [Client setup]](#Client_setup)
-   [[7] [TODO]](#TODO)

## [Introduction]

debuginfod has two components:

1.  libdebuginfod - a library which [[[dev-debug/gdb]](https://packages.gentoo.org/packages/dev-debug/gdb)[]] and others can use to request debug information from a server
2.  debuginfod - a daemon which serves debug information to libdebuginfod-consuming clients

\
It is normally of use for binary distributions, but it has value in Gentoo now too:

-   Being able to debug anything that is part of the built stage3 without rebuilding it with debugging symbols (which might make a problem go away)
-   Debug information being available for [official Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart") binaries
-   Those creating their [own binary packages](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") can debug issues with them
-   Ability to debug a crashing binary from another distribution
-   Even where no binary distribution is happening, it can be used to debug a binary that later got upgraded on the system

\
libdebuginfod support is enabled by default in gdb and friends because it has few dependencies and allows debugging out-of-the-box. It does not communicate with any hosts by default, nor is it configured with the knowledge of any remote machines. gdb also won\'t communicate with a debuginfod instance without asking.

It also works in the other direction: if somebody reports a crash using a Gentoo-provided binary, they can share what the build ID of that binary is, and one can download a copy of that binary via the ID if a server has been configured to provide it.

The debuginfod daemon doesn\'t run by default and is only needed if serving files to clients. For users that don\'t use binary packages (either built by Gentoo or themselves), they can disable debuginfod entirely with:

[FILE] **`/etc/portage/make.conf`**

    USE="$ -debuginfod"

## [Build IDs]

Build IDs are a related but distinct topic from debuginfod support. The linker can stamp produced binaries with a *.note.gnu.build-id* note that contains a unique identifier for the build.

This has a few uses:

-   it allows identifying if a binary is identical to another by only hashing the meaningful parts of a binary;
-   it allows looking up debug information for that binary;
-   [caching](https://wiki.gentoo.org/wiki/GDB#Caching "GDB") for gdb requires it;
-   looking up debug information locally is faster (and more reliable, see [[[bug #917287]](https://bugs.gentoo.org/show_bug.cgi?id=917287)[]])

\
Software has started to assume build IDs may exist and having them is very cheap indeed.

## [Supporting changes]

Gentoo enabled build IDs by default again in 2026/02 ([[[bug #953869]](https://bugs.gentoo.org/show_bug.cgi?id=953869)[]]). Portage was modified to always salt build IDs ([[[bug #549672]](https://bugs.gentoo.org/show_bug.cgi?id=549672)[]]) when it sees them in binaries being installed to avoid file collisions between (usually prebuilt binary) packages with bundled libraries, done via [[[dev-util/debugedit]](https://packages.gentoo.org/packages/dev-util/debugedit)[]].

[debugedit] has always been needed for `FEATURES="installsources"` and Portage may enable `FEATURES="splitdebug compressdebug installsources"` by default ([[[bug #968133]](https://bugs.gentoo.org/show_bug.cgi?id=968133)[]]) to make it easier to debug in future in general, because experience guiding users to do this has shown that they find it frustrating and unnecessarily cumbersome to get debug symbols.

## [Overview]

[Portage](https://wiki.gentoo.org/wiki/Portage "Portage") (\>=3.0.74) can, with `FEATURES="packdebug"`, generate tarballs that contain the [/usr/lib/debug] and [/usr/src/debug] hierarchies, and only those hierarchies, and to install them into some location so that they are preserved on uninstalls and upgrades. This allows [debuginfod] to look for past builds for debug info rather than just the latest ones. This was implemented in [[[bug #728818]](https://bugs.gentoo.org/show_bug.cgi?id=728818)[]].

*packdebug* only needs to be enabled on the binpkg producer.

For `FEATURES="packdebug"`, Portage will automatically:

-   Create a tarball in [/usr/lib/debug/.tarball/\$/\$/\$-\$-debug.tar.xz] with debug information from [/usr/lib/debug/\*], [/usr/src/debug/\*]. This is installed but not part of the binpkg.
-   Set `UNINSTALL_IGNORE="/usr/lib/debug/.tarball"` to keep old debug information tarballs around to serve.
-   Set `COLLISION_IGNORE="/usr/lib/debug/.tarball"` to ignore collisions from such orphaned debug information tarballs left around by `UNINSTALL_IGNORE`.
-   Set `PKG_INSTALL_MASK="/usr/lib/debug/* /usr/src/debug/*"` so binpkgs do not contain debug information (they should fetch it via debuginfod instead).

## [Server setup]

This is only required if one wishes to serve debug information for custom built binary packages.

### [Build IDs]

Build IDs must be enabled in the toolchain. Since [[[bug #953869]](https://bugs.gentoo.org/show_bug.cgi?id=953869)[]], this is enabled by default.

`root `[`#`]`mkdir /etc/portage/env/sys-devel/`

[FILE] **`/etc/portage/env/sys-devel/gcc`**

    # https://bugs.gentoo.org/953869
    EXTRA_ECONF="$ --enable-linker-build-id

`root `[`#`]`emerge --ask -v1 sys-devel/gcc`

### [Configuration]

It is sufficient to set the following:

[FILE] **`/etc/portage/make.conf`**

    # Adapt -g* as desired
    CFLAGS="$ -g"
    CXXFLAGS="$ -g"
    LDFLAGS="$ -g"

    # Optional: don't install 'duplicate' copies of debug information to the live filesystem outside of produced packdebug tarballs
    INSTALL_MASK="$ /usr/lib/debug/ /usr/src/debug/ -/usr/lib/debug/.tarball"

    # Obviously binaries need to be built too
    FEATURES="$ buildpkg"

    # Produce separate debuginfo tarballs in /usr/lib/debug/.tarball
    FEATURES="$ packdebug"
    # packdebug requires splitdebug
    FEATURES="$ splitdebug compressdebug installsources"
    # sys-devel/dwz can make it smaller
    FEATURES="$ dedupdebug"
    USE="$ debuginfod"

Following that, you can run:

`root `[`#`]`debuginfod -Z tar.xz /usr/lib/debug/.tarball -Z.gpkg.tar='(bsdtar -xf- -O '*/image.tar.*' | bsdtar --strip-components 1 -cf- @-)<' /var/cache/binpkgs`

\... with your preferred service manager.

An example systemd unit can be created with:

`root `[`#`]`systemctl edit --full --force debuginfod`

Then:

[FILE] **`/etc/systemd/system/debuginfod.service`**

    # -*- conf-unix -*-

    [Unit]
    Description=elfutils debuginfod is a server that automatically distributes ELF/DWARF/source code from servers to clients such as debuggers across HTTP.
    Documentation=https://sourceware.org/elfutils/Debuginfod.html man:debuginfod(8)
    After=network.target

    [Service]
    DynamicUser=true
    # We pass in both the packdebug location and the binpkgs location itself for binaries
    ExecStart=/usr/bin/debuginfod --listen-address=127.0.0.1 --database=$/db.sqlite3 -Z tar.xz /usr/lib/debug/.tarball -Z.gpkg.tar='(bsdtar -xf- -O '*/image.tar.*' | bsdtar --strip-components 1 -cf- @-)<' /var/cache/binpkgs

    ProtectProc=invisible
    NoNewPrivileges=true
    ProtectSystem=strict
    ProtectHome=tmpfs
    PrivateTmp=on
    PrivateDevices=on
    PrivateIPC=on
    PrivateUsers=on
    ProtectClock=on
    ProtectHostname=on
    ProtectKernelTunables=on
    ProtectKernelModules=on
    ProtectKernelLogs=on
    ProtectControlGroups=on
    LockPersonality=on
    RestrictSUIDSGID=on
    PrivateMounts=on
    SystemCallFilter=@system-service
    UnsetEnvironment=DEBUGINFOD_URLS

    TemporaryFileSystem=/:ro
    BindReadOnlyPaths=/usr/src/debug /usr/bin/ /usr/lib64 /usr/lib
    NoExecPaths=/
    ExecPaths=/usr/bin/debuginfod

    CacheDirectory=debuginfod

    [Install]
    WantedBy=multi-user.target

This will expose debuginfod on [localhost:8002], which you can then expose via a reverse proxy, or any other means.

Note that the server reacts to the `DEBUGINFOD_URLS` environment variable, and will fall back to the servers listed in it to continue a search for debuginfo. You can use this property to have your server cache results from the [https://debuginfod.elfutils.org/](https://debuginfod.elfutils.org/) federated instance, which lets you also fetch debug info for other distributions. Take care to also clear this variable if you have it set globally outside the debuginfod server.

## [Client setup]

This is needed only to use debug information from a debuginfod instance configured manually. Gentoo does not yet have a debuginfod instance for its official binary packages but it is planned ([[[bug #967111]](https://bugs.gentoo.org/show_bug.cgi?id=967111)[]]).

To use the new debuginfod instance, presuming that you exposed it on [http://foo.mynet.local/debuginfo], you can create a file akin to the following:

[FILE] **`/etc/env.d/99debuginfod`**

    DEBUGINFOD_URLS="http://foo.mynet.local/debuginfo https://debuginfod.elfutils.org/"

As demonstrated, this variable holds a list of debug info servers. The latter server in that example federates with many other debuginfod servers.

Following an [env-update](https://wiki.gentoo.org/wiki/Env-update "Env-update"), new sessions should immediately have access to debug information. You will also likely want to adjust your [.gdbinit] file as such, to avoid [gdb](https://wiki.gentoo.org/wiki/Gdb "Gdb") nagging about whether to enable debuginfod support.

[FILE] **`$XDG_CONFIG_HOME/gdb/.gdbinit`**

    set debuginfod enabled on

## [TODO]

-   [eclean-pkg]: implement time delay cleanup for binpkgs ([[[bug #967114]](https://bugs.gentoo.org/show_bug.cgi?id=967114)[]])
-   Add OpenRC init script for debuginfod ([[[bug #970303]](https://bugs.gentoo.org/show_bug.cgi?id=970303)[]])
-   Have the elfutils ebuild install a special systemd unit (and OpenRC init script) for this use
-   ~~[eclean-pkg]: handle [/usr/lib/debug/.tarball] ([[[bug #967112]](https://bugs.gentoo.org/show_bug.cgi?id=967112)[]])~~
-   ~~Enable build IDs automatically in the toolchain ([[[bug #953869]](https://bugs.gentoo.org/show_bug.cgi?id=953869)[]])~~
-   ~~Teach portage to generate tarballs that contain the [/usr/lib/debug] and [/usr/src/debug] hierarchies, and only those hierarchies, and to install them into some location as unowned files. This will allow debuginfod to look for past builds for debug info rather than just the latest ones. This should also allow the user to `INSTALL_MASK` the source and debug info files. [[[bug #728818]](https://bugs.gentoo.org/show_bug.cgi?id=728818)[]], [[[bug #639376]](https://bugs.gentoo.org/show_bug.cgi?id=639376)[]]~~
-   ~~Uncrustify this article~~