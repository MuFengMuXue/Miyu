## Name

systemd.image-filter — Disk Image Dissection Filter

## Description

In systemd, whenever a disk image (DDI) implementing the UAPI.2 Discoverable Partitions Specification is activated, a filter may be specified controlling which partitions to consider for mounting. Such a disk image dissection filter is a string that contains per-partition-type patterns, separated by colons ("`:`"). The individual rules consist of a partition identifier, an equal sign ("`=`"), and a shell globbing pattern applied to the GPT label string of the partition. See glob(7) for details on shell globbing.

The partition identifiers currently defined are: `root`, `usr`, `home`, `srv`, `esp`, `xbootldr`, `swap`, `root-verity`, `root-verity-sig`, `usr-verity`, `usr-verity-sig`, `tmp`, `var`. These identifiers match the relevant partition types in the Discoverable Partitions Specification, but are agnostic to CPU architectures.

## Use

Various systemd components that support operating with disk images support a `--image-filter=` command line option to specify the image filter to use. If no filter is specified all partitions in partition table are considered and no per-label filtering is applied (except that partitions with the "`_empty`" label are always ignored).

For the host root file system image itself systemd-gpt-auto-generator(8) is responsible for processing the GPT partition table and making use of the included discoverable partitions. It accepts an image filter via the kernel command line option `systemd.image_filter=`.

## Examples

The following image filter string dictates that for the root file system partition only partitions shall be considered whose label begins with "`ParticleOS-`". For the `/usr/` partition the precise label "`ParticleOS_47110815`" is required.

``` programlisting
root=ParticleOS-*:usr=ParticleOS_47110815
```

## See Also

systemd(1), systemd-dissect(1), systemd-gpt-auto-generator(8), systemd.image-policy(7)
