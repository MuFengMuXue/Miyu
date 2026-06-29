This page contains [[changes](https://wiki.gentoo.org/index.php?title=Kubernetes&diff=1441798)] which are not marked for translation.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Kubernetes&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://kubernetes.io/)

[[]][Official documentation](https://kubernetes.io/docs/home/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Kubernetes "wikipedia:Kubernetes")

**Kubernetes**, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications.

This article outlines two approaches for running a Kubernetes cluster:

-   via **[minikube](https://minikube.sigs.k8s.io/)** to get started, great for learning Kubernetes from a user perspective (easy), or
-   via **[kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)**, an admin tool for cluster nodes that is part of Kubernetes itself (moderate to difficult).

Note that other approaches are available, like [kOps](https://kops.sigs.k8s.io/) to set up a cluster when a cloud API is available, or [Kubespray](https://kubespray.io/) to set up a cluster using [Ansible](https://wiki.gentoo.org/wiki/Ansible "Ansible").

## Contents

-   [[1] [Kubernetes architecture]](#Kubernetes_architecture)
-   [[2] [Kubernetes via minikube]](#Kubernetes_via_minikube)
-   [[3] [Kubernetes via kubeadm]](#Kubernetes_via_kubeadm)
    -   [[3.1] [Preparing the nodes]](#Preparing_the_nodes)
        -   [[3.1.1] [kubelet OpenRC]](#kubelet_OpenRC)
        -   [[3.1.2] [systemd]](#systemd)
    -   [[3.2] [Basic configuration]](#Basic_configuration)
    -   [[3.3] [Initializing the cluster]](#Initializing_the_cluster)
    -   [[3.4] [Adding nodes to the cluster]](#Adding_nodes_to_the_cluster)
    -   [[3.5] [Removal]](#Removal)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Kubernetes architecture]

TBD

Kubernetes groups containers that make up an application into logical units for easy management and discovery and runs them on a Kubernetes cluster. A Kubernetes cluster is made of [two groups of components](https://kubernetes.io/docs/concepts/overview/components/), namely control plane components, which are used to manage the cluster, and node components, which run the workers hosting the applications. Kubernetes requires a [container runtime interface](https://kubernetes.io/docs/concepts/architecture/cri/) (CRI), which is the mechanism for running a container.

## [Kubernetes via `minikube`]

`minikube` requires a \"driver\" in which to run itself and containers. Docker is one such driver, and this example will use it, but just note that other options exist.

`root `[`#`]`emerge --ask sys-cluster/minikube sys-cluster/kubectl app-containers/docker app-containers/docker-cli`

You will need to add your user to the `docker` group.

Then,

`user `[`$`]`minikube start`

You now have a single-node cluster! For example, you should now be able to run `kubectl get pods` to show the current running pods in the `default` namespace. (This will be empty, as there are none to start with.)

** Note**\
Note that while `minikube` is great for learning & local development, it is only capable of single node clusters, or multi-node clusters where all of the \"nodes\" are on the same machine. (For simulating a multi-node cluster.) It does not do multiple nodes where the nodes correspond to multiple real machines or VMs, like a more \"real\" or production-ready cluster might do. For that, see either the `kubeadm` section, or the manual section.

\

## [Kubernetes via [kubeadm]]

In the following instruction we are going to set up single-master multiple-node cluster. It consists of:

1.  Containerd as container runtime - on every node
2.  Kubelet as node (and master) agents - on every node
3.  Kubeadm to set up cluster - on every node
4.  cni-plugins for networking (Optionally) - on every node
5.  Kubectl to control them all - on the user\'s machine

The following components will be automatically installed as kubelet and run as containers:

1.  kube-apiserver
2.  kube-controller-manager
3.  kube-scheduler
4.  etcd
5.  kube-proxy (Optionally)
6.  CoreDNS (Optionally)

Cilium will be considered as a viable option to Kubernetes networking and kube-proxy.

### [Preparing the nodes]

Pick a suitable CRI driver, and follow the instructions on its page, e.g. [containerd](https://wiki.gentoo.org/wiki/Containerd "Containerd"). Pay special attention to the correct configuration of the cgroup driver of the CRI.

Install the main kubeadm-based bootstrap components.

`root `[`#`]`emerge --ask sys-cluster/kubectl sys-cluster/kubeadm`

#### [kubelet OpenRC]

[FILE] **`/etc/conf.d/kubelet`Adapting OpenRC kubelet service to kubeadm**

    ###
    # Kubernetes Kubelet (worker) config
    # This configuration example is tuned for kubeadm
    # Feel free to modify

    # If exists kubeadm-flags.env, then source it to get
    # environment variable $
    if [ -e /var/lib/kubelet/kubeadm-flags.env ]; then
      source /var/lib/kubelet/kubeadm-flags.env;
    fi

    # Pre-defined command-line args for kubeadm
    command_args="--config /var/lib/kubelet/config.yaml \
            --kubeconfig /etc/kubernetes/kubelet.conf \
            --bootstrap-kubeconfig /etc/kubernetes/bootstrap-kubelet.conf \
            $"

#### [systemd]

For [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), kubeadm uses what is called a \"drop-in\" systemd file. See [this page in the Kubernetes documentation](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/#the-kubelet-drop-in-file-for-systemd) for more info.

Usually, the drop-in file is created during the installation of the `kubeadm` package in [/usr/lib/systemd]. This is currently missing, so find the appropriate content in the documentation above, and place it in [/etc/systemd].

[FILE] **`/etc/systemd/system/kubelet.service.d/10-kubeadm.conf`Add overrides to kubelet.service for kubeadm integration**

    [Service]
    Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf"
    Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"
    # This is a file that "kubeadm init" and "kubeadm join" generates at runtime, populating the KUBELET_KUBEADM_ARGS variable dynamically
    EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
    # This is a file that the user can use for overrides of the kubelet args as a last resort. Preferably, the user should use
    # the .NodeRegistration.KubeletExtraArgs object in the configuration files instead. KUBELET_EXTRA_ARGS should be sourced from this file.
    EnvironmentFile=-/etc/sysconfig/kubelet
    ExecStart=
    ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS

Enable the unit, but do not start it.

`root `[`#`]`systemctl enable kubelet.service`

Starting it now would result in a crash loop because essential configuration is missing. kubeadm will configure and start the service later, and issue a warning if the service has not been enabled yet.

### [Basic configuration]

To initialize a cluster with kubeadm, we need to pass some basic configuration. It is recommended to write configuration manifests to a file and pass the file name via `--config`.

Supported kinds are:

-   `InitConfiguration` for node-specific runtime configuration
-   `ClusterConfiguration` for settings regarding the whole cluster
-   `KubeletConfiguration` for settings passed to every kubelet of the cluster
-   `KubeProxyConfiguration` for kube-proxy (if used)

Either `InitConfiguration` or `ClusterConfiguration` is required, so a minimum configuration could look like this:

[FILE] **`/etc/kubernetes/kubeadm-config.yaml`kubeadm config**

    ---
    apiVersion: kubeadm.k8s.io/v1beta4
    kind: ClusterConfiguration
    kubernetesVersion: v1.35.0

** Warning**\
The manifests may contain sensitive information, like bootstrap tokens. The file should be protected from unsolicited reads.

In Kubernetes 1.31+, kubeadm asks the CRI for the cgroup driver to use. For CRIs that do not support the [RuntimeConfig] CRI API, the cgroup driver used by the kubelet should be specified in the `KubeletConfiguration`. Kubernetes 1.37+ will drop support for CRIs that do not support the [RuntimeConfig] CRI API^[\[1\]](#cite_note-1)^. Support was added to [containerd](https://wiki.gentoo.org/wiki/Containerd "Containerd") in version v2.0^[\[2\]](#cite_note-2)^, and to [CRI-O](https://wiki.gentoo.org/index.php?title=CRI-O&action=edit&redlink=1 "CRI-O (page does not exist)") in version 1.28^[\[3\]](#cite_note-3)^.

[FILE] **`/etc/kubernetes/kubeadm-config.yaml`Specifying a cgroup driver**

    <omitted>
    ---
    apiVersion: kubelet.config.k8s.io/v1beta1
    kind: KubeletConfiguration
    cgroupDriver: cgroupfs # if omitted, kubeadm defaults to systemd

### [Initializing the cluster]

Run `kubeadm init` to initialize the cluster:

`root `[`#`]`kubeadm init --config /etc/kubernetes/kubeadm-config.yaml`

    <omitted>
    Your Kubernetes control-plane has initialized successfully!

    To start using your cluster, you need to run the following as a regular user:

The [official troubleshooting page](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/) lists problems that might occur during `kubeadm init`, and how to solve them.

### [Adding nodes to the cluster]

### [Removal]

Before removing a node from its cluster, make sure there are no pods left on the node.

`user `[`$`]`kubectl drain "$(hostname -s)" --ignore-daemonsets`

** Note**\
Replace `$(hostname -s)` with the actual node name if a custom name was specified during `kubeadm init` or `kubeadm join`.

The node should then be safe to remove.

`user `[`$`]`kubectl delete node "$(hostname -s)"`

** Note**\
Replace `$(hostname -s)` with the actual node name if a custom name was specified during `kubeadm init` or `kubeadm join`.

Finally, stop all Kubernetes containers and clean up the file system.

`root `[`#`]`kubeadm reset`

Some running containers might survive the reset. They can usually be identified via the `NAMESPACE` field in the output of

`root `[`#`]`crictl ps -a`

If *every* listed container belongs to the former node, they can be removed with `crictl rm -a`; otherwise remove them separately.

It is now safe to remove the system packages.

`root `[`#`]`emerge --ask --depclean --verbose sys-cluster/kubeadm sys-cluster/kubectl sys-cluster/kubeadm`

Even after running `kubeadm reset`, some traces of `kubeadm init` or `kubeadm join` and the following operation of the cluster will be left on the host. To be extra thorough, the user might want to review and clean up the contents of [/etc/kubernetes] and [/var/lib/kubelet].

In any case, to avoid problems in case this host will be used as a Kubernetes node again later, remove [/etc/cni/net.d].

`root `[`#`]`rm -rf /etc/cni/net.d`

Depending on the selected CNI, some obsolete network interfaces might still remain. The following example has interfaces left that were created by Cilium.

`root `[`#`]`ip link`

    # omitted: loopback and physical interfaces...
    6: cilium_net@cilium_host: <BROADCAST,MULTICAST,NOARP,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP mode DEFAULT group default
        link/ether 4e:e8:a1:fb:54:43 brd ff:ff:ff:ff:ff:ff
    7: cilium_host@cilium_net: <BROADCAST,MULTICAST,NOARP,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP mode DEFAULT group default qlen 1000
        link/ether 22:a9:f3:a1:16:f4 brd ff:ff:ff:ff:ff:ff
    8: cilium_vxlan: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UNKNOWN mode DEFAULT group default
        link/ether 36:5c:a1:7b:ad:ea brd ff:ff:ff:ff:ff:ff
    101: lxcf7ef2b630eac@if100: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP mode DEFAULT group default qlen 1000
        link/ether 7e:26:ac:b0:03:8e brd ff:ff:ff:ff:ff:ff link-netns cni-4c7a741d-7fdc-208c-e035-fcc76352ba7c

They should be safe to remove.

`root `[`#`]`ip link delete cilium_net`

`root `[`#`]`ip link delete cilium_vxlan`

The last remaining interface in the above example is in its own networking namespace; this was used to isolate a pod\'s network from other pods\' and the host\'s networks. Removing the networking namespace will remove the interface, too.

`root `[`#`]`ip netns delete cni-4c7a741d-7fdc-208c-e035-fcc76352ba7c`

## [See also]

-   [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") --- a [container](https://en.wikipedia.org/wiki/Container_(virtualization) "wikipedia:Container (virtualization)")-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") system
-   [LXD](https://wiki.gentoo.org/wiki/LXD "LXD") --- a system container manager
-   [Podman](https://wiki.gentoo.org/wiki/Podman "Podman") --- a daemonless container engine for developing, managing, and running [OCI Containers](https://opencontainers.org/), aiming to be a drop-in replacement for much of [Docker](https://wiki.gentoo.org/wiki/Docker "Docker")

## [References]

1.  [[[↑](#cite_ref-1)] [[https://kubernetes.io/docs/setup/production-environment/container-runtimes/#systemd-cgroup-driver](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#systemd-cgroup-driver) Version 1.36 ]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/containerd/containerd/blob/main/docs/cri/config.md#cgroup-driver](https://github.com/containerd/containerd/blob/main/docs/cri/config.md#cgroup-driver)]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/cri-o/cri-o/pull/7079](https://github.com/cri-o/cri-o/pull/7079)]]