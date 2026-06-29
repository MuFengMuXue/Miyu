**[] Deprecated article**\
\
This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

Usage of [repoman] [is deprecated](https://cgit.gentoo.org/proj/devmanual.git/commit/?id=c2c0b163b73c53d8aa65ed6403bdf8f116ef45b8). It is advised to use [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") instead.^[\[1\]](#cite_note-1)^

\
TLDR: **Do not use this article!**

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")][Project](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")

[[]][Package information](https://packages.gentoo.org/packages/app-portage/repoman)

[[]][GitWeb](https://gitweb.gentoo.org/proj/portage.git/log/?id=refs/heads/repoman)

**repoman** was a Python program used to enforce a minimal level of quality assurance in [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") and related metadata added to [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [\"Need user access\"]](#.22Need_user_access.22)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [Emerge]

Install [repoman] through [emerge]:

`root `[`#`]`emerge --ask --verbose app-portage/repoman`

## [Configuration]

For signing commits, enable the sign feature for portage and set the appropriate key ID:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="... sign ..."
    PORTAGE_GPG_KEY="<GnuPG fingerprint>"

Alternatively, set up [[git](https://wiki.gentoo.org/wiki/Git "Git")] to automatically sign your commits and set the `PORTAGE_GPG_DIR` environment variable to point at your [\~/.gnupg] (or similar) before running [repoman].

To automatically include `Signed-off-by: Name <email>` in the commit message, add:

[FILE] **`/etc/portage/make.conf`**

    SIGNED_OFF_BY="Name <email>"

This implies agreeing to the [Certificate of Origin](//www.gentoo.org/glep/glep-0076.html#certificate-of-origin).

## [Usage]

Using [repoman] is highly recommended for committing to Gentoo with [GitHub Pull Requests](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests "GitHub Pull Requests").

### [Invocation]

** Note**\
Messages pertaining to specific lines may be inaccurate in the presence of continuation lines from use of the `\` character in [bash](https://wiki.gentoo.org/wiki/Bash "Bash").

To create a package\'s [Manifest](https://wiki.gentoo.org/wiki/Repository_format/package/Manifest "Repository format/package/Manifest") file:

`user `[`$`]`repoman manifest`

    >>> Creating Manifest for /var/db/repos/local/app-misc/foo

** Note**\
Signed manifests are only created during [repoman commit].

To scan the directory tree for QA issues (full listing), include dev profiles in dependency checks and force the [metadata.xml] parse check to be carried out:

`user `[`$`]`repoman -dx full`

    RepoMan scours the neighborhood...
      dependency.badindev           16
       app-text/mupdf/mupdf-1.8.ebuild: DEPEND: ~arm(default/linux/uclibc/arm/armv7a)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.8.ebuild: RDEPEND: ~arm(default/linux/uclibc/arm/armv7a)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.8.ebuild: DEPEND: ~ppc(default/linux/uclibc/ppc)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.8.ebuild: RDEPEND: ~ppc(default/linux/uclibc/ppc)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.8.ebuild: DEPEND: ~arm(hardened/linux/uclibc/arm/armv7a)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.8.ebuild: RDEPEND: ~arm(hardened/linux/uclibc/arm/armv7a)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.8.ebuild: DEPEND: ~ppc(hardened/linux/uclibc/ppc)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.8.ebuild: RDEPEND: ~ppc(hardened/linux/uclibc/ppc)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.9a.ebuild: DEPEND: ~arm(default/linux/uclibc/arm/armv7a)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.9a.ebuild: RDEPEND: ~arm(default/linux/uclibc/arm/armv7a)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.9a.ebuild: DEPEND: ~ppc(default/linux/uclibc/ppc)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.9a.ebuild: RDEPEND: ~ppc(default/linux/uclibc/ppc)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.9a.ebuild: DEPEND: ~arm(hardened/linux/uclibc/arm/armv7a)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.9a.ebuild: RDEPEND: ~arm(hardened/linux/uclibc/arm/armv7a)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.9a.ebuild: DEPEND: ~ppc(hardened/linux/uclibc/ppc)
    ['>=media-libs/glfw-3']
       app-text/mupdf/mupdf-1.9a.ebuild: RDEPEND: ~ppc(hardened/linux/uclibc/ppc)
    ['>=media-libs/glfw-3']
    RepoMan sez: "You're only giving me a partial QA payment?
                  I'll take it this time, but I'm not happy."

To scan the directory tree for QA issues; if OK, commit via VCS, include dev profiles in dependency checks and force the [metadata.xml] parse check to be carried out:

`user `[`$`]`repoman -dx commit`

    * 0 files being committed...
    error: gpg failed to sign the data
    fatal: failed to write commit object
    !!! Exiting on git (shell) error code: 128

** Note**\
[repoman commit] only works inside local cvs, git, or subversion repositories.

When used in git, this command forces commit signature.

\
The key will have to be configured by [[git config user.signingkey key_id](https://help.github.com/articles/telling-git-about-your-gpg-key/)].

`user `[`$`]`repoman --help`

    usage: repoman [options] [mode]

    Modes: ci | commit | fix | full | help | manifest | manifest-check | scan

    optional arguments:
      -h, --help            show this help message and exit
      -a, --ask             Request a confirmation before commiting
      -m COMMITMSG, --commitmsg COMMITMSG
                            specify a commit message on the command line
      -M COMMITMSGFILE, --commitmsgfile COMMITMSGFILE
                            specify a path to a file that contains a commit
                            message
      --digest <y|n>        Automatically update Manifest digests for modified
                            files
      -p, --pretend         don't commit or fix anything; just show what would be
                            done
      -q, --quiet           do not print unnecessary messages
      --echangelog <y|n|force>
                            for commit mode, call echangelog if ChangeLog is
                            unmodified (or regardless of modification if 'force'
                            is specified)
      --experimental-inherit <y|n>
                            Enable experimental inherit.missing checks which may
                            misbehave when the internal eclass database becomes
                            outdated
      -f, --force           Commit with QA violations
      -S, --straight-to-stable
                            Allow committing straight to stable
      --vcs VCS             Force using specific VCS instead of autodetection
      -v, --verbose         be very verbose in output
      -V, --version         show version info
      -x, --xmlparse        forces the metadata.xml parse check to be carried out
      --if-modified <y|n>   only check packages that have uncommitted
                            modifications
      -i, --ignore-arches   ignore arch-specific failures (where arch != host)
      --ignore-default-opts
                            do not use the REPOMAN_DEFAULT_OPTS environment
                            variable
      -I, --ignore-masked   ignore masked packages (not allowed with commit mode)
      --include-arches ARCHES
                            A space separated list of arches used to filter the
                            selection of profiles for dependency checks
      -d, --include-dev     include dev profiles in dependency checks
      -e <y|n>, --include-exp-profiles <y|n>
                            include exp profiles in dependency checks
      --unmatched-removal   enable strict checking of package.mask and
                            package.unmask files for unmatched removal atoms
      --without-mask        behave as if no package.mask entries exist (not
                            allowed with commit mode)
      --output-style
                            select output type
      --mode
                            specify which mode repoman will run in (default=full)

    For more help consult the man page.

## [Troubleshooting]

### [][\"Need user access\"]

If [repoman] fails with the following obscure error message, you might have to adjust your filesystem permissions or make your user part of the `portage` group. See [[[bug #574130]](https://bugs.gentoo.org/show_bug.cgi?id=574130)[]] for details.

`user $``repoman -dx full`

    RepoMan scours the neighborhood...
    *** the local copy of metadata.xsd needs to be refetched, doing that now
    Repoman: Need user access

## [See also]

-   [Equery](https://wiki.gentoo.org/wiki/Equery "Equery") --- a tool to make several common [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") operations simpler.
-   [Pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.
-   [Portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq") --- a tool to quickly query Portage information.

## [External resources]

-   [\[gentoo-dev\] \[RFC\] Allowing pkgcheck as a replacement for repoman](https://archives.gentoo.org/gentoo-dev/message/6b236365a2876fc2b96a60445d146e23)
-   [A better ebuild workflow with pure git and pkgcheck](https://blogs.gentoo.org/mgorny/2019/12/12/a-better-ebuild-workflow-with-pure-git-and-pkgcheck/)
-   [\[gentoo-dev\] Deprecating repoman](https://archives.gentoo.org/gentoo-dev/message/93df9e7a2ad9d8d33e0cc83b50556d51)

## [References]

1.  [[[↑](#cite_ref-1)] [[Git for Gentoo Developers -- Gentoo Development Guide](https://devmanual.gentoo.org/ebuild-maintenance/git/#committing-to-gentoo.git), gentoo.org. Retrieved on April 20, 2022]]