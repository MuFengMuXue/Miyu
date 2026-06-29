[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Portage_Prefix_Python_Venv_Usr_Local_Multi_Distro&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Create a Gentoo prefix in /usr/local on a non-Gentoo Linux Distro using a Python Virtual Environment

[CODE] **Create a Portage Prefix in /usr/local on a non-Gentoo Linux Distro**

    FROM docker.io/ubuntu:rolling
    RUN \
    ln -sf /usr/share/zoneinfo/UTC /etc/localtime && \
    echo America/Los_Angeles > /etc/timezone && \
    env DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y --no-install-recommends build-essential python-is-python3 python3-venv busybox git ssh wget rsync libssl-dev libz-dev pkg-config && rm -rf /var/lib/apt/lists/* && \
    export EPREFIX=/usr/local && \
    python -m venv "$" && \
    . "$/bin/activate" && \
    pip install portage && \
    for p in env.d portage/make.conf portage/repos.conf; do mkdir -p "$/etc/$"; done && \
    echo ROOTPATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin > "$/etc/env.d/05rootpath" && \
    mkdir -p "$/var/db/repos" && git clone --depth 1 https://github.com/gentoo-mirror/gentoo.git "$/var/db/repos/gentoo" && \
    profile=$(find /usr/local/var/db/repos/gentoo/profiles/default/linux/amd64 -mindepth 1 -maxdepth 1 -type d | sort -V | tail -n1) && \
    ln -snf ../..$} "$/etc/portage/make.profile" && \
    groupadd --system -g 250 portage && \
    useradd --system -u 250 -g portage --home-dir "$/var/lib/portage/home" portage && \
    echo 'FEATURES="-buildpkg -ipc-sandbox -network-sandbox -pid-sandbox -sandbox -usersandbox"' >> "$/etc/portage/make.conf/01-defaults.conf" && \
    echo 'MAKEOPTS="-j'$(nproc)' -l'$(nproc)'"' >> "$/etc/portage/make.conf/01-defaults.conf" && \
    echo 'EMERGE_DEFAULT_OPTS="-j'$(nproc)' -l'$(nproc)'"' >> "$/etc/portage/make.conf/01-defaults.conf" && \
    env-update && \
    emerge -V