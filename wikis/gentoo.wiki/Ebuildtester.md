[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ebuildtester&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/dev-util/ebuildtester)

[[]][Official documentation](http://ebuildtester.readthedocs.io)

[[]][GitHub](https://github.com/nicolasbock/ebuildtester)

[[]][Home](https://pypi.org/project/ebuildtester/)

**ebuildtester** is a [Python](https://wiki.gentoo.org/wiki/Python "Python") script to help automate parts of the [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") testing process by generating [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") containers that replicate fresh Gentoo installations.

ebuildtester compiles a docker container holding the current Gentoo [stage3](https://wiki.gentoo.org/wiki/Stage3 "Stage3"), allowing testing in a clean environment.

This environment is configured by invoking [ebuildtester] with appropriate command-line parameters. On execution, ebuildtester either installs the specified package, or puts the user into a shell, inside the container.

** See also**\
The [official documentation](http://ebuildtester.readthedocs.io) has more details for using ebuildtester.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [No network in the container]](#No_network_in_the_container)
        -   [[3.1.1] [Host running with NFTables block forwarding packets for the container(s)]](#Host_running_with_NFTables_block_forwarding_packets_for_the_container.28s.29)
            -   [[3.1.1.1] [Dirty workaround]](#Dirty_workaround)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/ebuildtester](https://packages.gentoo.org/packages/dev-util/ebuildtester) [[]] [A dockerized approach to test a Gentoo package within a clean stage3 container]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-11 13:43] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-util/ebuildtester`

## [Usage]

`user `[`$`]`ebuildtester --help`

    usage: ebuildtester [-h] [--version] [--atom ATOM [ATOM ...]] [--binhost BINHOST] [--live-ebuild]
                        [--manual] --portage-dir PORTAGE_DIR [--overlay-dir OVERLAY_DIR] [--update]
                        [--install-basic-packages] [--threads N] [--use USE [USE ...]]
                        [--global-use GLOBAL_USE [GLOBAL_USE ...]] [--unmask ATOM] [--unstable] [--gcc-version VER]
                        [--python-single-target PYTHON_SINGLE_TARGET] [--python-targets PYTHON_TARGETS]
                        [--rm] [--storage-opt STORAGE_OPT [STORAGE_OPT ...]] [--with-X] [--with-vnc]
                        [--profile PROFILE] [--features FEATURES [FEATURES ...]] [--docker-image DOCKER_IMAGE]
                        [--docker-command DOCKER_COMMAND] [--pull] [--show-options]
                        [--ccache CCACHE_DIR] [--batch] [--debug]

    A dockerized approach to test a Gentoo package within a clean stage3.

    options:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      --atom ATOM [ATOM ...]
                            The package atom(s) to install
      --binhost BINHOST     Binhost URI
      --live-ebuild         Unmask the live ebuild of the atom
      --manual              Install package manually
      --portage-dir PORTAGE_DIR
                            The local portage directory
      --overlay-dir OVERLAY_DIR
                            Add overlay dir (can be used multiple times)
      --update              Update container before installing atom
      --install-basic-packages
                            Install basic packages after container starts
      --threads N           Use N (default 20) threads to build packages
      --use USE [USE ...]   The use flags for the atom
      --global-use GLOBAL_USE [GLOBAL_USE ...]
                            Set global USE flag
      --unmask ATOM         Unmask atom (can be used multiple times)
      --unstable            Globally 'unstable' system, i.e. ~amd64
      --gcc-version VER     Use gcc version VER
      --python-single-target PYTHON_SINGLE_TARGET
                            Specify a PYTHON_SINGLE_TARGET
      --python-targets PYTHON_TARGETS
                            Specify a PYTHON_TARGETS
      --rm                  Remove container after session is done
      --storage-opt STORAGE_OPT [STORAGE_OPT ...]
                            Storage driver options for all volumes (same as Docker param)
      --with-X              Globally enable the X USE flag
      --with-vnc            Install VNC server to test graphical applications
      --profile PROFILE     The profile to use (default = default/linux/amd64/23.0)
      --features FEATURES [FEATURES ...]
                            Set FEATURES in Gentoo Wiki (default = ['-sandbox', '-usersandbox', 'userfetch'])
      --docker-image DOCKER_IMAGE
                            Specify the docker image to use (default = gentoo/stage3)
      --docker-command DOCKER_COMMAND
                            Specify the docker command
      --pull                Download latest docker image
      --show-options        Show currently selected options and defaults
      --ccache CCACHE_DIR   Path to mount that contains ccache cache
      --batch               Do not drop into interactive shell
      --debug               Add some debugging output

** Note**\
The `--portage-dir` option is mandatory, as well as use of either `--atom` or `--manual`. It is possible to pass in one or more additional overlays with the `--overlay-dir` option.

** Warning**\
ebuildtester maps the [portage] and [overlay] dirs into the container, so changes to the files inside the container will affect the files outside the container on the actual local file system.

An example command for reference could look like this:

[CODE] **One-time test**

    ebuildtester --portage-dir /var/db/repos/gentoo/ \
    --overlay-dir /var/db/repos/src_prepare-overlay/ \
    --binhost https://mirror.bytemark.co.uk/gentoo/releases/amd64/binpackages/23.0/x86-64/ \
    --threads 20 \
    --rm \
    --update \
    --pull \
    --install-basic-packages \
    --global-use dist-kernel \
    --unmask =virtual/dist-kernel-6.19.3 \
    --unmask =sys-kernel/gentoo-kernel-bin-6.19.3 \
    --atom =sys-kernel/gentoo-kernel-bin-6.19.3 =games-util/xone-0.5.5

## [Troubleshooting]

### [No network in the container]

There might be several reasons explaining why the network doesn't works inside the container.

#### [][Host running with NFTables block forwarding packets for the container(s)]

Forwarding packets is needed for Docker to works.

**Docker works along IPTables and does not support NFTables** (officially, but this is a [work-in-progress](https://github.com/docker/for-linux/issues/1472)).

It could works, but running these two firewalls together in this scenario is not recommended because it could make the system(s) unresponsive(s) to the network (host, container or both), as it requires some tweaking to allow IPTables to get the required packets.

** Note**\
The ruleset needed for IPTables are automatically added by Docker on the host once running (and in this case, by ebuildtester) and should not be modified, or it could simply make the container unable to reach the network. See [this section](https://docs.docker.com/engine/network/packet-filtering-firewalls/#prevent-docker-from-manipulating-iptables) of the docker's documentation for more details.

For now there is no official way to properly make them works together. Docker's IPTables rule set needs to be able to forward packets to the proper network interface and if NFTable is dropping the packets before hands, it won't works and the container will have no network access.

##### [Dirty workaround]

A few solutions exist, but none are perfects.

This is a decision that should be made by the administrator, regarding the needs to protect with a firewall the machine or simply what tools suits best the user-case:

1.  Drop or flush the forwarding rules for NFTables, if any, while using docker/ebuildtester.
2.  Replace NFTables with IPTables and let docker/ebuildtester add the needed rules when using it.
3.  **DANGEROUS!** Disabling NFTables while using docker/ebuildtester.
4.  Running the container on a machine that does not need any firewall.
5.  Using any other containers management system that does not rely on IPTables.

\
**(1)** Allow the administrator to keep most of the actual (and working) configuration and require simply a command before and after running ebuildtester.

Keeping in mind that the system won't drop anymore the forwarding packets is important, *which could be seen as a security issue*.

It depends on the administrator to estimate if it is worth it.

It is a risk, but all the other rules for filtering are still actives. This is needed when having more than one interface (which is needed by docker). If the containers have to be working all the time, that probably means the forwarding rules should be disabled for good (or until the containers are not needed anymore).

See [NFTables documentation](https://wiki.nftables.org/wiki-nftables/index.php/Configuring_tables) and the [Nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables") wiki page about it for more details.

**(2)** It would require some works, translating rules from a firewall to another. The good part of this solution is probably that Docker needs IPTables and it won't be an issue anymore, at least until the project add support for NFTables. See the [Iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") wiki page about it.

**(3)** The third is also the worst one (**DANGEROUS**), because all the rule sets are disabled which left the system reachable on any ports worldwide, unless the network's router already block them.

** Warning**\
One should consider if it is useful to have a firewall active, which is a good practice even for a work station. It is more risky to have all the ports opened without filtering anything.

**(4)** Allow the administrator to easily get around the issue, without actually solving it.

**(5)** If not afraid to start over with a new tools to create container. This means also the use of ebuildtester is impossible.

Docker project is working on an implementation of NFTables for the moment, which could in the future solve this issue. See this [opened issue #1472 from the project](https://github.com/docker/for-linux/issues/1472) for more details.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-util/ebuildtester`

## [See also]

-   [Package testing](https://wiki.gentoo.org/wiki/Package_testing "Package testing") --- provides information for ebuild developers on **testing ebuilds**.
-   [Test environment](https://wiki.gentoo.org/wiki/Test_environment "Test environment")