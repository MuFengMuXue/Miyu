Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/de "/etc/portage/repos.conf (70% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/es "/etc/portage/repos.conf (4% translated)")
-   [français](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/fr "repos.conf (78% translated)")
-   [hrvatski](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/hr "/etc/portage/repos.conf (4% translated)")
-   [italiano](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/it "/etc/portage/repos.conf (4% translated)")
-   [magyar](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/hu "/etc/portage/repos.conf (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/pl "/etc/portage/repos.conf (4% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/pt-br "/etc/portage/repos.conf (4% translated)")
-   [русский](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/ru "/etc/portage/repos.conf (100% translated)")
-   [українська](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/uk "/etc/portage/repos.conf (74% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/zh-cn "/etc/portage/make.conf (13% translated)")
-   [日本語](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/ja "/etc/portage/repos.conf (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/ko "/etc/portage/repos.conf (4% translated)")

The [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") and [additional repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") configuration files are in the [/etc/portage/repos.conf] directory, which specifies current [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") configured repositories\' location and settings.

Creating it manually is not recommended by the handbook anymore. It changes [/usr/share/portage/config/repos.conf] defaults.

Necessary [repos.conf] settings, such as the `sync-uri` value, can be changed. Portage automatically adds some missing configuration file values, such as `priority`.

** Tip**\
The [eselect-repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") tool automatically configures [/etc/portage/repos.conf].

** Note**\
[man 5 portage](https://dev.gentoo.org/~zmedico/portage/doc/man/portage.5.html), section [/etc/portage/repos.conf] details repos.conf parameters and format information.

## Contents

-   [[1] [Manage repositories]](#Manage_repositories)
-   [[2] [List repositories]](#List_repositories)
-   [[3] [Ebuild repository priority]](#Ebuild_repository_priority)
-   [[4] [Alternative sync protocols]](#Alternative_sync_protocols)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [[] Manage repositories]

Add, disable, or remove ebuild repositories using [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository"), which also provides other functionality.

It is also possible to add a repository by manually creating files in [/etc/portage/repos.conf], see the [appropriate section of the Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/CustomTree#Defining_a_custom_ebuild_repository "Handbook:AMD64/Portage/CustomTree") ([other reference](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Files#Gentoo_ebuild_repository "Handbook:AMD64/Portage/Files")).

Files in [/etc/portage/repos.conf] can be [edited with a text editor](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file") to change the configuration options for an ebuild repository.

## [[] List repositories]

To show all repositories configured with portage, run [portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq"):

`user `[`$`]`portageq repos_config /`

    [DEFAULT]
    auto-sync = yes
    main-repo = gentoo
    strict-misc-digests = true
    sync-allow-hardlinks = true
    sync-rcu = false

    [brother-overlay]
    auto-sync = yes
    location = /var/db/repos/brother-overlay
    masters = gentoo
    strict-misc-digests = true
    sync-allow-hardlinks = true
    sync-rcu = false
    sync-type = git
    sync-uri = https://github.com/gentoo-mirror/brother-overlay.git

    [gentoo]
    auto-sync = yes
    location = /var/db/repos/gentoo
    masters =
    priority = -1000
    strict-misc-digests = true
    sync-allow-hardlinks = true
    sync-openpgp-key-path = /usr/share/openpgp-keys/gentoo-release.asc
    sync-openpgp-key-refresh-retry-count = 40
    sync-openpgp-key-refresh-retry-delay-exp-base = 2
    sync-openpgp-key-refresh-retry-delay-max = 60
    sync-openpgp-key-refresh-retry-delay-mult = 4
    sync-openpgp-key-refresh-retry-overall-timeout = 1200
    sync-openpgp-keyserver = hkps://keys.gentoo.org
    sync-rcu = false
    sync-type = rsync
    sync-uri = rsync://rsync.gentoo.org/gentoo-portage
    sync-rsync-verify-max-age = 24
    sync-rsync-extra-opts =
    sync-rsync-verify-jobs = 1
    sync-rsync-verify-metamanifest = yes

    [local]
    auto-sync = no
    location = /var/db/repos/local
    masters = gentoo
    strict-misc-digests = true
    sync-allow-hardlinks = true
    sync-rcu = false

## [[] Ebuild repository priority]

To set the *[priority](https://wiki.gentoo.org/wiki/Ebuild_repository#Installing_packages_from_other_repositories "Ebuild repository")* of a certain repository, manually edit the relevant repos.conf section and set `priority =` to the desired value. The higher the set value, the higher the priority. For example:

[FILE] **`/etc/portage/repos.conf/eselect-repo.conf`Set priority of a repository**

    # created by eselect-repo

    [guru]
    location = /var/db/repos/guru
    sync-type = git
    sync-uri = https://github.com/gentoo-mirror/guru.git
    priority = 100

Repositories that do not have a priority explicitly set, default to `0` - except the Gentoo ebuild repository, which defaults to to a value of `-1000`.

## [[] Alternative sync protocols]

See the [Portage with Git](https://wiki.gentoo.org/wiki/Portage_with_Git "Portage with Git") article for how to sync the ::gentoo ebuild repository using [git] as an alternative to the traditional rsync protocol.

## [[] See also]

-   [Project:Portage/Repository_Verification](https://wiki.gentoo.org/wiki/Project:Portage/Repository_Verification "Project:Portage/Repository Verification") --- describes different methods used to ensure authenticity of the Gentoo ebuild repository.
-   [Overview of the Portage sync system](https://wiki.gentoo.org/wiki/Project:Portage/Sync "Project:Portage/Sync")
-   [Overlays user guide](https://wiki.gentoo.org/wiki/Project:Overlays/Overlays_guide "Project:Overlays/Overlays guide")
-   [Repository format](https://wiki.gentoo.org/wiki/Repository_format "Repository format") --- A quick reference to Gentoo ebuild repository (overlay) format.
-   [Repository mirror and Continuous Integration](https://wiki.gentoo.org/wiki/Project:Repository_mirror_and_CI "Project:Repository mirror and CI")
-   [Query repository information](https://wiki.gentoo.org/wiki/Portageq#Query_repository_information "Portageq") in the [Portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq") article
-   [Using the gentoo git checkout as your local tree](https://wiki.gentoo.org/wiki/Gentoo_git_workflow#Using_the_gentoo_git_checkout_as_your_local_tree "Gentoo git workflow")
-   [Masking enabled ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository#Masking_enabled_ebuild_repositories "Ebuild repository")
-   [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") --- an [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect") module for configuring [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage").
-   [Portage Security](https://wiki.gentoo.org/wiki/Portage_Security "Portage Security") --- aims to answer the question *\"How can I dispel doubts regarding the security of the Gentoo ebuild repository on a system?\"*
-   [/etc/portage/binrepos.conf](https://wiki.gentoo.org/wiki//etc/portage/binrepos.conf "/etc/portage/binrepos.conf") --- specifies the location and settings for binary package repositories configured with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage").

## [[] External resources]

-   [rsync.gentoo.org rsync modules: gentoo-repo-changelog added, gentoo-x86-portage & gentoo-sec discontinued.](https://archives.gentoo.org/gentoo-dev-announce/message/651feb859ae9669dfeaa19547fa698dc)