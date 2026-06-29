This page contains [[changes](https://wiki.gentoo.org/index.php?title=Basic_guide_to_write_Gentoo_Ebuilds&oldid=1426925&diff=1427139)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds/de "Grundlegende Anleitung zum Schreiben von Gentoo Ebuilds (41% translated)")
-   [English]
-   [français](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds/fr "Guide basique d'écriture d'Ebuilds pour Gentoo (46% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds/it "Guida di base per scrivere Ebuild Gentoo (3% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds/hu "Alapvető útmutató a Gentoo Ebuild fájlok írásához (93% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds/pt-br "Guia básico para escrever ebuilds Gentoo (63% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds/ru "Начальное руководство по написанию ebuild-файлов в Gentoo (97% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds/zh-cn "Gentoo Ebuild 编写基本指南 (27% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds/ja "Gentoo Ebuild 執筆基本ガイド (100% translated)")

This is a guide to getting started writing **[ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild")**, to harness the power of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), to install and manage even more software.

Write an ebuild to install a piece of software on Gentoo, when there are no suitable preexisting ebuilds. It\'s a relatively straight forward task, and is the only way to cleanly install most \"third party\" software system-wide. The ebuild will allow the [package manager](https://wiki.gentoo.org/wiki/Project:Package_Manager_Specification#Implementation_in_package_managers "Project:Package Manager Specification") to track every file installed to the system, to allow clean updates and removal.

** Tip**\
**From the [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") article**: An *ebuild* file is a text file, usually stored in a [repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"), which identifies a specific software package and tells the Gentoo package manager how to handle it. Ebuilds use a [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell) "wikipedia:Bash (Unix shell)")-like syntax style and are standardized through the [Package Manager Specification](https://wiki.gentoo.org/wiki/Package_Manager_Specification "Package Manager Specification"), by adhering to a specific [EAPI](https://wiki.gentoo.org/wiki/EAPI "EAPI") version.\
\
Ebuilds contain metadata about each version of a piece of available software (name, version number, license, home page address\...), dependency information (both build-time and run-time), and instructions on how to build and install the software (configure, compile, build, install, test\...).

Once an ebuild is working, it can be shared by submitting it in a [pull request](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests "GitHub Pull Requests") or in a separate [ebuild repository](https://repos.gentoo.org/) and making it accessible publicly. With a little effort, ebuilds can be proposed and maintained in the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository.

** Note**\
See the [dev manual on writing ebuilds](https://devmanual.gentoo.org/ebuild-writing/index.html) for full reference documentation. See the [quick start to writing ebuilds in the dev manual](https://devmanual.gentoo.org/quickstart/index.html) for further examples of how to write ebuilds. See the [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") article for explanations about ebuilds themselves, the [ebuild repository article](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") about what an ebuild repository is, and the [creating an ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") article on how to create them.

## Contents

-   [[1] [Ebuild repositories]](#Ebuild_repositories)
-   [[2] [How to create an ebuild]](#How_to_create_an_ebuild)
    -   [[2.1] [Start with the skeleton]](#Start_with_the_skeleton)
    -   [[2.2] [Vim]](#Vim)
    -   [[2.3] [Emacs]](#Emacs)
    -   [[2.4] [Language server]](#Language_server)
-   [[3] [Demonstration by example]](#Demonstration_by_example)
-   [[4] [Patching upstream source in an ebuild]](#Patching_upstream_source_in_an_ebuild)
-   [[5] [QA testing]](#QA_testing)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [[] Ebuild repositories]

In order for ebuilds to be available to [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), they are placed in an [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") that is configured for Portage through [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")] (see the section on [repository management](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_management "Ebuild repository") for general information about working with ebuild repositories).

[Create](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository#Creating_an_empty_repository "Creating an ebuild repository") an ebuild repository to experiment in, while following on with this guide. The rest of the article will consider a repository in [/var/db/repos/example_repository].

[[eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository")] makes creating a repository simple:

`root `[`#`]`emerge -a app-eselect/eselect-repository`

`root `[`#`]`eselect repository create example_repository`

** Note**\
Ebuilds *can* be installed with the [ebuild command](https://devmanual.gentoo.org/eclass-reference/ebuild/index.html), however this is **not** recommended - this command is for development purposes only. This article will use the [ebuild] command with the ebuild file for testing during development, but be sure to use the [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") command with an ebuild in a repository otherwise.

## [[] How to create an ebuild]

Ebuilds are simply text files, in their most basic form. All that is needed to start writing ebuilds is a [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor"), to provide installable software packages for Gentoo.

** Note**\
In this section, [], [], and [] represent *package category*, *package name*, and *package name and version*, and are standard [variables used in ebuilds](https://devmanual.gentoo.org/ebuild-writing/variables/). Together, these variables can represent a [version specifier](https://wiki.gentoo.org/wiki/Version_specifier "Version specifier").

Some editors have optional ebuild functionality, in that case there skip to the appropriate section. Otherwise a skeleton (\"template\") may be used to get started quicker.

### [[] Start with the skeleton]

If the editor does not have integrated ebuild functionality to help to start off, there is a skeleton ebuild file ([skel.ebuild]) located in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"). To start with that file as a base, simply copy it to an appropriate location ([nano] is used as the text editor in this example):

`user `[`$`]`mkdir --parents /var/db/repos/example_repository// `

`user `[`$`]`cp /var/db/repos/gentoo/skel.ebuild /var/db/repos/example_repository///.ebuild `

`user `[`$`]`cd /var/db/repos/example_repository// `

`user `[`$`]`nano .ebuild `

### [[] Vim]

There is a vim plugin to automatically start from a skeleton when creating an empty ebuild file.

After installing [[[app-vim/gentoo-syntax]](https://packages.gentoo.org/packages/app-vim/gentoo-syntax)[]], create the appropriate directory for the ebuild, then launch [vim](https://wiki.gentoo.org/wiki/Vim "Vim") with a new \".ebuild\" filename provided on the command line, to be automatically met with a basic skeleton that can be modified and saved:

`user `[`$`]`mkdir --parents /var/db/repos/example_repository// `

`user `[`$`]`cd /var/db/repos/example_repository// `

`user `[`$`]`vim .ebuild`

### [[] Emacs]

A similar tool is available for users of [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs"), provided by [[[app-emacs/ebuild-mode]](https://packages.gentoo.org/packages/app-emacs/ebuild-mode)[]] or [[[app-xemacs/ebuild-mode]](https://packages.gentoo.org/packages/app-xemacs/ebuild-mode)[]], depending on Emacs distribution.

### [[] Language server]

There is [a language server for gentoo ebuild](https://github.com/termux/termux-language-server).

## [[] Demonstration by example]

This example will create an ebuild for [scrub](https://github.com/chaos/scrub), version 2.6.1 (if it didn\'t already exist), to show how a typical process might go.

Create a directory to house the ebuild, in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") created earlier:

`user `[`$`]`mkdir -p /var/db/repos/example_repository/app-misc/scrub`

Change the shell working directory to the new path:

`user `[`$`]`cd /var/db/repos/example_repository/app-misc/scrub`

** Tip**\
Some shells, such as Bash, provide the last parameter of the previous command in the \"\$\_\" variable. This can be used to call the newly created directory without specifying the path on the command line, as long as this is used as the directly next command.

`user `[`$`]`cd $_`

This example will use Vim to create the ebuild file and provide a skeleton to serve as a basis to write the ebuild on, but use editor of choice (see previous section about using Emacs, or the skeleton file):

`user `[`$`]`vim ./scrub-2.6.1.ebuild`

Add important information about the new package by setting the [ebuild-defined variables](https://devmanual.gentoo.org/ebuild-writing/variables/index.html#ebuild-defined-variables): DESCRIPTION, [HOMEPAGE](https://projects.gentoo.org/qa/policy-guide/other-metadata.html#pg0702), [SRC_URI](https://projects.gentoo.org/qa/policy-guide/ebuild-format.html#pg0104), [LICENSE](https://projects.gentoo.org/qa/policy-guide/other-metadata.html#pg0704). Licenses like BSD-clause-3 which are not found in [the tree](https://gitweb.gentoo.org/repo/gentoo.git/tree/licenses) might be mapped in [metadata](https://gitweb.gentoo.org/repo/gentoo.git/tree/metadata/license-mapping.conf) :

[FILE] **`scrub-2.6.1.ebuild`vim editing a new file from template**

    # Copyright 1999-2026 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    EAPI=8

    DESCRIPTION="Some words here"
    HOMEPAGE="https://github.com/chaos/scrub"
    SRC_URI="https://github.com/chaos/scrub/releases/download/2.6.1/scrub-2.6.1.tar.gz"

    LICENSE="GPL-2"
    SLOT="0"
    KEYWORDS="~amd64 ~x86"
    IUSE=""

    DEPEND=""
    RDEPEND="$"
    BDEPEND=""

This --- with the omission of those lines with `=""` --- is the minimum information necessary to get something that will work. Ebuilds inheriting certain eclasses might come with a different set of minimal information, e.g. [ant-jsch-1.10.9.ebuild](https://gitweb.gentoo.org/repo/gentoo.git/tree/dev-java/ant-jsch/ant-jsch-1.10.9.ebuild). Save the file - voila an ebuild, in its most basic form, it\'s that simple!

** Note**\
Using the [`$` variable](https://devmanual.gentoo.org/ebuild-writing/variables/) inside `SRC_URI` is allowed, though this is **not necessarily best practice**. While it may be shorter to type, there is some [reasoning on why not to use it](https://devmanual.gentoo.org/ebuild-writing/variables/#use-of-constant-value-variables-in-ebuilds) that may be worth consideration.

[CODE] **avoid using PN as such**

    SRC_URI="https://github.com/gentoo/$/releases/download/$/$.tar.gz"
    # Reads better as, e.g.
    SRC_URI="https://github.com/gentoo/gentoo/releases/download/$/$.tar.gz"

See this [ebuild file format policy guide page](https://projects.gentoo.org/qa/policy-guide/ebuild-format.html) for more recommendations.

It is possible to test fetching and unpacking the upstream sources by the new ebuild, using the [[ebuild](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.1.html)] command:

`root `[`#`]`GENTOO_MIRRORS="" ebuild ./scrub-2.6.1.ebuild manifest clean unpack`

    Appending /var/db/repos/customrepo to PORTDIR_OVERLAY...
    >>> Downloading 'https://github.com/chaos/scrub/releases/download/2.6.1/scrub-2.6.1.tar.gz'
    --2023-03-03 23:35:13--  https://github.com/chaos/scrub/releases/download/2.6.1/scrub-2.6.1.tar.gz
    Resolving github.com... 140.82.121.4
    Connecting to github.com|140.82.121.4|:443... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: https://objects.githubusercontent.com/github-production-release-asset-2e65be/23157201/405a65b8-2d4d-11e4-8f82-3e3a9951b650?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230303%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230303T223513Z&X-Amz-Expires=300&X-Amz-Signature=7d7d925ff8392ee2ba12028c73c8d8c3b3a7086b5aec11bbfae335222a4f2eb0&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=23157201&response-content-disposition=attachment%3B%20filename%3Dscrub-2.6.1.tar.gz&response-content-type=application%2Foctet-stream [following]
    --2023-03-03 23:35:13--  https://objects.githubusercontent.com/github-production-release-asset-2e65be/23157201/405a65b8-2d4d-11e4-8f82-3e3a9951b650?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230303%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230303T223513Z&X-Amz-Expires=300&X-Amz-Signature=7d7d925ff8392ee2ba12028c73c8d8c3b3a7086b5aec11bbfae335222a4f2eb0&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=23157201&response-content-disposition=attachment%3B%20filename%3Dscrub-2.6.1.tar.gz&response-content-type=application%2Foctet-stream
    Resolving objects.githubusercontent.com... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
    Connecting to objects.githubusercontent.com|185.199.108.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 362536 (354K) [application/octet-stream]
    Saving to: '/var/cache/distfiles/scrub-2.6.1.tar.gz.__download__'

    /var/cache/distfiles/scrub-2.6.1. 100%[============================================================>] 354.04K  --.-KB/s    in 0.08s

    2023-03-03 23:35:13 (4.31 MB/s) - '/var/cache/distfiles/scrub-2.6.1.tar.gz.__download__' saved [362536/362536]

     * scrub-2.6.1.tar.gz BLAKE2B SHA512 size ;-) ...                                                                               [ ok ]
    >>> Unpacking source...
    >>> Unpacking scrub-2.6.1.tar.gz to /var/tmp/portage/app-misc/scrub-2.6.1/work
    >>> Source unpacked in /var/tmp/portage/app-misc/scrub-2.6.1/work

This should download and unpack the source tarball, without error, as in the example output.

Also, there\'s [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") for creating Manifest files:

`user `[`$`]`pkgdev manifest -d ~/a/folder/for/distfiles ./app-misc/scrub/scrub-2.6.1.ebuild`

For some exceptionally simple packages like this one, that do not need patching or other more advanced treatment, the ebuild may work just so - with no further adjustments needed.

For best practice, the test suite may be run at this stage - this is particularly true when starting out:

`root `[`#`]`ebuild scrub-2.6.1.ebuild clean test install`

To actually install the new ebuild on the system, run:

`root `[`#`]`ebuild scrub-2.6.1.ebuild clean install merge`

## [[] Patching upstream source in an ebuild]

A patch can be created from the unpacked source code as explained in the [Creating a patch](https://wiki.gentoo.org/wiki/Creating_a_patch "Creating a patch") article. Patches should then be put in the [files] directory and be listed in an array called `PATCHES` as explained in the [devmanual](https://devmanual.gentoo.org/ebuild-writing/functions/src_prepare/eapply/index.html):

[CODE] **Patches will be applied during src_prepare**

    PATCHES=(
        "$"/$-foo.patch
        "$"/$-bar.patch
    )

    src_prepare()

## [[] QA testing]

Use [pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck") ([[[dev-util/pkgcheck]](https://packages.gentoo.org/packages/dev-util/pkgcheck)[]]) to check for QA errors in an ebuild:

`user `[`$`]`pkgcheck scan`

## [[] See also]

-   [GitHub Pull Requests](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests "GitHub Pull Requests") --- how to contribute to Gentoo by creating [pull requests on GitHub](https://github.com/gentoo/gentoo/pulls).
-   [java-ebuilder](https://wiki.gentoo.org/wiki/Java-ebuilder "Java-ebuilder") --- an experimental package being developed by Gentoo Java developers to generate initial ebuilds from [Maven](https://wiki.gentoo.org/wiki/Maven "Maven") `pom.xml` files.
-   [Notes on ebuilds with GUI](https://wiki.gentoo.org/wiki/Notes_on_ebuilds_with_GUI "Notes on ebuilds with GUI")
-   [Project:GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") --- an official repository of new Gentoo packages that are maintained collaboratively by Gentoo users
-   [Project:Proxy_Maintainers/User_Guide/Style_Guide](https://wiki.gentoo.org/wiki/Project:Proxy_Maintainers/User_Guide/Style_Guide "Project:Proxy Maintainers/User Guide/Style Guide")
-   [Project:Python](https://wiki.gentoo.org/wiki/Project:Python "Project:Python") --- the Python project pages have information on creating ebuilds for packages written in Python
-   [Project:X11/Ebuild_maintenance](https://wiki.gentoo.org/wiki/Project:X11/Ebuild_maintenance "Project:X11/Ebuild maintenance")
-   [Proxied Maintainer FAQ](https://wiki.gentoo.org/wiki/Proxied_Maintainer_FAQ "Proxied Maintainer FAQ")
-   [Test environment](https://wiki.gentoo.org/wiki/Test_environment "Test environment")
-   [Writing go Ebuilds‎‎](https://wiki.gentoo.org/wiki/Writing_go_Ebuilds "Writing go Ebuilds") --- a short reference, intended to be read alongside [Basic guide to write Gentoo Ebuilds] and the [go-module.eclass documentation](https://devmanual.gentoo.org/eclass-reference/go-module.eclass/index.html)
-   [Ebuild_guidance_for_ecosystems](https://wiki.gentoo.org/wiki/Ebuild_guidance_for_ecosystems "Ebuild guidance for ecosystems")

## [[] External resources]

-   [Gentoo Policy Guide](https://projects.gentoo.org/qa/policy-guide/)
-   [Quickstart Ebuild Guide](https://devmanual.gentoo.org/quickstart/)
-   [Gentoo Development guide](https://devmanual.gentoo.org/)
-   [Michał Górny: Category: Ebuild writing](https://blogs.gentoo.org/mgorny/category/gentoo/ebuild-writing/)
-   [Michał Górny: The ultimate guide to EAPI 7](https://mgorny.pl/articles/the-ultimate-guide-to-eapi-7.html)
-   [Michał Górny: The ultimate guide to EAPI 8](https://mgorny.pl/articles/the-ultimate-guide-to-eapi-8.html)
-   [ebuild command\'s man page](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.1.html)
-   [ebuild file format man page](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.5.html)
-   [The skel.ebuild](https://gitweb.gentoo.org/repo/gentoo.git/tree/skel.ebuild)
-   [Adding new packages via proxy-maint project](https://archives.gentoo.org/gentoo-proxy-maint/message/44f7712fb49850288cd840c3541f6d7e)