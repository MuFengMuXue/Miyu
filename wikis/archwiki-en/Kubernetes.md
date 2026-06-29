# Kubernetes

Kubernetes (aka. k8s) is an open-source system for automating the deployment, scaling, and management of containerized applications.

A k8s cluster consists of its control-plane components and node components (each representing one or more host machines running a container runtime and ). There are two options to install kubernetes, "the real one", described here, and a local install with k3s, kind, or .

## Installation
There are many methods to setup a kubernetes cluster. This article will focus on bootstrapping with .

## Deployment tools
## kubeadm
When bootstrapping a Kubernetes cluster with kubeadm, install  and  on each node.

## Manual installation
When manually creating a Kubernetes cluster install  and the package group  (for a control-plane node) and  (for a worker node).

## Cluster management
To control a kubernetes cluster, install  on the control-plane hosts and any external host that is supposed to be able to interact with the cluster.

## Container runtime
Both control-plane and regular worker nodes require a container runtime for their  instances which is used for hosting containers.
Install either  or  to meet this dependency.

## containerd runtime
There are two methods available to install containerd:

# Install the  package.
# To install a rootless containerd, use , which is a full nerdctl package, bundled with containerd, CNI plugin, and RootlessKit. Rootless containerd can be launched with .

Remember that Arch Linux uses systemd as its init system, so you need to choose systemd cgroup driver before deploying the control plane(s).

## (Optional) Package manager
 is a tool for managing pre-configured Kubernetes resources which may be helpful for getting started.

## Configuration
All nodes in a cluster (control-plane and worker) require a running instance of .

All provided systemd services accept CLI overrides in environment files:

* :
* :
* :
* :
* :

## Disable swap
Kubernetes currently does not support having swap enabled on the system. See KEP-2400: Node system swap support for details.

See Swap#Disabling swap for instructions on how to disable swap.

