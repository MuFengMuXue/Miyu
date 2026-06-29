# Static deltas for offline updates

OSTree supports generating “self-contained” static delta files, via an invocation similar to the following:

``` highlight
$ ostree --repo=/path/to/repo static-delta generate --min-fallback-size=0 --filename=delta-update-file --from=<from> <to>
```

Note the usage of `--min-fallback-size=0` to ensure that the delta is self-contained.

Then, you can copy `delta-update-file` to a USB key or similar, and a target system can apply it via e.g.:

``` highlight
$ ostree --repo=/ostree/repo static-delta apply-offline /path/to/delta-update-file
```

The above invocation will merely apply the content into the repository. To make it bootable, this will then need to be further followed up by e.g. `ostree admin deploy <to>` or with a higher level tool such as `rpm-ostree`, via `rpm-ostree deploy :<to>`.
