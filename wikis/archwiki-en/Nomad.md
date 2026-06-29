# Nomad

Nomad is a workload orchestrator to deploy and manage containers and non-containerized applications.

## Installation
Install the  package.

## Known issues
## NVIDIA not supported
NVIDIA support has been disabled due to there being no way to disable a non-existent driver being loaded. When compiled with NVIDIA support, the instance immediately crashes with the following error:

 /usr/bin/nomad: undefined symbol: nvmlDeviceGetGraphicsRunningProcesses

The NVIDIA driver plugin will be externalised, see GitHub issue #8330.

## Default plugin directory
The default plugin directory  has been changed to  to reflect FHS.

## Configuration
Nomad loads all configuration files in the  directory on startup.

See https://learn.hashicorp.com/tutorials/nomad/security-enable-tls to set up TLS encryption with Nomad.

## Server
Create a configuration file at :

{{hc|/etc/nomad.d/server.hcl|2=
server {
  enabled = true
  bootstrap_expect = 3
}
}}

## Client
Create a configuration file at :

{{hc|/etc/nomad.d/client.hcl|2=
client {
  enabled = true
}
}}

## Task drivers
Task drivers are used by Nomad clients to execute a task and provide resource isolation.

Nomad ships with support for the following task drivers out of the box:
* Docker (requires )
* Java (requires  or )
* QEMU (requires )
*  &

## containerd
In order to use the containerd driver, Install the  package.

Enable the plugin in the client configuration, then Reload .
{{hc|/etc/nomad.d/containerd.hcl|2=
plugin "containerd-driver" {
  config {
    # Arch Linux uses cgroups v2 by default
    # For cgroups v1, use "io.containerd.runc.v1"
    containerd_runtime = "io.containerd.runc.v2"
  }
}
}}

## podman
In order to user the podman driver, Install the .

Nomad requires  to be started.

Enable the driver in the client configuration, then reload .
{{hc|/etc/nomad.d/podman.hcl|2=
plugin "nomad-driver-podman" {
  config {
    # Arch Linux socket path for podman differs from the default value of socket_path (unix://run/podman/io.podman)
    socket_path = "unix://run/podman/podman.sock"
    # In case podman.service was started as user
    socket_path = "unix://run/user/USER_UID/podman/podman.sock"
  }
}
}}
