# Netbird

NetBird is an open-source VPN management platform built on top of WireGuard making it easy to create secure private networks for your organization or home. It is very similar to Tailscale, and has very similar features.

Netbird can be self-hosted.

## Initial network setup
Sign up for an account, and then install netbird on each of your devices. By signing up for an account, a virtual network will be created automatically.

## Installation
Install .

## Join the network
The netbird service is installed as a template unit. Create a default instance by starting/enabling , then join the network:

 # netbird up

If communication with the management server is successful, it will print a URL. Open it in a browser and sign in with your account credentials if needed. Follow the prompt on the browser, after which a success message will be printed on the console.

Just like Tailscale, it is possible to use a setup key to add a node:

 # netbird up --setup-key 2CA35F84-3D54-4997-884D-FE72864ACFD7

## Troubleshooting
## Network inaccessible
One possible cause is conflict with Tailscale. By default, the Tailscale service will create firewall entries to filter traffic within the virtual network. All traffic originating from Tailscale's subnet must come from Tailscale's network interface. However, Tailscale and Netbird both use the same  subnet, thus Tailscale traffic will work fine, but Netbird traffic will be completely blocked.

This is the offending rule:

 -A ts-input -s 100.64.0.0/10 ! -i tailscale0 -j DROP

Removing this rule on all affected nodes resolves the issue. However, this is not a permanent solution. Instead, disable the iptables rules entirely:

 # tailscale up --netfilter-mode off

A better solution would be to use different subnets for Tailscale and Netbird, but at the moment they are not supported:
* https://github.com/tailscale/tailscale/issues/183
* https://github.com/netbirdio/netbird/issues/446

## DNS and routing issues with systemd-networkd
When using systemd-networkd, NetBird's policy routing rules may be removed during DHCP renewals, sleep/wake cycles, or network reconfigurations. This causes DNS forwarding through the VPN tunnel to fail.

The root cause is  (the default), which makes systemd-networkd remove routing policy rules it did not create.

Create :

Then restart .

See netbird issue #4578 for more details.
