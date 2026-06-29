Other languages:

[English] • ‎[русский](//wiki.manjaro.org/index.php?title=Networking/ru "Сетевое взаимодействие (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Manually Setting DNS Servers]](#Manually_Setting_DNS_Servers)
    -   [[2.1] [NetworkManager]](#NetworkManager)
        -   [[2.1.1] [Use resolvconf]](#Use_resolvconf)
    -   [[2.2] [/etc/resolvconf.conf]](#.2Fetc.2Fresolvconf.conf)
    -   [[2.3] [dhcpcd and resolv.conf.head/tail]](#dhcpcd_and_resolv.conf.head.2Ftail)
-   [[3] [Setting Static IP Address]](#Setting_Static_IP_Address)
    -   [[3.1] [Using a GUI Tool]](#Using_a_GUI_Tool)
    -   [[3.2] [Using systemd]](#Using_systemd)
-   [[4] [Using dhcpcd Instead of NetworkManager]](#Using_dhcpcd_Instead_of_NetworkManager)
-   [[5] [See Also]](#See_Also)

# [Overview]

Networking on Manjaro generally works out of the box without any special user intervention. This article presents some specialized circumstances which some users may encounter and provides advice on how to overcome them.

\

# [Manually Setting DNS Servers]

Usually, your DNS servers will be provided by your ISP automatically through DHCP. However, sometimes it nesecary to use different DNS servers than the ones provided by your ISP. In this situation you may find that your DNS or other non-standard nameserver addresses will get reset on reboot as `/etc/resolv.conf` can be overwritten by NetworkManager or during the boot process. Here we will look at some techniques to preserve your settings.

\

## [NetworkManager]

If you are using NetworkManager, this is one solution to the problem. The NetworkManager\'s config drop folder is placed in `/etc/NetworkManager/conf.d`. In this folder you can place snippets which controls how NetworkManager works. The files should be named with a number and a description of its purpose and always end with `.conf`. The files are then applied in numerical order from the lowest to the highest. A configuration in a file with a higher number will override what could have been configured in a lower numbered file.

### [Use resolvconf]

To have the resolvconf script handle the resolv.conf file for NetworkManager. Create a configuration file in NetworkManager\'s config drop folder

    /etc/NetworkManager/conf.d/20-rc-manager.conf

Save the file with this content

    [main]
    rc-manager=resolvconf

To effectively make DNS handling a manual task create a file named

    /etc/NetworkManager/conf.d/99-dont-touch-my-dns.conf

Save the file with this content

    [main]
    dns=none

\

## [][/etc/resolvconf.conf]

The resolvconf.conf file is a shell script that is sourced by resolvconf, meaning that resolvconf.conf must contain valid shell commands. Take a look at its [man page](https://jlk.fjfi.cvut.cz/arch/manpages/man/resolvconf.conf.5) for more details and commands. The file is located at `/etc/resolvconf.conf` and will require root privelege to edit. For more information on how to edit a configuration file owned by root, please review [this article](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files "Viewing and editing configuration files").

\
As an example, we will prepend OpenDNS nameservers to the top of our resolvconf file whenever called. We can achieve this by adding the following lines to the bottom of resolvconf.conf.

    # OpenDNS servers
    name_servers="208.67.222.222 208.67.220.220"

\
After making any changes simply update and apply your settings with the following command

[user \$ ][ sudo resolvconf -u [COPY TO CLIPBOARD]]

\

## [][dhcpcd and resolv.conf.head/tail]

**Note**

------------------------------------------------------------------------

Most Manjaro installs will not be using dhcpd by default

\
An alternative solution if you are using dhcpd is to input our settings to the `/etc/resolv.conf.head` file. If this file does not exist then create it. The contents of `/etc/resolv.conf.head` get sent to the top of `/etc/resolv.conf` during the boot process.

\
Following our previous example, if we want to use the OpenDNS servers with this method, we could place the following in the file:

    # OpenDNS servers
    nameserver 208.67.222.222
    nameserver 208.67.220.220

\

# [Setting Static IP Address]

## [Using a GUI Tool]

Most editions of Manjaro come with some type a GUI tool or applet to manage NetworkManager. This is the easiest way to set a static IP. Simply go into the tool, usually in the system tray or menu, and input the required parameters for your network.

\

## [Using systemd]

If you don\'t want to use NetworkManager the next easiest thing is to configure a static IP in systemd.

\
First, make sure you aren\'t running NetworkManager

[user \$ ][ sudo systemctl disable \--now NetworkManager.service [COPY TO CLIPBOARD]]

\

\
Next you will need to find the name of your network device. To locate the name, use the command `ip a` as seen here:

    ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether 00:0c:29:02:55:c4 brd ff:ff:ff:ff:ff:ff
        inet 172.16.197.200/24 brd 172.16.197.255 scope global dynamic noprefixroute ens33
           valid_lft 1725sec preferred_lft 1725sec
        inet6 fe80::7116:2769:dac:6314/64 scope link noprefixroute
           valid_lft forever preferred_lft forever

\
lo is the loopback device which can be ignored for the purposes of this article. The device we need here is identified above as `ens33`. We will need this name in the next step.

\
Now create or edit a file to hold the network configuration at `/etc/systemd/network/devicename.network`. Using the example above, the file would be called `/etc/systemd/network/ens33.network`. This file will need to be created/edited as root. For more information on how to do that please review [this article](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files "Viewing and editing configuration files"). An example of the contents of the file would look like this:

    [Match]
    Name=enp0s3

    [Network]
    Address=192.168.1.101/24
    Gateway=192.168.1.1
    DNS=208.67.222.222
    DNS=208.67.220.220

\
All that remains is to start and enable the service using:

[user \$ ][ sudo systemctl enable \--now systemd-networkd.service [COPY TO CLIPBOARD]]

\

# [Using dhcpcd Instead of NetworkManager]

NetworkManager is the default solution for networking on most Manjaro editions. If you would prefer to use dhcpcd, that is also supported.

\
First, ensure NetworkManager is disabled and not running

[user \$ ][ sudo systemctl disable \--now NetworkManager.service [COPY TO CLIPBOARD]]

\

\
Next, start and enable the dhcpcd service

[user \$ ][ sudo systemctl start \--now dhcpcd.service [COPY TO CLIPBOARD]]

\

# [See Also]

-   [NetworkManager for Administrators](https://blogs.gnome.org/dcbw/2015/02/16/networkmanager-for-administrators-part-1/)
-   [Using resolvconf with NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager#Configure_NetworkManager_resolv.conf_management_mode_to_use_resolvconf)