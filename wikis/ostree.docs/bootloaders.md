# Bootloaders

1.  [OSTree and bootloaders](#ostree-and-bootloaders)
2.  [OSTree and grub](#ostree-and-grub)
3.  [OSTree and aboot](#ostree-and-aboot)
4.  [GRUB and os-prober](#grub-and-os-prober)
5.  [Anaconda](#anaconda)
6.  [bootupd](#bootupd)

## OSTree and bootloaders

The intended design of OSTree is that it just writes new files into `/boot/loader/entries`. There is a legacy GRUB script (shipped on Fedora as `ostree-grub2`) that is intended only for the cases where the system GRUB does not support the `blscfg` verb.

In the happy path then, the flow of an OS update is just:

- ostree writes a new set of files in `/boot/loader/entries` (during `ostree-finalize-staged.service` on system shutdown)
- On system start, GRUB reads those files

And that’s it.

## OSTree and grub

For historical reasons, OSTree defaults to detecting the bootloader; if some GRUB files are present then OSTree will default to executing `grub2-mkconfig`.

## OSTree and aboot

The Android bootloader is another bootloader that may be used with ostree. It still uses the files in `/boot/loader/entries` as metadata, but the boootloader does not read these files. Android bootloaders package their kernel+initramfs+cmdline+dtb in a signed binary blob called an [Android Boot Image](https://source.android.com/docs/core/architecture/bootloader/boot-image-header). This binary blob then is written to either partition boot_a or boot_b depending on which slot is suitable.

Android bootloaders by design inject kargs into the cmdline, some patches may be required in the Android bootloader implementation to ensure that the firmware does not switch between system_a and system_b partitions by populating a `root=` karg, or that a `ro` karg is not inserted (this karg is incompatible with ostree).

We have two accompanying scripts that work with this type of environment:

[aboot-update](https://gitlab.com/CentOS/automotive/rpms/aboot-update) is used to generate Android Boot Images to be delivered to the client.

[aboot-deploy](https://gitlab.com/CentOS/automotive/rpms/aboot-deploy) reads what the current slot is according to the `androidboot.slot_suffix=` karg, writes to the alternate boot_a or boot_b slot and sets a symlink either /ostree/root.a or /ostree/root.b so that it is known which userspace directory to boot into based on the `androidboot.slot_suffix=` karg, on subsequent boots.

``` highlight
                                                           +---------------------------------+
+-----------------------------+    +------------------+    |                                 |
|  bootloader_a appends karg: |    |                  |    |                                 |
|                             +--->+ boot_a partition +--->+                                 |
|  androidboot.slot_suffix=_a |    |                  |    |           /ostree/root.a -> ... |
+-----------------------------+    +------------------+    |                                 |
                                                           | system partition                |
+-----------------------------+    +------------------+    |                                 |
|  bootloader_b appends karg: |    |                  |    |           /ostree/root.b -> ... |
|                             +--->+ boot_b partition +--->+                                 |
|  androidboot.slot_suffix=_b |    |                  |    |                                 |
+-----------------------------+    +------------------+    |                                 |
                                                           +---------------------------------+
```

## GRUB and os-prober

A specific component of GRUB that can significantly impede the reliability of OS updates is the `os-prober` aspect, which scans all system block devices. If one doesn’t care about dual booting, avoiding this is a good idea.

## Anaconda

Until very recently, the Anaconda project only supported setting up the bootloader (e.g. GRUB) on its own, which requires `grub2-mkconfig` etc. As of recently, Anaconda now [supports bootupd](https://github.com/rhinstaller/anaconda/pull/5298).

## bootupd

As of recently, [the bootupd project](https://github.com/coreos/bootupd/) ships [static grub configs](https://github.com/coreos/bootupd/tree/main/src/grub2) and in this case, the `sysroot.bootloader` should be set to `none` (except on s390x). And assuming that the system grub has the `blscfg` support, which it does on Fedora derivatives per above.
