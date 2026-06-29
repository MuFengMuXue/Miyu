[Kubler](https://github.com/edannenberg/kubler) is a generic, extendable build orchestrator, written in [Bash](https://wiki.gentoo.org/wiki/Bash "Bash"). It can be used to take advantage of [Portage\'s](https://wiki.gentoo.org/wiki/Portage "Portage") features to build lightweight [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") or [Podman](https://wiki.gentoo.org/wiki/Podman "Podman") images without needing to mess with [crossdev], or as a tool to assist with [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") development.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Useful Notes]](#Useful_Notes)
    -   [[2.1] [Environmental Configuration]](#Environmental_Configuration)
    -   [[2.2] [Fixing Broken Builders]](#Fixing_Broken_Builders)
-   [[3] [Image Creation]](#Image_Creation)
    -   [[3.1] [Create a new namespace]](#Create_a_new_namespace)
    -   [[3.2] [Create a new image]](#Create_a_new_image)
        -   [[3.2.1] [Use interactive build to plan and test]](#Use_interactive_build_to_plan_and_test)
    -   [[3.3] [Build the image]](#Build_the_image)
    -   [[3.4] [Pushing Images to a Docker Repository]](#Pushing_Images_to_a_Docker_Repository)
-   [[4] [Ebuild Development with Kubler]](#Ebuild_Development_with_Kubler)
-   [[5] [Updating Build Containers]](#Updating_Build_Containers)
-   [[6] [External resources]](#External_resources)

## [Installation]

Kubler may be installed from the kubler [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"):

`root `[`#`]`eselect repository add kubler git `[`https://github.com/edannenberg/kubler-overlay.git`](https://github.com/edannenberg/kubler-overlay.git)

`root `[`#`]`emerge --sync`

`root `[`#`]`emerge --ask app-containers/kubler`

Building images requires a working Docker or Podman installation.

## [Useful Notes]

#### [Environmental Configuration]

Due to containerisation environmental configurations will not make it through to builder containers. This is often desirable as it enforces the documentation (through build-time configuration) of any non-standard configuration in the environment. To work around this many variables may be set in [kubler.conf] for either the namespace (global settings) or an individual image.

[FILE] **`kubler.conf`**

    HTTP_PROXY="http://proxy.server:80"
    HTTPS_PROXY="http://proxy.server:80"
    NO_PROXY="localhost,127.0.0.1,.localdomain"

#### [Fixing Broken Builders]

Eventually the installed version of Kubler and the [Gentoo repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") will come out of sync; typically the first sign of this is that Kubler becomes unable to create updated Portage containers. When this happens:

`root `[`#`]`emerge @live-rebuild`

`user `[`$`]`kubler clean`

`user `[`$`]`kubler build -C larry`

## [Image Creation]

Kubler provides a set of commands to create new images, builders and namespaces. These commands should be run from within a project directory, e.g.: [/data/development/gentoo-containers/]

`user `[`$`]`mkdir -p /data/development/gentoo-containers/`

`user `[`$`]`cd /data/development/gentoo-containers/`

### [Create a new namespace]

This example will create a new namespace called \'larry\' which may contain multiple images. The namespace will be created in the project directory.

Use the [new] command to take care of the boilerplate; choose \'multi\' when asked for the namespace type:

`user `[`$`]`kubler new namespace larry`

    »»»
    »»» <enter> to accept default value
    »»»
    »»» Working dir type? Choices:
    »»»   single - You can't add further namespaces to the created working dir, it only holds images
    »»»   multi  - Creates a working dir that can hold multiple namespaces
    »[?]» Type (single): multi
    »»»
    »»» Top level directory name for new namespace 'larry'? The directory is created at /data/development/gentoo-containers/
    »[?]» Namespaces Dir (kubler-images):
    »»»
    »»»»» Initial image tag, a.k.a. version?
    »[?]» Image Tag (20230706):
    »»»
    »[!]» New namespace location:  /data/development/gentoo-containers/kubler-images/larry
    »»»
    »»»»» Who maintains the new namespace?
    »[?]» Name (Your Name): Larry the Cow
    »[?]» EMail (your@mail.org): Larry.the.Cow@gentoo.zip
    »»»
    »»»»» Default build engine?
    »[?]» Engine (docker):
    »»»
    »[✔]» Successfully created "larry" namespace at /data/development/gentoo-containers/kubler-images
    »»»
    »[!]» Configuration file: /data/development/gentoo-containers/kubler-images/larry/kubler.conf
    »»»
    »[!]» To manage the new namespace with GIT you may want to run:
    »»»
    »»» $ git init /data/development/gentoo-containers/kubler-images/larry
    »»»
    »[!]» To create images in the new namespace run:
    »»»
    »»» $ cd /data/development/gentoo-containers/kubler-images/larry
        $ kubler new image larry/<image_name>

`user `[`$`]`cd larry/`

Although not strictly required, installing Kubler\'s example images is a good idea.

`user `[`$`]`kubler update`

It is worthwhile to begin tracking this new namespace with Git. Kubler will prepopulate a [.gitignore] file for convenience.

`user `[`$`]`pushd /data/development/gentoo-containers/kubler-images/larry`

`user `[`$`]`git init .`

`user `[`$`]`git add .`

`user `[`$`]`git commit -m "Initial commit"`

`user `[`$`]`popd`

### [Create a new image]

Kubler may be used to create container images for a variety of purposes. This example will create a new image called \'openldap\' within the existing \'larry\' namespace, based on the \'kubler/busybox\' image.

`user `[`$`]`kubler new image larry/openldap`

    »»»
    »»» <enter> to accept default value
    »»»
    »»» Extend an existing Kubler managed image? Fully qualified image id (i.e. kubler/busybox) or scratch
    »[?]» Parent Image (scratch): kubler/busybox
    »»»
    »»» Add test template(s)? Possible choices:
    »»»   hc  - Add a stub for Docker's HEALTH-CHECK, recommended for images that run daemons
    »»»   bt  - Add a stub for a custom build-test.sh script, a good choice if HEALTH-CHECK is not suitable
    »»»   yes - Add stubs for both test types
    »»»   no  - Fck it, we'll do it live!
    »[?]» Tests (hc): bt
    »»»
    »[✔]» Successfully created new image at /data/development/gentoo-containers/kubler-images/larry/images/openldap
    »»»

#### [Use interactive build to plan and test]

** Note**\
This step is *not* required; it is possible to directly edit the [config/build.sh] file if you are familiar with Portage.

Kubler brings a unique feature to the table when constructing an container image: the [\--interactive] build argument. As the name implies, this launches the build container in an interactive manner, enabling users to investigate the current / inherited configuration.

`user `[`$`]`kubler build larry/openldap -i`

This will build any missing parent images/builders; the first run may take quite a bit of time - once the local binary package cache and build containers are seeded future runs will be much faster. Once the prerequisite images are ready the build container will present a shell.

For first-time users it may be convenient to search for the openldap package to ensure that the correct atom is selected and investigate any USE flags that are of interest:

`root `[`#`]`eix openldap`

    * net-nds/openldap
         Available versions:  2.4.59-r2^t 2.5.14(0/2.5)^t 2.6.3-r7(0/2.6)^t ~2.6.4-r1(0/2.6)^t ~2.6.4-r2(0/2.6)^t
         Homepage:            https://www.openldap.org/
         Description:         LDAP suite of application and development tools

Edit the image\'s build script:

`root `[`#`]`nano /config/build.sh`

** Note**\
The [/config] directory in the build container is the host mounted image directory at [larry/images/openldap/]. Feel free to use a local IDE/editor to edit [build.sh] instead.

Add the [[[net-nds/openldap]](https://packages.gentoo.org/packages/net-nds/openldap)[]] and [[[net-misc/curl]](https://packages.gentoo.org/packages/net-misc/curl)[]] packages to the `_packages` variable in build.sh, update cURL USE flags, enable the **[\~arch]** versions of the packages we care about:

[FILE] **`/config/build.sh`**

    _packages="net-nds/openldap net-misc/curl"
    ...
    configure_rootfs_build()


** Note**\
If using the busybox image as a parent, unset the [su] USE flag from [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] in the [config/build.sh] file.

Perform a test run of the first build phase:

`root `[`#`]`kubler-build-root`

Once this completes successfully exit the interactive builder using [exit].

### [Build the image]

Assuming that [build.sh] has been configured as described above, it should be safe to attempt to build the image.

`user `[`$`]`kubler build larry/openldap -nF`

»\[✘\]»\[larry/openldap\]» fatal: build-test.sh for image larry/openldap:20230704 failed with exit signal: 1

** Note**\
The arguments are short hand for `--no-deps` and `--force-full-image-build`, omitting `-n` would also rebuild all parent images, which is waste of time in this case.

The build will fail, as expected, due to the [build-test.sh] script not being implemented. This is a good time to implement the [build-test.sh] script, which will be used to verify that the image is functional.

** Note**\
[pipefail] will cause build-test.sh to fail on busybox-based images

[FILE] **`build-test.sh`**

    #!/usr/bin/env sh

    set -eo

    # Do some tests and exit with either 0 for healthy or 1 for unhealthy
    # Check that the openldap bin launches and provides some expected output
    /usr/lib/openldap/lloadd -VV  2>&1 | grep "OpenLDAP" || exit 1

    exit 0

Unfortunately this image is not suitable for a build-time docker health check via the [docker-healthcheck.sh] mechanism, so it will not be demonstrated here.

Modify the image\'s [Dockerfile.template] to add any finishing touches, such as the [ENTRYPOINT] or [CMD] directives. In this example the container will act as an LDAP proxy via [lloadd]; additional configuration will be provided at runtime.

[FILE] **`Dockerfile.template`**

    FROM $
    LABEL maintainer="$"

    ADD rootfs.tar /

    #COPY docker-healthcheck.sh /usr/bin/docker-healthcheck
    #HEALTHCHECK --interval=60s --timeout=5s --start-period=5s --retries=3 CMD ["docker-healthcheck"]

    CMD ["/usr/lib/openldap/lloadd"]

Re-run the build:

`user `[`$`]`kubler build larry/openldap -nF`

»\[✔\]»\[larry/openldap\]» done.

At this point the image should exist in the local Docker/Podman registry and be ready for use:

`user `[`$`]`docker images`

    REPOSITORY                                              TAG                       IMAGE ID       CREATED          SIZE
    larry/openldap                                          20230704                  09347c55282b   2 minutes ago    56.4MB
    larry/openldap                                          latest                    09347c55282b   2 minutes ago    56.4MB

### [Pushing Images to a Docker Repository]

To push images to Docker Hub:

`user `[`$`]`kubler push larry/openldap larry/openldap`

The default assumes that the given namespace equals the respective Docker Hub account names, i.e. openldap and larry. To override this you may place a [push.conf] file in each namespace dir with the following format:

[FILE] **`push.conf`**

    DOCKER_LOGIN=larrythecowl
    DOCKER_PW=$uP3rsecretC0wPa$$w0rd
    #DOCKER_EMAIL=Larry.the.Cow@gentoo.zip

## [Ebuild Development with Kubler]

Kubler may be used to develop against any ebuild repository. Create a new namespace, let\'s call it [edev]:

`user `[`$`]`kubler new namespace edev`

Create a new builder, select `kubler/bob` as `IMAGE_PARENT`:

`user `[`$`]`kubler new builder edev/bob`

Edit the new builder\'s [build.sh] and add any additional repositories:

** Note**\
For [::gentoo] only there\'s no need to add the repo, it\'s already available; binding in the development fork and updating [.bashrc] is probably desirable, however.

[FILE] **`/config/build.sh`**

    configure_builder()

Create a new image, let\'s call it bench, use `kubler/bash` as `IMAGE_PARENT`:

`user `[`$`]`kubler new image edev/bench`

Edit the new image\'s build.conf and configure the builder and ebuild repo to be mounted builder:

[FILE] **`/config/build.conf`**

    BUILDER="edev/bob"
    BUILDER_MOUNTS=(
        "/data/development/ebuild-repos/gentoo:/var/db/repos/gentoo"
        "/data/development/ebuild-repos/kubler-overlay:/var/db/repos/kubler"
    )

Start an interactive build container and get tinkering:

`user `[`$`]`kubler build -i edev/bench`

`root `[`#`]`ebuild dev-lang/foo/foo-0.4.0.ebuild manifest merge`

## [Updating Build Containers]

Portage is updated frequently and the cached ebuild repository will quickly become stale. To check for new releases:

`user `[`$`]`kubler update`

This will also check for updates to the example images provided by Kubler, usually updated at the end of each month. If updates were found found simply rebuild the stack by running:

`user `[`$`]`kubler clean`

`user `[`$`]`kubler build -C namespace`

## [External resources]

\* [Building Hardened Docker Images from Scratch with Kubler](https://www.elttam.com/blog/kubler/)