The [gentoo repo](https://gitweb.gentoo.org/repo/gentoo.git) is the main element that is used to build the Gentoo ebuild repository that is delivered through rsync, but this repo doesn\'t contain everything it needs to be fully functional. It needs to be augmented with [data repos](https://gitweb.gentoo.org/data) and a Portage cache needs to be regenerated after each update.

This page describes how to assemble and verify the Gentoo ebuild repository from first-hand data.

## Contents

-   [[1] [Rationale]](#Rationale)
-   [[2] [Step 1: Trust Gentoo developers]](#Step_1:_Trust_Gentoo_developers)
    -   [[2.1] [Manual verification of Web Of Trust]](#Manual_verification_of_Web_Of_Trust)
-   [[3] [Step 2: Clone and verify]](#Step_2:_Clone_and_verify)
-   [[4] [Step 3: Augment with metadata]](#Step_3:_Augment_with_metadata)
-   [[5] [Step 4: repos.conf]](#Step_4:_repos.conf)
-   [[6] [Step 5: Generate Portage cache]](#Step_5:_Generate_Portage_cache)

## [Rationale]

Why would you want to do this? It\'s true that building an maintaining a Gentoo ebuild tree from scratch is a bit more of a hassle than using a pre-assembled one. You have to maintain your PGP trust whenever there\'s changes in the Gentoo developers PGP keys pool, it\'s a bit of work.

The most likely reason for doing this is to participate in strengthening Gentoo\'s web of trust. By making you trusting developers directly, you make Gentoo ebuild repo security less dependent on a single point of failure that is its infrastructure.

If you\'re a Gentoo developer, you might think it convenient to edit your active ebuild repository directly.

## [Step 1: Trust Gentoo developers]

Every commit of the Gentoo repo is signed by the Gentoo developer who wrote or reviewed it.

To be able to trust Gentoo developers using the web of trust, you first need to import all developer keys into your local keystore. This can be done via [[[sec-keys/openpgp-keys-gentoo-developers]](https://packages.gentoo.org/packages/sec-keys/openpgp-keys-gentoo-developers)[]].

### [Manual verification of Web Of Trust]

Optionally, the PGP keychain can be checked manually.

The tricky part: trusting those keys. How you manage PGP trust is very subjective, but ultimately, you *have* to trust all Gentoo developers to use the ebuild tree, but that doesn\'t mean that you have to blindly sign all those keys. For example, you could:

1.  Sign the keys of a couple of high-profile developers after having carefully reviewed their signed published messages (with enough of them, you can arrive to the conclusion that it\'s highly unlikely that this public key doesn\'t belong to them).
2.  Hope to cover most of the developers through transitive trust.
3.  Set your verification scripts to not error out on untrusted keys, but to generate visible warnings. You could then manually review commits of the few developers that aren\'t in your trust zone.

But that\'s only one possibility among others.

## [Step 2: Clone and verify]

The next thing to do is to clone [https://gitweb.gentoo.org/repo/gentoo.git](https://gitweb.gentoo.org/repo/gentoo.git) somewhere and verify its latest couple of hundred commits, or as many commit as you need to feel confident in your initial integrity.

Why not the whole repo? Because to do that, you would need more than just current Gentoo developers in your PGP trust DB, but all past ones as well. It becomes needlessly complicated.

You can use [git log \--show-signature] to augment logs with signature verification, but it\'s a bit tiresome to review manually. You can inspire yourself from [https://github.com/hsoft/devscripts/blob/master/verif-sign-until.sh](https://github.com/hsoft/devscripts/blob/master/verif-sign-until.sh) and run something like:

`user `[`$`]`verif-sign-until.sh HEAD~500`

No error? Well it looks like you have a Gentoo repo you can trust!

## [Step 3: Augment with metadata]

You need a few extra metadata repos checkout out for the tree to work properly:

`user `[`$`]`cd metadata `

`user `[`$`]`for x in dtd glsa xml-schema; do`

    > git clone "https://anongit.gentoo.org/git/data/$.git"
    > done

`user `[`$`]`git clone "https://anongit.gentoo.org/git/data/gentoo-news.git" news`

These are very low volume repositories and are easily verified with [git log \--show-signature]. You will also notice that the signature requirement in those repositories aren\'t as strict as with the main Gentoo repo, but since this is purely informational data, malicious injection can\'t have much of an impact there.

## [Step 4: repos.conf]

You can now change the location of your Gentoo [/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf") file to the path of your git clone. Remember to set `sync-openpgp-key-path` to the path of the chosen PGP keyring, e.g. [/usr/share/openpgp-keys/gentoo-developers.asc] if using [[[sec-keys/openpgp-keys-gentoo-developers]](https://packages.gentoo.org/packages/sec-keys/openpgp-keys-gentoo-developers)[]], or a custom keyring if following the manual Web Of Trust method above.

## [Step 5: Generate Portage cache]

The [metadata/md5-cache] directory contains metadata about ebuilds that greatly improves the speed of Portage\'s dependencies calculations. Without it, Portage will be dead slow on your machine:

`user `[`$`]`egencache --jobs=4 --repo gentoo --update --update-pkg-desc-index --update-use-local-desc`

The initial run of this command can take a long time (many minutes), but subsequent runs will be much faster.