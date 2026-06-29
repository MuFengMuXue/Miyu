**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Rust "Project:Rust")][Project](https://wiki.gentoo.org/wiki/Project:Rust "Project:Rust")

[[]][Home](https://www.rust-lang.org/)

[[]][Official documentation](https://doc.rust-lang.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/rust)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Rust_(programming_language) "wikipedia:Rust (programming language)")

[[]][GitHub](https://github.com/rust-lang/rust)

[[]][[#rust](ircs://irc.libera.chat/#rust)] ([[webchat](https://web.libera.chat/#rust)])

**Rust** is a general-purpose, multi-paradigm, compiled, programming language.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Rust Channels]](#Rust_Channels)
        -   [[1.3.1] [Stable]](#Stable)
        -   [[1.3.2] [Beta]](#Beta)
        -   [[1.3.3] [Nightly]](#Nightly)
    -   [[1.4] [Why dev-lang/rust depends on dev-lang/rust-bin]](#Why_dev-lang.2Frust_depends_on_dev-lang.2Frust-bin)
    -   [[1.5] [Distcc MAKEOPTS]](#Distcc_MAKEOPTS)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
        -   [[2.1.1] [Link Time Optimization (LTO)]](#Link_Time_Optimization_.28LTO.29)
        -   [[2.1.2] [Optimization level]](#Optimization_level)
    -   [[2.2] [Eselect Rust]](#Eselect_Rust)
    -   [[2.3] [Rustup]](#Rustup)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Development]](#Development)
    -   [[3.2] [Language servers]](#Language_servers)
    -   [[3.3] [Code formatting]](#Code_formatting)
    -   [[3.4] [Code linting]](#Code_linting)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/rust](https://packages.gentoo.org/packages/dev-lang/rust) [[]] [Systems programming language originally developed by Mozilla]

  ------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+clippy`](https://packages.gentoo.org/useflags/+clippy)                       Install clippy, Rust code linter
  [`+doc`](https://packages.gentoo.org/useflags/+doc)                             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`+rustfmt`](https://packages.gentoo.org/useflags/+rustfmt)                     Install rustfmt, Rust code formatter
  [`+system-llvm`](https://packages.gentoo.org/useflags/+system-llvm)             Use the system LLVM installation
  [`big-endian`](https://packages.gentoo.org/useflags/big-endian)                 Big-endian toolchain support
  [`debug`](https://packages.gentoo.org/useflags/debug)                           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`dist`](https://packages.gentoo.org/useflags/dist)                             Install dist tarballs (used for bootstrapping)
  [`llvm-libunwind`](https://packages.gentoo.org/useflags/llvm-libunwind)         Use llvm-runtimes/libunwind instead of sys-libs/libunwind
  [`lto`](https://packages.gentoo.org/useflags/lto)                               Enable Link-Time Optimization (LTO) to optimize the build
  [`miri`](https://packages.gentoo.org/useflags/miri)                             Install miri, an interpreter for Rust\'s mid-level intermediate representation (requires USE=nightly, sometimes is broken)
  [`mrustc-bootstrap`](https://packages.gentoo.org/useflags/mrustc-bootstrap)     Use dev-lang/mrustc to build the bootstrap Rust sysroot from this package\'s source
  [`nightly`](https://packages.gentoo.org/useflags/nightly)                       Enable nightly (UNSTABLE) features (NOTE: it does not install nightly version, just enables features marked as nightly at time of release)
  [`parallel-compiler`](https://packages.gentoo.org/useflags/parallel-compiler)   Build a multi-threaded rustc (experimental, not tested by upstream)
  [`rust-analyzer`](https://packages.gentoo.org/useflags/rust-analyzer)           Install rust-analyzer, A Rust compiler front-end for IDEs (language server)
  [`rust-src`](https://packages.gentoo.org/useflags/rust-src)                     Install rust-src, needed by developer tools and for build-std (cross)
  [`test`](https://packages.gentoo.org/useflags/test)                             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)                 Verify upstream signatures on distfiles
  [`wasm`](https://packages.gentoo.org/useflags/wasm)                             Build support for the wasm32-unknown-unknown target
  ------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-18 09:39] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [dev-lang/rust-bin](https://packages.gentoo.org/packages/dev-lang/rust-bin) [[]] [Systems programming language from Mozilla]

  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+clippy`](https://packages.gentoo.org/useflags/+clippy)               Install clippy, Rust code linter
  [`+doc`](https://packages.gentoo.org/useflags/+doc)                     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`+rustfmt`](https://packages.gentoo.org/useflags/+rustfmt)             Install rustfmt, Rust code formatter
  [`big-endian`](https://packages.gentoo.org/useflags/big-endian)         Big-endian toolchain support
  [`prefix`](https://packages.gentoo.org/useflags/prefix)                 Defines if a Gentoo Prefix offset installation is used
  [`rust-analyzer`](https://packages.gentoo.org/useflags/rust-analyzer)   Install rust-analyzer, A Rust compiler front-end for IDEs (language server)
  [`rust-src`](https://packages.gentoo.org/useflags/rust-src)             Install rust-src, needed by developer tools and for build-std (cross)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)         Verify upstream signatures on distfiles
  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-18 09:39] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

** Tip**\
Rust is a relatively large compile. Unless there is a specific reason to prefer the from-source build (such as the need for non default [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag")), consider selecting [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]].

Emerge the package:

`root `[`#`]`emerge --ask dev-lang/rust`

Alternatively, emerge the binary package:

`root `[`#`]`emerge --ask dev-lang/rust-bin`

### [Rust Channels]

> Rust is released to three different \"channels\": stable, beta, and nightly. The stable releases are made every 6 weeks (with occasional point releases). Beta releases are the version that will appear in the next stable release. Nightly releases are made every night.
>
> \-- The Rustup book

#### [Stable]

The `stable` channel is the latest versioned release of Rust. These ebuilds are always keyworded for supported arches and will eventually be stabilised, provided that no major issues are encountered. The `stable` channel is typically used on Gentoo systems for package dependencies.

Gentoo developers build [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] for niche architectures so this package is often a good choice.

#### [Beta]

Gentoo packages the `beta` channel for each [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] and [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] release. The beta channel is not keyworded, but is not particularly unsafe to use as the only development on this channel is fixing regressions. Users that need to build `nightly` [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] will need this channel first (though portage will handle this via package dependencies).

Users who would like to take advantage of prerelease language features and who are willing to report any bugs encountered may consider using this channel.

If installed the `beta` channel Rust may be selected by portage as the appropriate dependency for system packages.

#### [Nightly]

** Tip**\
No ebuilds in the Gentoo tree require `nightly` Rust.\
\
Any packages that require nightly features at compile-time will enable them via the `RUSTC_BOOTSTRAP` variable.

** Tip**\
If nightly Rust fails to compile, try fetching the latest beta or nightly snapshot and building with that. See `ERUST_SLOT_OVERRIDE` and `ERUST_TYPE_OVERRIDE` in [rust.eclass] for some pointers.

As per advice from upstream, it is best practice to only enable nightly builds on either bleeding-edge git checkouts or nightly tarball snapshots. As such, and to better reflect the \'unstable\' features enabled by `nightly` build type, the `nightly` USE flag will shortly be disappearing from versioned releases. Users desiring `nightly` Rust should instead unmask and install the live ebuilds. These are available for [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] and [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]].

The live ebuild for [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] has a large initial git checkout, however deltas should be relatively small for subsequent checkouts; consider [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] if this is a concern.

Users that would like (or have some reason) to run bleeding-edge Rust may emerge these ebuilds. There are no stability guarantees (although the [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] snapshots are theoretically safer than an arbitrary git checkout), and portage will select `nightly` Rust if it is available and suitable (i.e. there\'s no maximum Rust version set) for the package. **hic sunt dracones**; you have been warned.

### [][Why [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] depends on [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]]]

The Rust compiler is self-hosting, that is, Rust is used to build Rust. Very early versions of the Rust compiler were written in OCaml, and it is still possible to bootstrap Rust this way; doing so requires building many, many versions of Rust. This method is not supported on Gentoo and would likely involve bootstrapping an appropriate OCaml first.

Since Rust is required to build Rust, some method of breaking this circular dependency is required. Legacy Gentoo Rust packaging (in the absence of [[[system-bootstrap]](https://packages.gentoo.org/useflags/system-bootstrap)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]) would always download an appropriate binary Rust release and use that to bootstrap the Rust compiler in the release tarball. Modern Gentoo Rust packaging makes this requirement more explicit by depending on appropriate versions of [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] and [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] to ensure that a suitable Rust is available at build-time.

It is currently possible to bootstrap Rust entirely from source (on amd64) using [[[dev-lang/mrustc]](https://packages.gentoo.org/packages/dev-lang/mrustc)[]] via [[[dev-lang/rust\[mrustc-bootstrap\]]](https://packages.gentoo.org/packages/dev-lang/rust)[]]; this requires building all intermediate slots until a desired version is reached.

Of course, if one doesn\'t mind binaries, [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] could be used directly instead, but this section focuses on [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]].

If one desires to use [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] but not build every intermediate Rust version first, try:

`root `[`#`]`emerge --oneshot dev-lang/rust dev-lang/rust-bin`

Users on legacy Rust packaging [poor world file hygiene](https://wiki.gentoo.org/wiki/Portage/Help/Maintaining_a_Gentoo_system#World_file_hygiene "Portage/Help/Maintaining a Gentoo system") may encounter blockers due to this change. They can normally be resolved by deselecting Rust entirely:

`root `[`#`]`emerge --deselect dev-lang/rust dev-lang/rust-bin virtual/rust`

If this does not resolve the issue, try reaching out for help on IRC in [[#gentoo](ircs://irc.libera.chat/#gentoo)] ([[webchat](https://web.libera.chat/#gentoo)]).

### [Distcc MAKEOPTS]

Rust does not support [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") compiling, however it is possible to use a binary host to fill this role. [Binary_package_guide#Advanced_topics](https://wiki.gentoo.org/wiki/Binary_package_guide#Advanced_topics "Binary package guide")

If a user still wishes to use distcc for some unknown reason, it may require a local [package.env] defined to avoid excessive I/O consumption when building on distcc tuned hosts (i.e. `MAKEOPTS="-j30 -l4"`, 30 is greater than 4 local CPU cores).

`--local-load` is not honored, so an appropriate `--jobs` value in relation to the locally available build resources must be passed:

[FILE] **`/etc/portage/env/makeopts.conf`**

    MAKEOPTS="-jN"

[FILE] **`/etc/portage/package.env/rust`**

    dev-lang/rust makeopts.conf

## [Configuration]

### [Environment variables]

`RUSTFLAGS` is an environment variable that Cargo^[\[1\]](#cite_note-1)^, the Rust package manager^[\[2\]](#cite_note-2)^, gives [rustc], the Rust compiler^[\[3\]](#cite_note-3)^, space-separated \"codegen\" `-C` flags^[\[4\]](#cite_note-4)^. Here are example settings, not including model specific parallelism^[\[5\]](#cite_note-5)^, for [[/etc/portage/make.conf]](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf"):

[FILE] **`/etc/portage/make.conf`**

    # target-cpu=native is the equivalent of -march=native in C/CXXFLAGS:
    RUSTFLAGS="-C target-cpu=native"
    # enable target-cpu=native and DT_RELR
    RUSTFLAGS="-C target-cpu=native -C link-arg=-Wl,-z,pack-relative-relocs"

#### [][Link Time Optimization (LTO)]

LTO in Rust programs should only be enabled on LLVM/CLANG compiler based systems, please see the [LTO](https://wiki.gentoo.org/wiki/LTO "LTO") article for more information.

#### [Optimization level]

There is no need in specifying:

[FILE] **`/etc/portage/make.conf`**

    RUSTFLAGS="-C opt-level=3"

explicitly, because official Rust documentation^[\[6\]](#cite_note-6)^ states that default optimization level on Release profile is set to 3 already.

### [Eselect Rust]

** Tip**\
[eselect-rust] does not have any impact on the version of Rust that Portage selects to build software.

There is an [eselect](https://packages.gentoo.org/packages/app-eselect/eselect-rust) available to switch between different Rust slots. Usage in the usual way, get a numbered list of installed Rust versions with:

`user `[`$`]`eselect rust list`

Set the version of rust with the number x via:

`user `[`$`]`eselect rust set x`

### [Rustup]

** Note**\
Portage supports slotted Rust installations; it is typically easier to unmask the specific slot and ask Portage to emerge it. [eselect-rust] can be used to trivially switch the Rust implementation on-the-fly, or the appropriate version can be prefixed into a user\'s `PATH` without administrative access. But it is fine to use [rustup] for local Rust development and leave the system Rust installation alone.

Rustup can be used to setup a cargo-compatible environment for Rust development. First, install the package:

`root `[`#`]`emerge --ask dev-util/rustup`

Then, use `rustup-init-gentoo` to symlink the system rust installation to the local user\'s home directory:

`user `[`$`]`rustup-init-gentoo --symlink`

    '/home/larry/.cargo/bin/rustc' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/rustdoc' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/cargo' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/rust-lldb' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/rust-gdb' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/rust-gdbgui' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/rls' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/cargo-clippy' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/clippy-driver' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/cargo-miri' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/rust-analyzer' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/rustfmt' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/cargo-fmt' -> '/usr/bin/rustup-init'
    '/home/larry/.cargo/bin/rustup' -> '/usr/bin/rustup-init'
    * Setting gentoo rust-1.77.1 as default toolchain
    rustup 1.27.0 (2024-03-24)
    info: This is the version for the rustup toolchain manager, not the rustc compiler.
    verbose: read metadata version: '12'
    verbose: creating toolchains directory: '/home/larry/.rustup/toolchains'
    verbose: installing toolchain 'gentoo'
    verbose: toolchain directory: '/home/larry/.rustup/toolchains/gentoo'
    verbose: linking directory from: '/home/larry/.rustup/toolchains/gentoo'
    verbose: toolchain 'gentoo' installed
    verbose: read metadata version: '12'
    info: default toolchain set to 'gentoo'
    Default host: x86_64-unknown-linux-gnu
    rustup home:  /home/larry/.rustup

    gentoo (default)
    rustc 1.77.1 (7cf61ebde 2024-03-27) (gentoo)
    * Prepend /home/larry/.cargo/bin to your PATH to use rustup
    * rustup selfupdate is disabled, it will be updated by portage

Alternatively, you can use `rustup-init` to install rust separately in your home directory, isolated from the system\'s rust installation. This may be necessary for tools that require a local user installation, for example the [esp-rs](https://github.com/esp-rs/espup) toolchain. You will need to add your local installation\'s rust binaries to your `PATH` such that they override the system\'s binaries, like so:

[FILE] **`~/.config/localrust.sh`Overriding system rust using a script**

    export PATH="$/.cargo/bin:$"

It might be desirable to add this script as an alias in your `.bashrc`, so you can use the system installation of rust by default, and switch to your local environment by running `localrust`:

[FILE] **`~/.bashrc`Adding alias in bashrc**

    alias localrust=". ~/.config/localrust.sh"

## [Usage]

### [Development]

While the purpose of Gentoo\'s Rust package is mainly to provide a build environment to emerge other packages that use Rust, it is still possible to develop in Rust with this package. The Rust compiler, [rustc], is installed and available as soon as the package is emerged. However, there are certain other things to consider when developing in Rust.

In a generic installation of Rust (one that is not done with Gentoo\'s Rust package) things are usually updated and installed with [[[dev-util/rustup]](https://packages.gentoo.org/packages/dev-util/rustup)[]].

Another way is to install another Rust for development separately with the instructions from the [Rust documentation.](https://www.rust-lang.org/tools/install)

### [Language servers]

For code autocompletion and highlighting, two language servers are available in the Rust universe: [Rust-analyzer](https://github.com/rust-analyzer/rust-analyzer) and the [Rust Language Server](https://github.com/rust-lang/rls).

As of today RLS is deprecated and now longer maintained. But it still comes with the Rust package when the [[[rls]](https://packages.gentoo.org/useflags/rls)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled. Rust-analyzer was merged into the Rust language and is now part of Rust since version 1.64.0. Rust-analyzer can be installed with the enabled USE flag [[[rust-analyzer]](https://packages.gentoo.org/useflags/rust-analyzer)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] for [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] (or [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]]).

In order for the language server to autosuggest code from the Rust standard library [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]] or [[[dev-lang/rust-bin\[rust-src\]]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] is required.

### [Code formatting]

Rust comes with its own built in code formatter, [rustfmt]. To use rustfmt, emerge [[[dev-lang/rust\[rustfmt\]]](https://packages.gentoo.org/packages/dev-lang/rust)[]] (or [[[dev-lang/rust-bin\[rustfmt\]]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]]). Code formatting is invoked in a project directory via [cargo fmt].

### [Code linting]

Rust also comes with an officially supported code linter called [Clippy](https://github.com/rust-lang/rust-clippy). To make Clippy available, emerge [[[dev-lang/rust\[clippy\]]](https://packages.gentoo.org/packages/dev-lang/rust)[]] or [[[dev-lang/rust-bin\[clippy\]]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]]).

## [See also]

-   [Application level package management](https://wiki.gentoo.org/wiki/Application_level_package_management "Application level package management") --- provides best practice recommendations on managing the coexistence of operating system and **application level package managers** on Gentoo.
-   [Assembly language](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language") --- the lowest level of all programming languages, typically represented as a series of CPU architecture specific mnemonics and related operands.
-   [C](https://wiki.gentoo.org/wiki/C "C") --- a programming language developed for Bell Labs in the early 1970s
-   [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++") --- a general-purpose programming language that originated from C
-   [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") --- a C/C++/Objective-C/C++, CUDA, and RenderScript language front-end for the LLVM project
-   [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") --- a heavily stack-oriented self-compiling procedural programming language that is only slightly more abstract than [assembly](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language").
-   [WD-40](https://wiki.gentoo.org/wiki/WD-40 "WD-40") --- a feature in Gentoo [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") to disable [Rust] being built on the system

## [[] References]

1.  [[[↑](#cite_ref-1)] [The Rust Project Developers. [Environment Variables](https://doc.rust-lang.org/cargo/reference/environment-variables.html) Retrieved on June 16, 2024.]]
2.  [[[↑](#cite_ref-2)] [The Rust Project Developers. [The Cargo Book](https://doc.rust-lang.org/cargo/index.html) Retrieved on June 16, 2024.]]
3.  [[[↑](#cite_ref-3)] [The Rust Project Developers. [The rustc Book](https://doc.rust-lang.org/rustc/what-is-rustc.html) Retrieved on June 16, 2024.]]
4.  [[[↑](#cite_ref-4)] [The Rust Project Developers. [Codegen Options](https://doc.rust-lang.org/rustc/codegen-options/index.html) Retrieved on June 16, 2024.]]
5.  [[[↑](#cite_ref-5)] [The Rust SIMD Performance Guide Contributors. [Rust SIMD Performance Guide](https://rust-lang.github.io/packed_simd/perf-guide/target-feature/rustflags.html) Retrieved on October 28, 2024.]]
6.  [[[↑](#cite_ref-6)] [Rust Docs [\[1\]](https://doc.rust-lang.org/book/ch14-01-release-profiles.html)]]