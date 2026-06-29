# AUR helpers

AUR helpers automate usage of the Arch User Repository. In particular, they may automate the following tasks:

* searching for packages published on the AUR,
* resolving of dependencies between AUR packages,
* retrieve and build AUR packages,
* retrieve web content, such as user comments,
* submission of AUR packages.

Pacman only handles updates for pre-built packages in its repositories. AUR packages are redistributed in form of PKGBUILDs and need an AUR helper to automate the rebuild process. However, keep in mind that a rebuild of a package may be required when its shared library dependencies are updated, not only when the package itself is updated.

## Legend
The #Comparison tables columns have the following meaning:

;File review: Does not source the PKGBUILD file at all by default; or alerts the user and offers the opportunity to inspect the  file manually before it is sourced. Some helpers are known to source s before the user can inspect them, allowing malicious code to be executed.
;Diff view: Ability to view package differences on inspection. Besides the  file, this includes changes to files such as  or  files.
;Git clone: Uses  by default to retrieve build files from the AUR.
;Reliable parser: Ability to handle complex packages by using the provided metadata (RPC/) instead of the  file parsing, such as .
;Reliable solver: Ability to correctly solve and build complex dependency chains, such as .
;Split packages: Ability to correctly build and install:
:* Multiple packages from the same package base, without rebuilding or reinstalling multiple times, such as .
:* Split packages which depend on a package from the same package base, such as .
:* Split packages independently, such as  and .
;Shell completion: Tab completion is available for the listed shells.

## Comparison tables
## Search and download
{| class="wikitable sortable" style="text-align: center;"
! Name !! Written in !! File review !! Diff view !! Git clone !! Reliable parser !! Reliable solver !! Shell completion !! Specificity
|-
!
| C++ ||  ||  ||  ||  ||  || bash ||
|-
!
| Go ||  ||  ||  ||  ||  || bash, zsh, fish ||
|}

## Search and build
{| class="wikitable sortable" style="text-align: center;"
! Name !! Written in !! File review !! Diff view !! Git clone !! Reliable parser !! Reliable solver !! Split packages !! Shell completion !! Specificity
|-
!
| Bash ||  ||  ||  ||  ||  ||  || bash, zsh ||
|-
!
| Elvish ||  ||  ||  ||  ||  ||  || bash, zsh, elvish ||
|}

## Pacman wrappers
{| class="wikitable sortable" style="text-align: center;"
! Name !! Written in !! File review !! Diff view !! Git clone !! Reliable parser !! Reliable solver !! Split packages !! Unsafe flags !! Shell completion !! Specificity
|-
!
| Rust ||  ||  ||  ||  ||  ||  ||  || bash, fish, zsh ||
|-
!
| Nim ||  ||  ||  ||  ||  ||  ||  || bash, zsh ||
|-
!
| Rust||  ||  ||  ||  ||  ||  ||  || bash, fish, zsh ||
|-
!
| Python ||  ||  ||  ||  ||  ||  ||  || bash, fish, zsh ||
|-
!
| Perl ||  ||  || ||   ||  ||  ||  || bash, fish, zsh ||
|-
!
| Go ||  ||  ||  ||  ||  ||  ||  || bash, fish, zsh ||
|}

## Graphical
*
*
*
*
*
*
*
*
*
*
*
*

## Maintenance
*
*
*
*
*

## Other
*
*
*
*
*
*
