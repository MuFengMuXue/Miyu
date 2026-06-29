[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=GitLab/Pages&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://docs.gitlab.com/ee/user/project/pages/)

[[]][GitLab](https://gitlab.com/gitlab-org/gitlab-pages)

Gitlab-Pages serves the static content generated through the Gitlab-CI machinery of a Gitlab-HQ server. It provides a convenient means of hosting statically generated websites; usually this including ones project documentation. It does this over both HTTP and HTTPS connections and may be exposed directly to the internet or proxied through load balancing server.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [References]](#References)

## [Installation]

To install this package one must enable the Gitlab overlay, described under [GitLab](https://wiki.gentoo.org/wiki/GitLab "GitLab"), and installed as follows :

`root `[`#`]`emerge --ask dev-vcs/gitlab-pages`

## [Configuration]

The configuration file, [/etc/conf.d/gitlab-pages], handles the applications settings.

At a minimum one must specify the following attributes for Gitlab Pages to operate :

[gitlab-server]

The URL for ones Gitlab instance

[api-secret-key]

An API key generated as described below

[pages-domain]

The URL for ones Gitlab-Pages instance

[listen-proxy] or [listen-http] or [listen-https]

The IP address and/or port Gitlab-Pages is to listen on

[FILE] **`/etc/gitlab/gitlab.yml`Gitlab-Pages**

    pages:
      enabled: true
      ...
      secret_file: /opt/gitlab/gitlab/.gitlab-pages-secret

** Note**\
Use the following to generate a secret key for Gitlab-Pages

`user `[`$`]`mkdir /etc/gitlab-pages `

`user `[`$`]`sudo -u git -H openssl rand -base64 32 > /opt/gitlab/gitlab/.gitlab-pages-secret `

`user `[`$`]`ln -s /opt/gitlab/gitlab/.gitlab_pages_secret /opt/gitlab/gitlab-pages/.gitlab_pages_secret`

## [Usage]

Gitlb-Pages may be invoked directly, as follows, but this is best left to the OpenRC/SystemD service file.

`user `[`$`]`gitlab-pages -listen-http=:8090 -pages-root=/opt/gitlab/gitlab/shared/pages api-secret-key=/opt/gitlab/gitlab/.gitlab_pages_secret -pages-domain=example.io -internal-gitlab-server=https://gitlab.example.com`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-vcs/gitlab-pages`

## [References]

[Gitlab-Pages:Administration](https://docs.gitlab.com/ee/administration/pages/source.html#wildcard-domains)