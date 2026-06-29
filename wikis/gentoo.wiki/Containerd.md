[[]][Home](https://containerd.io/)

[[]][Official documentation](https://containerd.io/docs/main/)

[[]][Package information](https://packages.gentoo.org/packages/app-containers/containerd)

[[]][Wikipedia](https://en.wikipedia.org/wiki/containerd "wikipedia:containerd")

[[]][GitHub](https://github.com/containerd/containerd)

[[]][Bugs (upstream)](https://github.com/containerd/containerd/issues)

**containerd** is an implementation of the CNCF container runtime interface (CRI) often used along with [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") and [Kubernetes](https://wiki.gentoo.org/wiki/Kubernetes "Kubernetes").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [OCI Runtime]](#OCI_Runtime)
        -   [[2.2.1] [Default: runc]](#Default:_runc)
        -   [[2.2.2] [Alternative: NVIDIA]](#Alternative:_NVIDIA)
        -   [[2.2.3] [Alternative: crun]](#Alternative:_crun)
        -   [[2.2.4] [Alternative: gVisor]](#Alternative:_gVisor)
        -   [[2.2.5] [Alternative: Kata Containers]](#Alternative:_Kata_Containers)
    -   [[2.3] [Service]](#Service)
        -   [[2.3.1] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-containers/containerd](https://packages.gentoo.org/packages/app-containers/containerd) [[]] [A daemon to control runC]

  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+cri`](https://packages.gentoo.org/useflags/+cri)                     Support for Kubernetes CRI
  [`+seccomp`](https://packages.gentoo.org/useflags/+seccomp)             Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)             Enable support for the AppArmor application security system
  [`btrfs`](https://packages.gentoo.org/useflags/btrfs)                   Support for BTRFS snapshot driver
  [`device-mapper`](https://packages.gentoo.org/useflags/device-mapper)   Support for device mapper snapshot driver
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 00:57] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-containers/containerd`

### [Additional software]

containerd itself implements the CNCF container runtime interface (CRI), which makes it a viable backend for some frontends:

-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") always uses containerd.
-   [nerdctl](https://wiki.gentoo.org/index.php?title=Nerdctl&action=edit&redlink=1 "Nerdctl (page does not exist)") is compatible to, but much more lightweight than Docker. It is often used in settings where the complexity of Docker is not needed, e.g. in a server setting.
-   [kubelet](https://wiki.gentoo.org/index.php?title=Kubelet&action=edit&redlink=1 "Kubelet (page does not exist)"), a [Kubernetes](https://wiki.gentoo.org/wiki/Kubernetes "Kubernetes") component running on every cluster node, can use containerd as its CRI driver. The interaction between a kubelet and containerd can be debugged with [cri-tools](https://wiki.gentoo.org/index.php?title=Cri-tools&action=edit&redlink=1 "Cri-tools (page does not exist)").

## [Configuration]

### [Files]

containerd is configured via the file [/etc/containerd/config.toml]. It comes with sane defaults that can be viewed with:

`root `[`#`]`containerd dump defaults`

After the first installation of containerd, the config file does not exist and has to be created. With the following snippet, configuration can be modularized in the directory [/etc/containerd/config.d]:

[FILE] **`/etc/containerd/config.toml`Modular configuration**

    version = 3

    imports = ["/etc/containerd/config.d/*.toml"]

### [OCI Runtime]

containerd is capable of managing images, containers, volumes and network interfaces, but it needs an implementation of the OCI runtime specification to actually run, stop and delete containers. After installing those OCI runtimes, they have to be configured in [/etc/containerd/config.toml].

For most of those implementations, the cgroup driver must also be configured to match the host\'s configuration. See the following section for the implementation of choice for both settings.

When multiple OCI runtimes are configured, set a default:

[FILE] **`/etc/containerd/config.d/runtime-default.toml`Default runtime**

    version = 3

    [plugins.'io.containerd.cri.v1.runtime'.containerd]
      default_runtime_name = "crun"

#### [Default: runc]

The reference OCI runtime implementation is [runc](https://github.com/opencontainers/runc). Its package, [[[app-containers/runc]](https://packages.gentoo.org/packages/app-containers/runc)[]], is installed as a dependency of [[[sys-containerd]](https://packages.gentoo.org/packages/sys-containerd)[]].

The following snippet configures runc as a containerd runtime.

[FILE] **`/etc/containerd/config.d/runtime-runc.toml`Configure the runc runtime and its cgroup driver**

    version = 3

    [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc]
      runtime_type = "io.containerd.runc.v2"
      [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc.options]
        SystemdCgroup = true # false if not using systemd

#### [Alternative: NVIDIA]

The NVIDIA container runtime is a small wrapper around runc, used to expose NVIDIA graphics cards to a container.

`root `[`#`]`emerge --ask app-containers/nvidia-container-toolkit`

To use it as a runtime in containerd, run the following:

`root `[`#`]`nvidia-ctk runtime configure --runtime=containerd`

Double-check if the cgroup driver is configured correctly (or at all) in the generated file. Also, checking the config using `containerd config dump > /dev/null` might report errors for unknown keys being used in the NVIDIA runtime. After removing them, the result should look like similar to this:

[FILE] **`/etc/containerd/config.d/99-nvidia.toml`Configure the NVIDIA runtime and its cgroup driver**

    version = 3

    [plugins]
      [plugins."io.containerd.cri.v1.runtime"]
        [plugins."io.containerd.cri.v1.runtime".containerd]
          [plugins."io.containerd.cri.v1.runtime".containerd.runtimes]
            [plugins."io.containerd.cri.v1.runtime".containerd.runtimes.nvidia]
              privileged_without_host_devices = false
              runtime_type = "io.containerd.runc.v2"

              [plugins."io.containerd.cri.v1.runtime".containerd.runtimes.nvidia.options]
                BinaryName = "/usr/bin/nvidia-container-runtime"

#### [Alternative: crun]

[crun](https://github.com/containers/crun) is a drop-in replacement for runc. It is written in C++ and often considered faster.

`root `[`#`]`emerge --ask app-containers/crun`

The following snippet configures crun as a containerd runtime.

[FILE] **`/etc/containerd/config.d/runtime-crun.toml`Configure the crun runtime and its cgroup driver**

    version = 3

    [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.crun]
      runtime_type = "io.containerd.runc.v2"

      [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.crun.options]
        BinaryName = "/usr/bin/crun"
        SystemdCgroup = true # false if not using systemd

#### [Alternative: gVisor]

[gVisor](https://gvisor.dev/) intercepts some syscalls to replace them with userspace implementations. Its OCI runtime is called runsc.

gVisor is currently not available as a Gentoo package. After installing it manually, use the following snippet to configure gVisor as a containerd runtime.

[FILE] **`/etc/containerd/config.d/runtime-gvisor.toml`Configure the gVisor runtime and its cgroup driver**

    version = 3

    [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.gvisor]
      runtime_type = "io.containerd.runsc.v1"

      [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.gvisor.options]
        SystemdCgroup = true # false if not using systemd

#### [Alternative: Kata Containers]

[Kata Containers](https://katacontainers.io/) runs each container in a lightweight VM. Since Kata Containers do not share a kernel with the host system, no cgroup driver has to be configured.

Kata Containers is currently not available as a Gentoo package. After installing it manually, use the following snippet to configure Kata Containers as a containerd runtime.

[FILE] **`/etc/containerd/config.d/runtime-kata.toml`Configure the Kata Containers runtime**

    version = 3

    [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.kata]
      runtime_type = "io.containerd.kata.v2"

### [Service]

#### [systemd]

Make sure the service is started now, and automatically after boots:

`root `[`#`]`systemctl enable --now containerd.service`

After changing the configuration, check for syntax errors in the config file:

`root `[`#`]`containerd config dump > /dev/null`

Fix all reported errors and repeat until none are left, then restart the service:

`root `[`#`]`systemctl restart containerd.service`

## [Usage]

** Note**\
Even though containerd comes with a CLI frontend, interacting with it is usually done with a higher-level tool like [nerdctl](https://wiki.gentoo.org/index.php?title=Nerdctl&action=edit&redlink=1 "Nerdctl (page does not exist)"), [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") or [Kubernetes](https://wiki.gentoo.org/wiki/Kubernetes "Kubernetes"). [ctr] is primarily used to debug containerd itself.

### [Invocation]

List containers running in namespace `moby` (used by [Docker](https://wiki.gentoo.org/wiki/Docker "Docker")):

`user `[`$`]`ctr -n moby c ls`

    CONTAINER                                                           IMAGE    RUNTIME
    2724bfeaf88c09b1e96ef65529dbbdfaecc9008cfb061996ffc482d94c974095    -        io.containerd.runc.v2

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-containers/containerd`

## [See also]

-   [CRI-O](https://wiki.gentoo.org/index.php?title=CRI-O&action=edit&redlink=1 "CRI-O (page does not exist)")
-   [runc](https://wiki.gentoo.org/index.php?title=Runc&action=edit&redlink=1 "Runc (page does not exist)")
-   [nerdctl](https://wiki.gentoo.org/index.php?title=Nerdctl&action=edit&redlink=1 "Nerdctl (page does not exist)")
-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") --- a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system
-   [Kubernetes](https://wiki.gentoo.org/wiki/Kubernetes "Kubernetes") --- open-source system for automating deployment, scaling, and management of containerized applications