# Reproducible builds/Status

Arch Linux is constantly rebuilding core and extra packages and has a status page. This page contains a status of bad packages and what needs to be fixed.

## Issues
## General
* A rebuild is required for all packages build with pacman  pkg-order
    sort pkg-order > sort-order
    if ! diff pkg-order sort-order &>/dev/null; then
      echo $i;
    fi
    rm pkg-order sort-order
 done

## File order rebuild FTBFS
 accounts-qml-module-0.7-2-x86_64.pkg.tar.xz
 archboot-2019.03-1-any.pkg.tar.xz
 cmark-0.29.0-1-x86_64.pkg.tar.xz
 gtk-sharp-2-2.12.45-2-x86_64.pkg.tar.xz
 guile1.8-1.8.8-7-x86_64.pkg.tar.xz
 java11-openjfx-11.0.3.u1-1-x86_64.pkg.tar.xz
 java11-openjfx-doc-11.0.3.u1-1-x86_64.pkg.tar.xz
 java11-openjfx-src-11.0.3.u1-1-x86_64.pkg.tar.xz
 java8-openjfx-8.u202-3-x86_64.pkg.tar.xz
 java8-openjfx-doc-8.u202-3-x86_64.pkg.tar.xz
 java8-openjfx-src-8.u202-3-x86_64.pkg.tar.xz
 java-openjfx-13.u14-1-x86_64.pkg.tar.xz
 java-openjfx-doc-13.u14-1-x86_64.pkg.tar.xz
 java-openjfx-src-13.u14-1-x86_64.pkg.tar.xz
 jdk10-openjdk-10.0.2.u13-2-x86_64.pkg.tar.xz
 jre10-openjdk-10.0.2.u13-2-x86_64.pkg.tar.xz
 jre10-openjdk-headless-10.0.2.u13-2-x86_64.pkg.tar.xz
 jsonrpc-glib-3.34.0-1-x86_64.pkg.tar.xz
 libva-vdpau-driver-0.7.4-4-x86_64.pkg.tar.xz
 liferea-1.12.7-1-x86_64.pkg.tar.xz
 linux-atm-2.5.2-6-x86_64.pkg.tar.xz
 mono-tools-4.2-2-x86_64.pkg.tar.xz
 npapi-sdk-0.27.2-2-any.pkg.tar.xz
 nss_ldap-265-7-x86_64.pkg.tar.xz
 openjdk10-doc-10.0.2.u13-2-x86_64.pkg.tar.xz
 openjdk10-src-10.0.2.u13-2-x86_64.pkg.tar.xz
 pam_ldap-186-6-x86_64.pkg.tar.xz
 portaudio-1:19.6.0-6-x86_64.pkg.tar.xz
 qtav-1.13.0-1-x86_64.pkg.tar.xz

## Packages with JAR files
JARs include a modification timestamp for each file, making them unreproducible. Depending on the build system, there are different solutions available for this.

## Ant
Currently has no support for reproducible builds, see the upstream feature request.

## Gradle
Should support reproducible builds out of the box.

## Maven
Supports the  property that can be set to a fixed timestamp. Recent versions of Maven plugins respect this property to create reproducible artefacts. The property should be set in the project's  file, if upstream does not already do this, you can define it at compile time using a command like  It might be necessary to patch the project's  to update plugins to a more recent version with support for reproducible builds, see the Maven guide to reproducible builds for the minimum required versions and more information like additional necessary configuration options.

Example package (including a patch for a Maven plugin version update): junit-system-rules.

## OpenJDK jar command
The builtin OpenJDK  program will support  starting with OpenJDK version 15.

## strip-nondeterminism
As a last resort, strip-nondeterminism from Debian is able to strip unreproducible metadata like file timestamps from a variety of file types, including JARs. It is not a cure-all (e.g. build systems might include additional unreproducible metadata in the JAR manifest, strip-nondeterminism removes some, but not all of these) and should only be used as a last resort if no native support for reproducible builds is available:

## KDE Kdeveloper project files
KDE creates Package App template .tar.bz2 files which tar files and userid is different when reproducing with repro which might be a bug in repro. https://gist.githubusercontent.com/jelly/570313f56ee59be7674ad4cc002232e7/raw/b85536690c48b23ce97650e8db8f0ca18c2dbf1a/gistfile1.txt

