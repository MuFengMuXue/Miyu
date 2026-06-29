This is a short reference, intended to be read alongside [Basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") and the [cargo.eclass documentation](https://devmanual.gentoo.org/eclass-reference/cargo.eclass/index.html).

## Contents

-   [[1] [cargo.eclass]](#cargo.eclass)
    -   [[1.1] [Rust\'s dependency mechanism]](#Rust.27s_dependency_mechanism)
-   [[2] [Making a versioned ebuild]](#Making_a_versioned_ebuild)
    -   [[2.1] [Licenses]](#Licenses)
    -   [[2.2] [Common problems with dependencies in versioned ebuilds]](#Common_problems_with_dependencies_in_versioned_ebuilds)
        -   [[2.2.1] [crates.io dependencies]](#crates.io_dependencies)
        -   [[2.2.2] [GitHub/GitLab etc. dependencies]](#GitHub.2FGitLab_etc._dependencies)
    -   [[2.3] [Patching or updating crates]](#Patching_or_updating_crates)
        -   [[2.3.1] [Making a new release]](#Making_a_new_release)
        -   [[2.3.2] [Manually patching crates]](#Manually_patching_crates)
        -   [[2.3.3] [Using cargo.eclass]](#Using_cargo.eclass)
            -   [[2.3.3.1] [Substituting a compatible crate]](#Substituting_a_compatible_crate)
            -   [[2.3.3.2] [Overriding all crates with a particular name]](#Overriding_all_crates_with_a_particular_name)
-   [[3] [Writing live ebuilds]](#Writing_live_ebuilds)
    -   [[3.1] [Problems with live ebuilds]](#Problems_with_live_ebuilds)
        -   [[3.1.1] [\"can\'t update a git repository in the offline mode\"]](#.22can.27t_update_a_git_repository_in_the_offline_mode.22)
-   [[4] [USE flags]](#USE_flags)
    -   [[4.1] [Switching features off]](#Switching_features_off)
-   [[5] [Unbundling C libraries]](#Unbundling_C_libraries)
    -   [[5.1] [pkg-config crate]](#pkg-config_crate)
    -   [[5.2] [Common -sys crates]](#Common_-sys_crates)
    -   [[5.3] [Other -sys crates]](#Other_-sys_crates)
-   [[6] [Using a vendor tarball like in Go ebuilds]](#Using_a_vendor_tarball_like_in_Go_ebuilds)
    -   [[6.1] [Creating a vendor tarball]](#Creating_a_vendor_tarball)
    -   [[6.2] [Using a vendor tarball in an ebuild]](#Using_a_vendor_tarball_in_an_ebuild)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [cargo.eclass]

cargo.eclass is an eclass for utilizing Rust\'s own package manager, Cargo. Documentation for the eclass is available in [the relevant section of the Development Guide](https://devmanual.gentoo.org/eclass-reference/cargo.eclass/index.html) and in the cargo.eclass(5) man page provided by the [[[app-doc/eclass-manpages]](https://packages.gentoo.org/packages/app-doc/eclass-manpages)[]] package.

Cargo is very convenient for software developers. However, it comes with some caveats for maintainers.

Rust programs are usually statically bound. This makes runtime dependencies easier to figure out compared to C programs, but build dependencies are harder to get right. The good thing is that upstream needs to figure that out for packagers. Packagers only need to translate what upstream already figured out into the cargo.eclass way of handling dependency programs.

### [][Rust\'s dependency mechanism]

Rust dependencies come in the form of \'crates\'. Crates can be libraries or runnable programs. Like the term \'package\', \'crate\' is not defined strictly, so basically every Rust program that is provided in binary or source form can be considered a crate. In the context of packaging, crates are often dependency libraries of a package. Rust developers upload their crates along with documentation to [crates.io](https://crates.io). Other Rust developers can use the uploaded crates in their program by stating its name and version in a configuration file for Rust\'s build system, Cargo. If a dependency is only declared using the crate name, Cargo assumes it should download that dependency from crates.io.

However, developers can also declare dependencies with additional information, like a URL to a Git Repository and a Git tag, to get crates from elsewhere.

## [Making a versioned ebuild]

Gentoo has its own program to make ebuilds out of Rust projects automatically: [[[app-portage/pycargoebuild]](https://packages.gentoo.org/packages/app-portage/pycargoebuild)[]].

** Important**\
The user running [pycargoebuild] will need to belong to the `portage` group. Running it as superuser is also a possibility.

To use [pycargoebuild], obtain the repository of the Rust software being packaged (e.g. by cloning the repository), change to the directory containing the sources, and generate an ebuild by running:

`user `[`$`]`pycargoebuild ./`

If everything goes well, there will now be an ebuild in the repository, which can then be moved into an ebuild repository like ::gentoo or ::guru. However, note that the `HOMEPAGE` and `DESCRIPTION` variables in the ebuild will need to be added, and if the package is published on crates.io, it can be added to the `CRATES` variable (probably as `$@$`), and if it lives as an archive elsewhere, it should be added to `SRC_URI`. For cases where dependencies are not all on crates.io, see the [common problems](#Common_problems_with_dependencies_in_versioned_ebuilds) section for more information.

### [Licenses]

Automated ebuilds will have `LICENSE` assigned, but the value of this variable is not guaranteed to be correct. To generate a list of a Rust project\'s licenses, run:

`user `[`$`]`cargo license`

in the Rust repository.

Packagers must be aware that [cargo license] will give the licenses in SPDX format, which Gentoo does not always use. So some effort needs to be put into \'translating\' them.

Because the code of the dependencies is compiled into the finished binary (statically linked), all licenses of every crate used in a package must be stated in the `LICENSE` variable.

### [Common problems with dependencies in versioned ebuilds]

#### [crates.io dependencies]

If all dependencies are fetched from crates.io, the automatically generated ebuilds will often work from scratch. The crates.io dependencies are added to the `CRATES` variable in the ebuild, combining their name and version number with the \'@\' symbol, e.g.:

    CRATES="
           addr2line@0.21.0
           adler@1.0.2
           adler32@1.2.0
           ...
    "

and also add `$` to the `SRC_URI` variable, e.g.:

    SRC_URI="$"

These dependencies will automatically be fetched and unpacked into the right place via `cargo_src_unpack`, from cargo.eclass.

#### [][GitHub/GitLab etc. dependencies]

Sometimes upstream developers are not happy with the version of a crate on crates.io, or a crate is not available there and must instead be obtained from a git repository. In these situations, such a dependency is specified in [Cargo.toml] like this:

[FILE] **`Cargo.toml`**

    tree-sitter-haxe =

The above specifies that release 0.2.2 from the tree-sitter-haxe GitHub repository should be checked out.

The user can\'t clone a git repository without git-r3.eclass, but the user can simulate this in the ebuild. In this example, the user would add the lines:

    declare -A GIT_CRATES=(
           [tree-sitter-haxe]="https://github.com/vantreeseba/tree-sitter-haxe;32f6bda9b568ae47c89678096de9b4d0cbd450b8"
    )

to the ebuild.

The commit hash is obtained by browsing the files of that release (v0.2.2) on GitHub and copying it from the URL. It can also often be found in the [Cargo.toml] and [Cargo.lock] files of the upstream repository, by grepping the repository for the crate\'s name.

If the [Cargo.toml] of a Rust program has a line like:

    tree-sitter-c-sharp =

in its dependencies, it wants to fetch the latest commit on the master branch of that GitHub repository. This essentially means packagers must make a live ebuild, rather than a versioned ebuild.

Usually the cargo.eclass looks for [Cargo.toml] in the folder [\$WORKDIR/\$crate_name-\$commit-hash]. Thus, in the above example, the folder would be [\$WORKDIR/tree-sitter-haxe-32f6bda9b568ae47c89678096de9b4d0cbd450b8].

However, some crates have [Cargo.toml] in a different place, or have a different name in [Cargo.toml] as their GitHub repository name. In such cases, the path to [Cargo.toml] can be defined using:

    declare -A GIT_CRATES=(
           [tree-sitter-haxe]="https://github.com/vantreeseba/tree-sitter-haxe;32f6bda9b568ae47c89678096de9b4d0cbd450b8;tree-sitter-haxe-%commit%/mypath/to/cargotoml"
    )

where `%commit%` is automatically replaced with the commit hash specified.

If the last part of that line is not provided, the cargo.eclass composes that path out of the crate name (the part in `[]`) and the commit hash.

The path is a relative path that starts from [\$WORKDIR]. The part in `[]` usually needs to be the name of the package in the [Cargo.toml] of that package.

### [Patching or updating crates]

** Tip**\
Cargo crates almost always use [SemVer](https://semver.org/); use this knowledge and common sense when deciding on crate overrides / patches.

As the vast majority of Rust dependencies are in crates with fixed versions for a release, inevitably there will be a vulnerable (or otherwise outdated) crate that eventually needs to be patched. There are four ways to patch crates in a Gentoo ebuild.

#### [Making a new release]

The first (and most complex) is making a new release and dependency tarball (or just a new release that works with updated `CRATES`). This is relatively straightforward, but requires the most development effort. This approach is most useful where there are a number of crates that require updates, different versions are required, and replacements are non-trivial. This process is documented elsewhere, though the high level process involves using [cargo update] to update the Cargo metadata files [Cargo.] to include updated but compatible crates.

#### [Manually patching crates]

The second is manually patching the crate(s) in question within the ebuild environment. We don\'t often do this in Gentoo as there is most often an updated crate on crates.io, however it is sometimes unavoidable. When patching crates it is important to remember that the [.cargo-checksum.json] file **must** be updated to include the new checksum for each file that the patch changes. It is recommended that this approach only be used where required, and only for patches that cannot be fetched as an updated compatible crate from crates.io.

See [Adelie\'s Rust packaging](https://cgit.adelielinux.org/packages/tree/bootstrap/rust-1.73/ppc-libc-hugetlb.patch?id=e83dfc3c3c5e5490ef3b153a2fd9f4dec3012286) for a minimal example. The same approach can be used to patch a crate in `CRATES`, if required, but it may be better to just fix it upstream and ask for a new release.

#### [Using [[cargo.eclass](https://devmanual.gentoo.org/eclass-reference/cargo.eclass)]]

Finally there are the two [[cargo.eclass](https://devmanual.gentoo.org/eclass-reference/cargo.eclass)] -assisted methods:

##### [Substituting a compatible crate]

As the eclass unpacks dependencies into an offline repository and configures [cargo] to use this repository in place of crates.io, we can substitute compatible crates into `CRATES` then run [cargo update] to update the package against these dependencies. To do this, replace the crate in `CRATES` and then call the [cargo_update_crates] helper function in [src_prepare]. This calls [cargo update] with appropriate options to update the [Cargo.] files at build-time.

[FILE] **`foo-1.0.0-r1.ebuild`**

    CRATES="
        adler@1.0.2
    -   autocfg@1.1.0
    +   autocfg@1.2.0
        bindgen@0.65.1
        bit_field@0.10.1
        bitflags@1.3.2

    . . .

    # This whole phase is defined as cmake_src_prepare otherwise overrides it;
    # it was not previously required.
    +src_prepare()

##### [Overriding all crates with a particular name]

`paths = [...]` overrides: An array of paths to directories containing a [Cargo.toml]. [cargo] will read the [Cargo.toml] and override any crate with the same name in the dependency graph of the ([cargo]) package. This **does not** respect version constraints or the lock file. The eclass will automatically configure this for crates in `CRATE_PATHS_OVERRIDE`; crates in this variable are added to `CRATES` by the eclass, though it will not hurt to have them in both.

** Tip**\
Care *must* be taken to ensure that only compatible versions are being overridden. This method is not suitable when (e.g.) several different and SemVer-incompatible versions of the same crate are in `CRATES`. [cargo metadata] or [cargo tree] are useful tools for ensuring that this is the case.

Test the package extensively to ensure that no new bugs have been introduced. This method is primarily intended to support the replacement of vendored crates; consider whether it is more appropriate to substitute a new crate in `CRATES`.

[FILE] **`dev-lang/rust-1.54.0.ebuild`**

    # Requried to build against openssl-3.*
    CRATE_PATHS_OVERRIDE="
        openssl@0.10.35
        openssl-sys@0.9.65
    "
    . . .
    src_unpack() "/config.toml
    }

The [src_unpack] step is only necessary where the package in question overrides crates.io in *its* [cargo] config.

## [Writing live ebuilds]

First create the skeleton ebuild as described above. Then change the version in the ebuild\'s file name to 9999.

In the ebuild itself:

-   Remove the unnecessary `CRATES` variable.
-   Remove the unnecessary `SRC_URI` variable; sources are typically fetched via git-r3.eclass or similar. git-r3 should come after cargo on the inherit line.
-   Create a `src_unpack()` function, containing `cargo_live_src_unpack`:

<!-- -->

    src_unpack()

This will fetch the source from git and then the needed dependency crates using Cargo.

### [Problems with live ebuilds]

#### [][\"can\'t update a git repository in the offline mode\"]

When a Rust project uses unpinned dependencies in its [Cargo.toml], e.g.:

[CODE]

    tree-sitter-c-sharp =

Cargo will always want to check if that dependency is up-to-date in later stages of the ebuild. This will result in the error \"can\'t update a git repository in the offline mode\".

To fix this, add `cargo_src_configure --frozen` to `src_configure()`. This will stop Cargo from checking whether what it just fetched is up-to-date.

## [USE flags]

USE flags for Rust are usually added via cargo.eclass:

[CODE]

    src_configure()

### [Switching features off]

Often Rust programs do not allow switching individual default features off. So in order to only enable certain default features, disable all default features with `cargo_src_configure --no-default-features`, then enable the desired features via `myfeatures`, as described above.

## [Unbundling C libraries]

Start with constructing a dependency tree:

`user `[`$`]`cargo tree --all-features | less`

There\'s a naming convention[\[1\]](https://doc.rust-lang.org/cargo/reference/build-scripts.html#-sys-packages) for crates linking with native libraries to have a [-sys] suffix. The user\'s job as a maintainer is to find out which features pull them and put corresponding native libraries into package dependencies.

However, most crates use vendored C libraries by default (see [[[bug #709568]](https://bugs.gentoo.org/show_bug.cgi?id=709568)[]]), which is discouraged by Gentoo policies.

### [[pkg-config] crate]

If this crate is pulled, the user need to add [[[virtual/pkgconfig]](https://packages.gentoo.org/packages/virtual/pkgconfig)[]] to ebuild\'s [BDEPEND] and explicitly allow cross-compilation:

[CODE]

    export PKG_CONFIG_ALLOW_CROSS=1

### [Common [-sys] crates]

+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Crate                                                                                                            | Dependency                                                                                                                                                                                                                                                                                                                                                                      | Unbundling method                                                                                                                       | Notes                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [bzip2-sys]           | [[[app-arch/bzip2]](https://packages.gentoo.org/packages/app-arch/bzip2)[]]                | [Project:Rust/sys crates#bzip2-sys](https://wiki.gentoo.org/wiki/Project:Rust/sys_crates#bzip2-sys "Project:Rust/sys crates")           | Uses system libs unless revdeps enable [static] feature                                                                                                          |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [jemalloc-sys]        | [[[dev-libs/jemalloc]](https://packages.gentoo.org/packages/dev-libs/jemalloc)[]]       | ::::: gw-box                                                                                                                            |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | ::: box-caption                                                                                                                         |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | [CODE]                                                                    |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                                                                                     |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                         |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                    |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |     export JEMALLOC_OVERRIDE="$/usr/$(get_libdir)/libjemalloc.so"                                                             |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                                                                                     |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::::                                                                                                                                   |                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [libdeflate-sys]      | [[[app-arch/libdeflate]](https://packages.gentoo.org/packages/app-arch/libdeflate)[]] |                                                                                                                                         | Needs a workaround: [Project:Rust/sys crates#libdeflate-sys](https://wiki.gentoo.org/wiki/Project:Rust/sys_crates#libdeflate-sys "Project:Rust/sys crates")                                                                                                 |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [libgit2-sys]         | [[[dev-libs/libgit2]](https://packages.gentoo.org/packages/dev-libs/libgit2)[]]          | [Project:Rust/sys crates#libgit2-sys](https://wiki.gentoo.org/wiki/Project:Rust/sys_crates#libgit2-sys "Project:Rust/sys crates")       | Since 0.16.0                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [libsqlite3-sys]      | [[[dev-db/sqlite:3]](https://packages.gentoo.org/packages/dev-db/sqlite:3)[]]             | [Project:Rust/sys crates#libsqlite3-sys](https://wiki.gentoo.org/wiki/Project:Rust/sys_crates#libsqlite3-sys "Project:Rust/sys crates") | Since 0.28.0                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [libssh2-sys]         | [[[net-libs/libssh2]](https://packages.gentoo.org/packages/net-libs/libssh2)[]]          | [Project:Rust/sys crates#libssh2-sys](https://wiki.gentoo.org/wiki/Project:Rust/sys_crates#libssh2-sys "Project:Rust/sys crates")       |                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [libz-sys]            | [[[sys-libs/zlib]](https://packages.gentoo.org/packages/sys-libs/zlib)[]]                   |                                                                                                                                         | Uses system libs unless revdeps enable [static] or [zlib-ng] features |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [lz4-sys]             | [[[app-arch/lz4]](https://packages.gentoo.org/packages/app-arch/lz4)[]]                      | Not available                                                                                                                           | Always uses bundled library                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [openssl-sys]         | [[[dev-libs/openssl]](https://packages.gentoo.org/packages/dev-libs/openssl)[]]          | ::::: gw-box                                                                                                                            | Since 0.9.55                                                                                                                                                                                                                                                |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | ::: box-caption                                                                                                                         |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | [CODE]                                                                    |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                                                                                     |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                         |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                    |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |     export OPENSSL_NO_VENDOR=1                                                                                                          |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                                                                                     |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::::                                                                                                                                   |                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [rust-librocksdb-sys] | [[[dev-libs/rocksdb]](https://packages.gentoo.org/packages/dev-libs/rocksdb)[]]          | ::::: gw-box                                                                                                                            | Compatible with an exact version only                                                                                                                                                                                                                       |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | ::: box-caption                                                                                                                         |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | [CODE]                                                                    |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                                                                                     |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                         |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                    |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |     export SNAPPY_LIB_DIR="$/usr/$(get_libdir)"                                                                               |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |     export ROCKSDB_LIB_DIR="$/usr/$(get_libdir)"                                                                              |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 |     export ROCKSDB_INCLUDE_DIR="$/usr/include"                                                                                |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::                                                                                                                                     |                                                                                                                                                                                                                                                             |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                 | :::::                                                                                                                                   |                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [zstd-sys]            | [[[app-arch/zstd]](https://packages.gentoo.org/packages/app-arch/zstd)[]]                   | [Project:Rust/sys crates#zstd-sys](https://wiki.gentoo.org/wiki/Project:Rust/sys_crates#zstd-sys "Project:Rust/sys crates")             | Since [0.12.2](https://github.com/gyscos/zstd-rs/releases/tag/v0.12.2)                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### [Other [-sys] crates]

First, inspect crate\'s [Cargo.toml] for features that force static linking. If they are enabled by any revdeps, the user has run out of luck.

Then, inspect crate\'s [build.rs] script for environment variables that control build flow. Set them in ebuild\'s [src_configure()] or global scope.

## [Using a vendor tarball like in Go ebuilds]

The [go-module.eclass](https://devmanual.gentoo.org/eclass-reference/go-module.eclass/index.html) and the cargo.eclass are very similar regarding the functionality of loading statically linked dependencies. In a Go ebuild a packager defines the variable EGO_SUM with a list of dependencies from upstream, in a Rust ebuild the CRATES variable has the same functionality. The eclasses then proceed to download those dependencies and put them in the correct places in the working directory.

While it is an ongoing and controversial discussion whether the EGO_SUM-functionality should be deprecated or not in the go-module.eclass, the cargo.eclass is built with the CRATES variable in mind. The go.eclass offers the possibility to use a vendor-tarball instead of the EGO_SUM-functionality. That is a tar archive that contains all the statically linked dependencies. While Cargo also offers the possibility to create such a vendor-tarball as easily as Go, the cargo.eclass does not offer to use such a vendor-tarball without doing some extra steps.

Using a vendor-tarball instead of using the CRATES variable has some benefits. For example, the user don\'t need to recreate the list of dependencies (e.g. by using `pycargoebuild` in the upstream repo) and copy it into the new ebuild when bumping the version of that ebuild. If the vendor tarball is hosted right, bumping a Rust-ebuild is as easy as renaming the ebuilds filename with the new version.

#### [Creating a vendor tarball]

** Note**\
Vendor tarballs can be automatically generated in GitHub Actions using [projg2/crate-dist-mirror-action](https://github.com/projg2/crate-dist-mirror-action). You can either ask on [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") to set up a mirror in the [https://github.com/gentoo-crate-dist](https://github.com/gentoo-crate-dist) namespace or do it yourself in your personal namespace.

Creating a vendor tarball can be done by running `cargo vendor` in the upstream repository. It will create a vendor folder, which can be put into a tar archive with `XZ_OPT='-T0 -9' tar -acf vendor.tar.xz vendor`.

Note that current versions of cargo no longer generate a `vendor-config.toml` file and instead output the equivalent to stdout. You may still require a `vendor-config.toml` file however (see below). You can create one yourself like so: `cargo vendor > vendor-config.toml && mv vendor-config.toml vendor/`

#### [Using a vendor tarball in an ebuild]

Because the cargo.eclass is somewhat built with the CRATES variable in mind, it will complain when this variable is not set when the eclass in inherited. To work around this, the user can define the variable as `CRATES=" "`. The cargo.eclass looks for dependencies in `$ECARGO_VENDOR` directory which defaults to [\$CARGO_HOME/gentoo]. `$CARGO_HOME` itself is set to [\$WORKDIR/cargo_home]. A packager can either

1.  change default variable by setting `$ECARGO_VENDOR` to other location before src_unpack() or
2.  unpack the vendor-tarball into default `$ECARGO_VENDOR` directory, (by not calling `default` or `cargo_src_unpack` in src_unpack() and writing src_unpack() with own instructions.) or
3.  let portage do its default thing and let it unpack the vendor tarball into \$WORKDIR, then do `ln -s "$/<extracted directory>/"* "$/gentoo/"`.

In the case that a packages uses crates from git instead of crates.io cargo needs additional configuration. Luckily the vendor tarball has that configuration already included in a file called `vendor-config.toml`. This file expects the directory with the vendored sources in the working directory of the package itself. So when the vendor tarball is unpacked in `$WORKDIR/vendor` link it to the packages workdir like this for example: `ln -s "$/vendor/" "$/lapce-$/vendor" || die` (Set the path accordingly) The contents of `vendor-config.toml` collide with some settings that the cargo-eclass creates during `cargo_gen_config` in `$/config.toml`. Those settings need to be deleted:

    sed -i "$/config.toml" -e '/source.crates-io/d'  || die
    sed -i "$/config.toml" -e '/replace-with = "gentoo"/d'  || die
    sed -i "$/config.toml" -e '/local-registry = "\/nonexistent"/d'  || die

Then the contents of `vendor-config.toml` can be appended to `$/config.toml`: `cat "$/vendor/vendor-config.toml" >> "$/config.toml" || die`

## [See also]

-   [Basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") --- getting started writing **[ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild")**, to harness the power of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), to install and manage even more software.
-   [User:Schievel/autocreate_rust_sources](https://wiki.gentoo.org/wiki/User:Schievel/autocreate_rust_sources "User:Schievel/autocreate rust sources")

## [External resources]

-   [Documentation of cargo.eclass](https://devmanual.gentoo.org/eclass-reference/cargo.eclass/index.html)