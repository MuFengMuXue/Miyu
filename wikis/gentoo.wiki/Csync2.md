**Resources**

[[]][Home](https://github.com/LINBIT/csync2)

[[]][Package information](https://packages.gentoo.org/packages/sys-cluster/csync2)

[csync2] is a tool for asynchronous file synchronization in clusters.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Create ssl certificates for transfers]](#Create_ssl_certificates_for_transfers)
    -   [[2.2] [Create key for authentication with peers]](#Create_key_for_authentication_with_peers)
    -   [[2.3] [Setup synchronization]](#Setup_synchronization)
    -   [[2.4] [Things to note]](#Things_to_note)
    -   [[2.5] [Service]](#Service)
        -   [[2.5.1] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Sample parameters]](#Sample_parameters)
    -   [[3.2] [Invocation]](#Invocation)
        -   [[3.2.1] [Debug receiver]](#Debug_receiver)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [remote host remote_host did not accept my identification]](#remote_host_remote_host_did_not_accept_my_identification)
    -   [[4.2] [response from peer(/path/to/file): remote_host \[15\] \<- Permission denied!]](#response_from_peer.28.2Fpath.2Fto.2Ffile.29:_remote_host_.5B15.5D_.3C-_Permission_denied.21)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

Cannot load package information. Is the atom *sys-cluster/csync2* correct?

### [Emerge]

`root `[`#`]`emerge --ask sys-cluster/csync2`

## [Configuration]

### [Create ssl certificates for transfers]

`root `[`#`]`emerge --config sys-cluster/csync2`

### [Create key for authentication with peers]

`root `[`#`]`csync2 -k /etc/csync2/csync2.key_mygroup`

### [Setup synchronization]

[FILE] **`/etc/csync2/csync2.cfg`**

    group mygroup


### [Things to note]

-   All nodes (of a group) share a common key, for example [/etc/csync2/csync2.key_mygroup]. This means it has to be **copied** to each node.
-   The *shared* folder paths need to be identical for all nodes (of a group). The configuration file need *not* be identical.
-   Although the `host` parameter requires the actual `hostname` (or `ip`) to be used, it seems to work according to the [/etc/hosts] file.
    -   The following command shows what [csync2] sees as hostname:

    -   :::: cmd-box


        `root `[`#`]`csync2 -Tvv |& head`


        ::::

### [Service]

#### [OpenRC]

To enable the service to run at system boot:

`root `[`#`]`rc-update add csync2 default`

To start the daemon now:

`root `[`#`]`rc-service csync2 start`

## [Usage]

### [Sample parameters]

            -x [-d] [[-r] file..]   Run checks for all given files and update
                                    remote hosts.
            -d      Dry-run on all remote update operations
            -P peer1,peer1,...
                    Only update these peers (still mark all as dirty).
                    Only show files for these peers in -o (compare) mode.
            -f [-r] file..          Force files to win next conflict resolution.
            -r      Recursive operation over subdirectories.
            -M      List all dirty files from status db.

### [Invocation]

-   Update all with this one:
    -   :::: cmd-box


        `root `[`#`]`csync2 -x`


        ::::

    -   See failed changes:
        -   :::: cmd-box


            `root `[`#`]`csync2 -M`


            ::::
-   Dry-run an update towards `hostname3`:
    -   :::: cmd-box


        `root `[`#`]`csync2 -P hostname3 -xd`


        ::::

    -   Increased verbosity with [-vvv].
-   Force local files onto others:
    -   ::::: cmd-box


        `root `[`#`]`csync2 -fr /mnt/shared/force_these`





        `root `[`#`]`csync2 -x`


        :::::

#### [Debug receiver]

To see the messages of the receiver, after stopping any [csync2] daemon, for a single execution:

`root `[`#`]`csync2 -iii -vvv |& less`

## [Troubleshooting]

### [remote host remote_host did not accept my identification]

If working on both sides of an [iptables] [NAT] and getting this error from the inner side:

`root `[`#`]`csync2 -Tv this_host remote_host /path/to/file`

    Connecting to host remote_host (SSL) ...
    Connect to remote_ip:30865 (remote_host).
    ERROR: remote host remote_host did not accept my identification.
    Connection closed.
    Finished with 2 errors.

It might be because of this command on the router (that translates inner node addresses to the router\'s):

`root `[`#`]`iptables -t nat -A POSTROUTING -o $ -j MASQUERADE`

A solution to which, is to *prepend* the following, in order to exclude the `csync2` port:

`root `[`#`]`iptables -t nat -A POSTROUTING -o $ -p TCP --dport csync2 -j RETURN`

### [][response from peer(/path/to/file): remote_host \[15\] \<- Permission denied!]

Verify that the file mentioned is included in the remote host\'s [/etc/csync2/csync2.cfg].

## [See also]

-   [git](https://wiki.gentoo.org/wiki/Git "Git") --- widely used, open source, distributed [version control system](https://wiki.gentoo.org/wiki/Version_control_systems "Version control systems")
-   [rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") --- a powerful file sync program capable of efficient file transfers and directory synchronization.

## [External resources]

-   [Quickstart guide](https://github.com/LINBIT/csync2/blob/master/doc/csync2-quickstart.adoc)
-   [Documentation](https://github.com/LINBIT/csync2/blob/master/doc/csync2.adoc).