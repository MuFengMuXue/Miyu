# Snort

From the project website:
:Snort is the foremost Open Source Intrusion Prevention System (IPS) in the world. Snort IPS uses a series of rules that help define malicious network activity and uses those rules to find packets that match against them and generates alerts for users.

## Preamble
* A Snort setup that sniffs WAN  LAN is more difficult to use. It does not show you which computer triggered the alert, and it requires you to set HOME_NET as your WAN IP address, which can change if your modem uses DHCP.
* Snort will bridge the two interfaces for you, you will not need to configure this.

You can use Snort to sniff wireless traffic with two routers. For simplicity the router with DHCP on and wireless off will be called "router A" and the router with wireless on and DHCP off "router B".

* Ensure the routers do not have the same IP address, but are on the same subnet.
* If the machine running Snort is configured for inline mode, you will need 3 network interface cards. One for management, one for incoming traffic, and one for outgoing traffic.
* Connect an ethernet cord from router B to a spare NIC on the Snort machine.
* Connect another ethernet cord from router A to a spare NIC on the Snort machine.
* Once Snort is running traffic should flow from router B  Snort machine  router A  internet.
* If you are not using inline mode, then the traffic will need to be forwarded to the Snort machine, see: Port Mirroring

## Installation
Install the  package.

Cisco Telos team also provides a Docker image: == Configuration ==

The main configuration file is located at .

Local configuration can be set in . It is recommended to use  to download your rule set. By default the rules are stored under, $RULE_PATH/snort.rules.

Home network can be set in . If required, let Snort know what network (or networks) you want to monitor.
 HOME_NET =  10.0.0.0/8 172.16.0.0/12 192.168.0.0/16

## Inline mode
Inline mode means that packets pass through snort, rather than being diverted to snort. In this mode, snort can drop packets and abort exploitation attempts in real-time. In this mode, snort acts as an intrusion prevention system (IPS).

By default, snort runs in inline mode, which is defined as under in :
 daq =
 {
    modules =
    {
        {
            name = 'afpacket',

            --For netfilter (NFQUEUE) based IPS
            --name = 'nfq',

            mode = 'inline',
        },
    },
    module_dirs =
    {
        '/usr/lib/daq',
    },
 }

 ips =
 {
    mode = inline,
    ...
 }

## IDS mode
In intrusion detection mode (IDS), packets are diverted to snort. Snort can not drop packets, which means that it can only notify you that a exploitation attempt is occuring, or have already occured.

In IDS mode start .

## Updating the rules with Pulledpork
Install .

## Configuration
The configuration files are located in

Edit  and uncomment the rules you want to use. You will need an "oinkcode" to download some of the rules.

*  any rules matched in this file will have its traffic dropped.
*  is used to enable signatures. All signatures seem to be enabled by default, no need to edit this file.
*  is used to completely remove a signature from Snort.

The current categories that are within your rule set can be found by running the following:

 $ pulledpork.pl -c /etc/snort/pulledpork.conf -Pw
 $ zgrep -E '\.rules' /var/tmp/*.gz | cut -d'/' -f3 | sort -u | perl -lne '/(.*).rules/ && print $1' > rules.`date +%F`

## Drop traffic with Pulledpork
If you want to drop all traffic that matches a Snort signature instead of just alerting, add the following to your :
 pcre:.

Or if you want to drop all traffic matching an entire category:
 policy-social
 policy-other
 file-other

If you only want to drop a single rule:
 118:7

## Disabling rules with Pulledpork
If you want to disable a single signature add its gen_id and sig_id to
 118:22

If you want to disable an entire category:
 deleted
 protocol-icmp
 policy-social
 policy-other

## Running Pulledpork
This will pull the new rules and write them to
 pulledpork.pl -c /etc/pulledpork/pulledpork.conf  -P

## Update the rules: Oinkmaster
There are two sets of rules distributed by Snort: "Community Ruleset" and "Snort Subscriber Rule Set". The former one is freely available to all of the users. The latter one is made available to subscribed and registered users. Paid subscribers receive rulesets in real-time as they are released. Registered users will receive rulesets 30 days after the subscribers. Registration is free and available at: [https://snort.org/users/sign_up Snort: Sign up.

The  package is available.

## Oinkmaster setup
Edit  and look for the URL section and uncomment the 2.4 line. Make sure to replace '''' by the Oink code you generated after logging into your Snort account. For Bleeding Snort rules, uncomment the appropriate line.

When you log into your new account, create an "Oink code".
Another thing to change is
 use_external_bins=1 # 1 uses wget, tar, gzip instead of Perl modules

The rest of the configuration file is fine.

## Oinkmaster usage
 oinkmaster.pl -o /etc/snort/rules

Create an executable script with the exact command and place it in /etc/cron.daily to update the rules daily automatically.
