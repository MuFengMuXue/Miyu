**Resources**

[[]][Home](https://linuxcontainers.org/incus/introduction/)

[[]][Official documentation](https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/)

[[]][Package information](https://packages.gentoo.org/packages/app-containers/incus)

[[]][GitHub](https://github.com/lxc/incus)

[[]][Bugs (upstream)](https://github.com/lxc/incus/issues)

[[]][[#lxc](ircs://irc.libera.chat/#lxc)] ([[webchat](https://web.libera.chat/#lxc)])

**Incus** is a next generation system container and virtual machine manager. It offers a unified user experience around full Linux systems running inside [containers or virtual machines](https://wiki.gentoo.org/wiki/Virtualization "Virtualization"). Incus is a fork from [LXD](https://wiki.gentoo.org/wiki/LXD "LXD").

Incus is image based and provides images for a [wide number of Linux distributions](https://images.linuxcontainers.org/). It provides flexibility and scalability for various use cases, with support for different storage backends and network types and the option to install on hardware ranging from an individual laptop or cloud instance to a full server rack.

When using Incus, you can manage your instances (containers and VMs) with a simple command line tool, directly through the REST API or by using third-party tools and integrations. Incus implements a single REST API for both local and remote access.

## Contents

-   [[1] [Installing]](#Installing)
    -   [[1.1] [Configuring service files]](#Configuring_service_files)
        -   [[1.1.1] [OpenRC]](#OpenRC)
        -   [[1.1.2] [systemd]](#systemd)
    -   [[1.2] [Adding a user to correct groups]](#Adding_a_user_to_correct_groups)
    -   [[1.3] [Configure idmaps]](#Configure_idmaps)
    -   [[1.4] [Start the daemons]](#Start_the_daemons)
        -   [[1.4.1] [OpenRC]](#OpenRC_2)
            -   [[1.4.1.1] [With incus-user configured]](#With_incus-user_configured)
            -   [[1.4.1.2] [Without incus-user configured]](#Without_incus-user_configured)
        -   [[1.4.2] [systemd]](#systemd_2)
            -   [[1.4.2.1] [With incus-user configured]](#With_incus-user_configured_2)
    -   [[1.5] [Migrating from LXD]](#Migrating_from_LXD)
        -   [[1.5.1] [With the \'lxd-to-incus\' tool]](#With_the_.27lxd-to-incus.27_tool)
        -   [[1.5.2] [Manual migration]](#Manual_migration)
            -   [[1.5.2.1] [Local (single-host) system]](#Local_.28single-host.29_system)
            -   [[1.5.2.2] [Public system]](#Public_system)
    -   [[1.6] [Initializing Incus]](#Initializing_Incus)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Profile]](#Profile)
    -   [[2.2] [Network]](#Network)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Finding pre-built container images]](#Finding_pre-built_container_images)
    -   [[3.2] [Launching containers]](#Launching_containers)
        -   [[3.2.1] [Limiting container resources]](#Limiting_container_resources)
            -   [[3.2.1.1] [CPU]](#CPU)
            -   [[3.2.1.2] [Memory]](#Memory)
        -   [[3.2.2] [Launching virtual machines]](#Launching_virtual_machines)
            -   [[3.2.2.1] [Limiting virtual machine resources]](#Limiting_virtual_machine_resources)
            -   [[3.2.2.2] [Growing default disk size]](#Growing_default_disk_size)
            -   [[3.2.2.3] [Red Hat / CentOS variants]](#Red_Hat_.2F_CentOS_variants)
        -   [[3.2.3] [Making custom container images]](#Making_custom_container_images)
-   [[4] [Advanced usage]](#Advanced_usage)
    -   [[4.1] [Container backups]](#Container_backups)
    -   [[4.2] [Move/copy containers between projects]](#Move.2Fcopy_containers_between_projects)
    -   [[4.3] [Multi-host setup]](#Multi-host_setup)
    -   [[4.4] [Pulseaudio in a container]](#Pulseaudio_in_a_container)
    -   [[4.5] [Sharing files/directories between container and host]](#Sharing_files.2Fdirectories_between_container_and_host)
    -   [[4.6] [systemd containers on OpenRC host]](#systemd_containers_on_OpenRC_host)
    -   [[4.7] [X and Wayland apps in a container]](#X_and_Wayland_apps_in_a_container)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Adding a disk device with incus-user fails to \"Disk source path not allowed\"]](#Adding_a_disk_device_with_incus-user_fails_to_.22Disk_source_path_not_allowed.22)
    -   [[5.2] [Containers or virtual machines (OpenRC) not shutting down properly]](#Containers_or_virtual_machines_.28OpenRC.29_not_shutting_down_properly)
    -   [[5.3] [Fresh containers fail to start with a cryptic \"newuidmap failed to write mapping\" message]](#Fresh_containers_fail_to_start_with_a_cryptic_.22newuidmap_failed_to_write_mapping.22_message)
    -   [[5.4] [Various dnsmasq related issues]](#Various_dnsmasq_related_issues)
        -   [[5.4.1] [Can\'t create new network bridge incusbr0]](#Can.27t_create_new_network_bridge_incusbr0)
        -   [[5.4.2] [incus-user]](#incus-user)
        -   [[5.4.3] [IPv6]](#IPv6)
        -   [[5.4.4] [Launching containers fails with \"dnsmasq: bad command line options: bad dhcp-range\"]](#Launching_containers_fails_with_.22dnsmasq:_bad_command_line_options:_bad_dhcp-range.22)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installing]

To install incus, issue:

`root `[`#`]`emerge --ask app-containers/incus`

Pay attention to kernel config requirement messages when installing Incus. Missing kernel features may mean the program won\'t function at all. Also pay attention to any optional features printed by [emerge] after successful installation.

In a stable system, currently Incus and some of its dependencies must be allowed via [ACCEPT_KEYWORDS](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS "ACCEPT KEYWORDS").

### [Configuring service files]

Defaults should work just fine, but modifications for Incus\'s service can be made.

#### [OpenRC]

**Edit** [/etc/conf.d/incus]

#### [systemd]

`root `[`#`]`systemctl edit --full incus.service`

### [Adding a user to correct groups]

Incus can be run as a regular user, or as a root. To have a user capable of launching and operating containers, add the user to the `incus` group. For example, to add a user named **larry** into `incus` group, issue:

`root `[`#`]`usermod --append --groups incus larry`

There\'s also `incus-admin` group for **incus admin** commands. It\'s recommended that only root is able to call these, and not regular users.

### [Configure idmaps]

Incus uses idmaps to give non-root users root access inside containers. Easy way to get usable idmaps is to simply issue:

`root `[`#`]`echo "root:1000000:1000000000" | tee -a /etc/subuid /etc/subgid`

** Important**\
There\'s a \"bug\" in incus-0.4 regarding how incus-user is able to map ids, please check [Troubleshooting#Fresh-containers-fail-to-start-with-a-cryptic-\"newuidmap-failed-to-write-mapping\"-message](https://wiki.gentoo.org/wiki/Incus#Fresh_containers_fail_to_start_with_a_cryptic_.22newuidmap_failed_to_write_mapping.22_message "Incus").

### [Start the daemons]

#### [OpenRC]

##### [With incus-user configured]

When running incus as a regular user, the `incus-user` service needs to be started as well as main incus service.

`root `[`#`]`rc-service incus start `

`root `[`#`]`rc-service incus-user start`

To have the services automatically start at boot:

`root `[`#`]`rc-update add incus default `

`root `[`#`]`rc-update add incus-user default`

##### [Without incus-user configured]

If only using container through the root user, only incus main service needs to be started.

`root `[`#`]`rc-service incus start `

`root `[`#`]`rc-update add incus default`

#### [systemd]

##### [With incus-user configured]

When running incus as a regular user, the `incus-user` service needs to be started as well as main incus service.

`root `[`#`]`systemctl start incus `

`root `[`#`]`systemctl start incus-user`

To have the services automatically start at boot:

`root `[`#`]`systemctl enable incus `

`root `[`#`]`systemctl enable incus-user`

** Note**\
Note that there\'s also a **incus-startup** service that can be used instead of main **incus** service.

### [Migrating from LXD]

#### [][With the \'lxd-to-incus\' tool]

Incus ships with a tool called [lxd-to-incus] that can be used to convert an existing LXD system to Incus. If using this tool, Incus does not need to be initialized to get it running, but the main service needs to be started. The tool currently works with LXD-5.0 (LTS), LXD-5.18, LXD-5.19 and LXD-5.20.

Due to the way LXD and Incus works, it may be necessary to add users to the `incus-admin` group to see their LXD containers after migration.

Check that both Incus and LXD works before starting with

`root `[`#`]`incus info `

`root `[`#`]`lxc info`

[lxd-to-incus] tool will do a dry-run before applying any changes. In case of errors, no data will be migrated.

** Important**\
All containers are stopped before migration so make sure no important tasks are running - and plan for some downtime just in case!

`root `[`#`]`lxd-to-incus`

After a successful migration, Incus is ready for use!

#### [Manual migration]

It\'s possible to add local [lxd] image storage as a \"remote\", with [incus remote add] then manually [incus copy] or [incus move] to a new [incus] storage pool. **Note** that the containers need to be stopped for this to work!

** Important**\
Incus needs to be initialized first before manual migration can work, check [initializing Incus](https://wiki.gentoo.org/wiki/Incus#Initializing_Incus "Incus").

##### [][Local (single-host) system]

In this example both [incus] and [lxd] are installed on a single-host system.

First both [incus] and [lxd] must be made to allow connections. This operation can be done either-way, so it\'s possible to add incus as remote and move from local lxd to remote incus, or by adding lxd as remote and moving from remote lxd to local incus.

`user `[`$`]`incus config set core.https_address :8443 `

`user `[`$`]`lxc config set core.https_address :8444`

In this example, LXD\'s image pool is added as a remote and then LXD container is copied under [incus].

`user `[`$`]`incus remote add my-lxd unix:///var/lib/lxd/unix.socket `

`user `[`$`]`incus remote list`

LXD\'s containers and virtual machines should now be visible for [incus]:

`user `[`$`]`incus list my-lxd:`

Copy your desired `my-important-container` from LXD to incus.

`user `[`$`]`incus copy my-lxd:my-important-container local:`

Use `copy` or `move`. Note that the source container **must be stopped**!

Disable TLS access when you\'re done:

`user `[`$`]`lxc config unset core.https_address `

`user `[`$`]`incus config unset core.https_address`

\

##### [Public system]

Launching or copying from an already public image hosting system shouldn\'t change from how you normally operate. Use [lxd publish] to set your images visible.

### [Initializing Incus]

** Important**\
If you\'re migrating from LXD to Incus, use the **lxd-to-incus** tool as guided above, and **don\'t** initialize Incus here!

This needs to be done once after Incus has been installed. Simply issue

`root `[`#`]`incus admin init --minimal`

to initialize Incus with default settings. This will fit most setups, and can be re-configured through [incus admin] and [incus profile] later.

To edit the defaults, issue:

`root `[`#`]`incus admin init`

## [Configuration]

### [Profile]

Incus has a top-level profile which the containers can inherit, and which is accessible through

`user `[`$`]`incus profile`

command.

`user `[`$`]`incus profile list `

`user `[`$`]`incus profile show default `

`user `[`$`]`incus profile edit default`

Individual containers can be configured likewise with

`user `[`$`]`incus config show my-container `

`user `[`$`]`incus config edit my-container`

Custom profiles can be created and inherited for containers. Example shown in [Launching containers](https://wiki.gentoo.org/wiki/Incus#Launching_containers "Incus").

** Tip**\
Take a look at [upstream\'s documentation about \"project restrictions\"](https://linuxcontainers.org/incus/docs/main/reference/projects/#project-restrictions) to control user access to actions like snapshot creation or import/export.

### [Network]

When initializing Incus with the [incus admin init] command, it should create working network properties on the fly. Network can be configured manually afterwards, too.

`user `[`$`]`incus network list`

`user `[`$`]`incus network create incusbr0 `

`user `[`$`]`incus profile device remove default eth0 `

`user `[`$`]`incus profile device add default eth0 nic network=incusbr0 name=eth0`

etc. See [upstream documentation](https://linuxcontainers.org/incus/docs/main/networks/) for more details.

## [Usage]

### [Finding pre-built container images]

Upstream offers [variety of pre-built container and virtual machine images](https://images.linuxcontainers.org/) under the default `images:` remote repository. To list all images, please visit [website](https://images.linuxcontainers.org/) or find the images through incus:

`user `[`$`]`incus image list images:`

Find a specific distribution:

`user `[`$`]`incus image list images:gentoo`

    +-------------------------------+--------------+--------+---------------------------------------+--------------+-----------------+------------+-------------------------------+
    |             ALIAS             | FINGERPRINT  | PUBLIC |              DESCRIPTION              | ARCHITECTURE |      TYPE       |    SIZE    |          UPLOAD DATE          |
    +-------------------------------+--------------+--------+---------------------------------------+--------------+-----------------+------------+-------------------------------+
    | gentoo/openrc (3 more)        | 224df928674f | yes    | Gentoo current amd64 (20231226_16:07) | x86_64       | VIRTUAL-MACHINE | 1056.96MiB | Dec 26, 2023 at 12:00am (UTC) |
    +-------------------------------+--------------+--------+---------------------------------------+--------------+-----------------+------------+-------------------------------+
    | gentoo/openrc (3 more)        | 31864611e02c | yes    | Gentoo current amd64 (20231226_16:07) | x86_64       | CONTAINER       | 341.64MiB  | Dec 26, 2023 at 12:00am (UTC) |
    +-------------------------------+--------------+--------+---------------------------------------+--------------+-----------------+------------+-------------------------------+
    | gentoo/openrc/arm64 (1 more)  | 7bca8c9e9146 | yes    | Gentoo current arm64 (20231226_16:07) | aarch64      | CONTAINER       | 317.95MiB  | Dec 26, 2023 at 12:00am (UTC) |
    +-------------------------------+--------------+--------+---------------------------------------+--------------+-----------------+------------+-------------------------------+
    | gentoo/systemd (3 more)       | 5f36c387c427 | yes    | Gentoo current amd64 (20231226_16:07) | x86_64       | CONTAINER       | 360.51MiB  | Dec 26, 2023 at 12:00am (UTC) |
    +-------------------------------+--------------+--------+---------------------------------------+--------------+-----------------+------------+-------------------------------+
    | gentoo/systemd (3 more)       | 6a8e0e148c35 | yes    | Gentoo current amd64 (20231226_16:07) | x86_64       | VIRTUAL-MACHINE | 1093.95MiB | Dec 26, 2023 at 12:00am (UTC) |
    +-------------------------------+--------------+--------+---------------------------------------+--------------+-----------------+------------+-------------------------------+
    | gentoo/systemd/arm64 (1 more) | 68463fabbf65 | yes    | Gentoo current arm64 (20231226_16:07) | aarch64      | CONTAINER       | 333.32MiB  | Dec 26, 2023 at 12:00am (UTC) |
    +-------------------------------+--------------+--------+---------------------------------------+--------------+-----------------+------------+-------------------------------+

A simple [grep] can also be paired with the listing. The `TYPE` field will show whether a virtual machine image is available.

### [Launching containers]

To launch a container from upstream image server, check the `ALIAS` field an issue for example:

`user `[`$`]`incus launch images:gentoo/openrc my-gentoo-container`

which will download, unpack, and start an OpenRC-based Gentoo container. Log in to the container with:

`user `[`$`]`incus exec my-gentoo-container bash`

To edit container\'s config, first stop the container and then edit its config:

`user `[`$`]`incus stop my-gentoo-container `

`user `[`$`]`incus config edit my-gentoo-container`

If the container can\'t be stopped, please see [Troubleshooting#Containers or virtual machines (OpenRC) not shutting down properly](https://wiki.gentoo.org/wiki/Incus#Containers_or_virtual_machines_.28OpenRC.29_not_shutting_down_properly "Incus")

Find available containers:

`user `[`$`]`incus list `

`user `[`$`]`incus start my-gentoo-container `

`user `[`$`]`incus exec my-gentoo-container bash`

Launch a container with a specific, unique profile:

`user `[`$`]`incus launch images:gentoo/openrc -p my-predefined-profile my-gentoo-container-with-custom-profile`

\

#### [Limiting container resources]

Incus can allocate resources to containers in many different ways. Here are only few examples listed. Check [upstream documentation](https://linuxcontainers.org/incus/docs/main/reference/instance_options/#instance-options-limits) for everything: CPU, memory, disk I/O, process etc limits.

##### [CPU]

Allow specific container to only use 8 cores.

`user `[`$`]`incus config set my-container limits.cpu 8`

Or allow it to only use 80 % of CPU capability:

`user `[`$`]`incus config set my-container limits.cpu.allowance 80%`

And give it the lowest CPU priority:

`user `[`$`]`incus config set my-vm limits.cpu.priority 0`

##### [Memory]

Give the container 8 GB of memory:

`user `[`$`]`incus config set my-container limits.memory 8GB`

** Note**\
Also accepts `MB` as a value.

#### [Launching virtual machines]

Incus can use [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") to run virtual machines. Running and operating virtual machines requires [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") to be installed, with the following USE-flags enabled: `spice`, `usbredir`, `virtfs` along with [[[app-cdr/cdrtools]](https://packages.gentoo.org/packages/app-cdr/cdrtools)[]] for its **mkisofs** binary.

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu spice usbredir virtfs

Note: You might also need to disable `pin-upstream-blobs` USE flag from Qemu to allow installation of newer [[[sys-firmware/edk2-bin]](https://packages.gentoo.org/packages/sys-firmware/edk2-bin)[]].

[FILE] **`/etc/portage/sets/optfeature`**

    # incus vm support
    app-cdr/cdrtools
    app-emulation/qemu

`root `[`#`]`emerge --ask app-emulation/qemu`

The following kernel options are needed: `CONFIG_MACVTAP`, `CONFIG_VHOST_VSOCK`, `CONFIG_KVM` and either `CONFIG_KVM_AMD` or `CONFIG_KVM_INTEL` depending on the system\'s CPU. Please see [QEMU#Kernel](https://wiki.gentoo.org/wiki/QEMU#Kernel "QEMU") for more accurate config options. You\'ll also need to enable virtualization in your BIOS, otherwise you\'ll get an error message of \"KVM: disabled by BIOS\". Basically, make sure [/dev/kvm] exists before trying to launch a virtual machine. And setup QEMU properly so it works.

For graphical sessions to work in a virtual machine, i.e. logging to a desktop, either [[[app-emulation/virt-viewer]](https://packages.gentoo.org/packages/app-emulation/virt-viewer)[]] or [[[net-misc/spice-gtk]](https://packages.gentoo.org/packages/net-misc/spice-gtk)[]] needs to be installed.

The [default image server](https://images.linuxcontainers.org/) already hosts many virtual machine alternatives, even pre-configured desktop VM images. When listing upstream images through

`user `[`$`]`incus image list images:`

as shown before, check the `TYPE` field that a virtual machine is available. Many pre-configured desktop images can be found with a \"desktop\" in their description.

Virtual machines can be launched in a similar manner to containers, just append the `--vm` flag to the command:

`user `[`$`]`incus launch images:gentoo/openrc my-gentoo-vm --vm`

If everything is working properly, the VM will be started upon launching it. If not, check [Troubleshooting](https://wiki.gentoo.org/wiki/Incus#Troubleshooting "Incus").

Access the shell similarly with

`user `[`$`]`incus exec my-gentoo-vm bash`

A graphical virtual machine session can be opened with

`user `[`$`]`incus console my-gentoo-vm --type=vga`

Note that it requires a GUI-capable program to be installed. See options above.

##### [Limiting virtual machine resources]

Allocating CPU and memory resources for VMs works the same way as for containers. Please see [Limiting container resources](https://wiki.gentoo.org/wiki/Incus#Limiting_container_resources "Incus").

** Note**\
By default VMs are very limited for CPU and memory and it\'s recommended to raise them before trying to use those VMs.

##### [Growing default disk size]

Simply the following should work when the VM is **off**:

`user `[`$`]`incus config device set my-vm root size=20GB`

These **profile** settings can be used to create VMs with bigger disk sizes. Make sure the profile is inherited by the VM in question.

`user `[`$`]`incus profile show bigger-vm-disk`

    config:
    description: VM Profile for a bigger root disk
    devices:
      root:
        path: /
        pool: default
        size: 50GB
        type: disk

`user `[`$`]`incus config show my-vm`

    ...
    profiles:
    - default
    - bigger-vm-disk
    ...

If it does not, the manual method below is a more sureway to get it done:

On the **host** resize image with [qemu-img].

`root `[`#`]`cd /var/lib/incus/virtual-machines/my-vm/ `

`root `[`#`]`qemu-img resize root.img 20G`

** Note**\
Depending on image, [qemu-img resize -f raw root.img 20G] might be required instead.

Now move on to the virtual machine.

`user `[`$`]`incus start my-vm `

`user `[`$`]`incus exec my-vm bash`

`my-vm #``emerge -av sys-fs/growpart `

`my-vm #``df -h `

`my-vm #``growpart /dev/sda 2 `

`my-vm #``resize2fs /dev/sda2 `

`my-vm #``df -h`

\

##### [][Red Hat / CentOS variants]

Due to RHEL/CentOS based distributions not shipping the `9p` driver, workarounds are needed to launch their virtual machines.

`user `[`$`]`incus create images:centos/9-Stream my-centos-vm --vm `

`user `[`$`]`incus config device add my-centos-vm agent disk source=agent:config `

`user `[`$`]`incus start my-centos-vm`

A profile can be created with this config pre-defined, then vm\'s launched using that profile:

`user `[`$`]`incus profile create rhel-vm-agent `

`user `[`$`]`incus profile device add rhel-vm-agent agent disk source=agent:config `

`user `[`$`]`incus launch images:centos/9-Stream my-centos-vm-2 --vm -p default -p rhel-vm-agent`

#### [Making custom container images]

[Distrobuilder](https://wiki.gentoo.org/wiki/Distrobuilder "Distrobuilder") can be used to make a custom container or virtual machine images. Please see the wiki page for guidance.

## [Advanced usage]

### [Container backups]

TODO

### [][Move/copy containers between projects]

Let\'s say you later decided to start using Incus by utilizing the `incus-user` approach, but all your containers are migrated/created with `incus-admin` privileges. You can move/copy these containers under your user\'s profile. First make sure `incus-user` is initialized, and working properly on your user. Then identify the projects:

`root `[`#`]`incus project list`

    +-------------------+--------+----------+-----------------+-----------------+----------+---------------+---------------------------------------------+---------+
    |       NAME        | IMAGES | PROFILES | STORAGE VOLUMES | STORAGE BUCKETS | NETWORKS | NETWORK ZONES |                 DESCRIPTION                 | USED BY |
    +-------------------+--------+----------+-----------------+-----------------+----------+---------------+---------------------------------------------+---------+
    | default (current) | YES    | YES      | YES             | YES             | YES      | YES           | Default Incus project                       | 10      |
    +-------------------+--------+----------+-----------------+-----------------+----------+---------------+---------------------------------------------+---------+
    | user-1000         | YES    | YES      | YES             | YES             | NO       | YES           | User restricted project for "larry" (1000) | 4       |
    +-------------------+--------+----------+-----------------+-----------------+----------+---------------+---------------------------------------------+---------+

Check the container names:

`root `[`#`]`incus list`

Move or copy the desired containers under your user\'s project, therefore giving your user the full access to the moved/copied containers:

** Important**\
The containers need to be stopped before this can be attempted!

`root `[`#`]`incus copy --target-project user-1000 source-container target-container`

Fix any errors if there are some. After successful operation, the container should be visible in your user\'s project:

`user `[`$`]`incus list`

### [Multi-host setup]

TODO

### [Pulseaudio in a container]

TODO

### [][Sharing files/directories between container and host]

With `incus-user` your project should already have default idmaps solved. If it does not, add the following config either to your individual containers, or to the profile you\'re using.

`user `[`$`]`incus profile edit default`

    config:
      raw.idmap: |-
        uid 1000 1000
        gid 1000 1000

Where the `uid` and `gid` values match your user\'s [id -u] and [id -g] values. These need to be present in hosts [/etc/subuid] and [/etc/subgid] files too:

[FILE] **`/etc/subuid`**

    root:1000000:1000000000
    incus:1000000:1000000000
    root:1000:1
    incus:1000:1

[FILE] **`/etc/subgid`**

    root:1000000:1000000000
    incus:1000000:1000000000
    root:1000:1
    incus:1000:1

Share directories with:

`user `[`$`]`incus config edit my-container`

    devices:
      containerscripts:
        path: /root/bin
        source: /home/larry/bin/containerscripts
        type: disk
      distfiles:
        path: /var/cache/distfiles/
        source: /var/cache/distfiles/
        type: disk

If you get a message saying \"Disk source path not allowed\", please check the [Troubleshooting section](https://wiki.gentoo.org/wiki/Incus#Adding_a_disk_device_with_incus-user_fails_to_.22Disk_source_path_not_allowed.22 "Incus") for it.

### [systemd containers on OpenRC host]

First **openrc** must be configured to be in `hybrid` or `unified` mode.

[FILE] **`/etc/rc.conf`**

    rc_cgroup_mode="hybrid"

    rc_cgroup_controllers="yes"
    rc_controller_cgroups="yes"

Reboot is a must if you made changes here.

Incus\'s default init.d file should already create the required [/sys/fs] mounts,

[FILE] **`/etc/init.d/incus`**

    ...
    install -d /sys/fs/cgroup/systemd --group incus-admin --owner root
    mount -t cgroup -o none,name=systemd systemd /sys/fs/cgroup/systemd
    ...

### [X and Wayland apps in a container]

For X applications, edit the container config with:

`user `[`$`]`incus config edit my-container`

    config:
      environment.DISPLAY: :0.0
    ...
    devices:
      X0:
        path: /tmp/.X11-unix
        source: /tmp/.X11-unix
        type: disk
      mygpu:
        gid: "1000"
        type: gpu
        uid: "1000"

Where `environment.DISPLAY` is the value of your hosts `$DISPLAY` env value. gid and uid should match your [id -g] and [id -u] respectively. With Xorg you\'ll also need to allow connections from container by using [xhost +local:].

Wayland is a bit trickier. Many programs will disallow running wayland as root, therefore you\'ll need to create a new user to the container, and map that user\'s subgid and subid in your host.

`root `[`#`]`echo "gui:1000:1" `

`root `[`#`]` sudo tee -a /etc/subuid /etc/subgid`

Note: the id (1000) should match your user\'s [id -g] and [id -u] values.

Log in to the container to create the new user, then logout:

`user `[`$`]`incus start my-container `

`user `[`$`]`incus exec my-container bash`

`my-container #``useradd gui`

`my-container #``logout`

`user `[`$`]`incus stop my-container`

Edit your container, or profile with:

`user `[`$`]`incus config edit my-container`

      mygpu:
        gid: "1000"
        type: gpu
        uid: "1000"
      xdgruntimedir:
        path: /home/gui/.xdg_runtime_dir
        source: /run/user/1000
        type: disk

Where the id, gid and [/run/user/1000] needs to match your hosts user\'s [id -g] and [id -u].

Start your container:

`user `[`$`]`incus start my-container`

`my-container #``su gui`

`my-container #``cd ~ `

`my-container #``vim ~/.profile`

[FILE] **`/home/gui/.profile`**

    export XDG_RUNTIME_DIR=/home/gui/.xdg_runtime_dir
    export WAYLAND_DISPLAY=wayland-0
    export QT_QPA_PLATFORM=wayland
    export DISPLAY=:0.0

Now inside your container the **gui** user can launch X or wayland applications. On Wayland host, [Xwayland :0.0] needs to be launched before X applications can work from containers. See also [Xwayland -help] for more parameters, like `-geometry`. Alternatively, try [Xephyr]: [Xephyr -br -ac -noreset -screen 1920x1080 :0.0]

## [Troubleshooting]

First things to do when facing problems is to check the containers log, incus\'s log and system log.

`user `[`$`]`incus start <instance_name> --debug`

`user `[`$`]`incus info <instance_name> --show-log`

Attach immediately to systart:

`user `[`$`]`incus start <instance_name> ; incus console --show-log <instance_name>`

By default incus\'s logs can be found from [/var/log/incus/] - this can also be modified from [conf.d] and service files.

[Upstream discussion forum](https://discuss.linuxcontainers.org) is a great resource for finding answers to many different kind of issues.

Try also calling:

`root `[`#`]`lxc-checkconfig`

to find out any obvious missing kernel configuration bits. Installing [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] and booting into that, to rule out any kernel-related errors could help.

### [][Adding a disk device with incus-user fails to \"Disk source path not allowed\"]

With `incus-user` by default the disk access is restricted. Check if this is the cause:

`user `[`$`]`incus project get user-1000 restricted.devices.disk.paths`

And if yes, unset or edit it:

`user `[`$`]`incus project unset user-1000 restricted.devices.disk.paths`

`root `[`#`]`incus project set user-1000 restricted.devices.disk.paths "/home/larry,/var/cache/distfiles,/tmp/.X11-unix,/run/user/1000"`

### [][Containers or virtual machines (OpenRC) not shutting down properly]

If the container freezes during the stop command with

`user `[`$`]`incus stop my-container`

while using OpenRC, try to turn it off directly with [poweroff]:

`user `[`$`]`incus exec my-container -- poweroff`

If that works, edit the [/etc/inittab] file **in the container** adding following part:

[FILE] **`/etc/inittab`**

    pf:12345:powerwait:/sbin/halt

Shutdown the container with [poweroff], and next time it is booted, the container should work like normal and [incus stop] should work as expected. Be careful when doing world updates to not blindly merge changes to [/etc/inittab].

### [][Fresh containers fail to start with a cryptic \"newuidmap failed to write mapping\" message]

** Important**\
This should be fixed in incus \>=0.5, as it got completely new logic in handling the subuid/subgid ranges. When using incus \>=0.5 **completely clean** the subuid/subgid files first, only leaving `root:1000000:1000000000` in there! Then work adding whatever is needed. `incus-user` will automatically idmap your user\'s ID\'s to containers.

This is an unfortunate and annoying bug when using incus-user. The easiest and fastest way to \"fix\" it is to issue [incus profile unset default raw.idmap] and re-launching the container with a new name, since idmaps are issued when the container is spawned. Make sure to fix the profile you\'re using, or make sure the new container will inherit the `default` profile.

If `raw.idmap`s are desired, another way is to carefully observe the numerical idmaps in the error message, and allow them manually in [/etc/lxc/default], [/etc/subuid] and [/etc/subgid] files. For example, these could look like:

[FILE] **`/etc/lxc/default`**

    lxc.idmap = u 0 100000 1000
    lxc.idmap = g 0 100000 1000
    lxc.idmap = u 1000 1000 1
    lxc.idmap = g 1000 1000 1
    lxc.idmap = u 1001 101001 0
    lxc.idmap = g 1001 101001 0
    lxc.idmap = u 1001 1001 1
    lxc.idmap = g 1001 1001 1
    lxc.idmap = u 1002 101002 0
    lxc.idmap = g 1002 101002 0
    lxc.idmap = u 1002 1002 1
    lxc.idmap = g 1002 1002 1
    lxc.idmap = u 1003 101003 0
    lxc.idmap = g 1003 101003 0
    lxc.idmap = u 1003 1003 1
    lxc.idmap = g 1003 1003 1

[FILE] **`/etc/subuid`**

    root:1000:1
    root:1001:1
    root:1002:1
    root:1003:1
    root:100000:65536
    incus:100000:65536

[FILE] **`/etc/subgid`**

    root:1000:1
    root:1001:1
    root:1002:1
    root:1003:1
    root:100000:65536
    incus:100000:65536

** Important**\
After editing these files, the **incus** and **incus-user** services must be restarted!

### [Various dnsmasq related issues]

#### [][Can\'t create new network bridge incusbr0]

Most likely wrongly configured [/etc/dnsmasq.conf] - check the file\'s configuration, or create the network bridge manually:

`user `[`$`]`incus network create incusbr0 ipv4.address=192.168.100.1/24 ipv6.address=none ipv4.nat=yes ipv4.dhcp=yes ipv4.dhcp.ranges=192.168.100.1-192.168.100.100,infinite ipv4.dhcp.gateway=192.168.100.1`

#### [incus-user]

When opting to use `incus-user`, if the user can\'t use [incus] command it may be related to dnsmasq permissions. Add the user to dnsmasq group:

`root `[`#`]`usermod --append --groups dnsmasq larry`

**Relog/Reboot**, just make sure the user is in the group!

`user `[`$`]`groups`

    ... incus dnsmasq ...

#### [IPv6]

When primarily using `ipv6`, make sure [[[net-dns/dnsmasq]](https://packages.gentoo.org/packages/net-dns/dnsmasq)[]] is built with the `+ipv6` use flag.

#### [][Launching containers fails with \"dnsmasq: bad command line options: bad dhcp-range\"]

Most likely wrongly configured [/etc/dnsmasq.conf] - check the file\'s configuration.

[FILE] **`/etc/dnsmasq.conf`**

    bind-interfaces
    except-interface=incusbr0
    dhcp-range=192.168.100.1,192.168.100.100,infinite

## [See also]

-   [Incus/Gentoo Github pullrequest testing](https://wiki.gentoo.org/wiki/Incus/Gentoo_Github_pullrequest_testing "Incus/Gentoo Github pullrequest testing") --- easy and automated way for testing ebuild contributions via [Gentoo\'s Github mirror](https://github.com/gentoo/gentoo) that\'s based on [Incus]
-   [LXD](https://wiki.gentoo.org/wiki/LXD "LXD") --- a system container manager (original project, of which Incus is a fork)
-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.

## [External resources]

-   [First Steps with Incus.](https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/)
-   [Incus\'s upstream discussion site, support forums etc.](https://discuss.linuxcontainers.org/)
-   [Youtube channel focusing on using and developing Incus.](https://www.youtube.com/@TheZabbly)