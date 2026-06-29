[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-VCS+PKGBUILD+Guidelines&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=VCS_PKGBUILD_Guidelines "VCS PKGBUILD Guidelines (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=VCS_PKGBUILD_Guidelines/tr "VCS PKGBUILD Yönergeleri (14% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=VCS_PKGBUILD_Guidelines/ru "Руководство PKGBUILD VCS (100% translated)")

## Contents

-   [[1] [Guidelines]](#Guidelines)
    -   [[1.1] [VCS sources]](#VCS_sources)
    -   [[1.2] [The pkgver() function]](#The_pkgver.28.29_function)
        -   [[1.2.1] [Git]](#Git)
        -   [[1.2.2] [Subversion]](#Subversion)
        -   [[1.2.3] [Mercurial]](#Mercurial)
        -   [[1.2.4] [Bazaar]](#Bazaar)
        -   [[1.2.5] [Fallback]](#Fallback)
-   [[2] [Tips]](#Tips)
    -   [[2.1] [A sample Git PKGBUILD]](#A_sample_Git_PKGBUILD)
    -   [[2.2] [Git Submodules]](#Git_Submodules)

[Version control systems](https://en.wikipedia.org/wiki/Revision_control "wikipedia:Revision control") can be used for retrieval of source code for both usual statically versioned packages and latest (trunk) version of a development branch. This article covers both cases.

## [Guidelines]

-   Suffix `pkgname` with `-cvs`, `-svn`, `-hg`, `-darcs`, `-bzr`, `-git` etc. unless the package fetches a specific release.

<!-- -->

-   If the resulting package is different after changing the dependencies, URL, sources, etc. increasing the `pkgrel` is mandatory. Touching the `pkgver` is not.

<!-- -->

-   `--holdver` can be used to prevent [makepkg](//wiki.manjaro.org/index.php?title=Makepkg "Makepkg") from updating the `pkgver` (see: [makepkg(8)](https://www.archlinux.org/pacman/makepkg.8.html))

<!-- -->

-   Include what the package conflicts with and provides (e.g. for [fluxbox-git](https://aur.archlinux.org/packages/fluxbox-git/): `conflicts=('fluxbox')` and `provides=('fluxbox')`).

<!-- -->

-   `replaces=()` generally causes unnecessary problems and should be avoided.

<!-- -->

-   When using the cvsroot, use `anonymous:@` rather than `anonymous@` to avoid having to enter a blank password or `anonymous:password@`, if one is required.

<!-- -->

-   Include the appropriate VCS tool in `makedepends=()` (`cvs`, `subversion`, `git`, \...).

### [VCS sources]

**Note**

------------------------------------------------------------------------

Pacman 4.1 supports the following VCS sources: `bzr`, `git`, `hg` and `svn`. See the `fragment` section of `man PKGBUILD` or [PKGBUILD(5)](https://www.archlinux.org/pacman/PKGBUILD.5.html) for a list of supported VCS.

Starting with `pacman` 4.1, the VCS sources should be specified in the `source=()` array and will be treated like any other source. `makepkg` will clone/checkout/branch the repo into `$SRCDEST` (same as `$startdir` if not set in [makepkg.conf(5)](https://www.archlinux.org/pacman/makepkg.conf.5.html)) and copy it to `$srcdir` (in a specific way to each VCS). The local repo is left untouched, thus invalidating the need for a `-build` directory.

The general format of a VCS `source=()` array is:

    source=('[folder::][vcs+]url[#fragment]')

-   `folder` (optional) is used to change the default repo name to something more relevant (e.g. than `trunk`) or to preserve the previous sources
-   `vcs+` is needed for URLs that do not reflect the VCS type, e.g. `git+`[`http://some_repo`](http://some_repo).
-   `url` is the URL to the distant or local repo
-   `#fragment` (optional) is needed to pull a specific branch or commit. See `man PKGBUILD` for more information on the fragments available for each VCS.

An example Git source array:

    source=('project_name::git+http://project_url#branch=project_branch')

### [][The pkgver() function]

The `pkgver` autobump is now achieved via a dedicated `pkgver()` function. This allows for better control over the `pkgver`, and maintainers should favor a `pkgver` that makes sense.

It is recommended to have following version format: *RELEASE.rREVISION* where *REVISION* is a monotonically increasing number that uniquely identifies the source tree (VCS revisions do this). The last VCS tag can be used for *RELEASE*. If there are no public releases and no repository tags then zero could be used as a release number or you can drop *RELEASE* completely and use version number that looks like *rREVISION*. If there are public releases but repo has no tags then developer should get the release version somehow e.g. by parsing the project files.

Following are some examples showing the *intended* output:

#### [Git]

Using the annotated tag of the last commit:

```
pkgver()
```

```
2.0.r6.ga17a017
```

Using the unannotated tag of the last commit:

```
pkgver()
```

```
0.71.r115.gd95ee07
```

If there are no tags then use number of revisions since beginning of the history:

```
pkgver()
```

```
r1142.a17a017
```

\

**Note**

------------------------------------------------------------------------

SHA1 (in this case `a17a017`) is not used in the version comparison and can be omitted, although it allows quick identification of the exact revision used and might be useful during debugging.

#### [Subversion]

```
pkgver() "
}
```

```
r8546
```

\

**Note**

------------------------------------------------------------------------

If the project has releases you should use them instead of the `0.`.

#### [Mercurial]

```
pkgver()
```

```
r2813.75881cc5391e
```

#### [Bazaar]

```
pkgver()
```

```
r830
```

#### [Fallback]

The current date can be used, in case no satisfactory `pkgver` can be extracted from the repository:

```
pkgver()
```

```
20130408
```

Although it does not identify source tree state uniquely, so avoid it if possible.

## [Tips]

### [A sample Git PKGBUILD]

    # Maintainer: Dave Reisner <d@falconindy.com>
    # Contributor: William Giokas (KaiSforza) <1007380@gmail.com>

    pkgname=expac-git
    pkgver=0.0.0
    pkgrel=1
    pkgdesc="Pacman database extraction utility"
    arch=('i686' 'x86_64')
    url="https://github.com/falconindy/expac"
    license=('MIT')
    depends=('pacman')
    makedepends=('git')
    conflicts=('expac')
    provides=('expac')
    # The git repo is detected by the 'git:' or 'git+' beginning. The branch
    # '$pkgname' is then checked out upon cloning, expediating versioning:
    #source=('git+https://github.com/falconindy/expac.git'
    source=("$pkgname"::'git://github.com/falconindy/expac.git'
            'expac_icon.png')
    # Because the sources are not static, skip Git checksum:
    md5sums=('SKIP'
             '020c36e38466b68cbc7b3f93e2044b49')

    pkgver()

    build()

    package()

### [Git Submodules]

Git submodules are a little tricky to do. The idea is to add the URLs of the submodules themselves directly to the sources array and then reference them during prepare(). This could look like this:

    source=("git://somewhere.org/something/something.git"
            "git://somewhere.org/mysubmodule/mysubmodule.git")

    prepare()