# Man / Nm Online

NetworkManager developers

nm-online

1

NetworkManager

General Commands Manual

nm-online

ask NetworkManager whether the network is connected

nm-online

OPTIONS

# Description

`nm-online` is a utility to find out whether we are online. It is done by asking NetworkManager about its status. When run, `nm-online` waits until NetworkManager reports an active connection, or specified timeout expires. On exit, the returned status code should be checked (see the return codes below).

This tool is not very useful to call directly. It is however used by `NetworkManager-wait-online.service` with `--wait-for-startup` argument (see [`NetworkManager-wait-online.service(8)`](#NetworkManager-wait-online.service)).

By default, connections have the `ipv4.may-fail` and `ipv6.may-fail` properties set to `yes`; this means that NetworkManager waits for one of the two address families to complete configuration before considering the connection activated. If you need a specific address family configured before `network-online.target` is reached, set the corresponding `may-fail` property to `no`.

# Options

`-h` `--help`
Print help information.

`-q` `--quiet`
Don't print anything.

`-s` `--wait-for-startup`
Wait for NetworkManager startup to complete, rather than waiting for network connectivity specifically. Startup is considered complete once NetworkManager has activated (or attempted to activate) every auto-activate connection which is available given the current network state. This corresponds to the moment when NetworkManager logs `"startup complete"`. This mode is generally only useful at boot time. After startup has completed, `nm-online -s` will just return immediately, regardless of the current network state.

There are various ways to affect when startup complete is reached. For details see [`NetworkManager-wait-online.service(8)`](#NetworkManager-wait-online.service).

`-t` `--timeout` \<seconds\>
Time to wait for a connection, in seconds. If the option is not provided, the environment variable `NM_ONLINE_TIMEOUT` is honored. The default timeout is 30 seconds.

`-x` `--exit`
Exit immediately if NetworkManager is not running or connecting.

# Exit Status

`nm-online` exits with status 0 if it succeeds, a value greater than 0 is returned if an error occurs.

0
Success already online or connection established within given timeout.

1
Offline or not online within given timeout.

2
Unknown or unspecified error.

# See Also

[`nmcli(1)`](#nmcli), [`NetworkManager(8)`](#NetworkManager), [`NetworkManager-wait-online.service(8)`](#NetworkManager-wait-online.service).
