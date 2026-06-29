# Minikube

Minikube lets you quickly setup a local Kubernetes cluster. It supports the use of Virtual Machines, containers and even bare metal as its driver.

## Installation
Install  or  for those that prefer the latest development version.

## Usage
## QEMU
To use minikube with QEMU, the following packages are required:

*
*
*
*
*

Additionally the current user needs to be in the  user group.

Start the  unit and check its unit status for any issues.

Then set the kvm2 provider in minikube:

 $ minikube config set driver kvm2

And start it:

 $ minikube start

## Rootless Docker
See Docker#Rootless Docker daemon for docker setup.

Configure Internet sharing#Enable packet forwarding to allow outbound network requests from pods.

Start minikube:

 $ minikube start --driver=docker --container-runtime=containerd

Test network:

 $ kubectl run -it --rm --restart=Never --image alpine tmp -- sh
 > ping 1.1.1.1
 > ping ping.archlinux.org
 > ping host.minikube.internal

## Rootless Podman
See Podman#Rootless Podman for rootless Podman setup.

Configure minikube before starting it:

 $ minikube config set rootless true
 $ minikube config set driver podman
 $ minikube config set container-runtime cri-o

Start minikube:

 $ minikube start
