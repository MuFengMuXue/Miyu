**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Point-to-point_protocol "wikipedia:Point-to-point protocol")

**PPP** (**P**oint-to-**P**oint **P**rotocol) is commonly used in establishing a direct connection between two networking nodes. It can provide connection authentication, transmission encryption, and compression.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Example setup with systemd and automatic connection]](#Example_setup_with_systemd_and_automatic_connection)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags for] [net-dialup/ppp](https://packages.gentoo.org/packages/net-dialup/ppp) [[]] [Point-to-Point Protocol (PPP)]

  --------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  [`activefilter`](https://packages.gentoo.org/useflags/activefilter)   Enables active filter support
  [`atm`](https://packages.gentoo.org/useflags/atm)                     Enable Asynchronous Transfer Mode protocol support
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                     Installs GTK+ password prompting program that can be used by passprompt.so PPP plugin for reading the password from a X11 input terminal
  [`pam`](https://packages.gentoo.org/useflags/pam)                     Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`selinux`](https://packages.gentoo.org/useflags/selinux)             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)             Enable use of systemd-specific libraries and features like socket activation or session tracking
  --------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 13:27] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Portage has a USE flag `ppp` for enabling support for PPP for other packages.

** Note**\
Enabling `ppp` USE flag will pull in [[[net-dialup/ppp]](https://packages.gentoo.org/packages/net-dialup/ppp)[]] automatically

[FILE] **`/etc/portage/make.conf`**

    USE="... ppp ..."

After setting global USE flags update your system to the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Or emerge [[[net-dialup/ppp]](https://packages.gentoo.org/packages/net-dialup/ppp)[]] package manually:

`root `[`#`]`emerge --ask net-dialup/ppp`

### [Kernel]

Following kernel options need to be enabled, to support **PPPoE**, which is used in most cases.

** Note**\
Using PPP compression is not suggested.

[KERNEL]

    Device Drivers  --->
        [*] Network device support  --->
          <*>   PPP (point-to-point protocol) support
          < >     PPP BSD-Compress compression (NEW)
          < >     PPP Deflate compression (NEW)
          [ ]     PPP filtering (NEW)
          < >     PPP MPPE compression (encryption) (EXPERIMENTAL) (NEW)
          [ ]     PPP multilink support (EXPERIMENTAL) (NEW)
          <*>     PPP over Ethernet (EXPERIMENTAL)
          < >     PPP support for async serial ports (NEW)
          < >     PPP support for sync tty ports (NEW)

  ----------------------------------- -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Option                              Driver         Description
  PPP BSD-Compress compression        ppp_bsdcomp    (Not recommended) Support for data compression. \"PPP Deflate compression\" is preferable.
  PPP filtering                       \-             Support for packet filtering.
  PPP MPPE compression (encryption)   ppp_mppe       Driver for [Microsoft Point-to-Point Encryption](https://en.wikipedia.org/wiki/Microsoft_Point-to-Point_Encryption "wikipedia:Microsoft Point-to-Point Encryption").
  PPP multilink support               \-             Support for PPP multilink to combine serveral lines.
  PPP over Ethernet                   pppoe          Driver for [PPPoE](https://wiki.gentoo.org/wiki/PPPoE "PPPoE").
  PPP support for sync tty ports      ppp_sync_tty   Support for synchronous devices.
  ----------------------------------- -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Optional PPP options

Finally you need to rebuild linux, install and boot new kernel with PPP support.

## [Configuration]

Provided eth0 following lines should be added for PPPoE connection:

[FILE] **`/etc/conf.d/net`Add:**

    ...
    config_ppp0="ppp"
    link_ppp0="eth0" (Specify your ethernet interface)
    plugins_ppp0="pppoe"
    username_ppp0='user'
    password_ppp0='password'
    pppd_ppp0="
    noauth
    defaultroute
    usepeerdns
    mtu 9120 (Get the correct MTU (Jumbo frame) value from your eth0 Gigabit Ethernet card interface)
    holdoff 3
    child-timeout 60
    lcp-echo-interval 15
    lcp-echo-failure 3
    noaccomp noccp nobsdcomp nodeflate nopcomp novj novjccomp"
    ...
    rc_net_ppp0_need="net.eth0"

Create an init script for the PPP device by symlinking to net.lo:

`root `[`#`]`ln -s /etc/init.d/net.lo /etc/init.d/net.ppp0`

`root `[`#`]`/etc/init.d/net.ppp0 start`

## [Example setup with systemd and automatic connection]

First, create the configuration file:

[FILE] **`/etc/ppp/peers/provider`**

    plugin pppoe.so
    # network interface
    enp41s0
    # login name
    name "you_login_to_ISP"
    usepeerdns
    persist
    # Uncomment this to enable dial on demand
    #demand
    #idle 180
    defaultroute
    defaultroute-metric 1023
    hide-password
    noauth
    #linkname eth0
    ifname eth0

enp41s0 is the network interface card to use. It can be found with [ip link] command.

** Note**\
When using ppp of version less than 2.4.9, the first line should be (rp- prefix):

    plugin rp-pppoe.so

Next, create the password secrets file:

[FILE] **`/etc/ppp/chap-secrets`**

    # Secrets for authentication using CHAP
    # client        server  secret                  IP addresses
    your_login_to_ISP   *       your_secret_password

For this to work at system startup, add the following unit in [/etc/systemd/system/pppoe.service]:

[FILE] **`/etc/systemd/system/pppoe.service`**

    [Unit]
    Description=PPPoE connection
    BindsTo=sys-subsystem-net-devices-enp41s0.device
    After=sys-subsystem-net-devices-enp41s0.device

    [Service]
    Type=forking
    PIDFile=/var/run/eth0.pid
    #RemainAfterExit=true
    ExecStart=/usr/sbin/pon
    ExecStop=/usr/sbin/poff provider

    [Install]
    WantedBy=multi-user.target

\
sys-subsystem-net-devices-enp41s0.device is the network device via which pppoe will connect on. To find out the exact name you can use the following bash command

`root `[`#`]`systemctl list-units | grep device | grep net`

Optionally, create a service unit to handle wake up after sleep:

[FILE] **`/etc/systemd/system/pppoe-after-wakeup.service`**

    [Install]
    WantedBy=sleep.target

    [Unit]
    After=systemd-suspend.service systemd-hybrid-sleep.service systemd-hibernate.service

    [Service]
    Type=simple
    ExecStart=/bin/systemctl restart pppoe

\
Finally, test it with:

`root `[`#`]`systemctl start pppoe `

`root `[`#`]`systemctl start pppoe-after-wakeup `

If it works as expected, enable them on a permanent basis:

`root `[`#`]`systemctl enable pppoe `

`root `[`#`]`systemctl enable pppoe-after-wakeup `

## [See also]

-   [Gentoo handbook PPPoE configuration](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Modular#ADSL_with_PPPoE.2FPPPoA "Handbook:AMD64/Networking/Modular")