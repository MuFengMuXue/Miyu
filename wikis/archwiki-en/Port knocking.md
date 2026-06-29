# Port knocking

Port knocking is a stealth method to externally open ports that, by default, the firewall keeps closed. It works by requiring connection attempts to a series of predefined closed ports. With a simple port knocking method, when the correct sequence of port "knocks" (connection attempts) is received, the firewall opens certain port(s) to allow a connection.

The benefit is that, for a regular port scan, it may appear as the service of the port is just not available. This article shows how to use port knocking with either a daemon, or with firewall rules only.

## Introduction
Installing and configuring nftables or iptables is a prerequisite for the content of this article.

The module recent in iptables is used to dynamically create list of IP addresses based on their (successful or unsuccessful) port connections. Using recent, the firewall can find out if a certain IP address has knocked the correct ports, and if that is the case, open certain port(s).

A session with port knocking may look like this:

It is wise to randomly select the ports that you use for the knock sequence. random.org can help you generate a selection of ports between 1 and 65535. To check that you have not inadvertantly selected commonly used ports, use this port database, and/or your  file.

## Simple port knocking
## Server side
## With a daemon helper
A specialised daemon can be used to handle port knocking. Besides easing the setup of rules these helper programs may also offer advanced features.

 is such a port knocking daemon that can provide an added layer of security to your network.  provides three example port knocking configurations.  These configs can be easily altered to integrate properly with an iptables firewall. If you followed Simple stateful firewall, you should substitute the  chain specification, with the custom  chain used in the firewall.

For example:

## With iptables only
In the following we construct an  file to handle port knocking for SSH. The rules are setup to open the standard SSH port 22 after a series of single knocks to the ports ,  and  in that order.

First we define the default filter policies and chains for this sample script. The OUTPUT ACCEPT is necessary in this example, because otherwise the SSH port could be opened, but traffic would be dropped - which defeats the purpose. The last three chains we require for the port knocking in the following rules.

Now we add the rules for the main chain, . The concept of port knocking is based on sending singular connect requests to the right ports in a sequence. We need ICMP for some network traffic control and to allow an established connection, e.g. to SSH.

The last of the above rules is the one to open the port 22 for 30 seconds, if the connecting IP is on the list . It can be on top of the chain, because it will only apply if this condition is met. It also introduces the first of the lists of connection attempts, which are used to track the port knocking sequence in the following. In this example, the port will be closed again after 30 seconds, but nothing else is triggered. So, a new port knocking attempt could be done from the same source IP.

If the last rule did not accept the traffic (e.g. no connection attempt in 30 seconds) but the connecting IP is on the correct list to allow , it is removed from that to knock again from the beginning. The removal directly after the check for the respective list is important for the correct handling of the sequence.

 -A TRAFFIC -m state --state NEW -m tcp -p tcp -m recent --name SSH2 --remove -j DROP

Now that the end of the sequence has been handled first, the following rules do the checking of the port sequence. For each of the ports to knock, one rule checks for the correct port in sequence. If the sequence is met, a jump occurs to where the IP is added to the list for the next knock in sequence. If no jump to  or  occured, it can only mean that the wrong port was knocked or (more likely) that it is some other traffic.  Hence, the second rule removes the IP from the list and drops the traffic, same as the rule for  before.

 -A TRAFFIC -m state --state NEW -m tcp -p tcp --dport 9991 -m recent --rcheck --name SSH1 -j SSH-INPUTTWO
 -A TRAFFIC -m state --state NEW -m tcp -p tcp -m recent --name SSH1 --remove -j DROP

The same procedure is followed for the next port to be knocked. The ordering of the sequence in the  chain can be any way, as long as the rules corresponding to the same list are kept together and in the right order.

 -A TRAFFIC -m state --state NEW -m tcp -p tcp --dport 7777 -m recent --rcheck --name SSH0 -j SSH-INPUT
 -A TRAFFIC -m state --state NEW -m tcp -p tcp -m recent --name SSH0 --remove -j DROP

In the final block of rules, the magic of setting the connection attempt for the IP to the respective recent list of allowed IPs for the next step of the knocking sequence is done.

The first is the one for the first knock in sequence, which is checked as part of the main chain  since any new connection attempt may be the start of a port knocking. On success (correct port) it sets the knock to the first list, . This in turn one can see in the last block of rules to be checked against, where the rule for checking the second knock (7777) requires a recent knock on the first port and only then may set the next recent list (). This switch brings the sequencing of the lists.

Note that the traffic is dropped in the last rules too, although a correct port is knocked. This DROP disguises that the connection attempt was a successful knock for any of them.

Now that the rules are complete, do a daemon-reload and restart  with with the rules.

Example of  file after running all the commands from above:

## With nftables only
Port knocking examples with nftables only.

## Client script
Now that configuration is done, to do the port knocking you will need a tool. , mentioned above, comes with the knock tool, which is simple and probably sufficient for many requirements. The upstream site has the knock tool for other OSs.

 can also be used here. A simple shell script () automates the port knocking:

Alternatively, you could use  and simply set a shell alias:

 alias knock="nc -z"

You can call all above methods with .

In the following we use the script. In order not to have adverse effects from other ongoing networking, this test has been done on localhost.

First, the IP for SSHD to listen to is setup, after pulling the network cable:

 ~# ip link set up dev enp8s0
 ~# ip address add 192.168.1.1/24 dev enp8s0
 ~# ip route add default via 192.168.1.1
 ~# systemctl status sshd |grep listening
 Aug 21 14:36:53 host sshdServer listening on 192.168.1.1 port 22

Second, it is checked if SSHD accepts connections and then the script is executed, followed by a successful SSH login:

The first connection attempt has to be stopped, because the DROP of the connection sends no reply. For testing purposes one can change the last rules' DROP to REJECT, which will return a  instead. Finally, right after the successful login, one can see the successful knocks in the kernel's recent lists:

## fwknop
 attempts to overcome some of the limitations mentioned above for simpler port knocking method. At the price of higher complexity and resource usage, mainly for the server to be protected. It provides port knocking and Single Package Authorization (SPA). It achieves its goals by using  and a cryptographic method. The usage of libpcap, which is the underlying library beneath tcpdump, enables it to examine all the incoming packets. Including packets the firewall does not let through. And including packets that no service is openly listens to. The usage of cryptography prevents an attacker from bypassing fwknop by retransmitting previous packets.
