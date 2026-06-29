# Buildah

Buildah is a tool that facilitates building Open Container Initiative (OCI) container images. The Buildah package provides a command line tool that can be used to:

* create a working container, either from scratch or using an image as a starting point
* create an image, either from a working container or via the instructions in a Dockerfile
* images can be built in either the OCI image format or the traditional upstream docker image format
* mount a working container's root filesystem for manipulation
* unmount a working container's root filesystem
* use the updated contents of a container's root filesystem as a filesystem layer to create a new image
* delete a working container or an image
* rename a local container

The most widely known alternative for building containers is docker. Do note that Buildah does not run containers, for that you may want to consider podman.

## Installation
Install the  and  packages.

## Configuration
## Enable support to build unprivileged containers
Users wishing to use Buildah to build unprivileged containers need to complete additional setup steps before running podman for the first time.

Finally, create both  and  to contain the mapping to the containerized UID/GID pairs for each user who shall be able to run the containers.The example below is for the root user (and systemd system unit) and an example user :

If you did run podman before applying the changes above, you will get errors when trying to pull images as an unprivileged user. Run  to fix it.

If everything went well then after logging out and logging back in  should not result in error

## Usage
See the [https://github.com/containers/buildah/tree/main/docs/tutorials#readme Buildah tutorials.

## Troubleshooting
## WARN"/" is not a shared mount, this could cause issues or missing mounts with rootless containers
Buildah/Podman running as rootless expects the bind mount to be shared, check if it is set to private:

In this case see  and set temporarily the mount as shared with:

 # mount --make-shared /

To set it permanently, edit /etc/fstab and add the shared option to the desired mount and reboot. It will result in a entry like:
