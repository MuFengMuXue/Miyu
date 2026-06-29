VPN services are offered by several companies. They allow users to protect their privacy and security while using the Internet. Guides to using various service providers on Gentoo are below.

** Important**\
VPN services are not an absolute privacy or security solution. The service allows a system to act as if it was at the VPN host\'s location. Anything beyond the VPN is subject to the standard rules of the Internet. Some VPN services have been known to collect data and, in extreme cases, sell it for profit. Always do research on each option and understand what such a service really does.

## Contents

-   [[1] [Private Internet Access]](#Private_Internet_Access)
-   [[2] [Free VPN]](#Free_VPN)
    -   [[2.1] [Troubleshooting]](#Troubleshooting)
-   [[3] [Troubleshooting]](#Troubleshooting_2)
-   [[4] [Windows L2TP/IPsec VPN]](#Windows_L2TP.2FIPsec_VPN)
-   [[5] [VPN on your remote machine or cloud]](#VPN_on_your_remote_machine_or_cloud)

## [Private Internet Access]

[https://www.privateinternetaccess.com/](https://www.privateinternetaccess.com/)

The following will auto-start [openvpn](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN") upon boot:

1.  Buy a subscription and log in

2.  :::: cmd-box


    `root `[`#`]`echo "net-vpn/openvpn passwordsave examples" >> /etc/portage/package.use # optional`


    ::::

3.  :::: cmd-box


    `root `[`#`]`emerge --ask openvpn`


    ::::

4.  Go to [https://www.privateinternetaccess.com/pages/client-control-panel](https://www.privateinternetaccess.com/pages/client-control-panel) and locate the \"PPTP/L2TP/SOCKS Username and Password\"

5.  Generate Username/Password if they are not there

6.  In the next step, replace USERNAME and PASSWORD with the located or generated ones.

    :::::: cmd-box


    `root `[`#`]`cd /etc/openvpn`





    `root `[`#`]`echo "USERNAME" >> login.conf`





    `root `[`#`]`echo "PASSWORD" >> login.conf`


    ::::::

7.  Download the privateinternetaccess configurations and certificates.

    ::::::::::: cmd-box


    `root `[`#`]`mkdir -p pia`





    `root `[`#`]`cd pia`





    `root `[`#`]`wget `[`https://www.privateinternetaccess.com/openvpn/openvpn.zip`](https://www.privateinternetaccess.com/openvpn/openvpn.zip)





    `root `[`#`]`unzip openvpn.zip`





    `root `[`#`]`cp US\ East.ovpn ../openvpn.conf # replace with your desired region`





    `root `[`#`]`cd ..`





    `root `[`#`]`ln -s pia/ca.rsa.2048.crt`





    `root `[`#`]`ln -s pia/crl.rsa.2048.pem`


    :::::::::::

8.  Modify the configuration file and permissions.

    ::::::: cmd-box


    `root `[`#`]`echo "auth-nocache" >> openvpn.conf`





    `root `[`#`]`echo "auth-user-pass login.conf" >> openvpn.conf`





    `root `[`#`]`chmod 600 openvpn.conf login.conf pia/*`





    `root `[`#`]`chmod 700 pia`


    :::::::

9.  Start the service and add to default runlevel.

    ::::: cmd-box


    `root `[`#`]`/etc/init.d/openvpn start`





    `root `[`#`]`rc-update add openvpn # don't use this line if you don't want openvpn upon boot`


    :::::

If [Openvpn](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN") doesn\'t connect you would want to add www.privateinternetaccess.com\'s DNS servers to your [/etc/resolv.conf.head] file. Create \'/etc/resolv.conf.head\' file if it doesn\'t already exist, edit the file by adding the two DNS servers:

[FILE] **`/etc/resolv.conf.head`**

    nameserver 209.222.18.222
    nameserver 209.222.18.218

Go to www.privateinternetaccess.com\'s to make sure you entered the correct DNS servers:

-   Click on \'Client Support Tab\' and scroll down to \'DNS leak protection\' section

Save and Reboot.

## [Free VPN]

[https://freevpn.me/](https://freevpn.me/)

1.  Go to [https://freevpn.me/accounts/](https://freevpn.me/accounts/) and click on \"Download OpenVPN Certificate Bundle\". You will get a zip file with the ovpn configuration files for all the Free VPN servers. .ovpn files are [Openvpn](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN") configuration files with the client configuration at the beginning of the file, followed by inlined certificates. Choose one of these servers and copy the corresponding directory into [/etc/openvpn] (You can use mc for that kind of task). I renamed the directory in order to get rid of the spaces in its name.
2.  On the website, click on the left menu to choose the server you want. When done click on \"Accounts\", as example [https://freevpn.me/accounts/](https://freevpn.me/accounts/) . On that page, you can read the user and password needed for that server in the Open VPN section. In the console do, as example for freevpn.me using udp on port 40000:
3.  To not get prompted for the username and password:

    :::: cmd-box


    `root `[`#`]`cd /etc/openvpn/1-FreeVPN.me-FR`


    ::::

    :::: cmd-box


    `root `[`#`]`echo "<username>" > auth`


    ::::

    :::: cmd-box


    `root `[`#`]`echo "" >> auth`


    ::::

    and change the line:

    ::: box-caption
    [FILE] **`/etc/openvpn/1-FreeVPN.me-FR/FreeVPN.me-UDP-40000.ovpn`**
    :::

    :::
        auth-user-pass
    :::

    into

    ::: box-caption
    [FILE] **`/etc/openvpn/1-FreeVPN.me-FR/FreeVPN.me-UDP-40000.ovpn`**
    :::

    :::
        auth-user-pass /etc/openvpn/1-FreeVPN.me-FR/auth
    :::
4.  You can test it with:

    :::: cmd-box


    `root `[`#`]`openvpn FreeVPN.me-UDP-40000.ovpn`


    ::::
5.  In order to run it at boot time, follow one of the methods described here: [OpenVPN#Gentoo_specifics](https://wiki.gentoo.org/wiki/OpenVPN#Gentoo_specifics "OpenVPN")

### [Troubleshooting]

It [Openvpn](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN") fail to connect with something like:

`root `[`#`]`openvpn FreeVPN.me-UDP-53.ovpn`

    ...
    TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)

it can be a firewall blocking you, but other vpn servers will fails too in that case. It other vpn servers are working, just try another configuration file. At that time of writing, FreeVPN.me-UDP-53 fails with that error, but FreeVPN.me-UDP-40000 is running just fine.

## [Troubleshooting]

The above setup requires that root has write permission on /etc/resolv.conf. To make sure this is the case run

`root `[`#`]`lsattr /etc/resolv.conf`

If the output looks like this

`root `[`#`]`lsattr /etc/resolv.conf`

    ----i---------e---- /etc/resolv.conf

than, since \"i\" means that the file has the immutable bit, not even the root can write on it. To change that just run

`root `[`#`]`chattr -i /etc/resolv.conf`

and reboot.

## [][Windows L2TP/IPsec VPN]

Users wishing to connect to their company\'s L2TP/IPsec network can follow the below guide. Assuming you are already running a gnome profile, follow these steps:

[FILE] **`/etc/portage/package.use`**

    net-vpn/strongswan -caps -non-root

`root `[`#`]`emerge --ask net-vpn/networkmanager-l2tp`

The USE flag modifications are necessary to bypass sepolicy issues with the charon daemon. These flags are not recommended if you\'re running an L2TP server (according to the ebuild).

## [VPN on your remote machine or cloud]

Multiple solutions exists, a few of them:

[https://github.com/trailofbits/algo](https://github.com/trailofbits/algo)

[https://amnezia.org/en](https://amnezia.org/en)