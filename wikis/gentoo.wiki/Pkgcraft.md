[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Pkgcraft&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/pkgcraft-tools)

[[]][GitHub](https://github.com/pkgcraft/pkgcraft)

**pkgcraft** is a highly experimental tooling ecosystem for Gentoo written in Rust.

It can be used for metadata generation via [pk repo metadata] with a measurable performance improvement for metadata generation. It uses a forked copy of bash, wrapped by pkgcraft\'s scallop library. ^[\[1\]](#cite_note-1)^

It can also be used for QA checking via [pkgcruft] and [pkgcruft-git].

** Warning**\
pkgcraft is highly experimental and may result in breakage.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage (pkgcruft)]](#Usage_.28pkgcruft.29)
-   [[4] [Usage (pkgcruft-git)]](#Usage_.28pkgcruft-git.29)
-   [[5] [Usage (pkgcraft-tools)]](#Usage_.28pkgcraft-tools.29)
    -   [[5.1] [Category/package/version (cpv) utils]](#Category.2Fpackage.2Fversion_.28cpv.29_utils)
    -   [[5.2] [Dependency commands]](#Dependency_commands)
    -   [[5.3] [Package commands]](#Package_commands)
    -   [[5.4] [Repository commands]](#Repository_commands)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/pkgcraft-tools](https://packages.gentoo.org/packages/sys-apps/pkgcraft-tools) [[]] [pkgcraft-based tools for Gentoo]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-01 15:46] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

There are several members of the Pkgcraft family.

The main tools reside in:

`root `[`#`]`emerge --ask sys-apps/pkgcraft-tools`

pkgcruft is pkgcraft\'s QA tool, like [Pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck"):

`root `[`#`]`emerge --ask dev-util/pkgcruft`

pkgcruft also has a git hook available:

`root `[`#`]`emerge --ask dev-vcs/pkgcruft-git`

Python and C bindings exist:

`root `[`#`]`emerge --ask dev-python/pkgcraft`

`root `[`#`]`emerge --ask sys-libs/pkgcraft`

## [Configuration]

Pkgcraft has its own configuration, distinct from Portage\'s [/etc/portage], residing at [/etc/pkgcraft].

To configure repositories, consider the following example:

[FILE] **`/etc/pkgcraft/repos/gentoo`**

    location = "/var/db/repos/gentoo"
    format = "ebuild"

See [https://github.com/pkgcraft/pkgcraft/issues/244](https://github.com/pkgcraft/pkgcraft/issues/244) and [https://github.com/pkgcraft/pkgcraft/issues/335](https://github.com/pkgcraft/pkgcraft/issues/335) for background.

## [][Usage (pkgcruft)]

pkgcruft is a [QA scanning tool](https://pkgcraft.github.io/posts/evolving-qa-tooling/), provided by [[[dev-util/pkgcruft]](https://packages.gentoo.org/packages/dev-util/pkgcruft)[]]. It is similar to [Pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck").

The main entrypoint is [pkgcruft scan] which is to be run within an ebuild repository.

It has many filters available. For example, to scan all maintainer-needed packages:

`user `[`$`]`pkgcruft scan --filters "maintainers is none"`

    app-admin/amazon-ec2-init
      VariableOrder: version 20101127-r2, line 14: LICENSE should occur before KEYWORDS

    app-admin/chroot_safe
      EapiDeprecated: version 1.4-r1: 7

## [][Usage (pkgcruft-git)]

A [git](https://wiki.gentoo.org/wiki/Git "Git") hook is available for pkgcruft to run before [git push], provided by [[[dev-vcs/pkgcruft-git]](https://packages.gentoo.org/packages/dev-vcs/pkgcruft-git)[]].

Setup is easy. Inside of a repository clone, run:

`user `[`$`]`ln -s /usr/bin/pkgcruft-git-pre-push .git/hooks/pre-push`

Alternatively, a full push URL can be given:

`user `[`$`]`echo 'pkgcruft-git-pre-push origin git@git.gentoo.org:repo/proj/gentoo.git' > .git/hooks/pre-push`

`user `[`$`]`chmod +x .git/hooks/pre-push`

Then upon running [git push], a QA report will be shown and prevent pushing if serious errors are found:

`user `[`$`]`git push`

    app-misc/tmuxp
      PythonUpdate: version 1.54.0: python3_14

    app-misc/yq
      PythonUpdate: version 3.4.3: python3_14

## [][Usage (pkgcraft-tools)]

[[[sys-apps/pkgcraft-tools]](https://packages.gentoo.org/packages/sys-apps/pkgcraft-tools)[]] consists of a single binary: [/usr/bin/pk]. It also has shell-completions for bash, fish and zsh.

### [][Category/package/version (cpv) utils]

Compare cpv with \<, \<=, ==, !=, \>=, and \> operators, returns 0 if true:

`user `[`$`]`pk cpv compare "cat/pkg-1.2.3-r1 <= cat/pkg-1.2.3-r2" && echo Yes`

Yes

Determine if a cpv intersects another value:

`user `[`$`]`pk cpv intersect cat/pkg-1.2.3-r1 =cat/pkg-1* && echo Yes`

Yes

Parse cpv and optionally print formatted output:

`user `[`$`]`pk cpv parse -f "/" cat/pkg-1.0-r1`

cat/pkg-1.0

Collapse cpvs into a set:

`user `[`$`]`pk cpv set a/b-1 a/b-2 a/b-1`

a/b-1\
a/b-2

Sort cvps:

`user `[`$`]`pk cpv sort $(equery list '*')`

### [Dependency commands]

Compare/intersect/parse/set/sort dependencies:

`user `[`$`]`pk dep compare "cat/pkg == cat/pkg" && echo Yes`

`user `[`$`]`pk dep intersect ">=cat/pkg-1" "cat/pkg-9999" && echo Yes`

`user `[`$`]`pk dep parse -f "" cat/pkg`

`user `[`$`]`pk dep set cat/a cat/b cat/a`

`user `[`$`]`pk dep sort $(cat /var/lib/portage/world)`

### [Package commands]

Output ebuild environment, e.g. SRC_URI for each package in gentoo repository, ignoring invalid packages:

`user `[`$`]`pk pkg env -f SRC_URI -r gentoo -i`

Find all packages that have [[[dev-cpp/nlohmann_json]](https://packages.gentoo.org/packages/dev-cpp/nlohmann_json)[]] in `RDEPEND` (header-only libraries should usually be in `DEPEND`):

`user `[`$`]`pk pkg env -f RDEPEND -r gentoo -i | sed -n '\|^RDEPEND=.*dev-cpp/nlohmann_json| ; /./h'`

Fetch distfiles. Example: pretend to fetch all versions of fastfetch.

`user `[`$`]`pk pkg fetch --verbose -pretend --repo gentoo app-misc/fastfetch`

Manifest manipulation. Example: force redownload and recalculate hashes in the Manifest file:

`user `[`$`]`pk pkg manifest --force --concurrent 3 app-misc/fastfetch`

[pk pkg metadata] - manipulate cached package metadata (regenerate/remove).

Run the pkg_pretend phase: [pk pkg pretend \<target\>\...]

Show reverse dependencies of a package: [pk pkg revdeps \--repo gentoo dev-cpp/gtest]

Output package keywords: [pk pkg showkw dev-cpp/gtest]

Benchmark ebuild sourcing: [pk pkg source /var/db/repos/gentoo \--sort]

### [Repository commands]

Output statistics for eapi, eclass, license, mirrors:

`user `[`$`]`pk repo eapi gentoo`

`user `[`$`]`pk repo eclass gentoo`

`user `[`$`]`pk repo license gentoo`

`user `[`$`]`pk repo mirror gentoo`

[pk pkg metadata] - manipulate repository metadata (clean/regen/remove).

## [See also]

-   [Pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore") --- an alternative package manager for Gentoo that aims for high performance, extensibility, and a clean design.
-   [pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck") --- a [pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore")-based QA utility for ebuild repos.
-   [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.

## [References]

1.  [[[↑](#cite_ref-1)] [[Metadata cache generation](https://pkgcraft.github.io/posts/metadata-cache-generation/)]]