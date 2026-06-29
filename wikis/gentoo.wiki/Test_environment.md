[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

Testing your ebuilds (see also [Package testing](https://wiki.gentoo.org/wiki/Package_testing "Package testing")) can be a tedious task. Beside a simple re-emerge of the package in question, to see whether it merges successfully, a good testing practice usually needs to take one or more of the following questions into account:

-   Having a clean gentoo installation to test with: Using your day to day desktop, might miss on dependencies, which you happen to have installed already and thus producing false positives, i.e. letting your ebuild successfully install, while on a new system it would have been failed due to missing dependencies.
-   An exhaustive testing of all possible **USE flag combinations:** For ebuilds with only a few USE flags, this can be done easily by hand. For packages with a lot of USE flags, such an approach is error-prone. You might be better by writing a shell or python script to enumerate all the possibilities.
-   **Profile testing:** Here testing of default vs. hardened and multilib vs. no-multilib profiles is of interest. It may for example uncover problems with PIC/PIE code in hardened profiles or problems of missing proper multiclassing in the ebuild. Usually you don\'t want to switch profiles just for the purpose of testing an ebuild.
-   **Keyword testing:** This requires the proper hardware and is done by the arch projects.

So to run proper and efficient tests for your ebuild, a dedicated test environment seems necessary. There are several options for this, like using a chroot environment, VM\'s, a containerized enviroment or even dedicated hardware. The table below summarizes some of the pros and cons of these options.

+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Method                                                                                                                                           | Pros                                                                                                                | Cons                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot") [guide](https://wiki.gentoo.org/wiki/Project:X86/Chroot_Guide "Project:X86/Chroot Guide") | -   fast setup                                                                                                      | need to reset the environment after each emerge               |
|                                                                                                                                                  | -   small memory footprint                                                                                          |                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [chroot using btrfs](https://wiki.gentoo.org/wiki/Chroot_for_package_testing "Chroot for package testing")                                       | -   fast setup                                                                                                      | -   needs [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") |
|                                                                                                                                                  | -   small memory footprint                                                                                          | -   need to reset the environment after each emerge           |
+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [Virtual Machine](https://wiki.gentoo.org/wiki/Virtualization#Hypervisors "Virtualization")                                                      | -   easy to set up from a live DVD                                                                                  | large memory footprint                                        |
|                                                                                                                                                  | -   snapshots can be used to avoid reinstallation                                                                   |                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [Container](https://wiki.gentoo.org/wiki/Virtualization#Containers "Virtualization")                                                             | -   fast setup                                                                                                      |                                                               |
|                                                                                                                                                  | -   re-usable (with some work)                                                                                      |                                                               |
|                                                                                                                                                  | -   [safe](https://wiki.gentoo.org/wiki/LXD#Authorize_a_non-privileged_user "LXD")                                  |                                                               |
|                                                                                                                                                  | -   [OpenRC \<-\> Systemd](https://wiki.gentoo.org/wiki/LXD#Running_systemd_based_containers_on_OpenRC_hosts "LXD") |                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

## Contents

-   [[1] [Using Docker containers for ebuild testing with ebuildtester]](#Using_Docker_containers_for_ebuild_testing_with_ebuildtester)
-   [[2] [Using LXC containers for ebuild testing]](#Using_LXC_containers_for_ebuild_testing)
-   [[3] [Using Kubler for ebuild testing]](#Using_Kubler_for_ebuild_testing)
-   [[4] [See also]](#See_also)

#### [Using Docker containers for ebuild testing with ebuildtester]

**[ebuildtester](https://wiki.gentoo.org/wiki/Ebuildtester "Ebuildtester")** is a [Python](https://wiki.gentoo.org/wiki/Python "Python") script for testing ebuilds in a [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") container.

[ebuildtester] compiles a docker container with the parameters passed at invocation time and either installs the specified package or puts the user into a shell inside the container.

Usage of the script is simple, go to the [ebuildtester](https://wiki.gentoo.org/wiki/Ebuildtester "Ebuildtester") article for more details.

#### [Using LXC containers for ebuild testing]

These instructions make use of [unprivileged LXC containers](https://wiki.gentoo.org/wiki/LXC#Configuring_unprivileged_LXC "LXC").

`user `[`$`]`lxc-create -t download -n proxy-maint`

Then for **Distribution**, choose *gentoo*; **Release**, choose *current*; and **Architecture**, choose *amd64*.

When it completes, start up the container with,

`user `[`$`]`lxc-start -n proxy-maint`

Then configure a basic development environment using the [recommended tools](https://wiki.gentoo.org/wiki/Package_testing#Tools "Package testing").

[FILE] **`/etc/portage/sets/tools`**

    # tools
    app-crypt/gnupg
    app-editors/vim # or just symlink busybox to `/usr/local/bin/vi` and update your environment variables.
    app-portage/tatt
    dev-vcs/git
    dev-util/pkgcheck
    dev-util/pkgdev

`user `[`$`]`lxc-console -n proxy-maint`

`root `[`#`]`emerge --ask @tools`

To stop the container,

`user `[`$`]`lxc-stop -n proxy-maint`

To clone the container for working on a particular ebuild,

`user `[`$`]`lxc-copy -n proxy-maint -N "$" # clones the original container`

To delete it when finished,

`user `[`$`]`lxc-destroy -n "$" # destroy the container when finished`

#### [Using Kubler for ebuild testing]

See [Kubler](https://wiki.gentoo.org/wiki/Kubler "Kubler") for more info.

Kubler may be used to develop against any ebuild repository.

Create a new namespace, let\'s call it [edev]:

`user `[`$`]`kubler new namespace edev`

Create a new builder, select `kubler/bob` as `IMAGE_PARENT`:

`user `[`$`]`kubler new builder edev/bob`

Edit the new builder\'s [build.sh] and add any additional repositories:

** Note**\
For [::gentoo] only there\'s no need to add the repo, it\'s already available; binding in the development fork and updating [.bashrc] is probably desirable, however.

[FILE] **`/config/build.sh`**

    configure_builder()

Create a new image, let\'s call it bench, use `kubler/bash` as `IMAGE_PARENT`:

`user `[`$`]`kubler new image edev/bench`

Edit the new image\'s build.conf and configure the builder and ebuild repo to be mounted builder:

[FILE] **`/config/build.conf`**

    BUILDER="edev/bob"
    BUILDER_MOUNTS=(
        "/data/development/ebuild-repos/gentoo:/var/db/repos/gentoo"
        "/data/development/ebuild-repos/kubler-overlay:/var/db/repos/kubler"
    )

Start an interactive build container and get tinkering:

`user `[`$`]`kubler build -i edev/bench`

`root `[`#`]`ebuild dev-lang/foo/foo-0.4.0.ebuild manifest merge`

## [See also]

-   [Incus/Gentoo Github pullrequest testing](https://wiki.gentoo.org/wiki/Incus/Gentoo_Github_pullrequest_testing "Incus/Gentoo Github pullrequest testing") --- easy and automated way for testing ebuild contributions via [Gentoo\'s Github mirror](https://github.com/gentoo/gentoo) that\'s based on [Incus](https://wiki.gentoo.org/wiki/Incus "Incus")
-   [Package testing](https://wiki.gentoo.org/wiki/Package_testing "Package testing") --- provides information for ebuild developers on **testing ebuilds**.
-   [Project:X86/Chroot Guide](https://wiki.gentoo.org/wiki/Project:X86/Chroot_Guide "Project:X86/Chroot Guide") --- provides instructions on how to create a fresh Gentoo installation inside a [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot") to assist in testing Gentoo packages for stabilization and for other sundry testing.
-   [User:SwifT/Gensetup](https://wiki.gentoo.org/wiki/User:SwifT/Gensetup "User:SwifT/Gensetup") --- automates the installation of Gentoo on KVM guests for testing and development purposes.