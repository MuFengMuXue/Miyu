**Article status**

[[]]This article needs wikification.

**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

Juniper\'s Network Connect document to describe the setup running on a 64-bit linux client. This describes a method to setup a client VPN connection using a webbrowser (SSL VPN). Documentation of a working setup as of October 2013 on a target network that requires login via a web page, and it has multiple pages on the portal for different groups. Running client version 7.1. The VPN client would not start automatically or complete when manually invoked using `ncsvc`.

** Tip**\
The setup method described is considered old (2013). To setup a client SSL VPN connection to a Juniper\'s hardware nowadays, it is suggested to use [OpenConnect](https://wiki.gentoo.org/wiki/OpenConnect "OpenConnect") or [vpnc](https://wiki.gentoo.org/wiki/Vpnc "Vpnc").

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Stepwise]](#Stepwise)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [Prerequisites]](#Prerequisites)
    -   [[1.4] [Concise Connection Steps]](#Concise_Connection_Steps)
        -   [[1.4.1] [Installation Steps]](#Installation_Steps)
    -   [[1.5] [Split tunneling]](#Split_tunneling)
        -   [[1.5.1] [Sample route]](#Sample_route)
-   [[2] [See also]](#See_also)
-   [[3] [References]](#References)

# [Configuration]

## [Stepwise]

Go to the network portal web page and examine page source for REALM:

-   Login through web portal, attmpt to intiate network connect
-   Software downloads and installs into [\~/.juniper_network/network_connect/]
-   Examine the cookies for the site and find DSID. *This will have to be refreshed each time*

Change path to the installation path :

`user `[`$`]`cd ~/.juniper_network/network_connect`

Get the certificate, e.g.:

`user `[`$`]`openssl s_client -connect portal.example.net:443 -showcerts < /dev/null 2> /dev/null | openssl x509 -outform der > cert.der`

Compile the [lbncui.so] into an executable file:

`user `[`$`]`` gcc -m32 -Wl,-rpath,`pwd` -o ncui libncui.so ``

Finally execute `ncui` using following command:

`user `[`$`]`./ncui -h portal.example.net -u USERNAME -p PASSWORD -r REALM -f cert.der -l 5 -L 5 -U `[`https://portal.example.net/dana-na/auth/url_0/welcome.cgi`](https://portal.example.net/dana-na/auth/url_0/welcome.cgi)` -c DSID=COOKIE-VALUE-FOR-DSID`

Where [https://portal.example.net/dana-na/auth/url_0/welcome.cgi](https://portal.example.net/dana-na/auth/url_0/welcome.cgi) is the full path to the login page of the portal.

When the connection has been established be a TUN device will be created. This can be verfied using the [ip link show up] command.

## [Kernel]

First make sure that TUN is enabled in your kernel as this is required to be able to create the tunnel to your vpn. Personally, I build this into the kernel and not as a module.

[KERNEL] **\'make menuconfig\' options**

    Device Drivers --->
      Network device support --->
        <*> Universal TUN/TAP device driver support

## [Prerequisites]

Software requirements: SUN Java JRE (both 64 and 32 bit versions) with nsplugin , e.g.:

-   [[[app-emulation/emul-linux-x86-java]](https://packages.gentoo.org/packages/app-emulation/emul-linux-x86-java)[]]
-   [[[dev-java/sun-jre-bin]](https://packages.gentoo.org/packages/dev-java/sun-jre-bin)[]]
-   [[[dev-libs/openssl]](https://packages.gentoo.org/packages/dev-libs/openssl)[]]

## [Concise Connection Steps]

I\'m writing this section to explain how I connect to Juniper Network Connect in a more succinct and consolidated manner. Recent versions of Google Chrome block the Java plugin, so it requires a different approach. This method does not use Java and is, personally, a better way.

### [Installation Steps]

You will need to download ncLinuxApp.jar for your version of Juniper Network Connect. Replace \"yoursite\" with the address for your vpn website.

*[https://yoursite.net/dana-cached/nc/ncLinuxApp.jar](https://yoursite.net/dana-cached/nc/ncLinuxApp.jar)*

Once you have ncLinuxApp.jar download, create a folder somewhere in your home directory. This is where you will be running the network connect client from.

`user `[`$`]`mkdir ~/juniper_networks`

Now extract the contents of ncLinuxApp.jar

`user `[`$`]`unzip ncLinuxApp.jar`

** Note**\
If you ran this app from the browser, using Firefox or something else, it will have extracted the needed files to the following directory: *\~/.juniper_networks/network_connect/*

Once you have the files extracted, you will need to change the ownership and set file permissions for a couple files. You will need to be root.

Change ownership of ncsv and set to executable

`root `[`#`]`chown root ncsv && chmod +x ncsv`

Set ncdiag to executable as well. Ownership of this file doesn\'t seem to need to be root

`root `[`#`]`chmod +x ncdiag`

As the instructions state in the previous section, you will need to obtain the certificate from your Juniper installation.

`user `[`$`]`openssl s_client -connect yoursite.net:443 -showcerts < /dev/null 2> /dev/null | openssl x509 -outform der > cert.der`

Compile libncui.so for your arch. This creates the executable you will need. This must be done as your user.

`user `[`$`]`` gcc -m32 -Wl,-rpath,`pwd` -o ncui libncui.so ``

`user `[`$`]`chmod +x ncui`

Instructed in the previous section, you will need to obtaini the REALM and DSID from your Juniper installation. The REALM is found in the login form on the front page of your Juniper site and the DSID can be obtained from your cookies after logging into the site.

`root `[`#`]`./ncui -h portal.example.net -u USERNAME -p PASSWORD -r REALM -f cert.der -l 5 -L 5 -U `[`https://portal.example.net/dana-na/auth/url_0/welcome.cgi`](https://portal.example.net/dana-na/auth/url_0/welcome.cgi)` -c DSID=COOKIE-VALUE-FOR-DSID`

** Note**\
I needed to be root to be able to create the tunnel to the VPN. You might be able to change it so that your user has access, but I just use root.

The one annoying thing about this is that you do have to log into your Juniper site to obtain the DSID everytime. At least it does work! I hope this guide helps others in need! :)

## [Split tunneling]

[Workaround for JUNIPER VPN split-tunneling restriction](https://www.digitalinternals.com/124/20090430/workaround-for-juniper-vpn-split-tunneling-restriction/) describes methods to achieve split tunneling.

Using `LD_PRELOAD` to preload a custom library to redirect reads to /proc/net/route to another file seem promising, but proved problematic on a 64-bit client. see [https://gist.github.com/anonymous/6777345](https://gist.github.com/anonymous/6777345)

Patching the ncsvc binary can disable the route monitoring function, allowing one to change routes as needed manually or by script. Without patching, a route monitor may be in place that will disconnect if routes are changed.

There are probably many ways to achieve, but one tested is to convert a conditional jump statement in the route monitoring routine:

1.  make backup copy of ncsvc
2.  open ncsvc in disasembler
3.  search for text \"no routes to monitor\" in the disassembly
4.  a few lines up should be something that looks like

<!-- -->

    .text:0805CC9F                 mov     [ebp+var_19], 0
    .text:0805CCA3                 cmp     dword ptr [eax+60h], 0
    .text:0805CCA7                 jnz     loc_805CE1A
    .text:0805CCAD                 sub     esp, 8
    .text:0805CCB0                 push    offset aNoRoutesToMoni ; "no routes to monitor"

1.  the jnz (or possibly jne) signals the program to jump if the previous step is not zero (or equal). Change this to invert the conditional, ie jump if zero (or equal).
2.  To do so, look at the hexdump for this bit of code. Depending on your debugger, you may be able to change it within the program, or else open up the ncsvc binary in a hexeditor and find the corresponding bits.
3.  The bits will likely be either start with 75 ?? ?? or 0F 85 ?? ??
4.  change the 75 to 74, or 85 to 84.
5.  save and test.

### [Sample route]

In order to achieve desirerd access to VPN resources, local LAN resources, and internet resources, possible post-connect commands:

Consider ncsvc gave original default gw has a higher metric, added a second default with a lower metirc, and target vpn resources are on 10.0.0.0 and 170.0.0.0, and a tun0 ip of 10.15.15.15 (besides principal resources, check the vpn network\'s dns servers etc)

`root `[`#`]`route del default `

`root `[`#`]`route del default `

`root `[`#`]`route add default gw 192.168.1.1 metric 2 `

`root `[`#`]`route del 192.168.1.0 dev eth0 `

`root `[`#`]`route del -net 192.168.1.0 netmask 255.255.255.0 dev eth0 `

`root `[`#`]`route del -net 192.168.1.0 gw 10.15.15.15 netmask 255.255.255.0 `

`root `[`#`]`route add -net 192.168.1.0 netmask 255.255.255.0 dev eth0 `

`root `[`#`]`route add -net 170.0.0.0 netmask 255.0.0.0 gw 10.15.15.15 dev tun0 `

`root `[`#`]`route add -net 10.0.0.0 netmask 255.0.0.0 gw 10.15.15.15 dev tun0 `

`root `[`#`]`echo "nameserver 192.168.1.1" >> /etc/resolv.conf `

# [See also]

-   [OpenConnect](https://wiki.gentoo.org/wiki/OpenConnect "OpenConnect")
-   [vpnc](https://wiki.gentoo.org/wiki/Vpnc "Vpnc")

# [References]

-   [https://forums.gentoo.org/viewtopic-t-494883.html](https://forums.gentoo.org/viewtopic-t-494883.html)
-   [https://ubuntuforums.org/showthread.php?t=232607&page=45&p=11189826#post11189826](https://ubuntuforums.org/showthread.php?t=232607&page=45&p=11189826#post11189826)
-   [https://wiki.archlinux.org/index.php/Juniper_VPN](https://wiki.archlinux.org/index.php/Juniper_VPN)
-   [https://techydodo.wordpress.com/2012/01/17/cracking-the-juniper-network-connect-problem-on-linux-64-bit/](https://techydodo.wordpress.com/2012/01/17/cracking-the-juniper-network-connect-problem-on-linux-64-bit/)
-   [https://www.scc.kit.edu/scc/net/juniper-vpn/linux/](https://www.scc.kit.edu/scc/net/juniper-vpn/linux/)
-   [https://mad-scientist.net/juniper.html](https://mad-scientist.net/juniper.html)