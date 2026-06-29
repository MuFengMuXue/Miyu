# Kata Containers

Kata Containers (previously Clear Containers) is an OCI-compatible application container runtime meant to provide isolation of potentially untrusted processes from the host system and other processes by leveraging virtualization. Currently upstream-supported hypervisors are ,  and .

## Architecture
*  - supervisor process running on the hypervised guest sandbox, tasked with managing its lifetime
*  - container runtime component responsible for handling commands specified by the OCI runtime specification and tasked with launching shims
*  (before 2.0) - routes I/O streams and signals between on-guest agent and host-side processes associated with running a given sandbox using gRPC
*  (before 2.0) - container process monitor and reaper
*  (optional, before 2.0) -
*  - patched kernel used to launch VMs serving as container/pod sandboxes
*  - initramfs and rootfs images used for spawning VM sandboxes

## Usage
Kata, by default, picks up its configuration from , but that can be overridden by providing a path to configuration through the  environment variable. Be sure to initialize configuration from .

## v1
## Docker
In order to use Kata Containers with Docker, the user needs to add it to supported runtimes in :

  {
    "runtimes": {
      "kata": {
        "path": "/usr/bin/kata-runtime"
      }
    }
  }

To use it as the default runtime for Docker: {{ic|{"default-runtime": "kata"} }}.

To use it with the Firecracker hypervisor, due to its limitations, the  storage driver has to be used: {{ic|{"storage-driver": "devicemapper"} }}.

Afterward you can use the runtime key: .

## Podman
Running a container: .

Keep in mind that a Kata VM sandbox conceptually maps to Kubernetes pods or a shared netns, not just individual containers.

## v2
Install the runtime , kernel  and set of initrd and rootfs .

Docker has added support for OCI-compatible runtimes in Docker Engine 23.0 [https://docs.docker.com/engine/release-notes/23.0/#2300. To run a Docker container using Kata:

## Containerd CLI
 # ctr image pull docker.io/library/archlinux:latest
 # ctr run --rm -t --runtime io.containerd.kata.v2 docker.io/archlinux/base:latest example-container-name date
