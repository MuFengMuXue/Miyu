This article covers using [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") to bootstrap [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") for a specific architecture.

## Contents

-   [[1] [Environment]](#Environment)
-   [[2] [crossdev]](#crossdev)
-   [[3] [Rust]](#Rust)
    -   [[3.1] [Grab repo]](#Grab_repo)
    -   [[3.2] [Build it]](#Build_it)
    -   [[3.3] [On the other side]](#On_the_other_side)
        -   [[3.3.1] [Install built Rust temporarily]](#Install_built_Rust_temporarily)
        -   [[3.3.2] [Ebuild mangling]](#Ebuild_mangling)
-   [[4] [Distribution tarball]](#Distribution_tarball)
-   [[5] [See Also]](#See_Also)
-   [[6] [External references]](#External_references)

## [Environment]

-   Figure out the LLVM target name corresponding to the destination platform (look at e.g. [emerge -pvO sys-devel/llvm] for hints).
    -   This will be referred to as `LLVM_TARGET` just for the purposes of this page.
    -   For sparc, it\'s `Sparc`.

<!-- -->

-   Figure out the Rust target name for the destination platform.
    -   Hint: try [rustc \--print target-list \| grep \$.
    -   For sparc, it\'s `sparc64-unknown-linux-gnu`.

<!-- -->

-   Figure out `CHOST` for use with both [crossdev] and later, Rust as `CTARGET`.
    -   This will be called CTARGET.
    -   Hint: look at [/var/db/repos/gentoo/profiles/arch/\$/make.defaults].
    -   For sparc, it\'s `sparc64-unknown-linux-gnu` as 32-bit will not be covered (at least for now!)

## [crossdev]

Install crossdev:

`root `[`#`]`emerge --ask sys-devel/crossdev`

Create an overlay for it to dump its ebuilds into:

`root `[`#`]`eselect repository create crossdev`

Create a cross toolchain for the chosen `CHOST`. For sparc, it\'ll be:

`amd64 `[`#`]`crossdev --ov-output /var/db/repos/local/crossdev sparc64-unknown-linux-gnu`

## [Rust]

### [Grab repo]

The git repo is used because the tag tarballs lack the required submodules:

`amd64 `[`#`]`git clone `[`https://github.com/rust-lang/rust.git`](https://github.com/rust-lang/rust.git)` -b stable && cd rust `

`amd64 `[`#`]`git submodule update --init --recursive`

### [Build it]

Install [[[dev-libs/openssl]](https://packages.gentoo.org/packages/dev-libs/openssl)[]] for the `openssl-sys` create:

`amd64 `[`#`]`sparc64-unknown-linux-gnu-emerge -v1 openssl`

** Note**\
Versions of Rust released before or slightly after May 15, 2023 may depend on OpenSSL 1.1.1 instead of the latest version, which is EOL and masked as of the time of writing. For more details see [https://github.com/sfackler/rust-openssl/issues/1645](https://github.com/sfackler/rust-openssl/issues/1645).

Configure:

[FILE] **`config.toml`**

    # Includes one of the default files in src/bootstrap/defaults
    profile = "user"
    changelog-seen = 2

    [rust]
    channel = "stable"

    [target.sparc64-unknown-linux-gnu]
    # Needed because of some mixup between Rust target names and defaults(?)
    # for it -- seems to assume Debian naming of sparc64-linux-gnu otherwise?
    cc = "sparc64-unknown-linux-gnu-gcc"
    cxx = "sparc64-unknown-linux-gnu-g++"

Run the mono [x.py] build script:

`amd64 `[`#`]`OPENSSL_INCLUDE_DIR=/usr/sparc64-unknown-linux-gnu/usr/include/ OPENSSL_LIB_DIR=/usr/sparc64-unknown-linux-gnu/usr/lib PKG_CONFIG_PATH=/usr/sparc64-unknown-linux-gnu/usr/lib/pkgconfig ./x.py dist --build x86_64-unknown-linux-gnu --host sparc64-unknown-linux-gnu --target sparc64-unknown-linux-gnu`

All going well, when it terminates, there should be a fresh [rustc] binary:

`amd64 `[`#`]`file build/sparc64-unknown-linux-gnu/stage2/bin/rustc`

    build/sparc64-unknown-linux-gnu/stage2/bin/rustc: ELF 64-bit MSB pie executable, SPARC V9, total store ordering, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux.so.2, for GNU/Linux 3.2.0, with debug_info, not stripped

### [On the other side]

#### [Install built Rust temporarily]

** Warning**\
Use a path like [/usr/local] where it\'s easy to delete the files afterwards and be sure nothing is lingering \"contaminating\" later builds. In fact, this whole procedure should be done in a clean chroot.

Copy the files over to the destination box (sparc in this case):

-   Copy over:
    -   [build/dist/cargo-1.61.0-sparc64-unknown-linux-gnu.tar.xz]
    -   [build/dist/rust-std-1.61.0-sparc64-unknown-linux-gnu.tar.xz]
    -   [build/dist/rustc-1.61.0-sparc64-unknown-linux-gnu.tar.xz]
-   For each: on the other side, untar it to a temporary location, and run inside [./install.sh \--prefix=/usr/local/lib/rust/1.61.0/]

#### [Ebuild mangling]

Some changes are needed to [/etc/portage]:

[FILE] **`/etc/portage/package.unmask`**

    app-eselect/eselect-rust
    dev-lang/rust
    virtual/rust

[FILE] **`/etc/portage/package.accept_keywords`**

    app-eselect/eselect-rust * ~*
    dev-lang/rust * ~*
    virtual/rust * ~*

[FILE] **`/etc/portage/package.use`**

    # This is our LLVM_TARGET from earlier.
    dev-lang/rust RUST_TARGETS: Sparc

Copy the Rust ebuilds to a temporary location:

`sparc `[`#`]`mkdir -p /tmp/dev-lang/rust && cd /tmp/dev-lang/rust `

`sparc `[`#`]`cp -rv /var/db/repos/gentoo/dev-lang/rust/* .`

Modify the Rust ebuild corresponding to the current latest Rust release (must match the version built from git):

1.  Put \'python-any-r1_pkg_setup\' at the top of pkg_setup, then add \'return\' immediately below it in `pkg_setup` (re [eselect-rust] checks) (so only those two lines are run)
2.  Replace the [rustc] call in `src_configure` by just setting [rust_stage0_root=/usr/local/lib/rust/1.61.0/]
3.  May need to comment out the `[[ -d $ ]]` check (?)

Todo: [ **Todo:**]

-   Check if previous point should be commented out or not.

\

Then try to [emerge] using it:

`sparc `[`#`]`USE=system-bootstrap ebuild rust-1.61.0.ebuild clean merge`

Once done, some manual fiddling may be needed to get `LDPATH` right initially and make [eselect rust] happy.

Run [eselect rust update] and placate any complaints it has if there\'s stale stuff left over from the [/usr/local] bits. Try [env-update && . /etc/profile].

Remember to clean up [/usr/local/.

Now do it all again using a vanilla ebuild:

`sparc `[`#`]`USE=system-bootstrap ebuild /var/db/repos/gentoo/dev-lang/rust/rust-1.61.0.ebuild clean merge`

## [Distribution tarball]

** Note**\
See [[[bug #671736]](https://bugs.gentoo.org/show_bug.cgi?id=671736)[]] and [[[bug #842246]](https://bugs.gentoo.org/show_bug.cgi?id=842246)[]] which will make it easier to add non-upstream bootstrap tarballs into [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]].

Now re-emerge [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] with the `dist` USE flag:

`sparc `[`#`]`USE="dist system-bootstrap" ebuild rust-1.61.0.ebuild clean merge`

Once done, the binaries should be at [\$(rustc \--print sysroot)/dist] (in this case, that\'s [/usr/lib/rust/1.61.0/dist]):

`sparc `[`#`]`ls -al $(rustc --print sysroot)/dist`

    total 61732
    drwxr-xr-x 2 root root     4096 Jun 22 19:19 .
    drwxr-xr-x 7 root root     4096 Jun 22 19:19 ..
    -rw-r--r-- 1 root root  4134536 Jun 22 19:18 cargo-1.61.0-sparc64-unknown-linux-gnu.tar.xz
    -rw-r--r-- 1 root root 20586916 Jun 22 19:18 rust-std-1.61.0-sparc64-unknown-linux-gnu.tar.xz
    -rw-r--r-- 1 root root 38477600 Jun 22 19:18 rustc-1.61.0-sparc64-unknown-linux-gnu.tar.xz

## [See Also]

-   [Project:Rust](https://wiki.gentoo.org/wiki/Project:Rust "Project:Rust")
-   [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") --- a general-purpose, multi-paradigm, compiled, programming language.
-   [User:Immolo/rust_i686](https://wiki.gentoo.org/wiki/User:Immolo/rust_i686 "User:Immolo/rust i686")

## [External references]

-   [https://rustc-dev-guide.rust-lang.org/building/how-to-build-and-run.html](https://rustc-dev-guide.rust-lang.org/building/how-to-build-and-run.html)
-   [https://rustc-dev-guide.rust-lang.org/building/build-install-distribution-artifacts.html](https://rustc-dev-guide.rust-lang.org/building/build-install-distribution-artifacts.html)
-   [https://gitlab.com/stikonas/gentoo-bootstrap#bootstrapping-rust](https://gitlab.com/stikonas/gentoo-bootstrap#bootstrapping-rust)