## Choose cgroup driver for containerd
To use the  cgroup driver in  with , set

 ...
   [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options
     SystemdCgroup = true

If  does not exist, the default configuration can be generated with # mkdir -p /etc/containerd/
 # containerd config default > /etc/containerd/config.toml

Remember to restart  to make the change take effect.

See the [https://kubernetes.io/docs/setup/production-environment/container-runtimes/#cgroup-drivers official documentation for a deeper discussion on whether to keep  driver or use  cgroup driver.

## Choose container runtime interface (CRI)
A container runtime has to be configured and started, before  can make use of it.

You will pass flag  with the container runtime interface endpoint to  or  in order to create or join a cluster.

For example, if you choose  as CRI runtime, the flag  will be:

 kubeadm init --cri-socket /run/containerd/containerd.sock

## Containerd
Before Kubernetes version 1.27.4, when using  as container runtime, it is required to  provide  or  with its CRI endpoint. To do so, specify their flag  to  kubeadm join --cri-socket=/run/containerd/containerd.sock

After Kubernetes version 1.27.4, kubeadm will auto detect this CRI for you, flag  is only needed when you installed multiple CRI.

## CRI-O
When using CRI-O as container runtime, it is required to  provide  or  with its CRI endpoint:

## Choose cluster network parameter
## Choose a pod CIDR range
The networking setup for the cluster has to be configured for the respective container runtime. This can be done using .

The pod CIDR addresses refer to the IP address range that is assigned to pods within a Kubernetes cluster. When pods are scheduled to run on nodes in the cluster, they are assigned IP addresses from this CIDR range.

The pod CIDR range is specified when deploying a Kubernetes cluster and is confined within the cluster network. It should not overlap with other IP ranges used within the cluster, such as the service CIDR range.

You will pass flag  with value of the virtual network's CIDR to  or  in order to create or join a cluster.

For example:

 kubeadm init --pod-network-cidr='10.85.0.0/16'

will set your kubernetes' pod CIDR range to .

## (Optional) Choose API server advertising address
If your node for control plane is in multiple subnets (for example you may have installed a tailscale tailnet),
when initializing the Kubernetes master with kubeadm init, you can specify the IP address that the API server will advertise with the  flag. This IP address should be accessible to all nodes in your cluster.

## (Optional) Choose alternative node network proxy provider
Node proxy provider like  is a network proxy that runs on each node in your cluster, maintaining network rules on nodes to allow network communication to your Pods from network sessions inside or outside of your cluster.

By default  choose  as the node proxy that runs on each node in your cluster.

Container Network Interface (CNI) plugins like cilium offer a complete replacement for kube-proxy.

If you want to use cilium's implementation of node network proxy to fully leverage cilium's network policy feature, you should pass flag  to  to skip the install of kube-proxy.

Cilium will install a full replacement during its installation. See this[https://docs.cilium.io/en/latest/network/kubernetes/kubeproxy-free/ for details.

## Create cluster
Before creating a new kubernetes cluster with  start and enable .

## kubeadm without config
When creating a new kubernetes cluster with  a control-plane has to be created before further worker nodes can join it.

## Initialize control-plane
To initialize control-plane, you need pass the following necessary flags to

If run successfully,  will have generated configurations for the  and various control-plane components below  and .

Finally, it will output commands ready to be copied and pasted to setup  and make a worker node join the cluster (based on a token, valid for 24 hours).

To use  with the freshly created control-plane node, setup the configuration (either as root or as a normal user):

 $ mkdir -p $HOME/.kube
 # cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
 # chown $(id -u):$(id -g) $HOME/.kube/config

## Installing CNI plugins (pod network addon)
Pod network add-ons (CNI plugins) implement the Kubernetes network model differently from simple solutions like flannel to more complicated solutions like calico. See this list for more options.

An increasingly adopted advanced CNI plugin is cilium, which achieves impressive performance with eBPF. To install  as CNI plugin, use :

 # cilium-cli install

This will create the  plugin, config file  and deploy two pods on the Kubernetes cluster.

## kubeadm with config
You will most likely find that creating the control plane requires several attempts find the optimal configuration for your particular setup. To make this easier (and the process with  more repeatable generally), you may run the initialization step using config files.

## Create the init config
You can create this file anywhere, but we will go with  for this example.

 # mkdir -pv /etc/kubeadm
 # cd /etc/kubeadm
 # kubeadm config print init-defaults > init.yaml

This will produce the following file.

{{hc|/etc/kubeadm/init.yaml|
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
}}

Most of the default settings should work, though you will need to update a few of them.

## Bootstrap token
Create a token with  and use it instead of  in the config.

## Advertise address
The  should be an IPv4 address of a network interface on the control plane being initialized, probably something in the  subnet.

## Node name
The default node name can either be left at  and added to your local DNS server or hosts file, or you can change it to an address that is routable on your local network. It should be a DNS-compatible hostname, such as . This will allow your control plane to be found on your local network when you join other nodes.

## Init the cluster
With all of these changes set, we can initialize our cluster.

 # kubeadm init --config /etc/kubeadm/init.yaml

This will produce a good amount of output that will provide instructions on how to join nodes to the cluster, update your kubeconfig to interact with the new cluster, and other tasks.

## Use calico for CNI config
The last thing you need before you can start adding nodes and running workloads is a properly configured CNI. This example will use calico for that.

 # cd /etc/cni/net.d
 # curl https://raw.githubusercontent.com/projectcalico/calico/v3.27.2/manifests/calico.yaml -O
 # kubectl create -f calico.yaml

If this completes successfully, you are ready to start adding nodes and running workloads on your cluster.

## Create the reset config
Just in case  does not land the init the first time, you can also create a config file for use with the reset command:

 # kubeadm config print reset-defaults > /etc/kubeadm/reset.yaml

This will create the following file:

## Reset a cluster
To reset the cluster back to zero, run the following command:

 # kubeadm reset --config /etc/kubeadm/reset.yaml

This can be done as many times as required to sort out your cluster's ideal configuration.

## Create the join config
Most likely once you init the cluster you'll be able to join any nodes with the command listed in the output of the init command, but if you happen to run in to trouble it will be helpful to have a join config available on the nodes you're joining. You can either create this file on your control plane, or run the command on nodes that you intend to join to the cluster, we'll assume you did the latter.

 # kubeadm config print join-defaults > /etc/kubeadm/join.yaml

This will create the following file.

## Join cluster
With the token information generated in #Create cluster it is possible to make another machine join the cluster as worker node with command .

Remember you need to choose a container runtime interface for working nodes as well by passing flag  to command .

For example:

 # kubeadm join : --token ' --discovery-token-ca-cert-hash sha256:' --node-name=' --cri-socket='

To generate new bootstrap token,
 kubeadm token create --print-join-command

If you are using Cilium and find the working node remains to be , check the status of working node using:

 kubectl describe node  --namespace=kube-system

If you found the following condition status:

 Type                  Status       Reason
 ----                  ------       ------
 NetworkUnavailable    False        CiliumIsUp
 Ready                 False        KubeletNotReady container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized

Restart  and  on the working node

## Tips and tricks
## Tear down a cluster
When it is necessary to start from scratch, use  to tear down a cluster.

 kubectl drain  --delete-local-data --force --ignore-daemonsets

Here  is the name of the node that should be drained and reset.
Use  to list all nodes.

Then reset the node:

 # kubeadm reset

## Operating from behind a proxy
 reads the , , and  environment variables. Kubernetes internal networking should be included in the latest one, for example

 export no_proxy="192.168.122.0/24,10.96.0.0/12,192.168.123.0/24"

where the second one is the default service network CIDR.

## Troubleshooting
## Failed to get container stats
If  emits

 Failed to get system container stats for "/system.slice/kubelet.service": failed to get cgroup stats for "/system.slice/kubelet.service": failed to get container info for "/system.slice/kubelet.service": unknown container "/system.slice/kubelet.service"

it is necessary to add configuration for the kubelet (see relevant upstream ticket).

## Pods cannot communicate when using Flannel CNI and systemd-networkd
See upstream bug report.

systemd-networkd assigns a persistent MAC address to every link. This policy is defined in its shipped configuration file . However, Flannel relies on being able to pick its own MAC address. To override systemd-networkd's behaviour for  interfaces, create the following configuration file:

Then restart .

If the cluster is already running, you might need to manually delete the  interface and the  pod on each node, including the master. The pods will be recreated immediately and they themselves will recreate the  interfaces.

Delete the interface :

 # ip link delete flannel.1

Delete the  pod. Use the following command to delete all  pods on all nodes:

 $ kubectl -n kube-system delete pod -l="app=flannel"

## CoreDNS Pod pending forever, the control plane node remains "NotReady"
When bootstrap the Kubernetes with  on a single machine, and there is no other machine  the cluster, the control-plane node is default to be tainted. As a result, no workload will be scheduled on the working machine.

One can confirm the control-plane node is tainted by the following commands:

 kubectl get nodes -o json | jq '.itemsTo temporarily allow scheduling on the control-plane node, execute:

 kubectl taint nodes  node-role.kubernetes.io/control-plane:NoSchedule-

Then restart  and  to apply the updates.

## [kubelet-finalize malformed header: missing HTTP content-type
You may have forgotten to choose systemd cgroup driver. See kubeadm issue 2767 reporting this.

## CoreDNS Pod does not start due to loops
When the host node runs a local DNS cache such as systemd-resolved, the CoreDNS may fail to start due to detecting a forwarding loop. This can be checked as follows:

This is caused by kubelet passing the host  file, to all Pods using the default . CoreDNS uses this  as a list of upstreams to forward requests to. Since it contains a loopback address such as 127.0.0.53, CoreDNS ends up forwarding requests to itself.

See https://coredns.io/plugins/loop/#troubleshooting to resolve the issue.

## Some containers are slow to start/don't start in kind.
By default on Arch,  is set to a really high value.

You can fix this with .

References:

* https://github.com/kubernetes-sigs/kind/pull/760
* https://github.com/kubernetes-sigs/kind/issues/4001
* https://github.com/kubernetes-sigs/kind/pull/1799/files
