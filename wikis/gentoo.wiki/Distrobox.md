[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Distrobox&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://distrobox.it/)

[[]][GitHub](https://github.com/89luca89/distrobox)

[[]][Package information](https://packages.gentoo.org/packages/app-containers/distrobox)

**distrobox** is a program used to run a Linux Distribution in a terminal.

## Contents

-   [[1] [Use Flags]](#Use_Flags)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Installing a container]](#Installing_a_container)
    -   [[3.1] [Podman]](#Podman)
    -   [[3.2] [Docker]](#Docker)
-   [[4] [Usage]](#Usage)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Installing basic packages\... Error: An error occured While Entering Distrobox]](#Installing_basic_packages..._Error:_An_error_occured_While_Entering_Distrobox)
        -   [[5.1.1] [Ubuntu: update-locale: Error: invalid locale settings]](#Ubuntu:_update-locale:_Error:_invalid_locale_settings)

## [Use Flags]

### [USE flags for] [app-containers/distrobox](https://packages.gentoo.org/packages/app-containers/distrobox) [[]] [Use any Linux distribution inside your terminal (powered by docker/podman)]

  --------------------------------------------------- -----------------------------------------------
  [`gui`](https://packages.gentoo.org/useflags/gui)   Enable support for a graphical user interface
  --------------------------------------------------- -----------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-29 21:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Installation]

### [Emerge]

[[[app-containers/distrobox]](https://packages.gentoo.org/packages/app-containers/distrobox)[]] is in Gentoo\'s main repository:

`root `[`#`]`emerge --ask app-containers/distrobox`

## [Installing a container]

### [Podman]

Emerge [Podman](https://wiki.gentoo.org/wiki/Podman "Podman"):

`root `[`#`]`emerge --ask app-containers/podman`

### [Docker]

Emerge [Docker](https://wiki.gentoo.org/wiki/Docker "Docker"):

`root `[`#`]`emerge --ask app-containers/docker`

## [Usage]

** Note**\
More Information could be found at [official documentation](https://distrobox.it/#quick-start).

First, install an image (for this command [sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo") needs to be installed):

`user `[`$`]`distrobox create --name gentoo -i docker.io/gentoo/stage3:latest --root`

Then, enter the Distrobox Container:

`user `[`$`]`distrobox enter --root gentoo`

## [Troubleshooting]

### [`Installing basic packages... Error: An error occured` While Entering Distrobox]

A command line parameter `verbose` could be added to show more detailed information.

`user `[`$`]`distrobox enter <container_name> --verbose`

From here, the issue will be categorized into container distribution and error messages.

#### [Ubuntu: `update-locale: Error: invalid locale settings`]

Invalid locale settings have been written into the `locale.gen` in the container and require manual intervention.

** Important**\
This is more a temporary fix; the root cause is yet to be investigated.

** Important**\
This section use [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") backend for example. [Podman](https://wiki.gentoo.org/wiki/Podman "Podman") backend may share a similar process.

1\. Identify the docker image that the [distrobox] environment is based on :

`user `[`$`]`docker images`

    REPOSITORY                      TAG            IMAGE ID       CREATED          SIZE
    ubuntu                          24.04          bbdabce66f1b   3 weeks ago      78.1MB
    (...)

2\. Spawn a container based on the corresponding image:

`user `[`$`]`docker run -dt <image_id> /bin/bash`

3\. Find the ID of the container created and entering it:

`user `[`$`]`docker ps`

    CONTAINER ID   IMAGE                COMMAND                   CREATED          STATUS          PORTS     NAMES
    61f04b55d573   ubuntu:24.04         "/bin/bash"               8 seconds ago    Up 8 seconds              clever_pasteur
    (...)

4\. Entering the container:

`user `[`$`]`docker exec -it <container_id> /bin/bash`

-   Now the username and hostname section of the bash would change to indicate it\'s in the container.

5\. Update the repository and install the `locales` package:

`root@<container_id>:/#``apt update && apt install locales `

** Important**\
Before the next step, the container image may not have an interactive text editor. Install one that matches the reader\'s preference:

`root@<container_id>:/#``apt install vi (vim, nano, emacs, etc.) `

6\. Edit the `/etc/locale.gen`, removing the invalid entries and enable needed ones.

7\. Regenerate locales:

`root@<container_id>:/#``locale-gen `

8\. Exit the container by exectuting `exit`.

-   Now the username and hostname section of the bash would change back.

9\. Save the changes to the container:

`user `[`$`]`docker commit <container_id> <container_name>:<tag>`

** Important**\
The `<container_name>:<tag>` should be a different one than the original and reflect the changes made. E.g. `ubuntu:24.04-fixed`.

10\. Stop the container spawned earlier.

`user `[`$`]`docker stop <container_id>`

11\. Regenerate the [distrobox] container based on the fixed [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") container and enter it.