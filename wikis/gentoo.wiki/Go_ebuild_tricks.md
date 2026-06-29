Packaging Go can often feel like a foreign experience. This is a collection of more niche Go packaging issues & how to tackle them, in lieu of a full-blown Python guide analogue..

## Contents

-   [[1] [Upgrading a dependency]](#Upgrading_a_dependency)
    -   [[1.1] [Example]](#Example)
-   [[2] [go tags]](#go_tags)
-   [[3] [Example]](#Example_2)
-   [[4] [See Also]](#See_Also)

### [Upgrading a dependency]

1.  Unpack the tarball and create a git repository to easily patch ([git init && git add . && git commit -m initial])
2.  Identify the problematic module(s).
3.  Instruct Go to upgrade them: [go get -x -u github.com/DataDog/zstd@v1.5.2]
4.  Apply the patch to the ebuild (it should touch [go.sum] and [go.mod])
5.  It may be necessary to drop references to the old module in those files!

#### [Example]

Take [dnsx](https://github.com/projectdiscovery/dnsx)\'s [1.1.1 release](https://github.com/projectdiscovery/dnsx/tree/v1.1.1).

For the purposes of this example, assume some annoying bug affects the zstd Go module included in 1.1.1.

First, identify the version:

`user `[`$`]`grep -rsin "zstd" go.mod go.sum`

    go.mod:25:      github.com/DataDog/zstd v1.4.5 // indirect
    go.sum:10:github.com/DataDog/zstd v1.4.5 h1:EndNeuB0l9syBZhut0wns3gV1hL8zX8LIu6ZiVHWLIQ=
    go.sum:11:github.com/DataDog/zstd v1.4.5/go.mod h1:1jcaCB/ufaK+sKp1NBhlGmpz41jOoPQ35bpF36t7BBo=

At this point, one may check upstream for the zstd module at [https://github.com/DataDog/zstd](https://github.com/DataDog/zstd) and note there\'s *much* newer versions available!

Attempt to upgrade the module to the latest version (1.5.2 at time of writing) to see if it fixes the hypothetical bug:

`user `[`$`]`go get -x -u github.com/DataDog/zstd@v1.5.2`

    # get https://proxy.golang.org/github.com/@v/v1.5.2.info
    # get https://proxy.golang.org/github.com/%21data%21dog/@v/v1.5.2.info
    # get https://proxy.golang.org/github.com/%21data%21dog/@v/v1.5.2.info: 404 Not Found (0.147s)
    # get https://proxy.golang.org/github.com/@v/v1.5.2.info: 404 Not Found (0.173s)
    # get https://proxy.golang.org/github.com/%21data%21dog/zstd/@v/list
    # get https://proxy.golang.org/github.com/%21data%21dog/zstd/@v/list: 200 OK (0.036s)
    go: upgraded github.com/DataDog/zstd v1.4.5 => v1.5.2

Check out what the command actually did, via [git diff]:

[FILE] **`git diff output`**

    --- a/go.mod
    +++ b/go.mod
    @@ -22,7 +22,7 @@ require (

     require (
            github.com/AndreasBriese/bbloom v0.0.0-20190825152654-46b345b51c96 // indirect
    -       github.com/DataDog/zstd v1.4.5 // indirect
    +       github.com/DataDog/zstd v1.5.2 // indirect
            github.com/akrylysov/pogreb v0.10.1 // indirect
            github.com/andres-erbsen/clock v0.0.0-20160526145045-9e14626cd129 // indirect
            github.com/asaskevich/govalidator v0.0.0-20210307081110-f21760c49a8d // indirect
    --- a/go.sum
    +++ b/go.sum
    @@ -9,6 +9,8 @@ github.com/CloudyKit/fastprinter v0.0.0-20170127035650-74b38d55f37a/go.mod h1:EF
     github.com/CloudyKit/jet v2.1.3-0.20180809161101-62edd43e4f88+incompatible/go.mod h1:HPYO+50pSWkPoj9Q/eq0aRGByCL6ScRlUmiEX5Zgm+w=
     github.com/DataDog/zstd v1.4.5 h1:EndNeuB0l9syBZhut0wns3gV1hL8zX8LIu6ZiVHWLIQ=
     github.com/DataDog/zstd v1.4.5/go.mod h1:1jcaCB/ufaK+sKp1NBhlGmpz41jOoPQ35bpF36t7BBo=
    +github.com/DataDog/zstd v1.5.2 h1:vUG4lAyuPCXO0TLbXvPv7EB7cNK1QV/luu55UHLrrn8=
    +github.com/DataDog/zstd v1.5.2/go.mod h1:g4AWEaM3yOg3HYfnJ3YIawPnVdXJh9QME85blwSAmyw=
     github.com/Joker/hpp v1.0.0/go.mod h1:8x5n+M1Hp5hC0g8okX3sR3vFQwynaX/UgSOM9MeBKzY=
     github.com/Joker/jade v1.0.1-0.20190614124447-d475f43051e7/go.mod h1:6E6s8o2AE4KhCrqr6GRJjdC/gNfTdxkIXvuGZZda2VM=
     github.com/OneOfOne/xxhash v1.2.2/go.mod h1:HSdplMjZKSmBqAxg5vPj2TmRDmfkzw+cTzAElWljhcU=

It seems that Go *may* still build the old module (even if it may or may not use the older version). It\'s possible to drop the old entry to mitigate the risk of at least a double-build:

`user `[`$`]`sed -i -e '/github.com.*zstd.*1.4.5/d' go.sum go.mod`

Giving a final [diff] that can be applied in the ebuild:

[FILE] **`git diff output`**

    --- a/go.mod
    +++ b/go.mod
    @@ -22,7 +22,7 @@ require (

     require (
            github.com/AndreasBriese/bbloom v0.0.0-20190825152654-46b345b51c96 // indirect
    -       github.com/DataDog/zstd v1.4.5 // indirect
    +       github.com/DataDog/zstd v1.5.2 // indirect
            github.com/akrylysov/pogreb v0.10.1 // indirect
            github.com/andres-erbsen/clock v0.0.0-20160526145045-9e14626cd129 // indirect
            github.com/asaskevich/govalidator v0.0.0-20210307081110-f21760c49a8d // indirect
    --- a/go.sum
    +++ b/go.sum
    @@ -7,8 +7,8 @@ github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03
     github.com/BurntSushi/xgb v0.0.0-20160522181843-27f122750802/go.mod h1:IVnqGOEym/WlBOVXweHU+Q+/VP0lqqI8lqeDx9IjBqo=
     github.com/CloudyKit/fastprinter v0.0.0-20170127035650-74b38d55f37a/go.mod h1:EFZQ978U7x8IRnstaskI3IysnWY5Ao3QgZUKOXlsAdw=
     github.com/CloudyKit/jet v2.1.3-0.20180809161101-62edd43e4f88+incompatible/go.mod h1:HPYO+50pSWkPoj9Q/eq0aRGByCL6ScRlUmiEX5Zgm+w=
    -github.com/DataDog/zstd v1.4.5 h1:EndNeuB0l9syBZhut0wns3gV1hL8zX8LIu6ZiVHWLIQ=
    -github.com/DataDog/zstd v1.4.5/go.mod h1:1jcaCB/ufaK+sKp1NBhlGmpz41jOoPQ35bpF36t7BBo=
    +github.com/DataDog/zstd v1.5.2 h1:vUG4lAyuPCXO0TLbXvPv7EB7cNK1QV/luu55UHLrrn8=
    +github.com/DataDog/zstd v1.5.2/go.mod h1:g4AWEaM3yOg3HYfnJ3YIawPnVdXJh9QME85blwSAmyw=
     github.com/Joker/hpp v1.0.0/go.mod h1:8x5n+M1Hp5hC0g8okX3sR3vFQwynaX/UgSOM9MeBKzY=
     github.com/Joker/jade v1.0.1-0.20190614124447-d475f43051e7/go.mod h1:6E6s8o2AE4KhCrqr6GRJjdC/gNfTdxkIXvuGZZda2VM=
     github.com/OneOfOne/xxhash v1.2.2/go.mod h1:HSdplMjZKSmBqAxg5vPj2TmRDmfkzw+cTzAElWljhcU=

Now apply the patch in the ebuild and regenerate the dependency tarball.

## [go tags]

Tags are how Go builds can be customized and can be thought of like restrictive autoconf/configure script `--with-x` or `--enable-x` arguments.

Tags are passed to Go builds via `GOFLAGS` in ebuilds as `-tags=x`, e.g.

[FILE] **`foo-1.2.3.ebuild`**

    src_configure()

Care is needed when handling `GOFLAGS` arguments because of word splitting and quirks in the parser:

-   [https://github.com/golang/go/issues/27368](https://github.com/golang/go/issues/27368)
-   [https://github.com/golang/go/issues/27282](https://github.com/golang/go/issues/27282)

## [Example]

This example is a continuation of the dnsx/zstd example above.

After upgrading the zstd module from v1.4.5 to v1.5.2, the maintainer notices some familiar filenames in the [build.log] like [zstd_compress.c] and recognizes those from [[[app-arch/zstd]](https://packages.gentoo.org/packages/app-arch/zstd)[]]. It seems that the module may be [bundling a copy](https://wiki.gentoo.org/wiki/Why_not_bundle_dependencies "Why not bundle dependencies") of zstd.

After visiting the GitHub project page, one can see that it supports using a [system copy](https://github.com/DataDog/zstd#building-against-an-external-libzstd) via *tags*: in this case, `external_libzstd`.

To set this in ebuild, `GOFLAGS` must be handled with care with **different** syntax than used in README on the project page:

[FILE] **`dnsx-1.1.1.ebuild`**

    DEPEND="app-arch/zstd[static-libs]"
    BDEPEND="
            >=dev-lang/go-1.17
            virtual/pkgconfig
    "

    PATCHES=(
            "$"/dnsx-1.1.1-upgrade-zstd-module.patch
    )

    src_configure()

## [See Also]

-   [Writing go Ebuilds](https://wiki.gentoo.org/wiki/Writing_go_Ebuilds "Writing go Ebuilds") --- a short reference, intended to be read alongside [Basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") and the [go-module.eclass documentation](https://devmanual.gentoo.org/eclass-reference/go-module.eclass/index.html)