# Doc / Additional Commands

LIST HOOKS
~~~~~~~~~~

This shows the list of functions that have been registered for the
given protocol family, including functions that have been
registered implicitly by kernel modules such as nf_conntrack. +

____
`list hooks` ['family']
`list hooks netdev` [ `device` 'DEVICE_NAME' ]
____

`list hooks` is enough to display everything that is active
on the system.  Hooks in the netdev family are tied to a network
device.  If no device name is given, nft will query all network
devices in the current network namespace.
Example Usage:


## .List All Active Netfilter Hooks In Either The Ip Or Ip6 Stack
% nft list hooks inet
family ip {
        hook prerouting {
                -0000000400 ipv4_conntrack_defrag [nf_defrag_ipv4]
                -0000000200 ipv4_conntrack_in [nf_conntrack]
                -0000000100 nf_nat_ipv4_pre_routing [nf_nat]
        }
        hook input {
                 0000000000 chain inet filter input [nf_tables]
                +0000000100 nf_nat_ipv4_local_in [nf_nat]

## [..]

The above shows a host that has nat, conntrack and ipv4 packet
defragmentation enabled.
For each hook location for the queried family a list of active hooks
using the format +

`priority` `identifier` [`module_name`]

will be shown.

The `priority` value dictates the order in which the hooks are called.
The list is sorted, the lowest number is run first.

The priority value of hooks registered by the kernel cannot be changed.
For basechains registered by nftables, this value corresponds to the
`priority` value specified in the base chain definition.

After the numerical value, information about the hook is shown.
For basechains defined in nftables this includes the table family,
the table name and the basechains name.
For hooks coming from kernel modules, the function name is used
instead.

If a `module name` is given, the hook was registered by the kernel
module with this name.  You can use 'modinfo `module name`' to
obtain more information about the module.

This functionality requires a kernel built with the option +
CONFIG_NETFILTER_NETLINK_HOOK
enabled, either as a module or builtin. The module is named
`nfnetlink_hook`.

MONITOR
~~~~~~~
The monitor command allows you to listen to Netlink events produced by the
nf_tables subsystem. These are either related to creation and deletion of
objects or to packets for which `meta nftrace` was enabled. When they
occur, nft will print to stdout the monitored events in either JSON or
native nft format. +

____
`monitor` [`new` | `destroy`] 'MONITOR_OBJECT'
`monitor` `trace`

'MONITOR_OBJECT' := `tables` | `chains` | `sets` | `rules` | `elements` | `ruleset`
____

To filter events related to a concrete object, use one of the keywords in
'MONITOR_OBJECT'.

To filter events related to a concrete action, use keyword `new` or `destroy`.

The second form of invocation takes no further options and exclusively prints
events generated for packets with `nftrace` enabled.

Hit ^C to finish the monitor operation.


## .Listen To All Events, Report In Native Nft Format

## % Nft Monitor


## .Listen To Deleted Rules, Report In Json Format

## % Nft -J Monitor Destroy Rules


## .Listen To Both New And Destroyed Chains, In Native Nft Format

## % Nft Monitor Chains


## .Listen To Ruleset Events Such As Table, Chain, Rule, Set, Counters And Quotas, In Native Nft Format

## % Nft Monitor Ruleset


## .Trace Incoming Packets From Host 10.0.0.1
% nft add rule filter input ip saddr 10.0.0.1 meta nftrace set 1

## % Nft Monitor Trace