The cmake file which generates the issue.

## Doxygen documentation build with graphviz-2.44.0-2
graphviz lacked a dependency on libpng, making PNG generation unavailable in dot as graphviz was installed before libpng was available and therefore not marking it as to be dlopen'd. All packages which depend on doxygen for generation documentation and with the following diff require a rebuild.

 │ │ --rw-r--r--   0 root         (0) root         (0)    20234 2020-05-16 12:32:36.000000 usr/share/doc/grantlee/classGrantlee_1_1Parser.html
 │ │ --rw-r--r--   0 root         (0) root         (0)      265 2020-05-16 12:32:36.000000 usr/share/doc/grantlee/classGrantlee_1_1Parser__inherit__graph.map
 │ │ --rw-r--r--   0 root         (0) root         (0)       32 2020-05-16 12:32:36.000000 usr/share/doc/grantlee/classGrantlee_1_1Parser__inherit__graph.md5
 │ │ --rw-r--r--   0 root         (0) root         (0)     3136 2020-05-16 12:32:36.000000 usr/share/doc/grantlee/classGrantlee_1_1Parser__inherit__graph.png
 │ │ +-rw-r--r--   0 root         (0) root         (0)    19961 2020-05-16 12:32:36.000000 usr/share/doc/grantlee/classGrantlee_1_1Parser.html
 │ │ +-rw-r--r--   0 root         (0) root         (0)      598 2020-05-16 12:32:36.000000 usr/share/doc/grantlee/classGrantlee_1_1Parser__inherit__graph.dot

##
{| class="wikitable sortable"
! Package
! Issue
! Solution/Patch
! Assignee
! Solved
|-
|  || Signed modules || none || none ||
|-
|  || lots of issues - ordering, linking, ... || none || none ||
|-
|  ||  [https://gist.github.com/allanmcrae/31604043163f6379139c767e7d9efefd diff || none || none ||
|-
|  || as for  || none || none ||
|-
|  || as for  || none || none ||
|-
|  || as for  || none || none ||
|}

##
{| class="wikitable sortable"
! Package
! Issue
! Solution/Patch
! Assignee
! Solved
|-
|  || .jar file differences || none || none ||
|-
|  || lots of timestamps (javadoc), and .zip file difference || none || none ||
|-
|  || Dates in html and info. PDF document differences (dates?) || none || none ||
|-
|  || Timestamp in man pages,  with different file ownership, and a small binary change in  || need export MAN_PAGE_DATE=... and configure --enable-timeout=70 || none ||
|-
|  || uname and timestamps all over the place || none || none ||
|-
|  || 3.0.2.3-3 reproducible with both repro and makechrootpkg || tooling issue? || none ||
|-
|  || ip address; timestamps in ps docs, likely much more || none || none ||
|-
|  || .pyc file, .egg files || none || none ||
|-
|  || lots of pdfs with differences || none || none ||
|-
|  || uname, timestamp, gzip, lots of other binary differences || none || none ||
|-
|  || .jar file || none || none ||
|-
|  ||  has binary differences || none || none ||
|-
|  || lots of binary differences || none || none ||
|-
|  || binary differences in  || none || none ||
|-
|  || It is firefox; [https://github.com/bmwiedemann/theunreproduciblepackage/tree/master/pgo PGO? || none || none ||
|-
|  || file attribute(?) differences in {{ic|usr/share/java/{libbluray{,-awt}-j2se-1.2.0.jar}} || none || none ||
|-
|  || uname in  || none || none ||
|-
|  || timestamp in  &  || none || none ||
|-
|  || timestamp in yaml files,  has lots of timestamp differences, repro causes poll() detection issue not found in makerepropkg || patch || none ||
|-
|  || Lots of timestamps in files, gzip timestamps, randomly(?) generated paths in , binary differences... || none || none ||
|-
|  || Timestamp in  || none || none ||
|}

##
{| class="wikitable sortable"
! Package
! Issue
! Solution/Patch
! Assignee
! Solved
|-
|  || Binary includes build date || [https://gitlab.archlinux.org/archlinux/packaging/packages/lib32-keyutils/-/issues/1 proposed || none ||
|}
