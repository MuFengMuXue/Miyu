A reusable [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot") environment can be prepared using a snapshot of a [btrfs file system](https://wiki.gentoo.org/wiki/Btrfs "Btrfs"), a subdirectory, or a container, with [[[sys-apps/bubblewrap]](https://packages.gentoo.org/packages/sys-apps/bubblewrap)[]].

## [Preparing a chroot environment]

To create the snapshot, use the following command; the snapshot, subdirectory, or container, will be placed in [/mnt/gentoo]:

`root `[`#`]`btrfs subvolume create /mnt/gentoo`

[Get the stage 3 tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Downloading_the_stage_tarball "Handbook:AMD64/Installation/Stage"), then unpack stage 3 in it:

`root `[`#`]`cp stage3-*.tar.xz /mnt/gentoo `

`root `[`#`]`cd /mnt/gentoo `

`root `[`#`]`tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner `

When using a btrfs file system, space and operations will be saved by creating a snapshot:

`root `[`#`]`btrfs subvolume snapshot /mnt/gentoo /mnt/stage3`

If using a container, chroot using the following:

`root `[`#`]`bwrap --bind /mnt/gentoo / --dev /dev --proc /proc --perms 1777 --tmpfs /dev/shm --ro-bind /etc/resolv.conf /etc/resolv.conf /bin/bash --login`

If not, chroot following [Chrooting in the Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Chrooting "Handbook:AMD64/Installation/Base"). Then set up a stable Gentoo from stage 3 by following [Chrooting in the Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Chrooting "Handbook:AMD64/Installation/Base"). Inside the chroot (or container), install [[[dev-util/pkgcheck]](https://packages.gentoo.org/packages/dev-util/pkgcheck)[]], [[[dev-util/pkgdev]](https://packages.gentoo.org/packages/dev-util/pkgdev)[]], and Portage, with the `gentoo-dev` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") enabled:

`root `[`#`]`echo "sys-apps/portage gentoo-dev" >> /etc/portage/package.use/portage `

`root `[`#`]`emerge -1av sys-apps/portage dev-util/pkgcheck dev-util/pkgdev `

At this point, if using a btrfs file system, exit the chroot / container and then make a snapshot:

`root `[`#`]` btrfs subvolume snapshot /mnt/gentoo /mnt/stable_stage3`

The original subvolume may then be deleted.

## [Testing the package foo]

If using a btrfs filesystem, create a snapshot of the stable stage 3 and chroot into it. If not, just chroot into the stable stage 3:

`root `[`#`]`btrfs subvolume snapshot /mnt/stable_stage3 /mnt/foo`

For a chroot:

`root `[`#`]`mount --types proc /proc /mnt/foo/proc `

`root `[`#`]`mount --rbind /sys /mnt/foo/sys `

`root `[`#`]`mount --make-rslave /mnt/foo/sys `

`root `[`#`]`mount --rbind /dev /mnt/foo/dev `

`root `[`#`]`mount --make-rslave /mnt/foo/dev `

`root `[`#`]`chroot /mnt/foo /bin/bash `

You can have such script in the root of your chroot directory:

[FILE] **`/mychroot/chroot.sh`**

    mount --rbind /dev dev
    mount --make-rslave dev
    mount -t proc /proc proc
    mount --rbind /sys sys
    mount --make-rslave sys
    mount --rbind /tmp tmp
    mount --bind /run run

    mount -o bind /var/db/repos/ var/db/repos/
    mount -o bind /var/cache/distfiles/ var/cache/distfiles/

    chroot . /bin/bash

For a container:

`root `[`#`]`bwrap --bind /mnt/gentoo / --dev /dev --proc /proc --perms 1777 --tmpfs /dev/shm --ro-bind /etc/resolv.conf /etc/resolv.conf /bin/bash --login`

When testing multiple packages, renaming the prompt according to the package in testing phase can prove useful:

`root `[`#`]` export PS1="(foo) $"`

Next, [create a custom repository](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/CustomTree#Defining_a_custom_repository "Handbook:AMD64/Portage/CustomTree") and copy in the ebuild to be tested. Before testing the package ` foo/bar `, emerge all its test dependencies:

`root `[`#`]` emerge -1av --onlydeps --with-test-deps foo`

Then make the adjustments of the [make.conf] from [Package testing](https://wiki.gentoo.org/wiki/Package_testing "Package testing"), and then emerge the package:

`root `[`#`]` emerge -1av foo`

Once testing is done, the btrfs file system may be deleted:

`root `[`#`]` btrfs subvolume delete /mnt/foo`

If using another file system, execute the following after each test to get back to a stable stage 3:

`root `[`#`]` emerge --depclean`

## [Keeping up to date]

To keep a stable_stage3 up to date, it is possible to chroot into it and execute the following command:

`root `[`#`]` emerge --sync && emerge --quiet --update --deep --newuse @world `

Alternatively, set up a new stable stage 3 using the instructions from the beginning of this article.