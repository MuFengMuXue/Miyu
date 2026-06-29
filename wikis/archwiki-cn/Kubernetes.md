**翻译状态：**

  * 本文（或部分内容）译自 [Kubernetes](<https://wiki.archlinux.org/title/Kubernetes> "arch:Kubernetes")，最近一次同步于 2025-02-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Kubernetes?diff=0&oldid=823606>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Kubernetes_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 缺少详细提示（在[Talk:Kubernetes](<../zh-cn/Talk:Kubernetes.html>)讨论）

[Kubernetes](<https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/>) (简称k8s)是一套用于自动部署，扩展以及管理容器化应用的开源系统。 

k8s集群由一个[控制平面组件](<https://kubernetes.io/docs/concepts/overview/components/#control-plane-components>)和一个或多个[节点组件](<https://kubernetes.io/docs/concepts/overview/components/#node-components>)构成(每个组件代表一台或多台运行容器运行时和 `kubelet.service` 服务的主机机器)。安装 Kubernetes 有两种选择：一种是更为正统的Kubernetes安装方式（此处所描述的方式），另一种则是使用 [k3s](<https://k3s.io/>)，[kind](<https://kind.sigs.k8s.io/>) 或者 [minikube](<https://archlinux.org/packages/?name=minikube>)包 进行本地安装。 

##  安装

配置一个 Kubernetes 集群的方法有很多，本文将主要介绍如何使用 [kubeadm](<https://archlinux.org/packages/?name=kubeadm>)包 进行配置。 

###  部署工具

#### kubeadm

如果要使用 _kubeadm_ 来引导 Kubernetes 集群，请在每一个节点上[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [kubeadm](<https://archlinux.org/packages/?name=kubeadm>)包 和 [kubelet](<https://archlinux.org/packages/?name=kubelet>)包。 

####  手动配置

如你想要手动创建一个 Kubernetes 集群，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [etcd](<https://aur.archlinux.org/packages/etcd/>)AUR，并安装[软件包组](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "软件包组") [kubernetes-control-plane](<https://archlinux.org/groups/x86_64/kubernetes-control-plane/>)包组 (在控制平面节点) 或 [kubernetes-node](<https://archlinux.org/groups/x86_64/kubernetes-node/>)包组 (在 worker 节点)。 

####  集群管理

要管理一个 Kubernetes 集群，请在控制平面节点和要与集群交互的主机上安装 [kubectl](<https://archlinux.org/packages/?name=kubectl>)包。 

###  容器运行时

控制平面节点和常规 worker 节点都需要一个容器运行时以运行 `kubelet` 实例。 [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [containerd](<https://archlinux.org/packages/?name=containerd>)包 或 [cri-o](<https://archlinux.org/packages/?name=cri-o>)包 来提供一个运行时。 

####  containerd 运行时

有两种方式可以安装 _containerd_ : 

  1. [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [containerd](<https://archlinux.org/packages/?name=containerd>)包 软件包。
  2. 安装非特权模式(rootless)_containerd_ ，你需要安装 [nerdctl-full-bin](<https://aur.archlinux.org/packages/nerdctl-full-bin/>)AUR，其是一个完整的 nerdctl 包（containerd，CNI 插件，和 RootlessKit）。随后你需要运行 `containerd-rootless-setuptool.sh install` 以安装非特权模式 _containerd_ 。

请注意，由于 Arch Linux 使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 作为 init 系统，你需要在部署控制平面之前[选择 systemd cgroup 驱动](<#%E4%B8%BA_containerd_%E9%80%89%E6%8B%A9_cgroup_%E9%A9%B1%E5%8A%A8>)。 

###  (可选) 包管理器

[helm](<https://archlinux.org/packages/?name=helm>)包 是一个用于管理预配置的 Kubernetes 资源的工具，这可能会有所帮助。 

##  配置

集群中的所有节点（控制平面和工作节点）都需要运行一个 `kubelet.service` 实例。 

**提示：** 在启动 `kubelet.service` 或使用 `kubeadm` 之前，请仔细阅读以下小节。

所有提供的 systemd 服务都允许通过环境文件进行命令行参数覆盖： 

  * `kubelet.service`: `/etc/kubernetes/kubelet.env`
  * `kube-apiserver.service`: `/etc/kubernetes/kube-apiserver.env`
  * `kube-controller-manager.service`: `/etc/kubernetes/kube-controller-manager.env`
  * `kube-proxy.service`: `/etc/kubernetes/kube-proxy.env`
  * `kube-scheduler.service`: `/etc/kubernetes/kube-scheduler.env`

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：**

  * 不使用 `kubeadm` 的配置示例，使用 `kube-apiserver.service`、`kube-controller-manager.service`、`kube-proxy.service` 和 `kube-scheduler.service`。
  * 使用 [配置文件](<https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file>) 来进行对 `kubeadm` 的配置。

(在 [Talk:Kubernetes](<../zh-cn/Talk:Kubernetes.html>) 中讨论)

###  禁用交换分区

Kubernetes 目前不支持在系统上启用交换分区。详情请参阅 [KEP-2400: 节点系统交换支持](<https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/2400-node-swap>)。 

有关如何禁用交换分区的说明，请参阅 [Swap#关闭交换分区](<../zh-cn/Swap.html#%E5%85%B3%E9%97%AD%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA> "Swap")。 

###  为 containerd 选择 cgroup 驱动

如要在使用 `runc` 时，同时也在 `/etc/containerd/config.toml` 中使用 `systemd` cgroup 驱动，请设置： 
    
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
      ...
      [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
        SystemdCgroup = true
    
如果 `/etc/containerd/config.toml` 不存在，可以使用[以下命令](<https://github.com/containerd/containerd/blob/main/docs/getting-started.md#customizing-containerd>)生成默认配置： 
    
    # mkdir -p /etc/containerd/
    # containerd config default > /etc/containerd/config.toml
    
请记住[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `containerd.service` 以使更改生效。 

有关是否保留 `cgroupfs` 驱动或使用 `systemd` cgroup 驱动的深入讨论，请参阅[官方文档](<https://kubernetes.io/docs/setup/production-environment/container-runtimes/#cgroup-drivers>)。 

###  选择容器运行时接口 (CRI)

在使用 `kubelet.service` 之前，必须配置并启动[容器运行时](<https://kubernetes.io/docs/setup/production-environment/container-runtimes/>)。 

你需要在创建或加入集群时，将带有容器运行时接口端点的标志 `--cri-socket` 传递给 `kubeadm init` 或 `kubeadm join`。 

例如，如果你选择 [containerd](<https://archlinux.org/packages/?name=containerd>)包 作为 CRI 运行时，则在创建时附带上`--cri-socket`标志： 
    
    kubeadm init --cri-socket /run/containerd/containerd.sock
    
#### Containerd

在 Kubernetes 1.27.4 版本之前，当使用 [containerd](<https://archlinux.org/packages/?name=containerd>)包 作为容器运行时，需要向 `kubeadm init` 或 `kubeadm join` 提供其 CRI 端点。为此，请将其 `--cri-socket` 标志指定为 `/run/containerd/containerd.sock`[[1]](<https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime>)。 
    
    kubeadm join --cri-socket=/run/containerd/containerd.sock
    
在 Kubernetes 1.27.4 版本之后，kubeadm 将自动检测此 CRI，只有在安装了多个 CRI 时才需要 `--cri-socket` 标志。 

#### CRI-O

当使用 [CRI-O](</wzh/index.php?title=CRI-O&action=edit&redlink=1> "CRI-O（页面不存在）") 作为容器运行时，需要向 `kubeadm init` 或 `kubeadm join` 提供其 CRI 端点：`--cri-socket='unix:///run/crio/crio.sock'`

###  选择集群网络参数

####  选择 Pod CIDR 范围

必须为相应的容器运行时配置集群的网络设置。这可以使用 [cni-plugins](<https://archlinux.org/packages/?name=cni-plugins>)包 来完成。 

**Pod CIDR 地址** 指的是分配给 Kubernetes 集群中 Pod 的 IP 地址范围。当 Pod 被调度到集群中的节点上运行时，它们会从此 CIDR 范围中分配 IP 地址。 

**Pod CIDR 范围** 在部署 Kubernetes 集群时指定，并且仅限于集群网络内。它不应与集群中使用的其他 IP 范围（例如如 _service CIDR 范围_ ）重叠。 

你将向 `kubeadm init` 或 `kubeadm join` 传递 `--pod-network-cidr` 标志，并指定虚拟网络的 [CIDR](<https://en.wikipedia.org/wiki/CIDR> "wikipedia:CIDR") 值，以创建或加入集群。 

例如： 
    
    kubeadm init --pod-network-cidr='10.85.0.0/16'
    
会将你的 Kubernetes Pod CIDR 范围设置为 `10.85.0.0/16`。 

####  （可选）选择 API 服务器广播地址

如果你的控制平面节点位于多个子网中（例如，你可能安装了 Tailscale tailnet），在使用 kubeadm init 初始化 Kubernetes 主节点时，你可以使用 `--apiserver-advertise-address` 标志指定 API 服务器将广播的 IP 地址。注意，此 IP 地址应可被集群中的所有节点访问。 

####  （可选）选择其他的节点网络代理提供者

节点代理提供者（如 `kube-proxy`）是在集群中每个节点上运行的网络代理，用于维护节点上的网络规则，以允许从集群内部或外部的网络会话与你的 Pod 进行网络通信。 

默认情况下，[kubeadm](<https://archlinux.org/packages/?name=kubeadm>)包 选择 `kube-proxy` 作为在集群中每个节点上运行的节点代理。 

容器网络接口 (CNI) 插件（如 Cilium）提供了 kube-proxy 的完整替代方案。 

如果你想使用 Cilium 的节点网络代理实现以充分利用 Cilium 的网络策略功能，你应向 `kubeadm init` 传递 `--skip-phases=addon/kube-proxy` 标志，以跳过 kube-proxy 的安装。 

Cilium 将在其安装过程中安装完整的替代方案。详情请参阅 [[2]](<https://docs.cilium.io/en/latest/network/kubernetes/kubeproxy-free/>)。 

##  创建集群

在使用 `kubeadm` [创建新的 Kubernetes 集群](<https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/>)之前，请先[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `kubelet.service`。 

**注意：**`kubelet.service` 会失败（但会重启），直到为其提供配置。

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：**

  * 不使用 `kubeadm` 进行设置的示例，使用 `kube-apiserver.service`、`kube-controller-manager.service`、`kube-proxy.service` 和 `kube-scheduler.service`。
  * 使用 `kubeadm` 进行设置的示例，使用 [配置文件](<https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file>)。

(在 [Talk:Kubernetes](<../zh-cn/Talk:Kubernetes.html>) 中讨论)

###  不使用配置文件的 kubeadm

在使用 `kubeadm` [创建新的 Kubernetes 集群](<https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/>)时，必须先创建一个控制平面，然后其他工作节点才能加入。 

**提示：**

  * 如果集群以后要转换为 [高可用性](<https://en.wikipedia.org/wiki/High_availability> "wikipedia:High availability") 集群（[堆叠式 etcd 拓扑](<https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/#stacked-etcd-topology>)），则需要在 `kubeadm init` 时提供 `--control-plane-endpoint=_< IP 或域名>_`（无法事后进行此操作！）。
  * 可以使用 [配置文件](<https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file>) 来代替一组参数进行 `kubeadm init`。

####  初始化控制平面

要初始化控制平面，你需要向 `kubeadm init` 传递以下必要的标志。 

如果成功运行，`kubeadm init` 将在 `/etc/kubernetes/` 和 `/var/lib/kubelet/` 下生成 `kubelet` 和各种控制平面组件的配置。 

最后，它将输出可以复制并粘贴的命令，用于设置 [kubectl](<https://archlinux.org/packages/?name=kubectl>)包 并使工作节点加入集群（基于有效期为 24 小时的令牌）。 

要将 `kubectl` 与刚创建的控制平面节点一起使用，请设置配置（以 root 或普通用户身份）： 
    
    $ mkdir -p $HOME/.kube
    # cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    # chown $(id -u):$(id -g) $HOME/.kube/config
    
####  安装 CNI 插件（Pod 网络插件）

**注意：** 你必须部署一个基于 **Container Network Interface (CNI)** 的 Pod 网络插件，以便你的 Pod 可以相互通信。**集群 DNS (CoreDNS)** 在网络安装之前不会启动。

[Pod 网络插件](<https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network>)（CNI 插件）以不同的方式实现 Kubernetes [网络模型](<https://kubernetes.io/docs/concepts/services-networking/>)，从简单的解决方案如 [flannel](<https://github.com/flannel-io/flannel>) 到更复杂的解决方案如 [calico](<https://www.tigera.io/project-calico/>)。有关更多选项，请参阅[此列表](<https://kubernetes.io/docs/concepts/cluster-administration/addons/#networking-and-network-policy>)。 

一个日益被采用的高级 CNI 插件是 [cilium](<https://cilium.io/>)，它通过 eBPF 实现了[令人印象深刻的性能](<https://cilium.io/blog/2021/05/11/cni-benchmark/>)。要安装 `cilium` 作为 CNI 插件，请使用 [cilium-cli](<https://archlinux.org/packages/?name=cilium-cli>)包： 
    
    # cilium-cli install
    
这将创建 `/opt/cni/bin/cilium-cni` 插件、配置文件 `/etc/cni/net.d/05-cilium.conflist`，并在 Kubernetes 集群上部署两个 Pod。 

**注意：** 如果你使用 CRI-O，请确保已启用 `/opt/cni/bin/` 插件目录。请参阅 [CRI-O#Plugin directories](</wzh/index.php?title=CRI-O&action=edit&redlink=1> "CRI-O（页面不存在）")。

###  使用配置文件的 kubeadm

你很可能会发现，创建控制平面需要多次尝试才能找到适合你特定设置的最佳配置。为了使此过程更容易（并且使 [kubeadm](<https://archlinux.org/packages/?name=kubeadm>)包 的过程更具可重复性），你可以使用配置文件运行初始化步骤。 

**提示：** 计划使用两个配置文件，一个用于初始化，一个用于重置，以便更快地测试配置。

####  创建初始化配置文件

你可以在任何地方创建此文件，但在此示例中我们将使用 `/etc/kubeadm`。 
    
    # mkdir -pv /etc/kubeadm
    # cd /etc/kubeadm
    # kubeadm config print init-defaults > init.yaml
    
这将生成以下文件。 
    
    /etc/kubeadm/init.yaml
    
    apiVersion: kubeadm.k8s.io/v1beta3
    bootstrapTokens:
    - groups:
      - system:bootstrappers:kubeadm:default-node-token
      token: abcdef.0123456789abcdef
      ttl: 24h0m0s
      usages:
      - signing
      - authentication
    kind: InitConfiguration
    localAPIEndpoint:
      advertiseAddress: 1.2.3.4
      bindPort: 6443
    nodeRegistration:
      criSocket: unix:///var/run/containerd/containerd.sock
      imagePullPolicy: IfNotPresent
      name: node
      taints: null
    ---
    apiServer:
      timeoutForControlPlane: 4m0s
    apiVersion: kubeadm.k8s.io/v1beta3
    certificatesDir: /etc/kubernetes/pki
    clusterName: kubernetes
    controllerManager: {}
    dns: {}
    etcd:
      local:
        dataDir: /var/lib/etcd
    imageRepository: registry.k8s.io
    kind: ClusterConfiguration
    kubernetesVersion: 1.29.0
    networking:
      dnsDomain: cluster.local
      serviceSubnet: 10.96.0.0/12
    scheduler: {}
    
大多数默认设置应该可以工作，但你需要更新其中的一些设置。 

#####  引导令牌

使用 `kubeadm token generate` 创建一个令牌，并在配置中使用它代替 `token: abcdef.0123456789abcdef`。 

#####  公告地址

`advertiseAddress: 1.2.3.4` 应该是正在初始化的控制平面的网络接口的 IPv4 地址，可能是 `192.168.0.0/16` 子网中的某个地址。 

#####  节点名称

默认节点名称可以保留为 `node` 并添加到本地 DNS 服务器或 hosts 文件中，或者你可以将其更改为本地网络上可路由的地址。它应该是一个 DNS 兼容的主机名，例如 `kcp01.example.com`。这将允许你的控制平面在加入其他节点时在本地网络上被发现。 

####  初始化集群

完成所有这些更改后，我们可以初始化我们的集群。 
    
    # kubeadm init --config /etc/kubeadm/init.yaml
    
这将产生大量输出，输出提供了有关如何将节点加入集群、更新 kubeconfig 以与新集群交互以及其他任务的说明。 

#####  使用 calico 进行 CNI 配置

在开始添加节点和运行工作负载之前，你最后需要的东西是 正确配置的 CNI。此示例将使用 [calico](<https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises>) 来实现这一点。 
    
    # cd /etc/cni/net.d
    # curl <https://raw.githubusercontent.com/projectcalico/calico/v3.27.2/manifests/calico.yaml> -O
    # kubectl create -f calico.yaml
    
如果此操作成功完成，你就可以开始添加节点并在集群上运行工作负载啦。 

####  创建重置配置文件

为防止 [kubeadm](<https://archlinux.org/packages/?name=kubeadm>)包 第一次初始化不成功，你还可以创建一个用于重置命令的配置文件： 
    
    # kubeadm config print reset-defaults > /etc/kubeadm/reset.yaml
    
这将创建以下文件： 
    
    /etc/kubeadm/reset.yaml
    
    apiVersion: kubeadm.k8s.io/v1beta4
    certificatesDir: /etc/kubernetes/pki
    criSocket: unix:///var/run/containerd/containerd.sock
    kind: ResetConfiguration
    
#####  重置集群

要将集群重置为零，请运行以下命令： 
    
    # kubeadm reset --config /etc/kubeadm/reset.yaml
    
可以根据需要多次执行此操作，以确定集群的理想配置。 

####  创建加入配置文件

很可能在初始化集群后，你可以使用 init 命令输出中列出的命令加入任何节点，但如果你遇到问题，在要加入的节点上准备一个加入配置文件将会很有帮助。你可以在控制平面上创建此文件，或者在要加入集群的节点上运行命令，我们假设你执行了后者。 
    
    # kubeadm config print join-defaults > /etc/kubeadm/join.yaml
    
这将创建以下文件。 
    
    /etc/kubeadm/join.yaml
    
    apiVersion: kubeadm.k8s.io/v1beta3
    caCertPath: /etc/kubernetes/pki/ca.crt
    discovery:
      bootstrapToken:
        apiServerEndpoint: kcp01.example.com:6443
        token: abcdef.0123456789abcdef
        unsafeSkipCAVerification: true
      timeout: 5m0s
      tlsBootstrapToken: abcdef.0123456789abcdef
    kind: JoinConfiguration
    nodeRegistration:
      criSocket: unix:///var/run/containerd/containerd.sock
      imagePullPolicy: IfNotPresent
      name: node01.example.com
      taints: null
    
**注意：** 你需要为此配置文件创建两个不同的令牌，第一个用于 `discovery.bootstrapToken.token`，第二个用于 `discovery.tlsBootstrapToken` 属性。

##  加入集群

使用在[#创建集群](<#%E5%88%9B%E5%BB%BA%E9%9B%86%E7%BE%A4>)中生成的令牌信息，可以通过命令 `kubeadm join` 使另一台机器作为工作节点加入集群。 

请记住，你还需要通过将标志 `<SOCKET>` 传递给命令 `kubeadm join` 来为工作节点[选择容器运行时接口](<#%E9%80%89%E6%8B%A9%E5%AE%B9%E5%99%A8%E8%BF%90%E8%A1%8C%E6%97%B6%E6%8E%A5%E5%8F%A3_\(CRI\)>)。 

例如： 
    
    # kubeadm join _< api-server-ip>:<port>_ --token _< token>_ --discovery-token-ca-cert-hash sha256:_< hash>_ --node-name=_< name_of_the_node>_ --cri-socket=_< SOCKET>_
    
要生成新的引导令牌，可以使用以下命令： 
    
    kubeadm token create --print-join-command
    
如果你使用 Cilium 并且发现工作节点仍然处于 `NotReady` 状态，请使用以下命令检查工作节点的状态： 
    
    kubectl describe node <node-id> --namespace=kube-system
    
如果你发现以下条件状态： 
    
    Type                  Status       Reason
    ----                  ------       ------
    NetworkUnavailable    False        CiliumIsUp
    Ready                 False        KubeletNotReady container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized
    
请在工作节点上[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `containerd.service` 和 `kubelet.service`。 

##  提示与技巧

###  拆除集群

当需要从头开始重建集群时，可使用 [kubectl](<https://archlinux.org/packages/?name=kubectl>)包 按官方文档[拆除集群](<https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#tear-down>)的步骤操作： 
    
    kubectl drain <节点名称> --delete-local-data --force --ignore-daemonsets
    
此处 `<节点名称>` 是需要清空并重置的节点名称，可通过 `kubectl get node -A` 列出所有节点。 

随后重置该节点： 
    
    # kubeadm reset
    
###  在代理后方操作

`kubeadm` 会读取 `https_proxy`、`http_proxy` 和 `no_proxy` 环境变量。需确保 Kubernetes 内部网络包含在 `no_proxy` 中，例如： 
    
    export no_proxy="192.168.122.0/24,10.96.0.0/12,192.168.123.0/24"
    
其中第二个 CIDR（10.96.0.0/12）是 Kubernetes 默认的服务网络地址段。 

##  故障排除

###  无法获取容器统计信息

如果 `kubelet.service` 输出以下错误： 
    
    Failed to get system container stats for "/system.slice/kubelet.service": failed to get cgroup stats for "/system.slice/kubelet.service": failed to get container info for "/system.slice/kubelet.service": unknown container "/system.slice/kubelet.service"
    
则需要为 kubelet 添加配置（参见[相关的上游问题](<https://github.com/kubernetes/kubernetes/issues/56850>)）。 
    
    /var/lib/kubelet/config.yaml
    
    systemCgroups: '/systemd/system.slice'
    kubeletCgroups: '/systemd/system.slice'
    
###  使用 Flannel CNI 和 systemd-networkd 时 Pod 无法通信

参见[上游问题报告](<https://github.com/flannel-io/flannel/issues/1321#issuecomment-678284129>)。 

[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 会为每个链接分配一个持久的 MAC 地址。此策略在其默认配置文件 `/usr/lib/systemd/network/99-default.link` 中定义。然而，[Flannel](<https://github.com/flannel-io/flannel/>) 依赖于能够选择自己的 MAC 地址。要覆盖 systemd-networkd 对 `flannel _*_` 接口的行为，请创建以下配置文件： 
    
    /etc/systemd/network/50-flannel.link
    
    [Match]
    OriginalName=flannel*
    
    [Link]
    MACAddressPolicy=none

然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `systemd-networkd.service`。 

如果集群已经在运行，你可能需要手动删除每个节点上的 `flannel.1` 接口和 `kube-flannel-ds-_*_` Pod，包括主节点。Pod 会立即重新创建，并且它们自己会重新创建 `flannel.1` 接口。 

删除 `flannel.1` 接口： 
    
    # ip link delete flannel.1
    
删除 `kube-flannel-ds-_*_` Pod。使用以下命令删除所有节点上的所有 `kube-flannel-ds-_*_` Pod： 
    
    $ kubectl -n kube-system delete pod -l="app=flannel"
    
###  CoreDNS Pod 一直处于 Pending 状态，控制平面节点保持 "NotReady"

当在单台机器上使用 `kubeadm init` 引导 Kubernetes 时，如果没有其他机器 `kubeadm join` 集群，控制平面节点默认会被添加上污点（Taint）。因此，工作负载将不会调度到该机器上。 

可以通过以下命令确认控制平面节点是否被添加了污点： 
    
    kubectl get nodes -o json | jq '.items[].spec.taints
    
要临时允许在控制平面节点上调度，执行： 
    
    kubectl taint nodes <your-node-name> node-role.kubernetes.io/control-plane:NoSchedule-
    
然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `containerd.service` 和 `kubelet.service` 以应用更新。 

###  [kubelet-finalize] 畸形头：缺少 HTTP content-type

你可能忘记了[选择 systemd cgroup 驱动](<#%E4%B8%BA_containerd_%E9%80%89%E6%8B%A9_cgroup_%E9%A9%B1%E5%8A%A8>)。参见 [kubeadm 问题 2767](<https://github.com/kubernetes/kubeadm/issues/2767#issuecomment-1623967664>) 报告此问题。 

###  CoreDNS Pod 由于循环无法启动

当主机节点运行本地 DNS 缓存（如 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")）时，CoreDNS 可能会由于检测到转发循环而无法启动。可以通过以下方式检查： 
    
    # kubectl get pods -n kube-system
    
    NAME                               READY   STATUS             RESTARTS      AGE
    cilium-jc98m                       1/1     Running            0             21m
    cilium-operator-64664858c8-zjzcq   1/1     Running            0             21m
    coredns-7db6d8ff4d-29zfg           0/1     CrashLoopBackOff   6 (41s ago)   21m
    coredns-7db6d8ff4d-zlvsm           0/1     CrashLoopBackOff   6 (50s ago)   21m
    etcd-k8s                           1/1     Running            19            21m
    kube-apiserver-k8s                 1/1     Running            17            21m
    kube-controller-manager-k8s        1/1     Running            16            21m
    kube-proxy-cvntt                   1/1     Running            0             21m
    kube-scheduler-k8s                 1/1     Running            23            21m
    
    # kubectl logs -n kube-system coredns-7db6d8ff4d-29zfg
    
    ...
    [FATAL] plugin/loop: Loop ([::1]:46171 -> :53) detected for zone ".", see <https://coredns.io/plugins/loop#troubleshooting>. Query: "HINFO 64811921068182325.3042126689798234092."
    
这是由于 _kubelet_ 将主机的 `/etc/resolv.conf` 文件传递给所有使用默认 `dnsPolicy` 的 Pod。CoreDNS 使用此 `/etc/resolv.conf` 作为上游转发请求的列表。由于它包含一个环回地址（如 127.0.0.53），CoreDNS 最终将请求转发给自己。 

参见 <https://coredns.io/plugins/loop/#troubleshooting> 以解决此问题。 

##  参见

  * [Kubernetes Documentation](<https://kubernetes.io/docs/home/>) \- The upstream documentation
  * [Kubernetes Cluster with Kubeadm](<https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/>) \- Upstream documentation on how to setup a Kubernetes cluster using kubeadm
  * [Kubernetes Glossary](<https://kubernetes.io/docs/reference/glossary/?fundamental=true>) \- The official glossary explaining all Kubernetes specific terminology
  * [Kubernetes Addons](<https://kubernetes.io/docs/concepts/cluster-administration/addons/>) \- A list of third-party addons
  * [Kubelet Config File](<https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/>) \- Documentation on the Kubelet configuration file
  * [Taints and Tolerations](<https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>) \- Documentation on node affinities and taints
