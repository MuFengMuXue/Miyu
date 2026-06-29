The [emerge \--quickpkg-direct] and related [emerge \--quickpkg-direct-root] options are useful inside Dockerfiles. Here is an example Dockerfile that creates a minimal busybox image from a [stage 3](https://wiki.gentoo.org/wiki/Stage_tarball#Stage_3 "Stage tarball") [container image](https://hub.docker.com/r/gentoo/stage3), using [emerge \--quickpkg-direct=y] to avoid building anything from source:

[CODE] **example emerge invocation in a multi-stage Dockerfile**

    FROM docker.io/gentoo/stage3:musl-vanilla as buildtime
    RUN if [ ! -e /etc/portage/make.profile ]; then \
            mkdir -p $(realpath --canonicalize-missing /etc/portage/make.profile) || exit 1; \
            portage_version=$(portageq match / sys-apps/portage 2>/dev/null); \
            ( \
                printf -- 'ARCH='; \
                portageq metadata / installed "$" ARCH 2>/dev/null; \
            ) >> /etc/portage/make.profile/make.defaults; \
        fi; \
        env ACCEPT_KEYWORDS="**" QUICKPKG_DEFAULT_OPTS="--include-config=y" \
            emerge --root=/runtime-image --usepkgonly --quickpkg-direct=y --ignore-soname-deps=n busybox && \
        ln -s busybox /runtime-image/bin/sh

    FROM scratch
    COPY --from=buildtime /runtime-image /
    RUN /bin/busybox --list-applets | while read -r; do \
            [ "$" = "$" ] && target=../bin/busybox || target=busybox; \
            busybox ln -s "$" /$ &>/dev/null || true; \
        done
    CMD ["/bin/sh", "--login"]

The [emerge \--ignore-soname-deps=n] option ensures that emerge will account for soname dependencies, which will become the default in the future ([bug 687956](https://bugs.gentoo.org/687956)). However, there are no soname dependencies in this busybox image, because the busybox executable happens to be statically linked.

    $ podman build -f Dockerfile -t localhost/busybox:musl-vanilla --squash
    STEP 1: FROM docker.io/gentoo/stage3:musl-vanilla AS buildtime
    STEP 2: RUN if [ ! -e /etc/portage/make.profile ]; then       mkdir -p $(realpath --canonicalize-missing /etc/portage/make.profile) || exit 1;        [ -n "$(portageq envvar ARCH 2>/dev/null | sed '/^$/d')" ] || echo ARCH=amd64 >> /etc/portage/make.profile/make.defaults;    fi;     env ACCEPT_KEYWORDS="**" QUICKPKG_DEFAULT_OPTS="--include-config=y"         emerge --root=/runtime-image --usepkgonly --quickpkg-direct=y --ignore-soname-deps=n busybox &&     ln -s busybox /runtime-image/bin/sh
    unknown seccomp syscall `close_range` ignored
    unknown seccomp syscall `epoll_pwait2` ignored
    WARNING: One or more repositories have missing repo_name entries:

       /var/db/repos/gentoo/profiles/repo_name

    NOTE: Each repo_name entry should be a plain text file containing a
    unique name for the repository on the first line.

    Calculating dependencies  ... done!

    >>> Emerging binary (1 of 3) sys-libs/musl-1.2.1-r2::gentoo for /runtime-image/
    >>> Extracting info
    >>> Extracting sys-libs/musl-1.2.1-r2

    >>> Installing (1 of 3) sys-libs/musl-1.2.1-r2::gentoo to /runtime-image/

    >>> Emerging binary (2 of 3) virtual/libcrypt-1-r1::gentoo for /runtime-image/
    >>> Extracting info
    >>> Extracting virtual/libcrypt-1-r1

    >>> Installing (2 of 3) virtual/libcrypt-1-r1::gentoo to /runtime-image/

    >>> Emerging binary (3 of 3) sys-apps/busybox-1.32.1::gentoo for /runtime-image/
    >>> Extracting info
    >>> Extracting sys-apps/busybox-1.32.1

    >>> Installing (3 of 3) sys-apps/busybox-1.32.1::gentoo to /runtime-image/

    >>> Recording sys-apps/busybox in "world" favorites file...
    >>> Auto-cleaning packages...

    >>> Using system located in ROOT tree /runtime-image/

    >>> No outdated packages were found on your system.

     * GNU info directory index is up-to-date.
    --> b1fcfff9772
    STEP 3: FROM scratch
    STEP 4: COPY --from=buildtime /runtime-image /
    --> cdfed93bcfc
    STEP 5: RUN /bin/busybox --list-applets | while read -r; do        [ "$" = "$" ] && target=../bin/busybox || target=busybox         busybox ln -s ../bin/busybox /$ &>/dev/null || true;  done
    unknown seccomp syscall `close_range` ignored
    unknown seccomp syscall `epoll_pwait2` ignored
    --> 6812e38d3e4
    STEP 6: CMD ["/bin/sh", "--login"]
    STEP 7: COMMIT
    --> 3c9260e3351
    3c9260e33510bfad9597f7c8c34b5832e57d550986dea884ba41b2b8c90d4147
    $ podman images | grep localhost/busybox
    localhost/busybox                                                                                 musl-vanilla                      3c9260e33510  2 minutes ago  6.05 MB
    $ podman run --rm -it localhost/busybox:musl-vanilla sh -c 'tail /var/db/pkg/*/*/*DEPEND; tail /var/db/pkg/*/*/REQUIRES'
    ==> /var/db/pkg/sys-apps/busybox-1.32.1/DEPEND <==
    virtual/libcrypt:0/1= virtual/libcrypt[static-libs] >=sys-kernel/linux-headers-2.6.39

    ==> /var/db/pkg/sys-apps/busybox-1.32.1/RDEPEND <==
    virtual/libcrypt:0/1=

    ==> /var/db/pkg/virtual/libcrypt-1-r1/RDEPEND <==
    sys-libs/musl
    tail: can't open '/var/db/pkg/*/*/REQUIRES': No such file or directory
    tail: no files