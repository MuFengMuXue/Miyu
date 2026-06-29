This is a short reference, intended to be read alongside [Basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") and the [go-module.eclass documentation](https://devmanual.gentoo.org/eclass-reference/go-module.eclass/index.html).

## Contents

-   [[1] [go-module eclass]](#go-module_eclass)
    -   [[1.1] [Packaging the dependencies]](#Packaging_the_dependencies)
        -   [[1.1.1] [Vendor tarball]](#Vendor_tarball)
        -   [[1.1.2] [Dependency tarball]](#Dependency_tarball)
        -   [[1.1.3] [Uploading the tarball]](#Uploading_the_tarball)
    -   [[1.2] [Compiling and installing]](#Compiling_and_installing)
    -   [[1.3] [Writing live ebuilds]](#Writing_live_ebuilds)
    -   [[1.4] [Unbundling C/C++ libraries]](#Unbundling_C.2FC.2B.2B_libraries)
-   [[2] [Licenses]](#Licenses)
-   [[3] [See also]](#See_also)

## [go-module eclass]

If the software to be packaged has a file named [go.mod] in its top level directory, it uses modules and the ebuild should inherit this eclass.

### [Packaging the dependencies]

Ebuilds using the [go-module](https://devmanual.gentoo.org/eclass-reference/go-module.eclass/index.html) eclass are different from most other ebuilds, because they have to include every go dependency. With some luck, the project will have a [vendor/] directory and no special action will be needed. If it doesn\'t, in the short-term, the dependencies will have to be packaged manually. But longer term, try to convince upstream to [generate a tarball](https://github.com/noborus/ov/pull/196/files) in CI.

Previously, go-module packages often used `EGO_SUM`, but [that is deprecated](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=62fb29b23e3bc0eec89b6cf33d33c6cc939c1990) and will not be covered here. The currently favored method is creating a vendor or dependency-tarball.

** Note**\
Dependency tarballs can be automatically generated in GitHub Actions using [projg2/golang-dist-mirror-action](https://github.com/projg2/golang-dist-mirror-action). You can either ask on [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") to set up a mirror in the [https://github.com/gentoo-golang-dist](https://github.com/gentoo-golang-dist) namespace or do it yourself in your personal namespace.

Write the ebuild like normal, `inherit go-module` and add the upstream tarball to `SRC_URI`. Then unpack the package and [cd] to the build directory:

`user `[`$`]`cd "$(portageq get_repo_path / <repo name>)"/app-misc/foo `

`user `[`$`]`nano foo-1.ebuild `

`user `[`$`]`ebuild foo-1.ebuild unpack `

`user `[`$`]`cd /path/to/the/unpacked/source/foo-1 `

#### [Vendor tarball]

This method produces far smaller tarballs, but might not include everything needed to compile the package, especially if the dependencies compile C or C++ code:

`user `[`$`]`go mod vendor `

`user `[`$`]`cd .. `

`user `[`$`]`tar --create --owner root --group root --auto-compress --file foo-1-vendor.tar.xz foo-1/vendor `

Upload the tarball somewhere and add it to `SRC_URI`.

#### [Dependency tarball]

If the package won\'t compile because [the vendor tarball has not all dependencies](https://archives.gentoo.org/gentoo-dev/message/c29e1c6a355101fd00eb0cbc49b1c540), a dependency tarball is needed:

`user `[`$`]`GOMODCACHE="$"/go-mod go mod download -modcacherw -x `

`user `[`$`]`tar --create --owner root --group root --auto-compress --file foo-1-deps.tar.xz go-mod `

Upload the tarball somewhere and add it to `SRC_URI`.

** Note**\
Some Go projects do not set [go.mod] and [go.sum] in the root directory. So need to enter the specific directory to execute the above commands, otherwise likely to get an incomplete [xxx-deps.tar.xz].

#### [Uploading the tarball]

Gentoo developers can put the generated tarballs into their devspace, but what about others?

-   For those having access to a web or FTP server, or a file hosting service, put it there. Make sure the file can be downloaded without having to solve a captcha or having a cookie set. The easiest way to test this is by downloading it with [wget].
-   For those who have access to a git forge such as GitLab, Gitea, GitHub, ... create an empty repository, add a new tag for each new version (named `$`) and upload the tarballs to these "releases". Make sure that the host of the forge allows this usage.
-   An alternative approach when having access to a git forge is using a CI pipeline to automatically create and publish dependency tarballs. An example for automating this with the GitLab CI can be found here: [https://gitlab.fem-net.de/gentoo/fem-overlay-vendored](https://gitlab.fem-net.de/gentoo/fem-overlay-vendored).

### [Compiling and installing]

Since the go-module eclass doesn\'t implement `src_compile()` and `src_install()`, this must be done manually:

[FILE] **`foo-1.ebuild`Simple implementation of the compile and install phases**

    …
    src_compile()

    src_install()
    …

### [Writing live ebuilds]

First create the skeleton ebuild as described above. Then change the version in the ebuild\'s file name to 9999.

In the ebuild itself:

-   Remove the unnecessary `SRC_URI` variable; sources are typically fetched via git-r3.eclass or similar. git-r3 should come after go-module on the inherit line.

<!-- -->

-   Create a `src_unpack()` function:

<!-- -->

     src_unpack()

This will fetch the source from git and then the needed modules using go.

### [][Unbundling C/C++ libraries]

One way to detect bundled C or C++ libraries is to create a vendor tarball instead of a dependency tarball, because the former does not include the C/C++ source code. If the build fails, there is a good chance one has been found. Determine the go package that caused the failure by studying the build log and look into its source code. Go uses `#cgo` statements in go files to set compiler commands. With luck, the author included a define to switch from compiling the library to using the system one:

[FILE] **`foo-1-unbundle-webp.patch`Example patch for unbundling libwebp**

    --- a/vendor/github.com/bep/gowebp/internal/libwebp/a__cgo.go
    +++ b/vendor/github.com/bep/gowebp/internal/libwebp/a__cgo.go
    @@ -2,5 +2,6 @@

     package libwebp

    -// #cgo linux LDFLAGS: -lm
    +// #cgo linux LDFLAGS: -lm -lwebp
    +// #cgo CFLAGS: -DLIBWEBP_NO_SRC
     import "C"
    --
    2.35.1

## [Licenses]

Since Go programs are statically linked, it is important that the ebuild\'s `LICENSE` setting includes the licenses of all statically linked dependencies. So please make sure it is accurate. Use a utility like [[[dev-go/go-licenses]](https://packages.gentoo.org/packages/dev-go/go-licenses)[]] to extract this information.

** Note**\
Please remember that the generated license names may clash with licenses identifiers in gentoo, the identifier for the bsd-3-clause license shows as BSD-3-Clause, but it\'s identifier for gentoo is BSD

** Note**\
`...` has a special meaning in go

I think that to run `go-licenses` you need to `cd` into the untarred tarball directory, where you can find `vendor/` and `go.mod`, then run `go-licenses report ...` or `go-licenses report ./...`. You can get the list of licenses with `go-licenses report ... | awk -F, '' | sort | uniq`.

## [See also]

-   [Basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") --- getting started writing **[ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild")**, to harness the power of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), to install and manage even more software.
-   [Go ebuild tricks](https://wiki.gentoo.org/wiki/Go_ebuild_tricks "Go ebuild tricks") --- a collection of more niche Go packaging issues & how to tackle them, in lieu of a full-blown Python guide analogue.

<!-- -->

-   [go-module.eclass](https://devmanual.gentoo.org/eclass-reference/go-module.eclass/index.html)