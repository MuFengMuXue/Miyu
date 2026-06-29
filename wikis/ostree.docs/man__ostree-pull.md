## Name

ostree-pull — Download data from a remote repository

## Synopsis

`ostree pull {REMOTE} [BRANCH]`

## Options

`--commit-metadata-only`  
Fetch only the commit metadata.

`--cache-dir`=DIR  
Use an alternate cache directory in `DIR`.

`--disable-fsync`  
Do no invoke fsync().

`--localcache-repo`  
Like git's `clone --reference`. Reuse the provided OSTree repo as a local object cache when doing HTTP fetches. May be specified multiple times.

`--untrusted`  
Do not trust local sources, verify checksums and don't hardlink into source.

`--disable-static-deltas`  
Do not use static deltas.

`--mirror`  
Write refs suitable for a mirror, i.e. refs are stored in the `heads/` directory rather than the `remotes/` directory. This makes the target repo suitable to be exported for other clients to pull from as an ostree remote. If no specific refs are specified, all refs will be fetched (the remote must have a summary file present).

`--subpath`=SUBPATH  
Only pull the provided subpath.

`--depth`=DEPTH  
Traverse DEPTH parents (-1=infinite) (default: 0).

`--network-retries`=N  
Specifies how many times each download should be retried upon error (default: 5)

`--disable-retry-on-network-errors`  
Do not retry when network issues happen, instead fail automatically. (Currently only affects libcurl)

`--low-speed-limit-bytes`=N  
The average transfer speed per second of a transfer during the time set via 'low-speed-time-seconds' for libcurl to abort (default: 1000)

`--low-speed-time-seconds`=N  
The time in number seconds that the transfer speed should be below the 'low-speed-limit-bytes' setting for libcurl to abort (default: 30)

`--max-outstanding-fetcher-requests`=N  
The max amount of concurrent connections allowed. (default: 8)

`--disable-verify-bindings`  
Disable verification of commit metadata bindings.

## Description

Without --mirror, this command will create new refs under `remotes/REMOTE/` directory for each pulled branch unless they are already created. Such refs can be then referenced by `REMOTE:BRANCH` in `ostree` subcommands (e.g. `ostree log origin:exampleos/x86_64/standard`).

This command can retrieve just a specific commit, or go all the way to performing a full mirror of the remote repository. If no `BRANCH` is specified, all configured branches are retrieved.

A special syntax in the `@` character allows specifying a specific commit to retrieve from a branch. The use cases for this are somewhat similar to pulling a specific git tag; one could e.g. script a system upgrade to a known-good version, rather than the latest from the content provider.

## Example

**\$ ostree --repo=repo pull --depth=-1 --mirror remote_name**

Perform a complete mirror of the remote. (This is likely most useful if your repository is also `archive` mode)

**\$ ostree --repo=repo pull remote_name exampleos/x86_64/standard**

Fetch the most recent commit to `exampleos/x86_64/standard`.

**\$ ostree --repo=repo pull remote_name exampleos/x86_64/standard@98ea6e4f216f2fb4b69fff9b3a44842c38686ca685f3f55dc48c5d3fb1107be4**

Download the specific commit starting with `98ea6e` as if it was the latest commit for `exampleos/x86_64/standard`.
