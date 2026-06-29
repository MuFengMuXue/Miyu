\
This page aims to answer the question *\"How can I dispel doubts regarding the security of the Gentoo ebuild repository on a system?\"* That is, to cryptographically ensure each file under [[/var/db/repos/gentoo]](https://wiki.gentoo.org/wiki//var/db/repos/gentoo "/var/db/repos/gentoo") is entirely composed of code written by or reviewed by Gentoo developers.

This question is answered differently depending on the sync method in use (webrsync, rsync, git-mirror, or canonical git repositories) for the system in question.

## Contents

-   [[1] [webrsync]](#webrsync)
    -   [[1.1] [Configuration]](#Configuration)
    -   [[1.2] [Dispelling doubt]](#Dispelling_doubt)
    -   [[1.3] [Required trust]](#Required_trust)
-   [[2] [rsync]](#rsync)
    -   [[2.1] [Configuration]](#Configuration_2)
    -   [[2.2] [Dispelling doubt]](#Dispelling_doubt_2)
    -   [[2.3] [Required trust]](#Required_trust_2)
-   [[3] [git-mirror repositories]](#git-mirror_repositories)
    -   [[3.1] [Configuration]](#Configuration_3)
    -   [[3.2] [Dispelling doubt]](#Dispelling_doubt_3)
    -   [[3.3] [Required trust]](#Required_trust_3)
-   [[4] [canonical git repositories]](#canonical_git_repositories)
    -   [[4.1] [Configuration]](#Configuration_4)
    -   [[4.2] [Dispelling doubt]](#Dispelling_doubt_4)
    -   [[4.3] [Required trust]](#Required_trust_4)
-   [[5] [See also]](#See_also)

## [webrsync]

Whenever [emerge \--sync] is run, the [repos.conf] `sync-type` is set to `webrsync`, and the `sync-webrsync-verify-signature` option is enabled, the downloaded tarball is always checked against Gentoo release keys provided by the [[[sec-keys/openpgp-keys-gentoo-release]](https://packages.gentoo.org/packages/sec-keys/openpgp-keys-gentoo-release)[]] package.

The only caveat is: this method does not perform further checking after the tarball has been unpacked. Therefore, if the Gentoo ebuild repository was compromised *before* the webrsync, it is possible that it still could be compromised. If the state of the Gentoo repository is in question, wipe it out *before* running [emerge \--sync]:

`root `[`#`]`gentoo_repo=$(portageq get_repo_path / gentoo) && mv $ $.bak && emerge --sync `

If everything succeeded, the backup at [\$.bak] can be deleted.

### [Configuration]

1.  Ensure that Portage has the [rsync-verify] USE flag enabled.
2.  In [repos.conf], set `sync-type` to `webrsync` and enable the `sync-webrsync-verify-signature` option
3.  Make sure that [emerge \--sync] emits \"Using keys from \...\" and \"Valid OpenPGP signature found\"

### [Dispelling doubt]

Seeing \"Checking signature\...\" should be enough to dispel doubts. Also, reading the contents of [/usr/bin/emerge-webrsync] which is small enough to be easily audited.

Hardcore users can arrange a man-in-the-middle attack and check that verification fails.

### [Required trust]

1.  That Gentoo\'s release keys have not been compromised.
2.  That the content in the file that `SRC_URI` points to in [[[sec-keys/openpgp-keys-gentoo-release]](https://packages.gentoo.org/packages/sec-keys/openpgp-keys-gentoo-release)[]] is actually the Gentoo release keys.
3.  Everything that is needed to trust in the [canonical git repositories](https://wiki.gentoo.org/wiki/Portage_Security#canonical_git_repositories "Portage Security") method.

## [rsync]

Portage 2.3.21+ supports recursive signed manifests checking. [Project:Portage/Repository Verification](https://wiki.gentoo.org/wiki/Project:Portage/Repository_Verification "Project:Portage/Repository Verification") explains how it works.

### [Configuration]

1.  Ensure that Portage has the [rsync-verify] USE flag enabled.
2.  Make sure that [emerge \--sync] emits \"Using keys from \...\" and \"Valid OpenPGP signature found\".
3.  **Never miss errors during `--sync`**

### [Dispelling doubt]

Simulate malicious injection:

1.  Change an ebuild.
2.  Run [gemato verify -K /usr/share/openpgp-keys/gentoo-release.asc /var/db/repos/gentoo]
3.  A manifest mismatch error should result.
4.  Go a step further and update the manifest with [ebuild foobar-1.2.3.ebuild manifest]
5.  Run [gemato verify -K /usr/share/openpgp-keys/gentoo-release.asc /var/db/repos/gentoo]
6.  A mismatch error will occur.

### [Required trust]

Same thing as with [webrsync](https://wiki.gentoo.org/wiki/Portage_Security#webrsync "Portage Security"). With repository verification, the integrity of rsync mirrors are no longer an issue. So, it is not less secure than webrsync.

## [git-mirror repositories]

The [gentoo git mirror](https://gitweb.gentoo.org/repo/sync/gentoo.git/) is a git repo that delivers the equivalent of the rsync method, that is, the content of the canonical git repository but with DTD, [GLSA](https://wiki.gentoo.org/wiki/GLSA "GLSA"), news items, and XML schema information attached and an up to date Portage cache generated.

Every commit is signed by either the developer or the \"repomirrorci@gentoo.org\" PGP key. So, integrity is ensured through the recent `sync-git-verify-commit-signature` repository option.

### [Configuration]

1.  Install [[[sec-keys/openpgp-keys-gentoo-release]](https://packages.gentoo.org/packages/sec-keys/openpgp-keys-gentoo-release)[]].
2.  Add the \'sync\' repo to the system\'s [[repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")] file (either \<[https://anongit.gentoo.org/git/repo/sync/gentoo.git](https://anongit.gentoo.org/git/repo/sync/gentoo.git) or [https://github.com/gentoo-mirror/gentoo](https://github.com/gentoo-mirror/gentoo))
3.  In [repos.conf], set `sync-type` to git and enable the `sync-git-verify-commit-signature` option.

### [Dispelling doubt]

1.  Make a local clone of the mirror.
2.  Set the `sync-uri` value to the local clone.
3.  Add a commit on top of the local clone.
4.  [emerge \--sync] should complain.

### [Required trust]

1.  The integrity of the \"repomirrorci@gentoo.org\" PGP key.
2.  The CI server isn\'t compromised (which would compromise the key).
3.  Everything that is needed to trust in the [canonical git repositories](https://wiki.gentoo.org/wiki/Portage_Security#canonical_git_repositories "Portage Security") method.

## [canonical git repositories]

All methods above take their content from the same source: [The canonical Gentoo ebuild repository](https://gitweb.gentoo.org/repo/gentoo.git/). Every commit in this repository is required to be signed by developers using PGP keys listed in Gentoo\'s LDAP. Those keys are listed in the [Current Gentoo developers](https://www.gentoo.org/inside-gentoo/developers/) page.

Why isn\'t this method preferred? Because this repo doesn\'t contain everything it needs to be fully functional. It needs to be augmented with [data repos](https://gitweb.gentoo.org/data) and a Portage cache needs to be regenerated at each update (which can take a little while).

Despite this method being more hassle, it has the advantage of having a different trust model: trusting release keys and infra is no longer required for Gentoo ebuild repository syncs. Directly trusting developers and the strength of their PGP web of trust.

### [Configuration]

Follow instructions from [Gentoo ebuild tree from scratch](https://wiki.gentoo.org/wiki/Gentoo_ebuild_tree_from_scratch "Gentoo ebuild tree from scratch").

### [Dispelling doubt]

Because this method requires self-configuration of the verification processes, there shouldn\'t be much doubt left once complete.

### [Required trust]

1.  That the web of trust of Gentoo developers is strong.
2.  That Gentoo developers have good practices regarding the security of their private PGP key.

The great thing about this trust model is that it doesn\'t rely on infrastructure integrity. Sure, a developer\'s key can be compromised but it\'s something that can easily be spotted (especially by the compromised developer. \"hey! that commit isn\'t mine!\") and integrity and trust is easy to bring back (review all recent commits by this developer and remove malicious ones). There is no single point of failure.

## [See also]

-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.
-   [Project:Portage/Repository_verification](https://wiki.gentoo.org/wiki/Project:Portage/Repository_verification "Project:Portage/Repository verification") --- describes different methods used to ensure authenticity of the Gentoo ebuild repository.