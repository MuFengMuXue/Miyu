SSH reverse tunneling is a method of forwarding any type of traffic **from a remove machine to your local laptop** - so you can have, for example, [AWS free tier](https://aws.amazon.com/free/) with static ipv4/ipv6 - and calls to that IP will be forwarded to your laptop (and answers from your laptop back to the client). It can be useful if you want to share something directly from your laptop but you are behind [NAT](https://wiki.gentoo.org/wiki/NAT "NAT") (most ISP have this - because of [IPv4 address exhaustion](https://en.wikipedia.org/wiki/IPv4_address_exhaustion)) and without static IP at your home. Another direction - tunneling *from your local laptop to remove machine* is called [SSH tunneling](https://wiki.gentoo.org/wiki/SSH_tunneling "SSH tunneling").

### [][Server (remote with static IP)]

[FILE] **`/etc/ssh/sshd_config`Make sure to have GatewayPorts yes**

    Port 22
    UsePAM yes
    PrintMotd no
    AcceptEnv LANG LC_*
    AllowTcpForwarding yes
    AllowAgentForwarding no
    AllowStreamLocalForwarding yes
    PermitTunnel yes
    GatewayPorts yes

### [][Client (your laptop)]

How to connect without a config file:

`user `[`$`]`ssh -i key.pem -R :localhost: algo@xx.xx.xx.xx -p <for-for-connecting>`

It can be simplier with config file that is supplied by **-F**

[FILE] **`ssh_config_reverse_tunnel`Port 63368 of remote incoming will be forwarded to your local port 8000**

    Host xx.xx.xx.xx
      User user
      Port 22
      IdentitiesOnly yes
      IdentityFile /path/to/key.pem
      KeepAlive yes
      ServerAliveInterval 30
      RemoteForward 63368 localhost:8000

And now you command is shorter:

`user `[`$`]`ssh -F ssh_config_reverse_tunnel xx.xx.xx.xx`

It works even if you connected to the same machine by [VPN](https://wiki.gentoo.org/wiki/VPN "VPN").

### [See also]

[SSH tunneling](https://wiki.gentoo.org/wiki/SSH_tunneling "SSH tunneling")

[https://serveo.net](https://serveo.net): SSH reverse tunneling as-a-service

[man](https://linux.die.net/man/1/ssh)