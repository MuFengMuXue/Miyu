# CRI-O

CRI-O is an OCI-based implementation of the Kubernetes Container Runtime Interface. As such, it is one of the container runtimes that can be used with a node of a Kubernetes cluster.

## Installation
Install the  package.

The package will set the system up to load the  and  modules and set the following sysctl options:

 net.bridge.bridge-nf-call-iptables = 1
 net.bridge.bridge-nf-call-ip6tables = 1
 net.ipv4.ip_forward = 1

To use CRI-O without a reboot, make sure to load the modules and configure the sysctl values accordingly.

## Configuration
CRI-O is configured via  or via drop-in configuration files in .

## Network
## Plugin installation
CRI-O can make use of container networking as provided by , or plugins installed with in-cluster deployments such as weave, flannel, calico, etc.

## Plugin directories
Arch installs the plugins provided by  to both  and , but most other plugins (e.g. in-cluster deployments, kubelet managed plugins, etc.) by default only install to the second directory. CRI-O is only configured to look for plugins in the first directory, and as a result, any plugins in the second directory are unavailable without some configuration changes.

This may present itself as a non-working network and an entry in the CRI-O logs similar to the following error:

 Error validating CNI config file /etc/cni/net.d/.conf: to find plugin "" in path /usr/lib/cni/

There are two solutions available to resolve this: either have each of the other systems changed to use  instead, or update CRI-O to use the latter directory instead of the first. The second solution can be achieved with a drop-in configuration file:

As this is an array, you can also set both or any other directories here as possible plugin locations.

## Plugin configuration
Copy one of the examples from  to  and modify it as needed.

## Storage
By default, CRI-O makes use of the  driver as its  for the container storage in . However, it can also be configured to use Btrfs or ZFS natively by changing the  in :

## Runtime
The  package depends on the oci-runtime virtual package, which selects  by default using lexicographic ordering.

However, CRI-O makes use of the  container runtime by default. Either install the  package explicitly, or configure  as the container runtime by adding the following drop-in configuration file:

## Running
Start and enable the  systemd unit.

## Testing
Use  like this:

and:

 # crio status config

Now install the  package, and see e.g. https://kubernetes.io/docs/tasks/debug-application-cluster/crictl/ or https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md, or simply:

 # source <(crictl completion bash)

 # crictl pull index.docker.io/busybox
 # crictl pull quay.io/prometheus/busybox
 # crictl images

 # curl -O https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/examples/podsandbox-config.yaml
 # curl -O https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/examples/container-config.yaml
 # crictl run container-config.yaml podsandbox-config.yaml

 # crictl logs $(crictl ps --last 1 --output yaml | yq -r .containers# crictl exec -it $(crictl ps --last 1 --output yaml | yq -r .containers[0.id) /bin/sh

 # crictl rm -af
 # crictl rmp -af

Note how Docker Hub is not hard-coded, so specify container registry explicitly. (See also https://github.com/kubernetes-sigs/cri-tools/pull/718.)
