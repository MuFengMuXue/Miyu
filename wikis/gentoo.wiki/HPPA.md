[] This article is a **work in progress**; treat its contents with caution - [immolo](https://wiki.gentoo.org/wiki/User:Immolo "User:Immolo") ([talk](https://wiki.gentoo.org/wiki/User_talk:Immolo "User talk:Immolo") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/immolo "Special:Contributions/immolo")).

A collection of handy hints for HPPA Gentoo users.

## [QEMU install]

First enable HPPA system support in [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]]:

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu QEMU_SOFTMMU_TARGETS: hppa

Then rebuild [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]]:

`root `[`#`]`emerge --ask app-emulation/qemu`

### [Boot installcd]

First download the hppa installcd from your local mirror at [https://gentoo.org/downloads/mirrors/](https://gentoo.org/downloads/mirrors/)

then, create an image to use as a hard drive source:

`user `[`$`]`qemu-img create -f qcow2 gentoo-hppa.qcow2 30G`

Next, you can boot the installcd with:

`user `[`$`]`qemu-system-hppa -drive file=gentoo-hppa.qcow2 -drive file=<Gentoo ISO location>,media=cdrom -boot order=d -nographic -serial mon:stdio -accel tcg,thread=multi -smp cpus=2`

### [Stage3]

[qemu-system-hppa] as of 2024-08-24. only supports 32bit installs so use the hppa-1.1 stage tarballs.