# VCS package guidelines

Version control systems can be used for retrieval of source code for usual statically versioned packages, and the latest (trunk) version of a development branch.

## Package naming
Suffix  with , , , , , , etc., unless the package fetches a specific release.

## Versioning
If the resulting package is different after changing e.g. the dependencies, URL or sources — update  to the latest version. If  has not changed since the last update to the , increase  instead.

It is recommended to have following version format: , where  is a monotonically increasing number that uniquely identifies the source tree (VCS revisions do this). If there are no public releases and no repository tags then zero could be used as a release number or you can drop  completely and use version number that looks like . If there are public releases but repository has no tags then the developer should get the release version somehow e.g. by parsing the project files.

The revision number delimiter —  right before  — is important. This delimiter allows to avoid problems in case if upstream decides to make its first release or uses versions with different number of components. E.g. if at revision  upstream decides to release version , then the revision delimiter preserves version monotonicity: . Without the delimiter monotonicity fails:

The VCS sources should be specified in the  array and will be treated like any other source. makepkg will clone/checkout/branch the repository into  — same as  if not set in , and copy it to  (in a specific way to each VCS). The local repository is left untouched, thus invalidating the need for a  directory.

The general format of a  array is:

 source=('*  (optional) — is used to change the default repository name to something more relevant, e.g. than , or to preserve the previous sources.
*  is needed for URLs that do not reflect the VCS type, e.g. .
*  is the URL to the distant or local repository.
*  (optional) — is needed to pull a specific branch or commit. See  for a list of supported VCS and the respective fragments available.

An example Git source array:

 source=('project_name::git+https://project_url#branch=project_branch')

## The pkgver() function
The  autobump is now achieved via a dedicated  function. This allows for better control over the , and maintainers should favor a  that makes sense. To use , you still need to declare the  variable with the most recent value. makepkg will invoke function , and update variable  accordingly.

## Bazaar
{{hc|
pkgver() {
  cd "$pkgname"
  printf "r%s" "$(bzr revno)"
}|
r830
}}

## Git
Using the most recent annotated tag reachable from the current commit:

{{hc|
pkgver() {
  cd "$pkgname"
  git describe --long --abbrev=7 | sed 's/\([^-*-g\)/r\1/;s/-/./g'
}|
2.0.r6.ga17a017
}}

Using the most recent tag (annotated or non-annotated) reachable from the current commit:

{{hc|
pkgver() {
  cd "$pkgname"
  git describe --long --tags --abbrev=7 | sed 's/\(}|
0.71.r115.gd95ee07
}}

If the  does not contain dashes, then one can use simpler  expression .

If tag contains a prefix, like  or project name, then it should be cut off:

{{hc|
pkgver() {
  cd "$pkgname"
  # cutting off 'foo-' prefix that presents in the git tag
  git describe --long --abbrev=7 | sed 's/^foo-//;s/\([^-*-g\)/r\1/;s/-/./g'
}|
6.1.r3.gd77e105
}}

If there are no tags then use number of revisions since beginning of the history:

{{hc|
pkgver() {
  cd "$pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}|
r1142.a17a017
}}

Version and only commit/revision number (SHA-1 omitted; however, without a SHA-1 quick referencing of an exact revision is lost if not mindful of versioning):

 git describe --long --abbrev=7 --tags | sed 's/\(Both methods can also be combined, to support repositories that start without a tag but get tagged later on (uses a bashism):

{{hc|
pkgver() {
  cd "$pkgname"
  ( set -o pipefail
    git describe --long --abbrev=7 2>/dev/null | sed 's/\([^-*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
  )
}|
0.9.9.r27.g2b039da  # if tags exist
r1581.2b039da       # else fallback
}}

## Mercurial
{{hc|
pkgver() {
  cd "$pkgname"
  printf "r%s.%s" "$(hg identify -n)" "$(hg identify -i)"
}|
r2813.75881cc5391e
}}

## Subversion
{{hc|
pkgver() {
  cd "$pkgname"
  local ver="$(svnversion)"
  printf "r%s" "${ver//:alpha:}"
}|
r8546
}}

## Fallback
In case no satisfactory  can be extracted from the repository, the current  can be used:

{{hc|
pkgver() {
  date +%Y%m%d
}|
20130408
}}

## Tips and tricks
## Git submodules
Git submodules are a little tricky to do. The idea is to add the URLs of the submodules themselves directly to the sources array and then reference them during .

Downstream project developers may not name their submodule as the same name as the upstream module's repository. To view the name of the Git submodules, go to the  file in the project's repository and preview it. For example, a repository named  by the upstream developers may be registered as a submodule named  in  downstream.

{{bc|
source=("git+https://example.org/main-project/main-project.git"
        "git+https://example.org/lib-dependency/lib-dependency.git")

prepare() {
  cd main-project
  git submodule init
  git config submodule.libs/libdep.url "$srcdir/lib-dependency"
  git -c protocol.file.allow=always submodule update
}
}}

For recursive submodules, first update the top-level's submodules as above, then do so recursively to the submodules themselves where applicable. In the above example, let's say  had a submodule itself named  as shown below.

After updating the top-level project's submodules as in the prior example, change directories to the submodule's path specified in , then perform the same steps again to update its own submodules.

{{bc|
source=("git+https://example.org/main-project/main-project.git"
        "git+https://example.org/lib-dependency/lib-dependency.git"
        "git+https://example.org/lib-dependency/lib-double-dependency.git")

prepare() {
  cd main-project
  git submodule init
  git config submodule.libs/libdep.url "$srcdir/lib-dependency"
  git -c protocol.file.allow=always submodule update

  cd libs/libdep  # The path specified in main-project's .gitmodules
  git submodule init
  git config submodule.deps/double-dep.url "$srcdir/lib-double-dependency"
  git -c protocol.file.allow=always submodule update
}
}}

## Git LFS
Git LFS needs a bit of extra setup:

{{bc|
prepare() {
  git lfs install --local
  git remote add network-origin https://example.org/upstream/lfs/repo
  git lfs pull network-origin
}
}}

This also works when the LFS is used in submodules:
{{bc|
prepare() {
  git submodule init
  git config submodule.libs/libdep.url "$srcdir/lib-dependency"
  git -c protocol.file.allow=always submodule update

  git -C libs/libdep lfs install --local
  git -C libs/libdep remote add network-origin https://example.org/upstream/lfs/repo
  git -C libs/libdep lfs pull network-origin
}
}}

## Git checksums
When referencing stable git tags or specific commits as a source via , it is possible to specify their checksum in the . To do so, simply use  or  to generate them as you would for any other non-git source.
