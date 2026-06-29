# Extensions / Libxt Nfacct

The nfacct match provides the extended accounting infrastructure for iptables. You have to use this match together with the standalone user-space utility **nfacct(8)**

The only option available for this match is the following:

**--nfacct-name** *name*
This allows you to specify the existing object name that will be use for accounting the traffic that this rule-set is matching.

To use this extension, you have to create an accounting object:

> nfacct add http-traffic

Then, you have to attach it to the accounting object via iptables:

> iptables -I INPUT -p tcp --sport 80 -m nfacct --nfacct-name http-traffic

> iptables -I OUTPUT -p tcp --dport 80 -m nfacct --nfacct-name http-traffic

Then, you can check for the amount of traffic that the rules match:

> nfacct get http-traffic

> { pkts = 00000000000000000156, bytes = 00000000000000151786 } = http-traffic;

You can obtain **nfacct(8)** from https://www.netfilter.org or, alternatively, from the git.netfilter.org repository.
